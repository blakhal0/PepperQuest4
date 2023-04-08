#class blank:
#	name = "name of beast"
#	hp = Number - amount of HP
#	mp = Number - amount of MP
#	attack = Number - attack strength
#	defense = Number - defense strength
#	gold = Number - amount of gold won for defeat
#	exp = Number - amount of exp won for defeat
#	actions = ["a", "d", "m", "i", "f", "n", "s"] a-attack, d-defend, m-magic, i-incapacitate, f-flee, n-no move, s-steal
#	noflee = yes(Hero cannot flee battle) no (Hero can attempt to flee battle)
#	weakness = ["no", "a", "e", "f", "w"] - no-no weaknesses, a-aqua weakness, e-electric weakness, f-fire weakness, w-wind weakness
#	incapatt = "Message sent to user to indicate incapacitation attack attempted"
#	incapsuc = "Message for successful incapacitation"
#	lazymsg = "Message for a no-move round."
#	stealtype = "magic/money"
#	drop = "yes/no"
#	droptype = "items/weapons/armor"
#	dropitem = "itemname"

#Monster ideas: Knight Owl, Desert Eagle

class droptest:
	name = "Drop Test"
	desc = "Test for dropping loot"
	phrases = []
	hp = 10
	mp = 0
	spells = [""]
	attack = 3
	defense = 3
	gold = 5
	exp = 1
	actions = ["a", "n"]
	noflee = "no"
	weakness = ["n"]
	incapatt = ""
	incapsuc = ""
	lazymsg = "stands there, organizing its inventory."
	stealtype = "none"
	drop = "yes"
	dropitem = "spicyherb"
	droptype = "items"

#zone 0
class trainingdummy:
	name = "Training Dummy"
	desc = "A simple training dummy."
	phrases = []
	hp = 6
	mp = 0
	spells = [""]
	attack = 3
	defense = 1
	gold = 0
	exp = 0
	actions = ["a", "d", "a", "a"]
	noflee = "no"
	weakness = ["f"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "n"
	dropitem = ""

#gods
class anansi:
	name = "Anansi"
	desc = "The spider god, formerly occupied the Temple of Small Gods."
	phrases = ["Hundreds of tiny spiders attack you.", "Anansi stabs at you with a giant leg."]
	hp = 40
	mp = 40
	spells = ["drown", "sprinkle"]
	attack = 8
	defense = 9
	gold = 200
	exp = 20
	actions = ["a", "m", "m", "i", "a", "i", "i", "m", "a", "a"]
	noflee = "yes"
	weakness = ["f"]
	incapatt = "weaves a tangled web around you."
	incapsuc = "You struggle against the spiders web, but cannot break free."
	lazymsg = ""
	stealtype = "none"
	drop = "yes"
	droptype = "items"
	dropitem = "lifepepper"
	god = "yes"
	successmsg = "|/Om begins to glow, brightening to a blinding light, his one eye blazing a bright red.|/|mOm the Mighty|n says: I AM OM THE MIGHTY, GREATEST OF ALL SMALL GODS, GOD OF THIS TEMPLE.|/A mighty thunderclap shakes the building.|/|mOm the Mighty|n says: I thank you for your belief in me. There are things I must tend to.|/A blinding flash of light emits from Om the Mighty."
	tagstoadd = ["omthemighty"]
	tagstoremove = []
	itemstoremove = ["Om the Mighty"]
	accoladetoadd = ""
	sendto = "#7529"

class thegoddessmorrighan:
	name = "The Goddess Morrighan"
	desc = "The washer at the ford, goddess of battle, will she clean your armor in the stream today?"
	phrases = ["Morrighan thrusts a wicked spear.", "Morrigan swings her sword."]
	hp = 50
	mp = 45
	spells = ["highboltage", "fullheal", "khionekiss"]
	attack = 61
	defense = 59
	gold = 400
	exp = 45
	actions = ["a", "m", "a", "a", "d", "m"]
	noflee = "yes"
	weakness = ["e"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "yes"
	dropitem = "powerpepper"
	droptype = "items"
	god = "yes"
	successmsg = "|/Morrighan kneels in defeat.|/|mThe Goddess Morrighan|n says: Today I wash no armor. You are truly a warrior of great might. But like all warriors, I will one day lead you from the field of battle. Watch for the day your armor is clean, for that day we will meet again."
	tagstoadd = ["morrighan"]
	tagstoremove = []
	itemstoremove = []
	accoladetoadd = ""
	sendto = ""

class thegoldengodofgreedmammoo:
	name = "The Golden God of Greed Mammoo"
	desc = "A golden god that hungers for nothing other than riches. Gold, gems, your life. All will be added to the great horde."
	phrases = ["Mammoo hurls golden coins at you.", "Mammoo laughs, golden eyes flashing as he swings his gilded sword.", "Mammoo swings a diamond gauntleted fist."]
	hp = 65
	mp = 45
	spells = ["twentyfourkarat", "fullheal"]
	attack = 55
	defense = 46
	gold = 2000
	exp = 60
	actions = ["a", "m", "a", "i", "a", "i"]
	noflee = "yes"
	weakness = []
	incapatt = "flashes golden eyes at you."
	incapsuc = "You have been turned into a golden statue, unable to move."
	lazymsg = ""
	stealtype = "none"
	drop = "yes"
	dropitem = "lifepepper"
	droptype = "items"
	god = "yes"
	successmsg = "|/Mammoo cries out in defeat and slumps to the ground.|/The golden statues begin to crack and shatter, Nemesis and Tyche step forward."
	tagstoadd = []
	tagstoremove = []
	itemstoremove = []
	accoladetoadd = "Fortunate One"
	sendto = ""

#Mini Bosses
class guardcaptain:
	name = "Guard Captain"
	desc = "A large and bulky guard in heavy armor. Captain of the Ardismouf Castle Guards."
	phrases = [""]
	hp = 45
	mp = 0
	spells = [""]
	attack = 25
	defense = 17
	gold = 200
	exp = 20
	actions = ["a"]
	noflee = "yes"
	weakness = ["n"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "yes"
	droptype = "items"
	dropitem = "armoredpepper"
	god = "yes"
	successmsg = "|/|mGuard Captain|n says: You don't fight like a thief. Your face, like from the books, where are you from?|/You cut the Guard Captain off, tossing the Red, Blue, and Green keys for the castle in their face. Wouldn't want anyone to get in trouble for losing the keys again.|/With the Guard Captain safely incapacitated, you can retrieve the Treasury Key without issue."
	tagstoadd = []
	tagstoremove = []
	itemstoremove = ["Ardismouf Blue Key", "Ardismouf Red Key", "Ardismouf Green Key"]
	accoladetoadd = ""
	sendto = ""

class honkiamat:
	name = "Honkiamat"
	desc = "The physical manifestation of hate and vitriol in buoyant and feathery form."
	phrases = ["Honk-honk-HONK-hONK-HonK", "Gigantic wings flap furiously, blasting you with wind.", "You lose sight of Honkiamat, *OUCH**OUCH**OUCH**OUCH**OUCH* you've been bitten on the butt."]
	hp = 100
	mp = 45
	spells = ["fullheal", "highboltage", "insinerate", "frostflower", "galeforce", "honkoffivehells"]
	attack = 89
	defense = 96
	gold = 2000
	exp = 500
	actions = ["a", "m", "a", "a", "i", "s", "m", "m"]
	noflee = "yes"
	weakness = ["n"]
	incapatt = "lowers one of its heads and hisses at you"
	incapsuc = "You are too terrified to move."
	lazymsg = ""
	stealtype = "magic"
	drop = "yes"
	droptype = "items"
	dropitem = "armoredpepper"
	god = "yes"
	successmsg = "|/|mHonkiamat|n hisses angrily: What have you done, why would you do this??? I was the only thing keeping them contained. You've released them back into the world."
	tagstoadd = []
	tagstoremove = []
	itemstoremove = []
	accoladetoadd = "Hellion"
	sendto = ""

class malashai:
	name = "Malashai"
	desc = "The Dark Sorcerer of Time"
	phrases = [""]
	hp = 90
	mp = 180
	spells = ["hurt", "moreheal", "timewarp"]
	attack = 69
	defense = 87
	gold = 500
	exp = 250
	actions = ["a", "m", "m", "i", "m", "a", "m", "s"]
	noflee = "yes"
	weakness = ["a", "w"]
	incapatt = "throws hourglass sand in the air, freezing you in time."
	incapsuc = "You are frozen in time, unable to move."
	lazymsg = ""
	stealtype = "magic"
	drop = "no"
	droptype = ""
	dropitem = ""
	god = "yes"
	successmsg = "|/Malashai|n screams: NO! NO! I AM THE MASTER OF TIME!|/Malashai flickers and fades, flipping rapidly between a child, a young man, an adult, the inky miasma, and a rotting skeleton.|/The hourglass drops from his grip, rapidly disintegrating as he disappears into nothingness."
	tagstoadd = [""]
	tagstoremove = [""]
	itemstoremove = [""]
	accoladetoadd = ""
	sendto = ""

#Titan Arena Monsters
class titanslime:
	name = "Titan Slime"
	desc = "The Titan Slime strongest of all goo based terrestrial slimes in the arena. "
	phrases = ["*Sluuuurp*", "The Titan Slime jumps high into the air and lands on you."]
	hp = 18
	mp = 0
	spells = [""]
	attack = 12
	defense = 24
	gold = 10
	exp = 10
	actions = ["a", "d", "i", "a", "a"]
	noflee = "yes"
	weakness = ["e"]
	incapatt = "jumps on you, surrounding you in slime."
	incapsuc = "You are trapped in the Titan Slime and cannot move."
	lazymsg = ""
	stealtype = "none"
	drop = "n"
	dropitem = ""
	god = "yes"
	successmsg = "|/|mAnnouncer: AND WE HAVE A WINNER IN ROUND 1!! LET'S SEE IF THEY CAN SURVIVE THE CHALLENGE IN THE NEXT FIGHT!"
	tagstoadd = ["arena1"]
	tagstoremove = []
	itemstoremove = []
	accoladetoadd = ""
	sendto = "#7875"

class magidraky:
	name = "MagiDraky"
	desc = "The Titan Arena's very own, and very special, MagiDraky is the oldest and wisest of Draky's having spent a long life leaning the mystic arts."
	phrases = ["MagiDraky swoops in with a razor wing.", "MagiDraky gnaws at your knee."]
	hp = 26
	mp = 30
	spells = ["moreheal", "volt", "swoosh", "flicker", "furnace"]
	attack = 18
	defense = 22
	gold = 10
	exp = 10
	actions = ["m", "m", "m", "d", "a", "m", "a", "a", "m", "s"]
	noflee = "yes"
	weakness = ["w"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "magic"
	drop = "n"
	dropitem = ""
	god = "yes"
	successmsg = "|/|mAnnouncer: AND WE HAVE A WINNER IN ROUND 2!! LET'S SEE IF THEY CAN SURVIVE THE CHALLENGE IN THE NEXT FIGHT!"
	tagstoadd = ["arena2"]
	tagstoremove = ["arena1"]
	itemstoremove = []
	accoladetoadd = ""
	sendto = "#7876"

class chromadillo:
	name = "Chromadillo"
	desc = "The shiniest monster in the Titan Arena the chrome clad weremadillo... the Chomeadillo."
	phrases = ["Scuttle-scuttle-POUNCE!"]
	hp = 34
	mp = 0
	spells = [""]
	attack = 23
	defense = 30
	gold = 10
	exp = 10
	actions = ["a", "d", "d", "a", "a", "a", "i", "d", "a"]
	noflee = "yes"
	weakness = ["e"]
	incapatt = "curls into a disco ball and blinds you with light!"
	incapsuc = "You are blinded and cannot see to attack."
	lazymsg = ""
	stealtype = "none"
	drop = "n"
	dropitem = ""
	god = "yes"
	successmsg = "|/|mAnnouncer: AND WE HAVE A WINNER IN ROUND 3!! LET'S SEE IF THEY CAN SURVIVE THE CHALLENGE IN THE NEXT FIGHT!"
	tagstoadd = ["arena3"]
	tagstoremove = ["arena2"]
	itemstoremove = []
	accoladetoadd = ""
	sendto = "#7877"

class knightowl:
	name = "Knight Owl"
	desc = "A knight of the Tital Arena, a real hoot if you're not on the receiving end of their claws."
	phrases = ["Knight Owl attacks with claws.", "Hucks a pellet at you."]
	hp = 35
	mp = 26
	spells = ["heal", "gust", "galeforce"]
	attack = 48
	defense = 34
	gold = 90
	exp = 10
	actions = ["a", "a", "m", "d", "a", "m"]
	noflee = "yes"
	weakness = ["w", "f"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "yes"
	dropitem = "restoringruby"
	droptype = "items"
	god = "yes"
	successmsg = "|/|mAnnouncer: AND WE HAVE A WINNER IN ROUND 4!! LET'S SEE IF THEY CAN SURVIVE THE CHALLENGE IN THE NEXT FIGHT!"
	tagstoadd = ["arena4"]
	tagstoremove = ["arena3"]
	itemstoremove = []
	accoladetoadd = ""
	sendto = "#7878"

class stealslime:
	name = "Steal Slime"
	desc = "The Titan Arena's sneakiest enemy."
	phrases = []
	hp = 15
	mp = 20
	spells = ["hurt"]
	attack = 10
	defense = 90
	gold = 90
	exp = 10
	actions = ["m", "d", "s", "s", "m", "s", "d"]
	noflee = "yes"
	weakness = ["a"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "magic"
	drop = "yes"
	dropitem = "diamondring"
	droptype = "items"
	god = "yes"
	successmsg = "|/|mAnnouncer: AND WE HAVE A WINNER IN ROUND 5!! IT'S GETTING CLOSE LADIES AND GENTLEMEN. LET'S SEE IF THEY CAN SURVIVE THE CHALLENGE IN THE NEXT FIGHT!"
	tagstoadd = ["arena5"]
	tagstoremove = ["arena4"]
	itemstoremove = []
	accoladetoadd = ""
	sendto = "#7879"

class blothartheberserker:
	name = "Blothar the Berserker"
	desc = "Titan Arena's only demigod. Blothar was born in the Bay of Blood and raised by scumdogs."
	phrases = ["Swings his axe with a grunt.", "Flicks a booger at you."]
	hp = 85
	mp = 0
	spells = [""]
	attack = 88
	defense = 80
	gold = 150
	exp = 10
	actions = ["a"]
	noflee = "yes"
	weakness = ["n"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "n"
	dropitem = ""
	god = "yes"
	successmsg = "|/|mAnnouncer: AND WE HAVE A WINNER IN ROUND 6!! ONLY TWO CHALLENGES REMAIN! LET'S SEE IF THEY CAN SURVIVE THE CHALLENGE IN THE NEXT FIGHT!"
	tagstoadd = ["arena6"]
	tagstoremove = ["arena5"]
	itemstoremove = []
	accoladetoadd = ""
	sendto = "#7880"

class megoosea:
	name = "Megoosea"
	desc = "Gorgon of the Titan Arena but with long slender goose heads instead of snakes. HONK!"
	phrases = ["*honk-HONK-hoNK-HoNK*", "honk honk honk", "Megoosa attacks with biting goose heads.", "HONK!!!!"]
	hp = 90
	mp = 45
	spells = ["aquaduck", "frostflower", "moreheal"]
	attack = 90
	defense = 90
	gold = 90
	exp = 10
	actions = ["a", "i", "i", "a", "a", "m"]
	noflee = "yes"
	weakness = ["f"]
	incapatt = "unleashes a sonic boom of honks."
	incapsuc = "You are terrified from all the honking and cannot move."
	lazymsg = ""
	stealtype = "none"
	drop = "yes"
	dropitem = "magicalpepper"
	droptype = "items"
	god = "yes"
	successmsg = "|/|mAnnouncer: AND WE HAVE A WINNER IN ROUND 7!! THIS IS IT LADIES AND GENTLEMEN! THE ONE WE'VE ALL BEEN WAITING FOR, A CHALLENGER HAS EARNED THE RIGHT TO FACE THE TITAN!!! LET'S SEE IF THEY CAN SURVIVE THE CHALLENGE IN THE NEXT FIGHT!"
	tagstoadd = ["arena7"]
	tagstoremove = ["arena6"]
	itemstoremove = []
	accoladetoadd = ""
	sendto = "#7881"

class titanophion:
	name = "Titan Ophion"
	desc = "Titan of the Arena."
	phrases = ["Strikes with a gigantic fist.", "Sweeps a massive foot at you.", "Smashes you with an open hand."]
	hp = 100
	mp = 75
	spells = ["fullheal", "titansfury"]
	attack = 95
	defense = 98
	gold = 2000
	exp = 500
	actions = ["a", "m", "i", "a", "d", "m", "a", "i"]
	noflee = "yes"
	weakness = ["n"]
	incapatt = "stomps the ground causing an earthquake."
	incapsuc = "The ground continues to shake, you cannot stand up."
	lazymsg = ""
	stealtype = "none"
	drop = "n"
	dropitem = ""
	god = "yes"
	successmsg = "|/The Titan Ophion bends to a knee and bows his head before you.|/|mTitan|n says: Never before have I witnessed such strength and perseverance. My throne is yours.|/The crowd erupts, shaking the very arena like an earthquake.|/|mAnnouncer|n says: A SIGHT FOR THE AGES!! WE HAVE A NEW TITAN OF THE ARENA!!!! CONGRATULATIONS!|/Please see the Host to collect your reward."
	tagstoadd = ["titan"]
	tagstoremove = ["arena7"]
	itemstoremove = []
	accoladetoadd = ""
	sendto = "#7861"

#papzone 1 HP 3-7, att 5-11, def 3-8, 
class slime:
	name = "Slime"
	desc = "The noble slime. Blue, slimy, but with a friendly smile. It's almost a shame to kill them.... almost."
	phrases = ["The slime slides forward and attacks!", "*Giggle...giggle...BOUNCE!* The slime pounces!"]
	hp = 3
	mp = 0
	attack = 5
	defense = 3
	gold = 1
	exp = 1
	noflee = "no"
	weakness = ["no"]
	actions = ["a"]
	drop = "no"
	dropitem = ""
	droptype = ""

class ghostpepper:
	name = "Ghost Pepper"
	desc = "As spooky as it is spicy. BOOOOO!"
	phrases = []
	hp = 4
	mp = 0
	spells = [""]
	attack = 4
	defense = 3
	gold = 2
	exp = 1
	actions = ["a"]
	noflee = "no"
	weakness = ["n"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "yes"
	dropitem = "spicyherb"
	droptype = "items"

class drip:
	name = "Drip"
	desc = "A drip of malevolent fluid."
	phrases = ["Flies up in the air and drips on your head."]
	hp = 4
	mp = 0
	spells = [""]
	attack = 3
	defense = 2
	gold = 2
	exp = 1
	actions = ["a"]
	noflee = "no"
	weakness = ["n"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "no"
	dropitem = ""

#papzone 2
class fishnclips:
	name = "Fish n Clips"
	desc = "Who gave the fish a gun??!?!?! Beware all pescatarians."
	phrases = ["Unloads a full clip from its Mackerel-10 in your general direction."]
	hp = 15
	mp = 0
	spells = [""]
	attack = 10
	defense = 7
	gold = 5
	exp = 3
	actions = ["a", "n", "a", "a"]
	noflee = "no"
	weakness = ["e", "f"]
	incapatt = ""
	incapsuc = ""
	lazymsg = "flops on the ground because it can't breathe. You know, since it's a fish. duh."
	stealtype = "none"
	drop = "yes"
	dropitem = "seashell"
	droptype = "items"

class monstrositea:
	name = "Monstrositea"
	desc = "An unholy cup of leaf water."
	phrases = ["Oolong live the queen! Monstrositea attempts to colonize your land.", "Monstrositea slaps you with a teabag."]
	hp = 8
	mp = 0
	spells = [""]
	attack = 11
	defense = 8
	gold = 6
	exp = 4
	actions = ["a"]
	noflee = "no"
	weakness = ["e"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "yes"
	dropitem = "spicyherb"
	droptype = "items"

#papzone 3
class draky:
	name = "Draky"
	desc = "A mischievous little fat flying critter."
	phrases = []
	hp = 15
	mp = 8
	spells = ["flicker"]
	attack = 3
	defense = 3
	gold = 4
	exp = 3
	noflee = "no"
	weakness = ["w"]
	actions = ["m", "m", "a"]
	drop = "no"
	dropitem = ""
	droptype = ""

class silverslime:
	name = "Silver Slime"
	desc = "A shimmering silver blob, bet that hide is worth a few pennies..."
	phrases = ["I'm the gooreatest!! Silver Slime attacks!", "The Silver Slime transforms into a metal spike and launches itself at you."]
	hp = 22
	mp = 0
	spells = [""]
	attack = 12
	defense = 24
	gold = 23
	exp = 10
	actions = ["a", "a", "d", "f", "d", "a", "a", "f"]
	noflee = "yes"
	weakness = ["n"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "yes"
	dropitem = "silverknife"
	droptype = "weapons"


#tormey HP 12-20, att 11-18, def 12-16, exp 4-6, gold 11-16
#tormey marsh
class poisonfrog:
	name = "Poison Frog"
	desc = "A brightly colored spear toting frog. Pretty, but don't let it lick you!"
	phrases = ["Poison Frog slaps you with its tongue.", "Poison Frog launches in the air and lands on you."]
	hp = 12
	mp = 0
	attack = 11
	defense = 12
	gold = 13
	exp = 4
	noflee = "no"
	weakness = ["no"]
	actions = ["a", "i", "a"]
	incapatt = "licks you with a bumpy tongue."
	incapsuc = "You are paralyzed and cannot attack!"
	drop = "yes"
	dropitem = "spicyherb"
	droptype = "items"

class battree:
	name = "Bat Tree"
	desc = "An evil tree swarming with electric bats. Quite shocking."
	phrases = ["Bat Tree shakes its branches, launching a flurry of bats at you."]
	hp = 16
	mp = 10
	spells = ["spark", "arc"]
	attack = 13
	defense =16
	gold = 4
	exp = 6
	noflee = "no"
	weakness = ["a"]
	actions = ["m", "m", "a"]
	drop = "no"
	dropitem = ""
	droptype = ""
#highlands
class chillidog:
	name = "Chili Dog"
	desc = "Might act like a hot-dog, but its bite will leave you dead cold."
	phrases = []
	hp = 15
	mp = 12
	spells = ["frostbite"]
	attack = 11
	defense = 12
	gold = 13
	exp = 5
	actions = ["a", "m", "n"]
	noflee = "no"
	weakness = ["n"]
	incapatt = ""
	incapsuc = ""
	lazymsg = "scratches lazily at an itch."
	stealtype = "none"
	drop = "no"
	dropitem = ""
	droptype = ""

class pizzarat:
	name = "Pizza Rat"
	desc = "It just needs a little money for a slice, just one slice. Got tree-fiddy?"
	phrases = ["Pizza Rat pushes you down trying to steal money.", "Pizza Rat throws an empty pizza box."]
	hp = 18
	mp = 0
	spells = [""]
	attack = 17
	defense = 15
	gold = 14
	exp = 6
	actions = ["a", "i", "s"]
	noflee = "no"
	weakness = ["n"]
	incapatt = "asks if you could spare some money."
	incapsuc = "You're stunned by the audacity of the rat and cannot gather your thoughts to attack."
	lazymsg = ""
	stealtype = "money"
	drop = "no"
	dropitem = ""
	droptype = ""

class spicypickle:
	name = "Spicy Pickle"
	desc = "A proud warrior from the Vinegara region, raised on hot peppers, it's said their very spit is acidic."
	phrases = []
	hp = 20
	mp = 0
	attack = 18
	defense = 16
	gold = 16
	exp = 6
	noflee = "no"
	weakness = ["no"]
	actions = ["a", "a", "i", "a"]
	incapatt = "spits acid at your eyes."
	incapsuc = "You are blinded and cannot attack!"
	drop = "no"
	dropitem = ""
	droptype = ""

class thegimp:
	name = "The Gimp"
	desc = "A tall lanky form, clad head to toe in shiny black leather armor."
	phrases = ["Uhhhhh, YES!! HARDER!!!!", "The Gimp just stares at you, making a little heart sign with their hands", "Can we fight later? I'm a little tied up.", "Do you like sandwiches? I prefer a sub.", "Why do I dress like this? BEATS ME!!!", "I just love getting gag gifts."]
	hp = 35
	mp = 20
	attack = 15
	defense = 18
	gold = 20
	exp = 15
	noflee = "yes"
	weakness = ["no"]
	actions = ["i", "a", "a", "i"]
	incapatt = "grabs you by the back of the neck and throws you in the stocks. You hear strange music suddenly.|/|mThe Gimp|n says: Looks like the spider caught a fly."
	incapsuc = "You are trapped!"
	drop = "yes"
	dropitem = "gimpsuit"
	droptype = "armor"

class castleguard:
	name = "Castle Guard"
	desc = "A Guard of the Castle Ardismouf."
	phrases = []
	hp = 28
	mp = 0
	attack = 20
	defense = 17
	gold = 13
	exp = 5
	actions = ["a"]
	noflee = "no"
	weakness = ["n"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "no"
	dropitem = ""
	droptype = ""

#Kharro HP 22-34, att 22-40, def 18-30, exp 14-16, gold 16-45
#dunes and cliffs
class sandwitch:
	name = "Sand Witch"
	desc = "A wrinkly dried out old desert hag, warts and all."
	phrases = []
	hp = 22
	mp = 20
	spells = ["gust", "heal"]
	attack = 15
	defense = 18
	gold = 20
	exp = 15
	noflee = "no"
	weakness = ["no"]
	actions = ["s", "m", "m", "a"]
	stealtype = "magic"
	drop = "yes"
	dropitem = "magicdust"
	droptype = "items"

class weremadillo:
	name = "Weremadillo"
	desc = "Beware the full moon, for that is when the Weremadillo stalks the night. Scuttle-scuttle-scuttle POUNCE!! Deathly allergic to chrome plated bumpers."
	phrases = []
	hp = 34
	mp = 0
	attack = 40
	defense = 30
	gold = 45
	exp = 16
	noflee = "no"
	weakness = ["e"]
	actions = ["a", "d", "a", "d", "i", "a"]
	incapatt = "kicks up a cloud of dirt."
	incapsuc = "You are blinded and cannot attack!"
	drop = "yes"
	dropitem = "pocketsand"
	droptype = "items"

class fradycat:
	name = "Fradycat"
	desc = "Aww, a cute cuddly kitty!!"
	phrases = ["Fradycat scratches with its claws!", "Fradycat bites your elbow."]
	hp = 26
	mp = 0
	attack = 28
	defense = 22
	gold = 30
	exp = 11
	noflee = "no"
	weakness = ["a"]
	actions = ["a", "a", "f", "a"]
	drop = "yes"
	dropitem = "marcasitesugar"
	droptype = "items"
#kharro desert
class firewolf:
	name = "Fire Wolf"
	desc = "A majestic beast, wreathed in flame. Wherever it goes, destruction is sure to follow."
	phrases = []
	hp = 33
	mp = 20
	spells = ["furnace"]
	attack = 33
	defense = 28
	gold = 35
	exp = 16
	actions = ["a", "m", "a", "a", "i"]
	noflee = "no"
	weakness = ["a"]
	incapatt = "emits a smoky howl, paralyzing you with fear."
	incapsuc = "You are paralyzed with fear and cannot attack."
	lazymsg = ""
	stealtype = "magic"
	drop = "yes"
	dropitem = "chromacrystal"
	droptype = "items"

class robinhood:
	name = "Rob in Hood"
	desc = "It's Rob, your friendly neighborhood thief... but in a hood! He wants to know if he can borrow your bike."
	phrases = ["Rob in Hood throws a pocket of gold coins at you.", "Rob in Hood attacks with a bow staff!"]
	hp = 10
	mp = 0
	attack = 3
	defense = 1
	gold = 2
	exp = 1
	noflee = "no"
	weakness = ["no"]
	actions = ["s", "a", "a", "s"]
	stealtype = "money"
	drop = "yes"
	dropitem = "goldbar"
	droptype = "items"

#Orthan HP 35-46, att 47-68, def 34-56, exp 17-28, gold 85-120
class apeofwrath:
	name = "Ape of Wrath"
	desc = "A descendant of those that once ruled, this damned dirty ape seeks revenge for its fallen civilization."
	phrases = []
	hp = 35
	mp = 0
	spells = [""]
	attack = 48
	defense = 34
	gold = 90
	exp = 18
	actions = ["a"]
	noflee = "yes"
	weakness = ["n"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "no"
	dropitem = ""

class swearwolf:
	name = "SwearWolf"
	desc = "What the F*&^ are you looking at? This lycanthrope is more like a lycanNOPE."
	phrases = ["Jebiesz jeze", "Merde", "Tofu no kado ni atama wo butsukete shine", "Ik laat een scheet in jouw richting", "Zajebiste", "Go n-ithe an cat thu, is go n-ithe an diabhal an cat."]
	hp = 43
	mp = 0
	spells = [""]
	attack = 53
	defense = 37
	gold = 96
	exp = 21
	actions = ["a", "n", "a", "a", "i", "i"]
	noflee = "no"
	weakness = ["w"]
	incapatt = "unleashes a torrent of foul language."
	incapsuc = "You are shocked and stunned at the profanity and cannot attack."
	lazymsg = "scratches at a flea bite, swearing incessantly."
	stealtype = "none"
	drop = "no"
	dropitem = ""

class beezerker:
	name = "Beezerker"
	desc = "A giant, angry, fuzzy bumblebee. WITH A TASTE FOR BLOOD!!!"
	phrases = []
	hp = 45
	mp = 0
	spells = [""]
	attack = 57
	defense = 42
	gold = 105
	exp = 23
	actions = ["a"]
	noflee = "yes"
	weakness = ["n"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "yes"
	dropitem = "spicyherb"
	droptype = "items"

class sonarlesssheep:
	name = "Sonarless Sheep"
	desc = "It's a sheep, but without sonar. So, I guess a regular sheep? But spicier."
	phrases = []
	hp = 40
	mp = 0
	spells = [""]
	attack = 62
	defense = 50
	gold = 115
	exp = 26
	actions = ["a", "f", "n"]
	noflee = "no"
	weakness = ["e"]
	incapatt = ""
	incapsuc = ""
	lazymsg = "stands there grazing, apparently completely unaware that you're fighting."
	stealtype = "none"
	drop = "no"
	dropitem = ""
	droptype = ""

class brickfrog:
	name = "Brick Frog"
	desc = "It's BRICK FROG!!!!"
	phrases = ["Brick Frog chucks a brick at you."]
	hp = 44
	mp = 0
	spells = [""]
	attack = 61
	defense = 51
	gold = 117
	exp = 28
	actions = ["a", "i", "i", "a"]
	noflee = "no"
	weakness = ["n"]
	incapatt = "smacks you with a brick."
	incapsuc = "Your vision is blurry from a severe case of brick to the head-itis."
	lazymsg = ""
	stealtype = "none"
	drop = "no"
	dropitem = ""

class battlepenguin:
	name = "Battle Penguin"
	desc = "Forced from its home by the destruction of the polar icecaps, this penguin is out for revenge."
	phrases = []
	hp = 46
	mp = 0
	spells = [""]
	attack = 68
	defense = 56
	gold = 120
	exp = 30
	actions = ["a", "d", "a", "a"]
	noflee = "no"
	weakness = ["e"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "no"
	dropitem = ""

#varken hp 50-70, att 65-86, def 57-80, exp 34-50, gold 110-160
class mentholmage:
	name = "Menthol Mage"
	desc = "Icy cool spells are this creatures calling card."
	phrases = []
	hp = 50
	mp = 45
	spells = ["frostflower", "moreheal"]
	attack = 60
	defense = 57
	gold = 121
	exp = 36
	actions = ["a", "m", "m"]
	noflee = "no"
	weakness = ["f"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "yes"
	dropitem = "sageelixir"
	droptype = "items"

class nightdanger:
	name = "Night Danger"
	desc = "A moose once bit my sister... No really. Mind you, moose bites can be pretty nasty. All moose appearing in PepperQuest 4: Ever trained by Yutte Hermsgervordenbrotborda. Special moose effects by Olaf Prot. *No moose were harmed during the making of PepperQuest 4: Ever. Not from lack of trying though, they're just bloody tough critters. One 'Ralph the Venezuelan Wonder Llama' got a bit roughed up, but he started it. **PepperQuest, Peppercon, its subsidiaries and franchises, and all persons (and moose) associated with production of this game respect and revere the noble moose. Please take appropriate precautions when dealing with wild animals. This message brought to you by Svenge, an Olso dentist who, like 9 out of 10 Norwegian dentists, thoroughly endorses InterSpace Toothbrushes. ***Do not use sharpened InterSpace Toothbrushes to attempt to carve your initials into a moose. You can get bit that way you know."
	phrases = []
	hp = 58
	mp = 0
	spells = [""]
	attack = 65
	defense = 62
	gold = 134
	exp = 46
	actions = ["a"]
	noflee = "yes"
	weakness = ["n"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "no"
	dropitem = ""

class abdominalsnowman:
	name = "Abdominal Snowman"
	desc = "Just because it's chilly won't stop this monster from getting those reps in. Do you even ski-lift bro?"
	phrases = []
	hp = 67
	mp = 0
	spells = [""]
	attack = 72
	defense = 72
	gold = 150
	exp = 50
	actions = ["a", "n", "i", "a", "n", "n"]
	noflee = "no"
	weakness = ["a"]
	incapatt = "takes off its shirt of starts flexing."
	incapsuc = "You are in awe of the physique, so... many... abs."
	lazymsg = "sees itself in a nearby reflection and starts posing and making kissy noises at itself."
	stealtype = "none"
	drop = "no"
	dropitem = ""

class haranguetan:
	name = "Haranguetan"
	desc = "This ape knows how to really hurt you... with words."
	phrases = ["Well, if THAT's the look you're going for, I guess.|/EMOTIONAL DAMAGE!!!", "Oh, it's my turn to attack finally, well thanks for letting me have a turn, I know you're just sooooo busy.|/EMOTIONAL DAMAGE!!!"]
	hp = 70
	mp = 100
	spells = ["emotionaldamage"]
	attack = 86
	defense = 80
	gold = 160
	exp = 55
	actions = ["a", "m", "m", "m"]
	noflee = "no"
	weakness = ["n"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "no"
	dropitem = ""
	droptype = ""

class goldenslime:
	name = "Golden Slime"
	desc = "A shiny slime, made of gold!"
	phrases = []
	hp = 20
	mp = 0
	attack = 60
	defense = 90
	gold = 1000
	exp = 20
	noflee = "no"
	weakness = ["no"]
	actions = ["a", "d", "a", "a", "a", "f"]
	drop = "yes"
	dropitem = "diamondring"
	droptype = "items"

#warfront
class bonesnapper:
	name = "Bone Snapper"
	desc = "How many have fallen before you? How many have you sent below? How can you ever show pity? Is that word that you know?"
	phrases = []
	hp = 75
	mp = 0
	spells = [""]
	attack = 86
	defense = 74
	gold = 110
	exp = 62
	actions = ["a", "i", "a", "a"]
	noflee = "no"
	weakness = ["e"]
	incapatt = "opens its maw of death and snaps!"
	incapsuc = "Your bones are snapped, you wail in agony, unable to move."
	lazymsg = ""
	stealtype = "none"
	drop = "yes"
	dropitem = "fixerflask"
	droptype = "items"

class gwarrior:
	name = "GWARrior"
	desc = "During one fateful battle the Scumdogs of the Universe were destroyed, utterly. From the writhing pile of guts and pustulance rose anew the GWARrior."
	phrases = ["Death cannot kill the GWARrior!!"]
	hp = 85
	mp = 0
	spells = [""]
	attack = 88
	defense = 80
	gold = 160
	exp = 65
	actions = ["a", "i", "a", "a", "i"]
	noflee = "no"
	weakness = ["n"]
	incapatt = "barfs space slime in your face and screams."
	incapsuc = "You are enthralled by the GWARrior and cannot attack."
	lazymsg = ""
	stealtype = "none"
	drop = "no"
	dropitem = ""

class heckromancer:
	name = "Heckromancer"
	desc = "Pied Piper of the dead, summons sounds from beyond the grave to attack."
	phrases = ["A corpse shaking bass line rattles your teeth.", "Summons the screams of the dead, but with a nice groove.", "Flings spicy queso at you, made from the milk of an undead cow."]
	hp = 45
	mp = 60
	spells = []
	attack = 30
	defense = 25
	gold = 77
	exp = 10
	actions = ["a"]
	noflee = "no"
	weakness = ["n"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "no"
	dropitem = ""
	droptype = ""

#magmamadness
class lavalarvae:
	name = "Lava Larvae"
	desc = "A fiery crawling critter, dripping molten rock as it crawls along."
	phrases = ["Spits a ball of lava"]
	hp = 50
	mp = 0
	spells = [""]
	attack = 60
	defense = 53
	gold = 85
	exp = 45
	actions = ["a", "n"]
	noflee = "no"
	weakness = ["a"]
	incapatt = ""
	incapsuc = ""
	lazymsg = "takes a slurp of lava flowing past."
	stealtype = "none"
	drop = "n"
	dropitem = ""

class krakentoa:
	name = "Krakentoa"
	desc = "Eight arms, one beak, all living fire."
	phrases = []
	hp = 55
	mp = 0
	spells = [""]
	attack = 67
	defense = 53
	gold = 132
	exp = 46
	actions = ["a"]
	noflee = "no"
	weakness = ["e", "a"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "n"
	dropitem = ""

class vulcanvillain:
	name = "Vulcan Villain"
	desc = "A wizard robed in fire."
	phrases = []
	hp = 59
	mp = 72
	spells = ["charbq"]
	attack = 69
	defense = 56
	gold = 125
	exp = 52
	actions = ["a", "m", "a", "m", "m"]
	noflee = "no"
	weakness = ["w"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "yes"
	dropitem = "restoringruby"
	droptype = "items"

class galeras:
	name = "Galeras"
	desc = "A lava slobbering mound of lumbering rock."
	phrases = []
	hp = 70
	mp = 0
	spells = [""]
	attack = 70
	defense = 64
	gold = 150
	exp = 65
	actions = ["a", "d", "a", "a", "a"]
	noflee = "no"
	weakness = ["n"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "n"
	dropitem = ""

#valharra
class granreaper:
	name = "Gran Reaper"
	desc = "It's just a sweet little old lady, how dangerous could she be?"
	phrases = ["Now just come on over you little whipper-snapper! Gran Reaper swings her scythe.", "Back in my day we respected the physical manifestation of death!! YEYAAAA!!!"]
	hp = 70
	mp = 30
	spells = ["death"]
	attack = 88
	defense = 74
	gold = 225
	exp = 54
	actions = ["a", "m", "a", "a"]
	noflee = "no"
	weakness = ["n"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "no"
	dropitem = ""
	droptype = ""

class thaihothydra:
	name = "Thai Hot Hydra"
	desc = "A living plant monster with hundreds of heads growing from its branches."
	phrases = ["Gouts of flame flow from all mouths."]
	hp = 90
	mp = 45
	spells = ["insinerate"]
	attack = 95
	defense = 86
	gold = 250
	exp = 70
	actions = ["a", "m", "s"]
	noflee = "no"
	weakness = ["w"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "magic"
	drop = "yes"
	dropitem = "yorkshiretea"
	droptype = "items"

class deathspiraldragon:
	name = "Death Spiral Dragon"
	desc = "An ancient and horrible dragon covered in toxic curved horns."
	phrases = ["The dragon emits a violent shiver, showering you in poisoned horns.", "*SNAP* The dragon gives you a mighty chomp."]
	hp = 100
	mp = 60
	spells = ["fullheal"]
	attack = 100
	defense = 90
	gold = 300
	exp = 100
	actions = ["a", "m"]
	noflee = "no"
	weakness = ["n"]
	incapatt = ""
	incapsuc = ""
	lazymsg = ""
	stealtype = "none"
	drop = "no"
	dropitem = ""
	droptype = ""

class mourningbelle:
	name = "Mourning Belle"
	desc = "Lost spirit of a tortured funeral priestess, fated to haunt the lands forever."
	phrases = ["Mourning Belle shrieks a haunted cry."]
	hp = 75
	mp = 28
	spells = ["Pyre"]
	attack = 53
	defense = 76
	gold = 150
	exp = 88
	actions = ["a", "m", "i", "n", "m", "i"]
	noflee = "yes"
	weakness = ["w"]
	incapatt = "screams a tortured cry."
	incapsuc = "You are frozen in fear, unable to move."
	lazymsg = "Sings a mournful dirge and cries, too preoccupied to attack."
	stealtype = "none"
	drop = "no"
	dropitem = ""
