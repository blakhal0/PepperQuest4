from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random

class violintotemcmd(default_cmds.MuxCommand):
	key = "use totem"
	aliases = ["Use Totem", "Use totem", "use Totem", "use violin totem", "Use Violin Totem"]
	auto_help = True
	def func(self):
		if not "M'lanchrus" in self.caller.db.monsterstats.keys():
			self.caller.msg("|/|/M:4/4")
			self.caller.msg("L:1/8")
			self.caller.msg("Q:1/4=94")
			self.caller.msg("K:E")
			self.caller.msg("[C-A,E,]C/2-[C/2-A,/2E,/2] C/2-[C/2-A,/2E,/2]C/2-[C/2-A,/2E,/2]||[C/2A,/2E,/2]z/2[B,/2G,/2D,/2]z/2 [E2C2G,2] [D-B,-F,-][F/2D/2-B,/2-F,/2-][F/2D/2-B,/2-F,/2-] [F2D2B,2F,2-]|[F/2C/2-^A,/2-F,/2-][FC-^A,-F,-][C/2-^A,/2-F,/2-] [GC-^A,-F,-][^A/2C/2-^A,/2-F,/2][B/2-C/2^A,/2] [B2-D2-B,2-G,2-] [B/2D/2-B,/2-G,/2-][D3/2-B,3/2-G,3/2-]|")
			self.caller.msg("[d/2B/2D/2-B,/2-G,/2-][d3/2B3/2D3/2-B,3/2-G,3/2-] [ecD-B,-G,-][f/2d/2D/2B,/2-G,/2]B,/2 [fdC=A,E,][e/2c/2][e/2-c/2-C/2A,/2E,/2] [e/2c/2][d/2B/2C/2A,/2E,/2][e/2-c/2-][e/2c/2C/2A,/2E,/2]|[e/2-c/2-C/2A,/2E,/2][e/2-c/2-][e/2-c/2-B,/2G,/2D,/2][e/2-c/2-] [e6c6E6C6G,6]|[=A-F-C-A,-][a/2A/2-F/2-C/2-A,/2-][A/2-F/2-C/2-A,/2-] [a/2A/2-F/2-C/2-A,/2-][A/2-F/2-C/2-A,/2-][a/2A/2-F/2-C/2-A,/2-][a/2-A/2-F/2-C/2A,/2-] [a/2A/2-F/2-=D/2-A,/2-][A/2-F/2-=D/2-A,/2-][aA-F-=D-A,-] [a/2A/2-F/2-=D/2-A,/2-][A/2-F/2-=D/2-A,/2-][aA-F=DA,-]|[a3A3-E3-C3-A,3-][g/2A/2-E/2-C/2-A,/2-][g/2-A/2E/2-C/2A,/2] [g3/2-G3/2E3/2-B,3/2-G,3/2-][g3/2A3/2E3/2-B,3/2-G,3/2][G/2-E/2B,/2-][G/2B,/2]|")
			self.caller.msg("[A-CA,-][a/2-A/2-E/2C/2A,/2-][a/2A/2-A,/2-] [a/2A/2-E/2C/2A,/2-][a/2A/2-E/2C/2A,/2-][a/2A/2-E/2C/2A,/2-][a/2A/2-E/2C/2A,/2-] [a/2A/2-F/2=D/2A,/2-][a/2-A/2-F/2=D/2-A,/2-][a/2A/2-=D/2A,/2-][a/2A/2-F/2=D/2A,/2-] [A/2-A,/2-][a/2A/2-F/2=D/2A,/2-][A/2-A,/2-][a/2-A/2-E/2-C/2-A,/2-]|[a-A-ECA,-][a/2A/2-A,/2-][a/2A/2-E/2C/2A,/2-] [a/2A/2-E/2C/2A,/2-][g/2-A/2-E/2B,/2-A,/2-][g/2A/2-B,/2A,/2-][A/2E/2-B,/2-A,/2] [g3/2-G3/2E3/2-B,3/2-G,3/2-][g3/2A3/2E3/2-B,3/2-G,3/2][G/2-E/2B,/2]G/2|[A-F-][a/2A/2-F/2-E/2-C/2-][A/2-F/2-E/2C/2] [a/2A/2-F/2-][A/2-F/2-E/2C/2][a/2A/2-F/2-E/2C/2][a/2-A/2-F/2E/2C/2] [a-A-F=D][a/2-A/2-][a/2A/2-F/2=D/2] [a/2-A/2-][a/2A/2-F/2=D/2][a/2A/2-][A/2-E/2-C/2-]|[a-A-E-C][a/2-A/2-E/2][a/2-A/2-E/2C/2] [a/2-A/2-E/2C/2][a/2A/2-E/2B,/2][g/2A/2-][g/2-A/2E/2-B,/2-] [g3/2-G3/2E3/2-B,3/2-][g3/2-A3/2E3/2-B,3/2-][g/2-G/2-E/2B,/2][g/2G/2]|")
			self.caller.msg("[A-A,-][a/2A/2-E/2C/2A,/2-][A/2-A,/2-] [a/2A/2-E/2C/2A,/2-][a/2A/2-E/2C/2A,/2-][a/2A/2-E/2C/2A,/2-][a/2A/2-E/2C/2A,/2-] [a/2A/2-F/2=D/2A,/2-][a/2-A/2-F/2-=D/2A,/2-][a/2A/2-F/2A,/2-][a/2A/2-F/2=D/2A,/2-] [A/2-A,/2-][a/2A/2-F/2=D/2A,/2-][A/2-A,/2-][a/2-A/2-E/2-C/2-A,/2-]|[aA-E-CA,-][A/2-E/2A,/2-][a/2A/2-E/2C/2A,/2-] [a/2A/2-E/2C/2A,/2-][g/2-A/2-E/2B,/2-A,/2-][g/2A/2-B,/2A,/2-][A/2E/2-B,/2-A,/2] [g2-G2-E2-B,2] [g/2G/2-E/2][f/2G/2-C/2A,/2][eGB,G,]||[g2E2-B,2-E,2-] [E/2B,/2E,/2-][a/2C/2E,/2-][g/2-B,/2-B,/2E,/2-][g/2B,/2E,/2] [f/2-C/2-A,/2-A,/2F,/2-][f3/2C3/2-A,3/2-F,3/2-] [C/2A,/2F,/2][E3/2G,3/2]||[CA,-E,]A,/2[C/2A,/2E,/2] z/2[C/2A,/2E,/2]z/2[C/2A,/2E,/2] [C/2A,/2E,/2]z/2[G,/2D,/2]z/2 E-[f/2c/2E/2-][e/2B/2E/2-]|")
			self.caller.msg("[c/2G/2E/2-][e/2B/2E/2-][f/2c/2E/2-][e/2B/2E/2-] [c/2G/2E/2-][e/2B/2E/2-][f/2-c/2E/2-][f/2e/2B/2E/2-] [c/2G/2E/2-][B/2F/2E/2-][c/2G/2E/2-][B/2F/2E/2-] [c/2G/2-E/2-][f/2c/2G/2E/2-][e/2B/2-E/2-][B/2E/2]||[C-A,-E,][C/2A,/2][C/2A,/2E,/2] z/2[C/2A,/2E,/2]z/2[C/2A,/2E,/2] [C/2A,/2E,/2]z/2[G,/2D,/2]z/2 [E-C-][f/2c/2E/2-C/2-][e/2B/2E/2-C/2-]||[c/2G/2E/2-C/2-][e/2B/2E/2-C/2-][f/2c/2E/2-C/2-][e/2B/2E/2-C/2-] [c/2G/2E/2-C/2-][e/2B/2E/2-C/2-][f/2-c/2E/2-C/2-][f/2e/2B/2E/2-C/2-] [c/2G/2E/2-C/2-][B/2F/2E/2-C/2-][c/2G/2E/2-C/2-][B/2F/2E/2-C/2-] [c/2G/2-E/2-C/2-][f/2c/2G/2E/2-C/2-][e/2B/2E/2-C/2-][E/2C/2]|")
			answer = yield("|/ABC? You tell me. With such a mess, what do I bless?")
			if "rains down in africa" in answer.lower():
				self.caller.msg("|/The strings of the violin begin to vibrate with fiendish intensity.|/The air itself begins to vibrate and shimmer, a portal opens before you and a tall thin creature clad in tattered black robes steps through, bone white violin and bow in long skinny pale hands.")
				self.caller.msg("|/|mM'lanchrus|n says: You disturb my rest? Quite foolish.")
				yield 3
				results = search_object("#10027")
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				self.caller.tags.add("letsfight")
				self.caller.execute_cmd('fight')
			else:
				self.caller.msg("|/Pain like lightning enters your mind. Your eyes go wide as you begin to scream in pain grabbing your head as you crumble to your knees. After several agonizing moments, through the sobs, you realize that the pain has subsided.")
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

class ViolinTotemCmdSet(CmdSet):
	key = "ViolinTotemCmdSet"
	def at_cmdset_creation(self):
		self.add(violintotemcmd())

class violintotem(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A large bone white violin totem stands as an altar. The bow strings drip red. There are many lines of writing on the totem."
		self.db.defeateddesc = "The totem is destroyed."
		self.cmdset.add_default(ViolinTotemCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:tag(vanya)")
		self.db.get_err_msg = "|/|r*pop* AAHHHHHH!!! Son of a gun that is heavy!!! You throw your back out trying to lift it.|n"
		self.db.monster = "M'lanchrus"
	def return_appearance(self, looker):
		if not looker:
			return ""
		if self.db.monster in looker.db.monsterstats.keys():
			desc = self.db.defeateddesc
		else:
			desc = self.db.desc
		return desc