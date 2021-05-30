import aiohttp
import utils # type: ignore
from common.helpers import userhelper, privilegehelper # type: ignore

async def badges(r: aiohttp.web.RequestHandler):
    if not await privilegehelper.logged_in(r) or not await privilegehelper.is_admin(r): 
        return aiohttp.web.HTTPForbidden()
    return await utils.render_template(r, "admin/badges.html", badges=await userhelper.get_badges())