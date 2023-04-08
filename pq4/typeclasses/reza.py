from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn


class chatreza(default_cmds.MuxCommand):
	key = "talk reza"
	aliases = ["Talk Reza", "Talk reza", "talk Reza" ]
	auto_help = True
	def endconvo():
		self.caller.msg("|/|mReza|n says: Stop back again! Keep an eye open for materials!")
		return
	def func(self):
		stuff = []
		colors = []
	#Converstaion
		#Check for needed items
		for i in self.caller.contents:
			stuff.append(i.key)
		if all(i in stuff for i in ('Gold Bar', 'Sea Shell')):
			self.caller.msg("|/|mReza|n says: Oh, you've got the precious materials!")
			for i in self.caller.contents:
				if i.db.glasscolor:
					colors.append(i.db.glasscolor.title())
			if colors == []:
				self.caller.msg("|/|mReza|n says: You know, if you had some colored glass I could make you some of my famous flowers. It's not too hard to find, just look around town, there's a merchant that sells it here at the market but the prices are absurd. You can probably get a better deal straight from the glass makers in Glass Alley.")
				self.caller.msg("|/|mReza|n says: Stop back again! Keep an eye open for materials!")
				return
			else:
				coloroptions = ', '.join([i for i in colors])
				answer = yield("|mReza|n says: And you've got some colored glass. Would you like me to make you a flower?|/|gY|nes, |gN|no")
				if answer.lower() in ["yes", "y"]:
					coloranswer = yield("|/|mReza|n says: Which color would you like to use? You have %s." % (coloroptions))
					if coloranswer.title() not in colors:
						self.caller.msg("|/|mReza|n says: It doesn't look like you've got any %s colored glass. Maybe you could go get some if that's what you want." % (coloranswer.title()))
						endconvo()
						return
					else:
						self.caller.msg("|/|mReza|n says: You got it! One %s glass flower coming up!" % (coloranswer.title()))
					#remove the needed items
						goldtarget = self.caller.search('Gold Bar', candidates=self.caller.contents, quiet=True)
						if goldtarget:
							goldtarget[0].db.qty -= 1
							if goldtarget[0].db.qty <= 0:
								goldtarget[0].delete()
						shelltarget = self.caller.search('Sea Shell', candidates=self.caller.contents, quiet=True)
						if shelltarget:
							shelltarget[0].db.qty -= 1
							if shelltarget[0].db.qty <= 0:
								shelltarget[0].delete()
						glasstype = coloranswer.title() + " Glass"
						glasstarget = self.caller.search(glasstype, candidates=self.caller.contents, quiet=True)
						if glasstarget:
							glasstarget[0].db.qty -= 1
							if glasstarget[0].db.qty <= 0:
								glasstarget[0].delete()
					#create and put the flower in the inventory or increment quantity
						flowertype = coloranswer.title() + " Flower"
						flowertarget = self.caller.search(flowertype, candidates=self.caller.contents, quiet=True)
						if not flowertarget:
							flwr_proto = {
								"key": flowertype,
								"name": "%s" % (flowertype),
								"typeclass": "typeclasses.objects.glassflower",
								"desc": "A beautiful %s glass and gold flower" % (coloranswer.title()),
								"color": "%s" % (coloranswer.title()),
								"qty": 1,
								"location": self.caller
								}
							spawn(flwr_proto)
						else:
							flowertarget[0].db.qty += 1
						self.caller.msg("*Clink Clink* *WHoosh...WHOOOSH* *Ting-Ting-Ting*")
						yield 2
						self.caller.msg("|/|mReza|n says: Here you are, one %s flower! Enjoy!!" % (coloranswer.title()))
						return
				else:
					endconvo()
					return
		self.caller.msg("|/|mReza|n says: Hello, welcome to my shop. I see you're admiring some of my work. Well let me tell you, it's not easy getting the materials. Well, yes the glass is plentiful, but the metals needed to bond the parts is hard to come by. You see, the particular gold needed has to be extremely pure, only place I know of to get it is from a monster in the Kharro Desert, and they're very rare. But anyone can weld together glass and gold. You wanna hear a secret? I use the coating from inside Sea Shells to give my work some extra oomph. Only problem is ever since Papricallah blocked the mountain pass, getting Sea Shells has been really difficult. The ones here just don't have the same color to them. If you find yourself way over west by the Gadoz Beach, keep an eye out for a Fish-n-Clips, they're pretty common to find and they seem to carry them.")
		return


class RezaCmdSet(CmdSet):
	key = "RezaCmdSet"
	def at_cmdset_creation(self):
		self.add(chatreza())

class reza(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "."
		self.cmdset.add_default(RezaCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")