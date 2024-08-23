from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject
import random
from random import randint
from evennia.prototypes.spawner import spawn

class hanging(default_cmds.MuxCommand):
	key = "watch execution"
	aliases = ["Watch execution", "watch Execution", "Watch Execution"]
	auto_help = True
	def func(self):
		pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========", "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========", "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",  "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========", "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========", "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]
		if not self.caller.tags.get("ladrone"):
			self.caller.msg("|/The crowd quiets as trumpets from the castle echo through the Upper District and into the City Center.")
			self.caller.msg("A small group of soldiers push and shove a bound prisoner with a bag over their head through the rings of the Upper District and down towards Execution Square.")
			self.caller.msg("Guards shove the surging crowd back away from the gallows, occasionally giving a good clubbing to an attendee that gets a little over excited.")
			self.caller.msg("The crowd goes silent as the prisoner is led onto the gallows platform and the noose is tightened around their neck.")
			self.caller.msg("|mKing Vauquelin|n says: Good people of Vak Dal, Okefen, and all of Tormey as well as the entire continent. Today, I give you a gift. A gift of safety, security, justice.")
			self.caller.msg("|mKing Vauquelin|n says: Today we hang the so called 'Thief King' Ladrone.")
			self.caller.msg("Half the crowd erupts in cheers, shouting curses and throwing old fruit at the prisoner, the other half hisses and boo's.")
			self.caller.msg("|mKing Vauquelin|n says: BEHOLD THE FACE OF THE PERSON THAT STOLE FROM YOU!")
			self.caller.msg("The crowd gasps as the King pulls the bag off, spilling golden blonde curls around a tanned round face with a scar below the right eye.")
			self.caller.msg("Ladrone, the Thief King, is a young woman, barely into her middle years.")
			self.caller.msg("|mLadrone|n says: It is true I am a thief, I proudly admit that. I never stole from one who couldn't afford it, and those of you in the crowd that needed it know where the money went.")
			self.caller.msg("|mLadrone|n says: I have nothing more to say, get on with it.")
			self.caller.msg("The executioner pulls the lever and the trap door drops.")
			self.caller.msg("In the silence you can here the neck bones snap as Ladrone's body convulses, settles into small spasms, and finally slowly sways.")
			self.caller.msg("|mKing Vauquelin|n says: Behold the King's justice! And BE WARNED THIEVES! Your actions will not be tolerated in Tormey! See your future hanging here if you continue in your ways!")
			self.caller.msg("With the excitement and spectacle over, people begin to file out of the city, some taking to the bars and inns on their way out.")
			self.caller.tags.add("ladrone")
			self.caller.msg("As you turn to make your leave, you feel a slight tug on your coin purse.")
			self.caller.msg("Making a quick grab you find a small dirty wrist ending with a dirty hand holding a small but very sharp knife in your your grip...")
			self.caller.msg("|mSmall Thief|n says: Whoa, hehe, hey, uhh sorry, didn't know you were part of the gang.")
			self.caller.msg("|m%s|n says: What? I'm no.." % (self.caller.key))
			self.caller.msg("|mSmall Thief|n says: It's fine, there's no guards around. I'm Friday the Filcher, you can just call me Friday. You must be new to town. And you obviously are one of us, no one has EVER caught me in the act. You, uh, mind letting me go before we draw the wrong eyes?")
			self.caller.msg("Friday rubs his wrist a bit as the knife disappears down a sleeve.")
			self.caller.msg("|mFriday|n says: Look, everyone's working the crowd right now hoping to get plump before all the money leaves town but later there's going to be a gathering at the Rat and Cutter, just ask for Vinnie O'Neill, they'll sort you out.")
			self.caller.msg("Friday disappears back into the exiting crowd, moving like a viper in the grass. Doubtlessly leaving many a cut purse strings.")
			self.caller.msg("The undertakers pull up the hanging rope, dump Ladrone's corpse into a box, and begin to carry it away back up to the castle.")
		else:
			self.caller.msg("|/The hanging is over.|/What? You want to see someone else hang? Just not enough gore for you eh?|/You sick freak.")
			i = 0
			image = 0
			wrongguesses = []
			words = ["goose", "peppercon", "capsaicin", "paprika", "cayenne", "spice", "honk", "jalapeno", "goosebumps", "hooligan", "mango", "gooseberry", "duckling", "allegedly", "ostrich", "ancho", "peppers", "lobster", "chicken", "quack", "wolverine"]
			currentword = random.choice(words)
			hiddenword = "-" * len(currentword)
			while i < 1:
				positionofletter = []
				self.caller.msg(pics[image])
				if image == 6:
					self.caller.msg("|/|rYOU LOSE!!!|/There you have it you sick freak, another life ended due to your desire for death. Way to go.|n")
					break
				if hiddenword == currentword:
					self.caller.msg("|/|gCONGRATULATIONS!!|n|/The secret word was %s!" % (currentword.title()))
					status = "success"
					break
				self.caller.msg("Word: %s" % (hiddenword))
				if wrongguesses:
					self.caller.msg("Not used: %s" % (' '.join(wrongguesses)))
				option = yield("|gG|nuess a letter, |gS|nolve, |gQ|nuit")
				if option.lower() in ["q", "quit"]:
					self.caller.msg("|/You quitter.")
					break
				elif option.lower() in ["s", "solve"]:
					checkans = yield("Enter your guess: ")
					if checkans.lower() == currentword:
						self.caller.msg("|/|gCONGRATULATIONS!!|n|/The secret word was %s!" % (currentword.title()))
						status = "success"
						break
					else:
						self.caller.msg("|/|rLOL, Nope!|n")
						image += 1
						continue
				elif option.lower() in ["g", "guess"]:
					answer = yield("Enter your guess: ")
					if not answer.lower().isalpha():
						self.caller.msg("|/|rWhat are you trying to pull here? Letters only.|n")
						image += 1
						continue
					if not len(answer) == 1:
						self.caller.msg("|/|rWhat are you trying to pull here? One letter, and only one, at a time.|n")
						image += 1
						continue
					if answer.lower() in wrongguesses:
						self.caller.msg("|/|rWasn't in there the first time you guessed, still not in there.|n")
						image += 1
						continue
					if not answer.lower() in currentword:
						image += 1
						self.caller.msg("|/Lol, nope! Try again.")
						wrongguesses.append(answer.lower())
						continue
					if answer.lower() in currentword:
						self.caller.msg("|/YAY! You got one!")
						for pos, char in enumerate(currentword):
							if(char == answer.lower()):
								positionofletter.append(pos)
						for position in positionofletter:
							hiddenword = hiddenword[:position] + answer.lower() + hiddenword[position+1:]
						continue
				else:
					image += 1
					self.caller.msg("I'm not sure what you're trying to do here, but that's not one of the options.")
					continue
			if status == "success":
				reward = randint(20, 75)
				self.caller.db.gold += reward
				self.caller.msg("|/You receive a reward of %d gold!" % (reward))
				chance = randint(1, 3)
				if chance == 1:
					target = self.caller.search("Hangmans Rope", candidates=self.caller.contents, quiet=True)
					if not target:
						hmr_proto = {
						"key": "Hangmans Rope",
						"typeclass": "typeclasses.items.hangmansrope",
						"qty": 1,
						"location": self.caller
						}
						spawn(hmr_proto)
					else:
						target[0].db.qty += 1
					self.caller.msg("You find a piece of Hangmans Rope and put it in your inventory.")
				return

class HangingCmdSet(CmdSet):
	key = "HangingCmdSet"
	def at_cmdset_creation(self):
		self.add(hanging())

class hangingevent(DefaultObject):
	def at_object_creation(self):
		self.db.desc = ""
		self.cmdset.add_default(HangingCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:false()")
