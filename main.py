import aiohttp
import jinja2
import aiohttp_jinja2

port = 80

app = aiohttp.web.Application()
templates = aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("assets/html"))
routes = aiohttp.web.RouteTableDef()

def html_resp(**kwargs) -> aiohttp.web.Response:
    kwargs.setdefault("content_type", "text/html")
    return aiohttp.web.Response(**kwargs)

def text_resp(text=None, *args, **kwargs):
    return aiohttp.web.Response(text=text, *args, **kwargs)

app.router.add_static("/assets/", path="./assets/", name="assets")

def main():
    aiohttp.web.run_app(app, port=port)
    
if __name__ == "__main__":
    main()