from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class mezapraycmd(default_cmds.MuxCommand):
	key = "pray"
	auto_help = True
	def func(self):
		contentslist = []
		for i in self.caller.contents:
			contentslist.append(i.key)
		if "PyrettaBlaze" in contentslist or "pyrettablaze" in self.caller.db.battlespells:
			self.caller.msg("|/|mThe Mother of Forests|n says: You have already received my gift. Do not be a greedy child.")
			results = search_object("#1617")
			self.caller.move_to(results[0], quiet=True, move_hooks=True)
			return
		if "Booplesnoot" in self.caller.db.monsterstats.keys():
			self.caller.msg("|/|mMeza|n sternly says: I told you not to hurt my beloved Booplesnoots, and like a petulant child you refused to listen. A mother must be loving but also harsh when her children do not listen, and now you must accept your punishment.")
			self.caller.db.hp = 1
			self.caller.db.mp = 0
			self.caller.db.gold = 0
			for i in self.caller.contents:
				if i.key in ["Spicy Herb", "Fixer Flask", "Magic Dust", "Sage Elixir", "Restoring Ruby", "Yorkshire Tea"]:
					i.delete()
			self.caller.msg("Vines erupt from the ground entangling you, preventing you from moving.|/One vine strikes you in the heart and you feel your life drain away, all but 1 hp has been absorbed.")
			self.caller.msg("Another vine strikes you in the temple, you feel your magic flow from you. You are bereft of mp.")
			self.caller.msg("Small animals scurry up the vines and begin searching you, you see them carrying off your healing and magic restoring items.")
			self.caller.msg("A raccoon waddles over, climbs up the vines, and begins rummaging through your pockets. It takes all of your gold.")
			self.caller.msg("The vines retract, but not before giving you a sharp whack on the backside.")
			self.caller.msg("|mMeza|n says: I believe the consequences fit the offense, nothing I have taken from you cannot be regained with hard work.")
		else:
			self.caller.msg("|/|mMeza|n warmly says: I am very proud of you, you showed kindness and a gentle hand to my beloved Booplesnoots. You've made your mother very proud.")
		self.caller.msg("|mMeza|n says: You completed the trials required to obtain the knowledge I possess, I give you a great power of destruction that has been used time and time again to destroy my forests. Use it wisely.")
		tof_proto = {
		"key": "PyrettaBlaze",
		"typeclass": "typeclasses.items.pyrettablazespellbook",
		"location": self.caller
		}
		spawn(tof_proto)
		self.caller.msg("|/You receive a spell book.")
		self.caller.msg("|/|mMeza|n says: Now, return to the world and make your mother proud with acts of kindness and wisdom. My vines can reach anywhere, and I will be watching.")
		results = search_object("#1617")
		self.caller.move_to(results[0], quiet=True, move_hooks=True)
		return

class MezaCmdSet(CmdSet):
	key = "MezaCmdSet"
	def at_cmdset_creation(self):
		self.add(mezapraycmd())

class altarofmeza(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A gigantic tree, covered with different fruits and berries, home to many many animals, stands before you. As you look at it, you begin to notice that it bears a striking resemblance to a woman, head turned towards the sky, body turning with arms raised into the air"
		self.cmdset.add_default(MezaCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|rYou wrap your arms around the giant tree and pull with all your might, an apple drops and bonks you on the head.|n"