from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from random import randint


class obeliskcmd(default_cmds.MuxCommand):
	key = "Use Obelisk"
	aliases = ["use obelisk"]
	auto_help = True
	def func(self):
		topstone = ["|/   _____|/   \   /|/   -\-/-|/     v ", "|/     ^|/    / \|/   /___\ ", "|/     ^|/   -/-\-|/   /___\ ", "|/   _____|/   \   /|/    \ /|/     v"]
		middlestone =["     ^|/     =", "     =|/     v"]
		bottomstone = ["   _____|/   \   /|/   -\-/-|/     v ", "     ^|/    / \|/   /___\ ", "     ^|/   -/-\-|/   /___\ ", "   _____|/   \   /|/    \ /|/     v"]
		topstonepos = randint(0,3)
		middlestonepos = randint(0,1)
		bottomstonepos = randint(0,3)
		while 1 > 0:
			self.caller.msg("|b" + topstone[topstonepos] + "|n")
			self.caller.msg("|g" + middlestone[middlestonepos] + "|n")
			self.caller.msg("|y" + bottomstone[bottomstonepos] + "|n")
			answer = yield("|/|/Action? |cA|nctivate the Obelisk, |cR|neconfigure Obelisk, |cQ|nuit")
			if answer.lower() in ("a", "activate"):
				if topstonepos == 2 and middlestonepos == 0 and bottomstonepos == 0:
					self.caller.msg("|/|gThe Obelisk symbols glow vibrantly. A prismatic light surrounds you and you are lifted into the air.|n")
					results = search_object("#9533")
					self.caller.move_to(results[0], quiet=True, move_hooks=True)
					break
				elif topstonepos == 1 and middlestonepos == 1 and bottomstonepos == 0:
					self.caller.msg("|/The Obelisk symbols glow vibrantly. Fire rains down from the sky, burning you.")
					if self.caller.db.hp > 1:
						damage = self.caller.db.hp * .5
					if self.caller.db.hp <= 1:
						damage = 0
					self.caller.msg("You lost %d hp." % (damage))
					self.caller.db.hp -= damage
					continue
				elif topstonepos == 3 and middlestonepos == 1 and bottomstonepos == 0:
					self.caller.msg("|/The Obelisk symbols glow vibrantly. A torrent of rain falls from the sky, soaking you to the bone.")
					continue
				else:
					self.caller.msg("|/|rThe Obelisk does nothing.|n")
					continue
			elif answer.lower() in ("r", "reconfigure"):
				stoneanswer = yield("Which stone do you want to change? |cT|nop, |cM|niddle, |cB|nottom")
				if stoneanswer.lower() not in ("t", "m", "b", "top", "middle", "bottom"):
					self.caller.msg("|/|rFrustrated, you begin to bang on the Obelisk in rage screaming and clattering like an ape slamming your fists up and down.|n")
					continue
				directionanser = yield("|cR|night or |cL|neft")
				if directionanser not in ("r", "l", "right", "left"):
					self.caller.msg("|/|rFrustrated, you begin to bang on the Obelisk in rage screaming and clattering like an ape slamming your fists up and down.|n")
					continue
				if directionanser.lower() in ("r", "right"):
					if stoneanswer.lower() in ("t", "top"):
						topstonepos += 1
						if topstonepos > 3:
							topstonepos = 0
					if stoneanswer.lower() in ("m", "middle"):
						middlestonepos += 1
						if middlestonepos > 1:
							middlestonepos = 0
					if stoneanswer.lower() in ("b", "bottom"):
						bottomstonepos += 1
						if bottomstonepos > 3:
							bottomstonepos = 0
				if directionanser.lower() in ("l", "left"):
					if stoneanswer.lower() in ("t", "top"):
						topstonepos -= 1
						if topstonepos < 0:
							topstonepos = 3
					if stoneanswer.lower() in ("m", "middle"):
						middlestonepos -= 1
						if middlestonepos < 0:
							middlestonepos = 1
					if stoneanswer.lower() in ("b", "bottom"):
						bottomstonepos -= 1
						if bottomstonepos < 0:
							bottomstonepos = 3
				continue
			elif answer.lower() in ("q", "quit"):
				self.caller.msg("|/You step away from the Obelisk.")
				break
			else:
				self.caller.msg("|/Frustrated, you begin to bang on the Obelisk in rage screaming and clattering like an ape slamming your fists up and down.")
				break





class ObeliskCmdSet(CmdSet):
	key = "ObeliskCmdSet"
	def at_cmdset_creation(self):
		self.add(obeliskcmd())

class obelisk(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A large black obelisk stands at the edge of the inlet, slanting slightly. Various icons are carved into the three sides."
		self.cmdset.add_default(ObeliskCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "You dig at the base of the object, removing some of the dirt, then give a mighty grunt as you try to lift it. It's very heavy. You can't budge it."