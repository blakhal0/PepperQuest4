from evennia import default_cmds, CmdSet, search_object, search_tag
from typeclasses.objects import DefaultObject
import typeclasses.weapons as weapons
from evennia.prototypes.spawner import spawn

class chatblacksmith(default_cmds.MuxCommand):
	key = "talk blacksmith"
	aliases = ["Talk Blacksmith", "Talk blacksmith", "talk Blacksmith" ]
	auto_help = True
	def func(self):
		if not self.obj.access(self.caller, "view"):
			self.caller.msg("There's no blacksmith to talk to.")
			return
		def leave():
			self.caller.msg("|/|mBlacksmith|n says: If you manage to not get yourself killed, stop back again!")
			return
		weaponsavailable = []
		playerweapons = []
		answer = yield("|/|mBlacksmith|n says: You looking to buy or sell?|/|gB|nuy, |gS|nell, |gE|nxit")
	#Exit
		if answer.lower() in ["e", "exit"]:
			leave()
			return
	#Buy
		elif answer.lower() in ["b", "buy"]:
		#Build inventory lists
			target = self.caller.search("blacksmith")
			if not target:
				self.caller.msg("|/The merchant unexpectedly runs away")
				return
			for o in self.caller.contents:
				if o.tags.get("equipable", category="weapon"):
					playerweapons.append(o.key)
			for o in target.db.weaponsforsale:
				if getattr(weapons, o).name not in playerweapons:
					weaponsavailable.append(o)
		#Purchase Loop
			while 1 < 10:
				#check if no weapons
				if weaponsavailable == []:
					self.caller.msg("|/|mBlacksmith|n says: Fresh out of weapons 'guv, sorry about that.")
					leave()
					break
				else:
					self.caller.msg("   |/|005.|015:|025*|035~|nWeapons for Sale|035~|025*|015:|005.|n")
					for i in weaponsavailable:
						name = getattr(weapons, i).name
						price = int(getattr(weapons, i).price)
						attack = int(getattr(weapons, i).attack)
						desc = getattr(weapons, i).desc
						self.caller.msg("%s - %d gold, +%d attack.|/	+ %s|/|/" % (name, price, attack, desc))
				#actual buying
				answer = yield("|/Current Weapon: %s, +%d attack.|/|mBlacksmith|n says: Well, how about it, anything catch your eye?|/You have %d gold.|/|gE|nxit to quit." % (self.caller.db.weaponequipped, self.caller.db.equipatt, self.caller.db.gold))
				if answer.lower() in ["e", "exit", "q", "quit"]:
					leave()
					break
				listanswer = answer.replace(" ", "").lower()
				if not listanswer in weaponsavailable:
					self.caller.msg("|/|mBlacksmith|n says: I'm very sorry, I don't have any %s. Please, take another look." % (answer))
					yield 1
					continue
				elif not self.caller.db.gold >= int(getattr(weapons, listanswer).price):
					self.caller.msg("|/|mBlacksmith|n says: You think I slave over the forge fires for free? Go kill some stuff and get some gold.")
					yield 1
					continue
				else:
					self.caller.msg("|/|mBlacksmith|n says: The %s? A wonderful choice made by an exceedingly smart person. Don't forget to equip that, won't do you a lick of good just sitting in your inventory!" % (getattr(weapons, listanswer).name))
					#take gold
					self.caller.db.gold -= int(getattr(weapons, listanswer).price)
					#spawn weapon to player
					w_proto = {
					"key": getattr(weapons, listanswer).name,
					"typeclass": "typeclasses.weapons.%s" % (listanswer),
					"location": self.caller
					}
					spawn(w_proto)
					self.caller.msg("You receive the %s" % (getattr(weapons, listanswer).name))
					#remove weapon from available list
					weaponsavailable.remove(listanswer)
					yield 1
	#Sell
		elif answer.lower() in ["s", "sell"]:
			sell = []
		#Create list of players weapons
			for o in self.caller.contents:
				if o.tags.get("equipable", category="weapon"):
					sell.append(o.key)
			self.caller.msg("|/|mBlacksmith|n says: Okay let's take a look at what you've got...")
			if sell == []:
				self.caller.msg("|mBlacksmith|n says: You having a laugh? You don't have any weapons to sell.")
				leave()
				return
			else:
			#Sell Loop
				while 1 < 10:
					self.caller.msg("|mBlacksmith|n says: Looks like you've got some good loot. Here's what I'll give you, it's a fair price... for me.")
					self.caller.msg("   |/|005.|015:|025*|035~|nSell a Weapon?|035~|025*|015:|005.|n")
					for o in sell:
						target = self.caller.search(o, candidates=self.caller.contents)
						if target.db.name == self.caller.db.weaponequipped:
							self.caller.msg("%s - %d gold. |g*Equipped|n" % (o, int(target.db.price * .75)))
						else:
							self.caller.msg("%s - %d gold." % (o, int(target.db.price * .75)))
					answer = yield("|/|mBlacksmith|n says: So how about it? What do you want to sell?|/You have %d gold.|/|gE|nxit to sell nothing." % (self.caller.db.gold))
					if answer.lower() in ("e", "exit"):
						leave()
						break
					elif not answer.lower() in (i.lower() for i in sell):
						self.caller.msg("|/|mBlacksmith|n says: Nice try, you don't have a %s to sell." % (answer))
						yield 1
						continue
					elif answer.lower() in (i.lower() for i in sell):
						target = self.caller.search(answer.lower(), candidates=self.caller.contents)
						saleprice = int(target.db.price * .75)
						salename = target.db.name
						if target.db.name == self.caller.db.weaponequipped:
							self.caller.db.weaponequipped = "none"
							self.caller.db.equipatt = 0
							self.caller.msg("|/|rYou just sold your equipped weapon. Don't forget to equip a new one!!!|n")
						self.caller.db.gold += saleprice
						sell.remove(target.db.name)
						for i in self.caller.contents:
							if i.key == target.db.name:
								i.delete()
						self.caller.msg("|/|mBlacksmith|n says: I otta be able to make somefing nice out of this.|/You get %d gold, the Blacksmith takes the %s.|/|/" % (saleprice, salename))
						yield 1
						if sell == []:
							self.caller.msg("|/|mBlacksmith|n says: Looks like you've sold the whole lot 'guv.")
							leave()
							break
						continue
					else:
						self.caller.msg("Something went wrong selling a weapon. Tell Blakhal0")
						break
	#Catchall
		else:
			self.caller.msg("|/|mBlacksmith|n says: You're speaking in all 6's and 7's mate. Beat it!")
			return

class WeaponerCmdSet(CmdSet):
	key = "WeaponerCmdSet"
	def at_cmdset_creation(self):
		self.add(chatblacksmith())

class blacksmith(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The Blacksmith sings a song as her hammer rings the steel, thrusting the piece back into the forge they take a break from the tune.|/|mBlacksmith|n says: Best weapons around!! Get 'em while they're hot!!!"
		self.db.weaponsforsale = [""]
		self.tags.add("specialnpc")
		self.tags.add("weaponer")
		self.cmdset.add_default(WeaponerCmdSet, permanent=True)
		self.locks.add("get:false()")