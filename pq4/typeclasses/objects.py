"""
Object

The Object is the "naked" base class for things in the game world.

Note that the default Character, Room and Exit does not inherit from
this Object, but from their respective default implementations in the
evennia library. If you want to use this class as a parent to change
the other types, you can do so by adding this as a multiple
inheritance.

"""
from evennia import DefaultObject
import random
from random import randint

class Object(DefaultObject):
	"""
	This is the root typeclass object, implementing an in-game Evennia
	game object, such as having a location, being able to be
	manipulated or looked at, etc. If you create a new typeclass, it
	must always inherit from this object (or any of the other objects
	in this file, since they all actually inherit from BaseObject, as
	seen in src.object.objects).

	The BaseObject class implements several hooks tying into the game
	engine. By re-implementing these hooks you can control the
	system. You should never need to re-implement special Python
	methods, such as __init__ and especially never __getattribute__ and
	__setattr__ since these are used heavily by the typeclass system
	of Evennia and messing with them might well break things for you.


	* Base properties defined/available on all Objects

	 key (string) - name of object
	 name (string)- same as key
	 dbref (int, read-only) - unique #id-number. Also "id" can be used.
	 date_created (string) - time stamp of object creation

	 account (Account) - controlling account (if any, only set together with
					   sessid below)
	 sessid (int, read-only) - session id (if any, only set together with
					   account above). Use `sessions` handler to get the
					   Sessions directly.
	 location (Object) - current location. Is None if this is a room
	 home (Object) - safety start-location
	 has_account (bool, read-only)- will only return *connected* accounts
	 contents (list of Objects, read-only) - returns all objects inside this
					   object (including exits)
	 exits (list of Objects, read-only) - returns all exits from this
					   object, if any
	 destination (Object) - only set if this object is an exit.
	 is_superuser (bool, read-only) - True/False if this user is a superuser

	* Handlers available

	 aliases - alias-handler: use aliases.add/remove/get() to use.
	 permissions - permission-handler: use permissions.add/remove() to
				   add/remove new perms.
	 locks - lock-handler: use locks.add() to add new lock strings
	 scripts - script-handler. Add new scripts to object with scripts.add()
	 cmdset - cmdset-handler. Use cmdset.add() to add new cmdsets to object
	 nicks - nick-handler. New nicks with nicks.add().
	 sessions - sessions-handler. Get Sessions connected to this
				object with sessions.get()
	 attributes - attribute-handler. Use attributes.add/remove/get.
	 db - attribute-handler: Shortcut for attribute-handler. Store/retrieve
			database attributes using self.db.myattr=val, val=self.db.myattr
	 ndb - non-persistent attribute handler: same as db but does not create
			a database entry when storing data

	* Helper methods (see src.objects.objects.py for full headers)

	 search(ostring, global_search=False, attribute_name=None,
			 use_nicks=False, location=None, ignore_errors=False, account=False)
	 execute_cmd(raw_string)
	 msg(text=None, **kwargs)
	 msg_contents(message, exclude=None, from_obj=None, **kwargs)
	 move_to(destination, quiet=False, emit_to_obj=None, use_destination=True)
	 copy(new_key=None)
	 delete()
	 is_typeclass(typeclass, exact=False)
	 swap_typeclass(new_typeclass, clean_attributes=False, no_default=True)
	 access(accessing_obj, access_type='read', default=False)
	 check_permstring(permstring)

	* Hooks (these are class methods, so args should start with self):

	 basetype_setup()	 - only called once, used for behind-the-scenes
							setup. Normally not modified.
	 basetype_posthook_setup() - customization in basetype, after the object
							has been created; Normally not modified.

	 at_object_creation() - only called once, when object is first created.
							Object customizations go here.
	 at_object_delete() - called just before deleting an object. If returning
							False, deletion is aborted. Note that all objects
							inside a deleted object are automatically moved
							to their <home>, they don't need to be removed here.

	 at_init()			- called whenever typeclass is cached from memory,
							at least once every server restart/reload
	 at_cmdset_get(**kwargs) - this is called just before the command handler
							requests a cmdset from this object. The kwargs are
							not normally used unless the cmdset is created
							dynamically (see e.g. Exits).
	 at_pre_puppet(account)- (account-controlled objects only) called just
							before puppeting
	 at_post_puppet()	 - (account-controlled objects only) called just
							after completing connection account<->object
	 at_pre_unpuppet()	- (account-controlled objects only) called just
							before un-puppeting
	 at_post_unpuppet(account) - (account-controlled objects only) called just
							after disconnecting account<->object link
	 at_server_reload()   - called before server is reloaded
	 at_server_shutdown() - called just before server is fully shut down

	 at_access(result, accessing_obj, access_type) - called with the result
							of a lock access check on this object. Return value
							does not affect check result.

	 at_before_move(destination)			 - called just before moving object
						to the destination. If returns False, move is cancelled.
	 announce_move_from(destination)		 - called in old location, just
						before move, if obj.move_to() has quiet=False
	 announce_move_to(source_location)	   - called in new location, just
						after move, if obj.move_to() has quiet=False
	 at_after_move(source_location)		  - always called after a move has
						been successfully performed.
	 at_object_leave(obj, target_location)   - called when an object leaves
						this object in any fashion
	 at_object_receive(obj, source_location) - called when this object receives
						another object

	 at_traverse(traversing_object, source_loc) - (exit-objects only)
							  handles all moving across the exit, including
							  calling the other exit hooks. Use super() to retain
							  the default functionality.
	 at_after_traverse(traversing_object, source_location) - (exit-objects only)
							  called just after a traversal has happened.
	 at_failed_traverse(traversing_object)	  - (exit-objects only) called if
					   traversal fails and property err_traverse is not defined.

	 at_msg_receive(self, msg, from_obj=None, **kwargs) - called when a message
							 (via self.msg()) is sent to this obj.
							 If returns false, aborts send.
	 at_msg_send(self, msg, to_obj=None, **kwargs) - called when this objects
							 sends a message to someone via self.msg().

	 return_appearance(looker) - describes this object. Used by "look"
								 command by default
	 at_desc(looker=None)	  - called by 'look' whenever the
								 appearance is requested.
	 at_get(getter)			- called after object has been picked up.
								 Does not stop pickup.
	 at_drop(dropper)		  - called when this object has been dropped.
	 at_say(speaker, message)  - by default, called if an object inside this
								 object speaks

	 """

	pass
donttake = ["Hey, quit stealing shit!", "THIEF!!! THIEF!!!!", "In some countries they'd take your hand for stealing.", "CALL THE GUARDS!! THIEF!! THEY'RE RESISTING!!!", "You hear an ethereal voice... 'keep your hands off stuff you little shit.'", "You'd try to take the shirt off my back if I turned my head, wouldn't you.", "You'd try stealing someones grandma if she sat still long enough, wouldn't you.", "Good thing I bolted down the kitchen sink with you around eh.", "Thou shall not steal!!", "We hang thieves around here...", "Don't take things that aren't yours!", "You wanna get smited? I'll smite ya, prepare to get smote!!"]

class nogetobj(DefaultObject):
	def at_object_creation(self):
		self.locks.add("get:false()")
		self.db.desc = "."
		self.db.get_err_msg = "|r%s|n" % random.choice(donttake)

class addtagobj(DefaultObject):
	def at_object_creation(self):
		self.locks.add("get:false()")
		self.db.desc = ""
		self.db.tagname = "tagname"
		self.db.get_err_msg = "|r%s|n" % random.choice(donttake)
	def return_appearance(self, looker):
		if not looker:
			return ""
		desc = str(self.db.desc)
		if not looker.tags.get(self.db.tagname):
			looker.tags.add(self.db.tagname)
		return desc

class remtagobj(DefaultObject):
	def at_object_creation(self):
		self.locks.add("get:false()")
		self.db.desc = ""
		self.db.tagname = "tagnametoremove"
		self.db.tagremovemsg = ""
		self.db.get_err_msg = "|r%s|n" % random.choice(donttake)
	def return_appearance(self, looker):
		if not looker:
			return ""
		desc = str(self.db.desc)
		if looker.tags.get(self.db.tagname):
			looker.tags.remove(self.db.tagname)
			if self.db.tagremovemsg:
				desc = desc + "|/" + self.db.tagremovemsg
		return desc

class enigmaobj(DefaultObject):
	def at_object_creation(self):
		self.locks.add("get:false()")
		self.db.desc = ""
		self.db.enigmadesc = ""
		self.db.get_err_msg = "|r%s|n" % random.choice(donttake)
	def return_appearance(self, looker):
		if not looker:
			return ""
		contentslist = []
		for i in self.caller.contents:
			contentslist.append(i.key)
		if set(["Enigma Shield", "Enigma Weapon", "Enigma Armor"]).issubset(contentslist):
			desc = self.db.enigmadesc
		else:
			desc = self.db.desc
		return desc

class torch(DefaultObject):
	def at_object_creation(self):
		self.locks.add("drop:false()")
		self.db.desc = "A stinky torch glowing weakly."

class shovel(DefaultObject):
	def at_object_creation(self):
		self.locks.add("drop:false()")
		self.db.desc = "A sturdy shovel. Good for digging."

class glassflower(DefaultObject):
	def at_object_creation(self):
		self.locks.add("drop:false()")
		self.db.name = ""
		self.db.price = 0
		self.db.qty = 0
		self.db.desc = ""
	def return_appearance(self,looker):
		desc = str()
		desc = "|/"+ self.key + " - " + str(self.db.qty) + ". " + self.db.desc
		return desc

class tagviewobj(DefaultObject):
	def at_object_creation(self):
		self.locks.add("get:false()")
		self.db.desc = ""
		self.db.tagdesc = ""
		self.db.tagname = ""
		self.db.tagnametwo = ""
		self.db.get_err_msg = "|r%s|n" % random.choice(donttake)
	def return_appearance(self, looker):
		if not looker:
			return ""
		desc = str()
		if looker.tags.get(self.db.tagnametwo):
			looker.tags.remove(self.db.tagnametwo)
		if looker.tags.get(self.db.tagname):
			desc = self.db.tagdesc
		else:
			desc = self.db.desc
		return desc

class map(DefaultObject):
	def at_object_creation(self):
		self.locks.add("drop:false()")
		self.tags.add("map")
		self.db.desc = "."
		self.db.locationname = ""

class giosemap(DefaultObject):
	def at_object_creation(self):
		self.locks.add("drop:false()")
		self.tags.add("map")
		self.db.desc = "A map stamped onto thin steel. It looks to be made of old armor."
		self.db.locationname = "giose"

class madmap(DefaultObject):
	name = "Map to Madness"
	def at_object_creation(self):
		self.locks.add("drop:false()")
		self.tags.add("map")
		self.db.desc = "A map painted on a fragment of mirror, reflecting distorted images of twisted landscapes and lurking shadows."
		self.db.locationname = "islandofthemad"

class valaharranmap(DefaultObject):
	def at_object_creation(self):
		self.locks.add("drop:false()")
		self.tags.add("map")
		self.db.desc = "Valaharran Pirate Map."
		self.db.locationname = "magmamadness"

class panahonmap(DefaultObject):
	def at_object_creation(self):
		self.locks.add("drop:false()")
		self.tags.add("map")
		self.db.desc = "A small hourglass filled with sand. As you watch the sand flows from one side to the other to change the direction it points."
		self.db.locationname = "panahon"

class book(DefaultObject):
	def at_object_creation(self):
		self.tags.add("readable", category="isreadable")
		self.tags.add("single", category="isreadable")
		self.db.story = "Book Contents"
		self.locks.add("get:false()")
		self.db.desc = "It's a book, you might want to try and Read it."
		self.db.get_err_msg = "|rLeave the book alone or we will sic the librarians on you.|n"

class spellbook(DefaultObject):
	def at_object_creation(self):
		self.tags.add("readable", category="isreadable")
		self.tags.add("spellbook", category="isreadable")
		self.db.story = "Book Contents"
		self.db.spelldisplay = ""
		self.db.spell = ""
		self.locks.add("get:false()")
		self.db.desc = "It's a book, you might want to try and Read it."
		self.db.get_err_msg = "|rLeave the book alone or we will sic the librarians on you.|n"

class monsterjournal(DefaultObject):
	def at_object_creation(self):
		self.tags.add("readable", category="isreadable")
		self.tags.add("monsterjournal")
		self.locks.add("drop:false()")
		self.db.desc = "A journal that tracks your accomplishments vs monsters."

class rustysword(DefaultObject):
	def at_object_creation(self):
		self.locks.add("drop:false()")
		self.db.desc = "An old rusty sword with a black obsidian dragon head pommel."

class rustyarmor(DefaultObject):
	name = "Rusty Armor"
	def at_object_creation(self):
		self.locks.add("drop:false()")
		self.db.desc = "An old rusty set of armor with dragons engraved across the chest plate."

class bookshelf(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A bookshelf, it holds books."
		self.locks.add("get:false()")
		self.tags.add("bookshelf")
		self.db.get_err_msg = "|rIt's very heavy, you can't take it.|n"
	def return_appearance(self, looker):
		message = ""
		for o in self.contents:
			message += "|g%s|n - %s|/" % (o.key, o.db.desc)
		if message == "":
			looker.msg("The %s is empty" % (self.key))
		else:
			looker.msg("|/You look at the %s and see:" % (self.key))
			looker.msg(message)

class smallgodskey(DefaultObject):
	name = "Small Gods Key"
	def at_object_creation(self):
		self.db.desc = "A small but heavy iron key."
		self.locks.add("drop:false()")
		
class coin(DefaultObject):
	name = "Coin"
	def at_object_creation(self):
		self.db.desc = "A small gold coin."
		self.db.chargeddesc = "A small gold coin, glowing with luck."
		self.db.charged = "no"
		self.locks.add("drop:false()")
	def return_appearance(self, looker):
		if self.db.charged == "no":
			desc = self.db.desc
		if self.db.charged == "yes":
			desc = self.db.chargeddesc
		looker.msg(desc)

class horseshoe(DefaultObject):
	name = "Horseshoe"
	def at_object_creation(self):
		self.db.desc = "A well-made, but dull, horseshoe."
		self.db.chargeddesc = "A well-made horseshoe glowing with luck."
		self.db.charged = "no"
		self.locks.add("drop:false()")
	def return_appearance(self, looker):
		if self.db.charged == "no":
			desc = self.db.desc
		if self.db.charged == "yes":
			desc = self.db.chargeddesc
		looker.msg(desc)

class chest(DefaultObject):
	def at_object_creation(self):
		self.db.chestid = randint(10000000, 99999999)
		self.tags.add("treasurechest")
		self.db.loottype = ["gold", "weapon", "armor", "item", "genericitem", "book", "monster"]
		self.db.goldloot = []
		self.db.weaponloot = []
		self.db.armorloot = []
		self.db.itemloot = []
		self.db.genericitem = []
		self.db.bookloot = []
		self.db.desc = "A treasure chest."
		self.db.looteddesc = "|/It's empty."
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|rWhoa there, no need to take the whole thing.|n"
	def return_appearance(self, looker):
		if not looker:
			return ""
		if self.db.chestid in looker.db.chests:
			desc = self.db.looteddesc
		else:
			desc = self.db.desc
		return desc

#Locked UNLESS a player has a tag
class tagchest(chest):
	def at_object_creation(self):
		self.db.chestid = randint(10000000, 99999999)
		self.tags.add("treasurechest")
		self.tags.add("tagchest")
		self.db.lockedtagname = ""
		self.db.loottype = ["gold", "weapon", "armor", "item", "genericitem", "book", "monster"]
		self.db.goldloot = []
		self.db.weaponloot = []
		self.db.armorloot = []
		self.db.itemloot = []
		self.db.genericitem = []
		self.db.bookloot = []
		self.db.lockedmsg = "It appears to be locked somehow."
		self.db.desc = "A treasure chest."
		self.db.looteddesc = "|/It's empty."
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|rWhoa there, no need to take the whole thing.|n"

#Locked WHILE a player has a tag
class nottagchest(chest):
	def at_object_creation(self):
		self.db.chestid = randint(10000000, 99999999)
		self.tags.add("treasurechest")
		self.tags.add("nottagchest")
		self.db.lockedtagname = ""
		self.db.loottype = ["gold", "weapon", "armor", "item", "genericitem", "book", "monster"]
		self.db.goldloot = []
		self.db.weaponloot = []
		self.db.armorloot = []
		self.db.itemloot = []
		self.db.genericitem = []
		self.db.bookloot = []
		self.db.lockedmsg = "It appears to be locked somehow."
		self.db.desc = "A treasure chest."
		self.db.looteddesc = "|/It's empty."
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|rWhoa there, no need to take the whole thing.|n"

class holdschest(chest):
	def at_object_creation(self):
		self.db.chestid = randint(10000000, 99999999)
		self.tags.add("treasurechest")
		self.tags.add("holdschest")
		self.db.holdsitemname = ""
		self.db.loottype = ["gold", "weapon", "armor", "item", "genericitem", "book", "monster"]
		self.db.goldloot = []
		self.db.weaponloot = []
		self.db.armorloot = []
		self.db.itemloot = []
		self.db.genericitem = []
		self.db.bookloot = []
		self.db.lockedmsg = "It appears to be locked somehow."
		self.db.desc = "A treasure chest."
		self.db.looteddesc = "|/It's empty."
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|rWhoa there, no need to take the whole thing.|n"

class mondefchest(chest):
	def at_object_creation(self):
		self.db.chestid = randint(10000000, 99999999)
		self.tags.add("treasurechest")
		self.tags.add("defeatedchest")
		self.db.defeatedmonstername = ""
		self.db.qtydefeated = ""
		self.db.loottype = ["gold", "weapon", "armor", "item", "genericitem", "book", "monster"]
		self.db.goldloot = []
		self.db.weaponloot = []
		self.db.armorloot = []
		self.db.itemloot = []
		self.db.genericitem = []
		self.db.bookloot = []
		self.db.lockedmsg = "It appears to be locked somehow."
		self.db.desc = "A treasure chest."
		self.db.looteddesc = "|/It's empty."
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|rWhoa there, no need to take the whole thing.|n"

class goldchest(chest):
	def at_object_creation(self):
		self.db.chestid = randint(10000000, 99999999)
		self.tags.add("treasurechest")
		self.db.loottype = ["gold"]
		self.db.goldloot = ["10", "45", "63", "78"]
		self.db.desc = "A treasure chest."
		self.db.looteddesc = "|/It's empty."
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|rWhoa there, no need to take the whole thing.|n"

class weaponchest(chest):
	def at_object_creation(self):
		self.db.chestid = randint(10000000, 99999999)
		self.tags.add("treasurechest")
		self.db.loottype = ["weapon"]
		self.db.weaponloot = []
		self.db.desc = "A treasure chest."
		self.db.looteddesc = "|/It's empty."
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|rWhoa there, no need to take the whole thing.|n"

class armorchest(chest):
	def at_object_creation(self):
		self.db.chestid = randint(10000000, 99999999)
		self.tags.add("treasurechest")
		self.db.loottype = ["armor"]
		self.db.armorloot = []
		self.db.desc = "A treasure chest."
		self.db.looteddesc = "|/It's empty."
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|rWhoa there, no need to take the whole thing.|n"

class itemchest(chest):
	def at_object_creation(self):
		self.db.chestid = randint(10000000, 99999999)
		self.tags.add("treasurechest")
		self.db.loottype = ["item"]
		self.db.itemloot = []
		self.db.desc = "A treasure chest."
		self.db.looteddesc = "|/It's empty."
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|rWhoa there, no need to take the whole thing.|n"

class genericitemchest(chest):
	def at_object_creation(self):
		self.db.chestid = randint(10000000, 99999999)
		self.tags.add("treasurechest")
		self.db.loottype = ["genericitem"]
		self.db.genericitem = []
		self.db.desc = "A treasure chest."
		self.db.looteddesc = "|/It's empty."
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|rWhoa there, no need to take the whole thing.|n"

class bookchest(chest):
	def at_object_creation(self):
		self.db.chestid = randint(10000000, 99999999)
		self.tags.add("treasurechest")
		self.db.loottype = ["book"]
		self.db.bookloot = []
		self.db.desc = "A treasure chest."
		self.db.looteddesc = "|/It's empty."
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|rWhoa there, no need to take the whole thing.|n"

class monsterchest(chest):
	def at_object_creation(self):
		self.db.chestid = randint(10000000, 99999999)
		self.tags.add("treasurechest")
		self.db.loottype = ["monster"]
		self.db.desc = "A treasure chest."
		self.db.looteddesc = "|/It's empty."
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|rWhoa there, no need to take the whole thing.|n"

class lefteye(DefaultObject):
	def at_object_creation(self):
		self.locks.add("drop:false()")
		self.db.desc = "The Left Eye of the Blind God."

class righteye(DefaultObject):
	def at_object_creation(self):
		self.locks.add("drop:false()")
		self.db.desc = "The Right Eye of the Blind God."

class centereye(DefaultObject):
	def at_object_creation(self):
		self.locks.add("drop:false()")
		self.db.desc = "The Center Eye of the Blind God."