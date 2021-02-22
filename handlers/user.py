import aiohttp
import utils

async def user(r: aiohttp.web.RequestHandler):
    username = r.match_info["username"]
    return utils.render_template("user.html", {"username": username})