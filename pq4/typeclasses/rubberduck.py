from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chatrubberduck(default_cmds.MuxCommand):
	key = "talk rubber duck"
	aliases = ["Talk Rubber Duck"]
	auto_help = False
	def func(self):
		self.caller.msg("|/It's not one of those secret ducks you're looking for, it's just a plain old rubber duck. Sorry.")
		return

class playduck(default_cmds.MuxCommand):
	key = "play rubber duck"
	aliases = ["Play Rubber Duck"]
	auto_help = True
	def func(self):
		self.caller.msg("|/You grab the rubber ducky and give it a squeeze.")
		self.caller.msg("*SQUEEK*")
		self.caller.msg("You amuse yourself playing with the rubber ducky, dipping and diving it in the water.")
		yield 2
		self.caller.msg("|mRubber Duck|n says: So child, you return to your mother? I welcome you into my house.")
		self.caller.msg("The dubber duck melts in your hands. The steam swirling in the room, turning black as you are sucked deep into the bath.")
		self.caller.db.hp = self.caller.db.maxhp
		self.caller.db.mp = self.caller.db.maxmp
		yield 3
		self.caller.db.bathhouse = {'water':'off', 'pipe':'broken', 'temp':'cold'}
		results = search_object("#11222")
		self.caller.move_to(results[0], quiet=True, move_hooks=True)

class RubberDuckCmdSet(CmdSet):
	key = "RubberDuckCmdSet"
	def at_cmdset_creation(self):
		self.add(chatrubberduck())
		self.add(playduck())

class rubberduck(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A wonderful little yellow rubber ducky. Perfect to make any bath time fun."
		self.cmdset.add_default(RubberDuckCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/Planning on stealing a rubber duck from a nice old lady? Shame on you!"
