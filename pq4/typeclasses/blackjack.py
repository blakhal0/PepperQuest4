from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random

class Card:
	def __init__(self, suit, value, card_value):
		# Suit of the Card like Spades and Clubs
		self.suit = suit
		# Representing Value of the Card like A for Ace, K for King
		self.value = value
		# Score Value for the Card like 10 for King
		self.card_value = card_value

class playblackjack(default_cmds.MuxCommand):
	key = "Black Jack"
	aliases = ["black jack", "blackjack", "Blackjack" ]
	auto_help = True
	def func(self):
	#find tablemax
		tablemax = self.caller.search("Black Jack Table", quiet=True)
		tablemax = tablemax[0].db.tablemax
	#Create a deck of cards
		suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
		suits_values = {"Spades":"♠", "Hearts":"|r♥|n", "Clubs": "♣", "Diamonds": "|r♦|n"}
		cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
		cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
		deck = []
		if int(tablemax) == 0:
			maxbet = "no table limit"
		else:
			maxbet = "a table max bet of %d tokens" % (tablemax)
		self.caller.msg("|/|mDealer|n says: Welcome to the BlackJack Table. This table has %s." % (maxbet))
#Gaming loop.
		while 1 > 0:
			for suit in suits:
				for card in cards:
					deck.append(Card(suits_values[suit], card, cards_values[card]))
		#Get wager
			wager = yield("|/|mDealer|n says: How much would you like to wager?|/You have %d tokens.|/|cQ|nuit to leave table." % (self.caller.db.tokens))
			if wager.lower() in ["q", "quit"]:
				self.caller.msg("|/|mDealer|n says: Thanks for playing, stop back again!")
				break
			if not int(tablemax) == 0:
				if int(wager) > int(tablemax):
					self.caller.msg("|/|mDealer|n says: Not good at math eh? There's %s." % (maxbet))
					continue
			if not wager.isnumeric():
				self.caller.msg("|/|mDealer|n says: *Sigh* another wannabe. GOOONS!!!|/The Goons grab you by the collar and toss you out of the chair.")
				break
			if int(wager) > self.caller.db.tokens:
				self.caller.msg("|/|mDealer|n says: Uh-huhh, so you want to wager more than you have? Crafty, but not allowed. Go get some more tokens.")
				break
			if int(wager) <= 0:
				self.caller.msg("|/|mDealer|n says: *Sigh* another wannabe. GOOONS!!!|/The Goons grab you by the collar and toss you out of the chair.")
				break
		#The actual game
			self.caller.msg("The dealer shuffles and deals out the cards.")
			#Cards for both dealer and player
			player_cards = []
			dealer_cards = []
			# Scores for both dealer and player
			player_score = 0
			dealer_score = 0
		#Deal Players Cards
			while len(player_cards) < 2:
				player_card = random.choice(deck)
				player_cards.append(player_card)
				deck.remove(player_card)
		#Deal Dealers Cards
			while len(dealer_cards) < 2:
				dealer_card = random.choice(deck)
				dealer_cards.append(dealer_card)
				deck.remove(dealer_card)
		#Show Player Cards and Dealer up card
			self.caller.msg("|/Your Cards: |[W|X" + player_cards[0].value + player_cards[0].suit + "|n |[W|X" + player_cards[1].value + player_cards[1].suit + "|n")
			self.caller.msg("Dealers Up Card: |[W|X" + dealer_cards[0].value + dealer_cards[0].suit + "|n")
		#Check if player AND dealer have blackjack
			if player_cards[0].card_value + player_cards[1].card_value == 21 and dealer_cards[0].card_value + dealer_cards[1].card_value == 21:
				self.caller.msg("|/Dealers Cards: |[W|X" + dealer_cards[0].value + dealer_cards[0].suit + "|n |[W|X" + dealer_cards[1].value + dealer_cards[1].suit + "|n")
				self.caller.msg("|/Push")
				continue
		#Check if player has blackjack
			if player_cards[0].card_value + player_cards[1].card_value == 21:
				self.caller.msg("|/Winner Winner, Chicken Dinner!|/BLACK JACK!!")
				self.caller.msg("You win %d tokens!" % (int(wager) * 2))
				self.caller.db.tokens += int(wager) * 2
				self.caller.db.winnings += int(wager) * 2
				continue
		#Insurance check
			if dealer_cards[0].card_value == 11:
				insurance = yield("|mDealer|n says: Ace UP! Buy insurance?|/|cY|nes, |cN|no")
				if insurance.lower() in ["y", "yes"]:
					if dealer_cards[1].card_value == 10:
						self.caller.msg("|mDealer|n says: Smart call!/Dealers Cards: |[W|X" + dealer_cards[0].value + dealer_cards[0].suit + "|n |[W|X" + dealer_cards[1].value + dealer_cards[1].suit + "|n")
						continue
					else:
						self.caller.msg("Dealer checks the hole card.|/|mDealer|n says: No body home.|/You lose the %d token insurance bet." % (int(int(wager)/2)))
						self.caller.db.tokens -= int(int(wager)/2)
						self.caller.db.winnings -= int(int(wager)/2)
				else:
					if not dealer_cards[1].card_value == 10:
						self.caller.msg("|/Dealer checks the hole card.|/|mDealer|n says: No body home.")
		#Check if Dealer has 21
			if dealer_cards[0].card_value + dealer_cards[1].card_value == 21:
				self.caller.msg("|/Dealers Cards: |[W|X" + dealer_cards[0].value + dealer_cards[0].suit + "|n |[W|X" + dealer_cards[1].value + dealer_cards[1].suit + "|n")
				self.caller.msg("Dealer Black Jack!|/You Lose.")
				self.caller.db.tokens -= int(wager)
				self.caller.db.winnings -= int(wager)
				continue
		#Player hand
			playerstand = False
			player_score = player_cards[0].card_value + player_cards[1].card_value
			playercarddisplay = "|/Your Cards: |[W|X" + player_cards[0].value + player_cards[0].suit + "|n |[W|X" + player_cards[1].value + player_cards[1].suit + "|n"
			while playerstand == False:
				if player_score > 21:
					playerstand = True
					continue
				if len(player_cards) == 2 and int(wager) <= (self.caller.db.tokens * .5):
					options = "|cH|nit, |cS|ntand, |cD|nouble Down"
					optionslist = ["h", "hit", "s", "stand", "d", "double down"]
				elif len(player_cards) == 2 and int(wager) > (self.caller.db.tokens * .5):
					options = "|cH|nit, |cS|ntand"
					optionslist = ["h", "hit", "s", "stand"]
				else:
					options = "|cH|nit, |cS|ntand"
					optionslist = ["h", "hit", "s", "stand"]
				play = yield("You have %d.|/%s" % (player_score, options))
				if not play.lower() in optionslist:
					self.caller.msg("The Dealer shakes their head.|/|mDealer|n says: What part of %s didn't you understand?" % (options))
					continue
				if play.lower() in ["s", "stand"]:
					playerstand = True
					continue
				if play.lower() in ["h", "hit"]:
					player_card = random.choice(deck)
					player_cards.append(player_card)
					deck.remove(player_card)
					playercarddisplay = playercarddisplay + " |[W|X" + player_card.value + player_card.suit + "|n"
					self.caller.msg(playercarddisplay)
					self.caller.msg("Dealers Up Card: |[W|X" + dealer_cards[0].value + dealer_cards[0].suit + "|n")
					player_score += player_card.card_value
					c = 0
					while player_score > 21 and c < len(player_cards):
						if player_cards[c].card_value == 11:
							player_cards[c].card_value = 1
							player_score -= 10
							c += 1
						else:
							c += 1
					continue
				if play.lower() in ["d", "double down"]:
					wager = int(wager) * 2
					player_card = random.choice(deck)
					player_cards.append(player_card)
					deck.remove(player_card)
					playercarddisplay = playercarddisplay + " |[W|X" + player_card.value + player_card.suit + "|n"
					player_score += player_card.card_value
					self.caller.msg(playercarddisplay)
					self.caller.msg("Dealers Up Card: |[W|X" + dealer_cards[0].value + dealer_cards[0].suit + "|n")
					c = 0
					while player_score > 21 and c < len(player_cards):
						if player_cards[c].card_value == 11:
							player_cards[c].card_value = 1
							player_score -= 10
							c += 1
						else:
							c += 1
					self.caller.msg("You have %d." % (player_score))
					playerstand = True
					continue
		#check if player busted
			if player_score > 21:
				self.caller.msg("|/|mDealer|n says: Oh, too many.|/BUST!")
				self.caller.db.tokens -= int(wager)
				self.caller.db.winnings -= int(wager)
				continue
		#Dealer hand
			dealer_score = dealer_cards[0].card_value + dealer_cards[1].card_value
			dealercarddisplay = "|/Dealer Cards: |[W|X" + dealer_cards[0].value + dealer_cards[0].suit + "|n |[W|X" + dealer_cards[1].value + dealer_cards[1].suit + "|n"
			while dealer_score < 17:
				dealer_card = random.choice(deck)
				dealer_cards.append(dealer_card)
				deck.remove(dealer_card)
				dealercarddisplay = dealercarddisplay + " |[W|X" + dealer_card.value + dealer_card.suit + "|n"
				dealer_score += dealer_card.card_value
				c = 0
				while dealer_score > 21 and c < len(dealer_cards):
					if dealer_cards[c].card_value == 11:
						dealer_cards[c].card_value = 1
						dealer_score -= 10
						c += 1
					else:
						c += 1
				continue
			self.caller.msg(playercarddisplay + dealercarddisplay)
			if dealer_score > 21:
				self.caller.msg("|/|mDealer|n says: Well, lucky you.|/DEALER BUST!!|/You win %d tokens." % (int(wager)))
				self.caller.db.tokens += int(wager)
				self.caller.db.winnings += int(wager)
				continue
			if player_score == dealer_score:
				self.caller.msg("|/|mDealer|n says: Looks like we both win.|/PUSH")
				continue
			if player_score > dealer_score:
				self.caller.msg("|/|mDealer|n says: Congratulations!|/YOU WIN!!!|/You win %d tokens." % (int(wager)))
				self.caller.db.tokens += int(wager)
				self.caller.db.winnings += int(wager)
				continue
			if player_score < dealer_score:
				self.caller.msg("|/|mDealer|n says: Better luck next time!|/DEALER WIN.|/You lose %d tokens." % (int(wager)))
				self.caller.db.tokens -= int(wager)
				self.caller.db.winnings -= int(wager)
				continue

class BlackJackCmdSet(CmdSet):
	key = "BlackJackCmdSet"
	def at_cmdset_creation(self):
		self.add(playblackjack())

class blackjack(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A sharp dressed dealer stands behind the Black Jack Table, a large golden GPC logo emblazoned on the layout.|/|mDealer|n says: Care to try your hand at a hand? Black Jack pays 2 to 1, Insurance option available with dealers up card showing an Ace, the house stands on 17."
		self.db.tablemax = 0
		self.cmdset.add_default(BlackJackCmdSet, permanent=True)
		self.locks.add("get:false()")
