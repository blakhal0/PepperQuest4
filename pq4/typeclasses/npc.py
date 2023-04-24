from typeclasses.objects import DefaultObject
import random

geterrors = ["Hey hey! Hands off the merchandise!!", "EEEEK!!!! Don't touch me there!!", "MMMMmmm hmmmm, little lower will ya?", "Kidnapping is a crime ya know.", "BACK OFF!!", "You goat kissing pervert! Keep your hands to yourself!", "*SLAP* No touching!!", "Didn't your mother tell you to keep your hands to yourself?", "You do that again, you're going to have one less hand."]
cowmsg = ["moooOOOOOO!!", "Mooooo", "moo"]

class npc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("single", category="talkative")
		self.db.desc = "Just a normal person."
		self.db.msg = ""
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))

class chickenlocator(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("chickencompass", category="talkative")
		self.db.desc = "A strange character wearing a hat resembling the comb and wattles of a chicken and a shirt that simply says 'DOOM!!!!'."
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))

hangdesc = ["The onlooker bobs back and forth trying to get a glimpse of the gallows.", "The onlooker pushes through the crowd for a better spot.", "The onlooker stands there, marveling at the size of the crowd.", "Tears run down their face, quielty weeping."]
hangmsg = ["HANG THE FILTHY THIEF!!", "HAVE MERCY!!", "BOOOOOO!!!!!", "MAKE SURE THE NOOSE IS TIGHT!!"]

class hangingcrowd(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("single", category="talkative")
		self.db.desc = random.choice(hangdesc)
		self.db.msg = random.choice(hangmsg)
		self.locks.add("get:false()")
		self.locks.add("view:not tag(ladrone)")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))

class mugablenpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("single", category="talkative")
		self.tags.add("mugable")
		self.db.desc = "A very fancily dressed and apparently wealthy person."
		self.db.msg = "Oh dear, a peasant is speaking to me, shoo, shoo!!"
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))

class guard(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("single", category="talkative")
		self.db.desc = "The guard stands at attention, carefully eying the surrounding area for trouble."
		self.db.msg = "No lallygagging. Be off with you, and stay out of trouble or I'll put my boot up your backside."
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))

class hangguide(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("tagnpc", category="talkative")
		self.db.desc = ""
		self.db.tagdesc = ""
		self.db.untaggedresp = "You here for the hanging? Me too. It's in the City Center, just a little east and north of here."
		self.db.taggedresp = "Well, that was something. I better get the hell outta here while I've still got a purse!"
		self.db.tagname = "ladrone"
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))
	def return_appearance(self, looker):
		if not looker:
			return ""
		desc = str()
		if looker.tags.get(self.db.tagname):
			desc = self.db.tagdesc
		else:
			desc = self.db.desc
		return desc

class peasant(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("peasantriot", category="talkative")
		self.db.desc = "Just a normal person."
		self.db.tagdesc = ""
		self.db.untaggedresp = ""
		self.db.taggedresp = ""
		self.db.tagname = "thekingisdead"
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))
	def return_appearance(self, looker):
		if not looker:
			return ""
		desc = str()
		if looker.tags.get(self.db.tagname):
			desc = self.db.tagdesc
		else:
			desc = self.db.desc
		return desc

class loyalist(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("loyalist", category="talkative")
		self.db.desc = "Just a normal person."
		self.db.tagdesc = ""
		self.db.untaggedresp = ""
		self.db.taggedresp = ""
		self.db.tagname = "thekingisdead"
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))
	def return_appearance(self, looker):
		if not looker:
			return ""
		desc = str()
		if looker.tags.get(self.db.tagname):
			desc = self.db.tagdesc
		else:
			desc = self.db.desc
		return desc

class thief(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("thief", category="talkative")
		self.db.desc = "A shady looking character."
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|rAngry %s|n" % (random.choice(cowmsg))

class cow(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("single", category="talkative")
		self.db.desc = "A spotted cow looks up from grazing and stares at you, slowly chewing."
		self.db.msg = "%s" % (random.choice(cowmsg))
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|rAngry %s|n" % (random.choice(cowmsg))

class secretduck(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("single", category="talkative")
		self.db.desc = "Quacktastic! You found a Secret Duck!"
		self.db.msg = ""
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n|/HOLY SHIT!! A TALKING DUCK!!!" % (random.choice(geterrors))

class multinpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("multi", category="talkative")
		self.db.desc = "Just a normal person."
		self.db.msg = ""
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))

class omthemighty(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("multi", category="talkative")
		self.db.desc = "The small turtle stares back at you with an angry one-eyed glare."
		self.db.msg = ["…what gods need is belief, and what humans want is gods.", "At this pace I could get to the temple faster on my own! LET'S GOOOO!!!!", "Most gods find it hard to walk and think at the same time.", "I love to see an atheist about, gives me something to aim at."]
		self.locks.add("drop:false()")

class tagnpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("tagnpc", category="talkative")
		self.db.desc = ""
		self.db.taggedresp = ""
		self.db.untaggedresp = ""
		self.db.tagname = ""
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))

class paiprinpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("tagnpc", category="talkative")
		self.db.desc = ""
		self.db.taggedresp = ""
		self.db.untaggedresp = ""
		self.db.tagname = "thekingisdead"
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))

class addtagnpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("addtagnpc", category="talkative")
		self.db.desc = ""
		self.db.msg = ""
		self.db.addtag = ""
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))

class remtagnpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("remtagnpc", category="talkative")
		self.db.desc = ""
		self.db.msg = ""
		self.db.remtag = ""
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))

class evmnpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("evm", category="talkative")
		self.db.desc = "Just a normal person."
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))

class tagviewnpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("single", category="talkative")
		self.db.desc = ""
		self.db.tagdesc = ""
		self.db.msg = ""
		self.db.tagname = ""
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))
	def return_appearance(self, looker):
		if not looker:
			return ""
		desc = str()
		if looker.tags.get(self.db.tagname):
			desc = self.db.tagdesc
		else:
			desc = self.db.desc
		return desc

class tagviewtagrespnpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("tagnpc", category="talkative")
		self.db.desc = ""
		self.db.tagdesc = ""
		self.db.untaggedresp = ""
		self.db.taggedresp = ""
		self.db.tagname = ""
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))
	def return_appearance(self, looker):
		if not looker:
			return ""
		desc = str()
		if looker.tags.get(self.db.tagname):
			desc = self.db.tagdesc
		else:
			desc = self.db.desc
		return desc

class mapnpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("mapnpc", category="talkative")
		self.db.desc = ""
		self.db.msg = ""
		self.db.locationname = ""
		self.db.mapname = ""
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))

class accoladenpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("accoladenpc", category="talkative")
		self.db.accolade = ""
		self.db.desc = ""
		self.db.accoladedesc = ""
		self.db.msg = ""
		self.db.accolademsg = ""
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))
	def return_appearance(self, looker):
		if not looker:
			return ""
		desc = str()
		if self.db.accolade in looker.db.accolades:
			desc = self.db.accoladedesc
		else:
			desc = self.db.desc
		return desc

soldharadead = ["A rotting corpse lays there, swarming with flies.", "A pile of blood and viscera that used to be a villager is splattered on the ground.", "Little more than a crushed skull remains identifiable.", "A corpse with arms and legs lay bent at very unnatural angles.", "An unidentifiable pile of meat rots in the sun."]
class soldharanpc(tagviewnpc):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("soldharanpc", category="talkative")
		self.db.deaddesc = "%s" % random.choice(soldharadead)
		self.db.beginningdesc = ""
		self.db.msg = ""
		self.db.tagname = "beginning"
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))
	def return_appearance(self, looker):
		if not looker:
			return ""
		desc = str()
		if looker.tags.get(self.db.tagname):
			desc = self.db.beginningdesc
		else:
			desc = self.db.deaddesc
		return desc

helliongeterror = ["Unease and dread fill you as the ghostly energy of the entity washes over you.", "It may feel as though you have brushed up against something intangible.", "You feel a sense of the ghost's presence lingering on your skin, almost like a filth you cannot wash clean.", "You feel slightly disoriented, as if you have stepped into a realm that lies somewhere between the world of the living and the world of the dead."]
class hellionnpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("hellion", category="talkative")
		self.db.desc = "The ghost appears ethereal and translucent like wisps of smoke or fog. Forms twisted and distorted, with features bordering on grotesque. Faces contorted with expressions of anger, fear, and hatred. Otherworldly light flashes and blazes in their eyes like a shimmering gem as they see you."
		self.locks.add("get:false()")
		self.locks.add("view:mondefgtr(Honkiamat, 0)")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(helliongeterror))

class mondefnpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("mondefnpc", category="talkative")
		self.db.desc = ""
		self.db.mondefdesc = ""
		self.db.msg = ""
		self.db.mondefmsg = ""
		self.db.monstername = ""
		self.db.monsterqty = ""
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))
	def return_appearance(self, looker):
		if not looker:
			return ""
		desc = str()
		if self.db.mondefdesc == "":
			desc = self.db.desc
		elif not self.db.monstername in looker.attributes.get("monsterstats"):
			desc = self.db.desc
		elif looker.db.monsterstats[self.db.monstername]["killed"] < int(self.db.monsterqty):
			desc = self.db.desc
		elif looker.db.monsterstats[self.db.monstername]["killed"] >= int(self.db.monsterqty):
			desc = self.db.mondefdesc
		return desc

class questnpc(DefaultObject):
	def at_object_creation(self):
		self.tags.add("talkative", category="npc")
		self.tags.add("questnpc", category="talkative")
		self.db.desc = "A quest giving NPC."
		self.db.inprogdesc = ""
		self.db.completeddesc = ""
		self.db.msg = ""
		self.db.inprogmsg = ""
		self.db.successmsg = ""
		self.db.finishedmsg = ""
		self.db.questturneddown = ""
		self.db.questname = ""
		self.db.questtype = "get/kill"
		self.db.questthingname = "item/monster"
		self.db.questqty = 0
		self.db.rewardtype = "gold", "item", "weapon", "armor"
		self.db.rewardthingname = ""
		self.db.rewardthingtypeclass = ""
		self.db.rewardqty = 0
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|r%s|n" % (random.choice(geterrors))
	def return_appearance(self, looker):
		if not looker:
			return ""
		desc = str()
		if self.db.questname in looker.db.quests.keys():
		#check if they completed the quest
			if looker.db.quests[self.db.questname]["completed"] == "yes":
				if not self.db.completeddesc == "":
					desc = self.db.completeddesc
				else:
					desc = self.db.desc
		#quest is in progress
			else:
				if not self.db.inprogdesc == "":
					desc = self.db.inprogdesc
				else:
					desc = self.db.desc
		else:
			desc = self.db.desc
		return desc