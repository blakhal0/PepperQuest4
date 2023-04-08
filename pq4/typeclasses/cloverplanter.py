from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random
from random import randint

class usecoverplanter(default_cmds.MuxCommand):
	key = "Alembic"
	aliases = ["use alembic"]
	auto_help = True
	def func(self):
		posoptions = ["north", "south", "east", "west"]
		currentpos = random.choice(posoptions)
		currentitem = "nothing"
		targetcoin = self.caller.search("Coin", candidates=self.caller.contents, quiet=True)
		targetshoe = self.caller.search("Horseshoe", candidates=self.caller.contents, quiet=True)
		if not targetcoin and not targetshoe:
			self.caller.msg("|/You have no items that will fit onto the holding device.")
			return
		while 1 > 0:
		#Check if they've charged the horseshoe
			if not currentitem  == "nothing":
				if currentitem == "horseshoe" and currentpos == "north" and not targetshoe[0].db.charged == "yes":
					self.caller.msg("|/A drop splashes on the horseshoe, the green haze is drawn out of the alembic and into the horseshoe, it begins to glow!|/You remove the horseshoe from the holder and put it back in your inventory.")
					targetshoe[0].db.charged = "yes"
					currentitem = "nothing"
					break
				elif currentitem == "horseshoe" and currentpos == "south" and targetshoe[0].db.charged == "yes":
					self.caller.msg("|/The glow fades from the horseshoe.")
					targetshoe[0].db.charged = "no"
				else:
					self.caller.msg("|/The %s sits in the holder, nothing seems to be happening." % (currentitem))
			self.caller.msg("|/|gAlembic|n")
			answer = yield("The device is currently pointing to the %s position and is holding %s.|/|cC|nhange the holder position, |cP|nlace something in the holding device, |cQ|nuit using the device." % (currentpos, currentitem))
		#Place or remove items from the holder.
			if answer.lower() in ["p", "place"]:
				newitem = yield("|/What item do you want to place in the holder?")
				if newitem.lower() not in ["coin", "horseshoe", "horse shoe", "nothing"]:
					self.caller.msg("|/The %s doesn't seem to fit." % (newitem))
					continue
				if newitem.lower() == "nothing":
					if not currentitem == "nothing":
						self.caller.msg("You remove the %s and put it back in your inventory." % (currentitem))
					currentitem = "nothing"
					continue
				if newitem.lower() in ["coin"]:
					self.caller.msg("|/You place the coin in the holder.")
					currentitem = "coin"
					continue
				if newitem.lower() in ["horseshoe", "horse shoe"]:
					self.caller.msg("|/You place the horseshoe in the holder.")
					currentitem = "horseshoe"
					continue
		#Change device direction
			elif answer.lower() in ["c", "change"]:
				newpos = yield("|/The holding device notch is currently pointing %s. Which position would you like to change it to?|/|cN|north, |cS|nouth, |cE|nast, |cW|nest?" % (currentpos))
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
		#Quit
			elif answer.lower() in ["q", "quit"]:
				if not currentitem == "nothing":
					self.caller.msg("You take the %s out of the holder and put it back in your inventory." % (currentitem))
				self.caller.msg("You step away from the alembic.")
				break
		#Catchall
			else:
				self.caller.msg("|/Oh dear, the words you said right there %s... that was the trigger word to the emergency destruct spell protecting the lab." % (answer))
				self.caller.msg("The alembic begins to vibrate at an ever increasing speed, ultimately exploding sending shattered glass shards ripping through your body.|/You slowly bleed to death on the floor.")
				self.caller.msg("|/|rWhat tragic fate, you have died in a laboratory explosion.|n|/You have brought shame to yourself and your family for ignoring lab safety.|/Also everyone that heard about your death assumes you were making meth. Way to go.")
				self.caller.db.deathcount += 1
				self.caller.db.hp = int(self.caller.db.maxhp * .5)
				self.caller.db.mp = int(self.caller.db.maxmp * .5)
				self.caller.db.gold -= int(self.caller.db.gold * .2)
				results = search_object(self.caller.db.lastcity)
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				break
		return

class CloverPlanterCmdSet(CmdSet):
	key = "CloverPlanterCmdSet"
	def at_cmdset_creation(self):
		self.add(usecoverplanter())

class cloverplanter(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A small patch of clover flourishes inside an |cAlembic|n, a slight green haze hangs at the top and drips down the beak and onto a small holding device with a notch that appears to rotate."
		self.cmdset.add_default(CloverPlanterCmdSet, permanent=True)
		self.locks.add("get:false()")