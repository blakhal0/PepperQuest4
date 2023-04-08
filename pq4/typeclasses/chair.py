from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject

class haveaseat(default_cmds.MuxCommand):
	key = "sit down"
	aliases = ["Sit Down", "Sit down", "sit Down"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("holdingcourt"):
			self.caller.msg("|/|mFriday|n says: Not going to get much done sitting around on your ass.")
			return
		self.caller.msg("|/|mDanni One Eye|n says: Alright, quiet down! Let's lift up our glasses to Ladrone, a thieves thief. The King is Dead. All hail.|/|mEveryone|n: Here here!|/|mDanni One Eye|n says: Now, we all know what needs doin', we just gotta get organized on how to do it. Ideas?")
		self.caller.msg("|mJill Glass|n says: Hol up, first things first. We got a stranger in here. I know Friday vouches for ya, but who the hell are you?")
		self.caller.msg("The entire rooms turns and stares at you.")
		self.caller.msg("|m%s|n says: Uhhh, me, I'm %s, nobody important. Nope. Just here to pay my respects. I've done a few jobs, nothing anyones ever heard of I doubt because... because they don't know anything is gone. Yeah, that's right, I'm that good. hehehe, yep." % (self.caller.key, self.caller.key))
		self.caller.msg("You sweat nervously as the rest of the room looks back and forth to each other, some hands move to un-sheath knives.")
		self.caller.msg("|mDanni One Eye|n says: Good enough for me. Ol %s here caught Friday clipping purse strings, you all know that doesn't just happen." % (self.caller.key))
		self.caller.msg("|mHammer Harold|n says: Goodnuf for you is it? An that's supposed to mean somefing to the rest of us? You ain't the King, your word isn't rule.")
		self.caller.msg("*The room erupts into a quiet rabble*")
		self.caller.msg("|mRuby|n says: Hammer has a good point there, you aren't in charge. No one is.")
		self.caller.msg("|mDanni One Eye|n says: And if you'd all just settle down I'll get to that. Now we're all a bit taken back about Ladrone, but we have to keep going... I'm calling court in Tolvaj.")
		self.caller.msg("The room goes silent.")
		self.caller.msg("|mEveryone|n says: Take what you can, give nothing back!|/Glasses are raised high, tipped back, and thumped down with authority on the table.")
		self.caller.tags.add("holdingcourt")
		self.caller.msg("The thieves seated around the table push back and stand up from the table, the meeting is over without another word.")
		return

class SeatCmdSet(CmdSet):
	key = "SeatCmdSet"
	def at_cmdset_creation(self):
		self.add(haveaseat())

class chair(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "An empty seat sits at the table."
		self.cmdset.add_default(SeatCmdSet, permanent=True)
		self.locks.add("get:false()")