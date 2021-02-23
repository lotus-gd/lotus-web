import aiohttp
import utils

async def level(r: aiohttp.web.RequestHandler):
    levelname = r.match_info["levelname"]
    return utils.render_template("level.html", {"levelname": levelname})