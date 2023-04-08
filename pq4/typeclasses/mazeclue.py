from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn


class feelcmd(default_cmds.MuxCommand):
	key = "feel"
	auto_help = False
	def func(self):
		target = self.caller.location.search("clue")
		if target.db.feel == "lefteye":
			if not self.caller.tags.get("lefteye"):
				self.caller.tags.add("lefteye")
				le_proto = {
				"key": "Left Eye of Hod",
				"typeclass": "typeclasses.objects.lefteye",
				"location": self.caller
				}
				spawn(le_proto)
				self.caller.msg("You gently pick up the Left Eye of Hod, part of your vision returns.")
				return
			else:
				self.caller.msg("You've already got the Left Eye of Hod.")
				return
		if target.db.feel == "righteye":
			if not self.caller.tags.get("righteye"):
				self.caller.tags.add("righteye")
				le_proto = {
				"key": "Right Eye of Hod",
				"typeclass": "typeclasses.objects.righteye",
				"location": self.caller
				}
				spawn(le_proto)
				self.caller.msg("You gently pick up the Right Eye of Hod, part of your vision returns.")
				return
			else:
				self.caller.msg("You've already got the Right Eye of Hod.")
				return
		if target.db.feel == "centereye":
			if not self.caller.tags.get("centereye"):
				self.caller.tags.add("centereye")
				le_proto = {
				"key": "Center Eye of Hod",
				"typeclass": "typeclasses.objects.centereye",
				"location": self.caller
				}
				spawn(le_proto)
				self.caller.msg("You gently pick up the Center Eye of Hod, part of your vision returns.")
				return
			else:
				self.caller.msg("You've already got the Center Eye of Hod.")
				return
		self.caller.msg(target.db.feel)
		return

class listencmd(default_cmds.MuxCommand):
	key = "listen"
	auto_help = False
	def func(self):
		target = self.caller.location.search("clue")
		self.caller.msg(target.db.listen)
		return

class MazeClueCmdSet(CmdSet):
	key = "MazeClueCmdSet"
	def at_cmdset_creation(self):
		self.add(feelcmd())
		self.add(listencmd())

class mazeclue(DefaultObject):
	def at_object_creation(self):
		self.db.desc = ""
		self.db.feel = "You feel around and find nothing."
		self.db.listen = "You strain to listen, but there is no sound."
		self.cmdset.add_default(MazeClueCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:false()")