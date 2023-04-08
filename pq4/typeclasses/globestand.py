from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random
from random import randint

class useretortstand(default_cmds.MuxCommand):
	key = "Retort Stand"
	aliases = ["stand"]
	auto_help = True
	def func(self):
		posoptions = ["north", "south", "east", "west"]
		currentpos = random.choice(posoptions)
		currentitemtop = "nothing"
		currentitembottom = "nothing"
		targetcoin = self.caller.search("Coin", candidates=self.caller.contents, quiet=True)
		targetshoe = self.caller.search("Horseshoe", candidates=self.caller.contents, quiet=True)
		if not targetcoin and not targetshoe:
			self.caller.msg("|/You have no items that will fit onto the holding devices on the retort stand.")
			return
		while 1 > 0:
			if currentitemtop == "horseshoe" and currentpos == "south" and targetshoe[0].db.charged == "yes" and currentitembottom == "coin":
				self.caller.msg("|/The glow begins to fade from the horseshoe, transferring its light into the show globe illuminating the blue liquid.|/The light begins to focus onto the coin. Gold sweating, it begins to liquefy then reform shining with brilliance.")
				targetcoin[0].db.charged = "yes"
				targetshoe[0].db.charged = "no"
				currentitemtop == "nothing"
				currentitembottom == "nothing"
				self.caller.msg("You take the horseshoe and coin from the holders on the Retort Stand.")
				break
			elif currentitemtop == "horseshoe" and currentpos == "south" and targetshoe[0].db.charged == "yes" and currentitembottom == "nothing":
				targetshoe[0].db.charged = "no"
				self.caller.msg("|/The glow begins to fade from the horseshoe, transferring its light into the show globe illuminating the blue liquid.|/The light bounces around inside the globe, heating the liquid to boiling. The globe suddenly explodes!")
				self.caller.msg("|/|rWhat tragic fate, you have died in a laboratory explosion.|n|/You have brought shame to yourself and your family for ignoring lab safety.|/Also everyone that heard about your death assumes you were making meth. Way to go.")
				self.caller.db.deathcount += 1
				self.caller.db.hp = int(self.caller.db.maxhp * .5)
				self.caller.db.mp = int(self.caller.db.maxmp * .5)
				self.caller.db.gold -= int(self.caller.db.gold * .2)
				results = search_object(self.caller.db.lastcity)
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				break
			else:
				self.caller.msg("|/Nothing seems to be happening.")
			self.caller.msg("|/|gRetort Stand|n")
			answer = yield("The rotating clamp's spirit lines are currently pointing to the %s position and is holding %s. The stationary clamp is holding %s.|/|cC|nhange the holder position, |cP|nlace something in the holding devices, |cQ|nuit using the device." % (currentpos, currentitemtop, currentitembottom))
		#Change device direction
			if answer.lower() in ["c", "change"]:
				newpos = yield("|/The rotating clamp's spirit lines are currently pointing %s. Which position would you like to change it to?|/|cN|north, |cS|nouth, |cE|nast, |cW|nest?" % (currentpos))
				if newpos.lower() not in posoptions and newpos.lower() not in ["n", "s", "e", "w"]:
					self.caller.msg("Humm there doesn't seem to be a %s position on the device." % (newpos))
					continue
				elif newpos.lower() in ["n", "north"]:
					currentpos = "north"
					self.caller.msg("You turn the holder to north.")
					continue
				elif newpos.lower() in ["s", "south"]:
					currentpos = "south"
					self.caller.msg("You turn the holder to south.")
					continue
				elif newpos.lower() in ["e", "east"]:
					currentpos = "east"
					self.caller.msg("You turn the holder to east.")
					continue
				elif newpos.lower() in ["w", "west"]:
					currentpos = "west"
					self.caller.msg("You turn the holder to west.")
					continue
				else:
					self.caller.msg("Something went wrong.")
					continue
		#Place or remove items from the holder.
			if answer.lower() in ["p", "place"]:
				torb = yield("|/Place an item in the |cR|notating clamp on the top of the stand, or the |cS|ntationary clamp at the bottom of the stand?")
				if torb.lower() not in ["r", "rotating", "s", "stationary"]:
					self.caller.msg("|/You take a look around the stand, there's not a %s." % (torb))
					continue
			#top clamp
				if torb.lower() in ["r", "rotating"]:
					itemtop = yield("|/What do you want to place in the rotating clamp?")
					if itemtop.lower() not in ["coin", "horseshoe", "nothing"]:
						self.caller.msg("|/It doesn't look like a %s will fit in the clamp." % (itemtop))
						continue
					if itemtop.lower() == "coin":
						currentitemtop = "coin"
						if currentitemtop == currentitembottom:
							self.caller.msg("You take the coin from the stationary clamp.")
							currentitembottom = "nothing"
						self.caller.msg("You place the coin in the rotating clamp at the top of the stand.")
						continue
					if itemtop.lower() in ["horseshoe", "horse shoe"]:
						currentitemtop = "horseshoe"
						if currentitemtop == currentitembottom:
							self.caller.msg("You take the horseshoe from the stationary clamp.")
							currentitembottom = "nothing"
						self.caller.msg("You place the horseshoe in the rotating clamp at the top of the stand.")
						continue
					if itemtop.lower() == "nothing":
						if not currentitemtop == "nothing":
							self.caller.msg("You take the %s from the rotating clamp." % (currentitemtop))
							currentitemtop = "nothing"
							continue
						else:
							self.caller.msg("There's already nothing in the rotating clamp.")
							continue
			#bottom clamp
				if torb.lower() in ["s", "stationary"]:
					itembottom = yield("|/What do you want to place in the stationary clamp?")
					if itembottom.lower() not in ["coin", "horseshoe", "nothing"]:
						self.caller.msg("|/It doesn't look like a %s will fit in the clamp." % (itembottom))
						continue
					if itembottom.lower() == "coin":
						currentitembottom = "coin"
						if currentitemtop == currentitembottom:
							self.caller.msg("You take the coin from the rotating clamp.")
							currentitemtop = "nothing"
						self.caller.msg("You place the coin in the stationary clamp at the bottom of the stand.")
						continue
					if itembottom.lower() in ["horseshoe", "horse shoe"]:
						currentitembottom = "horseshoe"
						if currentitemtop == currentitembottom:
							currentitemtop = "nothing"
							self.caller.msg("You take the horseshoe from the rotating clamp.")
						self.caller.msg("You place the horseshoe in the stationary clamp at the bottom of the stand.")
						continue
					if itembottom.lower() == "nothing":
						if not currentitemtop == "nothing":
							self.caller.msg("You take the %s from the stationary clamp." % (currentitembottom))
							currentitembottom = "nothing"
							continue
						else:
							self.caller.msg("There's already nothing in the stationary clamp.")
							continue
		#Quit
			if answer.lower() in ["q", "quit"]:
				if not currentitemtop == "nothing":
					self.caller.msg("|/You take the %s out of the rotating holder and put it back in your inventory." % (currentitemtop))
				if not currentitembottom == "nothing":
					self.caller.msg("|/You take the %s out of the stationary holder and put it back in your inventory." % (currentitembottom))
				self.caller.msg("You step away from the Retort Stand.")
				break
		return


class GlobeStandCmdSet(CmdSet):
	key = "GlobeStandCmdSet"
	def at_cmdset_creation(self):
		self.add(useretortstand())

class globestand(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A tall |cRetort Stand|n looms in the corner. It has a rotating holding clamp at the top engraved with spirit lines, a show globe filled with blue liquid is attached near the middle, and a stationary clamp is at the bottom."
		self.cmdset.add_default(GlobeStandCmdSet, permanent=True)
		self.locks.add("get:false()")