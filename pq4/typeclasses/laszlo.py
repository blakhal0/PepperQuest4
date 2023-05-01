from evennia import default_cmds, CmdSet, search_object, search_tag
from typeclasses.objects import DefaultObject

# We have total dominion from here to here!


class chatlaszlo(default_cmds.MuxCommand):
	key = "talk laszlo"
	aliases = ["Talk Laszlo"]
	auto_help = True
	def func(self):
		theysay = "|mLaszlo|n says: "
		yousay = "|m" + self.caller.key + "|n says: "
		self.caller.msg("|/"+ theysay + "How about it then? What do you want?")
		self.caller.msg(yousay + "Umm, I'm uh here to find some old books that people are looking for.")
		self.caller.msg(theysay + "Surely I thought you were here to find and rescue me.")
		self.caller.msg(yousay + "Rescue? You've turned the entire staff into vampires! Why would someone be here to rescue you?")
		self.caller.msg(theysay + "Well have a seat my chap and let me tell you a story most tragic.")
		self.caller.msg(theysay + "You see I was off to the mountains with my sweet lady wife one night after a bunch of asshole villagers burnt down our hut, and I said to her, my dear, my sweet syrup pie, we should stop by the old library before we leave.")
		self.caller.msg(theysay + "I had stashed some fine erotic periodicals here and I wanted to pick them up before we were ran out of the country on account of that flapping a-hole Dragon character and his war.")
		self.caller.msg(theysay + "My fine lady wife said she would meet me here and that she absolutely wasn't going to go see her secret lover, Jesk.")
		self.caller.msg(theysay + "Apparently, she speaks the bullshit.")
		self.caller.msg(theysay + "So I get here, grab my por.. periodicals, and just when I was about to leave the entire bloody place was launched into the sky.")
		self.caller.msg(theysay + "I went outside and all that could be seen was sky, bright sunny sky. 'What kind of goat sorcery is this?' I exclaimed. The whole library was floating in the sky. It was those fucking witches, I'm sure of it.")
		self.caller.msg(theysay + "And I've been stuck here ever since. Thousands of years, trapped here. The sun is always up, and I can't leave.")
		self.caller.msg(theysay + "I stumbled into the library basement one day and I've been searching through all these documents looking for some type of spell to get me out of this donkey's bowel movement of a mess ever since.")
		self.caller.msg(yousay + "Mind if I take a look for the books I'm looking for?")
		self.caller.msg(theysay + "Couldn't possibly be bothered to give a fuck. Do what you want.")
		self.caller.msg("|/With that Laszlo goes back to reading completely ignoring you.")
		return

class lootlaszlo(default_cmds.MuxCommand):
	key = "loot laszlo"
	aliases = ["Loot Laszlo", "Loot laszlo", "loot Laszlo", "LOOT LASZLO"]
	auto_help = False
	def func(self):
		if "Laszlo Cravensworth" in self.caller.db.monsterstats.keys():
			self.caller.msg("|/|mLaszlo|n says: We already gave that a go, no need to take that ride again.")
			return
		self.caller.msg("|/|mLaszlo|n says: You must be mad as a wax banana to try that! I usually avoid the ones that are all 6's and 7's, they leave a funny aftertaste. But, if you want to die I'm not one to piss on your shoes about it, I'm a bit bored anyways. PREPAAAAARRE YOURSELF!")
		self.caller.msg("Laszlo leaps up from his seat! In a flash all you see is fangs and claws headed your direction.")
		self.caller.tags.add("letsfight")
		self.caller.execute_cmd('fight')
		return

class getlaszlo(default_cmds.MuxCommand):
	key = "get laszlo"
	aliases = ["Get Laszlo", "Get laszlo", "get Laszlo", "GET LASZLO"]
	auto_help = False
	def func(self):
		self.caller.msg("|/Laszlo leans in close to you.")
		self.caller.msg("|mLaszlo|n says: Listen, I don't know about you, but I'm very much in the mood for some sexual intercourse.")
		self.caller.msg("You rethink your idea of putting hands on the very lonely ancient vampire.")
		return

class LaszloCmdSet(CmdSet):
	key = "LaszloCmdSet"
	def at_cmdset_creation(self):
		self.add(chatlaszlo())
		self.add(getlaszlo())
		self.add(lootlaszlo())

class laszlo(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Laszlo Cravensworth, figure of myth and legend, sits upon a throne like chair in the middle of the room surrounded by books and manuscripts staring at you."
		self.tags.add("specialnpc")
		self.cmdset.add_default(LaszloCmdSet, permanent=True)
		self.locks.add("get:false()")
