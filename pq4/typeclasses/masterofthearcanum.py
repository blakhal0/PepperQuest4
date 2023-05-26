from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class talkmota(default_cmds.MuxCommand):
	key = "talk master"
	aliases = ["Talk Master", "Talk master", "talk Master", "talk master of the arcanum", "Talk Master of the Arcanum", "TALK MASTER OF THE ARCANUM"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("seekerofknowledge"):
			self.caller.msg("|/|mMaster of the Arcanum|n says: What the hell did you think you were doing putting your face where my hand was??!?!?!?!?! That was a one time spell! Well, I guess it's up to you to recover the great magics of the world. *huff* There's no way you're going to live through this. You need to find the four mother goddesses; Smilsu, Meza, Tirgus, and Pirts. Yadda yadda yadda, you're an adventurer, you'll figure it out. I need a drink.")
			self.caller.msg("The Master of the Arcanum walks over to his private stock and pours a large glass of some sort of enchanted brew.")
			self.caller.msg("It looks like you're on your own to figure the rest out.|/Good luck.")
			return
		for o in self.caller.contents:
			if o.key == "Cryptex Ultima":
				o.delete()
				self.caller.msg("|/|mMaster of the Arcanum|n says: AH! Wonderful, simply wonderful, I won't have to send over any more snacks to the damned library vampires.")
				self.caller.msg("|m%s|n says: Yeah... about that. You sonofa..." % (self.caller.key))
				self.caller.msg("|mMaster of the Arcanum|n says: Eh? I'm sure I told you about them. No matter, you seem hale and hearty.")
				self.caller.msg("The Master of the Arcanum gives you a slap on the back while levitating the book out of your grasp and onto the desk, robes swishing as they walk past you.")
				self.caller.msg("|mMaster of the Arcanum|n says: A book of light, a book of darkness. To see in the darkness, you need a light! Or a spell of vision, or night vision, you know what? Let's just ignore all that and leave it at you need light! I don't want to spend the energy to wipe your mind.")
				self.caller.msg("The Master flips open both books, the light from the Cryptex Ultima bending and being drawn out into an arc falling into the Black Book. Black particulate floating along the beam of light squirming and wriggling forming glowing dark glyphs in on the beam of light.")
				self.caller.msg("|mMaster of the Arcanum|n says: Tell me, what do you know of the Mahte? The Mother Goddesses of all things?")
				self.caller.msg("|m%s|n says: Ummmm...." % (self.caller.key))
				self.caller.msg("|mMaster of the Arcanum|n says: Yes, yes I thought so, it's a somewhat esoteric subject. Few do know about it, I would have been surprised if you had.")
				self.caller.msg("The Master consults the writing on the beam of light, squinting, mumbling, occasionally expressing a surprised sound.")
				self.caller.msg("|mMaster of the Arcanum|n says: There are a great many Mahte, a mother for all things. Long ago the great spells of mastery of the elements were created by great sorcerers. Fearing the power the spells held they where bound to physical form and given to the Mahte for protection. The sorcerers then destroyed all of their workings and sacrificed themselves so that they could never re-create the spells. Only one that is anointed may enter the realms of the mother goddesses.")
				self.caller.msg("The Master begins summoning jars and bottles from the shelves, mixing and measuring while chanting. The Master turns and raises a finger covered in the concoction.")
				self.caller.msg("|mMaster of the Arcanum|n says: BEHOLD FOR I SHALL BE THE ANNOINTED TO RETURN THE UTIMATE MAGICS TO THE WOOOorr *AHHH*.")
				self.caller.msg("The Master trips over his robes, lurches forward losing his balance, eyes wide as his arms flail seeking purchase on anything solid and ends up slapping you in the face smearing the concoction across your cheeks.")
				self.caller.msg("A blinding white light fills your vision.")
				self.caller.msg("|mA Distant Voice|n says: Your mothers await child of knowledge and destiny, return to us.")
				self.caller.msg("You come to laying on the floor with a very upset looking Master of the Arcanum standing over you.")
				self.caller.tags.add("seekerofknowledge")
				return
		self.caller.msg("|/|mMaster of the Arcanum|n says: Eh? What? Why am I blue? It was a minor miscalculation, nothing to be concerned with, could happen to anyone.")
		self.caller.msg("The Master of the Arcanum walks over to you, giving you a good looking over.")
		self.caller.msg("|mMaster of the Arcanum|n says: Well, you appear to be sober, that's better than most of the students here.")
		self.caller.msg("|m%s|n says: I'm not here to join the college, I'm an adventurer. I don't have time to attend a full class load." % (self.caller.key))
		self.caller.msg("|mMaster of the Arcanum|n says: Erm, well then. An adventurer you say. Well adventurer, what say you to an adventure? I've sent a good number of apprentice students over to the library to retrieve a book for me, the Cryptex Ultima. I believe this book is the key to unlocking the secrets to obtain the ultimate magic.")
		self.caller.msg("|m%s|n says: Uhh, well don't reall...." % (self.caller.key))
		self.caller.msg("|mMaster of the Arcanum|n says: Excellent, good to hear it. Head over to the library and track that down for me. I've got some very important wizard things to attend to, yes... quite.")
		self.caller.msg("The Master waves a dismissive hand and goes back to a book.")
		return


class MotACmdSet(CmdSet):
	key = "MotACmdSet"
	def at_cmdset_creation(self):
		self.add(talkmota())

class masterofthearcanum(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Flowing white hair, piercing green eyes, and an off blue tint skin. The Master of the Arcanum exudes an air of knowledge and power. Their regal robes, adorned with intricate patterns and symbols of magical significance, billow behind them as they walk, and the staff they carry seems to glow with an otherworldly light."
		self.tags.add("specialnpc")
		self.cmdset.add_default(MotACmdSet, permanent=True)
		self.locks.add("get:false()")