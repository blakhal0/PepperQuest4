from evennia import DefaultObject

class item(DefaultObject):
	name = ""
	price = ""
	desc = ""
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("givable")
		self.tags.add("battle" "world" "both")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = "?"
		self.db.desc = self.desc
	def return_appearance(self,looker):
		desc = str()
		desc = "|/"+ self.key + " - " + str(self.db.qty) + ". " + self.db.desc
		return desc

#sellable
class goldbar(item):
	name = "Gold Bar"
	price = 1500
	desc = "A shiny bar of solid gold."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class icemoss(item):
	name = "Ice Moss"
	price = 18
	desc = "Bright blue moss that glitters and sparkles."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class spiceflower(item):
	name = "Spice Flower"
	price = 40
	desc = "A red flower from an ancient pepper plant."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class wingofbat(item):
	name = "Wing of Bat"
	price = 40
	desc = "Probably pretty good fried with some hot sauce."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class stoneheart(item):
	name = "Stone Heart"
	price = 65
	desc = "A crystallized heart-shaped stone."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class rubymoss(item):
	name = "Ruby Moss"
	price = 100
	desc = "A lacy clump of ruby red moss."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class diamondring(item):
	name = "Diamond Ring"
	price = 5000
	desc = "A sparkling ring with a diamond in the shape of a slime."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class variablemap(DefaultObject):
	name = "Deserted Island Map"
	price = 5000
	desc = "Shimmering starlight makes a map on a large scallop shell marking a deserted island."
	def at_object_creation(self):
		self.locks.add("drop:false()")
		self.tags.add("map")
		self.db.desc = self.desc
		self.db.locationname = "desertedisland"

class seashell(item):
	name = "Sea Shell"
	price = 20
	desc = "An iridescent shell that shimmers in the sun."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class greenglass(item):
	name = "Green Glass"
	price = 700
	desc = "Beautiful green colored glass."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.glasscolor = "Green"
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class redglass(item):
	name = "Red Glass"
	price = 700
	desc = "Beautiful red colored glass."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.glasscolor = "Red"
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class blueglass(item):
	name = "Blue Glass"
	price = 700
	desc = "Beautiful blue colored glass."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.glasscolor = "Blue"
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class yellowglass(item):
	name = "Yellow Glass"
	price = 700
	desc = "Beautiful yellow colored glass."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.glasscolor = "Yellow"
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class purpleglass(item):
	name = "Purple Glass"
	price = 700
	desc = "Beautiful purple colored glass."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.glasscolor = "Purple"
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class orangeglass(item):
	name = "Orange Glass"
	price = 700
	desc = "Beautiful orange colored glass."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.glasscolor = "Orange"
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class chromacrystal(item):
	name = "Chroma Crystal"
	tokens = 350
	price = 80
	desc = "A color changing crystal."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class marcasitesugar(item):
	name = "Marcasite Sugar"
	price = 80
	desc = "Blue sand that glows in moonlight."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class hangmansrope(item):
	name = "Hangmans Rope"
	price = 1
	desc = "A length of hangmans rope."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

#World and Battle
	#health
class spicyherb(item):
	name = "Spicy Herb"
	tokens = 25
	price = 25
	desc = "Restores 15 HP. A spicy herb to put some pep in your step."
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("givable")
		self.tags.add("both")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["health", "15"]
		self.db.desc = self.desc

class fixerflask(item):
	name = "Fixer Flask"
	tokens = 75
	price = 75
	desc = "Restores 60 HP. Just a little sip to perk up the spirits."
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("givable")
		self.tags.add("both")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["health", "60"]
		self.db.desc = self.desc

	#magic
class magicdust(item):
	name = "Magic Dust"
	tokens = 30
	price = 30
	desc = "Restores 5 MP. Just like Grandma used to make!"
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("givable")
		self.tags.add("both")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["magic", "5"]
		self.db.desc = self.desc

class sageelixir(item):
	name = "Sage Elixir"
	tokens = 130
	price = 65
	desc = "Restores 15 MP. Small batch, hand crafted by dedicated sages."
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("givable")
		self.tags.add("both")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["magic", "15"]
		self.db.desc = self.desc

	#health and magic
class restoringruby(item):
	name = "Restoring Ruby"
	tokens = 200
	price = 200
	desc = "Restores 50 HP and 15 MP."
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("givable")
		self.tags.add("both")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["all", "50", "15"]
		self.db.desc = self.desc

class yorkshiretea(item):
	name = "Yorkshire Tea"
	tokens = 750
	price = 750
	desc = "Restores Full HP and Full MP."
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("givable")
		self.tags.add("both")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["all", "9999", "9999"]
		self.db.desc = self.desc

#World Only
	#travel
class fasterfeather(item):
	name = "Faster Feather"
	tokens = 10
	price = 50
	desc = "A mysterious feather of a lesser known avian. Travel to any known location."
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("givable")
		self.tags.add("world")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["travel"]
		self.db.desc = self.desc

#Battle Only
	#flee
class pocketsand(item):
	name = "Pocket Sand"
	tokens = 50
	price = 50
	desc = "Blinding sand used to escape from battle."
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("givable")
		self.tags.add("battle")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.phrase = "SHA-SHA-SHAAAA!!! You throw a handful of sand in the enemies eyes blinding them as you flee from battle."
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["flee"]
		self.db.desc = self.desc

#Attribute Increase
class powerpepper(item):
	name = "Power Pepper"
	price = 0
	statinc = 1
	stattype = "attack"
	desc = "Permanently increase attack by %d." % (statinc)
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("world")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["statinc"]
		self.db.stat = self.stattype
		self.db.increase = int(self.statinc)
		self.db.desc = self.desc

class armoredpepper(item):
	name = "Armored Pepper"
	price = 0
	statinc = 1
	stattype = "defense"
	desc = "Permanently increase defense by %d." % (statinc)
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("world")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["statinc"]
		self.db.stat = self.stattype
		self.db.increase = int(self.statinc)
		self.db.desc = self.desc

class magicalpepper(item):
	name = "Magical Pepper"
	price = 0
	statinc = 3
	stattype = "magic"
	desc = "Permanently increase max MP by %d." % (statinc)
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("world")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["statinc"]
		self.db.stat = self.stattype
		self.db.increase = int(self.statinc)
		self.db.desc = self.desc

class lifepepper(item):
	name = "Life Pepper"
	price = 0
	statinc = 5
	stattype = "health"
	desc = "Permanently increase max HP by %d." % (statinc)
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("world")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["statinc"]
		self.db.stat = self.stattype
		self.db.increase = int(self.statinc)
		self.db.desc = self.desc

#Generic
class itembook(DefaultObject):
	def at_object_creation(self):
		self.tags.add("readable", category="isreadable")
		self.tags.add("single", category="isreadable")
		self.db.story = "Book Contents"
		self.locks.add("drop:false()")
		self.db.desc = "It's a book, you might want to try and Read it."

class batspellbook(DefaultObject):
	name = "Bat!"
	price = 0
	desc = "A thick book bound in the skin of bats."
	def at_object_creation(self):
		self.tags.add("readable", category="isreadable")
		self.tags.add("spellbook", category="isreadable")
		self.db.story = """The ancient spell of Bat!|/|540|/     =/\                 /\=|/     / \'._    (\_/)   _.'/ \|/    / .''._'--(o.o)--'_.''. \|/   /.' _/ |`'=/ |500"|540 \='`| \_ `.\|/  /` .' `\;-,'\___/',-;/` '. '\|/ /.-'       `\(-V-)/`       `-.\|/ `            "   "            `|n"""
		self.db.spelldisplay = "Bat"
		self.db.spell = "bat"
		self.locks.add("get:false()")
		self.db.desc = "A thick book bound in the skin of bats."
		self.locks.add("drop:false()")

class raijinspellbook(DefaultObject):
	name = "Raijin"
	price = 0
	desc = "A thick book bound in copper, crackling with electricity."
	def at_object_creation(self):
		self.tags.add("readable", category="isreadable")
		self.tags.add("spellbook", category="isreadable")
		self.db.story = """The ancient spell of Raijin calls upon the spirit of the lightning god to destroy your enemies.|/|003                      dZZZZZ,|/                     dZZZZ  ZZ,|/             ,AZZZZZZZZZZZ  `ZZ,_|/        ,ZZZZZZV'      ZZZZ   `Z,`\|/|004      ,ZZZ    ZZ   .    ZZZZ   `V|/   ZZZZV'     ZZ         ZZZZ    \_|/   V   l   .   ZZ        ZZZZZZ|/   l    \       ZZ,     ZZZ  ZZZZZZ,|/  /            ZZ l    ZZZ    ZZZ `Z,|/              ZZ  l   ZZZ     Z Z, `Z,|/|005             ZZ      ZZZ      Z  Z, `l|/             Z        ZZ      V  `Z   \|/             V        ZZC     l   V|/|025             l        V ZR        l|/               \       l  ZA|/                \         C          |/|015                      \   K   /    /|/                   \   \  |  /  /|135|/                        \\||/ /  /|455|/                         \||/|n"""
		self.db.spelldisplay = "Raijin"
		self.db.spell = "raijin"
		self.locks.add("get:false()")
		self.db.desc = "A thick book bound in copper, crackling with electricity."
		self.locks.add("drop:false()")

class pyrettablazespellbook(DefaultObject):
	name = "PyrettaBlaze"
	price = 0
	desc = "A burning and charred book, red letters glow on the cover as it smokes."
	def at_object_creation(self):
		self.tags.add("readable", category="isreadable")
		self.tags.add("spellbook", category="isreadable")
		self.db.story = """The ancient spell of PyrettaBlaze calls upon the demon goddess of the funeral fire, Pyretta and her napalm tears.|/|300                       , ,                  |/                      /( )\                 |/                     ( \-/ )                |/            /\       )v  ))/        /\      |/           / \\'._    \_  /(      _.'/ \     |/          / .''._'--.--'   `-.--'_.''. \    |/         /.' _/ |`'=        , ='`| \_ `.\   |/        /` .' `\;-,' `(  (  ; ',-;/` '. '\  |/       /.-'       `\/  )   / \/`       `-.\ |/       `             .' .  |              ` |/                    /      |                |/                   |   ||/  |                |/                   |   |  /                 |/                   |   |.'                  |/                __/'  /                     |/            _ .'  _.-`                      |/          _.` `.-;`/   |550 (                   |/|550  ) |300       /_.-'` / |550/     )\ )      )    ) |/|550 /( ( |300         | / |550(   (()/(   ( /( ( /( ( |/|510(_)))\ ) |300     ( / |510))\   /(_))  )\()))\()))\ |/|500())(()/(  ) |300 /_/ |500/((_) (_))  )(_))/((_)\((_) |/|500 _| )(_))((_)_  (_))   / __|  | |_ | |(_)(_)|n"""
		self.db.spelldisplay = "pyrettablaze"
		self.db.spell = "pyrettablaze"
		self.locks.add("get:false()")
		self.db.desc = "A burning and charred book, red letters glow on the cover as it smokes."
		self.locks.add("drop:false()")

class khionekissspellbook(DefaultObject):
	name = "KhioneKiss"
	price = 0
	desc = "A book of solid ice with ancient runes glowing light blue on the cover."
	def at_object_creation(self):
		self.tags.add("readable", category="isreadable")
		self.tags.add("spellbook", category="isreadable")
		self.db.story = """The ancient spell of Khione Kiss calls upon the winter goddess as wicked and cold as a mountain storm, and just as deadly.|/|005                    ,;ssssssss;,|/|235        .|005         .;ssSSSSSSSSSs;,|/|235        :|005      .;ssSSSSSSSSSSSSSSSs|/|235  '.___/*\___.'|005ssSSSSSSSSSSSSSSSSSSs|n |510~~~~~~~~~|/|235    \* \ / */ |005ssSSSSSSSSSSSS'|511     ||///(((~~~~~~~|/|235     >--X--< |005ssSSSSSSSS(@)S' ====|n/=_ |512'))))~~~~~~|/|235    /*_/ \_*\|005SSSSSSSSSS()     ~=|n||_  ~  |513((((~~~~~~|/|235  .'   \*/ |005ss|235'|005SSSSSS'         | |n      |514(((((((((((|/|235        : |005sSSSSSS'         _/~'|n        |515)))))))))))|/|235        ' |005sSSSSS'   \      (|500x|n)         |415(((((((((((|/|005          /          ~-_   /|n~           |414)))))))))))|/|005         |            / ~~~|n\______--~  |413(((((((((((|/|005         |           | |n        /       |412)))))))))))|/|005        |   _-----__ | |n        /       |411((((((((((("""
		self.db.spelldisplay = "KhioneKiss"
		self.db.spell = "khionekiss"
		self.locks.add("get:false()")
		self.db.desc = "A book of solid ice with ancient runes glowing light blue on the cover.."
		self.locks.add("drop:false()")

class horrorcanespellbook(DefaultObject):
	name = "Horrorcane"
	price = 0
	desc = "A translucent tome, swirling with clouds and demonic forces."
	def at_object_creation(self):
		self.tags.add("readable", category="isreadable")
		self.tags.add("spellbook", category="isreadable")
		self.db.story = """The ancient spell of Horrorcane calls upon the wind demon Fuzuzu to unleash a hurricane of tormented souls.|/|=n               . '@(@@@@@@@)@. (@@)|/     .  @@'((@@@@@@@@@@@)@@@@@)@@@@@@@)@|/     @@(@@@@@@@@@@))@@@@@@@@@@@@@@@@)@@`|/  @.((@@@@@@@)(@@@@|500.-.|=n@@@@@@@))@\@@@@@)@@@|/ (@@@@@@@@@@@@@@@@|500(o o)|=n@@@@@\\@@)@@@@@@@@)|/(@@@@@@@@)@@@@@@@|500| O \|=n@@@@@@@@//@@@@@@@)|/ .@(@@@@)##&&&&&(@@|500\   \|=n@)(@\\@@@@)@@|/   @@`(@@)###&&&&&&&|500`~~~'|=n_=@@\\@)@`@|/   `   @@(@###&&&&!!;;;;-=_=@.@\\@@|/      `  @.#####&&&!;::=-_= .@  \\|/|500   .-.|=n      ####&&&!!;;::=_-     `|/|500  (o o)|=n       ###&&!!;;:-_=|/|500  | O \|=n        ##&&!;::_=|/|500   \   \|=n      ##&&!;:=|/|500    `~~~'|=n    ##&&!:-|/           #&!;:-    |500.-.|=n|/          #&!;=     |500(o o)|=n|/          #&!-      |500| O \|=n|/           #&=       |500\   \|=n|/            #&-       |500`~~~'|=n|/            \\#/'|n"""
		self.db.spelldisplay = "Horrorcane"
		self.db.spell = "horrorcane"
		self.locks.add("get:false()")
		self.db.desc = "A translucent tome, swirling with clouds and demonic forces."
		self.locks.add("drop:false()")

class hecatombspellbook(DefaultObject):
	name = "Hecatomb"
	price = 0
	desc = "A golden book emanating a holy light."
	def at_object_creation(self):
		self.tags.add("readable", category="isreadable")
		self.tags.add("spellbook", category="isreadable")
		self.db.story = """The holy spell of Hecatomb. Sacrifice half your life to the gods in hopes of destroying your enemy.|/______             |550 *  . | ,  * |n                 _______|/\______\-------___ |550 ._\  _^_  / _. |n  ____-------/_______/|/    \_____\---\\\\\\\\\    //_ _ \\    //////---/______/|/        \____\---\\\||| (( *||* )))  ||||//---/______/|/     _  _   \___\--\\\ ((\ = / ))) //--/___/     _ |/    ( `   )_    \__\-\_)))  \ _)))-/__/       (  _ )_|/   (    )    `)    \_/(((    ((((_/ _, _ .  ( `  ) . )|/|=s (_   (_ .  _) _)  (    )    `) ( )( (  _ )(_, _(  ,_)_)|/|=r              (_   (_ .  _) _)(_(_  _(_ ,)|/|=o            (_  _(_ ,)(_   (_ .  _) _)|n|/    \*"-._|/     \,   `"-._|/       ~'"-.__(o `._|/      /     \  `+-._`---.___|/   .-'      |500JL|n      `-.    /\|/  /   ` -  /|50088|n         `-.J_)|/ /./`Y ) '/  |500`"Y88b..|n|/ \) / / //      |500`Y8888a.|n|/(_.'_'.''         |50088888P|n"""
		self.db.spelldisplay = "Hecatomb"
		self.db.spell = "hecatomb"
		self.locks.add("get:false()")
		self.db.desc = "A golden book emanating a holy light."
		self.locks.add("drop:false()")

class deathspellbook(DefaultObject):
	name = "Death"
	price = 0
	desc = "A black book, dripping red ink."
	def at_object_creation(self):
		self.tags.add("readable", category="isreadable")
		self.tags.add("spellbook", category="isreadable")
		self.db.story = """An dark magic spell that creates a pact with a demon to instantly kill your enemy. But will the demon hold up their end of the bargain?|/                            ,-.|/       ___,|500---.__          |n/'|`\          |500__,---|n,___|/    ,-'    \|500`    `-.____,-|n'  |  `|500-.____,-'    |n//    `-.|/  ,'        | |500           ~'|n\     /|500`~          |n |        `.|/ /      ___//|500              |n`. ,'|500          ,  ,|n \___      \|/|    ,-'   |500`-.__   _        |        ,    __,-'|n   `-.    | |/|   /      |500    /\_  `   .   |    ,      _/\|n          \   | |/\  |       |500    \ \`-.___ \  |   / ___,-'/ /|n           |  /|/ \  \      |500     | `._   `\\  |  //'   _,' | |n           /  /|/  `-.\     |500    /'  _ `---'' , . ``---' _  `\|n         /,-'|/     ``   |500    /     \    ,='/ \`=.    /     \|n       ''|/          |500   ||__   /|\_,--.,-.--,--._/|\   __| |/          |n   /  `.|500/  \\`\ |  |  | /,//' \|n,'  \|/            /   /|500    ||-\--+--||--+--/-| |n    \   \|/           |   | |500    /'\_\_\  | /_/_/`\  |n   |   | |/            \   \__,|500 \_     `~'     _/|n .__/   /|/             `-._,-' |500  `-._______,-' |n   `-._,-'"""
		self.db.spelldisplay = "Death"
		self.db.spell = "death"
		self.locks.add("get:false()")
		self.db.desc = "A black book, dripping red ink."
		self.locks.add("drop:false()")

class ardtreaskey(DefaultObject):
	def at_object_creation(self):
		self.locks.add("drop:false()")
		self.db.desc = "Key to the Castle Ardismouf Treasury."