from evennia import default_cmds, CmdSet, search_object, search_tag
from typeclasses.objects import DefaultObject

class chattm(default_cmds.MuxCommand):
	key = "talk merchant"
	aliases = ["Talk Merchant", "Talk merchant", "talk Merchant"]
	auto_help = True
	def func(self):
		merchant = search_tag("tirgusmerchant").filter(db_location=self.caller.location)
		target = merchant[0]
		self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.welcome))
		while 1 > 0:
			transactiontype = yield("|/|m%s|n says: Are you looking to |cB|nuy or |cS|nell or |cQ|nuit?" % (target.key))
			  #BUY
			if transactiontype.lower() in ["b", "buy"]:
				self.caller.msg("|/")
				for i in target.db.forsale.keys():
					self.caller.msg(target.db.forsale[i]['name'].title() + ": " + str(target.db.forsale[i]['price']) + " pepper coins.")
			  #Get player answer
				answer = yield("|/|m%s|n says: %s|/What would you like to buy? You have %s pepper coins.|/|cQ|nuit to leave." % (target.key, target.db.salespitch, str(self.caller.db.tirgusmarket['foolsgold'])))
			  #Quit
				if answer.lower() in ["e", "exit", "q", "quit"]:
					self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.bye))
					continue
			  #Check if the merchant sells this.
				elif not answer.lower() in target.db.forsale.keys():
					self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.crazy))
					continue
			  #Get Quantity
				quantity = yield("|/|m%s|n says: How many do you want?" % (target.key))
				if not quantity.isnumeric():
					self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.crazy))
					continue
			  #Check if player has enough fake money
				if not self.caller.db.tirgusmarket['foolsgold'] >= int(target.db.forsale[answer.lower()]['price'] * int(quantity)):
					self.caller.msg("|/|m%s|n says: You don't have enough money for this purchase. Perhaps go make some trades?" % (target.key))
					continue
			  #Deduct Payment
				self.caller.db.tirgusmarket['foolsgold'] -= int(target.db.forsale[answer.lower()]['price'] * int(quantity))
				self.caller.msg("|/|m%s|n says: %s|/%s takes %d pepper coins and hands you %s %s." % (target.key, target.db.thanks, target.key, int(target.db.forsale[answer.lower()]['price'] * int(quantity)), str(quantity), answer.lower()))
				if answer.lower() in self.caller.db.tirgusmarket.keys():
					self.caller.db.tirgusmarket[answer.lower()]['quantity'] += int(quantity)
				else:
					self.caller.db.tirgusmarket[answer.lower()] = {"name": answer.lower(), "quantity": int(quantity)}
				continue
			  #SELL
			elif transactiontype.lower() in ["s", "sell"]:
				shoppinglist = []
			  #Build list of for sale items 
				for i in target.db.buy.keys():
					if i in self.caller.db.tirgusmarket.keys():
						shoppinglist.append(target.db.buy[i]['name'].title() + ": " + str(target.db.buy[i]['price']) + " pepper coins.|/")
			  #Check if player has nothing merchant is interested in
				if shoppinglist == []:
					self.caller.msg("|/%s rummages through your fanny pack.|/|m%s|n says: You don't have anything I'm interested in buying." % (target.key, target.key))
					self.caller.msg("|m%s|n says: But for future reference, here's the kinds of things I'm looking to buy and the prices I'll pay." % (target.key))
					for i in target.db.buy.keys():
						self.caller.msg(target.db.buy[i]['name'].title() + ": " + str(target.db.buy[i]['price']) + " pepper coins.")
					continue
			  #Start transaction
				else:
					self.caller.msg("|/|m%s|n says: This is what you've got that I'm interested in." % (target.key))
					self.caller.msg("|/")
					for i in shoppinglist:
						self.caller.msg(i)
					answer = yield("|/|m%s|n says: What would you like to sell?" % (target.key))
					if answer.lower() in self.caller.db.tirgusmarket.keys() and answer.lower() in target.db.buy.keys():
						quantity = yield("|/|m%s|n says: How many you looking to get rid of?|/You have %s %s" % (target.key, str(self.caller.db.tirgusmarket[answer.lower()]['quantity']), answer.lower()))
						if not quantity.isnumeric():
							self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.crazy))
							continue
						if int(quantity) > int(self.caller.db.tirgusmarket[answer.lower()]['quantity']):
							self.caller.msg("|/You only have %s %s to sell." % (str(self.caller.db.tirgusmarket[answer.lower()]['quantity']), answer.lower()))
							continue
						else:
							self.caller.db.tirgusmarket['foolsgold'] += int(target.db.buy[answer.lower()]['price'] * int(quantity))
							self.caller.db.tirgusmarket[answer.lower()]['quantity'] -= int(quantity)
							if int(self.caller.db.tirgusmarket[answer.lower()]['quantity']) <= 0:
								del self.caller.db.tirgusmarket[answer.lower()]
							self.caller.msg("|/%s takes the %d %s and hands you %d pepper coins." % (target.key, int(quantity), answer.title(), (target.db.buy[answer.lower()]['price'] * int(quantity))))
							continue
					else:
						self.caller.msg("|/|m%s|n says: Either you don't have it, or I'm not buying it. Either way, this deal isn't going to work." % (target.key))
						continue
			  #QUIT
			elif transactiontype.lower() in ["q", "quit"]:
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.bye))
				break
			#CATCHALL
			else:
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.crazy))
				continue


class TirgusMerchantCmdSet(CmdSet):
	key = "TirgusMerchantCmdSet"
	def at_cmdset_creation(self):
		self.add(chattm())

class tirgusmerchant(DefaultObject):
	def at_object_creation(self):
		self.db.forsale = {'unwritten history': {'name': 'unwritten history', 'price': 83}, 'grimoire necromata': {'name': 'grimoire necromata', 'price': 96}}
		self.db.buy = {'dusty tome': {'name': 'dusty tome', 'price': 50}, 'fire scroll': {'name': 'fire scroll', 'price': 63}}
		self.db.desc = "An eccentric collector with stacks of tomes and a deep fascination for knowledge."
		self.db.salespitch = "Welcome to my treasure trove of forgotten lore. Discover the wisdom within."
		self.db.welcome = "Greetings, seeker of knowledge. Step into the realms of history's whispers."
		self.db.thanks = "May the knowledge held within these pages illuminate your mind."
		self.db.crazy = "Apologies, but that particular tome is in the possession of another collector."
		self.db.bye = "Farewell, fellow custodian of ancient wisdom. May your library grow vast."


		self.cmdset.add_default(TirgusMerchantCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.tags.add("tirgusmerchant")