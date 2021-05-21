import aiohttp
import utils

async def user(r: aiohttp.web.RequestHandler):
    username = r.match_info["username"]
    return await utils.render_template(r, "user.html", {"username": username})