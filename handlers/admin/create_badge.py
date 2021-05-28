import aiohttp
import utils # type: ignore
from aiohttp_session import get_session
from common.helpers import userhelper # type: ignore

async def create_badge(r: aiohttp.web.RequestHandler):
    session = await get_session(r)
    try:
        if not session["user_id"]: return aiohttp.web.HTTPForbidden()
    except KeyError:
        return aiohttp.web.HTTPForbidden()
    #user = await userhelper.get_user(session["user_id"])
    #if not user.privilege_group.has_privilege(Privileges.DEVELOPER): return aiohttp.web.HTTPForbidden() # check if admin here
    return await utils.render_template(r, "admin/create_badge.html")