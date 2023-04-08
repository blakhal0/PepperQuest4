from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject, rustysword
from evennia.prototypes.spawner import spawn


class chatroshi(default_cmds.MuxCommand):
	key = "talk master roshi"
	aliases = ["Talk Master Roshi", "Talk Master roshi", "Talk master roshi", "talk Master Roshi", "talk Master roshi", "talk master Roshi", "talk roshi", "Talk Roshi", "talk Roshi", "Talk roshi"]
	auto_help = True
	def func(self):
		if not self.caller.tags.get("beginning"):
			self.caller.msg("|/Master Roshi is dead, he does not respond to you.")
			return
		if "Training Dummy" in self.caller.db.monsterstats.keys():
			if 3 <= int(self.caller.db.monsterstats["Training Dummy"]['killed']) <= 9:
				self.caller.msg("|/|mMaster Roshi|n says: Well, looky there, you knocked the stuffing out of that training dummy! Looks like you can take care of yourself enough to venture out of the village.")
			elif 10 <= int(self.caller.db.monsterstats["Training Dummy"]['killed']) <= 15:
				self.caller.msg("|/|mMaster Roshi|n says: You've been beating the heck out of that training dummy! Looks like you can take care of yourself enough to venture out of the village.")
			elif 16 <=int(self.caller.db.monsterstats["Training Dummy"]['killed']) <= 20:
				self.caller.msg("|/|mMaster Roshi|n says: Woweee! You're a regular warrior! You really have shown that training dummy who's boss. Looks like you can take care of yourself enough to venture out of the village.")
				if self.caller.db.gold < 100:
					self.caller.msg("|mMaster Roshi|n says: But before you go, here's a little something for bringing a smile to an old masters face.")
					self.caller.db.gold += 50
					self.caller.msg("Master Roshi reaches into his robes and hands you a purse of 50 gold.")
			elif int(self.caller.db.monsterstats["Training Dummy"]['killed']) > 50:
				self.caller.msg("|/|mMaster Roshi|n says: *sniffle sniffle* You bring a tear to an old fighting masters eye. I haven't seen a student with your ferocity in a hundred years!")
				if self.caller.search("Rusty Old Sword", candidates=self.caller.contents, quiet=True):
					self.caller.msg("|mMaster Roshi|n says: There's nothing else I can teach you, go forth warrior! Seek your fortunes in this world.")
					return
				self.caller.msg("|mMaster Roshi|n says: I've waited a long time for someone like you to come along, no surprise with dragon blood in your veins. *hehehehe* Here, I want you to have this.")
				r_proto = {
				"key": "Rusty Old Sword",
				"typeclass": "typeclasses.objects.rustysword",
				"location": self.caller
				}
				spawn(r_proto)
				self.caller.msg("|mMaster Roshi|n says: It won't do you much good now, but maybe along your travels you can find someone to fix it up for you.")
				self.caller.msg("Master Roshi hands you a Rusty Old Sword.")
		self.caller.msg("|/|mMaster Roshi|n says: Oh, well well well, look who we have here. *hehehehe* %s, I'm surprised to see you here." % (self.caller.key))
		self.caller.msg("|mMaster Roshi|n says: Come to pay an old man a visit or do you want to learn how to defend yourself?")
		answer = yield("What do you want to do? |cV|nisit, |cL|nearn, |cN|nothing")
		if answer.lower() in ["visit", "v"]:
			self.caller.msg("|/|mMaster Roshi|n says: *hehehehe* Well that's sure sweet of ya to check in on an old timer like me. I don't have many visitors these days, no need to fight, no use for an old fighting master like myself.")
			self.caller.msg("|mMaster Roshi|n says: BUT, if you wanna leave town, you gotta train to defend yourself. They'll keep you on your mothers apron strings until that happens.")
			return
		elif answer.lower() in ["learn", "l"]:
			if "Training Dummy" in self.caller.db.monsterstats.keys() and 3 <= int(self.caller.db.monsterstats["Training Dummy"]['killed']):
				self.caller.msg("|/|mMaster Roshi|n says: Well, looky there, you knocked the stuffing out of that training dummy! Looks like you can take care of yourself enough to venture out of the village.")
				self.caller.msg("|mMaster Roshi|n says: 'course you're welcome to keep training all you want. Nope, training never hurt anyone.")
				return
			else:
				self.caller.msg("|/|mMaster Roshi|n says: *humm* Yes, lets see here.")
				self.caller.msg("Master Roshi takes a slow walk around you, prodding your arms and legs with his cane, hemming and clucking between unintelligible mumbles.")
				self.caller.msg("|mMaster Roshi|n says: A bit on the lean side, yep, not a lot to work with. *harumpf* But, yes, potential. Maybe even a bit of destiny. *hehehehe* Sure as a turtle's got a shell. Got a bit of fire in you I think.")
				self.caller.msg("|mMaster Roshi|n says: Well, there's not a lot to it, best to learn by doing I always say. See that Training Dummy over there. It's a special one from a long time ago.")
				self.caller.msg("|mMaster Roshi|n says: Still has a bit of the old magic in it you see. You can |cTrain|n here with no consequences. That's right, no harm no foul, not one bit.")
				self.caller.msg("|mMaster Roshi|n says: During battle, |cA|nttack will attack the enemy with your equipped weapon, no weapon? No problem, just punch em! *hya-ha* Just like that.")
				self.caller.msg("|mMaster Roshi|n says: |cD|nefend will double your defence for one turn. Good if you think something big is coming.")
				self.caller.msg("|mMaster Roshi|n says: |cI|ntem will let you use an item from your inventory. Good for mid battle healing up, restoring magic, etc etc. You have to have something to use before you can use it though.")
				self.caller.msg("|mMaster Roshi|n says: |cM|nagic, *humrpf*, magic's pretty well gone from the world. If you do happen to learn a battle spell, that's how you use it.")
				self.caller.msg("|mMaster Roshi|n says: |cF|nlee. *harumpf* only cowards flee battle, but if you find you bit off more than you can chew, you can give it a shot. Won't work all the time, but there's a chance it will.")
				self.caller.msg("|mMaster Roshi|n says: Don't get dead, you'll lose some of your money, get half your life and magic back and get dropped off at the last place you visited.")
				self.caller.msg("|mMaster Roshi|n says: Well, you're not going to learn by standing here staring at my leathery old face, go on!")
				self.caller.msg("|mMaster Roshi|n says: Come on back over and talk to me again when you've won, oh, let's say three fights.")
				return
		elif answer.lower() in ["nothing", "n"]:
			self.caller.msg("|/|mMaster Roshi|n says: Well what're ya doing standing here wagging your jaw at me for? Don'tcha got some work to be doing, go on!!")
			self.caller.msg("|mMaster Roshi|n says: Damned kids these days, I tell ya, back in my day if I was wasting someones time I'd get my hide tanned for it. Bums.")
			return
		else:
			self.caller.msg("|/|mMaster Roshi|n says: HUH??!?!?! I can't hear so well these days you know. Might help if you yung'ns actually had something worth saying. *humpff* Mush brains, mush mouths. *humpff*")
			return

class RoshiCmdSet(CmdSet):
	key = "RoshiCmdSet"
	def at_cmdset_creation(self):
		self.add(chatroshi())

class masterroshi(DefaultObject):
	def at_object_creation(self):
		self.db.deaddesc = "Master Roshi's corpse lays in a puddle of dried blood surrounded by fallen Valaharran soldiers. The fighting master had one last fight left in him."
		self.db.desc = "Master Roshi stands there staring at you beneath huge bushy eyebrows, stroking his long white beard."
		self.db.tagname = "beginning"
		self.tags.add("specialnpc")
		self.cmdset.add_default(RoshiCmdSet, permanent=True)
		self.locks.add("get:false()")
	def return_appearance(self, looker):
		if looker.tags.get(self.db.tagname):
			return self.db.desc
		else:
			return self.db.deaddesc