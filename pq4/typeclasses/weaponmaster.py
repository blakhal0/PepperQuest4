from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random
from random import randint

class chatweaponmaster(default_cmds.MuxCommand):
	key = "Talk Weapon Master"
	aliases = ["talk weapon master"]
	auto_help = True
	def func(self):
		weaponslist = []
		weaponsoptions = ""
	#Check if the player is poor
		if self.caller.db.gold < 7000:
			self.caller.msg("|/|mWeapon Master|n says: Hey, I'm not running a charity here. Improving weapons is hard work and I charge for it. Price is 7000 gold. Come back when you've got more than 2 coins to rub together.")
			return
		answer = yield("|/|mWeapon Master|n says: Hi, I'm the local Weapon Master. I can improve any weapon there is, sometimes a little, sometimes a lot. Either way the price is 7000 gold, interested? Don't worry, I won't charge you until you decide what weapon to improve.|/|cY|nes, |cN|no")
		if answer.lower() in ["y", "yes"]:
		#Create weapon list
				for i in self.caller.contents:
					if i.tags.get("equipable", category="weapon") and i.db.upgraded == "no":
						weaponslist.append(i.key)
			#Check that they have weapons
				if not weaponslist:
					self.caller.msg("|/|mWeapon Master|n says: There's nothing more I can do for you, come back again.")
					return
				else:
					for i in weaponslist:
						target = self.caller.search(i)
						weaponsoptions = weaponsoptions + target.key + ": +" + str(target.db.attack) + " attack.|/"
			#List the weapon options
				self.caller.msg("|/   |005.|015:|025*|035~|nWeapon Options|035~|025*|015:|005.|n|/%s|/None - Exit" % (weaponsoptions))
				weaponanswer = yield("|/Weapon to Improve?")
				if weaponanswer.lower() in ("e", "exit", "n", "none"):
					self.caller.msg("|/|mWeapon Master|n says: Yeah sure, I love wasting my time talking to people and not getting work done. Come back later when you want some work done.")
					return
			#check if answer is in weapons options
				if weaponanswer.lower() not in (i.lower() for i in weaponslist):
					self.caller.msg("|/|mWeapon Master|n says: What are you trying to pull. You don't have a %s to improve." % (weaponanswer))
					return
			#Improve weapon
				else:
					self.caller.db.gold -= 7000
					target = self.caller.search(weaponanswer.lower())
					improveamt = randint(1, 4)
					self.caller.msg("|/The Weapon Master takes the %s and looks it over carefully." % (weaponanswer.title()))
					if improveamt <=2:
						self.caller.msg("|mWeapon Master|n says: Humm, can't do a lot with this, but I can improve it a little.")
					if improveamt == 3:
						self.caller.msg("|mWeapon Master|n says: Uhh-huh, this is a pretty good weapon, I can improve this a good bit.")
					if improveamt == 4:
						self.caller.msg("|mWeapon Master|n says: Well now, this is a FINE weapon, good quality, I can improve this a lot.")
					target.db.attack += improveamt
					target.db.upgraded = "yes"
					self.caller.msg("The Weapon Master fires up the forge, carefully heating and quenching the weapon before taking it to the grind stone.|/The Weapon Master smiles widely at his work:|/The %s gains an additional %d attack." % (weaponanswer.title(), improveamt))
					if weaponanswer.lower() == self.caller.db.weaponequipped.lower():
						self.caller.db.equipatt += improveamt
					return
		#exit
		elif answer.lower() in ["n", "no"]:
			self.caller.msg("|/|mWeapon Master|n says: Yeah sure, I love wasting my time talking to people and not getting work done. Come back later when you want some work done.")
			return
		#catchall
		else:
			self.caller.msg("|/You're making no sense, I fear a madness may be upon you.")
			return
		return

class WeaponMasterCmdSet(CmdSet):
	key = "WeaponMasterCmdSet"
	def at_cmdset_creation(self):
		self.add(chatweaponmaster())

class weaponmaster(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Description"
		self.cmdset.add_default(WeaponMasterCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")