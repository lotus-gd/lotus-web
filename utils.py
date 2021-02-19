import aiohttp
from web import templates

def render_template(template, **kwargs) -> aiohttp.web.Response:
    text = templates.get_template(template).render(**kwargs)
    return aiohttp.web.Response(text=text, content_type="text/html")

def text(**kwargs) -> aiohttp.web.Response:
    return aiohttp.web.Response(**kwargs, content_type="text/html")