from evennia import DefaultObject

class nogetbook(DefaultObject):
	def at_object_creation(self):
		self.tags.add("readable", category="isreadable")
		self.tags.add("single", category="isreadable")
		self.db.story = "Book Contents"
		self.locks.add("get:false()")
		self.db.desc = "It's a book, you might want to try and Read it."
		self.db.get_err_msg = "|rLeave the book alone or we will sic the librarians on you.|n"

class terrapinups(DefaultObject):
	name = "TerraPin-Ups"
	def at_object_creation(self):
		self.tags.add("readable", category="isreadable")
		self.tags.add("single", category="isreadable")
		self.db.story = "You flip through the pages.|/The articles are very informative."
		self.locks.add("drop:false()")
		self.db.desc = "TerraPin-Ups Volume 87."

class riotsheet(DefaultObject):
	name = "Riot Sheet"
	def at_object_creation(self):
		self.tags.add("readable", category="isreadable")
		self.tags.add("single", category="isreadable")
		self.db.story = "Signed: "
		self.db.count = 0
		self.locks.add("drop:false()")
		self.db.desc = "Peasant Revolt Sheet Signup."

class ladronenote(DefaultObject):
	name = "Note from Ladrone"
	def at_object_creation(self):
		self.tags.add("readable", category="isreadable")
		self.tags.add("single", category="isreadable")
		self.db.story = "You've been had. I've added the Enigma Shield to my stash. So long suckers!|/Signed,|/The world famous thief|/Ladrone"
		self.locks.add("drop:false()")
		self.db.desc = "A handwritten note."

class cryptexultima(DefaultObject):
	name = "Cryptex Ultima"
	def at_object_creation(self):
		self.tags.add("readable", category="isreadable")
		self.tags.add("single", category="isreadable")
		self.db.story = "Your eyes hurt immediately upon gazing at the pages.|/Strange glowing glyphs seem to shift and transform like fluid creeping across the page causing waves of nausea to wash over you."
		self.locks.add("drop:false()")
		self.db.desc = "The Cryptex Ultima."