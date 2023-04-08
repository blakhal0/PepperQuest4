from evennia import default_cmds, CmdSet, search_object, search_tag
import typeclasses.locations as locations
from typeclasses.objects import DefaultObject

class chatkingpancha(default_cmds.MuxCommand):
	key = "talk king pancha"
	aliases = ["Talk King Pancha", "Talk King pancha", "Talk king Pancha", "Talk king pancha", "talk King Pancha", "talk King pancha", "talk king Pancha", "Talk Pancha", "Talk pancha", "talk Pancha", "talk pancha"]
	auto_help = True
	def func(self):
		if not self.caller.tags.get("thekingisdead") and not self.caller.location.key == "Cell":
			self.caller.msg("|/You approach King Pancha.")
			self.caller.msg("|m%s|n says: King and Queen Pancha, it is very nice to meet you. My name is.." % (self.caller.key))
			self.caller.msg("|mKing Pancha|n says: EEEGADS!!! A filthy PEASANT!!! WHO LET IT IN!!")
			self.caller.msg("King Pancha attempts to scramble back in his throne away from you, legs kicking and flailing in effort.")
			self.caller.msg("|mKing Pancha|n says: QUICKLY!! GET IT AWAY BEFORE IT GETS PEASANT FILTH ON ME!!!!! DON'T LET IT TOUCH YOU OR YOU'LL CATCH... THE POOR!!!")
			self.caller.msg("The King and Queen scream hysterically as the guards close in on you.")
			if not self.caller.tags.get("trapped"):
				self.caller.tags.add("trapped")
			travelto = "#7599"
			results = search_object(travelto)
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		elif self.caller.tags.get("thekingisdead") and self.caller.location.key == "Cell":
			self.caller.msg("|/Pancha sobs quietly in the dark cell.")
			self.caller.msg("|mPancha|n says: Damned peasants *sniff* taking away all my nice things *sniff* all my pretty things *sniff* chasing away the Queen *sniff* being mean to me *sniff-sniff*.")
			self.caller.msg("Why did you do this to me? Rulers are supposed to suppress the filthy peasantry, it's how you rule.*sniff*")
			self.caller.msg("Sure, maybe a few went hungry or homeless or... you know... died a little. But that's why you have so many peasants. So you can look at them and know you're better than they are.")
			self.caller.msg("Stupid spiders, they promised. THEY PROMISED!! All I had to do was get rid of the old god, and I'd get to be King forever.")
			self.caller.msg("*sniff-sniff* *sob*")
			self.caller.msg("I shut down that stupid church, ran off Father Frank, had that stupid moose Brutha sent to that village in the north where the peasants stink like fish.")
			self.caller.msg("After all the followers were gone, it was easy. Then just seal up the temple and lock up the key in the treasury.")
			self.caller.msg("*bawling*")
			self.caller.msg("AND THEN YOU RUINED IT ALLLLLLLLLL!!!")
			self.caller.msg("|/The former King begins to wail madly and thrash about. Perhaps it's best to just leave.")
			return
		else:
			self.caller.msg("There is no one here by that name to talk to.")
			return

class KingPanchaCmdSet(CmdSet):
	key = "KingPanchaCmdSet"
	def at_cmdset_creation(self):
		self.add(chatkingpancha())

class kingpancha(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The King busies himself staring into a shining gem the size of a goose egg. Brightly colored silk billows around his arms and legs, a crown that appears to be made completely of jewels and gems sits atop carefully quaffed dark hair."
		self.db.tagdesc = "The former King scratches erratically at a wild and unkempt beard. Covered in filth, clothed in rough dirty cloth, he cries and sobs mumbling unintelligibly."
		self.db.tagname = "thekingisdead"
		self.tags.add("specialnpc")
		self.cmdset.add_default(KingPanchaCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|mKing Pancha|n says: UNHAND ME THIS INSTANT YOU FILTHY PEASANT!!!"
	def return_appearance(self, looker):
		if not looker:
			return ""
		desc = str()
		if looker.tags.get(self.db.tagname):
			desc = self.db.tagdesc
		else:
			desc = self.db.desc
		return desc