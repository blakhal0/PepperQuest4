from evennia import default_cmds, CmdSet, search_object, search_tag
import random
from typeclasses.objects import DefaultObject


class chatbarbarian(default_cmds.MuxCommand):
	key = "talk barbarian"
	aliases = ["Talk Barbarian"]
	auto_help = True
	def func(self):
		self.caller.msg("|/|mVariable the Barbarian|n says: You shouldn't be here, this is my place and I like the way it's not crowded.")
		self.caller.msg("The colossal barbarian stands up and is in front of you in one massive stride.")
		self.caller.msg("|mVariable the Barbarian|n says: If you want to go back, I can get you back to land. You don't belong here, this is my home and I don't like trespassers.")
		answer = yield("Would you like the barbarian to send you back to the continent?|/|cY|nes, |cN|no")
		if answer.lower() in ['y', 'yes']:
			locationchoices = ['#7910', '#8184', '#7589', '#8878']
			self.caller.msg("|mVariable the Barbarian|n says: No problem, I've gotten lost a time or two back in my adventuring days also, it happens to everyone. Don't feel too bad, I'm sure you're a great adventurer.")
			self.caller.msg("The barbarian walks with you back to the edge of the island, sticks a finger in the water and holds it up into the air.")
			self.caller.msg("|mVariable the Barbarian|n says: Hummmm, let's see here, wind out of the west, no dragons in the sky, and I caught a very nice Lusca for breakfast this morning. Let's say... 60% power.")
			self.caller.msg("|m%s|n says: What do you mean..." % (self.caller.key))
			self.caller.msg("You're interrupted as the barbarian scoops you into a huge hand, winds up, and hurls you into the sky.")
			self.caller.msg("|m%s|n says: WAAAhHAhHAHAHWhahHwhahahwwooooahahwhahahwhhaaaaaaaa!!!!!" % (self.caller.key))
			self.caller.msg("*THUD*")
			results = search_object(random.choice(locationchoices))
			self.caller.move_to(results[0], quiet=True, move_hooks=True)
			return
		else:
			if "Variable the Barbarian" in self.caller.db.monsterstats.keys():
				self.caller.msg("|/|mVariable the Barbarian|n says: We've already battled, and you got to receive the gifts of the tree. There's nothing else for you to do here but annoy me. So.... go on, get.")
				return
			else:
				self.caller.msg("A worrying scowl forms across the barbarians brow.")
				self.caller.msg("|mVariable the Barbarian|n says: Then you must want a fight. Heh-heh-he. I could use some bait for fishing tomorrow.")
				yield 1
				self.caller.tags.add("letsfight")
				self.caller.execute_cmd('fight')
				return


class VariabletheBarbarianCmdSet(CmdSet):
	key = "VariabletheBarbarianCmdSet,"
	def at_cmdset_creation(self):
		self.add(chatbarbarian())

class variablethebarbarian(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "*Glug-glug-glug* 'Oh, yes that is about perfect, that bitter root really did the job!' The barbarian sets down his coconut, sloshing some of the alcohol out in the process, and grabs what looks to be a tree trunk sized octopus tentacle off a rotisserie, dips it in soy sauce, tosses some peppers in his mouth and rips a huge bite out of it.|/As the steel cable like jaw muscles flex you see waves of power wash over his already colossal form, impossibly it looks like he's a little bigger and stronger."
		self.cmdset.add_default(VariabletheBarbarianCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.db.get_err_msg = "|/Heh-heh-he, Stop! That tickles!!!"
