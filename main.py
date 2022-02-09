import aiohttp
import jinja2
import aiohttp_jinja2
import base64
from cryptography import fernet
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage
import router
import os
from common import globals

port = 6942

os.chdir(os.path.dirname(os.path.realpath(__file__)))

app = aiohttp.web.Application(middlewares=[router.error_middleware])
templates = aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("assets/html"))

app.router.add_static("/assets/", path="./assets/", name="assets")

async def async_main() -> None:
    """Configures all of the async elements of the server."""

    await globals.startup_init()

def main():
    # key to store cookies
    fernet_key = open("fernet_key", "rb").read()
    secret_key = base64.urlsafe_b64decode(fernet_key)
    setup(app, EncryptedCookieStorage(secret_key))
    router.add_all_routes(app)
    globals.loop.run_until_complete(async_main())
    aiohttp.web.run_app(app, port=port)
    
if __name__ == "__main__":
    main()
