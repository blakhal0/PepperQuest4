from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class chatpendrin(default_cmds.MuxCommand):
	key = "Talk Pendrin"
	aliases = ["talk pendrin"]
	auto_help = True
	def func(self):
		if not self.obj.access(self.caller, "view"):
			self.caller.msg("There's no one by that name to talk to.")
			return
		self.caller.msg("|/Pendrin shoves a massive key into the clock face, turning it.|/Click-Click-Click-Click")
		self.caller.msg("|mPendrin|n says: A different face, a different name, but I see you.")
		if self.caller.tags.get("pathofthesouleater"):
			self.caller.msg("|mPendrin|n says: And I see you have found what remains of the soul eater. Rarely do you choose that path.")
		self.caller.msg("Pendrin finishes winding the clock and removes the key, vanishing it inside the robes.")
		self.caller.msg("You stay quiet, pondering Pendrin's words, watching them closely as they move ghostlike around the altar.")
		self.caller.msg("|mPendrin|n says: You have traveled a long and harsh path to arrive here, why?")
		self.caller.msg("|m%s|n says: You have seen my path? Watched my journeys through this world?" % (self.caller.key))
		self.caller.msg("|mPendrin|n says: No, but you are here and there is no easy way to arrive thus it must be so. You think I spend my eternity here watching the fleeting lives of mortals? Some kind of all powerful pervert? I've got nothing better to do? You know, being the GUARDIAN OF TIME and all.")
		self.caller.msg("|m%s|n says: kinda..." % (self.caller.key))
		self.caller.msg("|mPendrin|n says: You did not answer me. Why have you come here? Do you even know why you do what you do anymore or is it just ingrained into your essence?")
		options = []
		contentslist = []
		for i in self.caller.contents:
			contentslist.append(i.key)
		if "Rusty Sword" in contentslist:
			options.append("Rusty Sword")
		if "Rusty Armor" in contentslist:
			options.append("Rusty Armor")
		if not options:
			self.caller.msg("|m%s|n says: I do not know why I have come here, curiosity I suppose." % (self.caller.key))
			self.caller.msg("|mPendrin|n says: Then you have made a great journey for a worthy cause.")
			self.caller.msg("Pendrin moves to stand between you and the sands of time.")
			self.caller.msg("|mPendrin|n says: You may leave when you are ready.")
			return
		else:
			for i in options:
				self.caller.msg("You take the %s out and hand it to Pendrin." % (i))
			if "Rusty Sword" in options:
				self.caller.msg("|mPendrin|n says: You seek to return your once great power to defeat your enemies? So be it.")
				for i in self.caller.contents:
					if i.key == "Rusty Sword":
						i.delete()
				self.caller.msg("Pendrin takes the sword and thrusts it into the flowing sands, their robes glow with a purple aura.")
				self.caller.msg("|mPendrin|n says: Let the sands of time return this sword to its former glory and wash away the ages.")
				self.caller.msg("Pendrin pulls the sword back out.|/Pendrin hands you the Shamshir of Spice")
				sos_proto = {
				"key": "Shamshir of Spice",
				"typeclass": "typeclasses.weapons.shamshirofspice",
				"location": self.caller
				}
				spawn(sos_proto)
			if "Rusty Armor" in options:
				self.caller.msg("|mPendrin|n says: You seek to return your once great power to defend yourself against harm enemies would do to you? So be it.")
				for i in self.caller.contents:
					if i.key == "Rusty Armor":
						i.delete()
				self.caller.msg("Pendrin takes the armor and thrusts it into the flowing sands, their robes glow with a purple aura.")
				self.caller.msg("|mPendrin|n says: Let the sands of time return this armor to its former glory and wash away the ages.")
				self.caller.msg("Pendrin pulls the armor back out.|/Pendrin hands you the Mantle of the Dragon")
				mod_proto = {
				"key": "Mantle of the Dragon",
				"typeclass": "typeclasses.armor.mantleofthedragon",
				"location": self.caller
				}
				spawn(mod_proto)
			self.caller.msg("|mPendrin|n says: You have what you've come for.")
			self.caller.msg("Pendrin moves to stand between you and the sands of time.")
			self.caller.msg("|mPendrin|n says: You may leave when you are ready.")
			return

class PendrinCmdSet(CmdSet):
	key = "PendrinCmdSet"
	def at_cmdset_creation(self):
		self.add(chatpendrin())

class pendrin(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Wrapped in hooded robes that appear to ripple and shift in the colors of the cosmos,  black starry eyes stare at you from deep inside the hood. You almost become lost as you look into the eyes watching scenes of the world flash by, a mountain rises from the depths of an ocean creating an island, a massive war, a tree sprouting-growing-falling in the forest, an egg hatches, grows large, and is caught with a school of fish dragged from the water in a net, the entire rise and fall of an empire, eons of time and events unfolding in the black starry eyes. Two people meet, a love blossoms, graves are filled, a thousand generations later a young woman ascends to power, a thousand generations later again a old feeble and destitute man starves in the gutter. A great fire fills your chest and you break free from the fathomless depths of the eyes."
		self.cmdset.add_default(PendrinCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add('view:not mondef("Pendrin Guardian of Time")')
		self.tags.add("specialnpc")