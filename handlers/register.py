import aiohttp
import utils # type: ignore
from aiohttp_session import get_session

async def register(r: aiohttp.web.RequestHandler):
    return await utils.render_template(r, "register.html")