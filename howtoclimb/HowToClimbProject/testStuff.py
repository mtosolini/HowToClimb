import var
import counterJungle as cj
import afk
import matchFct as m
import bigstuffapicall as api
import geometry as g

cst = var.ApiCst()
listMatch = api.getLastMatches('starcraft243ver', 1, cst, True, ['RANKED_SOLO_5x5', 'TEAM_BUILDER_DRAFT_RANKED_5x5'], ['JUNGLE'])

test = cj.getTheJungleRoot(listMatch[0], '0chris1233')
print(test)
#print(m.extractPositions(listMatch[0]))