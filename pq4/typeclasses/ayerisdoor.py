from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random

class enterayerisdoor(default_cmds.MuxCommand):
	key = "temple door"
	aliases = ["Temple Door", "Temple", "Door", "door", "temple", "grand doorway", "Grand Doorway", "Grand doorway", "grand Doorway"]
	auto_help = False
	def func(self):
		def dothemove():
			self.caller.msg("|/You are both wise and knowledgeable. Your request to enter has been granted.")
			results = search_object("#9897")
			self.caller.move_to(results[0], quiet=True, move_hooks=True)
			return
		def wronganswer():
			self.caller.msg("|/Wisdom and knowledge does not flow through you.")
			return
		welcomemessage = "THE GODDESS AYERIS WELCOMES THOSE WITH THE WISDOM TO SEE AND KNOWLEDGE TO UNDERSTAND"
		welcomemessage = welcomemessage.upper()
		secretmessageoptions = ["Though blind I enlighten though loose I am bound I am often in tatters and often decked with gold", "No wings but I fly No eyes but I cry Wherever I go darkness follows me", "I have lakes with no water mountains with no stone and cities with no buildings"]
		secretmessagechoice = random.choice(secretmessageoptions)
		secretmessage = secretmessagechoice.upper()
		welcomecipher = ""
		cipher = ""
		CODE = {'A':'/_\ _\ / ', 'B':'/_\ _\ \ ', 'C':'/_\ _\ _ ', 'D':'/_\ /_ / ', 'E':'/_\ /_ \ ', 'F':'/_\ /_ _ ', 'G':'/_\ /\ / ', 'H':'/_\ /\ \ ', 'I':'/_\ /\ _ ', 'J':'/=\ _\ / ', 'K':'/=\ _\ \ ', 'L':'/=\ _\ _ ', 'M':'/=\ /_ / ', 'N':'/=\ /_ \ ', 'O':'/=\ /_ _ ', 'P':'/=\ /\ / ', 'Q':'/=\ /\ \ ', 'R':'/=\ /\ _ ', 'S':'/-\ _\ / ', 'T':'/-\ _\ \ ', 'U':'/-\ _\ _ ', 'V':'/-\ /_ / ', 'W':'/-\ /_ \ ', 'X':'/-\ /_ _ ', 'Y':'/-\ /\ / ', 'Z':'/-\ /\ \ ', ' ':'/-\ /\ _ '}
		for letter in secretmessage:
			cipher += CODE[letter] + " "
		for wletter in welcomemessage:
			welcomecipher += CODE[wletter] + " "
		self.caller.msg(welcomecipher + "|/ |/")
		self.caller.msg(cipher + "|/ |/")
		answer = yield("How do you answer? ")
		if secretmessagechoice == secretmessageoptions[0]:
			if "book" in answer.lower():
				dothemove()
			else:
				wronganswer()
		elif secretmessagechoice == secretmessageoptions[1]:
			if "cloud" in answer.lower():
				dothemove()
			else:
				wronganswer()
		elif secretmessagechoice == secretmessageoptions[2]:
			if "map" in answer.lower():
				dothemove()
			else:
				wronganswer()

class AyerisDoorCmdSet(CmdSet):
	key = "AyerisDoorCmdSet"
	def at_cmdset_creation(self):
		self.add(enterayerisdoor())

class ayerisdoor(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The door to the inner sanctum of the Goddess Ayeris. Only those of the greatest wisdom may enter."
		self.tags.add("specialexit")
		self.cmdset.add_default(AyerisDoorCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|rLook, this ain't looney toons, you can't take the door.|n"