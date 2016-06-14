class NotesApplication(object):
	'''note taking application class definition'''

	def __init__(self, author):
		'''constructor for the Notes Application. 
		Takes a string, the author, and initialises a list to
		store all the different notes''' 
		self.author = author

		self.notes = []


	
