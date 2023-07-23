from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class fixpipe(default_cmds.MuxCommand):
	key = "Fix Pipe"
	aliases = ["fix pipe"]
	auto_help = True
	def func(self):
		if self.caller.db.bathhouse['pipe'] == "fixed":
			self.caller.msg("|/The pipe is already fixed. It requires no further maintenance.")
			return
		self.caller.msg("|/You look on the wall, there appears to be some kind of instructions next to a large wrench.")
		self.caller.msg('touch instructions; echo "right" > instructions; echo "right" > instructions; echo "left left" >> instructions; cat instructions >> instructions >/dev/null 2>&1; [ "$(wc -l < instructions)" -ne 2 ] && (echo "right right right left right" >> instructions) ||| (echo "right left right left left" >> instructions)')
		answer = yield("You pick up the wrench and place it on the pipe, what series of turns do you make to fix the pipe?")
		if answer.lower() == "right left left right left right left left":
			self.caller.db.bathhouse['pipe'] = "fixed"
			self.caller.msg("|/You turn the giant wrench several times, the dripping stops.")
			self.caller.msg("You've fixed the pipe.")
		else:
			self.caller.msg("|/You turn the giant wrench several times, the dripping turns into a high pitched hiss.")
			self.caller.msg("A gigantic orange and black snake comes shooting out of the pipe, mouth open, fangs dripping, and latches directly onto your face. I guess this is where they keep their snakes.")
			self.caller.msg("|/|rWhat tragic fate, you've been killed by a Giant Pipe Snake. You spend the next few months being digested and turned into snake poop.|n|/You have brought shame to yourself and your family.")
			self.caller.db.deathcount += 1
			self.caller.db.hp = int(self.caller.db.maxhp * .5)
			self.caller.db.mp = int(self.caller.db.maxmp * .5)
			self.caller.db.gold -= int(self.caller.db.gold * .2)
			results = search_object(self.caller.db.lastcity)
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return

class PipeCmdSet(CmdSet):
	key = "PipeCmdSet"
	def at_cmdset_creation(self):
		self.add(fixpipe())

class bustedpipe(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "You look up at the pipe, instructions are tacked to the wall next to a giant wrench. Maybe you want to |cFix Pipe|n?"
		self.cmdset.add_default(PipeCmdSet, permanent=True)
		self.locks.add("get:false()")