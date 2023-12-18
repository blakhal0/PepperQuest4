from evennia import default_cmds, InterruptCommand, search_object, search_tag, utils, gametime
import random
from random import randint
from evennia.utils import interactive
from evennia.utils.logger import log_file
from evennia.prototypes.spawner import spawn
from evennia.utils.evmenu import EvMenu
import string
import typeclasses.beastiary as beastiary
import typeclasses.zones as zones
import typeclasses.battlespells as magic
import typeclasses.locations as places
import typeclasses.weapons as weapons
import typeclasses.armor as armor
import typeclasses.items as items
import typeclasses.books as books
import typeclasses.objects as genericobjects

#self.caller.msg(self.caller.dbid) return database ID number

#=============================
#==Admin and Testing Commands=
#=============================

class test(default_cmds.MuxCommand):
	key = "test"
	locks = "cmd:perm(developer)"
	def func(self):
		if not "Finder of the Song" in self.caller.db.accolades:
			self.caller.msg("Accolade not found")
		else:
			self.caller.msg("Accolade found")

class sethp(default_cmds.MuxCommand):
	key = "sethp"
	locks = "cmd:perm(developer)"
	def func(self):
		hp = self.args.strip()
		if not hp.isnumeric():
			self.caller.msg("You can't see it, but I'm giving you a disapproving look.")
			return
		if int(hp) > self.caller.db.maxhp:
			self.caller.msg("Hey now, that's more than your max hp. keep it reasonable.")
			return
		if int(hp) <= 0:
			self.caller.msg("Suicide isn't the answer.")
			return
		self.caller.db.hp = int(hp)
		self.caller.msg("|/|gHP set to %d|n" % int(hp))
		return

class journalentry(default_cmds.MuxCommand):
	key = "addmonster"
	locks = "cmd:perm(developer)"
	def parse(self):
		self.argslist = self.args.split(",")
	def func(self):
		if len(self.argslist) < 2:
			self.caller.msg("Needs 2 arguments: Monstername, Quantity Killed")
			return
		monstername = self.argslist[0]
		monstername = monstername.strip()
		quantitykilled = self.argslist[1]
		quantitykilled = quantitykilled.strip()
		if monstername in self.caller.db.monsterstats.keys():
			self.caller.msg("%s is already in your monster journal." % (monstername))
			return
		else:
			self.caller.db.monsterstats[monstername] = {"killed": int(quantitykilled), "desc": "Generic Description"}
			self.caller.msg("%s added to monster journal." % (monstername))

class removeentry(default_cmds.MuxCommand):
	key = "remmonster"
	locks = "cmd:perm(developer)"
	def parse(self):
		self.monstername = self.args.strip()
	def func(self):
		if not self.monstername in self.caller.db.monsterstats.keys():
			self.caller.msg("%s is not in your monster journal." % (self.monstername))
			return
		else:
			del self.caller.db.monsterstats[self.monstername]
			self.caller.msg("%s removed from monster journal." % (self.monstername))

class addaccolade(default_cmds.MuxCommand):
	key = "addacc"
	locks = "cmd:perm(developer)"
	def parse(self):
		self.accname = self.args.lstrip()
	def func(self):
		if self.accname in self.caller.db.accolades:
			self.caller.msg("Accolade already in Accolades.")
		else:
			self.caller.db.accolades.append(self.accname)
			self.caller.msg("|/Added accolade %s." % (self.accname))
		self.caller.msg(self.caller.db.accolades)
		return

class remaccolade(default_cmds.MuxCommand):
	key = "remacc"
	locks = "cmd:perm(developer)"
	def parse(self):
		self.accname = self.args.lstrip()
	def func(self):
		if self.accname in self.caller.db.accolades:
			self.caller.db.accolades.remove(self.accname)
			self.caller.msg("|/Removed accolade %s." % (self.accname))
		else:
			self.caller.msg("%s not in accolades." % (self.accname))
		self.caller.msg(self.caller.db.accolades)
		return

class showaccolade(default_cmds.MuxCommand):
	key = "shacc"
	locks = "cmd:perm(developer)"
	def func(self):
		self.caller.msg(self.caller.db.accolades)

class popchest(default_cmds.MuxCommand):
	key = "popchest"
	locks = "cmd:perm(developer)"
	def func(self):
		self.caller.db.chests.pop()
		self.caller.msg("You removed the last chest you looted")

class showtag(default_cmds.MuxCommand):
	key = "shtag"
	locks = "cmd:perm(developer)"
	def func(self):
		self.caller.msg("|/|rYou have the following tags:|n")
		self.caller.msg(self.caller.tags)

class givetag(default_cmds.MuxCommand):
	key = "tag"
	locks = "cmd:perm(developer)"
	def parse(self):
		self.tagname = self.args.lstrip()
	def func(self):
		if not self.caller.tags.get(self.tagname):
			self.caller.tags.add(self.tagname)
			self.caller.msg("|rYou've added a tag named %s|n" % (self.tagname))
			return
		else:
			self.caller.msg("|rYou already have a tag named %s|n" % (self.tagname))

class remtag(default_cmds.MuxCommand):
	key = "untag"
	locks = "cmd:perm(developer)"
	def parse(self):
		self.tagname = self.args.lstrip()
	def func(self):
		if self.tagname == "":
			self.caller.msg("Empty tag detected. You're an idiot, this would have removed ALL your tags. Go think about what you almost did.")
			return
		elif self.caller.tags.get(self.tagname):
			self.caller.tags.remove(self.tagname)
			self.caller.msg("|rYou've removed a tag named %s|n" % (self.tagname))
			return
		else:
			self.caller.msg("|rYou don't have a tag named %s|n" % (self.tagname))

class reup(default_cmds.MuxCommand):
	key = "reup"
	locks = "cmd:perm(developer)"
	def func(self):
		self.caller.db.hp = self.caller.db.maxhp
		self.caller.db.mp = self.caller.db.maxmp
		self.caller.msg("Status: HP: %d MP: %d" % (self.caller.db.hp, self.caller.db.mp))


#=============================
#=====Player Commands=========
#=============================
class slowdeath(default_cmds.MuxCommand):
	key = "slowdeath"
	auto_help = False
	def func(self):
		if not self.caller.tags.get("cursedbones"):
			return
		yield 10
		self.caller.tags.remove("cursedbones")
		self.caller.msg("|/|rYou suddenly do not feel well. Your stumble and fall, unable to support yourself, your limbs bend like a wet noodle. YOUR BONES!!! THEY LACK CALCIUM!!! YOU SHOULD HAVE ACCEPTED THE NECROMANCERS OFFER OF DELICIOUS CALCIUM FOR STRONG BONES!!")
		self.caller.msg("|/|rWhat tragic fate, you have died from lack of calcium and bad bones.|n|/You have brought shame to yourself, your bones, and your family. Doot Doot.|n")
		self.caller.db.deathcount += 1
		self.caller.db.hp = int(self.caller.db.maxhp * .5)
		self.caller.db.mp = int(self.caller.db.maxmp * .5)
		self.caller.db.gold -= int(self.caller.db.gold * .3)
		results = search_object(self.caller.db.lastcity)
		self.caller.move_to(results[0], quiet=True, move_hooks=False)
		return

class quests(default_cmds.MuxCommand):
	"""
	Check your ongoing quests.

	Usage:
	Quests

	Shows an overview of status of quests.
	"""
	key = "quests"
	auto_help = True
	def func(self):
		completed = 0
		inprogress = 0
		questdesc = ""
		for i in self.caller.db.quests:
			if self.caller.db.quests[i]['completed'] == "yes":
				completed += 1
			else:
				inprogress += 1
				remainingqty = 0
				if self.caller.db.quests[i]['type'] == "get":
					questdesc += self.caller.db.quests[i]['giver'] + " in " + self.caller.db.quests[i]['location'] + ". Quest type: " + self.caller.db.quests[i]['type'].capitalize() + " " + str(self.caller.db.quests[i]['qty']) + " " + getattr(items, self.caller.db.quests[i]['thingname']).name.title() + "\r\n"
				if self.caller.db.quests[i]['type'] == "kill":
					if getattr(beastiary, self.caller.db.quests[i]['thingname']).name.title() in self.caller.db.monsterstats.keys():
						if int(self.caller.db.quests[i]['qty']) - int(self.caller.db.monsterstats[getattr(beastiary, self.caller.db.quests[i]['thingname']).name.title()]["killed"]) > 0:
							remainingqty = str(int(self.caller.db.quests[i]['qty']) - int(self.caller.db.monsterstats[getattr(beastiary, self.caller.db.quests[i]['thingname']).name.title()]["killed"]))
						else:
							remainingqty = "0"
					else:
						remainingqty = str(self.caller.db.quests[i]['qty'])
					questdesc += self.caller.db.quests[i]['giver'] + " in " + self.caller.db.quests[i]['location'] + ". Quest type: " + self.caller.db.quests[i]['type'].capitalize() + " " + remainingqty + " more " + getattr(beastiary, self.caller.db.quests[i]['thingname']).name.title() + "\r\n"
		self.caller.msg("|/|mQuestella|n says: Hello %s! 'Tis I, Questella, your matron of quests for the hearty adventurer." % (self.caller.key))
		self.caller.msg("|mQuestella|n says: Hummm, yes, let's take a look.")
		self.caller.msg("|mQuestella|n says: You've completed %d quests." % (completed))
		self.caller.msg("|mQuestella|n says: You've got %d quests in progress." % (inprogress))
		if inprogress > 0:
			self.caller.msg("|mQuestella|n says: Here's your ongoing quests:")
			self.caller.msg(questdesc)

class loot(default_cmds.MuxCommand):
	key = "Loot"
	auto_help = False
	def parse(self):
		self.item = self.args.lstrip()
	def func(self):
		if not self.obj.access(self.caller, "view"):
			self.caller.msg("There's no %s to loot." % (self.item))
			return
		target = self.caller.search(self.item)
	#check if the thing exists
		if not target:
			self.caller.msg("|/There's not a %s to loot." % (self.item))
			return
	#Loot NPC's
		if target.tags.get("talkative", category="npc") or target.tags.get("specialnpc"):
			if target.tags.get("soldharanpc", category="talkative"):
				self.caller.msg("|/|rThat's not very nice! And a little gross.|n")
				return
			chance = randint(1,3)
			if chance == 1:
				profitlost = randint(1, int(self.caller.db.gold * .5))
				self.caller.db.gold -= int(profitlost)
				self.caller.msg("|/|m%s|n says: HEY!! What the hell do you think you're doing!!!" % (target.key))
				self.caller.msg("%s starts slapping you around. Flustered, you flee wildly losing %d gold in your escape." % (target.key, int(profitlost)))
				return
			elif chance == 2:
				healthlost = randint(1, self.caller.db.hp)
				self.caller.db.hp -= healthlost
				self.caller.msg("|/|m%s|n says: HEY!! What the hell do you think you're doing!!!" % (target.key))
				weapopts = ["club", "massive sword", "frying pan", "lake trout", "mace", "small knife", "war hammer", "executioners axe", "dull spoon", "sharpened toothbrush"]
				weaponchoice = random.choice(weapopts)
				if int(self.caller.db.hp) == 0:
					self.caller.msg("%s whips out a %s and murders you without remorse." % (target.key, weaponchoice))
					self.caller.msg("|m%s|n says: And that's how we handle filthy little thieves like you! *spits on your corpse*" % (target.key))
					self.caller.msg("|/|rWhat tragic fate, you have been murdered for thievery by %s|n|/You have brought shame to yourself and your family." % (target.key))
					self.caller.db.deathcount += 1
					self.caller.db.hp = int(self.caller.db.maxhp * .5)
					self.caller.db.mp = int(self.caller.db.maxmp * .5)
					self.caller.db.gold -= int(self.caller.db.gold * .3)
					results = search_object(self.caller.db.lastcity)
					self.caller.move_to(results[0], quiet=True, move_hooks=False)
					return
				else:
					self.caller.msg("%s whips out a %s and demonstrates the meaning of violence.|/You lose %d hp." % (target.key, weaponchoice, int(healthlost)))
					return
			elif chance == 3:
				profit = randint(1,100)
				self.caller.db.gold += int(profit)
				self.caller.msg("|/You manage to steal %d gold from %s.|/You greedily stuff it in your pockets and slink off like the filthy, no-good, low-down, thieving scum that you are." % (int(profit), target.key))
				return
	#check if the thing is lootable
		if not target.tags.get("treasurechest"):
			self.caller.msg("|/That's not something you can loot.")
			return
	#check if the chest is locked due to not having tag
		if target.tags.get("tagchest"):
			if not self.caller.tags.get(target.db.lockedtagname):
				self.caller.msg("|/%s" % (target.db.lockedmsg))
				return
		if target.tags.get("nottagchest"):
			if self.caller.tags.get(target.db.lockedtagname):
				self.caller.msg("|/%s" % (target.db.lockedmsg))
				return
	#check if the chest requires the player to have an item in inventory
		if target.tags.get("holdschest"):
			if target.db.holdsitemname not in [obj.key for obj in self.caller.contents]:
				self.caller.msg("|/%s" % (target.db.lockedmsg))
				return
			else:
				self.caller.msg("You use the %s to unlock the chest." % (target.db.holdsitemname))
	#check if the chest requires a monster to have been defeated
		if target.tags.get("defeatedchest"):
			if not target.db.defeatedmonstername in self.caller.db.monsterstats.keys():
				self.caller.msg("|/%s" % (target.db.lockedmsg))
				return
			if not self.caller.db.monsterstats[target.db.defeatedmonstername]["killed"] >= int(target.db.qtydefeated):
				self.caller.msg("|/%s" % (target.db.lockedmsg))
				return
	#Check if you've already looted the chest.
		if not target.db.chestid == "noid":
			if target.db.chestid in self.caller.db.chests:
				self.caller.msg("|/You've already looted that.")
				return
	#Add the chestID to the player
		if not target.db.chestid == "noid":
			self.caller.db.chests.append(target.db.chestid)
	#Get lootchoice
		lootchoice = random.choice(target.db.loottype)
	#Gold loot
		if lootchoice == "gold":
			lootprofit = random.choice(target.db.goldloot)
			#Left hand of Ladrone?
			self.caller.db.gold += int(lootprofit)
			self.caller.msg("|/What luck! You found %d gold!|/You greedily stuff the gold in your pockets." % int(lootprofit))
			return
	#Weapon loot
		elif lootchoice == "weapon":
			lw = random.choice(target.db.weaponloot)
			lootname = getattr(weapons, lw).name
			wt = self.caller.search(lootname, candidates=self.caller.contents, quiet=True)
			if wt:
				lootprofit = getattr(weapons, lw).price
				self.caller.db.gold += int(lootprofit)
				self.caller.msg("|/What luck! You found %d gold!|/You greedily stuff the gold in your pockets." % int(lootprofit))
				return
			else:
				self.caller.msg("|/You found a %s!|/You put the %s in your inventory." % (lootname, lootname))
				sitc = "typeclasses.weapons.%s" % (lw)
				tc_proto = {
				"key": "%s" % (lootname),
				"typeclass": "%s" % (sitc),
				"location": self.caller
				}
				spawn(tc_proto)
				return
	#Armor loot
		elif lootchoice == "armor":
			lw = random.choice(target.db.armorloot)
			lootname = getattr(armor, lw).name
			wt = self.caller.search(lootname, candidates=self.caller.contents, quiet=True)
			if wt:
				lootprofit = getattr(armor, lw).price
				self.caller.db.gold += int(lootprofit)
				self.caller.msg("|/What luck! You found %d gold!|/You greedily stuff the gold in your pockets." % int(lootprofit))
				return
			else:
				self.caller.msg("|/You found a %s!|/You put the %s in your inventory." % (lootname, lootname))
				sitc = "typeclasses.armor.%s" % (lw)
				tc_proto = {
				"key": "%s" % (lootname),
				"typeclass": "%s" % (sitc),
				"location": self.caller
				}
				spawn(tc_proto)
				return
	#Item loot
		elif lootchoice == "item":
			lw = random.choice(target.db.itemloot)
			lootname = getattr(items, lw).name
			self.caller.msg("|/You found a %s!|/You add the %s to your inventory." % (lootname, lootname))
			wt = self.caller.search(lootname, candidates=self.caller.contents, quiet=True)
			if not wt:
				sitc = "typeclasses.items.%s" % (lw)
				tc_proto = {
				"key": "%s" % (lootname),
				"typeclass": "%s" % (sitc),
				"qty": 1,
				"location": self.caller
				}
				spawn(tc_proto)
				return
			else:
				wt[0].db.qty += 1
				return
	#Generic Item loot
		elif lootchoice == "genericitem":
			lw = random.choice(target.db.genericitem)
			lootname = getattr(genericobjects, lw).name
			self.caller.msg("|/You found a %s!|/You add the %s to your inventory." % (lootname, lootname))
			sitc = "typeclasses.objects.%s" % (lw)
			tc_proto = {
			"key": "%s" % (lootname),
			"typeclass": "%s" % (sitc),
			"location": self.caller
			}
			spawn(tc_proto)
			return
	#Book loot
		elif lootchoice == "book":
			lw = random.choice(target.db.bookloot)
			lootname = getattr(books, lw).name
			self.caller.msg("|/You found a %s!|/You add the %s to your inventory." % (lootname, lootname))
			sitc = "typeclasses.books.%s" % (lw)
			tc_proto = {
			"key": "%s" % (lootname),
			"typeclass": "%s" % (sitc),
			"location": self.caller
			}
			spawn(tc_proto)
			return
	#Monster Fight
		elif lootchoice == "monster":
			self.caller.msg("|/|rOH NO!!!! It was actually a monster!!!!|n")
			self.caller.tags.add("letsfight")
			self.caller.execute_cmd('fight')
			return
		else:
			self.caller.msg("Hal0 messed up the loottype, tell him to fix it.")
			return

class mug(default_cmds.MuxCommand):
	key = "mug"
	auto_help = False
	def parse(self):
		self.item = self.args.lstrip()
	def func(self):
		if not self.caller.tags.get("mugger"):
			self.caller.msg("Command 'mug' is not available. Type 'help' for help.")
			return
		target = self.caller.search(self.item, quiet=True)
		if not target:
			self.caller.msg("|/There's no %s to mug." % (self.item))
			return
		guard = self.caller.search("Guard", quiet=True)
		if guard:
			self.caller.msg("|/As you go to make your move you suddenly feel an iron grip on your collar.")
			self.caller.msg("|mGuard|n says: I got you now you little thief!")
			goldlost = int(self.caller.db.gold * .15)
			if goldlost > 0:
				self.caller.msg("The Guard throws you on the ground and rummages around in your pockets, relieving you of %d gold." % (goldlost))
				self.caller.db.gold -= goldlost
			lifelost = int(self.caller.db.hp * .15)
			if lifelost > 0:
				self.caller.msg("The Guard hollers out a call, two other guards show up and proceed to beat the crap out of you. You lose %d hp." % (lifelost))
				self.caller.db.hp -= lifelost
				if self.caller.db.hp == 0:
					self.caller.msg("|/|rWhat tragic fate, you were 'accidentally' beaten to death by the guards, who received a two week paid leave, and no further repercussions.|n|/You have brought shame to yourself and your family.")
					self.caller.db.deathcount += 1
					self.caller.db.hp = int(self.caller.db.maxhp * .5)
					self.caller.db.mp = int(self.caller.db.maxmp * .5)
					self.caller.db.gold -= int(self.caller.db.gold * .2)
					results = search_object(self.caller.db.lastcity)
					self.caller.move_to(results[0], quiet=True, move_hooks=False)
					return
		elif target[0].tags.get("talkative", category="npc") or target[0].tags.get("specialnpc"):
			if target[0].tags.get("mugable"):
				clothestarget = self.caller.search("Fancy Clothes", candidates=self.caller.contents, quiet=True)
				if clothestarget:
					self.caller.msg("You've already got a set of Fancy Clothes, maybe you want to try to |cEquip|n them.")
					return
				else:
					self.caller.msg("|/You grab %s and hustle them into an out of the way location. Yes, these are some very fancy clothes indeed and will do nicely. You proceed to strip them down to their small clothes and make off with your new wardrobe." % (target[0].key))
					fc_proto = {
					"key": "Fancy Clothes",
					"typeclass": "typeclasses.armor.fancyclothes",
					"location": self.caller
					}
					spawn(fc_proto)
					return
			elif target[0].tags.get("thief", category="talkative"):
					self.caller.msg("|/|m%s|n says: Hey, what the hell? A little professional courtesy yeah? Yeesh. Can't trust anyone around here." % (target[0].key))
					return
			else:
				self.caller.msg("|/You grab %s and hustle them into an out of the way location. You search them from head to toe, but there's nothing worth taking." % (target[0].key))
				return
		else:
			self.caller.msg("|/Oh you better hope none of the other thieves find out you're trying to mug inanimate objects. You'll get judged about that.")
			return

class read(default_cmds.MuxCommand):
	"""
	Read books and stuff

	Usage:
	Read (object) i.e. Read Tutorial

	Used to read books, signs, etc. Provides more info than just Look.
	"""
	key = "Read"
	def parse(self):
		self.item = self.args.lstrip()
	def func(self):
		bookshelves = search_tag("bookshelf").filter(db_location=self.caller.location)
		target = self.caller.search(self.item, quiet=True)
		if not target:
			if bookshelves:
				bookshelf = bookshelves[0]
				target = self.caller.search(self.item, candidates=self.caller.location.contents + bookshelf.contents)
		else:
			target = target[0]
		if not target:
			self.caller.msg("There's not a %s here to read." % (self.item))
			return
		if not target.tags.get("readable", category="isreadable"):
			self.caller.msg("This item can't be read, just Look at it")
			return
		#monsterjournal
		if target.tags.get("monsterjournal"):
			if not self.caller.db.monsterstats:
				self.caller.msg("You have not defeated any monsters yet. Get out there and show them what's what!!")
				return
			monlist = ""
			deadmonsters = 0
			unique = 0
			for i in self.caller.db.monsterstats.keys():
				unique += 1
				monlist = monlist + "|m" + i + "|n Defeated: " + str(self.caller.db.monsterstats[i]['killed']) + ". " + "Desc: " + self.caller.db.monsterstats[i]['desc'] + "|/"
				deadmonsters += self.caller.db.monsterstats[i]['killed']
			self.caller.msg("|/You've defeated %d unique monsters and a total of %d monsters." % (unique, deadmonsters))
			self.caller.msg(monlist)
			return
		elif target.tags.get("spellbook", category="isreadable"):
			if not target.db.spell in self.caller.db.battlespells:
				self.caller.msg("|/|g%s|n|/ |/%s" % (target.key, target.db.story))
				self.caller.msg("|/An arcane mist surrounds you! The book begins to melt, runes merging into your skin, you learn the %s spell!" % (target.db.spelldisplay))
				self.caller.db.battlespells.append(target.db.spell)
			else:
				self.caller.msg("|/|g%s|n|/ |/%s" % (target.key, target.db.story))
				self.caller.msg("|/You already know the spell contained in this book. The book bursts into flame and disintegrates.")
			target.delete()
		#regularbook
		elif target.tags.get("single", category="isreadable"):
			self.desc = target.db.story
			self.caller.msg("|/|g%s|n|/ |/%s" % (target.key, self.desc))
			return
		else:
			return

class useitem(default_cmds.MuxCommand):
	key = "item"
	def func(self):
	#Create items list
		itemslist = []
		self.caller.msg("|/|005.|015:|025*|035~|nItems|035~|025*|015:|005.|n")
		for i in self.caller.contents:
			if i.tags.get("item") and i.tags.get("world"):
				self.caller.msg("%s - %d. %s" % (i.db.name, i.db.qty, i.desc))
				itemslist.append(i.key)
			if i.tags.get("item") and i.tags.get("both"):
				self.caller.msg("%s - %d. %s" % (i.db.name, i.db.qty, i.desc))
				itemslist.append(i.key)
		if itemslist == []:
			self.caller.msg("|/You do not currently have any items available to use outside of battle.|/Please visit one of the many item vendors or search around to stock up.")
			return
	#Player chooses Item
		answer = yield("|/Which item would you like to use?|/|gE|nxit to quit.")
	#Check to exit
		if answer.lower() in ["e", "exit"]:
			self.caller.msg("Goodbye.")
			return
	#Check if item is not in inventory.
		if answer.lower() not in (i.lower() for i in itemslist):
			self.caller.msg("|/You do not appear to have any %s." % (answer))
			return
	#Check if item is in inventory
		if answer.lower() in (i.lower() for i in itemslist):
		#Get the target
			target = self.caller.search(answer.lower(), candidates=self.caller.contents)
			if not target:
				self.caller.msg("|/Something went wrong with your inventory, contact blakhal0")
				return
		#Check that quantity is over 0.
			if int(target.db.qty) <= 0:
				self.caller.msg("|/You are all out of %s." % (target.db.name))
				target.delete()
				return
		#Use the item.
			if target.db.qty > 0:
			#Health Restore Items
				if target.db.action[0] == "health":
					self.caller.db.hp += int(target.db.action[1])
					if self.caller.db.hp > self.caller.db.maxhp:
						self.caller.db.hp = self.caller.db.maxhp
					self.caller.msg("|/You use the %s and restore %s HP." % (target.db.name, target.db.action[1]))
					self.caller.msg("%d HP %d MP" % (self.caller.db.hp, self.caller.db.mp))
			#Magic Restore Items
				if target.db.action[0] == "magic":
					self.caller.db.mp += int(target.db.action[1])
					if self.caller.db.mp > self.caller.db.maxmp:
						self.caller.db.mp = self.caller.db.maxmp
					self.caller.msg("|/You use the %s and restore %s MP." % (target.db.name, target.db.action[1]))
					self.caller.msg("%d HP %d MP" % (self.caller.db.hp, self.caller.db.mp))
			#Health and Magic Restore Items
				if target.db.action[0] == "all":
					self.caller.db.hp += int(target.db.action[1])
					if self.caller.db.hp > self.caller.db.maxhp:
						self.caller.db.hp = self.caller.db.maxhp
					self.caller.db.mp += int(target.db.action[2])
					if self.caller.db.mp > self.caller.db.maxmp:
						self.caller.db.mp = self.caller.db.maxmp
					self.caller.msg("|/You use the %s and restore %s HP and %s MP." % (target.db.name, target.db.action[1], target.db.action[2]))
					self.caller.msg("%d HP %d MP" % (self.caller.db.hp, self.caller.db.mp))
			#Travel Item
				if target.db.action[0] == "travel":
					if self.caller.location.tags.get("notravel"):
						self.caller.msg("|/The faster feather just floats there, doing nothing. It doesn't seem to work in this place.")
						return
					if not self.caller.db.locations:
						self.caller.msg("|/You must learn a location to be able to travel there.")
						return
					else:
						possibleplaces = ', '.join(self.caller.db.locations).title()
						answer = yield("|/Where to?|/%s" % (possibleplaces))
						if answer.lower() not in self.caller.db.locations:
							self.caller.msg("|/You do not know that location.")
							return
						else:
							travelto = getattr(places, answer.replace(" ", "").lower()).location
							self.caller.db.lastcity = travelto
							self.caller.msg("|/You toss the faster feather into the wind and suddenly find yourself in %s." % (answer.lower().title()))
							self.caller.msg("|/ ")
							yield 1
							results = search_object(travelto)
							self.caller.move_to(results[0], quiet=True, move_hooks=True)
			#Stat Increase Item
				if target.db.action[0] == "statinc":
					if target.db.stat == "attack":
						self.caller.db.attack += target.db.increase
					if target.db.stat == "defense":
						self.caller.db.defense += target.db.increase
					if target.db.stat == "magic":
						self.caller.db.maxmp += target.db.increase
					if target.db.stat == "health":
						self.caller.db.maxhp += target.db.increase
					self.caller.msg("|/You eat the %s and gain %d %s!" % (target.db.name, target.db.increase, target.db.stat))
			#Decrement quantity
				target.db.qty -= 1
			#Check if that used up the last of the item
				if int(target.db.qty) == 0:
					self.caller.msg("|/You've used up the very last of the %s." % (target.db.name))
					target.delete()
					return
				return

class fight(default_cmds.MuxCommand):
	key = "fight"
	auto_help = False
	def func(self):
	#disable fighting for building
		if self.caller.tags.get("pacifist"):
			self.caller.msg("|/" + self.caller.at_look(self.caller.location))
			return
		if self.caller.location.db.fight == "no":
			self.caller.msg("|/Easy there killer, there's nothing to fight in this area.")
			return
		if not self.caller.tags.get("letsfight"):
			self.caller.msg("|/Monsters aren't going to just show up, you gotta go find them. Just walk around a bit.")
			return
		self.caller.tags.remove("letsfight")
		def returnlook():
			self.caller.msg("|/" + self.caller.at_look(self.caller.location))
		def flee():
		#player ran away
			self.caller.tags.remove("battle")
			self.caller.msg("|/You tuck tail and run, like the yellow bellied coward you are.")
			self.caller.db.hp = herohp
			self.caller.db.mp = heromp
			self.caller.msg("|/  |005.|015:|025*|035~|nYou ran away.|035~|025*|015:|005.|n|/You gain 0 gold and 0 exp.|/HP: %d MP %d|/Gold: %d Exp: %d" % (herohp, heromp, self.caller.db.gold, self.caller.db.exp))
			utils.delay(2, returnlook)
			return
		def death():
		#player died in battle
			self.caller.tags.remove("battle")
			self.caller.msg("|/|rWhat tragic fate, you have fallen in battle to the %s|n|/You have brought shame to yourself and your family." % (beastname))
			self.caller.db.deathcount += 1
			if self.caller.tags.get("training"):
				self.caller.msg("|/|mMaster Roshi|n says: You couldn't fight yer way outta a stand of tall grass! HARHAR-har-har-har.|/|mMaster Roshi|n says: Get up! Have a pepper! These'll put a shine on yer shell! WOOOWEEE!")
				self.caller.msg("Your HP and MP have been restored!")
				self.caller.db.hp = self.caller.db.maxhp
				self.caller.db.mp = self.caller.db.maxmp
				returnlook()
				return
			if self.caller.tags.get("arenabattle"):
				self.caller.tags.remove("arenabattle")
				self.caller.msg("|/|mAnnouncer|n: OH THAT'S GOTTA HURT. LET'S GET A ROUND OF APPLAUSE FOR OUR CHALLENGER %s!!!!" % (self.caller.key.upper()))
				self.caller.msg("|gIf you made it past the first round, don't forget to talk to the Host to claim your reward!|n")
				self.caller.db.hp = self.caller.db.maxhp
				self.caller.db.mp = self.caller.db.maxmp
				results = search_object("#7861")
				self.caller.move_to(results[0], quiet=True, move_hooks=True)
				return
			else:
				self.caller.db.hp = int(self.caller.db.maxhp * .5)
				self.caller.db.mp = int(self.caller.db.maxmp * .5)
				self.caller.db.gold -= int(self.caller.db.gold * .2)
				results = search_object(self.caller.db.lastcity)
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				return
		def success():
		#player wins battle
			def monsterinventory():
				if beastname not in self.caller.db.monsterstats.keys():
					self.caller.db.monsterstats[beastname] = {"killed": 1, "desc": beastdesc}
				else:
					self.caller.db.monsterstats[beastname]["killed"] += 1
		#check if monster is a boss
			def checkgod():
				try:
					getattr(beastiary, beast).god
				except AttributeError:
					return
				else:
				#Success message
					self.caller.msg(getattr(beastiary, beast).successmsg)
				#Remove applicable tags
					if getattr(beastiary, beast).tagstoremove:
						for i in getattr(beastiary, beast).tagstoremove:
							if self.caller.tags.get(i):
								self.caller.tags.remove(i)
				#Add applicable tags
					if getattr(beastiary, beast).tagstoadd:
						for i in getattr(beastiary, beast).tagstoadd:
							if not self.caller.tags.get(i):
								self.caller.tags.add(i)
				#Add Accolades
					if getattr(beastiary, beast).accoladetoadd:
						if not getattr(beastiary, beast).accoladetoadd in self.caller.db.accolades:
							self.caller.db.accolades.append(getattr(beastiary, beast).accoladetoadd)
				#Remove inventory items
					if getattr(beastiary, beast).itemstoremove:
						for i in getattr(beastiary, beast).itemstoremove:
							for x in self.caller.contents:
								if x.key.lower() == i.lower():
									x.delete()
				#Send player to designated location
					if not getattr(beastiary, beast).sendto == "":
						results = search_object(getattr(beastiary, beast).sendto)
						self.caller.move_to(results[0], quiet=True, move_hooks=False)
					return
			def checkexp():
				levelup = "no"
				if self.caller.db.lvl == 1 and self.caller.db.exp >= 7:
					attplus = 0
					defplus = 0
					hpplus = 2
					mpplus = 0
					levelup = "yes"
				if self.caller.db.lvl == 2 and self.caller.db.exp >= 23:
					attplus = 1
					defplus = 1
					hpplus = 2
					mpplus = 0
					levelup = "yes"
				if self.caller.db.lvl == 3 and self.caller.db.exp >= 47:
					attplus = 2
					defplus = 1
					hpplus = 5
					mpplus = 11
					levelup = "yes"
				if self.caller.db.lvl == 4 and self.caller.db.exp >= 110:
					attplus = 0
					defplus = 1
					hpplus = 4
					mpplus = 4
					levelup = "yes"
				if self.caller.db.lvl == 5 and self.caller.db.exp >= 220:
					attplus = 5
					defplus = 1
					hpplus = 3
					mpplus = 4
					levelup = "yes"
				if self.caller.db.lvl == 6 and self.caller.db.exp >= 450:
					attplus = 4
					defplus = 3
					hpplus = 2
					mpplus = 2
					levelup = "yes"
				if self.caller.db.lvl == 7 and self.caller.db.exp >= 800:
					attplus = 2
					defplus = 1
					hpplus = 6
					mpplus = 3
					levelup = "yes"
				if self.caller.db.lvl == 8 and self.caller.db.exp >= 1300:
					attplus = 4
					defplus = 1
					hpplus = 4
					mpplus = 7
					levelup = "yes"
				if self.caller.db.lvl == 9 and self.caller.db.exp >= 2000:
					attplus = 8
					defplus = 1
					hpplus = 4
					mpplus = 4
					levelup = "yes"
				if self.caller.db.lvl == 10 and self.caller.db.exp >= 2900:
					attplus = 5
					defplus = 4
					hpplus = 8
					mpplus = 10
					levelup = "yes"
				if self.caller.db.lvl == 11 and self.caller.db.exp >= 4000:
					attplus = 5
					defplus = 2
					hpplus = 6
					mpplus = 8
					levelup = "yes"
				if self.caller.db.lvl == 12 and self.caller.db.exp >= 5500:
					attplus = 5
					defplus = 2
					hpplus = 7
					mpplus = 6
					levelup = "yes"
				if self.caller.db.lvl == 13 and self.caller.db.exp >= 7500:
					attplus = 4
					defplus = 3
					hpplus = 8
					mpplus = 6
					levelup = "yes"
				if self.caller.db.lvl == 14 and self.caller.db.exp >= 10000:
					attplus = 8
					defplus = 5
					hpplus = 8
					mpplus = 2
					levelup = "yes"
				if self.caller.db.lvl == 15 and self.caller.db.exp >= 13000:
					attplus = 8
					defplus = 3
					hpplus = 6
					mpplus = 23
					levelup = "yes"
				if self.caller.db.lvl == 16 and self.caller.db.exp >= 17000:
					attplus = 4
					defplus = 4
					hpplus = 8
					mpplus = 5
					levelup = "yes"
				if self.caller.db.lvl == 17 and self.caller.db.exp >= 21000:
					attplus = 0
					defplus = 3
					hpplus = 15
					mpplus = 8
					levelup = "yes"
				if self.caller.db.lvl == 18 and self.caller.db.exp >= 25000:
					attplus = 13
					defplus = 1
					hpplus = 15
					mpplus = 7
					levelup = "yes"
				if self.caller.db.lvl == 19 and self.caller.db.exp >= 29000:
					attplus = 2
					defplus = 1
					hpplus = 8
					mpplus = 0
					levelup = "yes"
				if self.caller.db.lvl == 20 and self.caller.db.exp >= 33000:
					attplus = 5
					defplus = 0
					hpplus = 11
					mpplus = 13
					levelup = "yes"
				if self.caller.db.lvl == 21 and self.caller.db.exp >= 37000:
					attplus = 3
					defplus = 2
					hpplus = 9
					mpplus = 11
					levelup = "yes"
				if self.caller.db.lvl == 22 and self.caller.db.exp >= 41000:
					attplus = 2
					defplus = 1
					hpplus = 7
					mpplus = 7
					levelup = "yes"
				if self.caller.db.lvl == 23 and self.caller.db.exp >= 45000:
					attplus = 2
					defplus = 3
					hpplus = 5
					mpplus = 12
					levelup = "yes"
				if self.caller.db.lvl == 24 and self.caller.db.exp >= 49000:
					attplus = 4
					defplus = 1
					hpplus = 5
					mpplus = 0
					levelup = "yes"
				if self.caller.db.lvl == 25 and self.caller.db.exp >= 53000:
					attplus = 10
					defplus = 1
					hpplus = 6
					mpplus = 6
					levelup = "yes"
				if self.caller.db.lvl == 26 and self.caller.db.exp >= 57000:
					attplus = 4
					defplus = 1
					hpplus = 6
					mpplus = 7
					levelup = "yes"
				if self.caller.db.lvl == 27 and self.caller.db.exp >= 61000:
					attplus = 8
					defplus = 3
					hpplus = 9
					mpplus = 5
					levelup = "yes"
				if self.caller.db.lvl == 28 and self.caller.db.exp >= 65000:
					attplus = 7
					defplus = 5
					hpplus = 7
					mpplus = 10
					levelup = "yes"
				if self.caller.db.lvl == 29 and self.caller.db.exp >= 70535:
					attplus = 11
					defplus = 5
					hpplus = 13
					mpplus = 10
					levelup = "yes"
				if self.caller.db.lvl == 30 and self.caller.db.exp >= 125000:
					attplus = 99
					defplus = 99
					hpplus = 99
					mpplus = 99
					levelup = "yes"
				if levelup == "yes":
					self.caller.db.lvl += 1
					self.caller.db.maxhp += hpplus
					self.caller.db.hp = self.caller.db.maxhp
					self.caller.db.maxmp += mpplus
					self.caller.db.mp = self.caller.db.maxmp
					self.caller.db.attack += attplus
					self.caller.db.defense += defplus
					self.caller.msg("|/|gCourage and wit have served you well.|/Your spice level increases to %d!!|n|/You gain %d HP, %d MP.|/Attack increases %d.|/Defense increases %d." % (self.caller.db.lvl, hpplus, mpplus, attplus, defplus))
					return
			def checkdrop():
#				if randint (1,2) in [1, 2]:
				if randint(1,6) in [2, 4, 6]:
					loot = getattr(beastiary, beast).dropitem
					loottype = getattr(beastiary, beast).droptype
					if loottype == "items":
						lootname = getattr(items, loot).name
					if loottype == "armor":
						lootname = getattr(armor, loot).name
					if loottype == "weapons":
						lootname = getattr(weapons, loot).name
					sitc = "typeclasses.%s.%s" % (loottype, loot)
					target = self.caller.search(lootname, candidates=self.caller.contents, quiet=True)
					if loottype in ["armor", "weapons"]:
						if target:
							return
						else:
							md_proto = {
							"key": "%s" % (lootname),
							"typeclass": "%s" % (sitc),
							"location": self.caller
							}
							spawn(md_proto)
					elif not target:
						#spawn item to player
						md_proto = {
						"key": "%s" % (lootname),
						"typeclass": "%s" % (sitc),
						"qty": 1,
						"location": self.caller
						}
						spawn(md_proto)
					else:
						target[0].db.qty += 1
					self.caller.msg("|/The %s was carrying loot!|/You get a %s!" % (beastname, lootname))
					return
				else:
					return
			self.caller.db.gold += gold
			self.caller.db.exp += exp
			self.caller.db.hp = herohp
			self.caller.db.mp = heromp
			self.caller.tags.remove("battle")
			self.caller.msg("|/       |005.|015:|025*|035~|n|gSuccess!|n|035~|025*|015:|005.|n|/You have defeated the %s.|/You gain %d gold and %d exp.|/HP: %d MP %d|/Gold: %d Exp: %d" % (beastname, gold, exp, herohp, heromp, self.caller.db.gold, self.caller.db.exp))
			checkexp()
			if getattr(beastiary, beast).drop == "yes":
				checkdrop()
			monsterinventory()
			checkgod()
			utils.delay(2, returnlook)
			return
		def ranaway():
		#monster ran away
			self.caller.db.hp = herohp
			self.caller.db.mp = heromp
			self.caller.tags.remove("battle")
			self.caller.msg("|/  |005.|015:|025*|035~|nOh no, it ran away!|035~|025*|015:|005.|n|/You gain 0 gold and 0 exp.|/HP: %d MP %d|/Gold: %d Exp: %d" % (herohp, heromp, self.caller.db.gold, self.caller.db.exp))
			utils.delay(2, returnlook)
			return
	#Get room zone
		loczone = self.caller.location.db.zone
	#Choose a monster
		if randint(1, 10) == 10 or self.caller.tags.get("fightrare"):
			if self.caller.tags.get("fightrare"):
				self.caller.tags.remove("fightrare")
			beast = random.choice(getattr(zones, loczone).rare)
		else:
			beast = random.choice(getattr(zones, loczone).monsters)
	#Set monster name, hp, mp, att, defense, and attack range
		beastname = getattr(beastiary, beast).name
		beasthp = getattr(beastiary, beast).hp
		beastmp = getattr(beastiary, beast).mp
		beastmaxhp = getattr(beastiary, beast).hp
		beastmaxmp = getattr(beastiary, beast).mp
		beastweakness = getattr(beastiary, beast).weakness
		beastatt = getattr(beastiary, beast).attack
		beastdef = getattr(beastiary, beast).defense
		beastlowdef = beastdef - int(beastdef * .75)
		beastlowatt = int(beastatt - (beastatt * .2))
		beasthighatt = int(beastatt + (beastatt * .3))
		beastattoption = getattr(beastiary, beast).actions
		beastphrase = getattr(beastiary, beast).phrases
		beastdesc = getattr(beastiary, beast).desc
	#Set reward gold and experience
		gold = getattr(beastiary, beast).gold
		exp = getattr(beastiary, beast).exp
	#Set fighter hp, mp, attack, defense, and attack range
		herohp = self.caller.db.hp
		heromp = self.caller.db.mp
		#Get attack
		#Check if player 'lost' their weapon
		if not self.caller.db.weaponequipped == "none":
			target = self.caller.search(self.caller.db.weaponequipped, candidates=self.caller.contents, quiet=True)
			if not target:
				self.caller.msg("|/|rOh no, it appears you've lost the %s, looks like you're going to be fighting barehanded.|n" % (self.caller.db.weaponequipped))
				heroatt = self.caller.db.attack
				self.caller.db.weaponequipped = "none"
				self.caller.db.equipatt = 0
			else:
				heroatt = self.caller.db.attack + self.caller.db.equipatt
		else:
			heroatt = self.caller.db.attack
		#Get defense
		regen = 0
		degen = 0
		#Check if player 'lost' their armor
		if not self.caller.db.armorequipped == "none":
			target = self.caller.search(self.caller.db.armorequipped, candidates=self.caller.contents, quiet=True)
			if not target:
				self.caller.msg("|/|rOh no, it appears you've lost the %s, looks like you're going to be fighting naked.|n" % (self.caller.db.armorequipped))
				herodef = self.caller.db.defense
				self.caller.db.armorequipped = "none"
				self.caller.db.equipdef = 0
			else:
				if target[0].tags.get("sainted"):
					healthregen = int(target[0].db.heal)
					regen = 2
					degen = 0
				if target[0].tags.get("cursed"):
					healthdegen = int(target[0].db.unheal)
					regen = 0
					degen = 10
		#Check if player 'lost' their shield.
		if not self.caller.db.shieldequipped == "none":
			target = self.caller.search(self.caller.db.shieldequipped, candidates=self.caller.contents, quiet=True)
			if not target:
				self.caller.msg("|/|rOh no, it appears you've lost the %s, looks like you're going to be fighting without a shield.|n" % (self.caller.db.shieldequipped))
				self.caller.db.shieldequipped = "none"
				self.caller.db.shielddef = 0
		#set defense
		herodef = self.caller.db.defense + self.caller.db.equipdef + self.caller.db.shielddef
		herolowdef = herodef - int(herodef * .75)
		herolowatt = int(heroatt - (heroatt * .2))
		herohighatt = int(heroatt + (heroatt * .3))
		spelllist = ""
		heallist = ""
		firelist = ""
		aqualist = ""
		eleclist = ""
		lightlist = ""
		darklist = ""
		windlist = ""
	#Create spells list
		for ms in self.caller.db.battlespells:
			mname = getattr(magic, ms).name
			mcost = str(getattr(magic, ms).cost)
			mgroup = getattr(magic, ms).group
			mkind = getattr(magic, ms).kind
			if mgroup == "heal":
				heallist = heallist + mname + " - " + mcost + ". "
			if mkind == "f":
				firelist = firelist + mname + " - " + mcost + ". "
			if mkind == "a":
				aqualist = aqualist + mname + " - " + mcost + ". "
			if mkind == "e":
				eleclist = eleclist + mname + " - " + mcost + ". "
			if mkind == "w":
				windlist = windlist + mname + " - " + mcost + ". "
			if mkind == "l":
				lightlist = lightlist + mname + " - " + mcost + ". "
			if mkind == "d":
				darklist = darklist + mname + " - " + mcost + ". "
#		for i in (heallist, firelist, aqualist, eleclist, windlist, lightlist, darklist):
		if not heallist == "":
			spelllist = spelllist + "Heal:|/|-" + heallist + "|/"
		if not firelist == "":
			spelllist = spelllist + "Fire:|/|-" + firelist + "|/"
		if not aqualist == "":
				spelllist = spelllist + "Water:|/|-" + aqualist + "|/"
		if not eleclist == "":
				spelllist = spelllist + "Electric:|/|-" + eleclist + "|/"
		if not windlist == "":
				spelllist = spelllist + "Wind:|/|-" + windlist + "|/"
		if not lightlist == "":
				spelllist = spelllist + "Light:|/|-" + lightlist + "|/"
		if not darklist == "":
				spelllist = spelllist + "Dark:|/|-" + darklist + "|/"
#			spelllist = spelllist + i + "|/"
		if spelllist == "":
			spelllist = "You do not know any spells."
	#Announce the monster
		self.caller.msg("|/A %s draws near!!" % (beastname))
		self.caller.tags.add("battle")
	#Monster quick attack
		if randint(1, 20) == 10:
			self.caller.msg("|/%s suddenly attacks, catching you off guard!!" % (beastname))
			beastdamage = randint(beastlowatt, beasthighatt)
			herohp -= beastdamage
			self.caller.msg("You take %d in damage." % (beastdamage))
			if herohp <= 0:
				death()
				return
	######################
	#Start the fight loop#
	######################
		herodoubledefense = "no"
		beastdoubledefense = "no"
		incap = 0
		rounds = 0
		while 1 < 10:
			rounds += 1
		#Sainted and Cursed Armor
			target = self.caller.search(self.caller.db.armorequipped, candidates=self.caller.contents, quiet=True)
			if target:
				if target[0].tags.get("sainted"):
					if regen > 0:
						if herohp + healthregen < self.caller.db.maxhp:
							if not randint(1, 3) == 1:
								herohp += healthregen
								self.caller.msg("|/|gThe sainted armor heals your wounds, you gain %d hp.|n" % (healthregen))
								regen -= 1
				if target[0].tags.get("cursed"):
					if degen > 0:
						if not randint(1, 3) == 1:
							herohp -= healthdegen
							self.caller.msg("|/|rThe cursed armor exacts it's toll, you lose %d hp.|n" % (healthdegen))
							degen -= 1
			self.caller.msg("|/%s HP: %d MP: %d" % (beastname, beasthp, beastmp))
			if herohp <= int(self.caller.db.maxhp * .25):
				self.caller.msg("%s |rHP: %d|n MP: %d" % (self.caller.key, herohp, heromp))
			else:
				self.caller.msg("%s HP: %d MP: %d" % (self.caller.key, herohp, heromp))
			answer = yield("Command? |gA|nttack, |gD|nefend, |gM|nagic, |gI|ntem, |gF|nlee")
	############
	#Hero Action
	############
		#Attack
			if answer.lower() in ["a", "attack"]:
				if incap > 0:
					herodamage = 0
					self.caller.msg("|/%s" % (heroincapmsg))
			#Check for Crit Hit or Double Defense
				else:
					if randint(1, 50) == 25:
						self.caller.msg("|/You attack with the spice of a thousand peppers!!")
						herodamage = int(heroatt * 2)
					else:
						self.caller.msg("|/You attack the %s!" % (beastname))
						herodamage = randint(herolowatt, herohighatt)
						if beastdoubledefense == "yes":
							herodamage = int(herodamage * .5)
							beastoubledefense = "no"
		#Magic
			elif answer.lower() in ["m", "magic"]:
				if incap > 0:
					herodamage = 0
					self.caller.msg("|/%s" % (heroincapmsg))
				else:
					magicanswer = yield("|005.|015:|025*|035~|nSpells|035~|025*|015:|005.|n|/%s" % (spelllist))
					magicanswer = magicanswer.lower()
					if magicanswer not in self.caller.db.battlespells:
						self.caller.msg("|/You do not know that spell.")
						herodamage = 0
					else:
						magicname = getattr(magic, magicanswer).name
						magiccost = getattr(magic, magicanswer).cost
						magicbase = getattr(magic, magicanswer).base
						magicgroup = getattr(magic, magicanswer).group
						magicphrase = getattr(magic, magicanswer).phrase
						magictype = getattr(magic, magicanswer).kind
						if magiccost > heromp:
							self.caller.msg("|/Your magic reserves are too low for that spell.")
							herodamage = 0
						else:
							heromp -= magiccost
						#attack spells
							if magicgroup == "aggressive":
								#killing spells
								#dark
								if magicname == "death":
									if randint(1,10) == 6:
										herodamage = beasthp + beastdef
									else:
										herodamage = 0
										magicphrase = "You summon a demon from the underworld, but none appear."
								if magicname == "graverobber":
									coin = randint(10,80)
									self.caller.db.gold += coin
									self.caller.msg("You sneak up and steal %d gold during your attack." % (coin))
								#light
								if magicname == "hecatomb":
									if herohp == 1:
										magicphrase = "Your hp is too low to attempt this spell."
									if herohp > 1:
										herohp = int(herohp * .5)
										if randint(1,10) == 7:
											herodamage = beasthp + beastdef
										else:
											herodamage = 0
											magicphrase = "You open a vein, but the light does not shine upon you."
								#Ladrone Special
								if magicname == "stolenheart":
									herohp += magicbase + int(self.caller.db.lvl * 2.5)
									if herohp > self.caller.db.maxhp:
										herohp = self.caller.db.maxhp
									self.caller.msg("You regain %d hp." % ((magicbase + int(self.caller.db.lvl * 2.5))))
								if magictype in beastweakness:
									herodamage = magicbase * 2
								else:
									herodamage = magicbase
								if randint(1, 50) == 25:
									self.caller.msg("|/A raging torrent of magic bursts forth!!")
									herodamage += int(heroatt * 2)
								herodamage = herodamage + int(self.caller.db.lvl * 2.5)
								self.caller.msg("|/%s" % (magicphrase))
						#heal spells
							elif magicgroup == "heal":
								if magictype == "self":
									herodamage = 0
									herohp += magicbase
									if herohp > self.caller.db.maxhp:
										herohp = self.caller.db.maxhp
									self.caller.msg("|/%s|/You regain %d HP." % (magicphrase, magicbase))
								elif magictype == "enemy":
									herodamage = 0
									beasthp += magicbase
									if beasthp > beastmaxhp:
										beasthp = beastmaxhp
									self.caller.msg("|/%s|/%s regains %d HP." % (magicphrase, beastname, magicbase))
		#Defend
			elif answer.lower() in ["d", "defend"]:
				if incap > 0:
					herodamage = 0
					self.caller.msg("|/%s" % (heroincapmsg))
				else:
					herodamage = 0
					self.caller.msg("|/You steel yourself for the coming attack.")
					herodoubledefense = "yes"
		#Item
			elif answer.lower() in ["i", "item"]:
				herodamage = 0
				itemslist = []
			#Create Items List
				self.caller.msg("|/|005.|015:|025*|035~|nItems|035~|025*|015:|005.|n")
				for i in self.caller.contents:
					if i.tags.get("item") and i.tags.get("battle"):
						self.caller.msg("%s - %d. %s" % (i.db.name, i.db.qty, i.desc))
						itemslist.append(i.key)
					if i.tags.get("item") and i.tags.get("both"):
						self.caller.msg("%s - %d. %s" % (i.db.name, i.db.qty, i.desc))
						itemslist.append(i.key)
				if itemslist == []:
					self.caller.msg("|/You do not currently have any items available to use during battle.")
					self.caller.msg("You forfeit your turn.")
			#Choose Item
				answer = yield("|/Which item would you like to use?|/|gN|none for no item.")
				if answer.lower() in ["n", "none"]:
					self.caller.msg("|/Paralyzed by indecision, bad choices, and confusion you forfeit your turn.")
			#Check if not in inventory.
				elif answer.lower() not in (i.lower() for i in itemslist):
					self.caller.msg("|/You do not appear to have any %s." % (answer))
					self.caller.msg("You forfeit your turn.")
			#Verify in inventory
				elif answer.lower() in (i.lower() for i in itemslist):
				#Get the target
					target = self.caller.search(answer.lower(), candidates=self.caller.contents)
					if not target:
						self.caller.msg("|/Something went disastrously wrong with your inventory, contact blakhal0")
						self.caller.msg("You forfeit your turn.")
				#Check that quantity is over 0.
					elif target.db.qty <= 0:
						self.caller.msg("|/You are all out of %s." % (target.db.name))
						target.delete()
						self.caller.msg("You forfeit your turn.")
				#Use the item.
					elif target.db.qty > 0:
					#Health Restore Items
						if target.db.action[0] == "health":
							herohp += int(target.db.action[1])
							if herohp > self.caller.db.maxhp:
								herohp = self.caller.db.maxhp
							self.caller.msg("|/You use the %s and restore %s HP." % (target.db.name, str(target.db.action[1])))
					#Magic Restore Items
						elif target.db.action[0] == "magic":
							heromp += int(target.db.action[1])
							if heromp > self.caller.db.maxmp:
								heromp = self.caller.db.maxmp
							self.caller.msg("|/You use the %s and restore %s MP." % (target.db.name, str(target.db.action[1])))
					#Health and Magic Restore Items
						elif target.db.action[0] == "all":
							herohp += int(target.db.action[1])
							if herohp > self.caller.db.maxhp:
								herohp = self.caller.db.maxhp
							heromp += int(target.db.action[2])
							if heromp > self.caller.db.maxmp:
								heromp = self.caller.db.maxmp
							self.caller.msg("|/You use the %s and restore %s HP and %s MP." % (target.db.name, str(target.db.action[1]), str(target.db.action[2])))
					#Flee Item
						elif target.db.action[0] == "flee":
							if getattr(beastiary, beast).noflee == "yes":
								target.db.qty -= 1
								if target.db.qty == 0:
									self.caller.msg("|/You've used up the very last of the %s." % (target.db.name))
									target.delete()
								self.caller.msg("|/%s circles around, blocking your escape.|/There appears to be no way to escape this fight." % (beastname))
							else:
								self.caller.msg("|/%s" % (target.db.phrase))
								flee()
								target.db.qty -= 1
								if target.db.qty == 0:
									self.caller.msg("|/You've used up the very last of the %s." % (target.db.name))
									target.delete()
								break
				#Decrement inventory quantity
					target.db.qty -= 1
				#Check if that used up the last of the item
					if target.db.qty == 0:
						self.caller.msg("|/You've used up the very last of the %s." % (target.db.name))
						target.delete()
		#Flee
			elif answer.lower() in ["f", "flee"]:
				if incap > 0:
					herodamage = 0
					self.caller.msg("%s" % (heroincapmsg))
				else:
					if getattr(beastiary, beast).noflee == "yes":
						herodamage = 0
						self.caller.msg("|/%s circles around, blocking your escape." % (beastname))
					else:
						if randint(1, 5) == 3:
							flee()
							break
						else:
							herodamage = 0
							self.caller.msg("|/%s circles around, blocking your escape." % (beastname))
		#Hero Catchall
			else:
				herodamage = 0
				self.caller.msg("|/|rThat's not a valid option.|n|/You attempt a maneuver, slip, fall on your butt, and cry.")
		#Settle out hero turn
			if herodamage > 0:
				herodamage -= randint(beastlowdef, beastdef)
				if herodamage <= 0:
					herodamage = 1
				beasthp -= herodamage
				self.caller.msg("%s takes %d damage." % (beastname, herodamage))
			elif herodamage < 0:
				herodamage = 1
				beasthp -= herodamage
				self.caller.msg("%s takes %d damage." % (beastname, herodamage))
		#Check if monster is dead
			if beasthp <= 0:
				success()
				break
#Pause for dramatic effect
			yield 1
	###############
	#Monster action
	###############
		#Count down incapacitation
			if incap > 0:
				incap -= 1
				if incap == 0:
					self.caller.msg("|/|gYou snap out of it, ready to fight.|n")
			baction = random.choice(beastattoption)
		#Attack
			if baction == "a":
				if beastphrase == []:
					self.caller.msg("|/%s attacks!" % (beastname))
				else:
					if randint(1, 2) == 2:
						self.caller.msg("|/%s" % (random.choice(beastphrase)))
					else:
						self.caller.msg("|/%s attacks!" % (beastname))
				beastdamage = randint(beastlowatt, beasthighatt)
				if herodoubledefense == "yes":
					beastdamage = int(beastdamage * .5)
					herodoubledefense = "no"
				else:
					beastdamage -= randint(herolowdef, herodef)
				if beastdamage < 1:
					beastdamage = 1
		#Defend
			elif baction == "d":
				self.caller.msg("|/%s steels itself for the next attack!" % (beastname))
				#figure out how to double beast defense
				beastdamage = 0
		#Magic
			elif baction == "m":
				self.caller.msg("|/%s attempts a spell." % (beastname))
				if beastmp == 0:
					self.caller.msg("The %s's magic reserves are depleted, the spell fails." % (beastname))
					beastdamage = 0
				else:
					beastspells = getattr(beastiary, beast).spells
					beastspell = random.choice(beastspells)
					magiccost = getattr(magic, beastspell).cost
					if beastmp < magiccost:
						self.caller.msg("The %s's magic reserves are too low, the spell fails." % (beastname))
						beastdamage = 0
					else:
						beastmp -= magiccost
						beastspellphrase = getattr(magic, beastspell).enemyphrase
						beastspellgroup = getattr(magic, beastspell).group
						beastspelltype = getattr(magic, beastspell).kind
						beastspellbase = getattr(magic, beastspell).base
						if beastspellgroup == "heal":
							if beastspelltype == "self":
								beastdamage = 0
								beasthp += beastspellbase
								if beasthp > beastmaxhp:
									beasthp = beastmaxhp
								self.caller.msg("%s|/%s regains %d hp." % (beastspellphrase, beastname, int(beastspellbase)))
							if beastspelltype == "enemy":
								beastdamage = 0
								herohp += beastspellbase
								if herohp > self.caller.db.maxhp:
									herohp = self.caller.db.maxhp
								self.caller.msg("|/%s|/You regain %d HP." % (beastspellphrase, int(beastspellbase)))
						else:
							beastdamage = beastspellbase
							if randint(1, 50) == 25:
								self.caller.msg("A raging torrent of magic bursts forth from the %s!!" % (beastname))
								beastdamage = int(beastdamage * 2)
							self.caller.msg("%s" % (beastspellphrase))
		#Incapacitate
			elif baction == "i":
				beastdamage = 0
				beastincattmsg = getattr(beastiary, beast).incapatt
				self.caller.msg("|/%s %s." % (beastname, beastincattmsg))
				if randint(1, 4) == 3:
					heroincapmsg = getattr(beastiary, beast).incapsuc
					self.caller.msg("|r%s|n" % (heroincapmsg))
					incap = randint(1, 3)
				else:
					self.caller.msg("The attack has no effect on you.")
		#Flee
			elif baction == "f":
				if randint(1, 5) == 3:
					self.caller.msg("|/The %s tucks tail and flees in terror." % (beastname))
					ranaway()
					break
				else:
					beastdamage = 0
					self.caller.msg("|/The %s attempts to flee from battle.|/You circle around, blocking its escape." % (beastname))
		#No Action
			elif baction == "n":
				beastdamage = 0
				beastlazymsg = getattr(beastiary, beast).lazymsg
				self.caller.msg("|/%s %s." % (beastname, beastlazymsg))
		#Steal
			elif baction == "s":
			#Steal Money
				if getattr(beastiary, beast).stealtype == "money":
					if self.caller.db.gold < 10:
						beastdamage = 10
						self.caller.msg("|/%s attempts to steal some gold but you're poor!|/In a rage of fury it attacks you." % (beastname))
					elif randint(1, 3) == 2:
						beastdamage = 0
						moneystolen = randint(int(self.caller.db.gold * .1), int(self.caller.db.gold * .3))
						self.caller.db.gold -= int(moneystolen)
						self.caller.msg("|/%s steals %d gold!" % (beastname, int(moneystolen)))
					else:
						beastdamage = 0
						self.caller.msg("|/The %s attempts to steal some gold! But it fails." % (beastname))
			#Steal Magic
				if getattr(beastiary, beast).stealtype == "magic":
					if heromp == 0:
						beastdamage = 10
						self.caller.msg("|/%s attempts to absorb your magic, but you have no MP!|/In a rage of fury it attacks you." % (beastname))
					elif heromp <= 5:
						beastdamage = 0
						self.caller.msg("|/%s attempts to absorb your magic.|/It steals 1 MP." % (beastname))
						heromp -= 1
						beastmp += 1
						if beastmp > beastmaxmp:
							beastmp = beastmaxmp
					else:
						beastdamage = 0
						magicstolen = randint(int(heromp * .1), int(heromp * .3))
						self.caller.msg("|/%s attempts to absorb your magic.|/It steals %d MP." % (beastname, int(magicstolen)))
						heromp -= magicstolen
						beastmp += magicstolen
						if beastmp > beastmaxmp:
							beastmp = beastmaxmp
		#Monster Catchall
			else:
				self.caller.msg("Something went wrong with the monster attack, let blakhal0 know that %s failed somehow." % (beastname))
		#Settle out monster turn
			if beastdamage > 0:
				if herodoubledefense == "yes":
					beastdamage -= int(beastdamage * .25)
					herodoubledefense = "no"
				beastdamage -= randint(herolowdef, herodef)
				if beastdamage <= 0:
					beastdamage = 1
				herohp -= beastdamage
				self.caller.msg("You take %d damage." % (beastdamage))
			elif beastdamage < 0:
				beastdamage = 1
				herohp -= beastdamage
				self.caller.msg("You take %d damage." % (beastdamage))
		#Check if hero is dead
			if herohp <= 0:
				death()
				break
		return

class status(default_cmds.MuxCommand):
	key = "status"
	def func(self):
	#check player has not lost items
		if not self.caller.db.weaponequipped == "none":
			target = self.caller.search(self.caller.db.weaponequipped, candidates=self.caller.contents, quiet=True)
			if not target:
				self.caller.msg("|/|rOh no, it appears you've lost the %s.|n" % (self.caller.db.weaponequipped))
				self.caller.db.weaponequipped = "none"
				self.caller.db.equipatt = 0
		if not self.caller.db.armorequipped == "none":
			target = self.caller.search(self.caller.db.armorequipped, candidates=self.caller.contents, quiet=True)
			if not target:
				self.caller.msg("|/|rOh no, it appears you've lost the %s.|n" % (self.caller.db.armorequipped))
				self.caller.db.armorequipped = "none"
				self.caller.db.equipdef = 0
		if not self.caller.db.shieldequipped == "none":
			target = self.caller.search(self.caller.db.shieldequipped, candidates=self.caller.contents, quiet=True)
			if not target:
				self.caller.msg("|/|rOh no, it appears you've lost the %s.|n" % (self.caller.db.shieldequipped))
				self.caller.db.shieldequipped = "none"
				self.caller.db.shielddef = 0
	#create spell list
		if not self.caller.db.battlespells:
			battlespell = "None"
		else:
			battlespell = ', '.join(self.caller.db.battlespells).title()
		if not self.caller.db.overworldspells:
			overspell = "None"
		else:
			overspell = ', '.join(self.caller.db.overworldspells).title()
		if not self.caller.db.locations:
			locations = "None"
		else:
			locations = ', '.join(self.caller.db.locations).title()
		self.caller.msg("|/|005.|015:|025*|035~|n%s Status|035~|025*|015:|005.|n" % (self.caller.key))
		self.caller.msg("|cSpice Lvl|n: %d." % (self.caller.db.lvl))
		if self.caller.db.hp <= int(self.caller.db.maxhp * .25):
			self.caller.msg("|cHP|n:|r %d of %d.|n" % (self.caller.db.hp, self.caller.db.maxhp))
		else:
			self.caller.msg("|cHP|n: %d of %d." % (self.caller.db.hp, self.caller.db.maxhp))
		self.caller.msg("|cMP|n: %d of %d." % (self.caller.db.mp, self.caller.db.maxmp))
		self.caller.msg("|cAttack|n: %d." % (self.caller.db.attack + self.caller.db.equipatt))
		self.caller.msg("|cDefense|n: %d." % (self.caller.db.defense + self.caller.db.equipdef + self.caller.db.shielddef))
		self.caller.msg("|cWeapon|n: %s." % (self.caller.db.weaponequipped))
		self.caller.msg("|cArmor|n: %s." % (self.caller.db.armorequipped))
		self.caller.msg("|cShield|n: %s." % (self.caller.db.shieldequipped))
		self.caller.msg("|cGold|n: %d." % (self.caller.db.gold))
		self.caller.msg("|cEXP|n: %d." % (self.caller.db.exp))
		self.caller.msg("|cBattle Magic|n: %s" % (battlespell))
		self.caller.msg("|cOverworld Magic|n: %s" % (overspell))
		self.caller.msg("|cLocations Learned|n: %s" % (locations))
		return

class equip(default_cmds.MuxCommand):
	key = "equip"
	def func(self):
		weaponslist = []
		weaponsoptions = ""
		armorlist = []
		armoroptions = ""
		shieldlist = []
		shieldoptions = ""
	#Create lists: weapon, armor, and shield
		for i in self.caller.contents:
			if i.tags.get("equipable", category="weapon"):
				weaponslist.append(i.key)
			if i.tags.get("equipable", category="armor"):
				armorlist.append(i.key)
			if i.tags.get("equipable", category="shield"):
				shieldlist.append(i.key)
	#Set currently equipped weapon attack
		if self.caller.db.weaponequipped == "none":
			cew = 0
		else:
			target = self.caller.search(self.caller.db.weaponequipped, candidates=self.caller.contents, quiet=True)
			if not target:
				self.caller.db.weaponequipped = "none"
				self.caller.db.equipatt = 0
				cew = 0
			else:
				cew = int(target[0].db.attack)
	#Set currently equipped armor defense
		if self.caller.db.armorequipped == "none":
			cea = 0
		else:
			target = self.caller.search(self.caller.db.armorequipped, candidates=self.caller.contents, quiet=True)
			if not target:
				self.caller.db.armorequipped = "none"
				self.caller.db.equipdef = 0
				cea = 0
			else:
				cea = int(target[0].db.defense)
	#Set currently equipped shield defense
		if self.caller.db.shieldequipped == "none":
			ces = 0
		else:
			target = self.caller.search(self.caller.db.shieldequipped, candidates=self.caller.contents, quiet=True)
			if not target:
				self.caller.db.shieldequipped = "none"
				self.caller.db.shielddef = 0
				ces = 0
			else:
				ces = int(target[0].db.defense)
	#return current status
		if not weaponslist:
			weaponsoptions = "You have no weapons, go buy some."
		else:
			for i in weaponslist:
				target = self.caller.search(i)
				if target.key == self.caller.db.weaponequipped:
					weaponsoptions = weaponsoptions + target.key + ": +" + str(target.db.attack) + " attack. |gEquipped|n|/"
				else:
					weaponsoptions = weaponsoptions + target.key + ": +" + str(target.db.attack) + " attack.|/"
		if not armorlist:
			armoroptions = "You have no armor, go buy some."
		else:
			for i in armorlist:
				target = self.caller.search(i)
				if target.key == self.caller.db.armorequipped:
					armoroptions = armoroptions + target.key + ": +" + str(target.db.defense) + " defense. |gEquipped|n|/"
				else:
					armoroptions = armoroptions + target.key + ": +" + str(target.db.defense) + " defense.|/"
		if not shieldlist:
			shieldoptions = "You have no shields, go buy some."
		else:
			for i in shieldlist:
				target = self.caller.search(i)
				if target.key == self.caller.db.shieldequipped:
					shieldoptions = shieldoptions + target.key + ": +" + str(target.db.defense) + " defense. |gEquipped|n|/"
				else:
					shieldoptions = shieldoptions + target.key + ": +" + str(target.db.defense) + " defense.|/"
		self.caller.msg("|/   |005.|015:|025*|035~|nCurrently Equipped|035~|025*|015:|005.|n|/Weapon: %s +%d attack.|/Armor: %s +%d defense.|/Shield: %s +%d defense." % (self.caller.db.weaponequipped, int(cew), self.caller.db.armorequipped, int(cea), self.caller.db.shieldequipped, int(ces)))
		answer = yield("|/Change? |gW|neapon, |gA|nrmor, |gS|nhield, |gN|none")
		#change weapon
		if answer.lower() in ["w", "weapon"]:
			#check if player has any weapons.
			if not weaponslist:
				self.caller.msg("You have no weapons to equip, go buy some. Peasant.")
				return
			if self.caller.db.weaponequipped == "Soul Edge":
				self.caller.msg("Tendrils dig into your hand, searing pain shooting up your arm, as your mind considers changing weapons.|/You cannot un-equip this weapon.")
				return
			#list weapon options
			self.caller.msg("|/   |005.|015:|025*|035~|nWeapon Options|035~|025*|015:|005.|n|/%sNone: +0 attack" % (weaponsoptions))
			answer = yield("|/Weapon to Equip?")
			#go it unarmed
			if answer.lower() == "none":
				self.caller.db.weaponequipped = "none"
				self.caller.db.equipatt = 0
				self.caller.msg("|/You decide to let your fists do the talking. Gotta respect that.|/Attack: %d" % (self.caller.db.attack))
				return
			#check if answer is in weapons options
			if answer.lower() not in (i.lower() for i in weaponslist):
				self.caller.msg("|/You don't have a %s to equip." % (answer))
				return
			#equip weapon
			else:
				for i in weaponslist:
					if i.lower() == answer.lower():
						target = self.caller.search(i)
						self.caller.db.weaponequipped = target.key
						self.caller.db.equipatt = target.db.attack
						self.caller.msg("|/You equip the %s.|/Attack: %d" % (target.key, self.caller.db.attack + self.caller.db.equipatt))
						return
				return
		#change armor
		elif answer.lower() in ["a", "armor"]:
			#check if player has any armor.
			if not armorlist:
				self.caller.msg("You have no armor to equip, go buy some. Peasant.")
				return
			if self.caller.db.armorequipped == "Soul Eater Armor":
				self.caller.msg("Spiked hooks dig into your chest and back, you feel blood trickle down your body before the armor drinks it in.|/You cannot un-equip this armor.")
				return
			#list armor options
			self.caller.msg("|/   |005.|015:|025*|035~|nArmor Options|035~|025*|015:|005.|n|/%sNone: +0 defense" % (armoroptions))
			answer = yield("|/Armor to Equip?")
			#buck nekkid
			if answer.lower() == "none":
				self.caller.msg("|/A thick hide and a smile is all you need for protection. Gotta respect that.|/Defense: %d" % (self.caller.db.defense))
				self.caller.db.armorequipped = "none"
				self.caller.db.equipdef = int(0)
				return
			#check if answer is in armor options
			if answer.lower() not in (i.lower() for i in armorlist):
				self.caller.msg("|/You don't have a %s to equip." % (answer))
				return
			#equip armor
			else:
				for i in armorlist:
					if i.lower() == answer.lower():
						target = self.caller.search(i)
						self.caller.db.armorequipped = target.key
						self.caller.db.equipdef = target.db.defense
						self.caller.msg("|/You equip the %s.|/Defense: %d" % (target.key, self.caller.db.defense + self.caller.db.equipdef + self.caller.db.shielddef))
						return
				return
		#change shield
		elif answer.lower() in ["s", "shield"]:
			if not shieldlist:
				self.caller.msg("You have no shield to equip, go buy one. Peasant.")
				return
			if self.caller.db.shieldequipped == "Soul Guard":
				self.caller.msg(".|/You cannot un-equip this shield.")
				return
			#list shield options
			self.caller.msg("|/   |005.|015:|025*|035~|nShield Options|035~|025*|015:|005.|n|/%sNone: +0 defense" % (shieldoptions))
			answer = yield("|/Shield to Equip?")
			#buck nekkid
			if answer.lower() == "none":
				self.caller.msg("|/Who needs a glorified garbage can lid anyways.|/Defense: %d" % (self.caller.db.defense))
				self.caller.db.shieldequipped = "none"
				self.caller.db.shielddef = int(0)
				return
			#check if answer is in shield options
			if answer.lower() not in (i.lower() for i in shieldlist):
				self.caller.msg("|/You don't have a %s to equip." % (answer))
				return
			#equip shield
			else:
				for i in shieldlist:
					if i.lower() == answer.lower():
						target = self.caller.search(i)
						self.caller.db.shieldequipped = target.key
						self.caller.db.shielddef = target.db.defense
						self.caller.msg("|/You equip the %s.|/Defense: %d" % (target.key, self.caller.db.defense + self.caller.db.equipdef + self.caller.db.shielddef))
						return
				return
		#exit
		elif answer.lower() in ["n", "none", "exit"]:
			self.caller.msg("|/Go forth warrior, equipped for battle.")
			return
		#catchall
		else:
			self.caller.msg("|/You're making no sense, I fear a madness may be upon you.")
			return
		return

class worldmagic(default_cmds.MuxCommand):
	key = "magic"
	def func(self):
		spelllist = ""
		if int(self.caller.db.mp) == 0:
			self.caller.msg("|/Your magic reserves are depleted.")
			return
		elif self.caller.db.overworldspells == []:
			self.caller.msg("|/You don't know any overworld magic.")
			return
		else:
			for i in self.caller.db.overworldspells:
				mlname = getattr(magic, i).name
				mlcost = str(getattr(magic, i).cost)
				spelllist = spelllist + mlname + " - " + mlcost + " MP" + "|/"
			magicanswer = yield("|/|005.|015:|025*|035~|nSpells|035~|025*|015:|005.|n|/%s|/Which spell?" % (spelllist))
			#figure out how to list the spells and cost
			if magicanswer.lower() not in self.caller.db.overworldspells:
				self.caller.msg("|/You do not know that spell or that spell cannot be used outside of battle.")
				return
			else:
				magicname = getattr(magic, magicanswer).name
				magiccost = getattr(magic, magicanswer).cost
				magicbase = getattr(magic, magicanswer).base
				magicgroup = getattr(magic, magicanswer).group
				magicphrase = getattr(magic, magicanswer).phrase
				if magiccost > self.caller.db.mp:
					self.caller.msg("|/Your magic reserves are too low for that spell.")
					return
				else:
					#heal spells
					if magicgroup == "heal":
						if self.caller.db.hp == self.caller.db.maxhp:
							self.caller.msg("|/You are already at full health.")
							return
						self.caller.db.mp -= magiccost
						self.caller.db.hp += magicbase
						if self.caller.db.hp > self.caller.db.maxhp:
							self.caller.db.hp = self.caller.db.maxhp
						self.caller.msg("|/%s|/You regain %d HP." % (magicphrase, magicbase))
						self.caller.msg("HP: %d of %d|/MP: %d of %d" % (self.caller.db.hp, self.caller.db.maxhp, self.caller.db.mp, self.caller.db.maxmp))
						return
					#travel
					elif magicname.lower() == "travel":
						if self.caller.location.tags.get("notravel"):
							self.caller.msg("|/Something is preventing you from traveling at this location.")
							return
						if not self.caller.db.locations:
							self.caller.msg("|/You have not learned any locations to travel to yet.")
							return
						else:
							possibleplaces = ', '.join(self.caller.db.locations).title()
							answer = yield("|/Where to?|/%s" % (possibleplaces))
							if answer.lower() not in (places.lower() for places in self.caller.db.locations):
								self.caller.msg("|/You do not know that location.")
								return
							else:
								self.caller.db.mp -= magiccost
								travelto = getattr(places, answer.replace(" ", "").lower()).location
								self.caller.db.lastcity = travelto
								self.caller.msg("|/You focus, concentrating on your memories of %s.|/The air shimmers and a portal opens, you step through." % (answer.lower().title()))
								self.caller.msg("|/ ")
								yield 2
								results = search_object(travelto)
								self.caller.move_to(results[0], quiet=True, move_hooks=True)
								return
					else:
						self.caller.msg("I'm not sure what happened, something went wrong.")

class talkNPC(default_cmds.MuxCommand):
	"""
	Talk to NPC's (non-playable characters).

	Usage:
	Talk <NPC Name>

	Checks if the NPC has something to say.
	Some NPC's might have more than just one thing to say,
	Try talking to them more than just once.
	"""
	key = "Talk"
	auto_help = True

	def parse(self):
		self.npcname = self.args.lstrip()

	def func(self):
		if not self.obj.access(self.caller, "view"):
			self.caller.msg("There's no one by that name to talk to.")
			return
		thiefphrases = ["What a wonderful day it is.", "Humm... full moon tonight, bad for business.", "Well hello there. I hope you're enjoying your time in our fair city. hehehehe.", "Oh, sweetie, you should get out of here right away.", "Welcome to Vak Dal!"]
		thiefdistractions = ["Oh!! LOOKOUT! BEHIND YOU!", "Have I ever shown you my KNIFE!!?", "Hi, I've been looking for you. Give me your money!", "Haha, sucker, you just got robbed!", "ha-HAAAA!!!!!", "You look rich, let's fix that.", "How about you give me some money? No? Ok, give me a lot of money!!", "A mugging I will go, a mugging I will go, hi, ho, the GIVE ME YOUR MONEY-O!!"]
		target = self.caller.search(self.npcname, quiet=True)
		if not target:
			self.caller.msg("|/There's no one here by that name to talk to.")
			return
		if target:
			target = target[0]
		if not target.tags.get("talkative", category="npc"):
			self.caller.msg("|r|/You're trying to talk to an inanimate object...|/Might be time to refill that prescription.|n")
			return
		if not target.access(self.caller, "view"):
			self.caller.msg("There's no one here by that name to talk to.")
			return
# Single
		elif target.tags.get("single", category="talkative"):
			if not target.db.msg:
				self.caller.msg("They don't appear to have anything to say.")
			else:
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.msg))
			return
# Multi
		elif target.tags.get("multi", category="talkative"):
			if not target.db.msg:
				self.caller.msg("They don't appear to have anything to say.")
			else:
				self.text = "%s" % random.choice(target.db.msg)
				self.caller.msg("|/|m%s|n says: %s" % (target.key, self.text))
			return
# If tag
		elif target.tags.get("tagnpc", category="talkative"):
			if self.caller.tags.get(target.db.tagname):
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.taggedresp))
			else:
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.untaggedresp))
			return
# Add tag
		elif target.tags.get("addtagnpc", category="talkative"):
			if not self.caller.tags.get(target.db.addtag):
				self.caller.tags.add(target.db.addtag)
			self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.msg))
#EvMenu
		elif target.tags.get("evm", category="talkative"):
			EvMenu(self.caller, "typeclasses.talking_spiceeasy", startnode="menu_start_node")
			return
#Sol Dhara Dead Folks
		elif target.tags.get("soldharanpc", category="talkative"):
			if not self.caller.tags.get("beginning"):
				self.caller.msg("|/Try as you might, the dead just won't respond do you.")
				return
			else:
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.msg))
			return
#Peasant Riot
		elif target.tags.get("peasantriot", category="talkative"):
			if self.caller.tags.get("folkhero") and not self.caller.tags.get("thekingisdead") and self.caller.search("Pitch Fork", candidates=self.caller.contents, quiet=True) and self.caller.search("Riot Sheet", candidates=self.caller.contents, quiet=True):
				targettwo = self.caller.search("Riot Sheet", candidates=self.caller.contents, quiet=True)
				if targettwo[0].db.count == 5:
					self.caller.msg("|/You've already gathered all the signatures needed.")
					return
				elif target.key in targettwo[0].db.story:
					self.caller.msg("|/|m%s|n says: I already signed the danged thing, quit bothering me!" % (target.key))
					return
				else:
					self.caller.msg("|/|m%s|n says: Hey, you maybe wanna overthrow the King and Queen?" % (self.caller.key))
					self.caller.msg("|m%s|n says: I think a revolt is exactly what this city needs! I'll sign up!" % (target.key))
					targettwo[0].db.story = targettwo[0].db.story + ". " + target.key
					targettwo[0].db.count += 1
					if targettwo[0].db.count == 5:
						self.caller.msg("|/You've gathered all the signatures needed!")
						return
					self.caller.msg("%s signs the sheet. You've gathered %d signatures." % (target.key, targettwo[0].db.count))
					return
			else:
				if self.caller.tags.get(target.db.tagname):
					self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.taggedresp))
				else:
					self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.untaggedresp))
				return
#Loyalist
		elif target.tags.get("loyalist", category="talkative"):
			if self.caller.tags.get("folkhero") and not self.caller.tags.get("thekingisdead") and self.caller.search("Pitch Fork", candidates=self.caller.contents, quiet=True) and self.caller.search("Riot Sheet", candidates=self.caller.contents, quiet=True):
				self.caller.msg("|/|m%s|n says: Hey, you maybe wanna overthrow the King and Queen?" % (self.caller.key))
				self.caller.msg("|m%s|n says: A REVOLT?!?!?! NEVER! I'm loyal to the King and Queen you treasonous peasant!! GUARDS!! GUARDS!!!" % (target.key))
				self.caller.msg("|mGuards|n say: What's all this then? A peasant revolt! Not on our watch!")
				self.caller.msg("You are dragged into the city center, kneeled down, and beheaded.")
				self.caller.msg("|/|rWhat tragic fate, you have died due to your own ineptitude.|n|/You have brought shame to yourself and your family.")
				self.caller.db.deathcount += 1
				self.caller.db.hp = int(self.caller.db.maxhp * .5)
				self.caller.db.mp = int(self.caller.db.maxmp * .5)
				self.caller.db.gold -= int(self.caller.db.gold * .2)
				results = search_object(self.caller.db.lastcity)
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				return
			else:
				if self.caller.tags.get(target.db.tagname):
					self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.taggedresp))
				else:
					self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.untaggedresp))
				return
#Thief
		elif target.tags.get("thief", category="talkative"):
			if self.caller.tags.get("kingofthieves"):
				self.caller.msg("|/|m%s|n says: Welcome back. The denizens of The Hooks are at your service." % (target.key))
				return
			luck = randint(1, 2)
			if luck == 1:
				if self.caller.db.gold < 100:
					self.caller.msg("|/|m%s|n says: Oh dear, you are just incredibly poor aren't you. Here, compliments of the local thieves. Take care of yourself." % (target.key))
					looted = randint(100, 2000)
					self.caller.db.gold += int(looted)
					self.caller.msg("You've been gifted %d gold from the local thieves." % (looted))
				else:
					looted = randint(1, int(self.caller.db.gold * .25))
					self.caller.db.gold -= int(looted)
					self.caller.msg("|/|m%s|n says: %s" % (target.key, random.choice(thiefdistractions)))
					self.caller.msg("You've been robbed for %d gold" % (looted))
					realbadluck = randint(1, 3)
					if realbadluck == 2:
						if self.caller.db.hp > 1:
							life = randint(1, int(self.caller.db.hp * .5))
							self.caller.db.hp -= life
							self.caller.msg("In addition to being robbed, you take %d damage in the assault." % (life))
					return
			if luck == 2:
				self.caller.msg("|/|m%s|n says: %s" % (target.key, random.choice(thiefphrases)))
				return
#Map NPC
		elif target.tags.get("mapnpc", category="talkative"):
			for i in self.caller.contents:
				if i.tags.get("map"):
					if i.db.locationname.lower() == target.db.locationname.lower():
						self.caller.msg("|/|m%s|n says: Oh, it looks like you've already got a map for %s. I don't have any other maps." % (target.key, target.db.locationname.title()))
						return
			self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.msg))
			self.caller.msg("%s hands you a map to %s." % (target.key, target.db.locationname.title()))
			map_proto = {
			"key": "%s Map" % (target.db.locationname.title()),
			"typeclass": "typeclasses.objects.%s" % target.db.mapname,
			"location": self.caller
			}
			spawn(map_proto)
			return
#Remove Tag NPC
		elif target.tags.get("remtagnpc", category="talkative"):
			if self.caller.tags.get(target.db.remtag):
				self.caller.tags.remove(target.db.remtag)
			self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.msg))
			return
#Accolade NPC
		elif target.tags.get("accoladenpc", category="talkative"):
			if target.db.accolade in self.caller.db.accolades:
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.accolademsg))
			else:
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.msg))
#Hellion NPC
		elif target.tags.get("hellion", category="talkative"):
			hellions = ["GET OUT!", "NO OUTSIDERS ALLOWED", "LEAVE NOW", "We are quite bitter beings and we stack the bodies high.", "Get out! This village is ours!", "You don't belong here!", "We don't want your kind around here!", "This is our home, not yours!", "You're not welcome here!", "Leave now, before it's too late!", "Stay away, or face the consequences!", "We won't let outsiders take what's rightfully ours!", "Go back where you came from!", "You have no business being here!"]
			self.caller.msg("|/|m%s|n growls: %s" % (target.key, random.choice(hellions)))
#Monster Defeated NPC
		elif target.tags.get("mondefnpc", category="talkative"):
			if not target.db.monstername in self.caller.attributes.get("monsterstats"):
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.msg))
				return
			elif self.caller.db.monsterstats[target.db.monstername]["killed"] < int(target.db.monsterqty):
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.msg))
				return
			elif self.caller.db.monsterstats[target.db.monstername]["killed"] >= int(target.db.monsterqty):
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.mondefmsg))
				return
#Quest NPC
		elif target.tags.get("questnpc", category="talkative"):
		#Player does not yet have quest.
			if not target.db.questname in self.caller.db.quests.keys():
				self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.msg))
				answer = yield("|/Will you accept this quest?|/|cY|nes|n, |cN|no")
				if answer.lower() in ["y", "yes"]:
					if target.db.questtype == "kill":
						if getattr(beastiary, target.db.questthingname).name.title() in self.caller.db.monsterstats.keys():
							requiredquantity = int(self.caller.db.monsterstats[getattr(beastiary, target.db.questthingname).name.title()]["killed"]) + int(target.db.questqty)
						else:
							requiredquantity = target.db.questqty
					if target.db.questtype == "get":
							requiredquantity = target.db.questqty
					self.caller.db.quests[target.db.questname] = {"giver": target.key, "location": target.location.key, "type": target.db.questtype, "thingname": target.db.questthingname, 'qty': requiredquantity, 'completed': 'no'}
					self.caller.msg("|/|m%s|n says: Thanks! Make sure to stop back when you're done." % (target.key))
					self.caller.msg("|/|gHOORAY! You've accepted a quest!!|n")
					return
				else:
					if not target.db.questturneddown == "":
						self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.questturneddown))
						return
					else:
						self.caller.msg("|/|m%s|n says: Well, if you change your mind, stop back." % (target.key))
						return
		#Quest is in progress or needs to be checked for completion
			elif self.caller.db.quests[target.db.questname]["completed"] == "no":
				if target.db.questtype == "kill":
					if not getattr(beastiary, target.db.questthingname).name.title() in self.caller.db.monsterstats.keys():
						if target.db.inprogmsg is None or target.db.inprogmsg == "":
							self.caller.msg("|/|m%s|n says: How's that quest coming along? Done yet? No? Well what are you waiting for?" % (target.key))
						else:
							self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.inprogmsg))
						return
					elif int(self.caller.db.monsterstats[getattr(beastiary, target.db.questthingname).name.title()]["killed"]) >= int(self.caller.db.quests[target.db.questname]["qty"]):
						self.caller.db.quests[target.db.questname]["completed"] = "yes"
						if target.db.successmsg is None or target.db.successmsg == "":
							self.caller.msg("|/|m%s|n says: Thanks for taking care of those %d %s for me." % (target.key, target.db.questqty, getattr(beastiary, target.db.questthingname).name.title()))
						else:
							self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.successmsg))
						self.caller.msg("|/|gHOORAY! You've completed a quest!!|n")
						#Give reward
						if target.db.rewardtype == "gold":
							self.caller.db.gold += target.db.rewardqty
							self.caller.msg("You get %d gold!" % (target.db.rewardqty))
							return
						elif target.db.rewardtype == "weapon":
							lootname = getattr(weapons, target.db.rewardthingname).name
							wt = self.caller.search(lootname, candidates=self.caller.contents, quiet=True)
							if wt:
								lootprofit = getattr(weapons, target.db.rewardthingname).price
								self.caller.db.gold += int(lootprofit)
								self.caller.msg("You get %d gold!" % int(lootprofit))
								return
							else:
								self.caller.msg("|m%s|n says: As a reward you get a %s!" % (target.key, lootname))
								sitc = "typeclasses.weapons.%s" % (target.db.rewardthingname)
								tc_proto = {
								"key": "%s" % (lootname),
								"typeclass": "%s" % (sitc),
								"location": self.caller
								}
								spawn(tc_proto)
								return
						elif target.db.rewardtype == "item":
							lootname = getattr(items, target.db.rewardthingname).name
							self.caller.msg("|m%s|n says: As a reward you get %d %s!" % (target.key, target.db.rewardqty, lootname))
							wt = self.caller.search(lootname, candidates=self.caller.contents, quiet=True)
							if not wt:
								sitc = "typeclasses.items.%s" % (target.db.rewardthingname)
								tc_proto = {
								"key": "%s" % (lootname),
								"typeclass": "%s" % (sitc),
								"qty": target.db.rewardqty,
								"location": self.caller
								}
								spawn(tc_proto)
								return
							else:
								wt[0].db.qty += target.db.rewardqty
								return
						elif target.db.rewardtype == "armor":
							lootname = getattr(armor, target.db.rewardthingname).name
							wt = self.caller.search(lootname, candidates=self.caller.contents, quiet=True)
							if wt:
								lootprofit = getattr(armor, target.db.rewardthingname).price
								self.caller.db.gold += int(lootprofit)
								self.caller.msg("You get %d gold!" % int(lootprofit))
								return
							else:
								self.caller.msg("|m%s|n says: As a reward you get a %s!" % (target.key, lootname))
								sitc = "typeclasses.armor.%s" % (target.db.rewardthingname)
								tc_proto = {
								"key": "%s" % (lootname),
								"typeclass": "%s" % (sitc),
								"location": self.caller
								}
								spawn(tc_proto)
								return
						return
					else:
						if target.db.inprogmsg is None or target.db.inprogmsg == "":
							self.caller.msg("|/|m%s|n says: How's that quest coming along? Done yet? No? Well what are you waiting for?" % (target.key))
							return
						else:
							self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.inprogmsg))
							return
				if target.db.questtype == "get":
					questitemname = getattr(items, target.db.questthingname).name
					wt = self.caller.search(questitemname, candidates=self.caller.contents, quiet=True)
					if not wt:
						if target.db.inprogmsg is None or target.db.inprogmsg == "":
							self.caller.msg("|/|m%s|n says: How's that quest coming along? Done yet? No? Well what are you waiting for?" % (target.key))
							return
						else:
							self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.inprogmsg))
							return
					elif wt[0].db.qty < target.db.questqty:
						if target.db.inprogmsg is None or target.db.inprogmsg == "":
							self.caller.msg("|/|m%s|n says: How's that quest coming along? Done yet? No? Well what are you waiting for?" % (target.key))
							return
						else:
							self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.inprogmsg))
							return
					elif wt[0].db.qty >= target.db.questqty:
						self.caller.db.quests[target.db.questname]["completed"] = "yes"
						wt[0].db.qty -= target.db.questqty
						if wt[0].db.qty <= 0:
							wt[0].delete()
						if target.db.successmsg is None or target.db.successmsg == "":
							self.caller.msg("|/|m%s|n says: Thanks for getting those %d %s for me!" % (target.key, target.db.questqty, getattr(items, target.db.questthingname).name.title()))
						else:
							self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.successmsg))
						self.caller.msg("|/|gHOORAY! You've completed a quest!!|n")
						#Give reward
						if target.db.rewardtype == "gold":
							self.caller.db.gold += target.db.rewardqty
							self.caller.msg("You get %d gold!" % (target.db.rewardqty))
							return
						elif target.db.rewardtype == "weapon":
							lootname = getattr(weapons, target.db.rewardthingname).name
							wt = self.caller.search(lootname, candidates=self.caller.contents, quiet=True)
							if wt:
								lootprofit = getattr(weapons, target.db.rewardthingname).price
								self.caller.db.gold += int(lootprofit)
								self.caller.msg("You get %d gold!" % int(lootprofit))
								return
							else:
								self.caller.msg("|m%s|n says: As a reward you get a %s!" % (target.key, lootname))
								sitc = "typeclasses.weapons.%s" % (target.db.rewardthingname)
								tc_proto = {
								"key": "%s" % (lootname),
								"typeclass": "%s" % (sitc),
								"location": self.caller
								}
								spawn(tc_proto)
								return
						elif target.db.rewardtype == "item":
							lootname = getattr(items, target.db.rewardthingname).name
							self.caller.msg("|m%s|n says: As a reward you get %d %s!" % (target.key, target.db.rewardqty, lootname))
							wt = self.caller.search(lootname, candidates=self.caller.contents, quiet=True)
							if not wt:
								sitc = "typeclasses.items.%s" % (target.db.rewardthingname)
								tc_proto = {
								"key": "%s" % (lootname),
								"typeclass": "%s" % (sitc),
								"qty": target.db.rewardqty,
								"location": self.caller
								}
								spawn(tc_proto)
								return
							else:
								wt[0].db.qty += target.db.rewardqty
								return
						elif target.db.rewardtype == "armor":
							lootname = getattr(armor, target.db.rewardthingname).name
							wt = self.caller.search(lootname, candidates=self.caller.contents, quiet=True)
							if wt:
								lootprofit = getattr(armor, target.db.rewardthingname).price
								self.caller.db.gold += int(lootprofit)
								self.caller.msg("You get %d gold!" % int(lootprofit))
								return
							else:
								self.caller.msg("|m%s|n says: As a reward you get a %s!" % (target.key, lootname))
								sitc = "typeclasses.armor.%s" % (target.db.rewardthingname)
								tc_proto = {
								"key": "%s" % (lootname),
								"typeclass": "%s" % (sitc),
								"location": self.caller
								}
								spawn(tc_proto)
								return
						return
				return
		#Player has completed quest.
			elif self.caller.db.quests[target.db.questname]["completed"] == "yes":
				if target.db.finishedmsg is None or target.db.finishedmsg == "":
					self.caller.msg("|/|m%s|n says: Thanks for taking care of that for me!" % (target.key))
					return
				else:
					self.caller.msg("|/|m%s|n says: %s" % (target.key, target.db.finishedmsg))
					return
			return
#Chicken Compass
		elif target.tags.get("chickencompass", category="talkative"):
			chicken = search_object("Chicken of Doom")
			self.caller.msg(chicken[0].location.key)
			self.caller.msg("|/|m%s|n: says: Bawk-buh-cauk? You seek the Chicken of DOOM? Well that's Eggcellent! Let's see if I can tune in to where our savior is currently." % (target.key))
			self.caller.msg("%s puts their head back and emits a mighty crow!" % (target.key))
			self.caller.msg("|m%s|n: says: Yes, yes, my comb tingles with chaotic energy..." % (target.key))
			if chicken[0].location.has_account:
				self.caller.msg("|/|m%s|n: says: The Chicken of Doom is currently with another member of the cult, spreading DOOOOOM!!!!!!" % (target.key))
			else:
				self.caller.msg("|/|m%s|n: says: Our savior of chaos is currently somewhere in %s." % (target.key, chicken[0].location.key))
			self.caller.msg("|m%s|n: says: I have great eggs-pectations from you. Good luck!!" % (target.key))
#catchall
		else:
			self.caller.msg("Hal0 fucked something up with an NPC, tell him to fix it.")
			return
			