import aiohttp
import utils
import operator
from common import Account, leaderboardhelper, userhelper

async def rankings(r: aiohttp.web.RequestHandler):
    #await leaderboardhelper.refresh_leaderboards() # broken rn
    scores = list(await leaderboardhelper.get_top_100())
    scores.sort()
    rankings = []
    # we need to get the username and the pp (its just the id rn)
    for score in scores:
        print(score[0])
        user = userhelper.get_user(score[0])
        rankings.append(Account(username=user.username, pp=user.pp))
    return utils.render_template("rankings.html", leaderboard_scores=rankings)