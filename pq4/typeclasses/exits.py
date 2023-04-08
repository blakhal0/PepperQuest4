"""
Exits

Exits are connectors between Rooms. An exit always has a destination property
set and has a single command defined on itself with the same name as its key,
for allowing Characters to traverse the exit to its destination.

"""
from evennia import DefaultExit, search_object
import random


class Exit(DefaultExit):
	"""
	Exits are connectors between rooms. Exits are normal Objects except
	they defines the `destination` property. It also does work in the
	following methods:

	 basetype_setup() - sets default exit locks (to change, use `at_object_creation` instead).
	 at_cmdset_get(**kwargs) - this is called when the cmdset is accessed and should
							  rebuild the Exit cmdset along with a command matching the name
							  of the Exit object. Conventionally, a kwarg `force_init`
							  should force a rebuild of the cmdset, this is triggered
							  by the `@alias` command when aliases are changed.
	 at_failed_traverse() - gives a default error message ("You cannot
							go there") if exit traversal fails and an
							attribute `err_traverse` is not defined.

	Relevant hooks to overload (compared to other types of Objects):
		at_traverse(traveller, target_loc) - called to do the actual traversal and calling of the other hooks.
											If overloading this, consider using super() to use the default
											movement implementation (and hook-calling).
		at_after_traverse(traveller, source_loc) - called by at_traverse just after traversing.
		at_failed_traverse(traveller) - called by at_traverse if traversal failed for some reason. Will
										not be called if the attribute `err_traverse` is
										defined, in which case that will simply be echoed.
	"""

	pass

class casinochaosexit(DefaultExit):
	def at_object_creation(self):
		self.db.locations = ['#9023', '#9011', '#9035', '#8999', '#9029', '#9005', '#9057', '#9051', '#9038', '#8996', '#9020', '#9014']
		self.locks.add("view:not inlist(accolades, Fortunate One)")
		self.locks.add("traverse:not inlist(accolades, Fortunate One)")
	def at_traverse(self, traversing_object, target_location):
		source_location = traversing_object.location
		target_location = search_object(random.choice(self.db.locations))
		target_location = target_location[0]
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)
		else:
			if self.db.err_traverse:
				traversing_object.msg(self.db.err_traverse)
			else:
				self.at_failed_traverse(traversing_object)

class iftagexit(DefaultExit):
	def at_object_creation(self):
		self.db.hastaglocation = "#XXXX"
		self.db.notaglocation = "#XXXX"
		self.db.tagname = ""
	def at_traverse(self, traversing_object, target_location):
		source_location = traversing_object.location
		if traversing_object.tags.get(self.db.tagname):
			target_location = search_object(self.db.hastaglocation)
			target_location = target_location[0]
		else:
			target_location = search_object(self.db.notaglocation)
			target_location = target_location[0]
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)
		else:
			if self.db.err_traverse:
				traversing_object.msg(self.db.err_traverse)
			else:
				self.at_failed_traverse(traversing_object)

class heartexit(DefaultExit):
	def at_object_creation(self):
		self.db.hastaglocation = "#9314"
		self.db.notaglocation = "#9315"
		self.db.tagname = "heart"
	def at_traverse(self, traversing_object, target_location):
		source_location = traversing_object.location
		if traversing_object.tags.get(category="SuitPath") == self.db.tagname:
			target_location = search_object(self.db.hastaglocation)
			target_location = target_location[0]
		else:
			target_location = search_object(self.db.notaglocation)
			target_location = target_location[0]
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)
		else:
			if self.db.err_traverse:
				traversing_object.msg(self.db.err_traverse)
			else:
				self.at_failed_traverse(traversing_object)


class diamondexit(iftagexit):
	def at_object_creation(self):
		self.db.hastaglocation = "#9314"
		self.db.notaglocation = "#9315"
		self.db.tagname = "diamond"
	def at_traverse(self, traversing_object, target_location):
		source_location = traversing_object.location
		if traversing_object.tags.get(category="SuitPath") == self.db.tagname:
			target_location = search_object(self.db.hastaglocation)
			target_location = target_location[0]
		else:
			target_location = search_object(self.db.notaglocation)
			target_location = target_location[0]
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)
		else:
			if self.db.err_traverse:
				traversing_object.msg(self.db.err_traverse)
			else:
				self.at_failed_traverse(traversing_object)

class clubexit(iftagexit):
	def at_object_creation(self):
		self.db.hastaglocation = "#9314"
		self.db.notaglocation = "#9315"
		self.db.tagname = "club"
	def at_traverse(self, traversing_object, target_location):
		source_location = traversing_object.location
		if traversing_object.tags.get(category="SuitPath") == self.db.tagname:
			target_location = search_object(self.db.hastaglocation)
			target_location = target_location[0]
		else:
			target_location = search_object(self.db.notaglocation)
			target_location = target_location[0]
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)
		else:
			if self.db.err_traverse:
				traversing_object.msg(self.db.err_traverse)
			else:
				self.at_failed_traverse(traversing_object)

class spadeexit(iftagexit):
	def at_object_creation(self):
		self.db.hastaglocation = "#9314"
		self.db.notaglocation = "#9315"
		self.db.tagname = "spade"
	def at_traverse(self, traversing_object, target_location):
		source_location = traversing_object.location
		if traversing_object.tags.get(category="SuitPath") == self.db.tagname:
			target_location = search_object(self.db.hastaglocation)
			target_location = target_location[0]
		else:
			target_location = search_object(self.db.notaglocation)
			target_location = target_location[0]
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)
		else:
			if self.db.err_traverse:
				traversing_object.msg(self.db.err_traverse)
			else:
				self.at_failed_traverse(traversing_object)

class loopexit(DefaultExit):
	def at_object_creation(self):
		self.db.locations = ["#9310","#9333", "#9334"]
		self.db.escapelocation = "#9310"
		self.db.msg = ""
	def at_traverse(self, traversing_object, target_location):
		source_location = traversing_object.location
		target_location = random.choice(self.db.locations)
		target_location = search_object(target_location)
		target_location = target_location[0]
		if not self.db.msg == "":
			traversing_object.msg("|/" + self.db.msg + "|/ |/")
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)
		else:
			if self.db.err_traverse:
				traversing_object.msg(self.db.err_traverse)
			else:
				self.at_failed_traverse(traversing_object)

class noviewexit(DefaultExit):
	def at_object_creation(self):
		self.locks.add("view:false()")

class msgexit(DefaultExit):
	def at_object_creation(self):
		self.db.message = "|/Test|/"
		self.db.err_traverse = "|/You cannot go that way|/"
	def at_traverse(self, traversing_object, target_location):
		traversing_object.msg(self.db.message)
		source_location = traversing_object.location
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)
		else:
			if self.db.err_traverse:
				traversing_object.msg(self.db.err_traverse)
			else:
				self.at_failed_traverse(traversing_object)

class sandstormexit(msgexit):
	def at_object_creation(self):
		self.db.message = "|/|rAAHHHHHHH!!!!!!!|/Your footing suddenly disappears and you find yourself hurtling towards the ground.|/*THUD*|/Ouch. You cough out a mouthful of sand, roll over, and moan in pain.|n|/|mEverett|n says: My word, that looked like it hurt!"

class sewerexits(DefaultExit):
	def at_object_creation(self):
		self.locks.add("view:holds(Torch)")

class sewermsgexit(DefaultExit):
	def at_object_creation(self):
		self.db.message = "|r|/You squint as the sun hits your eyes. You have emerged from the sewers.|n|/|mKuloa|n says: Whew! I knew you could do it! WE'RE FREE!! Look, I think you're the kind of person this country needs. It's time for a good ol peasant revolt! Meet me at The Far Lantern Pub, it's in the northeast corner of Paipri. Unless the King or Queen see us again I think we'll be just fine, the guards are idiots."
		self.locks.add("view:holds(Torch)")
	def at_traverse(self, traversing_object, target_location):
		if not traversing_object.tags.get("thekingisdead"):
			traversing_object.msg(self.db.message)
		if traversing_object.search("Torch", candidates=traversing_object.contents, quiet=True):
			for i in traversing_object.contents:
				if i.key == "Torch":
					i.delete()
					traversing_object.msg("You toss the torch back into the sewer, hissing as it's extinguished.")
		if not traversing_object.tags.get("folkhero") and not traversing_object.tags.get("thekingisdead"):
			traversing_object.tags.add("folkhero")
		source_location = traversing_object.location
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)
		else:
			if self.db.err_traverse:
				traversing_object.msg(self.db.err_traverse)
			else:
				self.at_failed_traverse(traversing_object)

class lvlchkexit(DefaultExit):
	def at_object_creation(self):
		self.db.lvllow = "|/|mSoldier says|n: Whoa-whoa-whoa there, this is a war front. You'll be a worm farm in a minute if you go trying to fight a Valaharran berserker. You best go get some experience instead of throwing your life away.|/"
		self.db.err_traverse = "You change your mind about heading that direction."
	def at_traverse(self, traversing_object, target_location):
		if traversing_object.db.lvl <= 20:
			traversing_object.msg(self.db.lvllow)
			self.at_failed_traverse(traversing_object)
		elif traversing_object.db.lvl > 20:
			source_location = traversing_object.location
			if traversing_object.move_to(target_location):
				self.at_after_traverse(traversing_object, source_location)
			else:
				if self.db.err_traverse:
					traversing_object.msg(self.db.err_traverse)
				else:
					self.at_failed_traverse(traversing_object)

class fancycheckexit(DefaultExit):
	def at_object_creation(self):
		self.db.notfancy = "|/|mGuard|n says: Whoa-whoa-whoa there, where do you think you're going? Look at you, you certainly don't belong in the Upper District."
		self.db.fancy = "|/|gThe guard nods slightly and moves out of your path.|n"
		self.db.kingofthieves = "|/|mGuard|n says: Hey, wait a min.. Oh, you again. dressing down these days eh? HARHARHAR No shame in slumming it occassionally. Welcome back."
		self.db.err_traverse = "The guard stands in front of you shooing you away."
	def at_traverse(self, traversing_object, target_location):
		if traversing_object.db.armorequipped.lower() == "none" and not traversing_object.tags.get("kingofthieves"):
			traversing_object.msg(self.db.notfancy)
			traversing_object.msg(self.db.err_traverse)
			self.at_failed_traverse(traversing_object)
		elif traversing_object.tags.get("kingofthieves"):
			traversing_object.msg(self.db.kingofthieves)
			source_location = traversing_object.location
			if traversing_object.move_to(target_location):
				self.at_after_traverse(traversing_object, source_location)
			else:
				if self.db.err_traverse:
					traversing_object.msg(self.db.err_traverse)
				else:
					self.at_failed_traverse(traversing_object)
		else:
			target = traversing_object.search(traversing_object.db.armorequipped, candidates=traversing_object.contents, quiet=True)
			if target[0].tags.get("fancy"):
				traversing_object.msg(self.db.fancy)
				source_location = traversing_object.location
				if traversing_object.move_to(target_location):
					self.at_after_traverse(traversing_object, source_location)
				else:
					if self.db.err_traverse:
						traversing_object.msg(self.db.err_traverse)
					else:
						self.at_failed_traverse(traversing_object)
			else:
				traversing_object.msg(self.db.notfancy)
				traversing_object.msg(self.db.err_traverse)
				self.at_failed_traverse(traversing_object)

class remtagexit(DefaultExit):
	def at_object_creation(self):
		self.db.tagname = "training"
	def at_traverse(self, traversing_object, target_location):
		if traversing_object.tags.get(self.db.tagname):
			traversing_object.tags.remove(self.db.tagname)
		source_location = traversing_object.location
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)

class cityentrance(DefaultExit):
	def at_object_creation(self):
		self.db.city = "#"
	def at_traverse(self, traversing_object, target_location):
		traversing_object.db.lastcity = self.db.city
		source_location = traversing_object.location
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)

class battlereadyexit(DefaultExit):
	def at_object_creation(self):
		self.db.desc = "|/All villagers wishing to travel outside the village must prove their strength with Master Roshi!"
	def at_traverse(self, traversing_object, target_location):
		if "Training Dummy" in traversing_object.db.monsterstats.keys():
			if int(traversing_object.db.monsterstats["Training Dummy"]['killed']) >= 3:
				source_location = traversing_object.location
				if traversing_object.move_to(target_location):
					self.at_after_traverse(traversing_object, source_location)
			else:
				traversing_object.msg("|/|mFat Sal|n says: Hummmm, no, I can't quite let you out of the village yet. Your mother would hang me by my ears!! Go train some more.")
		else:
			traversing_object.msg("|/|mFat Sal|n says: All villagers wishing to travel outside the village must prove their strength with Master Roshi!")