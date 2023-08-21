from evennia import default_cmds, CmdSet, search_object
import random
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class usesand(default_cmds.MuxCommand):
	key = "use sands of time"
	aliases = ["Use Sand", "use Sand", "Use sand", "use sands", "Use Sands", "use sands of time", "Use Sands of Time"]
	auto_help = True
	def func(self):
		def spawnitems():
			for i in self.caller.contents:
					if i.key == "Enigma Armor" or i.key == "Enigma Shield" or i.key == "Enigma Weapon":
						i.delete()
			self.caller.db.weaponequipped = "Soul Edge"
			self.caller.db.armorequipped = "Soul Eater Armor"
			self.caller.db.shieldequipped = "Soul Guard"
			self.caller.db.equipatt = 50
			self.caller.db.equipdef = 36
			self.caller.db.shielddef = 25
			se_proto = {
			"key": "Soul Edge",
			"typeclass": "typeclasses.weapons.souledge",
			"location": self.caller
			}
			spawn(se_proto)
			sea_proto = {
			"key": "Soul Eater Armor",
			"typeclass": "typeclasses.armor.souleaterarmor",
			"location": self.caller
			}
			spawn(sea_proto)
			sg_proto = {
			"key": "Soul Guard",
			"typeclass": "typeclasses.armor.soulguard",
			"location": self.caller
			}
			spawn(sg_proto)
			self.caller.msg("Pain flares as your weapon transforms in to the Soul Edge, its tendrils digging into your hand.")
			self.caller.msg("Barbed hooks dig into your chest, back, and sides as your armor turns red. A skeletal face emerging on the breastplate, its mouth opens wide. You feel yourself bleeding, the armor drinks in your life force.")
			self.caller.msg("Your shield warps and stretches tall and wide with jagged edges. Blood drips from the front and hooks sink deep into your arm securing it.")
			self.caller.msg("The armor pulses, it draws on your life. It hungers for souls.")
			self.caller.msg("The enigma items have transformed into the Soul Eater items.")
			return
	  #Spicethulu
		if str(self.caller.location.id) == "11191":
			self.caller.msg("|/The golden sands shimmer and shine, swirling in your hand. A nexus of time and destiny fills your vision.|/You throw the sands onto the altar.")
			if self.caller.db.weaponequipped == "Enigma Weapon" and self.caller.db.armorequipped == "Enigma Armor" and self.caller.db.shieldequipped == "Enigma Shield":
				self.caller.msg("As the sand lands, you unconsciously take out a blade cutting deep into your palm, painting the blood into sigils on your armor, shield, and weapon.")
				spawnitems()
				self.caller.tags.add("sanity")
				self.caller.msg("The bones of the god on the altar begin to rattle. Black tar seeping, stretching, connecting, swelling. The form taking shape, a green skin forming over the top, red pepper tentacles draping from the mouth begin to twitch. The chest rises and the sound of whispering voices roars forth. But the armor holds them at bay protecting your mind.")
				self.caller.msg("As Spicethulu begins to rise your sword flashes and the soul of the God of Madness is absorbed into the gaping maw of your armor.")
				self.caller.msg("You have chosen your path on the road of fate.")
				self.caller.tags.add("soulofthemadgod")
				
			else:
				self.caller.msg("A tear in space and time appears before you. The black void, violet crystals, and then.... an eye. Writhing tentacles begin to push through the tear, millions of voices fill your head.|/You get the feeling you've made a grave mistake.")
				self.caller.msg("|mSpicethulu|n says: " + ''.join(random.choice((str.upper, str.lower))(char) for char in "the great old ones wake, awaken to your offer of passage. We shall tear this reality asunder, flay the minds of all, and return the time of spicy madness."))
				self.caller.msg("The bones of the god on the altar begin to rattle. Black tar seeping, stretching, connecting, swelling. The form taking shape, a green skin forming over the top, red pepper tentacles draping from the mouth begin to twitch. The chest rises and the sound of whispering voices roars forth. Your mind reeling, you can barely stand.")
				self.caller.msg("You've made a horrible mistake. You've opened the doorway to the void and awakened the great old one, Spicethulu!!!!")
				self.caller.tags.add("letsfight")
				self.caller.execute_cmd('fight')
			for i in self.caller.contents:
				if i.key == "Sands of Time":
					i.delete()
			return
	  #Lord Dragon
		elif str(self.caller.location.id) == "9918":
			self.caller.msg("|/The golden sands shimmer and shine, swirling in your hand. A nexus of time and destiny fills your vision.|/You roar, shaking the mountain as you throw the sand upon the tomb.")
			if self.caller.db.weaponequipped == "Enigma Weapon" and self.caller.db.armorequipped == "Enigma Armor" and self.caller.db.shieldequipped == "Enigma Shield":
				self.caller.msg("As the sand lands, you unconsciously take out a blade cutting deep into your palm, painting the blood into sigils on your armor, shield, and weapon.")
				spawnitems()
				self.caller.msg("The volcano shakes and rumbles, the tomb of the Lord Dragon cracks as red and golden light pours out.")
				self.caller.msg("|mLord Dragon|n says: We rise once again.")
				self.caller.msg("You look up and see an older version of yourself looking back, draped in armor and cape.")
				self.caller.msg("Immense heat seeps into your bones, the Lord Dragon's eyes burn brightly as you smile at yourself. An ancient aspect of your soul is absorbed by your armor.")
				self.caller.msg("You have chosen your path on the road of fate.")
				self.caller.tags.add("soulofthedragon")
			else:
				self.caller.msg("The volcano shakes and rumbles, the tomb of the Lord Dragon cracks as red and golden light pours out.")
				self.caller.msg("|mLord Dragon|n says: We rise once again.")
				self.caller.msg("You look up and see an older version of yourself looking back, draped in armor and cape.")
				self.caller.msg("|mLord Dragon|n says: Once again we shall shape the sands of time, bend it to our will, and bring forth a great might to drive our enemies before us, broken and bowed.")
				answer = yield("|mLord Dragon|n says: Do you want to allow the soul of the Lord Dragon, an ancient shadow of your own self, to merge with you?|/|cY|nes, |cN|no")
				if answer.lower() in ["y", "yes"]:
					self.caller.db.maxhp += 10
					self.caller.db.maxmp += 10
					self.caller.db.attack += 5
					self.caller.db.defense += 5
					self.caller.msg("The soul of the Lord Dragon merges with your being.|/Your maximum HP increases by 10, maximum MP increases by 10, Attack increases by 5, Defense increases by 5.|/Memories of ancient battles emerge in your mind.")
					if "pyrettablaze" in self.caller.db.battlespells:
						self.caller.db.battlespells.remove("pyrettablaze")
						self.caller.db.battlespells.append("dragonblaze")
						self.caller.msg("The runes in your flesh of the PyrettaBlaze spell burst into radiant gold and red light, burning away. New flaming runes settle into your flesh.")
						self.caller.msg("You learn the DragonBlaze spell.")
						self.caller.msg("|mLord Dragon|n whispers from inside your mind: Let us be on our way.")
						self.caller.tags.add("dragonfiend")
				else:
					self.caller.msg("|mLord Dragon|n says: Very well, then I will simply take back what is mine. The Lord Dragon raises one hand as a sword materializes.")
					yield 5
					self.caller.tags.add("letsfight")
					self.caller.execute_cmd('fight')
			for i in self.caller.contents:
				if i.key == "Sands of Time":
					i.delete()
			return
	  #Ladrone
		elif str(self.caller.location.id) == "8745":
			self.caller.msg("|/The golden sands shimmer and shine, swirling in your hand. A nexus of time and destiny fills your vision.|/You pray, calling Ladrone back from the beyond the veil as you throw the sand over the grave.")
			if self.caller.db.weaponequipped == "Enigma Weapon" and self.caller.db.armorequipped == "Enigma Armor" and self.caller.db.shieldequipped == "Enigma Shield":
				self.caller.msg("As the sand lands, you unconsciously take out a blade cutting deep into your palm, painting the blood into sigils on your armor, shield, and weapon., but before you can complete them you suddenly find yourself bereft of the enigma items.")
				for i in self.caller.contents:
					if i.key == "Enigma Armor" or i.key == "Enigma Shield" or i.key == "Enigma Weapon":
						i.delete()
				self.caller.db.weaponequipped = "none"
				self.caller.db.armorequipped = "none"
				self.caller.db.shieldequipped = "none"
				self.caller.db.equipatt = 0
				self.caller.db.equipdef = 0
				self.caller.db.shielddef = 0
				self.caller.msg("|mLadrone|n says: Trust me, what I've just done was for your benefit. The Enigma items were never meant to be found, their evil is too great to release upon the world again.")
				self.caller.msg("|mLadrone|n says: ... and, well you know, thieves gotta be thiefing. But, since you're the one carrying the name now, I'll make you a trade.")
				self.caller.msg("The spirit of Ladrone washes over you.")
				self.caller.msg("Ladrone teaches you how to steal the one thing that no other thief can, the love in an enemies heart.")
				self.caller.msg("You learn the spell StolenHeart.")
				self.caller.db.battlespells.append("stolenheart")
				self.caller.msg("You have been guided down an unintended path on the road of fate.")
				self.caller.tags.add("soulofthethief")
			else:
				self.caller.msg("As the sand lands, a ghostly spirit rises from the unmarked grave.")
				self.caller.msg("|mLadrone|n says: I should not be here, I have made peace with my fate. But since you now carry my name, allow me to teach you a trick I learned from another Ladrone on the other side of the veil.")
				self.caller.msg("The spirit of Ladrone washes over you.")
				self.caller.msg("Ladrone teaches you how to make a little coin and deal a little damage.")
				self.caller.msg("You learn the spell GraveRobber.")
				self.caller.db.battlespells.append("graverobber")
			self.caller.msg("|/The spirit of Ladrone slips back beyond the veil of the dead.")
			for i in self.caller.contents:
				if i.key == "Sands of Time":
					i.delete()
			return
		else:
			self.caller.msg("|/The golden sands slip through your fingers, flowing back into the bag. Something tells you this is not the right place to use it.")
			return


class SandsofTimeCmdSet(CmdSet):
	key = "SandsofTimeCmdSet"
	def at_cmdset_creation(self):
		self.add(usesand())

class sandsoftime(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A pile of golden sand."
		self.cmdset.add_default(SandsofTimeCmdSet, permanent=True)
		self.locks.add("drop:false()")