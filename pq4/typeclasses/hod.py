from evennia import default_cmds, CmdSet, search_object, search_tag
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn


class chathod(default_cmds.MuxCommand):
	key = "talk hod"
	aliases = ["Talk Hod", "Talk hod", "talk Hod"]
	auto_help = True
	def func(self):
	#already completed the mission
		if self.caller.tags.get("allseeing"):
			self.caller.msg("|/|mHod|n says: I thank you for returning the all seeing eyes of the blind god. There is nothing more I require of you. Make good use of the gifts I have bestowed upon you.")
			return
	#has all of the eyes
		elif self.caller.tags.get("righteye") and self.caller.tags.get("lefteye") and self.caller.tags.get("centereye"):
			self.caller.tags.remove("righteye")
			self.caller.tags.remove("lefteye")
			self.caller.tags.remove("centereye")
			self.caller.tags.add("allseeing")
			self.caller.db.accolades.append('Savior of the Eyeless God')
			self.caller.db.battlespells.append('whoosh')
			for i in self.caller.contents:
				if i.key in ["Right Eye of Hod", "Left Eye of Hod", "Center Eye of Hod"]:
					i.delete
			self.caller.msg("|/|mHod|n says: I see you are victorious! See what I did there? Oh, I did it again. HAHAHAHAHA!")
			self.caller.msg("|mHod|n says: Now give me those!")
			self.caller.msg("You watch in third person as Hod snatches his all seeing eyes from your grasp.")
			self.caller.msg("|mHod|n says: That's so much better. Oh right, lets see here how do I do this again.")
			self.caller.msg("Hod waves his hands and your sight returns, you carefully poke at your eye sockets finding pleasant resistance when your fingers press on your eyes.")
			self.caller.msg("|mHod|n says: Let it never be said I am not a generous god. I bestow upon you the spell of Swoosh so that you may strike your opponents with unseen wind.")
			self.caller.msg("|mHod|n says: I also grant you a slight amount of my all seeing sight. Some things that are hidden from most will be easily found by you.")
			self.caller.msg("|mHod|n says: Go forth and lay low your enemies in my name.")
			return
	#has some of the eyes and somehow managed to escape the maze.
		elif self.caller.tags.get("righteye") or self.caller.tags.get("lefteye") or self.caller.tags.get("centereye"):
			self.caller.msg("|/|mHod|n says: *sniff sniff* You again? But you don't have all my eyes? How'd you get out of there. I smell a filthy cheating rat!")
			self.caller.msg("|mHod|n says: Get back down there, oh almost forgot.")
			self.caller.msg("*ShhluuuPOP, ShhluuuPOP*|/You scream in agonizing pain as Hod gouges out your eyes.")
			self.caller.msg("|mHod|n says: I was gentle last time, that's what you get for not finishing the job! AAAandd a BOOT!!")
			self.caller.msg("You scream as you fall down a flight of steps and land with a thud.")
			results = search_object("#7955")
			self.caller.move_to(results[0], quiet=True, move_hooks=True)
			return
	#has no eyes
		else:
			self.caller.msg("|/|mHod|n says: What, who, AHHHHH!! Who's there?")
			self.caller.msg("|m%s|n says: Umm no one? Yeah.... My name is No One." % (self.caller.key))
			self.caller.msg("|mHod|n says: Ah ah ah! Nope, I know that trick. Just because I can't see doesn't mean I'm an idiot. You're still dealing with a god here, I'll smite the whole temple to make sure I get you! Now tell me your name.")
			self.caller.msg("|m%s|n says: *Sigh* It's %s." % (self.caller.key, self.caller.key))
			self.caller.msg("|mHod|n says: Well, %s, it's nice to meet you. In case you haven't figured it out, I'm in a bit of a bind here." % (self.caller.key))
			self.caller.msg("|mHod|n says: I'm Hod The Blind God, *gesturing at his face* so named because of the whole no eyes thing I got going on.")
			self.caller.msg("|m%s|n says: You don't say. Aren't gods supposed to be all seeing?" % (self.caller.key))
			self.caller.msg("|mHod|n says: Har-de-har-har, yes smart mouth. And I was, until someone stole my three magic eyes. Without those, I can't see. If I can't see, my followers can't see. Well, at least not through my eyes. They could still see through their own if they'd just open their eyes. But, they are an absurdly dedicated group.")
			self.caller.msg("*CRASH*")
			self.caller.msg("|mHod|n says: *Sigh* Bunch of wandering idiots. WATCH WHERE YOU'RE GOING!")
			self.caller.msg("|mMonks|n: Yes my god! We trust in your guidance to lead the path!!")
			self.caller.msg("|mHod|n says: Idiots. Anyways, I don't know for sure who took them, but I'm pretty sure they're down in the labyrinth below the temple. Seems they wanted to play a prank on me.")
			self.caller.msg("|m%s|n says: Oh sure, why wouldn't they be. What is it with you people and labyrinths? Why can't you just have a storage room? Perhaps with a stout lock, Huh? But nooooooo always gotta have a horrible labyrinth filled with monsters and traps. 'Many of you will die but that is a sacrifice I am willing to accept.'" % (self.caller.key))
			self.caller.msg("|mHod|n says: When you're alive as long as we are, you get bored and need a project.")
			self.caller.msg("|mHod|n says: So how about it? You gonna help me out?")
			answer = yield("Accept the mission to find and return Hod's three eyes? |gY|nes, |gN|no.")
			if answer.lower() in ["y", "yes"]:
				self.caller.msg("|/|mHod|n says: Excellent. Come closer, let me get the feel of your face.")
				self.caller.msg("You approach Hod.")
				self.caller.msg("|m%s|n says: So here's the thing, don't freak out, I'm going to have to blind you. See, only my disciples can enter the labyrinth.")
				self.caller.msg("|m%s|n says: YOU DON'T THINK MAYBE YOU SHOULD HAVE BROUGHT THAT UP EARLIER??!?!?!?!" % (self.caller.key))
				self.caller.msg("You struggle in a futile effort as Hod grips your head in massive hands.")
				self.caller.msg("|mHod|n says: Oh come on buddy, it's not that big of a deal. You're going to be fine. I have total confidence in you. Now just hold still here...")
				self.caller.msg("*ShhluuuPOP, ShhluuuPOP*|/You scream in agonizing pain as Hod gouges out your eyes.")
				self.caller.msg("|mHod|n says: Don't be so dramatic. Now, just stumble over innnnn that direction, I think...*SHOVE*")
				self.caller.msg("You scream as you fall down a flight of steps and land with a thud.")
				results = search_object("#7955")
				self.caller.move_to(results[0], quiet=True, move_hooks=True)
			else:
				self.caller.msg("|/|mHod|n says: Well, if you're feeling generous and you've got some free time later help a god out yeah? Think it over.")
				self.caller.msg("|mHod|n says: Watch out for those idiot monks on the way out.")
				return
			return

class HodCmdSet(CmdSet):
	key = "HodCmdSet"
	def at_cmdset_creation(self):
		self.add(chathod())

class hod(DefaultObject):
	def at_object_creation(self):
		self.db.desc = ""
		self.db.tagdesc = ""
		self.db.tagname = "allseeing"
		self.tags.add("specialnpc")
		self.cmdset.add_default(HodCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/Whaaa? Whooo, who's there? What do you want? Where did you go?"
	def return_appearance(self, looker):
		if not looker:
			return ""
		desc = str()
		if looker.tags.get(self.db.tagname):
			desc = self.db.tagdesc
		else:
			desc = self.db.desc
		return desc