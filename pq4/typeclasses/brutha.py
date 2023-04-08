from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class chatbrutha(default_cmds.MuxCommand):
	key = "talk brutha"
	aliases = ["Talk Brutha", "Talk brutha", "talk Brutha" ]
	auto_help = True
	def func(self):
		if self.caller.tags.get("brotherbrutha"):
			self.caller.msg("There's no one by that name here to talk to.")
			return
		if self.caller.tags.get("omthemighty") and self.caller.location.key == "Temple of Small Gods":
			self.caller.msg("|/|mBrutha the Eighth Prophet of Om|n says: Welcome! I suppose we all owe you a debt of gratitude.")
			self.caller.msg("|mOm the Great and Mighty|n thunders: NO YOU DON'T, %s WAS JUST DOING AS THEIR GOD COMMANDED. QUIT BEING SO NICE TO PEOPLE." % (self.caller.key.upper()))
			self.caller.msg("|mBrutha the Eighth Prophet of Om|n says: *Ahem* Om apparently, in his omnipotence, has a dissenting opinion. But I thank you.")
			self.caller.msg("|mOm the Great and Mighty|n thunders: WELL I DON'T.")
			self.caller.msg("*zaaAAAAAPPP!* You hair stands on end as a bolt of lighting strikes near your feet.")
			self.caller.msg("|mOm the Great and Mighty|n thunders: THERE, I DIDN'T SMITE YOU. THAT'S THE BEST YOU'RE GETTING.")
			if not "Savior of Om the Mighty" in self.caller.db.accolades:
				self.caller.db.accolades.append("Savior of Om the Mighty")
			if not "spark" in self.caller.db.battlespells:
				self.caller.db.battlespells.append('spark')
				self.caller.msg("|mBrutha the Eighth Prophet of Om|n says: I think we can do a little better than NOT killing %s, don't you?" % (self.caller.key))
				self.caller.msg("|mOm the Great and Mighty|n thunders: FINE. I GUESS. PREPARE TO RECIEVE MY GIFT.")
				self.caller.msg("Your entire body tingles as you feel electricity flow into you.")
				self.caller.msg("|mOm the Great and Mighty|n thunders: YOU MAY NOW CALL UPON A TINY BIT OF MY MIGHT TO SMITE ENEMIES DURING BATTLE, IN MY NAME OF COURSE.")
				self.caller.msg("You have learned the Spark spell.")
			self.caller.msg("|mOm the Great and Mighty|n thunders: GO FORTH AND LAY LOW THE ENEMIES YOU FACE IN MY NAME AND WITH MY POWER!")
			self.caller.msg("|mBrutha the Eighth Prophet of Om|n says: It was very nice to see you again. Do take care and stop back anytime!")
			self.caller.msg("|mOm the Great and Mighty|n thunders: BEAT IT! GET TO SMITING. I HAVEN'T GOT ALL DAY TO SIT AROUND GABBING WITH THE LIKES OF YOU. I'M A VERY BUSY AND IMPORTANT GOD.")
			self.caller.msg("As you walk away another lightning bolt flashes, striking were you were just standing.")
			return
		elif "Om the Mighty" not in [obj.key for obj in self.caller.contents] and not self.caller.tags.get("omthemighty") and self.caller.location.key == "Gadoz Beach":
			self.caller.msg("|/|mBrutha|n says: Well, yes I suppose that is important... No, I still don't think smiting them with lightning is the answer... Because that's ALWAYS your answer. Oh, hello there. Don't worry, I'm not talking to myself. They just call me Mad Brutha, I'm not really mad.")
			self.caller.msg("|mBrutha|n says: I used to be a monk at the church in PaiPri, but when the new King and Queen were raised, they ran us all out. Now I've got nowhere to go and no one to go there with, aside from this one-eyed turtle here. His name is Om, he seems to think he's a god.")
			self.caller.msg("|mOm|n says: I AM A GOD!!! FEEL MY WRATH!!")
			self.caller.msg("A small static shock tickles your ear.")
			self.caller.msg("|mBrutha|n says: He's just a small god. Claims he needs to get back to his temple in the forest. I believe in him, but every time I go into the forest to try and find it, I get all turned around.")
			self.caller.msg("|mOm|n says: You couldn't find your own|/Brutha muffles the turtle with a finger and gets bit for his trouble.|/|mOm|n says: ...with a map and both hands!")
			answer = yield("|mBrutha|n says: Will you take him to the temple in the forest? He can be quite unpleasant at times, but you really should help people, or turtles that claim to be gods, when you can. It's just the right thing to do.|/|cY|nes, |cN|no.")
			if answer.lower() in ["y", "yes"]:
				self.caller.msg("|/|mBrutha|n says: Oh, that's very kind of you. Now Om, you be nice, %s seems to be a nice person." % (self.caller.key))
				om_proto = {
				"key": "Om the Mighty",
				"typeclass": "typeclasses.npc.omthemighty",
				"location": self.caller
				}
				spawn(om_proto)
				self.caller.msg("Brutha hands the one-eyed turtle to you.")
				self.caller.msg("|/|mOm|n says: Well, what are we waiting for. Get me to my temple you slow witted biped.|/You feel a small shock on your backside.")
				self.caller.msg("|mBrutha|n says: I wish you well on your travels, stop back again if you're in the area!|/Brutha goes back to staring out into the bay.")
				return
			elif answer.lower() in ["n", "no"]:
				self.caller.msg("|/|mBrutha|n says: Well, I can't really blame you there. He's a bit foul mouthed and quite rude. If you change your mind, I've got nowhere else to go.|/Brutha goes back to staring out into the bay.")
				return
			else:
				self.caller.msg("|/|mBrutha|n says: Are you possessed by a spirit? I think you're speaking in tongues. And they call me mad.|/Brutha goes back to staring out into the bay.")
				return
		elif "Om the Mighty" in [obj.key for obj in self.caller.contents] and not self.caller.tags.get("omthemighty") and self.caller.location.key == "Gadoz Beach":
			self.caller.msg("|/|mBrutha|n says: No luck finding the temple huh? I searched everywhere except the very far south east of the forest and I could never find it either. Don't feel bad.|/Brutha goes back to staring out into the bay.")
			return
		elif self.caller.tags.get("omthemighty") and self.caller.location.key == "Gadoz Beach":
			self.caller.msg("|/|mBrutha|n says: Oh, you found the temple and returned Om? I guess he wasn't just a delusional little turtle. Perhaps I'll go visit now that I've got somewhere to go. Thank you for that!")
			return
		else:
			return

class BruthaCmdSet(CmdSet):
	key = "BruthaCmdSet"
	def at_cmdset_creation(self):
		self.add(chatbrutha())

class brutha(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A tall, wide shouldered, slightly plump man in a rough brown robe stands on the sand staring into the Vahvuus Bay. He appears to be talking to himself."
		self.tags.add("specialnpc")
		self.cmdset.add_default(BruthaCmdSet, permanent=True)
		self.locks.add("get:false()")