import aiohttp
import utils # type: ignore
from common.helpers import userhelper, privilegehelper, levelhelper # type: ignore

async def index(r: aiohttp.web.RequestHandler):
    if not await privilegehelper.logged_in(r) or not await privilegehelper.is_admin(r): 
        return aiohttp.web.HTTPForbidden()
    
    return await utils.render_template(r, "admin.html",
                                       totalusers=await userhelper.get_total_users(),
                                       users=await userhelper.get_all_users(6),
                                       totallevels=await levelhelper.get_total_levels())