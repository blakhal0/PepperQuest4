from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class readeternitybook(default_cmds.MuxCommand):
	key = "read tales of eternity"
	aliases = ["Read Tales of Eternity"]
	auto_help = True
	def func(self):
		self.caller.msg("|/Reaching out you grasp the book, opening it with great effort.|/You flip through the pages, unable to decipher the writings until you find a page you can read.")
		self.caller.msg("The story on the pages suddenly filling your mind as you watch your life being retold, action by action in incredible detail.|/Frantically you flip through the other pages, the other stories, the other paths your life could have taken. Straining to make sense of the enigmatic writing, waiting for the images to flood your mind. But nothing happens.")
		self.caller.msg("You turn back to the pages describing your life and flip to the last page... images begin to flood your mind.")
		yourstuff = []
		for i in self.caller.contents:
			yourstuff.append(i.key)
		if self.caller.tags.get("soulofthemadgod"):
			self.caller.msg("|/You reach down, black writing tentacles wrapping around Pyretta's throat as you squeeze and snap her neck.")
			self.caller.msg("Dissonant whispers fill the air as you raise your head, black blood dripping, and begin to chant.")
			self.caller.msg("The fabric of reality begins to tear once again returning you to the temple Balheim.")
			self.caller.msg("The tears begin to grow as bulging eyes and writing masses of madness begin to pour out into this world.|/You hear the screams as your maddening whispers begin to fill the minds of all in this world.")
			self.caller.msg("|m%s|n says: leT tHE GreAT oLd oNEs reIgN oNCE mOre!!" % (self.caller.key))
			self.caller.msg("Madness spreads across the lands, flaying the minds of the feeble humans. One by one you destroy the gods and goddesses of the world until only madness remains.")
		elif self.caller.tags.get("soulofthedragon"):
			self.caller.msg("|/You hesitate, drawing back your final blow as you look down at the ruined form of Pyretta.")
			self.caller.msg("Something in the back of your mind flickers and the beast that was once your sister pains you.")
			self.caller.msg("You swing down with great force, crushing her skull in a sickening thwack.")
			self.caller.msg("Focusing your power, a doorway opens as you step back into the temple in Balheim.")
			self.caller.msg("Sorrow fills you.")
			self.caller.msg("Dragons breath bursts from your mouth, melting the bone and metals that made this temple.")
			self.caller.msg("|m%s|n says: We shall rid this world of such evil. With an iron fist crush it." % (self.caller.key))
			self.caller.msg("You watch as you slay every living thing in your path, raise an unstoppable army, bring gods and goddesses to heel and swear loyalty to you and finally take your rightful seat, the Dragon Throne, at the top of a volcano from which you rule.")
		elif self.caller.tags.get("soulofthethief"):
			self.caller.msg("|/Freed from the horrible grips of the enigma armor you stand, alone, and cry.")
			self.caller.msg("|m%s|n says: All of this, all of this loss. This greed for power." % (self.caller.key))
			self.caller.msg("Gently you lift the ruined face of Pyretta.")
			self.caller.msg("|m%s|n says: I am sorry sister. I am sorry, but this will not be our end." % (self.caller.key))
			self.caller.msg("You cast StolenHeart and steal Nuri's soul from the body of Pyretta.")
			self.caller.msg("You open a doorway back to your world and step through.")
			self.caller.msg("|m%s|n says: I will find a way to bring you back. I will find a way to cleanse this corrupted spirit from our blood." % (self.caller.key))
			self.caller.msg("After decades of searching, sneaking, thieving, you finally find the magic you need.|/Using the last grains of the Sands of Time you cast yourself and your sister back in time to try once more.")
		elif self.caller.tags.get("dragonfiend"):
			self.caller.msg("|/A voice fill your mind.")
			self.caller.msg("|mLord Dragon|n says: This is a good start. Now, we made a promise and we must keep our word to be a good ruler.")
			self.caller.msg("You cast a healing spell on Pyretta, bringing her back from the brink of death. As she begins to rise you grab her arms and snap them at the elbow, ripping off the lower half of her limbs.")
			self.caller.msg("With a burst of dragons breath you sear the torn and bleeding charred flesh as the demon screams in agony.")
			self.caller.msg("Searching around you find some thick chain and wrap it around her neck, using fire to melt the links together into a collar.")
			self.caller.msg("|mLord Dragon|n says: Excellent, this should due until we can get a mage to make something proper. Now, let's go get the new decoration for our halls.")
			self.caller.msg("You murmur in agreement as a new power fills you. You open a portal back to Balheim and step through. Dragging the ruins of Pyretta behind you.")
			self.caller.msg("You watch as you slay every living thing in your path, raise an unstoppable army, bring gods and goddesses to heel and swear loyalty to you and finally take your rightful seat, the Dragon Throne, at the top of a volcano from which you rule.")
		elif self.caller.tags.get("kindofajerk", category="ending"):
			self.caller.msg("|/The Demon Goddess Pyretta, now posessing your body, turns to Nuri.")
			self.caller.msg("|mThe Demon Goddess Pyretta|n says: Now now, don't cry little sister.")
			self.caller.msg("|mNuri|n growls: No!!!!!!")
			self.caller.msg("Nuri screams, the scream growing in volume until it is an earth quaking roar.")
			self.caller.msg("A wicked and determined smile grows on her face as she reaches into her pocket, golden sand falling from her hand.")
			if "Sands of Time" in yourstuff:
				self.caller.msg("You reach into your pack, quickly finding the Sands of Time. The string holding it closed loosened, just enough for a tiny hand.")
			self.caller.msg("|mNuri|n says: You won't steal this from me. I don't care how many times it takes.")
			self.caller.msg("That quaking laughter starts again as she throws the glimmering sands of time into the air.|/Pyretta screams in horror as reality begins to dissolve.")
			self.caller.msg("The last thing you see is Nuri's face twisted in a mad laughing smile.")
		else:
			if "Sands of Time" in yourstuff:
				self.caller.msg("|/Looking down at the ruined form of what was once your sister, tears begin to run down your face.")
				self.caller.msg("|m%s|n says: I will not let this be my fate. I will not let this be!" % (self.caller.key))
				self.caller.msg("You pull out the Sands of Time, watching the golden grains trickle through your fingers. A sickly smirk tugs at the corners of your lips.")
				self.caller.msg("|m%s|n says: I CONTROL THE VERY SANDS OF TIME AND THIS WILL NOT BE MY FATE!" % (self.caller.key))
				self.caller.msg("You throw the Sands of Time into the air, laughing madly.")
				self.caller.msg("|m%s|n says: One more time around. This time without making the same mistakes." % (self.caller.key))
			else:
				self.caller.msg("|/Looking down at the ruined form of what was once your sister, tears begin to run down your face.")
				self.caller.msg("|m%s|n says: What good is power when it corrupts everything you love." % (self.caller.key))
				self.caller.msg("The denizens of the Demon Plane begin to gather, surrounding you. At first you welcome their wrath, awaiting the killing blow.")
				self.caller.msg("|mDemons|n: Only at the end can you find the beginning. Only at the end can you find the beginning.")
				self.caller.msg("A demon in black robes steps forward plunging a clawed hand into Pyretta's chest, ripping out a malformed heart. Taking a claw it dips it into the heartblood of the demon goddess and draws a symbol on your forehead.")
				self.caller.msg("The denizens of the demon plane all prostrate themselves as a new and horrible power fills you.")
				self.caller.msg("Your skin darkens, cracking as the last remnants of humanity are burnt from you.")
				self.caller.msg("The demons begin to chant and roar as their new deity is born from the end of the last.")
		self.caller.msg("|/As your vision clears the book slams closed and you feel yourself being pulled through the warping time and space.")
		results = search_object("#12993")
		self.caller.move_to(results[0], quiet=True, move_hooks=False)
		return


class EternityBookCmdSet(CmdSet):
	key = "EternityBookCmdSet"
	def at_cmdset_creation(self):
		self.add(readeternitybook())

class talesofeternity(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A large thick leather bound book. A glimmering infinity symbol, broken and mended in multiple places, adorns the front."
		self.cmdset.add_default(EternityBookCmdSet, permanent=True)
		self.locks.add("get:false()")