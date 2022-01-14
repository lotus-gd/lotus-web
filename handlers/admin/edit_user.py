import aiohttp
import utils # type: ignore
from common.objects.account import Account # type: ignore
from common.helpers import privilegehelper # type: ignore

async def edit_user(r: aiohttp.web.RequestHandler):
    if not await privilegehelper.logged_in(r) or not await privilegehelper.is_admin(r): 
        return aiohttp.web.HTTPForbidden()
    
    acc = await Account.from_sql(r.rel_url.query["id"])
    
    paramlist = ["name", "id", "email", "country", "privileges", "pp", "stars", "coins", "u_coins", "demons"]
    mydict = {}
    for i in paramlist:
        try:
            if i == "pp": mydict[i] = float(r.rel_url.query[i].rstrip("pp"))
            else: mydict[i] = int(r.rel_url.query[i])
        except:
            mydict[i] = r.rel_url.query[i]
        
        if i in ["pp", "stars", "coins", "u_coins", "demons"]:
            setattr(acc.stats, i, mydict[i])
        else:
            setattr(acc, i, mydict[i])
        
    await acc.stats.save()
    await acc.save()
    return aiohttp.web.HTTPOk()