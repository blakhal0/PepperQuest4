from evennia import default_cmds, CmdSet, search_object, search_tag
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn


class chatkuloar(default_cmds.MuxCommand):
	key = "talk prisoner"
	aliases = ["Talk Prisoner", "Talk prisoner", "talk Prisoner", "Talk Kuloar", "Talk kuloar", "talk Kuloar", "talk kuloar"]
	auto_help = False
	def func(self):
	#first meet in cell
		if not self.caller.tags.get("thekingisdead") and self.caller.location.key == "Cell":
			self.caller.msg("|/|mPrisoner|n says: Well hi there. Real glad to meet you, and real glad you kept your word to let me out. Get thrown in here for being a peasant? Yeah, me too. The King and Queen were in their carriage going through town and I didn't see them coming. They saw me through their window and next thing I know, bam!, thrown in here because I happened to be in their eyesight.")
			self.caller.msg("|m%s|n says: They've got a real issue with regular folk eh?" % (self.caller.key))
			self.caller.msg("|mPrisoner|n says: Heh, yeah you could say that. All they do is tax us, beat us, take our food and produce, tax us some more. This place could do with a good revolt.")
			self.caller.msg("|mPrisoner|n says: .... yeah, yeah it could use a good revolt.")
			self.caller.msg("|mPrisoner|n says: Let's get the hell outta here.")
			self.caller.msg("The prisoner opens the door and motions for you to follow into the hallway.")
			return
	#second meet in prison hallway
		elif not self.caller.tags.get("thekingisdead") and self.caller.location.key == "Paipri Prison":
			self.caller.msg("|/|mPrisoner|n says: Oh yeah, my name is Kuloar Slove. Sorry, I've been down here quite a while, my manners are a bit rusty.")
			self.caller.msg("You shake hands and introduce yourself.")
			self.caller.msg("|mKuloar Slove|n says: Nice to meet you %s." % (self.caller.key))
			self.caller.msg("Kuloar walks the length of the prison hallway in both directions.")
			self.caller.msg("|mKuloar Slove|n says: Welp, our options are pretty limited. Looks like we could try and go right out the front door, into the castle and try to sneak out. I gotta say, I don't like the idea of breaking out of the prison and into where all the guards with their very sharp swords are. Not to mention they'd be able to smell us just as easy as see us.")
			self.caller.msg("|mKuloar Slove|n says: Or, we can try going down through that grate into the ol perfume river there. It's gotta end up somewhere. Damned dark down there though, wouldn't be able to see your hand in front of your face. Pretty easy to get lost.")
			self.caller.msg("|mKuloar Slove|n says: You look pretty trustworthy, whatever you decide I'll be right there with you.")
			return
	#third meeting in pub to organize the revolt
		elif not self.caller.tags.get("thekingisdead") and self.caller.tags.get("folkhero") and self.caller.location.key == "The Far Lantern Pub":
			if self.caller.search("Riot Sheet", candidates=self.caller.contents, quiet=True) and self.caller.search("Pitch Fork", candidates=self.caller.contents, quiet=True):
				target = self.caller.search("Riot Sheet", candidates=self.caller.contents, quiet=True)
			#start peasant riot
				if target[0].db.count == 5:
					self.caller.msg("|/|mKuloar Slove|n says: Well, looks like we've got enough volunteers for an angry mob! Let's get this party started!!")
					self.caller.msg("Kuloar stands up and clears his throat.")
					self.caller.msg("|mKuloar Slove|n says: My Fellow Peasants, it's time we stand up to these menacing monarchs!")
					self.caller.msg("|mPeasant|n says: THEY TOOK OUR CHICKENS!!!")
					self.caller.msg("|mAngry Mob|n: *rabble-rabble-rabble-rabble*!!")
					self.caller.msg("|mPeasant|n says: THEY TOOK OUR PINBALL MACHINES!!!")
					self.caller.msg("|mAngry Mob|n: *RABBLE-rabble-RABBLE-rabble*!!")
					self.caller.msg("|mPeasant|n says: I WISH SOMEONE WOULD INVENT THE GUN!!")
					self.caller.msg("|mAngry Mob|n: *rabble...rabble...confusion*!!")
					self.caller.msg("|mPeasant|n says: I LOVE LAMP!!")
					self.caller.msg("|mAngry Mob|n: *RABBLE-RABBLE-RABBLE-RABBLE*!!")
					self.caller.msg("You thrust your pitchfork into the air and the angry mob of peasants goes wild, spilling into the streets, quickly overwhelming the guards, and storming the castle.")
					self.caller.msg("The King and Queen are deposed, and the peasants elect Kuloar as their new king.")
					self.caller.tags.add("thekingisdead")
					self.caller.tags.remove("folkhero")
					for i in self.caller.contents:
						if i.key == "Riot Sheet":
							i.delete()
					results = search_object("#7657")
					self.caller.move_to(results[0], quiet=True, move_hooks=False)
					return
			#Get more signatures
				else:
					self.caller.msg("|/|mKuloar Slove|n says: Well, you've got the signup sheet, you've got %d signatures, you're going to need some more. We need 5 total." % (target[0].db.count))
					self.caller.msg("|mKuloar Slove|n says: What are you waiting for? Go recruit some peasants!")
					return
		#Peasant revolt signup
			elif self.caller.search("Pitch Fork", candidates=self.caller.contents, quiet=True) and not self.caller.search("Riot Sheet", candidates=self.caller.contents, quiet=True):
				self.caller.msg("|/|mKuloar Slove|n says: Good to see you again. I see you have the quintessential gear needed for a peasant revolt, the Pitch Fork.")
				self.caller.msg("|mKuloar Slove|n says: Now we need peasants. Luckily we have an entire city of angry overtaxed peasants. I've been all over the city laying the groundwork, sewing the seeds of revolt.")
				self.caller.msg("|mKuloar Slove|n says: I need you to go sort out who's up for joining.")
				self.caller.msg("|mKuloar Slove|n says: Keep in mind the King and Queen do still hold loyalty with some, you can't go about asking just anyone if they want to join a revolt to overthrow the monarchy. That's the fast path to becoming a head on a spike.")
				self.caller.msg("|mKuloar Slove|n says: Take this signup sheet, and for goodness sake don't go flashing it about. Size people up, see if they seem to have a grudge with the current administration. I have a feeling they'll know exactly what you're there for when you talk to them if they're interested.")
				riotsheet_proto = {
				"key": "Riot Sheet",
				"typeclass": "typeclasses.books.riotsheet",
				"location": self.caller
				}
				spawn(riotsheet_proto)
				return
		#essential supplies
			else:
				self.caller.msg("|/|mKuloar Slove|n says: Good to see you again. I owe my freedom to you. But more importantly I owe freedom to this city. We're going to start a peasant revolt!")
				self.caller.msg("|mKuloar Slove|n says: Now, keep that under your hat, just because we got out of prison once don't think that we can just go walking out of there any old time we want. They might just hang us next time and save the time and trouble of having more prisoners.")
				self.caller.msg("|mKuloar Slove|n says: Alright, first things first, we're going to need to get some basic necessities, namely a pitchfork. I'm told the blacksmith sells them.")
				self.caller.msg("|mKuloar Slove|n says: While you're doing that I'll start laying the ground work needed.")
				self.caller.msg("|mKuloar Slove|n says: Keep your head down! And down with the monarchy!")
				return
	#last meeting in throne room Kuloar Slove is King of Paipri
		elif self.caller.tags.get("thekingisdead") and self.caller.location.key == "Throne Room":
			self.caller.msg("|/|mKuloar Slove|n says: Well well well, %s! It's so good to see you again!" % (self.caller.key))
			self.caller.msg("|mKuloar Slove|n says: Former King and Queen Pancha were hording all the tax money in the treasury.")
			self.caller.msg("|mKuloar Slove|n says: We've started re-distributing the money back to the people and the city seems to be responding well.")
			self.caller.msg("|mKuloar Slove|n says: Turns out the city was really wealthy before they started taxing everything anyways, we didn't even have to sell anything from in the castle!")
			self.caller.msg("|mKuloar Slove|n says: What? Tormey? Why on earth would you want to go there? Well who am I to tell someone where they want to go. I'll send out a message to all the guards that you're allowed to go wherever you want.")
			self.caller.msg("|mKuloar Slove|n says: Until we meet again friend!")
			return
		else:
			self.caller.msg("There is no one here by that name to talk to.")
			return

class KuloarCmdSet(CmdSet):
	key = "KuloarCmdSet"
	def at_cmdset_creation(self):
		self.add(chatkuloar())

class kuloar(DefaultObject):
	def at_object_creation(self):
		self.db.prisonerdesc = "Covered in filth, the prisoner appears to be covered in white lines where the filth has dried and cracked off in the creases and crevices of his face."
		self.db.peasantdesc = "Kuloar sits in a dark corner of the inn, talking quietly to some fellow peasants."
		self.db.kingdesc = "King Kuloar sits on the throne attending to the many citizens that have come to discuss issues of importance to their area of the country."
		self.db.tagname = "thekingisdead"
		self.db.tagtwoname = "folkhero"
		self.tags.add("specialnpc")
		self.cmdset.add_default(KuloarCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/Hey HEY!! None of that now!"
	def return_appearance(self, looker):
		if not looker:
			return ""
		desc = str()
		if looker.tags.get(self.db.tagname):
			desc = self.db.kingdesc
		elif looker.tags.get(self.db.tagtwoname):
			desc = self.db.peasantdesc
		else:
			desc = self.db.prisonerdesc
		return desc