import aiohttp
import utils # type: ignore
from aiohttp_session import get_session
from common.helpers import userhelper # type: ignore

async def badges(r: aiohttp.web.RequestHandler):
    session = await get_session(r)
    try:
        if not session["user_id"]: return aiohttp.web.HTTPForbidden()
    except KeyError:
        return aiohttp.web.HTTPForbidden()
    user = await userhelper.get_user(session["user_id"])
    if not "7" in str(user.privileges): return aiohttp.web.HTTPForbidden() # teach me how do do privileges relesto
    return await utils.render_template(r, "admin/badges.html", badges=await userhelper.get_badges())