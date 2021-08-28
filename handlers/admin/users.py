import aiohttp
import utils # type: ignore
from aiohttp_session import get_session
from common.helpers import userhelper, privilegehelper # type: ignore

async def users(r: aiohttp.web.RequestHandler):
    if not await privilegehelper.logged_in(r) or not await privilegehelper.is_admin(r): 
        return aiohttp.web.HTTPForbidden()
    return await utils.render_template(r, "admin/users.html", users=await userhelper.get_all_users(15))