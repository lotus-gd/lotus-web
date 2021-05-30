import aiohttp
import utils # type: ignore
from common.helpers import userhelper, privilegehelper # type: ignore

async def user(r: aiohttp.web.RequestHandler):
    if not await privilegehelper.logged_in(r) or not await privilegehelper.is_admin(r): 
        return aiohttp.web.HTTPForbidden()
    id = r.match_info["id"]
    return await utils.render_template(r, "admin/user.html", viewed_user=await userhelper.get_user(id))