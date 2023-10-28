from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class credits(default_cmds.MuxCommand):
	key = "Roll Credits"
	aliases = ["roll credits"]
	auto_help = True
	def func(self):
		monsterskilled = 0
		for i in self.caller.db.monsterstats.keys():
			monsterskilled += self.caller.db.monsterstats[i]['killed']
		questscomplete = 0
		for i in self.caller.db.quests:
			if self.caller.db.quests[i]['completed'] == "yes":
				questscomplete += 1
		target = self.caller.search("#333")
		allaccolades = ' '.join(self.caller.db.accolades)
		self.caller.msg("|/|/|004.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.|n")
		self.caller.msg("The Deeds and Accomplishments of |m%s|n." % (self.caller.key))
		self.caller.msg("You finished the game with %d max hp and %d max mp." % (self.caller.db.maxhp, self.caller.db.maxmp))
		self.caller.msg("You acquired a total of %d experience points." % (self.caller.db.exp))
		self.caller.msg("You died %d times." % (self.caller.db.deathcount))
		self.caller.msg("You killed %d unique monsters." % (len(self.caller.db.monsterstats.keys())))
		self.caller.msg("You killed %d total monsters." % (monsterskilled))
		self.caller.msg("You finished the game with %d gold." % (self.caller.db.gold))
		self.caller.msg("You had a total win/loss of %d tokens at the casino." % (self.caller.db.winnings))
		self.caller.msg("You completed %d side quests." % (questscomplete))
		self.caller.msg("You found %d treasure chests." % (len(self.caller.db.chests)))
		self.caller.msg("You earned the following accolades: %s." % (', '.join(self.caller.db.accolades)))
		if self.caller.tags.get("soulofthemadgod"):
			self.caller.msg("You found the special ending 'Rise of the Mad God' - a Zoidberg production")
			target.db.story += "|/|/|r%s|n completed the game and released madness upon the world, this time. They died %d times doing it." % (self.caller.key, self.caller.db.deathcount)
		elif self.caller.tags.get("soulofthedragon"):
			self.caller.msg("You found the special ending 'Rebirth of the Dragon'")
			target.db.story += "|/|/|r%s|n completed the game and brought about the rebirth of the Lord Dragon, this time. They died %d times doing it." % (self.caller.key, self.caller.db.deathcount)
		elif self.caller.tags.get("soulofthethief"):
			self.caller.msg("You found the special ending 'A Thieves Tale'")
			target.db.story += "|/|/|r%s|n completed the game and straight up thieved their way to victory, this time. They died %d times doing it." % (self.caller.key, self.caller.db.deathcount)
		elif self.caller.tags.get("dragonfiend"):
			self.caller.msg("You found the special ending 'Dragon Fiend'")
			target.db.story += "|/|/|r%s|n completed the game and allied themselves with the Lord Dragon, this time. They died %d times doing it." % (self.caller.key, self.caller.db.deathcount)
		elif self.caller.tags.get("kindofajerk", category="ending"):
			self.caller.msg("You allowed a demon goddess to posses your body and rule over the world. WTF yo?!?!?!?! The peasants are NOT pleased.")
			target.db.story += "|/|/|r%s|n completed the game and sacrificed themselves allowing evil to take over the world. What a jerk. They died %d times doing it.|/" % (self.caller.key, self.caller.db.deathcount)
		else:
			self.caller.msg("You found the 'regular' ending of the game. You should be kinda proud, it's actually hard to not end up going down one of the other paths. Good job on not finding any of the hidden stuff in the game?")
			target.db.story += "|/|/|r%s|n completed the game without mucking about with all the side quest stuff, this time. I mean really, just because some yahoo spent TWO YEARS of their life making this game was no reason that this player felt the NEED to go and actually check out all the extra stuff. They just speed ran it, to hell with the carefully articulated details, plot lines, character and story arcs. They played the game how THEY wanted. They died %d times doing it. Which wasn't nearly enough." % (self.caller.key, self.caller.db.deathcount)
		self.caller.msg("|004.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.|n")
		self.caller.msg("|/Your deeds and accomplishments will be recorded forever in the Book of Heroes. Make sure to stop into the Storyroom when you start over and read about yourself.")
		answer = yield("Would you like to read your Monster Journal one last time?|/|cY|nes, |cN|no")
		if answer.lower() in ["y", "yes"]:
			monlist = ""
			for i in self.caller.db.monsterstats.keys():
				monlist = monlist + "|m" + i + "|n Defeated: " + str(self.caller.db.monsterstats[i]['killed']) + ". " + "Desc: " + self.caller.db.monsterstats[i]['desc'] + "|/"
			self.caller.msg("|/" + monlist)
		yield("|/|GPress enter, or any button I guess, to start over. Live your life how you want, I'm not your boss.|n|XDid you know that Laszlo Cravensworth was in this game? And you can fight him!|n")
	#RESET PLAYER
		if self.caller.tags.get("kindofajerk", category="ending"):
			self.caller.tags.remove("kindofajerk", category="ending")
		if self.caller.tags.get():
			for i in self.caller.tags.get():
				self.caller.tags.remove(i)
		self.caller.db.desc = "An adventurer."
		self.caller.db.hp = 10
		self.caller.db.mp = 2
		self.caller.db.maxhp = 10
		self.caller.db.maxmp = 2
		self.caller.db.lvl = 1
		self.caller.db.exp = 0
		self.caller.db.gold = 10
		self.caller.db.tokens = 0
		self.caller.db.winnings = 0
		self.caller.db.bank = 0
		self.caller.db.defense = 2
		self.caller.db.attack = 2
		self.caller.db.equipatt = 0
		self.caller.db.equipdef = 0
		self.caller.db.shielddef = 0
		self.caller.db.battlespells = []
		self.caller.db.overworldspells = []
		self.caller.db.locations = []
		self.caller.db.chests = []
		self.caller.db.lastcity = "#7121"
		self.caller.db.deathcount = 0
		self.caller.db.weaponequipped = "none"
		self.caller.db.armorequipped = "none"
		self.caller.db.shieldequipped = "none"
		self.caller.db.monsterstats = {}
		self.caller.tags.add("beginning")
		self.caller.db.accolades = []
		self.caller.db.quests = {}
		del self.caller.db.bathhouse
		del self.caller.db.docktimer
		for i in self.caller.contents:
			if not i.key == "Monster Journal":
				i.delete()
		self.caller.msg("|/...as you float in the black void of endless eternity you hear a voice.")
		self.caller.msg("|mBlakhal0|n says: Hello child of fire and destiny, there are many paths to walk. Let's see if you can find another one.")
		self.caller.msg("Your soul is pulled from this place and sent hurtling back to the world.")
		results = search_object("#2")
		yield 5
		self.caller.msg("Game Written and Directed by: Blakhal0")
		yield 1
		self.caller.msg("Produced by: Blakhal0")
		yield 1
		self.caller.msg("Best Significant Other: LadySqrrl")
		yield 1
		self.caller.msg("Executive Producer: variableLabel")
		yield 1
		self.caller.msg("Director of Photography: Blakhal0")
		yield 1
		self.caller.msg("Grip: Blakhal0")
		yield 1
		self.caller.msg("Foley Artist: Blakhal0")
		yield 1
		self.caller.msg("Wardrobe: Blakhal0")
		yield 1
		self.caller.msg("Visual Effects: Blakhal0")
		yield 1
		self.caller.msg("Casting Director: Blakhal0")
		yield 1
		self.caller.msg("Costume Design: Blakhal0")
		yield 1
		self.caller.msg("Editors: Blakhal0")
		yield 1
		self.caller.msg("Production Designer: Blakhal0")
		yield 1
		self.caller.msg("Music Supervisor: Blakhal0")
		yield 1
		self.caller.msg("Unit Production Supervisor: Blakhal0")
		yield 1
		self.caller.msg("Stunts: Blakhal0, Ralph the Wonder Llama")
		yield 1
		self.caller.msg("Craft Services: Blakhal0")
		yield 1
		self.caller.msg("Llama Provider: Lay-a-way Llamas of the Midwest - A Venezuelan Concern.")
		yield 1
		self.caller.msg("Title Design: Blakhal0")
		yield 1
		self.caller.msg("Llama Safety Supervisor: Teddy 'Don't Touch My *&$^#*@ Chicken Fingers' Larough")
		yield 1
		self.caller.msg("~=Special Thanks=~")
		yield 1
		self.caller.msg("The entire Peppercon Crew")
		yield 1
		self.caller.msg("PoliteAuthority and Zappy for doing whatever 'Docker' is and putting this game out on the tubes.")
		yield 1
		self.caller.msg("Everyone that sacrificed their time so I could make this game.")
		yield 1
		self.caller.msg("Kevin Smith and Jay Mewes")
		yield 1
		self.caller.msg("Whoever it was that made the call to give the Platypus a venomous spike.")
		yield 1
		self.caller.msg("Griatch")
		yield 1
		self.caller.msg("All the folks that helped me in the Evennia Discord")
		yield 1
		self.caller.msg("Everyone* on the Peppercon Discord")
		yield 1
		self.caller.msg("*probably")
		yield 1
		self.caller.msg("**I mean odds are at least one of you is a little sketchy")
		yield 1
		self.caller.msg("***so like maybe not that person, but the rest of you are cool.")
		yield 1
		self.caller.msg("****I'm not saying like all 'hey forget that chump/chumpette', I'm just saying, you know, Thank you.")
		yield 1
		self.caller.msg("The End")
		yield 3
		self.caller.msg("Signed: Richard M. Nixon|/Intergalactic Chief Lizard Person Representative to Planet Earth 18-B")
		yield 2
		self.caller.msg("Dictated but not read.")
		yield 4
		self.caller.msg("You should go watch Rubber if you haven't already. It's a great movie.")
		yield 1
		self.caller.move_to(results[0], quiet=True, move_hooks=True)
		return


class RollCreditsCmdSet(CmdSet):
	key = "RollCreditsCmdSet"
	def at_cmdset_creation(self):
		self.add(credits())

class endcredits(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The game's over you can stop looking at everything looking for hints... Or can you?|/I'm just messing with you, you can.|XOR CAN YOU???!?!?!?!??!?!? Find the 21 secret ducks.|n"
		self.cmdset.add_default(RollCreditsCmdSet, permanent=True)
		self.locks.add("drop:false()")