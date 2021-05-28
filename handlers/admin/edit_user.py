import aiohttp
import utils # type: ignore
from aiohttp_session import get_session
from common.helpers import userhelper # type: ignore
from common.objects.account import Account

async def edit_user(r: aiohttp.web.RequestHandler):
    session = await get_session(r)
    try:
        if not session["user_id"]: return aiohttp.web.HTTPForbidden()
    except KeyError:
        return aiohttp.web.HTTPForbidden()
    user = await userhelper.get_user(session["user_id"])
    if not "7" in str(user.privileges): return aiohttp.web.HTTPForbidden() # teach me how do do privileges relesto
    
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
    return utils.text("a")