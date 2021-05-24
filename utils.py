import aiohttp
from web import templates
from aiohttp_session import get_session

async def render_template(r, template, *args, **kwargs) -> aiohttp.web.Response:
    
    # This is not needed as we can just add .html to all
    #if not template.endswith(".html"):
    #    template += ".html"  # make sure we have .html always at the end or else the server will break.

    text = templates.get_template(template).render(*args, **kwargs, session=await get_session(r))
    return aiohttp.web.Response(text=text, content_type="text/html")

def text(**kwargs) -> aiohttp.web.Response:
    return aiohttp.web.Response(**kwargs, content_type="text/html")