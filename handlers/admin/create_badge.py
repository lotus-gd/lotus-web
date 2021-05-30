import aiohttp
import utils # type: ignore
from common.helpers import privilegehelper # type: ignore

async def create_badge(r: aiohttp.web.RequestHandler):
    if not await privilegehelper.logged_in(r) or not await privilegehelper.is_admin(r): 
        return aiohttp.web.HTTPForbidden()
    return await utils.render_template(r, "admin/create_badge.html")