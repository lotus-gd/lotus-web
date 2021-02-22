import aiohttp
from web import templates

def render_template(template, *args, **kwargs) -> aiohttp.web.Response:
    if not template.endswith(".html"):
        template += ".html"  # make sure we have .html always at the end or else the server will break.

    text = templates.get_template(template).render(*args, **kwargs)
    return aiohttp.web.Response(text=text, content_type="text/html")

def text(**kwargs) -> aiohttp.web.Response:
    return aiohttp.web.Response(**kwargs, content_type="text/html")