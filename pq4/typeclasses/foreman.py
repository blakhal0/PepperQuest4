from evennia import default_cmds, CmdSet, gametime
from typeclasses.objects import DefaultObject

class chatforeman(default_cmds.MuxCommand):
	key = "talk foreman"
	aliases = ["Talk Foreman", "Talk foreman", "talk Foreman" ]
	auto_help = True
	def func(self):
		if self.caller.tags.get("dockmaster"):
			self.caller.msg("|mForeman|n says: Oh, hey there. You arrived at the perfect time! We just finished up a couple days ago. Go ahead and take a look around!")
			return
		elif not self.caller.db.docktimer:
			self.caller.msg("|mForeman|n says: Oh, hey there. Gonna have to ask you to stay back, we've got an active work zone there. Wouldn't want anyone getting hurt now. I guess I should say we've got an active work zone for the moment. Funds are running a bit short. Say you wouldn't happen to have any spare coin would ya? Well, if you do it'd be just great if you could go talk to the folks putting up the funding for this, you can find them in the Brass Wolf Inn. Sure would be great for all the folks in the city if we could get the port back up and running.")
			return
		elif int(self.caller.db.docktimer) + 1200 >= int(gametime.runtime()):
			self.caller.msg("|mForeman|n says: Oh, hey there. Gotta say we sure do appreciate the extra funds! We were able to hire some extra workers and we're back on track, ahead of schedule even. Stop back a little later and don't you worry about your investment, I'll make sure that everyone is working! It's gonna look great!")
			return
		elif int(self.caller.db.docktimer) + 1200 < int(gametime.runtime()):
			self.caller.msg("|mForeman|n says: Oh, hey there. You arrived at the perfect time! We just finished up a couple days ago. Go ahead and take a look around!")
			if not self.caller.tags.get("dockmaster"):
				self.caller.tags.add("dockmaster")
			return
		else:
			self.caller.msg("Something has gone horribly wrong, let blakhal0 know there's an issue at the docks.")
			return

class ForemanCmdSet(CmdSet):
	key = "ForemanCmdSet"
	def at_cmdset_creation(self):
		self.add(chatforeman())

class foreman(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The Foreman stands tall watching over the workers, unrolling and rolling a set of blueprints occasionally hollering instructions, locations, and measurements."
		self.cmdset.add_default(ForemanCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")