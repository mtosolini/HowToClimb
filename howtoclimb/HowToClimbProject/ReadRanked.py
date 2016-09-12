import json

# Recuperation du fichier

def up_files(filename):
	with open(filename) as file_object:
		contents = json.load(file_object)
		test = Match_ranked(contents)
		print(test.teams[1].bans[1].keys())
		

# CLASSE : MATCH RANKED
class Match_ranked():
	""" modelize a ranked json """
	def __init__(self, _ranked):
		""" Attributes """
		self.matchVersion = _ranked['matchVersion'] 

		self.mapId = _ranked['mapId'] 
		self.region = _ranked['region'] 
		self.matchType = _ranked['matchType'] 
		self.matchId = _ranked['matchId'] 
		self.matchCreation = _ranked['matchCreation'] 
		self.matchMode = _ranked['matchMode']
		self.platformId = _ranked['platformId']
		self.season = _ranked['season']
		self.matchDuration = _ranked['matchDuration']
		self.queueType = _ranked['queueType']
		
		""" List of the teams """
		self.teams = []
		for team in _ranked['teams']:
			self.teams.append(MR_team(team))
			
		self.participants = _ranked['participants'] # n lignes
		self.participantIdentities = _ranked['participantIdentities'] # n lignes

		self.timeline = _ranked['timeline'] # n lignes

		
# CLASSE : Participants
class MR_participants():
	""" modelize the participants of a ranked json """
	def __init__(self, _participants):
		""" Attributes """	
		
# CLASSE : Team
class MR_team():
	""" modelize the teams of a ranked json """
	def __init__(self, _team):
		self.dominionVictoryScore= _team['dominionVictoryScore']
		self.winner = _team['winner']
		self.teamId = _team['teamId']
		self.baronKills = _team['baronKills']
		self.firstDragon = _team['firstDragon']
		self. riftHeraldKills = _team['riftHeraldKills']
		self.firstBaron = _team['firstBaron']
		self.bans = _team['bans'] 
		self.firstTower = _team['firstTower']
		self.firstRiftHerald = _team['firstRiftHerald']
		self.vilemawKills = _team['vilemawKills']
		self.dragonKills = _team['dragonKills']
		self.firstInhibitor = _team['firstInhibitor']
		self.inhibitorKills = _team['inhibitorKills']
		self.firstBlood = _team['firstBlood']
		self.towerKills = _team['towerKills']
		
# CLASSE : Bans
class MR_bans():
	""" modelize the bans of a ranked json """
	def __init__(self, _ban):
		self.championId = _ban['championId']
		self.pickTurn = _ban['pickTurn']
		
# ENDCLASSE

		

	

