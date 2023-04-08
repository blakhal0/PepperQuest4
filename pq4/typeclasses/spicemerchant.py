from evennia import default_cmds, CmdSet, search_object, search_tag
from typeclasses.objects import DefaultObject
import typeclasses.armor as armor
import typeclasses.weapons as weapons
import typeclasses.items as items
from evennia.prototypes.spawner import spawn


class chatspicemerchant(default_cmds.MuxCommand):
	key = "talk spice merchant"
	aliases = ["Talk Spice Merchant", "Talk Spice merchant", "Talk spice merchant", "talk Spice Merchant", "talk Spice merchant"]
	auto_help = True
	def func(self):
		def leave():
			target.tags.remove("doingbusiness")
			self.caller.msg("|/|mSpice Merchant|n says: Farewell friend, may you always find shade and water.")
			return
		armoravailable = []
		playerarmor = []
		weaponsavailable = []
		playerweapons = []
		itemsavailable = []
		monsterbellavail = "yes"
		target = self.caller.search("spice merchant")
		if not target.tags.get("doingbusiness"):
			target.tags.add("doingbusiness")
		answer = yield("|/|mSpice Merchant|n says: Welcome friend, welcome. Welcome to the traveling spice merchant caravan! Look, look. Many fantastic things from our travels, some things not found anywhere else.|/|cB|nuy |cE|nxit.")
	#Exit
		if answer.lower() in ["e", "exit"]:
			leave()
			return
	#Buy
		elif answer.lower() in ["b", "buy"]:
		#Build inventory lists
			if not target:
				self.caller.msg("|/The merchant unexpectedly runs away")
				return
		#Player inventory
			for o in self.caller.contents:
				if o.tags.get("equipable", category="armor") or o.tags.get("equipable", category="shield"):
					playerarmor.append(o.key)
				if o.tags.get("equipable", category="weapon"):
					playerweapons.append(o.key)
				if o.key == "Monster Bell":
					monsterbellavail = "no"
		#armor list
			if playerarmor == []:
				armoravailable = target.db.armorforsale.copy()
			else:
				for o in target.db.armorforsale:
					if getattr(armor, o).name not in playerarmor:
						armoravailable.append(o)
		#weapons list
			if playerweapons == []:
				weaponsavialable = target.db.weaponsforsale.copy()
			else:
				for o in target.db.weaponsforsale:
					if getattr(weapons, o).name not in playerweapons:
						weaponsavailable.append(o)
		#itemslist
			itemsavailable = target.db.itemsforsale.copy()
		#Purchase Loop
			while 1 < 10:
			#check if nothing left to sell
				if armoravailable == [] and weaponsavailable == [] and target.db.itemsforsale == []:
					self.caller.msg("|/|mSpice Merchant|n says: Well, you've bought me out of wares!")
					leave()
					break
				else:
					self.caller.msg("	|/|005.|015:|025*|035~|nThings for Sale|035~|025*|015:|005.|n")
					for i in armoravailable:
						name = getattr(armor, i).name
						price = int(getattr(armor, i).price)
						defense = int(getattr(armor, i).defense)
						desc = getattr(armor, i).desc
						self.caller.msg("%s - %d gold, +%d defense.|/	+ %s|/|/" % (name, price, defense, desc))
					for i in weaponsavailable:
						name = getattr(weapons, i).name
						price = int(getattr(weapons, i).price)
						attack = int(getattr(weapons, i).attack)
						desc = getattr(weapons, i).desc
						self.caller.msg("%s - %d gold, +%d attack.|/	+ %s|/|/" % (name, price, attack, desc))
					for i in itemsavailable:
						name = getattr(items, i).name
						price = int(getattr(items, i).price)
						desc = getattr(items, i).desc
						self.caller.msg("%s - %d gold. %s|/|/" % (name, price, desc))
					if monsterbellavail == "yes":
						self.caller.msg("Monster Bell - 500 gold. A small, ornate, golden bell in the shape of a monster. Calls monsters to battle instantly.")
			#actual buying
				answer = yield("|/Current Weapon: %s, +%d attack.|/Current Armor: %s, +%d defense.|/Current Shield: %s, %d defense.|/|mSpice Merchant|n says: Please, please. Look.|/You have %d gold.|/|gE|nxit to quit." % (self.caller.db.weaponequipped, self.caller.db.equipatt, self.caller.db.armorequipped, self.caller.db.equipdef, self.caller.db.shieldequipped, self.caller.db.shielddef, self.caller.db.gold))
				if answer.lower() in ["e", "exit", "q", "quit"]:
					leave()
					break
				listanswer = answer.replace(" ", "").lower()
				if not listanswer in armoravailable and not listanswer in weaponsavailable and not listanswer in itemsavailable and not answer.lower() == "monster bell":
					self.caller.msg("|/|mSpice Merchant|n says: Humm, let me check the trunks on the spice worms. No, no we don't have any %s." % (answer))
					yield 1
					continue
			#armor
				if listanswer in armoravailable:
					if not self.caller.db.gold >= int(getattr(armor, listanswer).price):
						self.caller.msg("|/|mSpice Merchant|n says: Traveling the desert is hard work, we don't give things away for free! You need more gold friend.")
						yield 1
						continue
					else:
						self.caller.msg("|/|mSpice Merchant|n says: The %s? Yes, this is very good. I have used the same to defend the caravan many times. As you see, I am still here." % (getattr(armor, listanswer).name))
						#take gold
						self.caller.db.gold -= int(getattr(armor, listanswer).price)
					#spawn armor to player
						a_proto = {
						"key": getattr(armor, listanswer).name,
						"typeclass": "typeclasses.armor.%s" % (listanswer),
						"location": self.caller
						}
						spawn(a_proto)
						self.caller.msg("You receive the %s" % (getattr(armor, listanswer).name))
					#remove armor from available list
						armoravailable.remove(listanswer)
						yield 1
						continue
			#weapons
				if listanswer in weaponsavailable:
					if not self.caller.db.gold >= int(getattr(weapons, listanswer).price):
						self.caller.msg("|/|mSpice Merchant|n says: Traveling the desert is hard work, we don't give things away for free! You need more gold friend.")
						yield 1
						continue
					else:
						self.caller.msg("|/|mSpice Merchant|n says: The %s? Yes, this is very good. I have used one to defend the caravan many times. All have fallen before it." % (getattr(armor, listanswer).name))
						#take gold
						self.caller.db.gold -= int(getattr(weapons, listanswer).price)
					#spawn weapons to player
						w_proto = {
						"key": getattr(weapons, listanswer).name,
						"typeclass": "typeclasses.weapons.%s" % (listanswer),
						"location": self.caller
						}
						spawn(w_proto)
						self.caller.msg("You receive the %s" % (getattr(weapons, listanswer).name))
					#remove weapons from available list
						weaponsavailable.remove(listanswer)
						yield 1
						continue
			#items
				if listanswer in itemsavailable:
					if not self.caller.db.gold >= int(getattr(items, listanswer).price):
						self.caller.msg("|/|mSpice Merchant|n says: Traveling the desert is hard work, we don't give things away for free! You need more gold friend.")
						yield 1
						continue
					else:
						ansqty = yield("|/|mSpice Merchant|n says: The %s? Humm, yes, yes, we have many of these.|/How many do you want?" % (getattr(items, listanswer).name))
						if not ansqty.isnumeric():
							self.caller.msg("|/|mSpice Merchant|n says: I would suggest not trying such tricks around here. There are many holes in the desert. Surely we could find one you fit in.")
							yield 1
							continue
						elif int(ansqty) < 0:
							self.caller.msg("|/|mSpice Merchant|n says: I would suggest not trying such tricks around here. There are many holes in the desert. Surely we could find one you fit in.")
							yield 1
							continue
						elif int(ansqty) == 0:
							self.caller.msg("|/|mSpice Merchant|n says: No? This is fine. Many many other items for sale.")
							yield 1
							continue
						elif int(ansqty) * int(getattr(items, listanswer).price) > self.caller.db.gold:
							self.caller.msg("|/|mSpice Merchant|n says: Your gold is too short and your request too large. Maybe a few less?")
							yield 1
							continue
						else:
							totalprice = int(ansqty) * int(getattr(items, listanswer).price)
							self.caller.db.gold -= totalprice
							#Check if player already has the item
							target = self.caller.search(answer.lower(), candidates=self.caller.contents, quiet=True)
							if not target:
							#spawn item to player
								i_proto = {
								"key": getattr(items, listanswer).name,
								"typeclass": "typeclasses.items.%s" % (listanswer),
								"qty": int(ansqty),
								"location": self.caller
								}
								spawn(i_proto)
							else:
								target[0].db.qty += int(ansqty)
							self.caller.msg("|/You receive %d %s and pay %d gold." % (int(ansqty), getattr(items, listanswer).name, totalprice))
							yield 1
							continue
			#monster bell
				if listanswer == "monsterbell":
					if not self.caller.db.gold >= 500:
						self.caller.msg("|/|mSpice Merchant|n says: Traveling the desert is hard work, we don't give things away for free! You need more gold friend.")
						yield 1
						continue
					else:
						self.caller.msg("|/|mSpice Merchant|n says: Ah, yes. A very special item indeed. Very rare, very useful. Only made in one place in the world, and only we know where.")
						#take gold
						self.caller.db.gold -= 500
					#spawn weapons to player
						mb_proto = {
						"key": "Monster Bell",
						"typeclass": "typeclasses.monsterbell.monsterbell",
						"location": self.caller
						}
						spawn(mb_proto)
						self.caller.msg("You receive the Monster Bell.")
					#remove weapons from available list
						monsterbellavail = "no"
						yield 1
						continue
	#Catchall
		else:
			self.caller.msg("|/|mSpice Merchant|n says: I think you've been out in the sun too long! Take your madness and go.")
			leave()
			return


class SpiceMerchantCmdSet(CmdSet):
	key = "SpiceMerchantCmdSet"
	def at_cmdset_creation(self):
		self.add(chatspicemerchant())

class spicemerchant(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A kind hand brushes the finger like hairs on the spice worm in a calming gesture.|/|mSpice Merchant|n says: There, there Alluaudia, we rest now and wait. Oh, greetings friend. Have no fear of the great spice worm.|/The Spice Merchant removes their head wrappings revealing short red hair, many jeweled earrings, and a crafty smile.|/|mSpice Merchant|n says: I represent the traveling merchants guild. We travel the Cashmere Highway through the desert on the backs of the great spice worms bringing goods to all."
		self.db.armorforsale = ['peacockpeacoat', 'scalemail']
		self.db.weaponsforsale = ['snakewhip']
		self.db.itemsforsale = ['pocketsand', 'restoringruby', 'yorkshiretea']
		self.db.specialarrivemsg = "drops from the back of the great spice worm, quickly erecting a small tent and spreading a colorful rug in front of it."
		self.db.specialleavemsg = "packs up their goods, collapses the tent and climbs onto the back of the great spice worm."
		self.cmdset.add_default(SpiceMerchantCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")