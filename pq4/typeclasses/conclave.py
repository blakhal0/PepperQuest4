from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class conclavechat(default_cmds.MuxCommand):
	key = "Address Conclave"
	aliases = ["address conclave"]
	auto_help = True
	def func(self):
		if "Thieves Jewel" in [obj.key for obj in self.caller.contents]:
			self.caller.tags.remove("mugger")
			self.caller.tags.add("kingofthieves")
			self.caller.db.accolades.append("The King of Thieves")
			target = self.caller.search("Thieves Jewel", candidates=self.caller.contents, quiet=True)
			target[0].delete()
			#after retrieving jewel stuff
			self.caller.msg("|/You toss the Thieves Jewel on the table and watch as mouths and eyes open wide watching it tumble and roll to a stop.")
			self.caller.msg("|m%s|n says: I think this is what you were looking for yeah?" % (self.caller.key))
			self.caller.msg("The room is silent until Friday clears their throat and wraps on the table. All hail %s! Saviour of the thieves!" % (self.caller.key))
			self.caller.msg("The thieves erupt in applause and victory cheers. Many toasts are made and drinks are had.")
			self.caller.msg("By the end of the night votes are tallied and Friday has been crowned the new Ladrone.")
			return
		elif self.caller.tags.get("kingofthieves"):
			self.caller.msg("|/The conclave is over, Friday might have something to say to you, after that best to get round to finding a way to Kharro. Maybe those pirates will help.")
			return
		else:
			#Danni One Eye, Hammer Harold, Jill Glass, Ruby, Friday
			self.caller.tags.add("mugger")
			self.caller.msg("|/Friday stands up and addresses the conclave.")
			self.caller.msg("|mFriday|n says: Ok, we all know why we're here. The Thieves Jewel was in Ladrone's possession when she was captured, as is the Ladrone's right to do. But that puts us in a pinch, we can't elect a new Ladrone without it.")
			self.caller.msg("|mHammer Harold|n says: Damn fool thing to do, carrying that around.")
			self.caller.msg("|mDanni One Eye|n says: A soft tongue will be used when referring to our leader, past or present, unless you need some help softening it?")
			self.caller.msg("Danni One Eye uses both eyes to stare down Hammer.|/Hammer Harold makes a slight gesture and nods.")
			self.caller.msg("|mFriday|n says: Our sources in Castle Ardismouf tell us the Thieves Jewel is locked up in the Treasury Room and absolutely no one is being let into the castle. Word is King Vauquelin is planning on selling it. We obviously can't let that happen.")
			self.caller.msg("|mRuby|n says: Why not wait for the literal boat load of gold and steal both at the same time?")
			self.caller.msg("|mJill Glass|n says: Not a bad idea, under normal circumstance, but we can't wait. We have egg on our face and we need to strike back NOW!")
			self.caller.msg("|mFriday|n says: Yes, Jill is right, as I was saying we don't have time to wait, we need to send someone capable TODAY. I recommend we send %s, they're not from here, guards don't know their face. It's not a huge advantage, but it's better than nothing." % (self.caller.key))
			self.caller.msg("The Den explodes.")
			self.caller.msg("|mHammer Harold|n says: Youv gon right round the bend, absolutely mental!")
			self.caller.msg("|mJill Glass|n shouts: Over my bloated rotting corpse will I trust this to them.")
			self.caller.msg("Ruby leans over and whispers in Jill's ear, her eyes light up.")
			self.caller.msg("|mJill Glass|n says: After conferring with the esteemed Ruby, I agree with Friday. Send the expendable scapegoat....errr honorable and talented %s." % (self.caller.key))
			self.caller.msg("|mFriday|n says: Excellent, that's three for, no need for further voting as that's majority. Decision made. %s will retrieve the Thieves Stone! HUZZAH!!!" % (self.caller.key))
			self.caller.msg("You stand there, shocked, but really are you surprised?")
			self.caller.msg("Friday pulls you aside.")
			self.caller.msg("|mFriday|n says: Look, I know you can do this, any one of us gets within arrow distance of that castle and we're dead. First step to getting into the castle is getting into the upper district. I hearby deputize you as an official thief, you're allowed to |cMug|n people now. Keep it civil, you're looking for someone that would fit in in the upper district. Give em a good mugging and put on their clothes. There's rumor of a secret passage into the castle in one of the mansions, apparently the King has, uhhh, special guests brought in through that route. After that, you're on your own. Use your wits and stealth well.")
			self.caller.msg("|mFriday|n says: Good luck!")
			return


class ConclaveCmdSet(CmdSet):
	key = "ConclaveCmdSet"
	def at_cmdset_creation(self):
		self.add(conclavechat())

class conclave(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Thieves from all around Tormey are gathered at the table, waiting for the conclave to begin. |cAddress Conclave|n to get the meeting started."
		self.cmdset.add_default(ConclaveCmdSet, permanent=True)
		self.locks.add("get:false()")