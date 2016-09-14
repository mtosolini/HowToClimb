import matchFct as m
import bigstuffapicall as api
import geometry as g
# positions des deux junglers / leur team / TIMEFRAME / liste des positions par frame / isInCircle
# team 100 : start 0/0 : team 200 : start 14000/14000


# Not used anymore.
def getTheJunglersPositions(match, junglers):
    listPositions = m.extractPositions(match)
    listPositionJunglers = []
    for jungler in junglers:
        for id in listPositions.keys():
            if str(id) == str(jungler.get('id')):
                listPositionJunglers.append({'id':jungler.get('id'), 'team': jungler.get('team'), 'positions':listPositions.get(id)})
    return listPositionJunglers


# in : dic {positions:[]}
# out : dic {positions:[], invade:bool, botstart:bool}
def getJunglerStart(junglerPosition):
    junglerPositionOut = junglerPosition
    position = junglerPosition.get('positions')[2]
    RedSideNormalStart = g.isOnRedSide(15000, position.get('x'), position.get('y')) and junglerPosition.get('team')==200 
    BlueSideNormalStart = g.isOnRedSide(15000, position.get('x'), position.get('y')) and junglerPosition.get('team')==100
    if RedSideNormalStart or BlueSideNormalStart:
        junglerPositionOut['invade'] = False
    else:
        junglerPositionOut['invade'] = True
    junglerPositionOut['botstart'] = g.isOnBotSide(position.get('x'), position.get('y'))
    return junglerPositionOut


# in : match, summonerName
# out : dic : {id:, team:, invade:, botstart:, positions:[]}
def getTheJungleRoot(match, junglerName):
    playerId = m.getPlayersIdByName(match, junglerName)
    jungler = m.extractPositionsByPlayerId(match, playerId)
    jungleRoot = {'id':playerId, 'team': m.getPlayersTeamByParticipantId(match, playerId), 'positions':jungler.get(str(playerId))}
    jungleRoot = getJunglerStart(jungleRoot)
    return jungleRoot
                  


        
        


