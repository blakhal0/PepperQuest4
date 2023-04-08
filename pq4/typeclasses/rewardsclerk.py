from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject
import typeclasses.armor as armor
import typeclasses.weapons as weapons
import typeclasses.items as items
from evennia.prototypes.spawner import spawn

class chatrewardsclerk(default_cmds.MuxCommand):
	key = "talk rewards clerk"
	aliases = ["Talk Rewards Clerk", "Talk Rewards clerk", "talk rewards Clerk", "talk clerk", "Talk Clerk"]
	auto_help = True
	def func(self):
		if not self.obj.access(self.caller, "view"):
			self.caller.msg("There's no one by that name to talk to.")
			return
		def leave():
			self.caller.msg("|mRewards Clerk|n says: Thanks for stopping by! Have a great day and good luck!")
			return
		armoravailable = []
		playerarmor = []
		weaponsavailable = []
		playerweapons = []
		itemsavailable = []
		monsterbellavail = "yes"
		target = self.caller.search("Rewards Clerk", quiet=True)
		target = target[0]
		self.caller.msg("|/|mRewards Clerk|n says: Welcome to The Golden Parliament Casino! We have some absolutely wonderful items you can exchange your tokens for! Of course you can just trade them in for gold, but you only get 1 gold per 2 tokens.|/Have a look at the fantastic items we have!")
	#Build inventory lists
		#Player inventory
		for o in self.caller.contents:
				if o.tags.get("equipable", category="armor") or o.tags.get("equipable", category="shield"):
					playerarmor.append(o.key)
				if o.tags.get("equipable", category="weapon"):
					playerweapons.append(o.key)
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
					price = int(getattr(armor, i).tokens)
					defense = int(getattr(armor, i).defense)
					desc = getattr(armor, i).desc
					self.caller.msg("%s - %d tokens, +%d defense.|/	+ %s|/|/" % (name, price, defense, desc))
				for i in weaponsavailable:
					name = getattr(weapons, i).name
					price = int(getattr(weapons, i).tokens)
					attack = int(getattr(weapons, i).attack)
					desc = getattr(weapons, i).desc
					self.caller.msg("%s - %d tokens, +%d attack.|/	+ %s|/|/" % (name, price, attack, desc))
				for i in itemsavailable:
					name = getattr(items, i).name
					price = int(getattr(items, i).tokens)
					desc = getattr(items, i).desc
					self.caller.msg("%s - %d tokens. %s|/|/" % (name, price, desc))
				if self.caller.db.tokens > 2:
					self.caller.msg("Gold - 1 Gold for 2 Tokens, Total of %d Gold.|/ |/" % (int(self.caller.db.tokens / 2)))
		#actual buying
			answer = yield("|mRewards Clerk|n says: Isn't it all just amazing! You have %d tokens. What would you like?|/|cE|nxit to leave." % (self.caller.db.tokens))
			if answer.lower() in ["e", "exit", "q", "quit"]:
				leave()
				break
			if answer.lower() in ["gold"]:
				if self.caller.db.tokens > 2:
					self.caller.msg("|mRewards Clerk|n says: Sure thing, %d gold coming up!" % (int(self.caller.db.tokens / 2)))
					self.caller.db.gold += int(self.caller.db.tokens / 2)
					self.caller.db.tokens = 0
					leave()
					break
				else:
					self.caller.msg("|mRewards Clerk|n says: I'm sorry, it appears you don't have enough tokens to cash out in gold.")
					continue
			listanswer = answer.replace(" ", "").lower()
			if not listanswer in armoravailable and not listanswer in weaponsavailable and not listanswer in itemsavailable:
				self.caller.msg("|/|mRewards Clerk|n says: Uhhh, I don't think we have any %s." % (answer))
				yield 1
				continue
		#armor
			if listanswer in armoravailable:
				if not self.caller.db.tokens >= int(getattr(armor, listanswer).tokens):
					self.caller.msg("|/|mRewards Clerk|n says: Looks like you're a little short on tokens, you should go win some more!")
					yield 1
					continue
				else:
					self.caller.msg("|/|mRewards Clerk|n says: The %s? It is marvelous isn't it!" % (getattr(armor, listanswer).name))
					#take gold
					self.caller.db.tokens -= int(getattr(armor, listanswer).tokens)
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
				if not self.caller.db.tokens >= int(getattr(weapons, listanswer).tokens):
					self.caller.msg("|/|mRewards Clerk|n says: Looks like you're a little short on tokens, you should go win some more!")
					yield 1
					continue
				else:
					self.caller.msg("|/|mRewards Clerk|n says: The %s? Wicked looking bit of work. Should keep you plenty safe." % (getattr(weapons, listanswer).name))
					#take gold
					self.caller.db.tokens -= int(getattr(weapons, listanswer).tokens)
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
				if not self.caller.db.tokens >= int(getattr(items, listanswer).tokens):
					self.caller.msg("|/|mRewards Clerk|n says: Looks like you're a little short on tokens, you should go win some more!")
					yield 1
					continue
				else:
					ansqty = yield("|/|mRewards Clerk|n says: The %s? You bet! I've got just tons of them, the traveling merchants were just here the other day.|/How many do you want?" % (getattr(items, listanswer).name))
					if not ansqty.isnumeric():
						self.caller.msg("|/|mRewards Clerk|n says: I would hate to have to call the goons over...")
						yield 1
						continue
					elif int(ansqty) < 0:
						self.caller.msg("|/|mRewards Clerk|n says: I would hate to have to call the goons over...")
						yield 1
						continue
					elif int(ansqty) == 0:
						self.caller.msg("|/|mRewards Clerk|n says: I have a hard time choosing sometimes too. It's okay.")
						yield 1
						continue
					elif int(ansqty) * int(getattr(items, listanswer).tokens) > self.caller.db.tokens:
						self.caller.msg("|/|mRewards Clerk|n says: Looks like you're a little short on tokens, you should go win some more!")
						yield 1
						continue
					else:
						totalprice = int(ansqty) * int(getattr(items, listanswer).tokens)
						self.caller.db.tokens -= totalprice
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
						self.caller.msg("|/You receive %d %s and pay %d tokens." % (int(ansqty), getattr(items, listanswer).name, totalprice))
						yield 1
						continue



class RewardsClerkCmdSet(CmdSet):
	key = "RewardsClerkCmdSet"
	def at_cmdset_creation(self):
		self.add(chatrewardsclerk())

class rewardsclerk(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The Rewards Clerk fusses over a pile of sage elixir bottles that won't just quite stay how she wants."
		self.db.weaponsforsale = ['diamondhands', 'sunspear', 'snakewhip']
		self.db.armorforsale = ['ominousarmor', 'scalemail', 'peacockpeacoat']
		self.db.itemsforsale = ['chromacrystal', 'fixerflask', 'sageelixir']
		self.tags.add("specialnpc")
		self.cmdset.add_default(RewardsClerkCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:inlist(accolades, Fortunate One)")