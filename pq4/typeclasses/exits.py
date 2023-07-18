"""
Exits

Exits are connectors between Rooms. An exit always has a destination property
set and has a single command defined on itself with the same name as its key,
for allowing Characters to traverse the exit to its destination.

"""
from evennia import DefaultExit, search_object
import random
from random import randint


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

class plantroomexit(DefaultExit):
	def at_object_creation(self):
		self.db.err_traverse = "|/|rYou are grappled by vines and cannot move."
		self.locks.add("traverse:not tag(nomove)")

class bathpipeexit(DefaultExit):
	def at_object_creation(self):
		self.db.successmoveto = "#11456"
		self.db.deathmessage = "You open the door.... SNAKES!!! Oh, nope, water. Lots and lots of water. Washed off your feet, you crack your head and drown."
	def at_traverse(self, traversing_object, target_location):
		source_location = traversing_object.location
	 #Player has correct puzzle value
		if traversing_object.db.bathhouse['water'] == "off":
			traversing_object.msg("|/You open the door and enter the room.|/")
		elif traversing_object.db.bathhouse['water'] == "on" and traversing_object.db.bathhouse['pipe'] == "fixed":
			traversing_object.msg("|/You open the door and enter the room.|/")
	 #Player does not have correct puzzle value and dies
		elif traversing_object.db.bathhouse['water'] == "on" and traversing_object.db.bathhouse['pipe'] == "broken":
			target_location = search_object(traversing_object.db.lastcity)
			target_location = target_location[0]
		 #Death Stuff
			traversing_object.msg("|/|r%s|n|/You have brought shame to yourself and your family." % (self.db.deathmessage))
			traversing_object.db.deathcount += 1
			traversing_object.db.hp = int(traversing_object.db.maxhp * .5)
			traversing_object.db.mp = int(traversing_object.db.maxmp * .5)
			traversing_object.db.gold -= int(traversing_object.db.gold * .2)
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)
		else:
			if self.db.err_traverse:
				traversing_object.msg(self.db.err_traverse)
			else:
				self.at_failed_traverse(traversing_object)

class bathsteamexit(DefaultExit):
	def at_object_creation(self):
		self.db.successmoveto = "#11345"
		self.db.deathmessage = "You summon your courage and charge in to face the horrid beast. You slip, fall, and crack your skull. You slowly come to consciousness realizing you are underwater, vision red you kick to free yourself but cannot move your legs. Looking around you see your legs, partially chewed and floating a few feet away."
	def at_traverse(self, traversing_object, target_location):
		source_location = traversing_object.location
	 #Player has completed all tasks
		if traversing_object.db.bathhouse['water'] == "on" and traversing_object.db.bathhouse['pipe'] == "fixed" and traversing_object.db.bathhouse['temp'] == "hot":
			traversing_object.msg("|/|gYou carefully step into the room, just managing to step over a wriggling tentacle, hidden from view in the steam.|n|/")
		else:
			target_location = search_object(traversing_object.db.lastcity)
			target_location = target_location[0]
		 #Death Stuff
			traversing_object.msg("|/|r%s|n|/You have brought shame to yourself and your family." % (self.db.deathmessage))
			traversing_object.db.deathcount += 1
			traversing_object.db.hp = int(traversing_object.db.maxhp * .5)
			traversing_object.db.mp = int(traversing_object.db.maxmp * .5)
			traversing_object.db.gold -= int(traversing_object.db.gold * .2)
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)
		else:
			if self.db.err_traverse:
				traversing_object.msg(self.db.err_traverse)
			else:
				self.at_failed_traverse(traversing_object)


boop = ["Your progress abruptly halts as you walk face-first into an unyielding mirror.", "You recoil in surprise, startled by the unexpected encounter with your own reflection.", "'Sunoffa...' your nose bleeds a little.", "Confusion washes over you as your face meets the cold surface of the mirror head-on.", "With a thud, you collide with an impenetrable barrier that mimics your every move.", "Stumbling forward, you crash into a mirror, disoriented and questioning your senses.", "The mirror mocks your futile attempts to find the path, leaving you frustrated.", "You rub your forehead, feeling foolish for running into your own mirrored reflection.", "Your hopes shatter, unlike the mirror, as you smack into your reflection.", "Collision with the mirror jolts you back to a frustrating reality.", "You stumble backward, disoriented by the mirror's deceptive presence.", "Your reflection mocks your failed attempts."]
class mirrorexit(DefaultExit):
	def at_object_creation(self):
		self.db.err_traverse = random.choice(boop)
		self.locks.add("traverse:false()")
	def at_traverse(self, traversing_object, target_location):
		source_location = traversing_object.location
		target_location = traversing_object.location
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)
		if self.db.err_traverse:
			damage = randint(5,13)
			traversing_object.msg("|/|r*THUD*|n " + self.db.err_traverse + "|/You take %d damage." % (damage))
			traversing_object.db.hp -= damage
			if traversing_object.db.hp <= 0:
				traversing_object.msg("|/|rWhat tragic fate, you accidentally killed yourself running into mirrors.|n|/You have brought shame to yourself and your family.")
				traversing_object.db.hp = int(traversing_object.db.maxhp * .5)
				traversing_object.db.mp = int(traversing_object.db.maxmp * .5)
				traversing_object.db.gold -= int(traversing_object.db.gold * .2)
				results = search_object(traversing_object.db.lastcity)
				traversing_object.move_to(results[0], quiet=True, move_hooks=False)
		else:
			self.at_failed_traverse(traversing_object)
	def return_appearance(self, looker):
		if not looker:
			return ""
		desc = str()
		if looker.db.armorequipped in ["None", "none"]:
			armordesc = "wearing not a single stitch of armor"
		else:
			armordesc = "clad in " + looker.db.armorequipped.lower()
	#Shield Desc
		if not looker.db.shieldequipped.lower() == "none":
			armordesc += " and a %s" % (looker.db.shieldequipped.lower())
	#Weapon Desc
		if looker.db.weaponequipped in ["none", "None"]:
			weapondesc = "clenching your bruised and bloody fists"
		else:
			weapondesc = "holding a " + looker.db.weaponequipped.lower()
	#Reversed character self.caller.db.desc
		desc = "You see yourself, %s, %s.|/As you look closer, you see the reflection twist and warp, darkening. A wicked smile stretches across its face." % (armordesc, weapondesc)
		luck = randint(1,3)
		if luck == 2:
			looker.msg(desc + "|/|rThe eyes of the image begin to glow malevolently. Suddenly the image in the mirror attacks!!|n")
			looker.tags.add("letsfight")
			looker.execute_cmd('fight')
		else:
			return desc

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

class healingexit(DefaultExit):
	def at_object_creation(self):
		self.db.message = "|/|gYou leave the bath feeling completely restored.|n"
	def at_traverse(self, traversing_object, target_location):
		traversing_object.msg(self.db.message)
		source_location = traversing_object.location
		traversing_object.db.hp = traversing_object.db.maxhp
		traversing_object.db.mp = traversing_object.db.maxmp
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

class sandexitexit(DefaultExit):
	def at_object_creation(self):
		self.db.message = "|/|rThe sand drains out from under your feet! You struggle for purchase trying to drag yourself out of the swallowing sand. But to no avail.|n|/"
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

class blindsandexit(DefaultExit):
	def at_object_creation(self):
		self.db.message = "|/|rThe sand drains out from under your feet! You struggle for purchase trying to drag yourself out of the swallowing sand. But to no avail.|n|/"
		self.db.err_traverse = "|/You cannot go that way|/"
		self.locks.add("view:false()")
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

class remtagmsgexit(DefaultExit):
	def at_object_creation(self):
		self.db.tagname = "tagnametoremove"
		self.db.message = "|/Test|/"
		self.db.err_traverse = "|/You cannot go that way|/"
	def at_traverse(self, traversing_object, target_location):
		traversing_object.msg(self.db.message)
		if traversing_object.tags.get(self.db.tagname):
			traversing_object.tags.remove(self.db.tagname)
		source_location = traversing_object.location
		if traversing_object.move_to(target_location):
			self.at_after_traverse(traversing_object, source_location)
		else:
			if self.db.err_traverse:
				traversing_object.msg(self.db.err_traverse)
			else:
				self.at_failed_traverse(traversing_object)

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