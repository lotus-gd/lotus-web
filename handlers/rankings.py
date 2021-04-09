import aiohttp
import utils
import operator
from common import Account, leaderboardhelper, userhelper

async def rankings(r: aiohttp.web.RequestHandler):
    #await leaderboardhelper.refresh_leaderboards() # broken rn
    scores = list(await leaderboardhelper.get_top_100())
    scores.sort(key=operator.attrgetter(scores[0]))
    rankings = []
    # we need to get the username and the pp (its just the id rn)
    for score in scores:
        print(score[1])
        user = await userhelper.get_user(score[1])
        rankings.append(Account(username=user.username, pp=user.pp))
    return utils.render_template("rankings.html", leaderboard_scores=rankings)