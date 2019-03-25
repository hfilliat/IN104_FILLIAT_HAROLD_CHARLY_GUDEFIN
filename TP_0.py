##tp 0 de in104
## type de sport = direct ou indirect

class Sport:
	def __init__(self, name, date_of_creation, nb_players_worldwide):
		self.age = age
		self.date_of_creation = date_of_creation
		self.nb_players_worldwide = nb_players_worldwide
	

	def nbPlayers(self):
		return self.nb_players

class individual(Sport):
	def __str__(self):
		return "This is an individual sport"
	def players(self):
		print("We need a team of "+str(nb_players)+" to play")
		 

class collective(Sport):
	def __str__(self):
		return "This is an collective sport"
	def players(self):
		print("We need a team of "+str(nb_players)+" to play")
