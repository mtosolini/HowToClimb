import matchFct as m
import bigstuffapicall as api
import geometry as g
# positions des deux junglers / leur team / TIMEFRAME / liste des positions par frame / isInCircle
# team 100 : start 0/0 : team 200 : start 14000/14000

def getTheJunglersPositions(match, junglers):
    listPositions = m.extractPositions(match)
    listPositionJunglers = []
    for jungler in junglers:
        for id in listPositions.keys():
            if str(id) == str(jungler.get('id')):
                listPositionJunglers.append({'id':jungler.get('id'), 'team': jungler.get('team'), 'positions':listPositions.get(id)})
    return listPositionJunglers


# Si team bleue/rouge - si start red/bleu - 4 cas possibles.
def getJunglerStart(junglerPosition):
    try:
        position = junglerPosition.get('positions')[2]
        RedSideNormalStart = g.isOnRedSide(15000, position.get('x'), position.get('y')) and junglerPosition.get('team')==200 
        BlueSideNormalStart = g.isOnRedSide(15000, position.get('x'), position.get('y')) and junglerPosition.get('team')==100
        if RedSideNormalStart or BlueSideNormalStart:
            position['invade'] = False
        else:
            position['invade'] = True
        position['BotStart'] = g.isOnBotSide(position.get('x'), position.get('y'))
    except:
        print('getJunglerStartBug')
    return position

def getTheJungleRoot(match, junglerName):
    jungler = m.extractPositionsByPlayerId(match, m.getPlayersIdByName(match, junglerName))
    jungleRoot = []
    for pos in jungler.values():
        jungleRoot.append(
            )
        
            


        
        


