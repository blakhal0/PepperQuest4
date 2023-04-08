from evennia import default_cmds, CmdSet, search_object, search_tag
from typeclasses.objects import DefaultObject

class chatmammoo(default_cmds.MuxCommand):
	key = "talk mammoo"
	aliases = ["Talk Mammoo"]
	auto_help = True
	def func(self):
		if not self.obj.access(self.caller, "view"):
			self.caller.msg("There's no one by that name to talk to.")
			return
		self.caller.msg("|/|mMammoo|n says: You do not bear the mark of my golden eyes, you're not one of my slaves. How curious. Well, let it not be said I am not a gracious host.")
		self.caller.msg("Mammoo throws his head back laughing making the golden coins of his mail armor jingle.")
		self.caller.msg("Gesturing in a wide arc Mammoo shows you his impressive horde. Running his hand over a gigantic pile of gold coins he turns.")
		self.caller.msg("|mMammoo|n says: It is impressive, no?")
		self.caller.msg("Mammoo walks over to two golden statues placed on a huge set of golden scales.")
		self.caller.msg("|mMammoo|n says: Two of my newest and finest pieces, Fortune and Retribution, the balancers of scales, you may know them better as Tyche and Nemesis. With control over their powers my horde will grow infinitely.")
		self.caller.msg("Mammoo flashes a golden glare at you.")
		self.caller.msg("|mMammoo|n says: I certainly hope you've not come in hopes of attempting to return them to power.")
		answer = yield("|/|mMammoo|n says: Do you really think that it's worth fighting over? Is the world really better with luck and misfortune being handed out by opposing forces? *Laughing* Do you really think YOU can stop ME?|/|cY|nes, |cN|no")
		if answer.lower() in ["n", "no"]:
			self.caller.msg("|/|mMammoo|n says: Good, I'm glad we're on the same page. I like you, it would be a shame to add your corpse to the horde.")
			self.caller.msg("Mammoo saunters away grabbing a handful of gold and smiling.")
			return
		elif answer.lower() in ["y", "yes"]:
			self.caller.msg("|/Mammoo affixes a diamond coated gauntlet, hefts a gilded sword, and stares at you wickedly with his golden eyes.")
			self.caller.msg("|mMammoo|n says: Well that's a shame. But... your corpse will make a wonderful addition to my horde.")
			self.caller.tags.add("letsfight")
			self.caller.execute_cmd('fight')
			return
		else:
			self.caller.msg("|/Mammoo looks at you confused before letting out a roaring laugh.")
			self.caller.msg("Mammoo backhands you, sending you flying across the room slamming into a pile of gold.")
			self.caller.msg("You lose %d hp." % (int(self.caller.db.hp * .5)))
			self.caller.db.hp -= int(self.caller.db.hp * .5)
			self.caller.msg("|mMammoo|n says: I will not suffer madness, take yourself back to the Island House of R'lyeh if you are one of theirs. The mad have no place nor welcome here.")
			return

class getmammoo(default_cmds.MuxCommand):
	key = "get mammoo"
	auto_help = False
	def func(self):
		self.caller.msg("|/Mammoo grabs you by the neck easily lifting you high off the ground.")
		self.caller.msg("|mMammoo|n says: As though I were some coin on the ground for you to just pick up. You belong on the Island of the Madness with R'lyeh, but I think I'll add you to my horde instead.")
		self.caller.msg("Mammoo's golden eyes flash and you turn to solid gold.")
		self.caller.msg("|/|rWhat tragic fate, you spend the rest of eternity as another golden statue in Mammoo's horde.|n|/You have brought shame to yourself and your family.")
		self.caller.db.deathcount += 1
		self.caller.db.hp = int(self.caller.db.maxhp * .5)
		self.caller.db.mp = int(self.caller.db.maxmp * .5)
		self.caller.db.gold -= int(self.caller.db.gold * .2)
		results = search_object(self.caller.db.lastcity)
		self.caller.move_to(results[0], quiet=True, move_hooks=False)
		return

class MammooCmdSet(CmdSet):
	key = "MammooCmdSet"
	def at_cmdset_creation(self):
		self.add(chatmammoo())
		self.add(getmammoo())

class mammoo(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Mammoo's skin shines from a coating of gold dust as he struts about. He wears a mail shirt made from linked golden coins that fill the room with a soft rustling as he strolls along marveling at his horde. Long braids woven with golden coins cascade down his back and fall in his face, but never mange to obscure the golden orbs of his eyes."
		self.tags.add("specialnpc")
		self.cmdset.add_default(MammooCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:not inlist(accolades, Fortunate One)")
