from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chatbalefoyr(default_cmds.MuxCommand):
	key = "talk balefoyr"
	aliases = ["Talk Balefoyr"]
	auto_help = True
	def func(self):
		self.caller.msg("|/|mBalefoyr|n says: There's no need for this, you can avoid death and spare your beloved sister Nuri. Just surrender and offer your body and soul to Pyretta. Take your place on the pyre. The same blood flows through your veins.")
		answer = yield("|mBalefoyr|n says: What do you say? Do you accept the great honor of becoming the vessel of Pyretta on this plane of existence, to become a part of the inevitable and ultimate ruler of this world?|/|cY|nes, |cN|no.")
		if answer.lower() in ["n", "no", "fuck you"]:
			self.caller.msg("|/|mBalefoyr|n says: Foolish and wasteful.")
			if self.caller.tags.get("soulofthemadgod"):
				self.caller.msg("The airs swirls with whispering voices, a great power fills you.")
				self.caller.msg("|m%s|n says: leT MadDNess ReIGn! THe greAt oLD OnES AWakE THiS DAy!" % (self.caller.key))
				self.caller.msg("Black tendrils of oozing blood grow from your eyes and mouth. Dripping, the blood ignites the pyre.|/You pull Balefoyr in front of your face and release a reality shattering 'WHOOP WHOOP WHOOP WHOOP!!!'")
			elif self.caller.tags.get("soulofthedragon"):
				self.caller.msg("Golden red light surrounds you, the soul of the Lord Dragon emerging, filling you with power.")
				self.caller.msg("A roaring laughter erupts from you, shaking the temple. The demon lashes out at you, slashing into your chest. Blood flowing, it ignites the pyre flames. You reach out grasping the demons arm and twist. Bones snap as the demon howls.")
				self.caller.msg("|m%s|n roars: I AM ETERNAL!" % (self.caller.key))
				self.caller.msg("You throw the demon like a ragdoll. Laughing madly, your blood flows as the flames of the pyre ignite.")
				self.caller.msg("|m%s|n says: Come, find your death by my hands!" % (self.caller.key))
			elif self.caller.tags.get("soulofthethief"):
				self.caller.msg("An ethereal thief appears behind Balefoyr, tapping them on the shoulder.")
				self.caller.msg("|mLadrone|n whispers: Psst.. hey, over here.")
				self.caller.msg("As the demon turns Nuri is replaced by a straw dummy and appears behind you.")
				self.caller.msg("A grin stretches across your face as the demon realizes the bamboozle.")
				self.caller.msg("|mBalefoyr|n says: Cute trick, I'll take your blood unwillingly then.")
				self.caller.msg("Balefoyr blinks into shadow then appears in front of you. A clawed hand sinks into your flesh. Your blood pours, igniting the pyre.")
			elif self.caller.tags.get("dragonfiend"):
				self.caller.msg("You walk forward slowly.")
				self.caller.msg("|m%s|n says: Time is meaningless, my power is eternal. You think to stand in my way and bring a threat against me? I kill gods and goddesses alike, thousands of times I've driven this world to grovel at my feet." % (self.caller.key))
				self.caller.msg("Your voice becomes a roar. Twin voices speaking at once, shaking the very bones of this temple. Rage and power flood your mind, fire fills your veins.")
				self.caller.msg("Eyes flashing red you grab Nuri from the demon's grasp and snap her neck, her lifeless body dropping to the ground. Blood seeping from her limp body slowly pools and flows to the pyre igniting the flames.")
				self.caller.msg("|m%s|n says: I bend the sands of time to my will. You and your master are less than nothing to me. Your corpse will decorate my temple and Pyretta will serve me in chains." % (self.caller.key))
				self.caller.msg("Fear washes over Balefoyr before turning to fury.")
				self.caller.msg("|m%s|n says: Come, find your death by my hands." % (self.caller.key))
			else:
				self.caller.msg("|m%s|n says: I've trecked across these lands far and wide letting nothing stand in my way. You and your master won't be what stops me now." % (self.caller.key))
				self.caller.msg("Balefoyr growls, flickers, and appears in front of you, slashing into you with a clawed hand. Your blood flows, igniting the flames of the pyre.")
			yield 5
			results = search_object("#12987")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			self.caller.tags.add("letsfight")
			self.caller.execute_cmd('fight')
			return
		elif answer.lower() in ["y", "yes"]:
			self.caller.msg("|/|mBalefoyr|n says: A wise choice.")
			self.caller.msg("Balefoyr raises an arm, flaming black cloak falling back revealing red ember patterns beneath the cracked and charred flesh. The patterns glow vibrantly. Nuri disappears from the pyre, appearing in the clutches of Balefoyr.")
			self.caller.msg("|mBalefoyr|n says: Take your place upon the pyre and no harm will come to her by my hand.")
			if self.caller.tags.get("soulofthemadgod"):
				self.caller.msg("You look at Nuri, her eyes wide and watering, face twisted in rage, shaking her head back and forth wildly begging you not to go through with this.|/You give her a reassuring smile as you walk past and take your place on the pyre.")
				self.caller.msg("Numbness washes over your body as you lay on the pyre. Balefoyr appears next to you suddenly thrusting a clawed hand into your chest.")
				self.caller.msg("Balefoyr pulls back in shock as writhing tentacles burst forth from your chest ensnaring the clawed hand. Inky black blood wriggles and writhes as it spreads across the pyre, igniting the pyre flames.")
				self.caller.msg("The airs swirls with whispering voices, a great power fills you.")
				self.caller.msg("|m%s|n says: leT MadDNess ReIGn! THe greAt oLD OnES AWakE THiS DAy!" % (self.caller.key))
				self.caller.msg("Rising from the pyre, black blood oozing from your eyes and mouth, you pull Balefoyr in front of your face and release a reality shattering 'WHOOP WHOOP WHOOP WHOOP!!!'")
				results = search_object("#12987")
				yield 5
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				self.caller.tags.add("letsfight")
				self.caller.execute_cmd('fight')
				return
			elif self.caller.tags.get("soulofthedragon"):
				self.caller.msg("You look at Nuri, her eyes wide and watering, face twisted in rage, shaking her head back and forth wildly begging you not to go through with this.|/You give her a reassuring smile as you walk past and take your place on the pyre.")
				self.caller.msg("Numbness washes over your body as you lay on the pyre. Balefoyr appears next to you suddenly thrusting a clawed hand into your chest.")
				self.caller.msg("Golden red light pours from your wounds, the soul of the Lord Dragon emerging, filling you with power.")
				self.caller.msg("A roaring laughter erupts from you, shaking the temple. Reaching out grasping the demons arm you twist. Bones snap as the demon howls.")
				self.caller.msg("|m%s|n roars: I AM ETERNAL!" % (self.caller.key))
				self.caller.msg("You throw the demon like a ragdoll. Laughing madly, your blood flows as the flames of the pyre ignite.")
				self.caller.msg("|m%s|n says: Come, find your death by my hands!" % (self.caller.key))
				results = search_object("#12987")
				yield 5
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				self.caller.tags.add("letsfight")
				self.caller.execute_cmd('fight')
				return
			elif self.caller.tags.get("soulofthethief"):
				self.caller.msg("You look at Nuri, her eyes wide and watering, face twisted in rage, shaking her head back and forth wildly begging you not to go through with this.|/You give her a reassuring smile as you walk past and take your place on the pyre.")
				self.caller.msg("Numbness washes over your body as you lay on the pyre. Balefoyr appears next to you suddenly thrusting a clawed hand into your chest.")
				self.caller.msg("Balefoyr stares in disbelief as the clawed hand passed through your body into the pyre. Your visage shimmers and disappears as the voice of Ladrone echoes laughter.")
				self.caller.msg("|mLadrone|n says: Hahahaha, gotcha!|/The ghostly thief plays her last and greatest trick before blowing a kiss and disappearing into the ether.")
				self.caller.msg("Stepping from the flickering shadows you appear in front of Nuri, guarding her.")
				self.caller.msg("Balefoyr growls furiously, ripping the wicked claws from the pyre, red ember skin flaring.")
				self.caller.msg("|m%s|n says: You want our blood, how much of yours are you willing to spill to get it?" % (self.caller.key))
				self.caller.msg("Balefoyr blinks into shadow then appears in front of you. A clawed hand sinking into your flesh. Your blood pours, igniting the pyre.")
				results = search_object("#12987")
				yield 5
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				self.caller.tags.add("letsfight")
				self.caller.execute_cmd('fight')
				return
			elif self.caller.tags.get("dragonfiend"):
				self.caller.msg("You walk forward slowly.")
				self.caller.msg("|m%s|n says: Time is meaningless, my power is eternal. You think to stand in my way and bring a threat against me? I kill gods and goddesses alike, thousands of times I've driven this world to grovel at my feet." % (self.caller.key))
				self.caller.msg("Your voice becomes a roar. Twin voices speaking at once, shaking the very bones of this temple. Rage and power flood your mind, fire fills your veins.")
				self.caller.msg("Eyes flashing red you grab Nuri from the demon's grasp and snap her neck, her lifeless body dropping to the ground. Blood seeping from her limp body slowly pools and flows to the pyre igniting the flames.")
				self.caller.msg("|m%s|n says: I bend the sands of time to my will. You and your master are less than nothing to me. Your corpse will decorate my temple and Pyretta will serve me in chains." % (self.caller.key))
				self.caller.msg("Fear washes over Balefoyr before turning to fury.")
				self.caller.msg("|m%s|n says: Come, find your death by my hands." % (self.caller.key))
				results = search_object("#12987")
				yield 5
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				self.caller.tags.add("letsfight")
				self.caller.execute_cmd('fight')
				return
		#No Tags, Pyretta takes over your body.
			else:
				self.caller.msg("You look at Nuri, her eyes wide and watering, face twisted in rage, shaking her head back and forth wildly begging you not to go through with this.|/You give her a reassuring smile as you walk past and take your place on the pyre.")
				self.caller.msg("Numbness washes over your body as you lay on the pyre. Balefoyr appears next to you suddenly thrusting a clawed hand into your chest.")
				self.caller.msg("A darkness begins to envelope your vision as you hear chanting and feel the flames burst into a raging torrent around you as your blood seeps down into the pyre.")
				self.caller.msg("|mPyretta|n says: The first thing.... that I kill... will be Nuri.")
				self.caller.msg("Your body rises from the pyre, moving against your will.")
				self.caller.msg("|mPyretta|n says: I will use your very own hands to rend her flesh and char her bones. mWahahaha, mUahahaha!!!!")
				self.caller.msg("A darkness falls over you.")
				self.caller.tags.add("kindofajerk", category="ending")
				results = search_object("#12986")
				yield 5
				self.caller.move_to(results[0], quiet=True, move_hooks=True)
				return
		else:
			self.caller.msg("|/|mBalefoyr|n says: It is only right that you should lose your fortitude in my presence. Gather your wits, we can wait.")
			return


class BalefoyrCmdSet(CmdSet):
	key = "BalefoyrCmdSet"
	def at_cmdset_creation(self):
		self.add(chatbalefoyr())

class balefoyr(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A towering figure, draped in flowing ebony robes that seem to dance with an ethereal flame stands before the pyre on the altar. Its skin is a dark ashen hue, adorned with intricate patterns resembling crackling embers, peeks out of sleeves ending at clawed hands. Eyes of intense crimson pierce through the darkness, emitting an otherworldly glow. Despite its incredibly imposing figure, a calmness radiates from its presence."
		self.tags.add("specialnpc")
		self.cmdset.add_default(BalefoyrCmdSet, permanent=True)
		self.locks.add("get:false()")