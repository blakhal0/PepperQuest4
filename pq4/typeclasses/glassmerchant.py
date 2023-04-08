from evennia import default_cmds, CmdSet, search_object, search_tag
from typeclasses.objects import DefaultObject
import typeclasses.items as items
from evennia.prototypes.spawner import spawn


class chatglassmerchant(default_cmds.MuxCommand):
	key = "talk glazier"
	aliases = ["Talk Glazier", "Talk glazier", "talk Glazier" ]
	auto_help = True
	def func(self):
		glassoptions = ["green", "red", "blue", "yellow", "orange", "purple"]
		def leave():
			self.caller.msg("|/|mGlazier|n says: *sniFFFFF* AAAHHhhhh, yeah-yeah, cool, right, not right now. I can dig that. Like just whenever you want *SNNNNNNIIIIIIFFFFFFF* HELL YEAH!, just stop on back. I'll be here.|/The Glazier wanders off in the shop.|/|mGlazier|n mutters: Huh, maybe I could knock down this wall and make a room to organize my string collection....")
			return
		answer = yield("|/|mGlazier|n says: Hey, hey-hi. Nice to meet you, yeah REAL good to see you, real good yeah. Uhhh-Glad you stopped in, I knew you'd be by sooner or later. *crunch-crunch, shuffle, tap-tap-tap, SNIIFFFFF* HOT DAMN! That glass is FANTASTIC! So what can I do for you?|/|gB|nuy |gE|nxit")
	#Exit
		if answer.lower() in ["e", "exit"]:
			leave()
			return
	#Buy
		elif answer.lower() in ["b", "buy"]:
			if self.caller.db.gold < 700:
				self.caller.msg("|/|mGlazier|n says: Glass is expensive! It's 700 gold EACH. You can't even get...... *thump thump* Ah there we go, heart stopped for a minute there HAHAHAHAHA. Hate it when that happens. Yeah you don't have enough gold for even one piece. Come back later.")
				return
			while 1 < 10:
				coloranswer = yield("|/|mGlazier|n says: Right on, right on, right-right-right. Yeah I've got glass, SO MUCH GLASSS!! *SNIIIIIIIIFFFF* WHOOO!! Yeah I got all the glass, what you want? I've got Green, Red, Blue, Yellow, Orange, and Purple. Today only, each piece is just $700 gold each, per piece, for one piece.|/Which color do you want?")
				#input validation
				if not coloranswer.lower() in glassoptions:
					self.caller.msg("|/|mGlazier|n says: I-I-I'm not sure I've got *snniIIFFFFFF* WOOOHOOO! I don't uhhh, think I've got any %s glass. Maybe stop back later when you've made up your mind to choose an option that's available." % (coloranswer.title()))
					break
			#actual buying
				#take gold
				self.caller.db.gold -= 700
				#Check if they already has this color of glass
				glasstarget = self.caller.search((coloranswer.title() + " Glass"), candidates=self.caller.contents, quiet=True)
				#If player has glass, increase quantity
				if glasstarget:
					glasstarget[0].db.qty += 1
				#spawn glass to player
				else:
					glass_proto = {
					"key": "%s Glass" % (coloranswer.title()),
					"typeclass": "typeclasses.items.%s" % (coloranswer.lower() + "glass"),
					"qty": 1,
					"location": self.caller
					}
					spawn(glass_proto)
				self.caller.msg("|/|mGlazier|n says: YEAH, yeah of course, yeah I've got some of that, PLENTY of that one. Yeah, lets see, it's right over....*SnnnIIIIFFFFFF* AAAAAHHHHHH SPIDERS UNDER MY SKIN!!!!! Oh, oh, just my arm hair, HAHAHAA. Okay yeah, here we go....")
				self.caller.msg("You receive the %s Glass" % (coloranswer.title()))
				self.caller.msg("|/|mGlazier|n says: Thanks for stopping in! Hope you enjoy the glass!!!")
				break
	#Catchall
		else:
			self.caller.msg("|/|mGlazier|n says: I haven't slept for a few... days? Yeah days now. I can't understand what you're asking for. Come back later when you're making some sense.")
			return

class GlassMerchantCmdSet(CmdSet):
	key = "GlassMerchant"
	def at_cmdset_creation(self):
		self.add(chatglassmerchant())

class glassmerchant(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The Glazier is very very twitchy and erratic. They seem to be involved in multiple small projects spread out all over the shop at the same time."
		self.cmdset.add_default(GlassMerchantCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")