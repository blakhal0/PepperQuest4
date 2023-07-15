from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random
from evennia.prototypes.spawner import spawn

class madnesscmd(default_cmds.MuxCommand):
	key = "dream"
	auto_help = False
	def func(self):
		contentslist = []
		for i in self.caller.contents:
			contentslist.append(i.key)
		if "Sands of Time" in contentslist:
			self.caller.msg("You have the sands of time")
			return
		elif "Map to Panahon" in contentslist:
			self.caller.msg("|mSpicethulu|n says: " + ''.join(random.choice((str.upper, str.lower))(char) for char in "You have what you've come for. Or is it your wish to stay here in the void with us, to sleep, to wait until we are called upon to return? No? Then be gone."))
			self.caller.msg("Your mind slams back into your body and you find yourself back in the temple.")
			return
		else:
			self.caller.tags.add("sanity")
			self.caller.msg("|/You relax, lowering your defenses, and open your mind to the whispers. They come slowly at first, then in a roaring flood. You feel your consciousness drift to another place.")
			self.caller.msg("|/Adrift in an endless darkness, have you actually moved? Or is it only your mind that is in this strange place. Enormous violet crystals float in the darkness containing tangled masses of creatures, creeping shadows jumping from one point of the crystal clusters to another. Ancient gods of mind rending horror and knowledge sleep here, sleep until it is time to awake, and they dream of madness.|/A gigantic mass of eyes and tentacles suddenly appears before you, the eyes all focus on you at once as pain grips your mind.")
			self.caller.msg("|mSpicethulu|n says: " + ''.join(random.choice((str.upper, str.lower))(char) for char in "You appear wearing the skin of the SoulEatter, but you are not the SoulEatter. Return here to the timeless void wearing the past, have you come to finish reopening the door? To wake the great old ones who sleep?"))
			answer = yield("The mass of eyes stare at you waiting your response.|/|gY|nes, |gN|no")
			if answer.lower() not in ["y", "yes", "n", "no"]:
				self.caller.msg("|mSpicethulu|n says: " + ''.join(random.choice((str.upper, str.lower))(char) for char in "Madness is my native language, but you will respond to my questions directly. Be gone."))
				self.caller.msg("Your mind slams back into your body and you find yourself back in the temple.")
				return
			elif answer.lower() in ["y", "yes"]:
				self.caller.msg("|mSpicethulu|n says: " + ''.join(random.choice((str.upper, str.lower))(char) for char in "Use care in traversing the paths of destiny, once started some cannot be undone. Return once you have what you seek and release us. Take this and be on your way."))
			elif answer.lower() in ["n", "no"]:
				self.caller.msg("|mSpicethulu|n says: " + ''.join(random.choice((str.upper, str.lower))(char) for char in "Then you return to attempt traversing the paths of time once again? Such a foolish way to perceive existence. The madness it brings does create great joy for me though. Take this and be on your way."))
			pm_proto = {
			"key": "Map to Panahon",
			"typeclass": "typeclasses.objects.panahonmap",
			"location": self.caller
			}
			spawn(pm_proto)
			self.caller.msg("|/You receive a Map to Panahon")
			self.caller.tags.remove("sanity")
			self.caller.msg("Your mind slams back into your body and you find yourself back in the temple.")
			self.caller.tags.add("pathofthesouleater")
			return
		


class CthuluAltarCmdSet(CmdSet):
	key = "CthuluAltarCmdSet"
	def at_cmdset_creation(self):
		self.add(madnesscmd())

class spicethulu(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "|/As you stare at the altar the pulsating runes begin to shift and fold until you can read 'Let the fires of chaos keep you warm, child, as you DREAM of madness.'"
		self.cmdset.add_default(CthuluAltarCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|rYou touch the black stone, tendrils of darkness begin to writhe and crawl onto and into your skin. You jerk your hand back trying to brush the inky blackness off.|n"