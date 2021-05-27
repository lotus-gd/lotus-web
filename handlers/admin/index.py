import aiohttp
import utils

async def index(r: aiohttp.web.RequestHandler):
    return await utils.render_template(r, "admin.html")