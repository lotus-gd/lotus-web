import aiohttp
import utils
import operator
from common import Account
from common import leaderboard

async def rankings(r: aiohttp.web.RequestHandler):
    #await leaderboard.refresh_leaderboards() # broken rn
    scores = list(await leaderboard.get_top_100())
    scores.sort()
    rankings = []
    # we need to get the username and the pp (its just the id rn)
    for score in scores:
        rankings.append(Account(username="not available", pp="not available"))
    return utils.render_template("rankings.html", leaderboard_scores=rankings)