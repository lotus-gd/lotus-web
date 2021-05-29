import aiohttp
import utils

async def level(r: aiohttp.web.RequestHandler):
    levelname = r.match_info["levelname"]
    return await utils.render_template(r, "level.html", {"levelname": levelname})