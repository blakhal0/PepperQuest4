
#travel
class travel:
	name = "Travel"
	cost = 5
	price = 20
	base = 0
	group = "travel"
	kind = "util"
	phrase = ""

#heal
class heal:
	name = "Heal"
	price = 50
	cost = 2
	base = 4
	group = "heal"
	kind = "self"
	phrase = "An aura of glittering spice surrounds you, slightly healing your wounds."
	enemyphrase = "The enemy chants a healing spell and recovers a little health."

class moreheal:
	name = "Moreheal"
	price = 200
	cost = 4
	base = 12
	group = "heal"
	kind = "self"
	phrase = "A wave of spice flows over you, moderately healing your wounds."
	enemyphrase = "The enemy chants a healing spell, and recovers much health."

class fullheal:
	name = "Fullheal"
	price = 1000
	cost = 16
	base = 100000
	group = "heal"
	kind = "self"
	phrase = "You chant the ancient words. Spice rages through you, healing all wounds."
	enemyphrase = "The enemy chants a healing spell, fully restoring its health."

class treason:
	name = "Treason"
	price = 400
	cost = 4
	base = 15
	group = "heal"
	kind = "enemy"
	phrase = "You render succor to the enemy, healing their wounds."
	enemyphrase = "The enemy takes pity upon you. Saying a small prayer they heal your wounds."

#electric
class spark:
	name = "Spark"
	price = 50
	cost = 2
	base = 4
	group = "aggressive"
	kind = "e"
	phrase = "The air tingles, the enemy receives a light shock."
	enemyphrase = "The air tingles, you receive a light shock."

class arc:
	name = "arc"
	price = 100
	cost = 4
	base = 8
	group = "aggressive"
	kind = "e"
	phrase = "A thin streak of lightning hits the enemy."
	enemyphrase = "A thin streak of lightning hits you."

class volt:
	name = "Volt"
	price = 500
	cost = 8
	base = 16
	group = "aggressive"
	kind = "e"
	phrase = "Forks of blue lightning strike the enemy."
	enemyphrase = "Forks of blue lightning strike you."

class highboltage:
	name = "HighBoltage"
	price = 1000
	cost = 12
	base = 32
	group = "aggressive"
	kind = "e"
	phrase = "You stomp your foot and point a finger to the sky. Torrents of lightning falls upon the enemy from the skies."
	enemyphrase = "Torrents of lightning falls upon you from the skies."

class raijin:
#Legendary
	name = "Raijin"
	price = 20000
	cost = 20
	base = 64
	group = "aggressive"
	kind = "e"
	phrase = "Lightning crashes as the earth quakes to a wild drumbeat, the thunder god answers your prayer."
	enemyphrase = ""

#fire
class flicker:
	name = "Flicker"
	price = 50
	cost = 2
	base = 4
	group = "aggressive"
	kind = "f"
	phrase = "A small fireball shoots forth and singes the enemy."
	enemyphrase = "A small fireball shoots forth and singes your eyebrows."

class furnace:
	name = "furnace"
	price = 100
	cost = 3
	base = 8
	group = "aggressive"
	kind = "f"
	phrase = "A large flame erupts from the ground, scorching the enemy."
	enemyphrase = "A large flame erupts from the ground, scorching you badly."

class charbq:
	name = "CharBQ"
	price = 500
	cost = 6
	base = 16
	group = "aggressive"
	kind = "f"
	phrase = "A massive fireball blasts the enemy, mmmm, bar-b-que."
	enemyphrase = "A massive fireball blasts you. Is something cooking?"

class insinerate:
	name = "InSinerate"
	price = 1000
	cost = 12
	base = 32
	group = "aggressive"
	kind = "f"
	phrase = "A riot of hellfire surrounds the enemy, burning and suffocating."
	enemyphrase = "A riot of hellfire surrounds you, burning and suffocating."

class pyrettablaze:
#Legendary
	name = "PyrettaBlaze"
	price = 20000
	cost = 20
	base = 64
	group = "aggressive"
	kind = "f"
	phrase = "Distant bells toll summoning a servant of the pyre demon, Pyretta. Napalm tears cover the enemy, bursting to flame as it wails in agony."
	enemyphrase = ""

class dragonblaze:
#Legendary
	name = "DragonBlaze"
	price = 20000
	cost = 20
	base = 70
	group = "aggressive"
	kind = "f"
	phrase = "You bite the inside of your cheek, the blood begins to seep into your mouth as you chomp a pepper. Inhaling a large breath, the blood and pepper ignite as you roar dragon fire."
	enemyphrase = "Lord Dragon chomps a pepper. Inhaling a large breath, they roar dragon fire."

#aqua
class sprinkle:
	name = "Sprinkle"
	price = 50
	cost = 2
	base = 4
	group = "aggressive"
	kind = "a"
	phrase = "You spit some water in the enemy's face, mildly annoying them."
	enemyphrase = "The enemy spits in your face, mildly annoying you."

class aquaduck:
	name = "AquaDuck"
	price = 100
	cost = 4
	base = 8
	group = "aggressive"
	kind = "a"
	phrase = "A glob of water forms into a duck, chasing the enemy biting them in the butt."
	enemyphrase = "A glob of water forms into a duck, chasing you and biting your butt."

class drown:
	name = "Drown"
	price = 500
	cost = 8
	base = 16
	group = "aggressive"
	kind = "a"
	phrase = "The enemy struggles for air as a cube of water surrounds them."
	enemyphrase = "You struggle and claw for air as a cube of water surrounds you."

class frostflower:
	name = "FrostFlower"
	price = 1000
	cost = 12
	base = 32
	group = "aggressive"
	kind = "a"
	phrase = "Frost flowers bloom from the enemy as their blood freezes."
	enemyphrase = "You are hit with a spine chilling spell and freezing you to the bone."

class khionekiss:
#Legendary
	name = "KhioneKiss"
	price = 20000
	cost = 20
	base = 64
	group = "aggressive"
	kind = "a"
	phrase = "A blizzard howls, freezing the enemy solid. Khione kisses the enemy, shattering their frozen form."
	enemyphrase = "You are hit with a titanic iceberg."

#wind
class gust:
	name = "Gust"
	price = 50
	cost = 2
	base = 4
	group = "aggressive"
	kind = "w"
	phrase = "A wild gust beats against the enemy."
	enemyphrase = "A cold wind beats against you."

class whoosh:
	name = "Whoosh"
	price = 100
	cost = 4
	base = 8
	group = "aggressive"
	kind = "w"
	phrase = "A battering wind threatens to blow the enemy away."
	enemyphrase = "A battering wind threatens to blow you away."

class swoosh:
	name = "Swoosh"
	price = 500
	cost = 8
	base = 16
	group = "aggressive"
	kind = "w"
	phrase = "You summon a cutting wind to attack the enemy."
	enemyphrase = "You are attacked by cutting winds."

class galeforce:
	name = "GaleForce"
	price = 1000
	cost = 12
	base = 32
	group = "aggressive"
	kind = "w"
	phrase = "A massive wind attempts to send the enemy to the afterworld."
	enemyphrase = "A massive wind attempts to send you to the afterworld."

class horrorcane:
#Legendary
	name = "Horrorcane"
	price = 20000
	cost = 20
	base = 64
	group = "aggressive"
	kind = "w"
	phrase = "Demonic winds swirl and whirl tearing at the enemy. Fazuzu answers your prayer."
	enemyphrase = "Demonic winds swirl and whirl tearing at you."

#light
class stolenheart:
	name = "StolenHeart"
	price = 50
	cost = 15
	base = 20
	group = "aggressive"
	kind = "l"
	phrase = "You bat your eyes at the enemy and make a heart shape with your hands. Deftly you employ your thieves skills stealing your enemy's heart and leaving damage in its place."
	enemyphrase = ""

class holyaura:
	name = "HolyAura"
	price = 50
	cost = 9
	base = 20
	group = "aggressive"
	kind = "l"
	phrase = "An ethereal light emanates from you, burning the enemy."
	enemyphrase = ""

class hecatomb:
	name = "Hecatomb"
	price = 1000
	cost = 5
	base = 1000
	group = "aggressive"
	kind = "l"
	phrase = "You open a vein, in hopes that the light shines upon you. 'Half my life, for all of yours!'"
	enemyphrase = ""

#dark
class graverobber:
	name = "GraveRobber"
	price = 50
	cost = 9
	base = 20
	group = "aggressive"
	kind = "d"
	phrase = ""
	enemyphrase = ""

class hurt:
	name = "Hurt"
	price = 50
	cost = 9
	base = 20
	group = "aggressive"
	kind = "d"
	phrase = "Searing pain wracks the enemy, wrenching their form into unnatural shapes."
	enemyphrase = "Searing pain wracks you, wrenching your body into unnatural shapes."

class death:
	name = "Death"
	price = 1000
	cost = 30
	base = 1000
	group = "aggressive"
	kind = "d"
	phrase = "You summon a demon of the underworld in an attempt to drag the enemy to the afterworld."
	enemyphrase = "The enemy summons a demon of the underworld in an attempt to drag you to the afterworld."

#enemyspecific
class sugarandspice:
	name = "Sugar and Spice"
	price = 20
	cost = 10
	base = 56
	group = "aggressive"
	kind = "f"
	phrase = ""
	enemyphrase = "Pyretta throws napalm covered candy peppers at you. They stick. She snaps her fingers igniting the napalm and melting the candy creating a tacky stretchy hellfire charring your flesh."

class requiemvampa:
	name = "Requiem Vampa"
	price = 20
	cost = 10
	base = 75
	group = "aggressive"
	kind = "f"
	phrase = ""
	enemyphrase = "Mournful screams give way to funeral bells amidst wordless chanting... a hauntingly beautiful song emerges in the dissonance. The blood from your wounds flickers and ignites. Your screams merge into the song."

class pyre:
	name = "Pyre"
	price = 20
	cost = 4
	base = 32
	group = "aggressive"
	kind = "f"
	phrase = ""
	enemyphrase = "The enemy blasts you with funeral fire!"

class bat:
	name = "Bat"
	price = 13
	cost = 9
	base = 20
	group = "aggressive"
	kind = "w"
	phrase = "Ba-AAAAAAAAAT!!!!|/A flurry of bats swarms the enemy biting and scratching."
	enemyphrase = "'Ba-AAAAAAT!!'|/Laszlo transforms into a bat and attacks!"

class emotionaldamage:
	name = "Emotional Damage"
	price = 20
	cost = 4
	base = 12
	group = "aggressive"
	kind = "d"
	phrase = ""
	enemyphrase = "Is THAT the armor your going to wear? Well I guess, if that's the look you're going for.|/EMOTIONAL DAMAGE!!!!"

class frostbite:
	name = "Frost Bite"
	price = 20
	cost = 3
	base = 12
	group = "aggressive"
	kind = "d"
	phrase = ""
	enemyphrase = "An invisible icy maw clamps down on your tender flesh."

class twentyfourkarat:
	name = "Twenty Four Karat"
	price = 20
	cost = 6
	base = 18
	group = "aggressive"
	kind = "d"
	phrase = ""
	enemyphrase = "Boiling gold falls from the sky, searing your skin."

class honkoffivehells:
	name = "Honk of Five Hells"
	price = 20
	cost = 12
	base = 36
	group = "aggressive"
	kind = "d"
	phrase = ""
	enemyphrase = "Honkiamat draws back all five heads and releases an earth trembling honk, you are hit with unimaginable pain."

class timewarp:
	name = "Timewarp"
	price = 20
	cost = 12
	base = 60
	group = "aggressive"
	kind = "d"
	phrase = ""
	enemyphrase = "Malashai turns an hourglass in his hand, time freezes. You are suddenly wracked with pain as a series of attacks hit you all at once."

class temporalchaos:
	name = "Temporal Chaos"
	price = 20
	cost = 10
	base = 60
	group = "aggressive"
	kind = "d"
	phrase = ""
	enemyphrase = "Pendrin summons the immense power of time, causing a localized temporal collapse."

class titansfury:
#Legendary
	name = "Titans Fury"
	price = 20000
	cost = 20
	base = 64
	group = "aggressive"
	kind = "a"
	phrase = "."
	enemyphrase = "The Titan reaches raises an arm to the sky. An asteroid plummets towards you and impacts."

class sirenslament:
	name = "Siren's Lament"
	price = 0
	cost = 12
	base = 60
	group = "aggressive"
	kind = "d"
	enemyphrase = "The demon minstrel sings a hauntingly beautiful melody that enthralls you, causing you pain."

class sirenssong:
	name = "Siren's Song"
	price = 0
	cost = 4
	base = 40
	group = "aggressive"
	kind = "d"
	enemyphrase = "The Siren sings a mesmerizing song that leaves you lost in memories past, wracking you with the pain of loss."

class needle:
	name = "10000 Needle Attack"
	price = 0
	cost = 10
	base = 100
	group = "aggressive"
	kind = "d"
	enemyphrase = "Cactuar stiffens oddly, then shakes violently! 10000 Needle Attack!!!!"

class harmonicchains:
	name = "Harmonic Chains"
	price = 0
	cost = 12
	base = 60
	group = "aggressive"
	kind = "d"
	enemyphrase = "Ethereal nooses of sound ensnare you and resonate with the enemy's power, causing mental anguish and disarray."

class rhythmofruin:
	name = "Rhythm of Ruin"
	price = 0
	cost = 12
	base = 60
	group = "aggressive"
	kind = "d"
	enemyphrase = "The demon minstrel taps into the primal beat of music, unleashing a rhythmic assault that pulses through the battlefield."

class dazzlingcolors:
	name = "Dazzling Colors"
	price = 0
	cost = 12
	base = 60
	group = "aggressive"
	kind = "d"
	enemyphrase = "A multitude of colored beams of light emit from the creature, reflecting off the mirrored walls striking you, burning you."