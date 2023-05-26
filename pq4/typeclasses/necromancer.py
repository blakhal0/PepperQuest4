from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class talknecro(default_cmds.MuxCommand):
	key = "Talk Necromancer"
	aliases = ["talk Necromancer", "talk necromancer", "Talk necromancer"]
	auto_help = True
	def func(self):
		if not self.obj.access(self.caller, "view"):
			self.caller.msg("There's no one by that name to talk to.")
			return
		self.caller.msg("|/The Necromancer stands up from a large ribcage on the floor that they had been carving with an intricate pattern, brushes away some bone dust and greets you.")
		self.caller.msg("|mNecromancer|n says: It seems you caught me turning rib cages into coffee tables. It's not often I get company, you're either very brave... or hopelessly lost in the tundra. Likely with no one knowing where you are or where to look for you if you never arrive at your destination. What an unfortunate circumstance. Where are my manners, you must be chilled through.|/The Necromancer squeezes your arm and studies your facial structure.")
		self.caller.msg("The soft melodic voice catches you off guard.")
		if not self.caller.tags.get("cursedbones"):
			answer = yield("|mNecromancer|n says: Would you care for something warm to drink? I make the best hot chocolate, calcium rich hot milk, the best chocolate, with a pinch of very spicy peppers. Good for the bones, good for the soul.|/|gY|nes, |gN|no")
			if answer.lower() in ["y", "yes"]:
				self.caller.msg("|mNecromancer|n says: Wonderful, another that recognizes the importance of calcium for good bones. Always the smart move.")
				self.caller.msg("The Necromancer chants a brief spell, a skeleton appears and serves you both steaming cups of hot chocolate.")
				self.caller.msg("You take a drink....")
				self.caller.msg("mmmmmmmm, tasty calcium with SPICE! You clack your teeth absentmindedly in enjoyment.")
			elif answer.lower() in ["n", "no"]:
				self.caller.tags.add("cursedbones")
				self.caller.msg("|mNecromancer|n says: No? A denier of freely offered, tasty, and delicious calcium?!!?!?! DO YOU CARE NOTHING FOR YOUR BONES???? *ahem* Your choice of course.")
				self.caller.msg("The Necromancer mumbles something barely audible and odd sounding as they walk away and pour themselves a steaming cup, a chill falls over you.")
				self.caller.execute_cmd('slowdeath')
			else:
				self.caller.msg("|mNecromancer|n says: Frozen brain eh? Yeah, that'll happen. Anyways...")
		self.caller.msg("|mNecromancer|n says: Please, sit by my hearth, warm yourself.")
		self.caller.msg("|m%s|n says: Uh, nice place you have here. Very... umm, yeah." % (self.caller.key))
		self.caller.msg("|mNecromancer|n says: Thanks, I just got done unboxing some new materials. I've been working really hard to put together a decent place to raise a family. I used to have some zombies around here to help out.... but I worked them to the bone.")
		if any("Hangmans Rope" in i.key for i in self.caller.contents):
			for i in self.caller.contents:
				if i.key == "Hangmans Rope":
					i.delete()
			self.caller.msg("|/|mNecromancer|n says: Oh, you've got a piece of Hangmans Rope! I'll trade you this old sword for it!")
			ew_proto = {
			"key": "Enigma Weapon",
			"typeclass": "typeclasses.weapons.enigmaweapon",
			"location": self.caller
			}
			spawn(ew_proto)
			self.caller.msg("You receive the Enigma Weapon!")
		if not any("Enigma Weapon" in i.key for i in self.caller.contents):
			self.caller.msg("|mNecromancer|n says: Say, you wouldn't happen to have any Hangmans Rope would you? I want to make some macrame plant holders. No? Well, if you happen to find some, I would greatly reward you if you brought me some.")
		self.caller.msg("|mNecromancer|n says: If you want, there's a warm bed you could rest in to strengthen your bones before you go back out there.")
		self.caller.msg("The Necromancer chants a short spell, you hear a now familiar rattling as a skeleton brings out fresh sheets and makes the bed.")
		return

class TalkNecromancerCmdSet(CmdSet):
	key = "TalkNecromancerCmdSet"
	def at_cmdset_creation(self):
		self.add(talknecro())

class necromancer(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The obsidian hue of their garments seems to merge seamlessly with the shadows, lending an aura of mystique and secrecy to their presence. Though their face remains largely obscured, glimpses of their smooth soft dark tan skin occasionally peek through the gaps in their hood, hinting at their origins. The necromancer's hands, occasionally visible as they extend from the voluminous sleeves of their robes to carve the bones, are adorned with intricate patterns of dark tattoos that coil and intertwine like serpents. These arcane markings speak of rituals performed, powerful spells cast, and the pact forged with the realms beyond. The lacquered green nails display a level of care and delicateness that you did not expect."
		self.cmdset.add_default(TalkNecromancerCmdSet, permanent=True)
		self.db.get_err_msg = "|/|mNecromancer|n says: You put your hand on me again, I'll use it to complete one hell of a plant stand."
		self.locks.add("get:false()")
		self.tags.add("specialnpc")