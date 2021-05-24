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

port = 80

os.chdir(os.path.dirname(os.path.realpath(__file__)))

app = aiohttp.web.Application(loop= globals.loop)
templates = aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("assets/html"))

app.router.add_static("/assets/", path="./assets/", name="assets")

async def async_main() -> None:
    """Configures all of the async elements of the server."""

    await globals.startup_init()

def main():
    #fernet_key = fernet.Fernet.generate_key()
    fernet_key = b"jWksJ7QjlsrE3IRcssxcdoYApAK6qGwYOlAbMzvpQ6g="
    secret_key = base64.urlsafe_b64decode(fernet_key)
    setup(app, EncryptedCookieStorage(secret_key))
    router.add_all_routes(app)
    aiohttp.web.run_app(app, port=port)
    
if __name__ == "__main__":
    main()