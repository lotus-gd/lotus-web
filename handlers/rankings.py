import aiohttp
import utils
from common import Account, leaderboardhelper, userhelper

async def rankings(r: aiohttp.web.RequestHandler):
    scores = await leaderboardhelper.get_top_100()
    rankings = []
    # we need to get the username and the pp (its just the id rn)
    for score in scores:
        rankings.append(Account(username=score[0], pp=score[1]))
    return await utils.render_template(r, "rankings.html", leaderboard_scores=rankings)