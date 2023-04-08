from evennia import default_cmds, CmdSet, search_object, search_tag
from typeclasses.objects import DefaultObject
import typeclasses.items as items
from evennia.prototypes.spawner import spawn

class chatpeddler(default_cmds.MuxCommand):
	key = "talk peddler"
	aliases = ["Talk Peddler", "Talk peddler", "talk Peddler" ]
	auto_help = True
	def func(self):
		if not self.obj.access(self.caller, "view"):
			self.caller.msg("There's no peddler to talk to.")
			return
		def leave():
			self.caller.msg("|/|mPeddler|n says: Remember, things and stuff, best prices around!")
			return
		itemsavailable = []
		answer = yield("|/|mPeddler|n says: I've got things... and stuff. What do you want?|/|gB|nuy, |gS|nell, |gE|nxit")
	#Exit
		if answer.lower() in ["e", "exit"]:
			leave()
			return
	#Buy
		elif answer.lower() in ["b", "buy"]:
		#Build inventory lists
			target = self.caller.search("peddler")
			if not target:
				self.caller.msg("|/The merchant unexpectedly runs away")
				return
			itemsavailable = target.db.itemsforsale.copy()
		#Purchase Loop
			while 1 < 10:
				#check if no items
				if itemsavailable == []:
					self.caller.msg("|/|mPeddler|n says: This should never happen. Contact Blackhal0.")
					leave()
					break
				else:
					self.caller.msg("   |/|005.|015:|025*|035~|nItems for Sale|035~|025*|015:|005.|n")
					for i in itemsavailable:
						name = getattr(items, i).name
						price = int(getattr(items, i).price)
						desc = getattr(items, i).desc
						self.caller.msg("%s - %d gold. %s|/" % (name, price, desc))
				#actual buying
				answer = yield("|/|mPeddler|n says: Hurry up, I don't have all day. What do you want?|/You have %d gold.|/|gE|nxit to quit." % (self.caller.db.gold))
				if answer.lower() in ["e", "exit", "q", "quit"]:
					leave()
					break
				listanswer = answer.replace(" ", "").lower()
				if not listanswer in itemsavailable:
					self.caller.msg("|/|mPeddler|n says: I got things, I got stuff, but I don't got %s." % (answer))
					yield 1
					continue
				elif not self.caller.db.gold >= int(getattr(items, listanswer).price):
					self.caller.msg("|/|mPeddler|n says: *Hummpff* You don't have enough money for that. Damned filthy poor peasants.")
					yield 1
					continue
				else:
					ansqty = yield("|/|mPeddler|n says: The %s? Great choice, that's one of my favorite things.|/How many do you want?" % (getattr(items, listanswer).name))
					if not ansqty.isnumeric():
						self.caller.msg("|/|mPeddler|n says: I don't know where you're from stranger, but we express quantity using numbers.")
						yield 1
						continue
					elif int(ansqty) < 0:
						self.caller.msg("|/|mPeddler|n says: I would suggest not trying such tricks around here.")
						yield 1
						continue
					elif int(ansqty) == 0:
						self.caller.msg("|/|mPeddler|n says: Changed your mind eh? No problem.")
						yield 1
						continue
					elif int(ansqty) * int(getattr(items, listanswer).price) > self.caller.db.gold:
						self.caller.msg("|/|mPeddler|n says: You can't afford quite that many, perhaps a few less?")
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
	#Sell
		elif answer.lower() in ["s", "sell"]:
			sell = []
		#Create list of players items
			for o in self.caller.contents:
				if o.tags.get("item") or o.tags.get("sellableitem"):
					sell.append(o.key)
			self.caller.msg("|/|mPeddler|n says: Humm, you got some stuff too? What about things? Got any things...")
			if sell == []:
				self.caller.msg("|mPeddler|n says: YOU'VE GOT NO STUFF, NOT EVEN ANY THINGS!!!")
				leave()
				return
			else:
			#Sell Loop
				while 1 < 10:
					self.caller.msg("|mPeddler|n says: Good stuff here, nice things. Here's what I'll pay.")
					self.caller.msg("   |/|005.|015:|025*|035~|nSell Items?|035~|025*|015:|005.|n")
					for o in sell:
						target = self.caller.search(o, candidates=self.caller.contents)
						self.caller.msg("%s - qty: %d. %d gold each." % (o, target.db.qty, int(target.db.price * .75)))
					answer = yield("|/|mPeddler|n says: So how about it? What do you want to sell?|/You have %d gold.|/|gE|nxit to sell nothing." % (self.caller.db.gold))
					if answer.lower() in ("e", "exit"):
						leave()
						break
					elif not answer.lower() in (i.lower() for i in sell):
						self.caller.msg("|/|mPeddler|n says: Nice try, you don't have a %s to sell." % (answer))
						yield 1
						continue
					elif answer.lower() in (i.lower() for i in sell):
						target = self.caller.search(answer.lower(), candidates=self.caller.contents)
						saleprice = int(target.db.price * .75)
						salename = target.db.name
						ansqty = yield("|/|mPeddler|n says: You've got %d %s. How many do you want to sell?" % (target.db.qty, salename))
						if not ansqty.isnumeric():
							self.caller.msg("|/|mPeddler|n says: I don't know where you're from stranger, but we express quantity using numbers.")
							yield 1
							continue
						elif int(ansqty) < 0:
							self.caller.msg("|/|mPeddler|n says: You trying to pull a fast one on me, you don't have that many to sell?|/*HIYYAAAA* The Peddler smacks you and takes some of your gold for trying to trick them.")
							if int(self.caller.db.gold) < 10:
								self.caller.db.gold -= 1
							else:
								self.caller.db.gold -= int(self.caller.db.gold * .10)
							yield 1
							continue
						elif int(ansqty) == 0:
							self.caller.msg("|/|mPeddler|n says: Changed your mind eh? No problem.")
							yield 1
							continue
						elif int(ansqty) > target.db.qty:
							self.caller.msg("|/|mPeddler|n says: You trying to pull a fast one on me, you don't have that many to sell?|/*HIYYAAAA* The Peddler smacks you and takes some of your gold for trying to trick them.")
							if int(self.caller.db.gold) < 10:
								self.caller.db.gold -= 1
							else:
								self.caller.db.gold -= int(self.caller.db.gold * .10)
							yield 1
							continue
						elif int(ansqty) <= target.db.qty:
							totalprice = int(saleprice) * int(ansqty)
							target.db.qty -= int(ansqty)
							if target.db.qty == 0:
								target.delete()
								sell.remove(target.key)
							self.caller.db.gold += int(totalprice)
							self.caller.msg("|/|mPeddler|n says: Ohh yeah, this is nice stuff.|/You get %d gold, the Peddler takes %d %s.|/|/" % (totalprice, int(ansqty), salename))
						yield 1
						if sell == []:
							self.caller.msg("|/|mPeddler|n says: Look here, you've got no more things... No stuff... Go away.")
							leave()
							break
						continue
					else:
						self.caller.msg("Something went wrong selling an item. Tell Blakhal0")
						break
	#Catchall
		else:
			self.caller.msg("|/|mPeddler|n says: Hummm, let me check to see if I have a translator tablet for babbling idiot.... dang, nope.")
			return

class PeddlerCmdSet(CmdSet):
	key = "PeddlerCmdSet"
	def at_cmdset_creation(self):
		self.add(chatpeddler())

class peddler(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The Peddler stands on a colorfully woven rug, extolling the values of their wares.|/|mPeddler|n says: Come, come, the best value for your gold guaranteed!!!"
		self.db.itemsforsale = [""]
		self.tags.add("specialnpc")
		self.tags.add("peddler")
		self.cmdset.add_default(PeddlerCmdSet, permanent=True)
		self.locks.add("get:false()")