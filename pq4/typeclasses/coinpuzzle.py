from evennia import default_cmds, CmdSet, search_object, search_tag
from random import randint
from typeclasses.objects import DefaultObject
import re

class coinproblem(default_cmds.MuxCommand):
	key = "talk ahlai"
	aliases = ["Talk Ahlai", "Talk ahlai", "talk Ahlai"]
	auto_help = True
	def func(self):
		fakecoin = randint(1,9)
		status = ""
		tries = 0
		if self.caller.tags.get("tolvaj"):
			self.caller.msg("|/|mAhlai|n says: Yeah yeah, you've already proven yourself, just go ahead on in. Oh, and don't forget you can take the |cHidden Path|n just outside Swamp Castle to get here instead of roaming all the way through that crap hole.")
			return
		self.caller.msg("|/|mAhlai|n says: So, you think you've got a bit of wit eh? A good thief needs to be quick on their head feet, not just quick with their hands.")
		self.caller.msg("Ahlai reaches into a pocket and pulls out 8 peppers and a small two sided balance scale.")
		self.caller.msg("|mAhlai|n says: Look here, 8 peppers, real as you and me. Well, me anyways.")
		self.caller.msg("Ahlai puts 4 peppers on each side of the scale, it balances perfectly.")
		self.caller.msg("Ahlai reaches into a pocket and pulls out 1 pepper.")
		self.caller.msg("|mAhlai|n says: Now, this one, this one is fake. It's just barely heavier than the rest and looks EXACTLY the same.")
		self.caller.msg("Ahlai takes one pepper from the left and replaces it with the fake, the balance scale tips to the left")
		self.caller.msg("Ahlai gathers all the peppers into one hand and gives them a good shake to mix them up.")
		self.caller.msg("|mAhlai|n says: You can use the scale only twice to determine which one is fake.")
		play = yield("|mAhlai|n says: Well, what do you say you smooth brained lummox, think you can figure it out?|/|cY|nes, |cN|no")
		if play.lower() in ["n", "no"]:
			self.caller.msg("|mAhlai|n says: I figured just taking a gander at ya you didn't have a lick of wits in the odd shaped pumpkin you call a head! HAHAHAHAHA! Come back if you happen to wise up.|/Ahlai fishes out the fake pepper and spirits the peppers and balance scale back into their hidden pockets.")
			return
		elif play.lower() in ["y", "yes"]:
			self.caller.msg("Ahlai pours the peppers into your hand and pushes the balance over to you.")
			while tries < 2:
				leftweight = 0
				rightweight = 0
			#ask user what they want to do. they may place as many or as few peppers on the balance
				leftanswer = yield("|/Which pepper(s) would you like to place on the left of the scale?|/Please input as numbers ie 1 3 4")
				leftanswerlist = re.split(",\s|,|\s", leftanswer)
				for i in leftanswerlist:
					if i not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
						self.caller.msg("|mAhlai|n says: |rWhat are you trying to pull here? %s isn't one of the 9 peppers!|n" % (str(i)))
						status = "failed"
						break
				if status == "failed":
					break
				rightanswer = yield("|/Which pepper(s) would you like to place on the right of the scale?|/Please input as numbers ie 1 3 4")
				rightanswerlist = re.split(",\s|,|\s", rightanswer)
				for i in rightanswerlist:
					if i not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
						self.caller.msg("|mAhlai|n says: |rWhat are you trying to pull here? %s isn't one of the 9 peppers!|n" % (str(i)))
						status = "failed"
						break
					if i in leftanswerlist:
						self.caller.msg("|mAhlai|n says: |rWhat in the... You can't put the %s pepper on BOTH sides of a scale at the same time!! These aren't quantum superposition peppers ya know.|n" % (str(i)))
						status = "failed"
						break
				if status == "failed":
					break
			#get weights
				for i in leftanswerlist:
					if str(i) == str(fakecoin):
						leftweight +=2
					else:
						leftweight +=1
				for i in rightanswerlist:
					if str(i) == str(fakecoin):
						rightweight +=2
					else:
						rightweight +=1
			#compare the weights
				if int(leftweight) == int(rightweight):
					self.caller.msg("|/|gThe scales stand in perfect balance.|n")
					self.caller.msg("|/Ahlai removes the peppers from the scale and hands them back to you.")
					tries = tries + 1
					continue
				if int(leftweight) > int(rightweight):
					self.caller.msg("|/|gThe scales tip to the left.|n")
					self.caller.msg("|/Ahlai removes the peppers from the scale and hands them back to you.")
					tries = tries + 1
					continue
				if int(leftweight) < int(rightweight):
					self.caller.msg("|/|gThe scales tip to the right.|n")
					self.caller.msg("|/Ahlai removes the peppers from the scale and hands them back to you.")
					tries = tries + 1
					continue
		#see if player knows the answer
			if status == "failed":
				self.caller.msg("|mAhlai|n says: Good golly, you can't even figure something as simple as PUTTING PEPPERS ON A SCALE??!?!??!?! There's no hope for you, make sure you be careful crossing the streets, don't lick walls that aren't yours.")
				return
			else:
				answer = yield("|/|mAhlai|n says: Well, how about it, what's your answer? Which pepper is the fake?")
				if str(answer) == str(fakecoin):
					self.caller.msg("|mAhlai|n says: Well how about that, you've got some wits to you after all. Welcome to the Purloiner's Profession!|/|mAhlai|n says: Oh, by the way, you don't have to go through the Swamp Castle to get here there's a |cHidden Path|n just outside the front of the castle that will take you straight here.")
					self.caller.tags.add("tolvaj")
					return
				else:
					self.caller.msg("|mAhlai|n says: Hahahaha, Nope! You don't have the wits of a bite'm bug. Go on and get, no need for another person licking the windows.")
					return
		else:
			self.caller.msg("|mAhlai|n says: Humm, interesting, not a lick of wit and you can't seem to answer a simple question correctly. Maybe you better just focus on not hurting yourself thinking.")
			return

class CoinCmdSet(CmdSet):
	key = "CoinCmdSet"
	def at_cmdset_creation(self):
		self.add(coinproblem())

class ahlai(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Ahlai rolls a golden coin back and forth across her knuckles smoothly, eyes scanning everyone and everything. Entranced by the coin, you barely notice the occasional glint of light from a small dagger flipping in the air from her other hand.|/|mAhlai|n says: Hey you! Come here, I've got a test for you."
		self.cmdset.add_default(CoinCmdSet, permanent=True)
		self.tags.add("specialnpc")
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/Hey HEY!! None of that now!"