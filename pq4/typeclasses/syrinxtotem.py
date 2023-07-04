from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random

class syrinxtotemcmd(default_cmds.MuxCommand):
	key = "use totem"
	aliases = ["Use Totem", "Use totem", "use Totem"]
	auto_help = True
	def func(self):
		if not "Discordia" in self.caller.db.monsterstats.keys():
			self.caller.msg("|/GfG fBg_ EC fF^a_ Gd_C fEd_ EC fBe_ fEd_ Gc_f EC GBC^ Ga_g_ EC fCf EC fGd_ fEG GBb_ GBC^ fF^D EC Gb_c_ fEd_ EC fCf fF^D fEd_ EC fF^a_ Gd_C fEd_ EC fGc_ fBg_ fEd_ fg_A EC Gb_a_ Gd_C fEG fF^a_ EC GCe_ Gg_B Gg_E")
			answer = yield("|/How do you respond?")
			if any(x in answer.lower() for x in ["fcg", "f c g", "f,c,g", "f, c, g", "f c and g", "f, c, and g"]):
				self.caller.msg("|XWell smiley day to ya!|n|/The pipes emit consonant chords. A portal opens and you hear chiming as a cloaked figure steps out.")
				self.caller.msg("|/|mDiscordia|n says: You wouldn't happen to have a twin would you? I've been thinking about making a new instrument.")
				yield 3
				results = search_object("#10029")
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				self.caller.tags.add("letsfight")
				self.caller.execute_cmd('fight')
			else:
				self.caller.msg("|/The wind picks up, blowing through the bone pipes creating a dissonant cacophony. Reaching up you feel blood dripping from your nose.")
				self.caller.db.hp -= 5
				if self.caller.db.hp > 0:
					self.caller.msg("|rYou lose 5 hp|n")
				else:
					self.caller.msg("|/|rWhat tragic fate, you have fallen.|n|/You have brought shame to yourself and your family.")
					self.caller.db.deathcount += 1
					self.caller.db.hp = int(self.caller.db.maxhp * .5)
					self.caller.db.mp = int(self.caller.db.maxmp * .5)
					self.caller.db.gold -= int(self.caller.db.gold * .2)
					results = search_object(self.caller.db.lastcity)
					self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		else:
			self.caller.msg("|/The totem is destroyed.")
			return

class SyrinxTotemCmdSet(CmdSet):
	key = "SyrinxTotemCmdSet"
	def at_cmdset_creation(self):
		self.add(syrinxtotemcmd())

class syrinxtotem(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A series of bone pipes jut up from the ground, each shorter than the last with keyholes are carved into them. The holes seem to only be two sizes, one size large, one small. Occasionally the wind picks up, echoing through the pipes creating grating sounds."
		self.db.defeateddesc = "The totem is destroyed."
		self.cmdset.add_default(SyrinxTotemCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:tag(vanya)")
		self.db.get_err_msg = "|/|r*pop* AAHHHHHH!!! Son of a gun that is heavy!!! You throw your back out trying to lift it.|n"
		self.db.monster = "Discordia"
	def return_appearance(self, looker):
		if not looker:
			return ""
		if self.db.monster in looker.db.monsterstats.keys():
			desc = self.db.defeateddesc
		else:
			desc = self.db.desc
		return desc