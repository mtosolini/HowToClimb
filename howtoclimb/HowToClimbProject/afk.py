import bigstuffapicall as api
import matchFct
from collections import Counter

def countAfkInGame(_match, summonerName):
    listPositions = matchFct.extractPositions(_match)
    mainPlayerId = matchFct.getPlayersIdByName(_match, summonerName)
    mainPlayerTeam = matchFct.getPlayersTeamByParticipantId(_match, mainPlayerId)
    afkStats = {
        'GameInfos' : {'matchId' : _match.get('matchId'), 'afk' : False, 'win' : matchFct.hasWonSummonerId(_match, mainPlayerId)},
        'whoAfk' : {
            'opponent' : {'short': 0, 'medium': 0, 'long': 0}, 
            'allied' : {'short': 0, 'medium': 0, 'long': 0}, 
            'self' : {'short': 0, 'medium': 0, 'long': 0} 
            }}        
    for player, positions in listPositions.items():
        timeAfk = countTimeAfk(positions)
        if timeAfk >= 2:
            afkStats['GameInfos']['afk']= True
            if timeAfk >= 2 and timeAfk < 5:
                keyTime = 'short'
            if timeAfk >= 5 and timeAfk < 15:
                keyTime = 'medium'
            if timeAfk >=20:
                keyTime = 'long'
            if str(mainPlayerTeam) == str(matchFct.getPlayersTeamByParticipantId(_match, player)):
                if str(player)==str(mainPlayerId):
                    afkStats['whoAfk']['self'][keyTime]+=1
                else:
                    afkStats['whoAfk']['allied'][keyTime]+=1
            else:
                afkStats['whoAfk']['opponent'][keyTime]+=1
    return afkStats

def GetAllAfk(summoner, n, _apiCst):
    listMatches = api.getLastMatches(summoner, n, _apiCst, "true", ['RANKED_SOLO_5x5', 'TEAM_BUILDER_DRAFT_RANKED_5x5'])
    totalAfk = { 
        'self' : { 'short' : 0, 'medium' : 0, 'long' : 0 },
        'opponent': { 'short' : 0, 'medium' : 0, 'long' : 0 },
        'allied': { 'short' : 0, 'medium' : 0, 'long' : 0 }}
    print('Matchs trouvés : '+str(len(listMatches)))
    for match in listMatches:
        afkResult = countAfkInGame(match, summoner)
        if afkResult.get('GameInfos').get('afk'):
            print(afkResult) 
            totalAfk['opponent'] = dict(Counter(totalAfk.get('opponent')) + Counter(afkResult.get('whoAfk').get('opponent')))
            totalAfk['allied'] = dict(Counter(totalAfk.get('allied')) + Counter(afkResult.get('whoAfk').get('allied')))
            totalAfk['self'] = dict(Counter(totalAfk.get('self')) + Counter(afkResult.get('whoAfk').get('self')))
    print('Total des Afk :')
    print(totalAfk)
        
def countTimeAfk(positions):
    x = -1
    y = -1
    timeAfk = 0
    for position in positions:
        if position != None:
            if position.get('x')== x and position.get('y')==y:
                timeAfk+=1
            x = position.get('x')
            y = position.get('y')
    return timeAfk



