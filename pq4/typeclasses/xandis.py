from evennia import default_cmds, CmdSet, search_object, search_tag
import typeclasses.locations as locations
from typeclasses.objects import DefaultObject

class chatxandis(default_cmds.MuxCommand):
	key = "talk xandis"
	aliases = ["Talk Xandis", "Talk xandis", "talk Xandis" ]
	auto_help = True
	def func(self):
		shipcaptain = search_tag("captain").filter(db_location=self.caller.location)
		target = shipcaptain[0]
		islands = []
	#Make a list of the maps player has
		for i in self.caller.contents:
			if i.tags.get("map"):
		#Map location name list
				islands.append(getattr(locations, i.db.locationname).name)
	#Check if the player has no maps
		if not islands:
			self.caller.msg("|/|mCaptain Xandis|n says: Oh, uhh, geez, this is a little embarrassing with you being the boss and all. But, ahhh, you've got no maps. I can't take you to a place we don't know how to get to, you know. Maybe if you go get some maps, well we'll set sail right as soon as you've got a destination for us.")
			return
	#Tell the player their options
		else:
			self.caller.msg("|/|mCaptain Xandis|n says: You're the boss, boss. You say, we go.")
			self.caller.msg("|mCaptain Xandis|n says: Let's just take a look here at the maps you've got. Looks like we can go to:")
			for i in islands:
				self.caller.msg(i.title())
			answer = yield("|mCaptain Xandis|n says: Well, where are we going?")
		#Check if the player answer is one of their map locations
			if not answer.lower() in islands:
				self.caller.msg("Captain Xandis thumbs through the maps.|/|mCaptain Xandis|n says: Oh gee, uhhh, %s? Yeah, you don't have a map for that place." % (answer.lower().title()))
				return
			else:
				if answer.lower() == "island of the mad":
					self.caller.msg("|/|mCaptain Xandis|n says: OH, oh, ok. Uhh, you've very brave. Or crazy, same thing I suppose. Just so you're aware, there's no real port there. We can get you there, but we have to leave as soon as we drop you off. It's too dangerous for the ship. Once you're there, you're on your own, we can't come pick you back up. It'd probably be a real good idea to stock up on healing type stuff before you go. Just my advice, do whatever you want.")
				answertwo = yield("You sure you wanna go there? |cY|nes, |cN|no.")
				if answertwo.lower() in ["y", "yes"]:
					travelto = getattr(locations, answer.replace(" ", "").lower()).location
					self.caller.msg("|/|mCaptain Xandis|n says: You got it. 'Let's go, boss has a destination!'")
					self.caller.msg("You climb on board and watch as the crew races back and forth, heaving lines and unfurling canvas. The Silver Sun lurches forward as you head out to sea.")
					self.caller.msg("|/ ")
					yield 2
					self.caller.msg("Days pass, waves crash, and you arrive at your destination.")
					self.caller.msg("|/ ")
					results = search_object(travelto)
					self.caller.move_to(results[0], quiet=True, move_hooks=True)
					return
				else:
					self.caller.msg("|/|mCaptain Xandis|n says: Change of mind eh? No problem. It's not as if I'm just like sitting here, waiting for you to make up your mind or anything.")
					self.caller.msg("Captain Xandis goes back to their tasks.")
					return

class XandisCmdSet(CmdSet):
	key = "XandisCmdSet"
	def at_cmdset_creation(self):
		self.add(chatxandis())

class xandis(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Stout, deeply tanned, with a shaved head Xandis sports tattoos of daggers on each cheek and a circlet with horns curving back over their head and flick upwards at the back. Bright orange vest over a loose flowing red shirt contrasts the sun tanned skin.|/|mXandis|n says: Hello there, I'm Captain Xandis, you can call me Captain, or Xandis, could say 'Cap', could say 'Cool Person'. You could call me 'Leader'. You can call me 'Most Gorgeous Thing You Ever Seen Before'. You can call me 'Savior'. I'll get you a list tomorrow. If you have any problems, any questions, any concerns, tell somebody else. I don't care. They'll tell me. If it's important, I'll come talk to you. You're the boss, but I'm the Captain, and it's my responsibility to get you where you want to go safely. This is the boat, the Silver Sun, it can handle anything from heavy seas to frozen water, pirates and beasties, but I'd prefer to stay where the weather's warm and the seas are calm if it's all the same to you."
		self.tags.add("captain")
		self.tags.add("specialnpc")
		self.cmdset.add_default(XandisCmdSet, permanent=True)
		self.locks.add("get:false()")