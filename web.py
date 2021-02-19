import aiohttp
import jinja2
import aiohttp_jinja2
import router
import os

port = 80

os.chdir(os.path.dirname(os.path.realpath(__file__)))

app = aiohttp.web.Application()
templates = aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("assets/html"))

app.router.add_static("/assets/", path="./assets/", name="assets")

def main():
    router.add_all_routes(app)
    aiohttp.web.run_app(app, port=port)
    
if __name__ == "__main__":
    main()