import aiohttp
import utils
from common.objects import Account

async def rankings(r: aiohttp.web.RequestHandler):
    scores = [Account(username="spookybear0", pp=10000), Account(username="RealistikDash", pp=1000), Account(username="Laica", pp=100)]
    return utils.render_template("rankings.html", leaderboard_scores=scores)