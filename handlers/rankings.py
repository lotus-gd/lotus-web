import aiohttp
import utils

async def rankings(r: aiohttp.web.RequestHandler):
    return utils.render_template("rankings.html")