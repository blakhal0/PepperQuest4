from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject
import random
from random import randint

pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========", "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========", "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",  "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========", "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========", "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]

class hangman(default_cmds.MuxCommand):
	key = "hangman"
	auto_help = True
	def func(self):
		i = 0
		image = 0
		wrongguesses = []
		words = ["goose", "peppercon", "capsaicin", "paprika", "cayenne", "spice", "honk", "jalapeno"]
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
			if option.lower() in ["s", "solve"]:
				checkans = yield("Enter your guess: ")
				if checkans.lower() == currentword:
					self.caller.msg("|/|gCONGRATULATIONS!!|n|/The secret word was %s!" % (currentword.title()))
					status = "success"
					break
				else:
					self.caller.msg("|/|rLOL, Nope!|n")
					image += 1
					continue
			if option.lower() in ["g", "guess"]:
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
		if status == "success":
			reward = randint(10, 40)
			self.caller.db.gold += reward
			self.caller.msg("|/You receive a reward of %d gold!" % (reward))
			return

class HangmanCmdSet(CmdSet):
	key = "HangmanCmdSet"
	def at_cmdset_creation(self):
		self.add(hangman())

class hangmangame(DefaultObject):
	def at_object_creation(self):
		self.db.desc = ""
		self.cmdset.add_default(HangmanCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:false()")