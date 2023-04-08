from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chatrctender(default_cmds.MuxCommand):
	key = "talk bartender"
	aliases = ["Talk Bartender", "Talk bartender", "talk Bartender" ]
	auto_help = True
	def func(self):
		if not "King of Thieves" in self.caller.db.accolades:
			if self.caller.tags.get("holdingcourt"):
				self.caller.msg("|/|mBartender|n says: Good to see you again, everyone took off after the meeting. Not sure where they were heading. Usually best not to ask those kinds of questions if you're happy with the number of holes you've got in your body.")
				return
			answer = yield("|/|mBartender|n says: Hello, and welcome to The Rat and Cutter. The finest establishment in Vak Dal. What can I do for you?|/The bartender stands there, waiting for a response.")
			if answer.lower() in ["vinnie", "vinnie o'neill"]:
				self.caller.msg("|/|mBartender|n says: Uh-huh, you must be the one Friday told me about. Right this way.")
				yield 2
				results = search_object("#8352")
				self.caller.move_to(results[0], quiet=True, move_hooks=True)
				return
			elif answer.lower() in ["drink"]:
				self.caller.msg("|/|mBartender|n says: Yeah, this is a bar, I can probably do that for you.|/The bartender grabs a bottle and pours you a drink.|/|mBartender|n says: Here you go.|/You tip the glass back and knock it down.")
				return
			else:
				self.caller.msg("|/|mBartender|n says: Humm, I'm not too sure about that. Probably better to ask someone that knows a bit more about that.")
				self.caller.msg("The Bartender goes back to work behind the bar.")
				return
		else:
			answer = yield("|/|mBartender|n says: Welcome, your highness.|/The Bartender grins a sly grin.|/|mBartender|n says: Always good to see you again, and welcome back to The Rat and Cutter.")
			return


class RCtenderCmdSet(CmdSet):
	key = "RCtenderCmdSet"
	def at_cmdset_creation(self):
		self.add(chatrctender())

class rnctender(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The bartender is busy attending to patrons."
		self.tags.add("specialnpc")
		self.cmdset.add_default(RCtenderCmdSet, permanent=True)
		self.locks.add("get:false()")