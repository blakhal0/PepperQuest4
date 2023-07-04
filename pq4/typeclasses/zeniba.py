from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chatzeniba(default_cmds.MuxCommand):
	key = "talk zeniba"
	aliases = ["Talk Zeniba", "Talk zeniba", "talk Zeniba" ]
	auto_help = True
	def func(self):
		self.caller.msg("|/|mZeniba|n says: Ah, welcome, dear guest. May the soothing waters of our hotsprings wash away the weariness that clings to your spirit. Here, amidst the healing waters, you shall find respite from the burdens of the world. Relax, dear one, and allow yourself to be enveloped by tranquility. Your well-being is our utmost concern, and we are honored to have you grace our bathhouse with your presence.")
		answer = yield("|mZeniba|n says: Would you care to enjoy the healing waters of the bathhouse this wonderful day?|/|gY|nes, |gN|no")
		if answer.lower() in ["y", "yes"]:
			self.caller.msg("|/|mZeniba|n says: Oh, that's just wonderful. I just know you're going to feel so much better.")
			if self.caller.tags.get("seekerofknowledge"):
				self.caller.msg("|mZeniba|n says: You look like you would enjoy this. My mother gave it to me and I occasionally let extra special guests use it.")
				self.caller.msg("Zeniba hands you a rubber duck.")
				bathlocation = "#11219"
			else:
				bathlocation = "#11218"
			self.caller.msg("|mZeniba|n says: Here, right this way. Please, take as long as you desire. It's worth every minute!")
			yield 3
			results = search_object(bathlocation)
			self.caller.move_to(results[0], quiet=True, move_hooks=True)
		else:
			self.caller.msg("|/|mZeniba|n says: No? Well, there's no harm in that but I promise you're missing out on a fantastic experience. Perhaps another time we will have the honor of your patronage. Please feel free to enjoy the bathhouse at your leisure. If you have a change of mind, just let me know dear.")
			self.caller.msg("Zeniba turns her attention to another guest.")
			return

class ZenibaCmdSet(CmdSet):
	key = "ZenibaCmdSet"
	def at_cmdset_creation(self):
		self.add(chatzeniba())

class zeniba(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Zeniba exudes an aura of grace and wisdom. With her silver-grey hair meticulously styled into a tight bun atop her head, she carries herself with an air of serene authority. Her age is etched upon her face, eternally marked by the lines of experience and kindness. Dressed in flowing robes of soft, pastel hues, each garment is adorned with delicate embroidery, showcasing her attention to detail and dedication to creating a harmonious atmosphere."
		self.tags.add("specialnpc")
		self.cmdset.add_default(ZenibaCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "Zeniba steps back quickly, winds up a towel, and delivers a wicked towel snap!|/*CRRRAAAAAACK!* OUCH!!!!|/|mZeniba|n says: Ah-ah-ah. Didn't your mother ever teach you to keep your hands to yourself?"