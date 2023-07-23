from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class changetemp(default_cmds.MuxCommand):
	key = "Adjust Temperature"
	aliases = ["adjust temperature"]
	auto_help = True
	def func(self):
		self.caller.msg("|/Looking at the giant boiler, you see three dials, a red dial, a green dial, and a blue dial, each one goes from 0 - 245")
		controls = {'rdial':245, 'gdial':236, 'bdial':66}
		dial = ""
		while 1 > 0:
			self.caller.msg("|/|rRed Dial|n - %d" % (controls['rdial']))
			self.caller.msg("|gGreen Dial|n - %d" % (controls['gdial']))
			self.caller.msg("|bBlue Dial|n - %d" % (controls['bdial']))
			answer = yield("|/Which dial do you want to adjust?|/|rR|ned, |gG|nreen, |bB|nlue, |cQ|nuit")
			if answer.lower() in ["quit", "q"]:
				self.caller.msg("|/You step away from the boiler controls.")
				break
			if answer.lower() not in ("red", "r", "green", "g", "blue", "b"):
				self.caller.msg("You look around for a %s dial, but you don't see one." % (answer))
				continue
			if answer.lower() in ["red", "r"]:
				dial = "rdial"
			if answer.lower() in ["green", "g"]:
				dial = "gdial"
			if answer.lower() in ["blue", "b"]:
				dial = "bdial"
			colorvalue = yield("|/What value?|/0-245")
			if not colorvalue.isnumeric() or int(colorvalue) > 245:
				self.caller.msg("|/|r!!ERROR: Invalid value!!|n")
				continue
			else:
				controls[dial] = int(colorvalue)
			if 188 <= controls['rdial'] <= 245 and 66 <= controls['gdial'] <= 120 and 66 <= controls['bdial'] <= 245:
				#Magenta\Red\Orange
				self.caller.msg("The boiler screeches, red hot rivets ping across the room.|/*BOOOOOM*")
				self.caller.msg("|/|rWhat tragic fate, you died in a boiler explosion, just like that one creepy fortune cookie said you would.|n|/You have brought shame to yourself and your family.")
				self.caller.db.deathcount += 1
				self.caller.db.hp = int(self.caller.db.maxhp * .5)
				self.caller.db.mp = int(self.caller.db.maxmp * .5)
				self.caller.db.gold -= int(self.caller.db.gold * .2)
				results = search_object(self.caller.db.lastcity)
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				break
			elif 66 <= controls['rdial'] <= 245 and 236 <= controls['gdial'] <= 245 and 66 <= controls['bdial'] <= 78:
				#Yellow\Light Green
				self.caller.db.bathhouse['temp'] = "cold"
				self.caller.msg("|/The boiler is not producing any heat.")
				yield 1
			elif 66 <= controls['rdial'] <= 244 and 236 <= controls['gdial'] <= 245 and 79 <= controls['bdial'] <= 245:
				#Light Green\Light Blue
				self.caller.db.bathhouse['temp'] = "warm"
				self.caller.msg("|/The boiler is barely warm to the touch. But, not enough to take the slight chill out of the air.")
				yield 1
			elif 66 <= controls['rdial'] <= 187 and 66 <= controls['gdial'] <= 235 and controls['bdial'] == 245:
				#Light Blue\Purple
				self.caller.db.bathhouse['temp'] = "hot"
				self.caller.msg("|/Emanating from its iron belly, tendrils of steam dance in the air. The rhythmic rumbling and hissing sounds of the boiler echo a gentle and relaxing song in the room")
				self.caller.msg("Hot water and steam begin to rise into the pipes and distribute through the bathhouse.|/You step away from the boiler controls.")
				break
			else:
				self.caller.msg("|/The settings seem not to have any effect on the boiler.")
				yield 1

class TempCmdSet(CmdSet):
	key = "TempCmdSet"
	def at_cmdset_creation(self):
		self.add(changetemp())

class boiler(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The boiler stands tall, wide at the bottom narrowing at the top, constructed of tarnished copper and wrought iron, adorned with intricate patterns and engravings. There are 3 dials on the boiler, they seem to |cAdjust Temperature|n."
		self.cmdset.add_default(TempCmdSet, permanent=True)
		self.locks.add("get:false()")
