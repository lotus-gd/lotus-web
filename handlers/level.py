import aiohttp
import utils

async def level(r: aiohttp.web.RequestHandler):
    return utils.render_template("level.html")