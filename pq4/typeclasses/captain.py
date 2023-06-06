from evennia import default_cmds, CmdSet, search_object, search_tag
import typeclasses.locations as locations
from typeclasses.objects import DefaultObject

class chatcaptain(default_cmds.MuxCommand):
	key = "talk captain"
	aliases = ["Talk Captain", "Talk captain", "talk Captain" ]
	auto_help = True
	def func(self):
		shipcaptain = search_tag("captain").filter(db_location=self.caller.location)
		target = shipcaptain[0]
		if self.caller.location.key in ["Port of Giose"]:
			self.caller.msg("|/|m%s|n says: Ye can no be using traveling magics on the islands, they do move about too much for it to work. Aye, we do be heading back to mainland. If ye be ready, we can take ye. No charge, you paid for the whole trip up front you see." % (target.key))
			answer = yield("Return to the mainland? |gY|nes, |gN|no")
			if answer.lower() in ["y", "yes"]:
				self.caller.msg("|/|m%s|n says: Then climb aboard, we do be setting sail as we speak!" % (target.key))
				results = search_object("#7054")
				self.caller.db.lastcity = "#7054"
				self.caller.move_to(results[0], quiet=True, move_hooks=True)
				return
			else:
				self.caller.msg("|/|mShip Captain|n says: Aye, be no worry to me when we leave. Come back round when ye be ready.")
				return
		else:
		#Get list of locations the captain will go.
			islands = []
		#Make a list of the maps player has
			for i in self.caller.contents:
				if i.tags.get("map"):
				#Map location name list
					islands.append(i.db.locationname)
		#Check if the player has no maps
			if not islands:
				self.caller.msg("|/|m%s|n says: It do appear that you don't have any maps to guide the way. The seas do be mysterious and the islands... well they tend to not be staying where you last left them. That's why you do be needing a map. The maps, they're made on and of the islands themselves. They WANT to go back to the islands. If you do be knowing how to read them they be reliable to lead the way even if the island do no be where it last was." % (target.key))
				self.caller.msg("|m%s|n says: I have a ship to sail. When you get your hands on a map bring it to me and I'll take you there, for a small fee." % (target.key))
				return
		#Tell the player their options
			else:
				self.caller.msg("|/|m%s|n says: Aye, ye do be wanting to sail the seas? Well, let's take a look at your maps." % (target.key))
				self.caller.msg("|m%s|n says: Ahhh yes, it looks like you've got some maps, humm, let's see here, you've got maps for:" % (target.key))
				for i in islands:
					self.caller.msg(i.title())
				answer = yield("|m%s|n says: Where do you want to be going?" % (target.key))
			#Check if the player answer is one of their map locations
				if not answer.lower() in islands:
					self.caller.msg("%s thumbs through the maps.|/|m%s|n says: You do no be having a map for %s. Do no be wasting my time making up places." % (target.key, target.key, answer.lower().title()))
					return
			#Check if the captain sails there
				elif answer.replace(" ", "").lower() not in target.db.locations:
					self.caller.msg("|/|m%s|n says: My apologies, but I do no sail those seas. You be needing a different captain at a different port for that adventure." % (target.key))
					return
			#Collect money and travel
				else:
				#Check if the player is a poor
					if self.caller.db.gold < 50:
						self.caller.msg("|/|m%s|n says: I can no be paying the crew with good intentions. Passage will cost you 50 gold, no matter where we do go. Come back when you've got the gold." % (target.key))
						return
					self.caller.msg("|/|m%s|n says: There do be the unpleasantness of the fee. I can no be paying the crew with good intentions. Passage will cost you 50 gold, no matter where we do go." % (target.key))
					answertwo = yield("Pay the fee? |cY|nes, |cN|no.")
					if answertwo.lower() in ["y", "yes"]:
						self.caller.db.gold -= 50
						travelto = getattr(locations, answer.replace(" ", "").lower()).location
						self.caller.db.lastcity = travelto
						self.caller.msg("|/|m%s|n says: Well then, let's do be setting sail! MAKE READY THE SHIP YOU SCURVY BILGE RATS!!! We do be off for adventure...." % (target.key))
						self.caller.msg("You climb on board and watch as the crew races back and forth, heaving lines and unfurling canvas. The ship lurches forward as you head out to sea.")
						self.caller.msg("|/ ")
						yield 2
						self.caller.msg("|/Days pass, waves crash, and you arrive at your destination.")
						results = search_object(travelto)
						self.caller.move_to(results[0], quiet=True, move_hooks=True)
						return
					else:
						self.caller.msg("|/|m%s|n says: The crew do no work for free. Come back when you're ready to part with some of that gold." % (target.key))
						return

class CaptainCmdSet(CmdSet):
	key = "CaptainCmdSet"
	def at_cmdset_creation(self):
		self.add(chatcaptain())

class captain(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The Captain looks up from a manifest, adjusts his hat, and shouts a curse at a sailor that appears to be slacking off."
		self.db.locations = []
		self.tags.add("captain")
		self.tags.add("specialnpc")
		self.cmdset.add_default(CaptainCmdSet, permanent=True)
		self.locks.add("get:false()")