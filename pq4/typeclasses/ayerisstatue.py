from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random

class praycmd(default_cmds.MuxCommand):
	key = "pray"
	auto_help = False
	def func(self):
	#Already Completed
		if "Sky High Wisdom" in self.caller.db.accolades:
			self.caller.msg("|/|mAyeris|n says: The flower of your mind drinks in the light of knowledge. You have proven yourself both knowledgeable and wise you may pass through my domain and enter the cold waste of Varken.")
			return
		colors = ["green", "red", "purple", "yellow", "blue", "orange"]
		#("green", "red"), ("blue", "orange"), ("yellow", "purple")
		offerings = []
	#Initial
		if not self.caller.tags.get(category="ayerisoffering"):
			color = random.choice(colors)
			self.caller.tags.add(color, category="ayerisoffering")
			self.caller.msg("You kneel down, staring up at the statue, and open your mind.")
			if "Hellion" in self.caller.db.accolades:
				self.caller.msg("|mAyeris|n says: YOU!!! You harm my dear sweet Honkiamat, set loose the Hellions, and allow Malashai to walk in this plane of existence again and you DARE ENTER MY TEMPLE?")
				self.caller.msg("|m%s|n says: Who knew a goose could be a force of good? Those things are horrible evil critters!!!! And that one had FIVE heads, that's so much hissing, honking, and biting!" % (self.caller.key))
				if "Malashai" in self.caller.db.monsterstats.keys():
					self.caller.msg("|m%s|n says: As far as Malashai, I've destroyed them and I will live with the deaths of the citizens of Carver City weighing on me forever." % (self.caller.key))
			self.caller.msg("Your vision is suddenly flooded with %s light." % (color))
			self.caller.msg("|mAyeris|n says: Like a flower to the light of day, the mind must open itself to knowledge. One compliments the other. Bring me an eternal offering to prove your wisdom and knowledge.")
			return
	#Puzzle
		else:
			self.caller.msg("|/Your vision is suddenly flooded with %s light." % (self.caller.tags.get(category="ayerisoffering")))
			self.caller.msg("|mAyeris|n says: Like a flower to the light of day, the mind must open itself to knowledge. One compliments the other.")
			for i in self.caller.contents:
				if i.typeclass_path == "typeclasses.objects.glassflower":
					offerings.append(i.key)
			if not offerings:
				self.caller.msg("|mAyeris|n says: You have brought nothing to offer. Return with an eternal offering.")
				return
			self.caller.msg("|mAyeris|n says: What do you wish to offer?")
			answer = yield(', '.join(offerings))
			if answer.title() in offerings:
				if self.caller.tags.get(category="ayerisoffering") == "green":
					correctanswer = "Red Flower"
				elif self.caller.tags.get(category="ayerisoffering") == "red":
					correctanswer = "Green Flower"
				elif self.caller.tags.get(category="ayerisoffering") == "purple":
					correctanswer = "Yellow Flower"
				elif self.caller.tags.get(category="ayerisoffering") == "yellow":
					correctanswer = "Purple Flower"
				elif self.caller.tags.get(category="ayerisoffering") == "blue":
					correctanswer = "Orange Flower"
				elif self.caller.tags.get(category="ayerisoffering") == "orange":
					correctanswer = "Blue Flower"
				if answer.title() == correctanswer:
					for i in self.caller.contents:
						if i.key == answer.title():
							i.delete()
					self.caller.msg("You hold aloft the %s, it begins to glow." % (answer.title()))
					self.caller.msg("|mAyeris|n says: The flower of your mind drinks in the light of knowledge. You have proven yourself both knowledgeable and wise you may pass through my domain and enter the cold waste of Varken.")
					self.caller.tags.add("varkenpass")
					self.caller.db.accolades.append("Sky High Wisdom")
					self.caller.tags.remove(category="ayerisoffering")
				else:
					for i in self.caller.contents:
						if i.key == answer.title():
							i.delete()
					self.caller.msg("You hold aloft the %s, it explodes in a shower of fragments." % (answer.title()))
					self.caller.msg("|mAyeris|n says: The flower of your mind remains closed to the light of knowledge.")
					return
			else:
				self.caller.msg("|/|mAyeris|n says: It is wise to try all options, even if they do not seem to be possible. However, that crap ain't gonna fly here.")
				return

class AyerisStatueCmdSet(CmdSet):
	key = "AyerisStatueCmdSet"
	def at_cmdset_creation(self):
		self.add(praycmd())

class ayerisstatue(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The statue of Ayeris stands tall and proud at the center of the cathedral made of crystal and color. It is a grand masterpiece of art and craftsmanship, standing over thirty feet tall. The goddess is depicted as a majestic figure with flowing hair and outstretched arms holding book with quill and crystal, as if welcoming all who come to the cathedral in search of knowledge. She wears a gown made of pure crystal that shimmers and glows with a soft light, reflecting the surrounding colors, amplifying their hue and intensity. Her face is serene and wise, with eyes that swirl like the stars of a galaxy and seem to hold all the knowledge of the universe. The statue is positioned on a pedestal made of the same crystal material as her gown, creating an ethereal effect as light passes through and illuminates the area around her."
		self.cmdset.add_default(AyerisStatueCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|rThe statue is far too large.|n"