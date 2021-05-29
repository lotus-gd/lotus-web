import aiohttp
import utils # type: ignore

async def index(r: aiohttp.web.RequestHandler):
    return await utils.render_template(r, "index.html")
