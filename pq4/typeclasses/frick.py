from evennia import default_cmds, CmdSet, search_object, search_tag
from typeclasses.objects import DefaultObject
import typeclasses.items as items
from evennia.prototypes.spawner import spawn


class chatfrick(default_cmds.MuxCommand):
	key = "talk frick"
	aliases = ["Talk Frick", "Talk frick", "talk Frick" ]
	auto_help = True
	def func(self):
		glassoptions = ["green", "red", "blue", "yellow", "orange", "purple"]
		def leave():
			self.caller.msg("|/|mFrick|n says: Well, alright. Nice seeing you, stop back and keep your eyes open for those ingredients!")
			return
		stuff = []
		glasscoloritems = ["Chroma Crystal", "Marcasite Sugar"]
		glassoptions = ["green", "red", "blue", "yellow", "orange", "purple"]
	#Converstaion
		#Check for needed items
		for i in self.caller.contents:
			stuff.append(i.key)
		if all(i in stuff for i in glasscoloritems):
			#do a thing about asking what color
			self.caller.msg("|/|mFrick|n says: Well look at that! The adventurer returns with the spoils of victory!")
			answer = yield("|mFrick|n says: Well, how about it? You want to trade in those ingredients for some colored glass?|/|gY|nes, |gN|no.")
			#Make some glass
			if answer.lower() in ["y", "yes"]:
				glasscolor = yield("|/|mFrick|n says: You bet! What color glass would you like? Green, Red, Blue, Yellow, Orange, or Purple?")
				if not glasscolor.lower() in glassoptions:
					self.caller.msg("|/|mFrick|n says: Hummmm, never heard of the color %s. Come back again if you want one of the colors that we can make." % (glasscolor.title()))
					return
				else:
					#remove the needed items
					cctarget = self.caller.search('Chroma Crystal', candidates=self.caller.contents, quiet=True)
					if cctarget:
						cctarget[0].db.qty -= 1
						if cctarget[0].db.qty <= 0:
							cctarget[0].delete()
					mstarget = self.caller.search('Marcasite Sugar', candidates=self.caller.contents, quiet=True)
					if mstarget:
						mstarget[0].db.qty -= 1
						if mstarget[0].db.qty <= 0:
							mstarget[0].delete()
					glasstype = glasscolor.title() + " Glass"
					glasstarget = self.caller.search(glasstype, candidates=self.caller.contents, quiet=True)
					if not glasstarget:
						glass_proto = {
							"key": glasstype,
							"name": "%s" % (glasstype),
							"typeclass": "typeclasses.items.%s" % (glasscolor.lower() + "glass"),
							"qty": 1,
							"location": self.caller
							}
						spawn(glass_proto)
					else:
						glasstarget[0].db.qty += 1
					self.caller.msg("|/|mFrick|n says: OKAY FOLKS! LET'S GOOOOOOOOO!!!!!")
					self.caller.msg("At the shouted order people jump into action.|/A fresh basket of peppers is brought in and chomped down. The furnaces erupt to life as fire blasts from the workers mouth.|/Frick places the Chroma Crystal into a complicated device with many angular adjustments and pulls a rope to lower a tent, letting in only a single pinpoint of light.|/Several quickly scribbled calculations and mutterings later the crystal flashes to %s.|/Frick performs the delicate process and throws the ingredients into the molten material, soon the molten material is being poured out and cooling into beautiful glass." % (glasscolor.title()))
					return
			#Exit conversation
			else:
				self.caller.msg("|/|mFrick|n says: Well, if you change your mind stop on back!")
				return
		else:
			self.caller.msg("|/|mFrick|n says: Hey there, this is a dangerous place to be without eye protection you know!|/Frick guides you out of the building.")
			self.caller.msg("|mFrick|n says: There we go, now what can I help you with? You must be interested in how we make the glass right?")
			self.caller.msg("|mFrick|n says: Well now, I can't just go telling any ol person about our secret processes now, don't want the competition getting a leg up on us or anyone else opening up shop.")
			self.caller.msg("|m%s|n says: Was that worker breathing FIRE?!?!?!" % (self.caller.key))
			self.caller.msg("|mFrick|n says: HAHAHA, yeah no harm in talking about that. Everyone knows the only way to get the furnaces going is with some good spicy peppers, really clears up the sinuses too! Bit rough on the plumbing though, if you know what I mean.")
			self.caller.msg("|m%s|n says: What about the colors? How can you make the glass so colorful?" % (self.caller.key))
			self.caller.msg("|mFrick|n says: That there's a trade secret! Did one of the other glassmakers send you here to spy on us? I'll beat the hide right off ya if that's the case!")
			self.caller.msg("|m%s|n says: No, no, never. I'm just a curious traveler, adventurer if you will." % (self.caller.key))
			self.caller.msg("|mFrick|n says: Adventurer you say? Humm, well maybe you can help me out a bit. See we're running low on the ingredients that we use for the glass pigments.")
			self.caller.msg("|mFrick|n says: Last few folks that went out collecting never came back, think they may have run into some pirates, or maybe the beasties got em, we'll likely never know.")
			self.caller.msg("|mFrick|n says: If we don't keep production up the merchants are going to start buying from our competition, can't be having that.")
			self.caller.msg("|mFrick|n says: Tell you what, we'll do a trade, you find me some pigment ingredients and I'll trade you for some finished glass. What's that? What kind of ingredients?")
			self.caller.msg("|mFrick|n says: Here's what you're looking for:")
			self.caller.msg("Chroma Crystals - Very dangerous to get. Firewolf's get them stuck in their fur in the Kharro desert. Chroma Crystals are crucial. They change color depending on the angle of the sunlight that passes through them and they stay that color until you expose them to light again.")
			self.caller.msg("Marcasite Sugar - It's not sugar, don't eat it. It's a special kind of crystalline gemstone sand that glows in moonlight. It binds the color from the Chroma Crystal to the molten sand. Took us a long time to figure that out. Fradycats like to, umm how to say this, micturate on it. Ends up collecting on their paws.")
			self.caller.msg("|mFrick|n says: Well, that's it. One each will do for one run of glass. It's a lot of work to get, but glass is hard work, and expensive. Good luck!")
			return

class FrickCmdSet(CmdSet):
	key = "FrickCmdSet"
	def at_cmdset_creation(self):
		self.add(chatfrick())

class frick(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A tall lanky manager, covered in black soot from head to toe, shouts orders to the workers."
		self.cmdset.add_default(FrickCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")