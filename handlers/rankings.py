import aiohttp
import utils
from common.objects import Account
import operator

async def rankings(r: aiohttp.web.RequestHandler):
    scores = [Account(username="spookybear0", pp=1), Account(username="RealistikDash", pp=1000), Account(username="Laica", pp=100)]
    
    scores.sort(key=operator.attrgetter("pp"))
    scores.reverse()
    
    return utils.render_template("rankings.html", leaderboard_scores=scores)