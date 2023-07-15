from evennia import default_cmds, CmdSet, search_object
import typeclasses.locations as locations
from typeclasses.objects import DefaultObject

class chatvanya(default_cmds.MuxCommand):
	key = "talk uncle vanya"
	aliases = ["Talk Uncle Vanya", "Talk uncle vanya", "talk vanya", "Talk Vanya", "Talk Uncle", "talk uncle"]
	auto_help = True
	def func(self):
		if not self.caller.tags.get("vanya"):
			self.caller.msg("|/|mUncle Vanya|n exclaims: AHH! New people, I love new people, new people come, come, have seat. Enjoy the never ending show that is.... UNCLE VANYA'S!!!!|/Uncle Vanya twirls and does a back flip landing with his arm outstretched pointing to an empty chair. He looks up at you as you stand there staring.|/|mUncle Vanya|n says: Oh no, you're a one that cannot see or hear. I apologize.|/Uncle Vanya does a cartwheel, lands next to you, grasps your shoulder in a firm grip and before you can react throws you, gracefully, into a chair at the bar.|/|mUncle Vanya|n shouts loudly: THERE MUCH BETTER YES? WE HAVE A DRINK TO CELEBRATE FRIENDSHIP!|/You wince not only from the volume of the voice, but also from the unmistakable smell of pickled fish on his breath.|/|mUncle Vanya|n says: Oh, you do hear. Again I apologize. So many apologies this day. Here, let us drink. Uncle Vanya's World Famous Capsaivit Balsam.|/Uncle Vanya places two short round glasses, about the height of your hand, on the bar and fills them with a brownish black liquid. It smells like rye bread, fruit, spices, and hot peppers. You each pick up your glasses, tap them together, and swallow.|/|/|/Steam blows out your ears as your stomach, and other internal organs, attempt to flee your body from your mouth.|/|mUncle Vanya|n says: Is very good yes? Will keep you warm and happy in the cold.")
			self.caller.tags.add("vanya")
		if not "Finder of the Song" in self.caller.db.accolades:
	#Player has not completed Varken Area
			self.caller.msg("|/|mUncle Vanya|n says: Welcome welcome to Uncle Vanya's! The greatest never ending show ever!")
			answer = yield("|mUncle Vanya|n says: How does Uncle Vanya help you today?|/Uncle Vanya leans over the bar swirling his mustaches waiting to hear what you want.")
			if answer.lower() in ["boareaus, ancient gusts, heed my plea, unleash your howling tempest, bend the world to its knees.", "boareaus ancient gusts heed my plea unleash your howling tempest bend the world to its knees"]:
				if all(["Discordia", "Seraphin", "M'lanchrus"]) in self.caller.db.monsterstats.keys():
					self.caller.msg("|/|/Uncle Vanya turns and looks at you with a wicked stare through completely blue eyes. His head tips back, smile widening until the mouth splits his face in two and a great deafening freezing wind is exhaled. A swirling form appears before you.")
					self.caller.msg("|mBoareaus|n says: So, you survived and figured out my ruse. Unfortunate for you, I was quite content just feeding on the people of this city. Listening to that gullible idiot Skaahde scream in pain as I torment her followers is just as delicious as their souls. Now your soul will feed the consuming north wind as well.")
					self.caller.msg("You are suddenly suspended in a freezing swirling wind...")
					yield 4
					results = search_object("#10014")
					self.caller.move_to(results[0], quiet=True, move_hooks=False)
					self.caller.tags.add("letsfight")
					self.caller.execute_cmd('fight')
				else:
					self.caller.msg("|/|/Uncle Vanya shivers violently, cracks their neck, then turns to you with a large smile.")
					self.caller.msg("|mUncle Vanya|n says: That's a very old song you know. How odd that you would know it without having met those that guard the words.")
					self.caller.db.hp -= int(self.caller.db.hp * .5)
					self.caller.db.gold -= int(self.caller.db.gold * .5)
					self.caller.msg("You feel a spine shivering chill... you lose half your hp.")
					self.caller.msg("And half your gold.")
			elif "drink" in answer.lower():
				self.caller.msg("|/Uncle Vanya smiles wide, almost seeming to split his face in two.")
				self.caller.msg("|mUncle Vanya|n says: Back for another eh?? HAHAHAHAHA NO ONE CAN STAY AWAY!! Is very good, keep you warm and happy in so much cold and sad.")
				self.caller.msg("Uncle Vanya sets glasses in front of both of you and pours the odd brown black liquid.")
				self.caller.msg("|mUncle Vanya|n says: May your life be full enough to satisfy the great northern wind!")
				self.caller.msg("Uncle Vanya clinks your glass and you both knock back a drink. A few of the sailors give a sideways glance at the toast but then go back to their conversations.")
				self.caller.msg("You feel spicy vomit start to creep up your throat, but choke it down.")
				self.caller.msg("Vanya goes back to entertaining and serving the guests.")
				return
			elif any(word in answer.lower() for word in ["history", "circus", "get here"]):
				self.caller.msg("|/|mUncle Vanya|n says: How I get here? Well, that is QUITE the story. Long ago I am on boat with other performers, the Traveling Wonders. Greatest performers in all world. Then boat hit ice, boat get a hole, boat sink. Everyone die except VANYA!!! Vanya is now the GREATEST PERFORMER!! I grow mustache to show world strength and open the never ending show that is UNCLE VANYA'S!!")
				self.caller.msg("|m%s|n says: You seem so joyous and animated, everyone else here is so... bleh. Why are you not affected." % (self.caller.key))
				self.caller.msg("|mUncle Vanya|n says: Uncle Vanya is old, but not so that much old. Secret is pickled fish, make you look young!!! Only people born or live here when it happen are no more music and sad. I get here after all the no more music. Now only Vanya performs!")
				self.caller.msg("Vanya goes back to entertaining and serving the guests.")
				return
			elif any(word in answer.lower() for word in ["what happened", "demon", "demons", "devils", "minstrels", "discordia", "seraphin", "m'lanchrus", "boareaus"]):
				self.caller.msg("|/|mUncle Vanya|n says: Long time ago performers come to Boars Snout, agents of Boareaus. They play music and steal souls of the people, make everything quiet and sad. Then disappear, never seen again. Many years later Boars Snout is very lucky and Vanya arrive!!")
				self.caller.msg("|mUncle Vanya|n says: Travelers say they see evil totems in Varken while traveling, some say in north fjords, some say in tundra, some say in the waste, near big dark mountains. But all say very easy to miss if not looking for them. Maybe now you know of them you will find them.")
				self.caller.msg("Vanya goes back to entertaining and serving the guests.")
			elif any(word in answer.lower() for word in ["varken"]):
				self.caller.msg("|/|mUncle Vanya|n says: Varken very very big, lots of cold not much else. Very nice hot springs to south west, but dangerous to get to. You look tough, maybe you get there safe. Warm bones in hot water feel happy. Ehhhhh...is also dead person in hut. Vanya would recommend you avoid dead person. Very kind, but creepy. Makes very tasty chocolate drink. Not as tasty as Vanya's own World Famous Capsaivit Balsam! We should have drink!")
				self.caller.msg("Uncle Vanya sets glasses in front of both of you and pours the odd brown black liquid.")
				self.caller.msg("|mUncle Vanya|n says: May your life be full enough to satisfy the great northern wind!")
				self.caller.msg("Uncle Vanya clinks your glass and you both knock back a drink.")
				self.caller.msg("You feel spicy vomit start to creep up your throat, but choke it down.")
				self.caller.msg("Vanya goes back to entertaining and serving the guests.")
				return
			elif any(word in answer.lower() for word in ["mirror"]):
				self.caller.msg("|/|mUncle Vanya|n says: Yes yes, this is how Vanya find land after ship sink! I see shiny light on shore and swim run swim over and through ice. Then Vanya find Boars Snout. Unusual place for big mirror, but Vanya is thankful. Maybe you go see it.")
				self.caller.msg("Vanya goes back to entertaining and serving the guests.")
			else:
				self.caller.msg("|/Uncle Vanya looks at you with a slight confusion in their eyes.")
				self.caller.msg("|mUncle Vanya|n says: You make no sense... YOU NEED DRINK!!! Good drink make you make sense.")
				self.caller.msg("Uncle Vanya sets glasses in front of both of you and pours the odd brown black liquid.")
				self.caller.msg("|mUncle Vanya|n says: May your life be full enough to satisfy the great northern wind!")
				self.caller.msg("Uncle Vanya clinks your glass and you both knock back a drink.")
				self.caller.msg("You feel spicy vomit start to creep up your throat, but choke it down.")
				self.caller.msg("Vanya goes back to entertaining and serving the guests.")
				return
			return
		else:
	#Player has completed Varken Area
			self.caller.msg("|/|mUncle Vanya|n says: Thank you for saving Vanya, for returning the song. Now all are happy and sing again and Uncle Vanya is not the only one who performs... but is still best!")
			self.caller.msg("Vanya leans in close to you.")
			self.caller.msg("|mUncle Vanya|n whispers: Uncle Vanya remembers more now that noisy wind is gone. These pirates that cause so much trouble, the Valaharran's that should not be here on this side of the world, when they get here no ships. So Vanya thinks, he thinks, how are they pirates with no ship? How so many they get across frozen tundra alive and without notice? Then Vanya think of it! If you don't go across the ground, or over the sea, you go UNDER the ground. You see is simple, you are strong like tusk horse Vanya used to train, very strong. You find Valaharran, you beat up Valaharran until you find secret maps. Valaharran here on water in boat. Water very cold, even for tusk horse is too cold. You need Valaharran on land. Tusk horse strong on land. Go find map, come back and captain will take you to secret underground!")
			yield 3
			self.caller.msg("Uncle Vanya leans back and smiles.")
			self.caller.msg("|mUncle Vanya|n says: But, before you go... WE DRINK!!!!")
			self.caller.msg("Uncle Vanya sets glasses in front of both of you and pours the odd brown black liquid.")
			self.caller.msg("|mUncle Vanya|n says: To the great %s! The bards sing your name forever and Skaahde protect you!!" % (self.caller.key))
			self.caller.msg("Uncle Vanya clinks your glass and you both knock back a drink.")
			self.caller.msg("You feel spicy vomit start to creep up your throat, but choke it down.")
			self.caller.msg("Vanya goes back to entertaining and serving the guests.")
			return


class VanyaCmdSet(CmdSet):
	key = "VanyaCmdSet"
	def at_cmdset_creation(self):
		self.add(chatvanya())

class vanya(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The ringmaster of this bizarre tavern is a short and stocky man, exuding an aura of warmth and friendliness. His attire reflects a blend of circus performer fashion and more than a touch of eccentricity. On his head, Uncle Vanya sports a close-fitting red fez with a thick fur lining adorning the edges. The fez itself is embellished with an assortment of shiny trinkets and baubles, creating glints of light at every turn or bounce of his lively step. Speaking of fur linings, a thick black handlebar mustache dominates the area under his nose. His attire continues with billowing pants, featuring vibrant stripes that puff out on each down step. The pants are tailored to allow ease of movement as Uncle Vanya effortlessly navigates the bustling tavern. The contrasting colors and patterns of the stripes contribute to his visually captivating ensemble. Completing his outfit, Uncle Vanya dons a fitted vest, which again serves as a canvas for even more vivid hues and intricate designs. The vest is adorned with sequins, embroidery, and patterns that catch the light and add a touch of sparkle to his appearance. It is a garment that mirrors his vibrant personality and draws the eye of anyone who enters the tavern.|/Vanya's eye light up as he sees you enter."
		self.tags.add("specialnpc")
		self.cmdset.add_default(VanyaCmdSet, permanent=True)
		self.locks.add("get:false()")