from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random

class chatfortuneteller(default_cmds.MuxCommand):
	key = "Talk Fortune Teller"
	aliases = ["talk fortune teller"]
	auto_help = True
	def func(self):
		if not self.obj.access(self.caller, "view"):
			self.caller.msg("There's no fortune teller to talk to.")
			return
		fortunes = ["Beware of the blinding red light. If you see this light, you must flee. It will only bring you death!", "You will find the answer to a long, mysterious riddle in your family bloodline buried between two oak trees, west of the village you grew up in.", "A path of death lies in your wake.", "Greed is a poor man’s compass, and I see gold and riches in your future.", "A single wolf is slaughtered by many enemies that surround it. Let this be a warning sign of danger that is preventable by the pack.", "The truth will come from a child’s toy. The lie will come from a weapon.", "You must drink of the poison well and eat of the spoiled pantry.", "Follow the flight of birds, never in winter, always returning.", "A song contains a wish. Only the name will answer.", "The mother has disguised herself. Her babe is lost and will not return. She will nurse no other.", "The gears turn long after the machine has been broken. He who built it cannot mend it. He who holds it cannot carry it. He who finds it cannot speak it.", "Gaze through the cracked window, and only then will you see clearly.", "Beware the men with gills. Speak not to the sea or the southern wind.", "Beware the snake’s venom, not its bite.", "Travel five days with the silver star at your heels, then cross the raging river. There you will come to realize your true self.", "The light will be in the shadowest darkness.", "Not all the frogs are in the pond, beware of them.", "One for the fire, two for the clouds, and three for the knights.", "Don’t trust the song of the birds.", "Cloak in the water. The man is crying. Let the leaf falls and everything will be fine.", "For one wish to make, it’ll be more wish to crumble.", "In the high plain there’s a dark moon. Don’t follow the light.", "When the dawn will come at the birthday of the mother, rats and snakes will devour all hopes.", "Near the mountains, there is a grey falcon. Look at the eyes, and you’ll die. Look at the tail, and you’ll be rich.", "Don’t move when the night song come, or you’ll gain something you don’t want, and lost something you wanted to keep.", "Today was possibly the most important day of your life! Congrat.. oh… you missed it… tsk tsk tsk… What a shame… A do-over, then! Tomorrow you will wake up and it will be today. Make sure you return or that decree will stay. k, Bye!", "Do not trust your thoughts. They will hinder your victory.", "And through the drifts the snowy cliffs did send a dismal sheen: Nor shapes of men nor beasts we ken the ice was all between.", "If you believe in telekinesis, raise my hand. The fortune teller then proceeds to raise their hand.", "When you are done, the spirit haunting will pass over you.", "A dragon will give you a jewel. Beware the generous miser.", "The path less traveled is paved in gold.", "Find the woman who gives birds their song.", "Beware, young mouse, for the lion is thorned.", "Do not Cross the Mountain!", "10 Stars Mark the Path!", "The Moon Shines Brightest to Those in Her Favor.", "Speak Not The Name Unspoken; They Listen, Always.", "Beware, for the Great Gyre is Nigh; The Slouching Beast Will Soon Arrive!", "Swords Shall Pierce Thine Heart; Pin Thy Love Lest It Be Lost.", "Three Crones Shall Visit Thee and Their Lights Shall Reveal the Truth of What Thou Doth Seek!", "Keep a Candle Burning; Lest The Dark Take Even Your Fears Away.", "Build Not Houses of White Stone.", "Three Coins Must Ye Pay; Three Prices Dear, Secrets Thrice Revealed, ‘ere The Light of Day.", "Spill Forth a Dram for the Lost; Make Merry in the Name of Those Who Pay the Highest Price!", "You Must Seek the Leaf that Grows Not On Any Tree!", "Jump the Broom; Dance above the Blades!", "Sphinx of Black Quartz, Judge Thy Vow.", "Seek the Egg of Stone; Face the Dragon!", "Your nights will grow colder still, to match the heat of growing fires.", "Trust the twin with no siblings, but abhor the lone child.", "The face of the one you seek is thus- a busker at dawn; a composer at noon; a patron at dusk; a maestro under the stars.", "Your money, here, have it back. The fortune you’ve asked me to read, never shall I speak of it in this life or any hereafter.", "A wilting lineage droops to shadowy lows. What the rotten fruit begets chokes out the tree of its birth.", "Beware! Blessings from above may actually be curses from below!", "A helping hand will come from an unlikely place. Trust it at your own peril.", "When the leaves fall from the trees so too shall the stars fall from the sky.", "The wisest men envy the grave.", "The poison of the moon lies only once.", "There be dragons in ye head. Make sure to feed them.", "The treasure you are looking for is in the fruit.", "Never bring upon yourself the wrath of the chicken. You may think this a metaphor, but it is not. Their beaks are sharp like my toes.", "Your hands will taste of orange in the near future.", "That which you hold most dear will turn against you and lead you to ruin", "Your actions have had unintended and unforeseeable consequences, and have placed into action the final piece of that which now approaches you. You are the harbinger of your own death", "The thoughts you have had but not put into action are leading you down a path to your own undoing", "The fall of slow rain upon the barren field will lead you to the house which shelters your destiny", "Steel your heart for darkness ahead. Your betrayal has already happened though you do not yet know it.", "Seek ye the good behind the bad and beware the bad behind the good.", "Never lick a horse in the mouth, they bite.", "A Fall is Coming; Winter Just Round the Bend; Enjoy Spring; Summer Shall Bring An End!", "Let Not Cold Enter Your Heart, For Then Only Love Can Drive It Out!", "The black sky will shield you from your enemies. Travel by night.", "The rope with which you climb may also hang you if you are not careful.", "You will be an old man/woman by the time your quest is complete.", "Fools will take great heed of your words. Use this to your advantage.", "A shrewd and very attractive fortune teller has put a curse on you. I will remove it for an additional sum.", "Trust not the travelers numbering odd.", "Take something old, give something new, doubt something red, trust something blue.", "Left at the stream, at the face look right, crawl through the dark, and you will find the light!", "Salt thy wounds, relish the sting, sweet is the knave, and bold is the king.", "Thrice will call the raven, heed its warn lest the fourth cry your dirge.", "Between silver and gold, choose evil’s bane. Between fire and chill, the lady’s kiss.", "The shadow of the dragon is an omen, but coming of the wolf is the sign.", "Begrudge not the thieving monkey, lest you take its place in the tiger’s jaws.", "Lay not your head in the barn animal's bed, for the headsman soon calls.", "A copper for the maid, a silver to the beggar, and a gold for a lonely tune, may the vault of riches open to you.", "Someone you remember, someone you forget, someone with a favor, another with a threat.", "Poor fortune for ye, unless you confess your guilt to the willow tree.", "Your luck is a shame until you trade with your mate who has one of the same.", "A fortune most cold if you do as you’re told.", "Torch and candle, wax and wick, in the hall of fire, move right quick!", "Look for the priestess, she will bring salvation.", "An ancient empire will rise from the waves along with ancient secrets.", "Only when the lovers are reunited can the curse be broken.", "As the hermit emerges from hiding, darkness shall soon emerge as well.", "Watch for a nobleman in red, for he is a devil in disguise."]
		def neededxpcalculate():
			self.caller.msg("|mFortune Teller|n says: Hmmm, yes, veerrry int-erst-innnnggg. You need %d more experience to achieve the next level. Go forth, and let fate guide you." % ((nlxp - self.caller.db.exp)))
			return
		self.caller.msg("|/|mFortune Teller|n says: Some things are easy to see, others take effort and therefore require a humble offering of 2 gold.")
		self.caller.msg("|mFortune Teller|n says: What do you wish to know? When you shall gain a new level or do you dare cast your gaze into the mists to see a glimpse of your future?")
		answer = yield("|cF|nortune, |cL|nevel, |cE|nxit")
		if answer.lower() in ["e", "exit"]:
			self.caller.msg("|/|mFortune Teller|n says: It is a wise warrior that attempts not to peer into the uncertain mists. Go forth, and let fate guide you.")
			return
		elif answer.lower() in ["l", "level"]:
			if self.caller.db.lvl == 1: 
				nlxp = 7
			if self.caller.db.lvl == 2:
				nlxp = 23
			if self.caller.db.lvl == 3:
				nlxp = 47
			if self.caller.db.lvl == 4:
				nlxp = 110
			if self.caller.db.lvl == 5:
				nlxp = 220
			if self.caller.db.lvl == 6:
				nlxp = 450
			if self.caller.db.lvl == 7:
				nlxp = 800
			if self.caller.db.lvl == 8:
				nlxp = 1300
			if self.caller.db.lvl == 9:
				nlxp = 2000
			if self.caller.db.lvl == 10:
				nlxp = 2900
			if self.caller.db.lvl == 11:
				nlxp = 4000
			if self.caller.db.lvl == 12:
				nlxp = 5500
			if self.caller.db.lvl == 13:
				nlxp = 7500
			if self.caller.db.lvl == 14:
				nlxp = 10000
			if self.caller.db.lvl == 15:
				nlxp = 13000
			if self.caller.db.lvl == 16:
				nlxp = 17000
			if self.caller.db.lvl == 17:
				nlxp = 21000
			if self.caller.db.lvl == 18:
				nlxp = 25000
			if self.caller.db.lvl == 19:
				nlxp = 29000
			if self.caller.db.lvl == 20:
				nlxp = 33000
			if self.caller.db.lvl == 21:
				nlxp = 37000
			if self.caller.db.lvl == 22:
				nlxp = 41000
			if self.caller.db.lvl == 23:
				nlxp = 45000
			if self.caller.db.lvl == 24:
				nlxp = 49000
			if self.caller.db.lvl == 25:
				nlxp = 53000
			if self.caller.db.lvl == 26:
				nlxp = 57000
			if self.caller.db.lvl == 27:
				nlxp = 61000
			if self.caller.db.lvl == 28:
				nlxp = 65000
			if self.caller.db.lvl == 29:
				nlxp = 65535
			if self.caller.db.lvl == 30:
				nlxp = 100000
			neededxpcalculate()
		elif answer.lower() in ["f", "fortune"]:
			if self.caller.db.gold < 2:
				self.caller.msg("|/|mFortune Teller|n says: To divine the fates and peer into the mists is hard work, you need 2 gold for this service, come back when you've got the coin. Go forth, and let fate guide you.")
				return
			self.caller.db.gold -= 2
			self.caller.msg("|/The Fortune Teller takes the 2 gold coins offered and tucks them into a purse.")
			self.caller.msg("|mFortune Teller|n says: Not all things will reveal themselves immediately, the fates guard their knowledge well in riddle and mystery. Not all knowledge is happy, I will tell you true what I see, be not upset with the one that delivers the message.")
			self.caller.msg("A sprinkling of spicy herbs are cast into a brazier, filling the air with wispy smoke. The Fortune Teller breathes in deeply, jerking back, eyes wide and clouded white.")
			self.caller.msg("|mA demonic voice|n says: HERE MY WORDS ADVENTURER FOR THE FATES WILL NOT SUFFER TO REPEAT!")
			self.caller.msg("|mA demonic voice|n says: " + random.choice(fortunes))
			self.caller.msg("The Fortune Teller collapses on her table.")
			self.caller.msg("|mFortune Teller|n says: Speak not what fate has revealed to any other lest your life be cut short. Go forth, and let fate guide you.")
			return
		else:
			self.caller.msg("|/|mFortune Teller|n says: I can divine the enigmatic words of the uncertain mists, but I can't understand what you're saying. Quit bothering me.")
			return

class FortuneTellerCmdSet(CmdSet):
	key = "FortuneTellerCmdSet"
	def at_cmdset_creation(self):
		self.add(chatfortuneteller())

class fortuneteller(DefaultObject):
	def at_object_creation(self):
		ftdescriptions = ["Wild red hair like a roaring fire barely contained by a bandanna flows down and engulfs the fortune teller's black dress, rings sparkle and glitter on her long skinny fingers.", "Piercing blue eyes like star sapphires stare up at you from a tan round face. You suddenly realize you've been staring for several minutes, entranced and terrified.", "Tattoos of ancient mystic symbols cover a wrinkled and worn face surrounding light grey eyes, a thin smile reveals a jack o'lantern grin."]
		self.db.desc = random.choice(ftdescriptions)
		self.cmdset.add_default(FortuneTellerCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")