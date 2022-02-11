import aiohttp
import utils
from common import userhelper # type: ignore

async def user(r: aiohttp.web.RequestHandler):
    user_id = r.match_info["id"]
    user = await userhelper.get_user(user_id)
    
    return await utils.render_template(r, "user.html", {"user": user})