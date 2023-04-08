from evennia import default_cmds, CmdSet, search_object, search_tag
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class chathost(default_cmds.MuxCommand):
	key = "talk host"
	aliases = ["Talk Host", "Talk host", "talk Host" ]
	auto_help = True
	def func(self):
	#rewards
		if self.caller.tags.get("arena1"):
			self.caller.tags.remove("arena1")
			self.caller.msg("|/|mHost|n says: Well, you didn't make it very far, but you gave it a good shot!!")
			self.caller.msg("|mHost|n says: As a reward, you get 3 Spicy Herb!")
			self.caller.msg("|mHost|n says: Congratulations, and come back again!")
			target = self.caller.search("Spicy Herb", candidates=self.caller.contents, quiet=True)
			if not target:
				aone_proto = {
				"key": "Spicy Herb",
				"typeclass": "typeclasses.items.spicyherb",
				"qty": 3,
				"location": self.caller
				}
				spawn(aone_proto)
			else:
				target[0].db.qty += 3
			return
		if self.caller.tags.get("arena2"):
			self.caller.tags.remove("arena2")
			self.caller.msg("|/|mHost|n says: Well, you didn't make it very far, but you gave it a good shot!!")
			self.caller.msg("|mHost|n says: As a reward, you get 3 Magic Dust!")
			self.caller.msg("|mHost|n says: Congratulations, and come back again!")
			target = self.caller.search("Magic Dust", candidates=self.caller.contents, quiet=True)
			if not target:
				atwo_proto = {
				"key": "Magic Dust",
				"typeclass": "typeclasses.items.magicdust",
				"qty": 3,
				"location": self.caller
				}
				spawn(atwo_proto)
			else:
				target[0].db.qty += 3
			return
		if self.caller.tags.get("arena3"):
			self.caller.tags.remove("arena3")
			self.caller.msg("|/|mHost|n says: You did a pretty respectable job in the arena!!")
			self.caller.msg("|mHost|n says: As a reward, you get 3 Faster Feather!")
			self.caller.msg("|mHost|n says: Congratulations, and come back again!")
			target = self.caller.search("Faster Feather", candidates=self.caller.contents, quiet=True)
			if not target:
				athree_proto = {
				"key": "Faster Feather",
				"typeclass": "typeclasses.items.fasterfeather",
				"qty": 3,
				"location": self.caller
				}
				spawn(athree_proto)
			else:
				target[0].db.qty += 3
			return
		if self.caller.tags.get("arena4"):
			self.caller.tags.remove("arena4")
			self.caller.msg("|/|mHost|n says: You make it a fair way before falling in battle, great work!")
			self.caller.msg("|mHost|n says: As a reward, you get 300 gold!")
			self.caller.msg("|mHost|n says: Congratulations, and come back again!")
			self.caller.db.gold += 300
			return
		if self.caller.tags.get("arena5"):
			self.caller.tags.remove("arena5")
			self.caller.msg("|/|mHost|n says: You make it a fair way before falling in battle, great work!")
			self.caller.msg("|mHost|n says: As a reward, you get 700 gold!")
			self.caller.msg("|mHost|n says: Congratulations, and come back again!")
			self.caller.db.gold += 700
			return
		if self.caller.tags.get("arena6"):
			self.caller.tags.remove("arena6")
			self.caller.msg("|/|mHost|n says: You did a pretty respectable job in the arena!!")
			self.caller.msg("|mHost|n says: As a reward, you get 4 Restoring Ruby!")
			self.caller.msg("|mHost|n says: Congratulations, and come back again!")
			target = self.caller.search("Restoring Ruby", candidates=self.caller.contents, quiet=True)
			if not target:
				asix_proto = {
				"key": "Restoring Ruby",
				"typeclass": "typeclasses.items.restoringruby",
				"qty": 4,
				"location": self.caller
				}
				spawn(asix_proto)
			else:
				target[0].db.qty += 4
			return
		if self.caller.tags.get("arena7"):
			self.caller.tags.remove("arena7")
			self.caller.msg("|/|mHost|n says: Amazing!! You almost made it to the end!")
			self.caller.msg("|mHost|n says: As a reward, you get 3 Yorkshire Tea! A perfectly balanced reward!")
			self.caller.msg("|mHost|n says: Congratulations, and come back again!")
			target = self.caller.search("Yorkshire Tea", candidates=self.caller.contents, quiet=True)
			if not target:
				aseven_proto = {
				"key": "Yorkshire Tea",
				"typeclass": "typeclasses.items.yorkshiretea",
				"qty": 3,
				"location": self.caller
				}
				spawn(aseven_proto)
			else:
				target[0].db.qty += 3
			return
		if self.caller.tags.get("titan"):
			self.caller.tags.remove("titan")
			self.caller.msg("|/|mHost|n says: Congratulations on conquering the Titan Arena!!")
			if not "Titan of the Arena" in self.caller.db.accolades:
				self.caller.db.accolades.append("Titan of the Arena")
			target = self.caller.search("Titan Shield", candidates=self.caller.contents, quiet=True)
			if target:
				self.caller.msg("|mHost|n says: Looks like this isn't your first rodeo. You've already got the top prize, so you get 5000 gold!")
				self.caller.db.gold += 5000
				self.caller.msg("|mHost|n says: Congratulations! Come back again!")
				return
			else:
				self.caller.msg("|mHost|n says: For your victory over the Titan Ophion you receive the Titan Shield!!")
				ts_proto = {
				"key": "Titan Shield",
				"typeclass": "typeclasses.armor.titanshield",
				"location": self.caller
				}
				spawn(ts_proto)
				self.caller.msg("|mHost|n says: History will forever remember your name!")
				self.caller.msg("|mHost|n says: Congratulations! Come back again!")
				return
			return
	#Interaction
		self.caller.msg("|/|mHost|n says: Welcome to the Throne of the Titan Arena!")
		if self.caller.db.lvl < 10:
			self.caller.msg("|/|mHost|n says: Well hello there %s, you don't appear to have the minimum recommended experience for the arena which would be level 10. You're still welcome to try, we respect the inner fight of a warrior, just giving you fair warning." % (self.caller.key))
		if self.caller.db.gold < 20:
			self.caller.msg("|/|mHost|n says: Oh, it looks like you're a bit short on funds there. Entry fee is 20 gold. Come back again when you've got some spare gold!")
			return
		self.caller.msg("|mHost|n says: Challengers from around the world come here to test their might against 7 of the strongest champions the arena has ever known. If you can make it past them, then you get to challenge the Titan for glorious victory!")
		self.caller.msg("|mHost|n says: You'll be given the opportunity to use items or change equipment between rounds.")
		self.caller.msg("|mHost|n says: Once you enter, you either come out victorious or fall in battle, there's no other way to leave the arena. No fleeing from battle, no traveling, no chickening out.")
		self.caller.msg("|mHost|n says: The cost per entry is 20 gold, you can test your skills in the arena as many times as you want.")
		self.caller.msg("|mHost|n says: If you happen to fall in battle, don't worry, we won't take any of your gold, your health and magic will be restored, and you'll end up right back here.")
		self.caller.msg("|mHost|n says: So, what's it going to be, want to test your skills against the worlds toughest opponents and seek eternal glory?")
	#Enter Arena Choice
		answer = yield("Enter the Titans Throne Arena Battle? |gY|nes, |gN|no.")
		if answer.lower() in ["y", "yes"]:
				self.caller.db.gold -= 20
				self.caller.tags.add("arenabattle")
				self.caller.msg("|mHost|n says: Alright, good luck in there, come back and talk to me when you're done!")
				yield 2
				results = search_object("#7874")
				self.caller.move_to(results[0], quiet=True, move_hooks=True)
				return
		else:
			self.caller.msg("|/|mHost|n says: Hey, there's no shame in knowing you're not ready. That there is wisdom. The opponents in there are really tough. Come back again when you're ready!")
			return

class HostCmdSet(CmdSet):
	key = "HostCmdSet"
	def at_cmdset_creation(self):
		self.add(chathost())

class host(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The Arena Host tends to a line of contestants wanting to try their skill in the arena battle."
		self.tags.add("specialnpc")
		self.cmdset.add_default(HostCmdSet, permanent=True)
		self.locks.add("get:false()")