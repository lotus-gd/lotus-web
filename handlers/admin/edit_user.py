import aiohttp
import utils # type: ignore
from common.objects.account import Account # type: ignore
from common.helpers import privilegehelper # type: ignore

async def edit_user(r: aiohttp.web.RequestHandler):
    if not await privilegehelper.logged_in(r) or not await privilegehelper.is_admin(r): 
        return aiohttp.web.HTTPForbidden()
    
    user = await Account.from_sql(r.rel_url.query["id"])
    
    paramlist = ["name", "email", "country", "privileges"]
    for param in paramlist:
        setattr(user, param, param)
    
    # save user but don't save stats since its not being updated
    await user.save()
    return aiohttp.web.HTTPOk()