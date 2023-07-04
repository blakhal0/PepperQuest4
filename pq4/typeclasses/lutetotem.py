from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random

class lutetotemcmd(default_cmds.MuxCommand):
	key = "use totem"
	aliases = ["Use Totem", "Use totem", "use Totem"]
	auto_help = True
	def func(self):
		if not "Seraphin" in self.caller.db.monsterstats.keys():
			self.caller.msg("|/T:Haydn's Practice(modified)")
			self.caller.msg("M:1/26")
		#Command me
			self.caller.msg("_F_c||:=B:||=E^B=F||=B^F||")
		#I will say whatever you desire
			self.caller.msg("_A||^e_A||:_B:|| ||=d=E=f||^e^G=E^d^F=e^F_d||=f_c_e||=F^F=d_A_d^F||")
		#But I never tell the truth
			self.caller.msg("^E_e^d||_A||^B^F=e^F_d||^d^F||:_B:|| ||^d^G^F||^d_d_e^d^G||")
			answer = yield("|/What am I?")
			if "lyre" in answer.lower():
				self.caller.msg("|/The persimmons begin to leak a blood red juice, running down the lutes, forming a pool at the base of the tree. A creature with wild blue hair arises from the pool, slowly strumming a black lute. Searing eyes snap open immediately focusing on you, peering through you.")
				self.caller.msg("|/|mSeraphin|n says: Have you come to feed my tree with your life? Surely if you seek me, you seek death.")
				yield 3
				results = search_object("#10028")
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				self.caller.tags.add("letsfight")
				self.caller.execute_cmd('fight')
			else:
				self.caller.msg("|/There is a sudden and intense tightness around your neck. You find yourself hoisted into the air, feet dangling, choking, clawing at the invisible rope around your neck for breath your vision begins to fade. Right before you pass out you feel yourself drop to the ground with a thud.")
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

class LuteTotemCmdSet(CmdSet):
	key = "LuteTotemCmdSet"
	def at_cmdset_creation(self):
		self.add(lutetotemcmd())

class lutetotem(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A tall black tree with red leaves and ripe persimmons. From the branches, hanging by nooses, are dozens lutes."
		self.db.defeateddesc = "The totem is destroyed."
		self.cmdset.add_default(LuteTotemCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:tag(vanya)")
		self.db.get_err_msg = "|/|r*pop* AAHHHHHH!!! Son of a gun that is heavy!!! You throw your back out trying to lift it.|n"
		self.db.monster = "Seraphin"
	def return_appearance(self, looker):
		if not looker:
			return ""
		if self.db.monster in looker.db.monsterstats.keys():
			desc = self.db.defeateddesc
		else:
			desc = self.db.desc
		return desc