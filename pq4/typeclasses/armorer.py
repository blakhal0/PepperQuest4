from evennia import default_cmds, CmdSet, search_object, search_tag
from typeclasses.objects import DefaultObject
import typeclasses.armor as armor
from evennia.prototypes.spawner import spawn


class chatarmorer(default_cmds.MuxCommand):
	key = "talk armorer"
	aliases = ["Talk Armorer", "Talk armorer", "talk Armorer" ]
	auto_help = True
	def func(self):
		if not self.obj.access(self.caller, "view"):
			self.caller.msg("There's no armorer to talk to.")
			return
		def leave():
			self.caller.msg("|/|mArmorer|n says: Please, don't stay away too long! |r<3 *MUAH*|n")
			return
		armoravailable = []
		playerarmor = []
		answer = yield("|/|mArmorer|n says: Can I get you something, or giiive you something? *ohhh ho ho ho*|/|gB|nuy, |gS|nell, |gE|nxit")
	#Exit
		if answer.lower() in ["e", "exit"]:
			leave()
			return
	#Buy
		elif answer.lower() in ["b", "buy"]:
		#Build inventory lists
			target = self.caller.search("armorer")
			if not target:
				self.caller.msg("|/The merchant unexpectedly runs away")
				return
			for o in self.caller.contents:
				if o.tags.get("equipable", category="armor") or o.tags.get("equipable", category="shield"):
					playerarmor.append(o.key)
			if playerarmor == []:
				armoravailable = target.db.armorforsale.copy()
			else:
				for o in target.db.armorforsale:
					if getattr(armor, o).name not in playerarmor:
						armoravailable.append(o)
		#Purchase Loop
			while 1 < 10:
				#check if no armor
				if armoravailable == []:
					self.caller.msg("|/|mArmorer|n says: Oh, goodness, I'm skint on armor right now. Unless you want the shirt off my back... *ouuwww hehehehe*")
					leave()
					break
				else:
					self.caller.msg("	|/|005.|015:|025*|035~|nArmor for Sale|035~|025*|015:|005.|n")
					for i in armoravailable:
						name = getattr(armor, i).name
						price = int(getattr(armor, i).price)
						defense = int(getattr(armor, i).defense)
						desc = getattr(armor, i).desc
						self.caller.msg("%s - %d gold, +%d defense.|/	+ %s|/|/" % (name, price, defense, desc))
				#actual buying
				answer = yield("|/Current Armor: %s, +%d defense.|/Current Shield: %s, %d defense.|/|mArmorer|n says: Anything catch your eye? Aside from me that is. *teehehehehe*|/You have %d gold.|/|gE|nxit to quit." % (self.caller.db.armorequipped, self.caller.db.equipdef, self.caller.db.shieldequipped, self.caller.db.shielddef, self.caller.db.gold))
				if answer.lower() in ["e", "exit", "q", "quit"]:
					leave()
					break
				listanswer = answer.replace(" ", "").lower()
				if not listanswer in armoravailable:
					if listanswer == "kiss":
						if self.caller.tags.get("heartbreaker"):
							self.caller.msg("|/|mArmorer|n says: You think your kisses will just buy you anything? That was a one time deal!")
							yield 1
							continue
						else:
							self.caller.msg("|/|mArmorer|n says: OOOHH, I thought you'd just never ask!! *Tehehehehe*|/The burly armorer adjusts his leather apron, smooths back an unruly mustache, and leans in for a kiss.")
							self.caller.msg("|r*SMOOOOOOOCH*|n")
							yield 1
							self.caller.msg("|mArmorer|n says: Ohhhhh myyyyyyyy. What a kisser!!! I'm just head over heals in LOVE!!!")
							self.caller.tags.add("sweetheartdeal")
							yield 1
							continue
					else:
						self.caller.msg("|/|mArmorer|n says: Oh no.. I don't have any %s. Please, ask me for just anything else." % (answer))
					yield 1
					continue
				elif not self.caller.db.gold >= int(getattr(armor, listanswer).price):
					self.caller.msg("|/|mArmorer|n says: You're just adorrrrable, truly. But I don't give things away for free. Go shake that money maker and get some gold!")
					yield 1
					continue
				else:
					self.caller.msg("|/|mArmorer|n says: The %s? Perfect, it'll fit you like a glove. A tight, thin, not there in just the right places glove, mmmmmm. *grrrrr*" % (getattr(armor, listanswer).name))
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
	#Sell
		elif answer.lower() in ["s", "sell"]:
			sell = []
		#Create list of players armor
			for o in self.caller.contents:
				if o.tags.get("equipable", category="armor") or o.tags.get("equipable", category="shield"):
					sell.append(o.key)
			self.caller.msg("|/|mArmorer|n says: Well, come on over and let me see... what... you've... GOT! *mmmhmmmmm*")
			if sell == []:
				self.caller.msg("|mArmorer|n says: OH! You played a trick on me!! There's nothing in your bag for sale. How delightfully mischievous!!")
				leave()
				return
			else:
			#Sell Loop
				while 1 < 10:
					self.caller.msg("|mArmorer|n says: Hmmmm, yes, there's some items of nice potential in here.")
					if self.caller.tags.get("sweetheartdeal"):
						self.caller.msg("|mArmorer|n says: I'll tell you what hotlips, just between you and me, I'll give you little better deal on one item of your choice.")
						rate = 3
					else:
						rate = .75
					self.caller.msg("   |/|005.|015:|025*|035~|nSell Armor?|035~|025*|015:|005.|n")
					for o in sell:
						target = self.caller.search(o, candidates=self.caller.contents)
						if target.db.name == self.caller.db.armorequipped or target.db.name == self.caller.db.shieldequipped:
							self.caller.msg("%s - %d gold. |g*Equipped|n" % (o, int(target.db.price * rate)))
						else:
							self.caller.msg("%s - %d gold." % (o, int(target.db.price * rate)))
					answer = yield("|/|mArmorer|n says: Anything looking good. BESIDES me of course. *hehehehehe*|/You have %d gold.|/|gE|nxit to sell nothing." % (self.caller.db.gold))
					if answer.lower() in ("e", "exit"):
						leave()
						break
					elif not answer.lower() in (i.lower() for i in sell):
						self.caller.msg("|/|mArmorer|n says: You won't fool me so easy cutiepie, you don't have a %s to sell." % (answer))
						yield 1
						continue
					elif answer.lower() in (i.lower() for i in sell):
						target = self.caller.search(answer.lower(), candidates=self.caller.contents)
						saleprice = int(target.db.price * rate)
						salename = target.db.name
						if target.db.name == self.caller.db.armorequipped:
							self.caller.db.armorequipped = "none"
							self.caller.db.equipdef = 0
							self.caller.msg("|/|rYou just sold your equipped armor. Don't forget to equip something else!!! Can't be running around naked.|n")
						if target.db.name == self.caller.db.shieldequipped:
							self.caller.db.shieldequipped = "none"
							self.caller.db.shielddef = 0
							self.caller.msg("|/|rYou just sold your equipped shield. Don't forget to equip something else!!!|n")
						self.caller.db.gold += saleprice
						sell.remove(target.db.name)
						for i in self.caller.contents:
							if i.key == target.db.name:
								i.delete()
						if self.caller.tags.get("sweetheartdeal"):
							self.caller.tags.remove("sweetheartdeal")
							self.caller.tags.add("heartbreaker")
						self.caller.msg("|/|mArmorer|n says: Mmmmm, oh yes, this should turn out lovely with a little work.|/You get %d gold, the Armorer takes the %s.|/|/" % (saleprice, salename))
						yield 1
						if sell == []:
							self.caller.msg("|/|mArmorer|n says: Oh goodness, I'm all out of armor. Just my apron left, if you want that too. *oohhhhhuuuuu* |r<3|n")
							leave()
							break
						continue
					else:
						self.caller.msg("Something went wrong selling armor. Tell Blakhal0")
						break
	#Catchall
		else:
			self.caller.msg("|/|mArmorer|n says: Your beauty is just intoxicating, I can't understand a single thing you're saying!")
			return


class ArmorerCmdSet(CmdSet):
	key = "ArmorerCmdSet"
	def at_cmdset_creation(self):
		self.add(chatarmorer())

class armorer(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A hulking man drips sweat, massive arms raining down hammer blows on a piece of work. Wearing nothing but a long, thick leather apron and a smile, the armorer turns and smiles seeing you."
		self.db.armorforsale = [""]
		self.cmdset.add_default(ArmorerCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.tags.add("armorer")