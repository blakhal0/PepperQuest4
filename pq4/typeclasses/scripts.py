"""
Scripts

Scripts are powerful jacks-of-all-trades. They have no in-game
existence and can be used to represent persistent game systems in some
circumstances. Scripts can also have a time component that allows them
to "fire" regularly or a limited number of times.

There is generally no "tree" of Scripts inheriting from each other.
Rather, each script tends to inherit from the base Script class and
just overloads its hooks to have it perform its function.

"""

'''
Create a new script on a single object
script #dbref=scripts.$scriptname

Create a new Global Script
@py evennia.create_script("typeclasses.scripts.scriptname", key="keyname", obj=None)
'''

from evennia import DefaultScript, search_object, search_tag
from evennia.utils.logger import log_file
import random
from random import randint


class Script(DefaultScript):
	"""
	A script type is customized by redefining some or all of its hook
	methods and variables.

	* available properties

	 key (string) - name of object
	 name (string)- same as key
	 aliases (list of strings) - aliases to the object. Will be saved
			  to database as AliasDB entries but returned as strings.
	 dbref (int, read-only) - unique #id-number. Also "id" can be used.
	 date_created (string) - time stamp of object creation
	 permissions (list of strings) - list of permission strings

	 desc (string)	  - optional description of script, shown in listings
	 obj (Object)	   - optional object that this script is connected to
						  and acts on (set automatically by obj.scripts.add())
	 interval (int)	 - how often script should run, in seconds. <0 turns
						  off ticker
	 start_delay (bool) - if the script should start repeating right away or
						  wait self.interval seconds
	 repeats (int)	  - how many times the script should repeat before
						  stopping. 0 means infinite repeats
	 persistent (bool)  - if script should survive a server shutdown or not
	 is_active (bool)   - if script is currently running

	* Handlers

	 locks - lock-handler: use locks.add() to add new lock strings
	 db - attribute-handler: store/retrieve database attributes on this
						self.db.myattr=val, val=self.db.myattr
	 ndb - non-persistent attribute handler: same as db but does not
						create a database entry when storing data

	* Helper methods

	 start() - start script (this usually happens automatically at creation
			   and obj.script.add() etc)
	 stop()  - stop script, and delete it
	 pause() - put the script on hold, until unpause() is called. If script
			   is persistent, the pause state will survive a shutdown.
	 unpause() - restart a previously paused script. The script will continue
				 from the paused timer (but at_start() will be called).
	 time_until_next_repeat() - if a timed script (interval>0), returns time
				 until next tick

	* Hook methods (should also include self as the first argument):

	 at_script_creation() - called only once, when an object of this
							class is first created.
	 is_valid() - is called to check if the script is valid to be running
				  at the current time. If is_valid() returns False, the running
				  script is stopped and removed from the game. You can use this
				  to check state changes (i.e. an script tracking some combat
				  stats at regular intervals is only valid to run while there is
				  actual combat going on).
	  at_start() - Called every time the script is started, which for persistent
				  scripts is at least once every server start. Note that this is
				  unaffected by self.delay_start, which only delays the first
				  call to at_repeat().
	  at_repeat() - Called every self.interval seconds. It will be called
				  immediately upon launch unless self.delay_start is True, which
				  will delay the first call of this method by self.interval
				  seconds. If self.interval==0, this method will never
				  be called.
	  at_stop() - Called as the script object is stopped and is about to be
				  removed from the game, e.g. because is_valid() returned False.
	  at_server_reload() - Called when server reloads. Can be used to
				  save temporary variables you want should survive a reload.
	  at_server_shutdown() - called at a full server shutdown.

	"""

	pass

class muggles(DefaultScript):
	def at_script_creation(self):
		self.key = "mugmove"
		self.interval = 90
		self.persistent = True
	def at_repeat(self):
		npclist = ["#8619", "#8620"]
		for i in npclist:
			target = search_object(i)
			exits = [exi for exi in target[0].location.exits if exi.access(target[0], "traverse")]
			exit = random.choice(exits)
			target[0].move_to(exit.destination)

class casinomover(DefaultScript):
	def at_script_creation(self):
		self.key = "gpcmove"
		self.interval = 60
		self.persistent = True
	def at_repeat(self):
		npclist = ["#9088", "#9087", "#9086", "#9089"]
		for i in npclist:
			target = search_object(i)
			exits = [exi for exi in target[0].location.exits if not exi.tags.get("nonpcs")]
			exit = random.choice(exits)
			target[0].move_to(exit.destination)
#			target[0].move_to(exit.destination, quiet=True, move_hooks = False)

class spicemerchantcaravan(DefaultScript):
	def at_script_creation(self):
		self.key = "spicemerchcarmove"
		self.interval = 420
		self.persistent = True
	def at_repeat(self):
		stops = ["#3106", "#3151", "#3624", "#3434", "#3343", "#3257", "#3286", "#3369", "#3511", "#3655", "#3128"]
		spicemerchant = search_object("#9292")
		spicemerchant = spicemerchant[0]
		spiceworm = search_object("#9294")
		spiceworm = spiceworm[0]
	#check if merchant is talking, if talking remove talking tag and exit
		if spicemerchant.tags.get("doingbusiness"):
			spicemerchant.tags.remove("doingbusiness")
			return
	#Move merchant inside worm object
		if not spicemerchant.location.key == spiceworm.key:
			spicemerchant.move_to(spiceworm, quiet=False, move_hooks=True)
	#Determine next location
		currentlocationinlist = stops.index(spiceworm.db.currentstop)
		if currentlocationinlist == len(stops) - 1:
			nextlocation = stops[0]
		else:
			nextlocation = stops[currentlocationinlist + 1]
	#Update location holder on worm object
		spiceworm.db.currentstop = nextlocation
	#Setup nextlocation
		nextlocation = search_object(nextlocation)
		nextlocation = nextlocation[0]
	#Message locations between???
#		
	#Move worm
		spiceworm.move_to(nextlocation, quiet=False, move_hooks=True)
	#Extract Merchant
		if spicemerchant.location.key == spiceworm.key:
			spicemerchant.move_to(spiceworm.location, quiet=False, move_hooks=True)


class cod(DefaultScript):
	def at_script_creation(self):
		self.key = "codscript"
		self.interval = 20
		self.persistent = True
	def at_repeat(self):
		phrases = ["I'm here to en'hen'ce your experience. BAWWWKAAWKAWKAWKAWK!", "Have I beaked your interest? BAWWWWK!!!", "The cluck is ticking...bok...bok...bok", "Don't make me flock you in the nose...", "How about a sneak beak of your demise? *evil bawks*", "Bawk Bawk", "BAWWWWWK", "Bawwwk ba-GAWWWWWWWWK", "*Chicken of Doom clucks in an evil tone*", "Baaawwwk bawk-bawwk, cluck", "YOUR SOUL WILL BE-GAWWWWWK MINE!", "Cluck you! Pathetic mortal! BAWGAWWWK"]
		target = search_object(self.obj.location)
		if not target:
			return
		if not target[0].has_account:
			chicken = search_object("Chicken of Doom")
			if chicken[0].db.idlecount <= 15:
				chicken[0].db.idlecount += 1
			if chicken[0].db.idlecount > 15:
				respawn = search_object(random.choice(chicken[0].db.spawnlocations))
				chicken[0].location.msg_contents("|/|rThe Chicken of Doom glows with an evil aura, crows loudly, and disappears.|n")
				log_file("Chicken moved to %s" % str(respawn[0]), filename="chicken.log")
				chicken[0].move_to(respawn[0], quiet=True, move_hooks=False)
				chicken[0].db.idlecount = 0
			return
		if target[0].tags.get("battle"):
			return
		else:
			if randint(1, 5) in [1, 3]:
				if randint(1, 10) == 3:
					target[0].msg("|/The Chicken of Doom begins to glow with an evil aura....|/BaGAwwwwAAAAAK! It laid a doom egg!")
					if randint(1, 2) == 1:
						target[0].msg("|gThe Doom Egg hatches, it's full of gold!!! You gain 10,000 gold.|n")
						target[0].db.gold += 10000
						return
					else:
						target[0].msg("|rThe Doom Egg hatches, you die instantly... from DOOM!!!!!!|n")
						target[0].db.hp = 0
				else:
					damage = randint(1,15)
					target[0].db.hp -= int(damage)
					target[0].msg("|/|rThe Chicken of Doom pecks you mercilessly, you lose %d hit points." % (damage))
				if target[0].db.hp <= 0:
					target[0].msg("|/|rWhat tragic fate, you have been killed by the Chicken of Doom.")
					target[0].db.deathcount += 1
					target[0].db.hp = int(target[0].db.maxhp * .5)
					target[0].db.hp = int(target[0].db.maxmp * .5)
					target[0].db.gold -= int(target[0].db.gold * .2)
					results = search_object(target[0].db.lastcity)
					target[0].move_to(results[0], quiet=True, move_hooks=False)
					chicken = search_object("Chicken of Doom")
					respawn = search_object(random.choice(chicken[0].db.spawnlocations))
					log_file("Chicken moved to %s" % str(respawn[0]), filename="chicken.log")
					chicken[0].move_to(respawn[0], quiet=True, move_hooks=False)
					chicken[0].db.idlecount = 0
					target[0].msg("|/The Chicken of Doom wipes its blood covered beak on your armor, crows in victory, takes a last peck at your eyeball, and vanishes.|/You no longer hold the Chicken of Doom.")
					return
			else:
				chickenwarcry = random.choice(phrases)
				target[0].msg("|/|mChicken of Doom|n says: %s|/" % (chickenwarcry))
				return

class armorscript(DefaultScript):
	def at_script_creation(self):
		self.key = "armor_script"
		self.interval = 60
		#self.persistent = True
	def at_repeat(self):
		heallist = search_tag(key="sainted")
		for i in heallist:
			target = search_object(i.location)
			if target[0].has_account:
				if not target[0].tags.get("battle"):
					if target[0].db.armorequipped == i.key:
						if target[0].location.tags.get("cursedlocation"):
							target[0].msg("|/|gThere is an evil aura in this place.|/The %s's blessing has no effect here.|n" % (i.key))
							pass
						elif target[0].db.hp + i.db.heal < target[0].db.maxhp:
							target[0].db.hp += i.db.heal
							target[0].msg("|/|gThe %s heals your wounds.|n" % (i.key))
						else:
							pass
					else:
						pass
				else:
					pass
			else:
				pass
		unheallist = search_tag(key="cursed")
		for i in unheallist:
			target = search_object(i.location)
			if target[0].has_account:
				if not target[0].tags.get("battle"):
					if target[0].db.armorequipped == i.key:
						if target[0].location.tags.get("cursedlocation"):
							if target[0].db.hp + i.db.unheal * 2 < target[0].db.maxhp:
								target[0].db.hp += i.db.unheal * 2
								target[0].msg("|/|gThere is an evil aura in this place.|/The %s's curse bolsters your vitality, you gain %d hp.|n" % (i.key, i.db.unheal * 2))
							else:
								pass
						elif target[0].db.hp - i.db.unheal > 0:
							target[0].db.hp -= i.db.unheal
							target[0].msg("|/|rThe %s's curse exacts its toll, you lose %d hp.|n" % (i.key, i.db.unheal))
						else:
							pass
					else:
						pass
				else:
					pass
			pass
		return

class poisonscript(DefaultScript):
	def at_script_creation(self):
		self.key = "poisonroomscript"
		self.interval = 5
		self.persistent = True
	def at_repeat(self):
		#build list of rooms
		for i in search_tag("poisonroom"):
			#get contents
			for x in i.contents:
				if x.tags.get("poisonproof"):
					continue
				#skip players in a battle
				if x.tags.get("battle"):
					continue
				#define players and make sure they're connected
				if x.permissions.get("player") and x.has_account:
					x.db.hp -= i.db.poisondamage
					if x.db.hp <= 0:
						x.msg("|/|rWhat tragic fate, you are dead.|n|/You have brought shame to yourself and your family.")
						x.db.deathcount += 1
						x.db.hp = int(x.db.maxhp * .5)
						x.db.mp = int(x.db.maxmp * .5)
						x.db.gold -= int(x.db.gold * .2)
						results = search_object(x.db.lastcity)
						x.move_to(results[0], quiet=True, move_hooks=False)
						continue
					else:
						x.msg("|/|r%s, you lose %d hp.|n" % (i.db.damagemsg, i.db.poisondamage))
						continue

class poisonroomslow(DefaultScript):
	def at_script_creation(self):
		self.key = "poisonroomslowscript"
		self.interval = 15
		self.persistent = True
	def at_repeat(self):
		slowpoisonrooms = ["#4502", "#4505", "#4508", "#4511", "#4514", "#4517", "#4520", "#4523", "#4526", "#4529", "#4532", "#4537", "#4540", "#4545", "#4550", "#4553", "#4556", "#4561", "#4564", "#4575", "#4578", "#4581", "#4584", "#4587", "#4590", "#4593", "#4608", "#4611", "#4614", "#4617", "#4620", "#4623", "#4626", "#4629", "#4652", "#4655", "#4658", "#4661", "#4664", "#4667", "#4670", "#4673", "#4676", "#4679", "#4682", "#4685", "#4688", "#4697", "#4700", "#4703", "#4706", "#4709", "#4712", "#4721", "#4724", "#4727", "#4730", "#4743", "#4746", "#4749", "#4752", "#4765", "#4768", "#4771", "#4774", "#4787", "#4790", "#4793", "#4796", "#4809", "#4812", "#4815", "#4818", "#4839", "#4842", "#4845", "#4848", "#4851", "#4854", "#4860", "#4863", "#4866", "#4869", "#4872", "#4875", "#4878", "#4881", "#4884", "#4887", "#4890", "#4893", "#4896", "#4899", "#4902", "#4905", "#4908", "#4911", "#4914", "#4917", "#4920", "#4923", "#4926", "#4929", "#4932", "#4935", "#4938", "#4941", "#4944", "#4947", "#4950", "#4953", "#4956", "#4959", "#4962", "#4965", "#4968", "#4971", "#4974", "#4977", "#4980", "#4983", "#4986", "#4989", "#4992", "#4995", "#5030", "#5033", "#5036", "#5039", "#5052", "#5055", "#5058", "#5061", "#5064", "#5067", "#5084", "#5087", "#5090", "#5093", "#5096", "#5099", "#5102", "#5105", "#5126", "#5129", "#5132", "#5135", "#5138", "#5141", "#5144", "#5147", "#5150", "#5153", "#5180", "#5183", "#5186", "#5189", "#5192", "#5195", "#5198", "#5201", "#5204", "#5207", "#5234", "#5237", "#5240", "#5243", "#5246", "#5249", "#5252", "#5255", "#5258", "#5261", "#5266", "#5295", "#5298", "#5301", "#5304", "#5307", "#5310", "#5313", "#5316", "#5339", "#5342", "#5345", "#5348", "#5351", "#5354", "#5357", "#5376", "#5379", "#5382", "#5385", "#5388", "#5391", "#5394", "#5415", "#5418", "#5421", "#5424", "#5427", "#5430", "#5449", "#5452", "#5455", "#5458", "#5461", "#5480", "#5483", "#5486"]
		for i in slowpoisonrooms:
			results = search_object(i)
			if not results[0].contents:
				continue
			for x in results[0].contents:
				if not x.permissions.get("player") and not x.has_account:
					continue
				if x.tags.get("poisonproof"):
					continue
				if x.tags.get("battle"):
					continue
#				if x.permissions.get("player") and x.has_account:
				x.db.hp -= results[0].db.poisondamage
				if x.db.hp <= 0:
					x.msg("|/|rWhat tragic fate, you are dead.|n|/You have brought shame to yourself and your family.")
					x.db.deathcount += 1
					x.db.hp = int(x.db.maxhp * .5)
					x.db.mp = int(x.db.maxmp * .5)
					x.db.gold -= int(x.db.gold * .2)
					results = search_object(x.db.lastcity)
					x.move_to(results[0], quiet=True, move_hooks=False)
					continue
				else:
					x.msg("|/|r%s, you lose %d hp.|n" % (results[0].db.damagemsg, results[0].db.poisondamage))
					continue


class libvamp(DefaultScript):
	def at_script_creation(self):
		self.key = "libvamp"
		self.interval = 30
		self.persistent = True
	def at_repeat(self):
		libraryrooms = ["#9730", "#9725", "#9722", "#9719", "#9716"]
		vampsays = ["1024 vampires all bite you, it's a MegaBite.", "A frozen vampire attacks, it's a frostbite.", "Be at ease, I'm a Doctor. Dr. Acula!", "I need your blood for my cold, I've really been coffin."]
		for i in libraryrooms:
			results = search_object(i)
			if not results[0].contents:
				continue
			for x in results[0].contents:
			#define players and make sure they're connected
				if x.permissions.get("player") and x.has_account:
					x.db.hp -= 6
					if x.db.hp <= 0:
						x.msg("|/|rWhat tragic fate, you are dead.|n|/You have brought shame to yourself and your family.")
						x.db.deathcount += 1
						x.db.hp = int(x.db.maxhp * .5)
						x.db.mp = int(x.db.maxmp * .5)
						x.db.gold -= int(x.db.gold * .2)
						results = search_object(x.db.lastcity)
						x.move_to(results[0], quiet=True, move_hooks=False)
						continue
					else:
						x.msg("|/|rYou hear soft steps, feel an eerie presence behind you, and a light breath on your neck.|/%s You feel light headed. You lose 6 hp.|n" % (random.choice(vampsays)))
						continue