from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject

class talkghost(default_cmds.MuxCommand):
	key = "Talk Ghost"
	aliases = ["talk Ghost", "talk ghost", "Talk ghost"]
	auto_help = True
	def func(self):
		if not self.obj.access(self.caller, "view"):
			self.caller.msg("There's no one by that name to talk to.")
			return
		self.caller.msg("|/You near the edge of the water as one of the spirits makes an attempt at escape.")
		self.caller.msg("Ethereal and translucent a ghostly hand stretches out, claw-like, towards you.")
		self.caller.msg("You squint your eyes, is it asking for help or trying in vain to attack?")
		self.caller.msg("Low gutteral sounds escape the spectral form's empty mouth making your hair stand on end.")
		self.caller.msg("As it finally nears gaining solid purchase on the wet sand, a gigantic head swings down snatching the ghost up and throwing it into the air landing back in the turbulent lake with a splash and wail.")
		answer = yield("|/You stand watching, conflicted, unsure if you should help these trapped ghosts or leave them to their, perhaps, deserved fate.|/Fight the goose monster? |gY|nes, |gN|no")
		if answer.lower() in ["y", "yes"]:
			self.caller.msg("|/You think to yourself 'I'm not really sure if those ghosts deserve my help, but I'll be damned if I'm going let a goose get all sassy in my presence.'.")
			if self.caller.db.weaponequipped.lower() == "none":
				self.caller.msg("You crack your knuckles and stretch your shoulders.")
			else:
				self.caller.msg("You grip your %s tightly." % (self.caller.db.weaponequipped))
			self.caller.msg("|/|m%s|n says: Hey, goose! HONK HONK HONK HONK HONK!!!" % (self.caller.key))
			yield 1
			self.caller.tags.add("letsfight")
			self.caller.execute_cmd('fight')
		elif answer.lower() in ["n", "no"]:
			self.caller.msg("|/'To hell with them. They obviously deserve their fate.' you think to yourself.|/You spit in the lake and give the ghosts a two finger goodbye.")
			self.caller.db.monsterstats["Honkiamat"] = {"killed": 0, "desc": "The physical manifestation of hate and vitriol in buoyant and feathery form."}
			return
		else:
			self.caller.msg("|/Unable to come to a determination, you decide to think about it for a while.")
			return

class TalkGhostCmdSet(CmdSet):
	key = "TalkGhostCmdSet"
	def at_cmdset_creation(self):
		self.add(talkghost())

class hellionghost(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A face twisted into grotesque masks of anger and hatred, with eyes that blaze with a fiery intensity, the ghost looks up at you."
		self.cmdset.add_default(TalkGhostCmdSet, permanent=True)
		self.tags.add("specialnpc")
		self.locks.add("get:false()")
		self.locks.add("view:monnotdef(Honkiamat)")