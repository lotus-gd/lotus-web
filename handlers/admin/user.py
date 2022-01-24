import aiohttp
import utils # type: ignore
from common.helpers import userhelper, privilegehelper # type: ignore

async def user(r: aiohttp.web.RequestHandler):
    if not await privilegehelper.logged_in(r) or not await privilegehelper.is_admin(r): 
        return aiohttp.web.HTTPForbidden()
    id = r.match_info["id"]
    return await utils.render_template(r, "admin/user.html", viewed_user=await userhelper.get_user(id))

async def user_post(r: aiohttp.web.RequestHandler):
    if not await privilegehelper.logged_in(r) or not await privilegehelper.is_admin(r): 
        return aiohttp.web.HTTPForbidden()
    data = await r.post()
    id = data["id"]
    try:
        id = int(id)
    except ValueError:
        user = await userhelper.get_user_by_name(id)
    else:
        user = await userhelper.get_user(id)
    return await utils.render_template(r, "admin/user.html", viewed_user=user)