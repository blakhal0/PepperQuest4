"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom, search_object, utils
from random import randint
import random


class Room(DefaultRoom):
	"""
	Rooms are like any Object, except their location is None
	(which is default). They also use basetype_setup() to
	add locks so they cannot be puppeted or picked up.
	(to change that, use at_object_creation instead)

	See examples/object.py for a list of
	properties and methods available on all Objects.
	"""

	pass

class vroom(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "A normal room"
		self.db.fight = "no"
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination and not con.tags.get("specialobject"):
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class mirrorroom(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "You find yourself surrounded by an uncanny symmetry. The paths ahead seem to lead in multiple directions simultaneously, and the reflections of the mirrored walls create an illusion of infinite corridors. Every step you take is met with its mirrored counterpart, causing a disorienting sensation as you try to distinguish between what is real, and what is a reflection. The mirror images create a mesmerizing visual spectacle. The play of light and shadow, the intricate patterns and reflections, create a surreal ambiance. It's as if the very essence of this strange place is alive, shifting and twisting with every movement."
		self.db.fight = "yes"
		self.db.zone = "mirrorzone"
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination and not con.tags.get("specialobject") and not con.tags.get("specialexit"):
				if looker.is_superuser or looker.tags.get("normalview"):
					exits.append(key)
				else:
					exits.append("rorrim")
			elif con.tags.get("specialexit"):
				if looker.is_superuser or looker.tags.get("normalview"):
					exits.append(key)
				else:
					exits.append("".join(reversed(key)))
			elif con.tags.get("specialnpc"):
				if looker.is_superuser or looker.tags.get("normalview"):
					npc.append(key)
				else:
					npc.append("".join(reversed(key)))
			elif con.permissions.get("player"):
				if con.has_account:
					if looker.is_superuser or looker.tags.get("normalview"):
						users.append(key)
					else:
						users.append("".join(reversed(key)))
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					if looker.is_superuser or looker.tags.get("normalview"):
						npc.append(key)
					else:
						npc.append("".join(reversed(key)))
				else:
					if looker.is_superuser or looker.tags.get("normalview"):
						things.append(key)
					else:
						things.append("".join(reversed(key)))
			elif con.tags.get("evnpc"):
				if looker.is_superuser or looker.tags.get("normalview"):
					npc.append(key)
				else:
					npc.append("".join(reversed(key)))
			else:
				if looker.is_superuser or looker.tags.get("normalview"):
					things.append(key)
				else:
					things.append("".join(reversed(key)))
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if looker.is_superuser or looker.tags.get("normalview"):
			desc = self.db.desc
		else:
			desc = "".join(reversed(self.db.desc))
		if desc:
			string += "%s" % desc
			string += "\n\n"
			if looker.is_superuser or looker.tags.get("normalview"):
				string += "You cast your gaze upon the area:"
			else:
				string += "".join(reversed("You cast your gaze upon the area:"))
		if exits:
			if looker.is_superuser or looker.tags.get("normalview"):
				string += "\n|025Exits|n: " + ", ".join(exits)
			else:
				string += "\n" + ", ".join(exits) + "|025 :stixE|n"
		if users:
			if looker.is_superuser or looker.tags.get("normalview"):
				string += "\n|550Players|n: " + ", ".join(users)
			else:
				string += "\n" + ", ".join(users) + "|550 :sreyalP|n"
		if npc:
			if looker.is_superuser or looker.tags.get("normalview"):
				string += "\n|520NPC's|n: " + ", ".join(npc)
			else:
				string += "\n" + ", ".join(npc) + "|520 :s'CPN|n "
		if things:
			if looker.is_superuser or looker.tags.get("normalview"):
				string += "\n|050Objects|n: " + ", ".join(things)
			else:
				string += "\n" + ", ".join(things) + "|050 :stcejbO|n"
		return string

class ifholdsview(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "You don't have a thing."
		self.db.holdsdesc = "You've got a thing."
		self.db.itemname = ""
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if looker.search(self.db.itemname, candidates=looker.contents, quiet=True):
			desc = self.db.holdsdesc
		else:
			desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

#conditional rooms
class singleplayerroom(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "A normal room"
		self.db.fight = "no"
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class iftagviewnf(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "You do not have a tag description."
		self.db.tagdesc = "You have a tag description."
		self.db.tagname = "test"
		self.db.fight = "no"
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if looker.tags.get(self.db.tagname):
			desc = self.db.tagdesc
		else:
			desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class ifaccolade(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "You don't have an accolade."
		self.db.hasaccoladedesc = "You've got an accolade."
		self.db.accolade = ""
		self.db.fight = "no"
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if self.db.accolade in looker.db.accolades:
			desc = self.db.hasaccoladedesc
		else:
			desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class twotagviewnf(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "You do not have a tag description."
		self.db.tagdesc = "You have a tag description."
		self.db.tagtwodesc = "You have tag2 description."
		self.db.tagname = "test"
		self.db.tagtwoname = "test"
		self.db.fight = "no"
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if looker.tags.get(self.db.tagname):
			desc = self.db.tagdesc
		elif looker.tags.get(self.db.tagtwoname):
			desc = self.db.tagtwodesc
		else:
			desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class ifnottagviewnf(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "You have a tag description."
		self.db.nottagdesc = "You do not have a tag description"
		self.db.tagname = "test"
		self.db.fight = "no"
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if not looker.tags.get(self.db.tagname):
			desc = self.db.nottagdesc
		else:
			desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class iftagviewfight(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "You do not have a tag description."
		self.db.tagdesc = "You have a tag description."
		self.db.tagname = "test"
		self.db.zone = ""
		self.db.fight = "yes"
		self.tags.add("autofight")
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if looker.tags.get(self.db.tagname):
			desc = self.db.tagdesc
		else:
			desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string
	def at_object_receive(self, character, source_location):
		if not character.permissions.get("player"):
			return
		chance = randint(1, 3)
		if chance == 2:
			character.tags.add("letsfight")
			character.execute_cmd('fight')
		else:
			character.execute_cmd('look')

class ifnottagviewfight(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "You have a tag description"
		self.db.nottagdesc = "You do not have a tag description"
		self.db.tagname = ""
		self.db.zone = ""
		self.db.fight = "yes"
		self.tags.add("autofight")
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if not looker.tags.get(self.db.tagname):
			desc = self.db.nottagdesc
		else:
			desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string
	def at_object_receive(self, character, source_location):
		if not character.permissions.get("player"):
			return
		chance = randint(1, 3)
		if chance == 2:
			character.tags.add("letsfight")
			character.execute_cmd('fight')
		else:
			character.execute_cmd('look')

class ifholdsviewnf(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "You don't have a thing."
		self.db.holdsdesc = "You've got a thing."
		self.db.itemname = ""
		self.db.fight = "no"
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if looker.search(self.db.itemname, candidates=looker.contents, quiet=True):
			desc = self.db.holdsdesc
		else:
			desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class ifholdsviewnfnt(DefaultRoom):
	def at_object_creation(self):
		self.tags.add("notravel")
		self.db.desc = "You don't have a thing."
		self.db.holdsdesc = "You've got a thing."
		self.db.itemname = ""
		self.db.fight = "no"
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if looker.search(self.db.itemname, candidates=looker.contents, quiet=True):
			desc = self.db.holdsdesc
		else:
			desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class ifholdsviewfight(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "You don't have a thing."
		self.db.holdsdesc = "You've got a thing."
		self.db.itemname = ""
		self.db.zone = ""
		self.db.fight = "yes"
		self.tags.add("autofight")
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if looker.search(self.db.itemname, candidates=looker.contents, quiet=True):
			desc = self.db.holdsdesc
		else:
			desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string
	def at_object_receive(self, character, source_location):
		if not character.permissions.get("player"):
			return
		chance = randint(1, 3)
		if chance == 2:
			character.tags.add("letsfight")
			character.execute_cmd('fight')
		else:
			character.execute_cmd('look')

class notravelroom(vroom):
	def at_object_creation(self):
		self.db.desc = "desc."
		self.tags.add("notravel")

class nofightroom(vroom):
	def at_object_creation(self):
		self.db.desc = "desc."
		self.db.fight = "no"

class nofightnotravel(vroom):
	def at_object_creation(self):
		self.db.desc = "desc."
		self.db.fight = "no"
		self.tags.add("notravel")

class ifmonsterdefeatedview(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "You have not defeated the specific monster."
		self.db.defeateddesc = "You have defeated the specific monster."
		self.db.monstername = ""
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if self.db.monstername in looker.db.monsterstats.keys():
			if looker.db.monsterstats[self.db.monstername]["killed"] >= 1:
				desc = self.db.defeateddesc
			else:
				desc = self.db.desc
		else:
			desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string


class moveroom(vroom):
	def at_object_creation(self):
		self.db.desc = ""
		self.db.sendlocation = "#"
		self.db.warning = ""
		self.db.movemsg = ""
	def at_object_receive(self, obj, source):
		utils.delay(2, self.sendmsg, obj)
	def sendmsg(self, obj):
		if not self.db.sendlocation:
			obj.msg("No Send To room assigned yet. Tell hal0 to fix this.")
			return
		for i in self.contents:
			if i.has_account and i.key == obj.key:
				obj.msg(self.db.warning)
				utils.delay(4, self.move, obj)
	def move(self, obj):
		for i in self.contents:
			if i.has_account and i.key == obj.key:
				destination = search_object(self.db.sendlocation)
				obj.msg(self.db.movemsg)
				obj.move_to(destination[0], quiet=False, move_hooks=True)

class killerplantroom(vroom):
	def at_object_creation(self):
		self.db.desc = "The air carries a pungent scent of sweet flowers and rotting meat. Grotesque flora sprawls in tangled masses, their vibrant hues distorted into sickly shades of deep green and darkly vibrant violet. Thorned vines snake through the undergrowth, their serpentine embrace serving as both warning and entrapment. Clumps of glowing eyes stare at you from the forest, not just sets of eyes, but clustered multitudes."
		self.db.entangled = "|/|rThorned vines snake around your legs, entangling you.|n|/The vines constrict and twist, digging into your skin, feeding on your blood."
		self.db.fight = "no"
		self.tags.add("notravel")
	def at_object_receive(self, obj, source):
		obj.tags.add("nomove")
		utils.delay(1, self.sendmsg, obj)
	def sendmsg(self, obj):
		for i in self.contents:
			if i.has_account and i.key == obj.key:
				obj.msg(self.db.entangled)
				quantity = randint(1,6)
				damage = 0
				while 0 < quantity:
					damage += randint(5,10)
					quantity -= 1
				obj.db.hp -= damage
				if obj.db.hp <= 0:
					obj.msg("|/You take %d damage" % damage)
					obj.tags.remove("nomove")
					obj.msg("|/|rWhat tragic fate, you have been consumed by the maddening jungle.|n|/You have brought shame to yourself and your family.|n")
					obj.db.deathcount += 1
					obj.db.hp = int(obj.db.maxhp * .5)
					obj.db.mp = int(obj.db.maxmp * .5)
					obj.db.gold -= int(obj.db.gold * .3)
					results = search_object(obj.db.lastcity)
					obj.move_to(results[0], quiet=True, move_hooks=False)
				else:
					obj.tags.remove("nomove")
					obj.msg("|/You take %d damage before finally breaking free." % damage)

#Islands
class giose(vroom):
	def at_object_creation(self):
		self.db.desc = "Gentle winds carry the roar of the crowd from the arena. A beautiful isle, with a thirst for violence.|/The palm trees sway under a clear blue sky, white sand gives gently under foot as you make your way."
		self.db.fight = "no"
		self.tags.add("notravel")

#Cities
class soldhara(iftagviewnf):
	def at_object_creation(self):
		self.db.desc = "Smoke and rancid meat, the retched smell of war, assaults your senses.|/Piles of ash where the huts once stood, bloated rotting corpses bob in the lake stripped to the bone where the crabs and fish have been feasting.|/The once verdant village full of life and golden light is gone, replaced with this charnel house."
		self.db.tagdesc = "The sleepy village buzzes with the usual sounds as people go about their day.|/Palm frond thatched huts cluster along the east and west sides of the village.|/Laughter drifts on the wind as people work cleaning fish and preparing fruit and vegetables near the lake in the center of the village.|/The sun shines down from the sky, chasing away the morning mists and bathing everything in beautiful golden light."
		self.db.tagname = "beginning"
		self.db.fight = "no"

class playerhut(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "Bloody streaks and splatters cover what little isn't burnt. Flies buzz in swarms around your head."
		self.db.tagdesc = "A tidy round palm frond hut, quite suitable for a small family.|/A gentle warm breeze flutters reed shades covering the windows."
		self.db.tagname = "beginning"
		self.db.fight = "no"
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if looker.tags.get(self.db.tagname):
			desc = self.db.tagdesc
		else:
			desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class soldharahut(iftagviewnf):
	def at_object_creation(self):
		self.db.desc = "Bloody streaks and splatters cover what little isn't burnt. Flies buzz in swarms around your head."
		self.db.tagdesc = "A tidy round palm frond hut, quite suitable for a small family.|/A gentle warm breeze flutters reed shades covering the windows."
		self.db.tagname = "beginning"
		self.db.fight = "no"

class fennimore(vroom):
	def at_object_creation(self):
		self.db.desc = "A gentle sound of dull bells clinking create a low murmur.|/Fennimore is barely more than a main thoroughfare, some houses, and spotted cows grazing at their leisure."
		self.db.fight = "no"

class gadoz(vroom):
	def at_object_creation(self):
		self.db.desc = "A gentle breeze blows through the port town.|/Stone houses with tiled roofs tower two and three stories into the air. Merchants houses, obviously.|/Sailors stride through the streets purposefully, either eager to get back out to sea or to spend the gold they just earned."
		self.db.fight = "no"

class gadozdocks(vroom):
	def at_object_creation(self):
		self.db.desc = "Seabirds circle overhead crying their screeching song, searching for a forgotten fish to flop onto the decks of the boats.|/Sailors holler back and forth as crates are hauled on and off of trading ships.|/Fat well dressed merchants haggle with the captains, complaining that the captains are trying to take the food right out of their children's mouths.|/A briny, fishy smell permeates the air."
		self.db.fight = "no"

class gadozmerchanthouse(vroom):
	def at_object_creation(self):
		self.db.desc = "An extravagantly decorated house, the telltale sign of a merchant.|/Excess surrounds you. Rare items displayed on pedestals. Cabinets of fine porcelain line the walls."
		self.db.fight = "no"

class sailorhouse(vroom):
	def at_object_creation(self):
		self.db.desc = "A simple house, for a hard working and simple sailor.|/It is neat and tidy with few extravagances."
		self.db.fight = "no"

class paipricity(iftagviewnf):
	def at_object_creation(self):
		self.db.desc = "The city has a deafening silence. A low buzz that seems to reverberate and intensify.|/The occasional head pokes out of a side street, looks, then darts across the street.|/Refuse is piled on the street sides."
		self.db.tagdesc = "The city bustles with life. People greet each other warmly as they pass, children laugh and play.|/The streets are clean with guards present, but apparently not needed."
		self.db.tagname = "thekingisdead"
		self.db.fight = "no"

class paipriprisoncell(vroom):
	def at_object_creation(self):
		self.db.desc = "Dark to near blackness and cramped with a stench that burns the nostrils, Paipri's prison is a terrible place.|/The cell is not tall enough to stand up, and jagged stone ceilings waiting to tear at the head of anyone that tries.|/The floors, forever verging on wet, have been worn smooth by hundreds of years of the previous tenants."
		self.db.fight = "no"
		self.tags.add("notravel")

class paipriprisonhall(vroom):
	def at_object_creation(self):
		self.db.desc = "The prison hallway is dimly lit by, from the smell one would guess, goat scat fueled torches. Paipri's prison is a terrible place.|/Thick wooden doors muffle the wails of the prisoners."
		self.db.fight = "no"
		self.tags.add("notravel")

class castlerika(vroom):
	def at_object_creation(self):
		self.db.desc = "The castle is the very embodiment of opulence.|/Statues and tapestries, fancies and curiosities, battle armor from past rulers.|/Servants scurry past, some transporting food or drink, some stopping to polish anything they find to be less than gleaming."
		self.db.fight = "no"

class prisonsewer(ifholdsviewnfnt):
	def at_object_creation(self):
		self.tags.add("notravel")
		self.db.desc = "You can't see anything, you can only hear the sloshing of your feet in the muck."
		self.db.holdsdesc = "The dim light of the torch lets you see reasonably well in the pitch black dark."
		self.db.itemname = "Torch"
		self.db.fight = "no"

class okefen(vroom):
	def at_object_creation(self):
		self.db.desc = "Long, stringy clumps of moss hang from the gnarled tree branches.|/Okefen is a very modest village, not without its charm. That charm is just hard to see through the humidity and constant barrage of biting bugs."
		self.db.fight = "no"

pickpocketedmsg = ["A scraggly stranger bumps into you.", "A small child stares up at you with big eyes and a dirty face, then stabs you in the leg.", "|mRandom Person|n says: Hey, could you spare some stuff?", "|mThief|n says: Oh, let me help you with that..."]
class vakdalhooks(vroom):
	def at_object_creation(self):
		self.db.desc = "The Hooks is dark and dirty. Not only caused by soot from the kiln fires in Glass Alley blanketing everything in black, but the buildings themselves are packed close and tall, blocking out any sunlight.|/Even during the day, The Hooks is a dangerous place, inhabited by every species of thief and assassin.|/Racking coughs are the ambient city sound through the shadowed, narrow, twisting alleyways periodically disrupted by very brief yelps of robbery victims."
		self.db.fight = "no"
	def at_object_receive(self, character, source_location):
		lootopts = ["gold", "item", "life"]
		if character.tags.get("mugable"):
			return
		chance = randint(1, 2)
		if chance == 1:
			if character.tags.get("kingofthieves"):
				character.msg("|/The gathered denizens of The Hooks give you a slight nod as you pass and move to clear your path.")
				return
			character.msg("|/|/" + random.choice(pickpocketedmsg))
			lost = random.choice(lootopts)
			if lost == "gold" and character.db.gold > 10:
				lootedgold = randint(1, int(character.db.gold * .25))
				character.db.gold -= int(lootedgold)
				character.msg("|rYOU'VE BEEN ROBBED!!|/You lose %d gold.|n" % (lootedgold))
				return
			elif lost == "item":
				itemopts = ["Spicy Herb", "Magic Dust", "Faster Feather"]
				lostitem = random.choice(itemopts)
				target = character.search(lostitem, candidates=character.contents, quiet=True)
				if not target:
					character.msg("|gYou quickly check you inventory, luckily nothing was taken.|n")
					return
				else:
					target[0].db.qty -= 1
					if target[0].db.qty <= 0:
						target[0].delete()
					character.msg("|rYOU'VE BEEN ROBBED!!|/You quickly check you inventory, you notice that a %s is missing.|n" % (lostitem))
					return
			elif lost == "life":
				if character.db.hp > 1:
					lootedlife = randint(1, int(character.db.hp * .25))
					character.db.hp -= int(lootedlife)
					character.msg("|rYOU'VE BEEN STABBED!!|/You notice you're bleeding, you lose %d hp.|n" % (lootedlife))
					return
				else:
					character.msg("|gYou luckily escape the attempted robbery unharmed.|n")
					return
		else:
			return

class vakdalglass(vroom):
	def at_object_creation(self):
		self.db.desc = "Heat dances on the air from the blazing fires in the glass kilns. Glass Alley rises on a hill, gradually, to the South bringing some small relief from the coastal breezes and carrying away the soot from the fires.|/Measured overlapping whooshes from the shop billows sound a promise of horrendous storms that never arrive."
		self.db.fight = "no"

class vakdalcitycenter(iftagviewnf):
	def at_object_creation(self):
		self.db.desc = "The masses of people flood through the streets heading to the city center to watch the execution.|/While less crowded than the gates, what little open area is left is quickly becoming filled with the spectators.|/Central Road travels east into the City Center and west to the gates out of town."
		self.db.tagdesc = "With the execution over, the city seems nearly empty. The streets still bustle and buzz with merchants and workers going about their day.|/Central Road travels east into the City Center and west to the gates out of town."
		self.db.tagname = "ladrone"
		self.db.fight = "no"

class vakdaliftag(iftagviewnf):
	def at_object_creation(self):
		self.db.desc = "You do not have a tag description."
		self.db.tagdesc = "You have a tag description."
		self.db.tagname = "ladrone"
		self.db.fight = "no"

class vakdalmarket(vroom):
	def at_object_creation(self):
		self.db.desc = "The Market District humms with activity. Coins of all shapes and sizes change hands as every possible type of good is traded and bought.|/The aristocracy of Vak Dal take their leisure looking at the various goods. A feel of fabric here, holding a jeweled ring up to see the stone catch the light, admiring glasswork while trying to find a single imperfection to drive down the asking price."
		self.db.fight = "no"

class vakdalupper(vroom):
	def at_object_creation(self):
		self.db.desc = "Tall white stone houses stab up at the sky, surrounded by gardens of colorful and sweet smelling flowers and fruit trees. Mosaic colored glass windows showing scenes, displaying family monograms, or intricate designs stand out from the smooth white stone.|/Workers on the lower rings of the Upper District labor relentlessly cleaning the houses of the ash and soot that manages to find its way there from Glass Alley as the Aristocracy meanders through the cobbled streets twirling umbrellas overhead."
		self.db.fight = "no"

class vakdalmansion(vroom):
	def at_object_creation(self):
		self.db.desc = ""
		self.db.fight = "no"

class baccami(ifaccolade):
	def at_object_creation(self):
		self.db.desc = "The 'Gem of the Desert' is more like a piece of coal. Baccami looks like it's been looted, several times, by large and greedy armies.|/Large columns stand in the middle of open areas used to hold statues by your guess. Little remains except jagged footings.|/The few buildings are stripped bare, windows missing glass and doors that were taken right off the hinges make grim faces on the houses.|/The few occupants of the city you see wear rags over thin bony bodies and scurry from place to place."
		self.db.hasaccoladedesc = "The 'Gem of the Desert' shines and sparkles.|/Golden statues stand atop marble columns depicting symbols of luck and good fortune.|/White alabaster houses and buildings stand adorned with colored patterns scrolling along the edges and circling the sturdy shudders and brass doors.|/Stylish, yet temperature minded, clothing is the fashion here and fashionable it is. Rings and necklaces, bracelets and bangles shimmer and shine as the residents and visitors pass by enjoying the beauty of the city."
		self.db.fight = "no"
		self.db.accolade = "Fortunate One"

class gpcasino(ifaccolade):
	def at_object_creation(self):
		self.db.desc = "The casino has all the joy and excitement of a funeral. There are quiet sobs and tortured screams occasionally.|/The sound of clicking slot machine reels fill the air like locusts.|/|/The casino is a study in gold and marble. Statues, pillars, fountains, and grand crystal chandeliers.|/Despite drowning in luxury, you feel an immense sense of dread."
		self.db.hasaccoladedesc = "Jackpot bells ring, excited screams and yells burst out and are quickly swallowed by the next round of bells and exclamations.|/The casino is a study in gold and marble. Statues, pillars, fountains, and grand crystal chandeliers. You feel like royalty just being here."
		self.db.fight = "no"
		self.tags.add = "notravel"
		self.db.accolade = "Fortunate One"

class oasismaze(vroom):
	def at_object_creation(self):
		self.db.desc = "The swirling sands part and divide, leaving identifiable paths.|/It's difficult to tell how far anything goes in a particular direction, the sand camouflages itself together between the color and the constant swirling movement, the latter of which almost makes you nauseous.|/Between the two any hopes of depth perception is near impossible beyond what's right in front of you."
		self.db.fight = "no"
		self.tags.add("notravel")

class oasismoveup(moveroom):
	def at_object_creation(self):
		self.db.desc = "The swirling sands part and divide, leaving identifiable paths.|/It's difficult to tell how far anything goes in a particular direction, the sand camouflages itself together between the color and the constant swirling movement, the latter of which almost makes you nauseous.|/Between the two any hopes of depth perception is near impossible beyond what's right in front of you."
		self.db.sendlocation = ""
		self.db.warning = "|/The sand begins to shift beneath your feet."
		self.db.movemsg = "|/A hole opens above your head, suddenly you're gently rising up. The hole beneath you closes quickly, leaving you on solid ground."
		self.db.fight = "no"
		self.tags.add("notravel")

class oasismovedown(moveroom):
	def at_object_creation(self):
		self.db.desc = "The swirling sands part and divide, leaving identifiable paths.|/It's difficult to tell how far anything goes in a particular direction, the sand camouflages itself together between the color and the constant swirling movement, the latter of which almost makes you nauseous.|/Between the two any hopes of depth perception is near impossible beyond what's right in front of you."
		self.db.sendlocation = ""
		self.db.warning = "|/The sand begins to shift beneath your feet."
		self.db.movemsg = "|/The sand opens below you, you gently fall and land softly. The hole overhead closes quickly."
		self.db.fight = "no"
		self.tags.add("notravel")

class oasismoveout(moveroom):
	def at_object_creation(self):
		self.db.desc = "The swirling sands part and divide, leaving identifiable paths.|/It's difficult to tell how far anything goes in a particular direction, the sand camouflages itself together between the color and the constant swirling movement, the latter of which almost makes you nauseous.|/Between the two any hopes of depth perception is near impossible beyond what's right in front of you."
		self.db.sendlocation = "#3502"
		self.db.warning = "|/The sand begins to shift beneath your feet."
		self.db.movemsg = "|/|rAAHHHHHHH!!!!!!!|/You scramble for purchase as you sink, but you find yourself hurtling towards the ground.|/*THUD*|/Ouch. You cough out a mouthful of sand, roll over, and moan in pain.|n|/|mEverett|n says: My word, that looked like it hurt!"
		self.db.fight = "no"
		self.tags.add("notravel")

class oasis(vroom):
	def at_object_creation(self):
		self.db.desc = "You find yourself in the eye of a swirling sand cyclone, in the Oasis.|/Verdant green trees with long wide leaves encircle the oasis and provide relief from the sun.|/A large pool of sparkling blue water sits welcoming in the center of the Oasis, with rows of crops neatly arrayed nearby."
		self.db.fight = "no"

class hellview(ifmonsterdefeatedview):
	def at_object_creation(self):
		self.db.desc = "You are struck by the eerie silence. The air is still and quiet, save for the occasional creak of a dilapidated wooden structure or the rustle of leaves in the wind.|/The ruins of the village seem frozen in time, as if they are a ghostly reminder of a bygone era."
		self.db.defeateddesc = "The air is thick with an oppressive energy, as if the very atmosphere is suffused with the lingering emotions of those who once lived here.|/You feel a cold hand on your shoulder, and you spin around to find nothing there.|/Slowly ghostly apparitions of the village's former residents appear, their faces twisted in anger and fear consumed by their hatred for outsiders and determined to keep anyone who is not like them from entering their realm."
		self.db.monstername = "Honkiamat"
		self.db.fight = "no"
		self.tags.add("notravel")

class carvercity(ifmonsterdefeatedview):
	def at_object_creation(self):
		self.db.desc = "Winding streets and narrow alleyways lead up and down in a maze-like fashion.|/As you wander through the city, you can see remnants of ancient wars in the form of old fortresses and crumbling walls, clearly preserved as a reminder of the city's strength and perseverance. Fresh cold water flows through small aqueducts through the city down from the mountains. You can catch glimpses of lush gardens and greenery growing in unexpected places.|/The city has been at peace for generations."
		self.db.defeateddesc = "Winding streets and narrow alleyways, all made of the ancient black stone or the mountain, lead up and down in a maze-like fashion through the city.|/As you wander through the city, you can see the destruction brought by the denizens of Hellview.|/The remains of the slaughtered lay lifeless, strewn about the small gardens and paths staring blankly at you as you pass. The once fresh water runs red."
		self.db.monstername = "Honkiamat"
		self.db.fight = "no"

class arcanumisland(vroom):
	def at_object_creation(self):
		self.db.desc = "A small spiraling island, like a sea shell.|/At the bottom of the island is an inn and pub. At the top of the island is the magicians guild.|/From the looks of it, they may as well hold classes in the pub."
		self.db.fight = "no"

class ayerisisland(vroom):
	def at_object_creation(self):
		self.db.desc = "The air is perfumed with the scent of flowers and incense, and the light reflects off the crystal surfaces, creating a dazzling and ethereal glow. Walls, ceilings, and floors are covered in intricate patterns of geometric shapes and symbols, which seem to shift and move."
		self.db.fight = "no"

class serenityisland(vroom):
	def at_object_creation(self):
		self.db.desc = "The sounds of artisans fills the air.|/The island is covered in lush greenery curated into small gardens and articulated topiaries.|/A small hill contours the island, moving up to the north, and down to the east."
		self.db.fight = "no"

class tomeisland(vroom):
	def at_object_creation(self):
		self.db.desc = "Tome island is dominated by a grand, sprawling structure made of polished marble and adorned with towering pillars and intricate carvings, The Citadel of the Celestial Archive.|/A repository of knowledge and wisdom that stretches back for centuries.|/Tome island is also home to a number of gardens and courtyards, where scholars can relax and reflect on the vast knowledge contained within the library's walls."
		self.db.fight = "no"

class gardenofserenity(vroom):
	def at_object_creation(self):
		self.db.desc = "The garden features a series of tranquil pools and fountains, surrounded by lush greenery and colorful flowers.|/The soothing sound of the water and the gentle rustling of leaves make this the perfect place for visitors to relax and reflect on the vast knowledge contained within the library."
		self.db.fight = "no"

class gardenofthesenses(vroom):
	def at_object_creation(self):
		self.db.desc = "Designed to stimulate the senses and ignite the imagination, this garden is filled with exotic plants and rare flowers, each with their own unique scent and texture.|/Visitors are encouraged to touch, smell, and taste the plants, to fully immerse themselves in the beauty of the natural world."
		self.db.fight = "no"

class courtyardofreflection(vroom):
	def at_object_creation(self):
		self.db.desc = "A series of peaceful alcoves and sitting areas where visitors can meditate and contemplate the mysteries of the universe create the courtyard.|/The courtyard is surrounded by tall trees and colorful flowers, providing a serene and calming environment for visitors to unwind and find inner peace."
		self.db.fight = "no"

class terraceofthestars(vroom):
	def at_object_creation(self):
		self.db.desc = "Panoramic views of the surrounding sky and stars fill your vision, illuminated clouds of galaxies swirl and gather in the sky.|/Visitors can relax on comfortable benches and chairs, gazing up at the vast expanse of the heavens above, and marveling at the wonders of the cosmos."
		self.db.fight = "no"

class gardenoftheancients(vroom):
	def at_object_creation(self):
		self.db.desc = "a place of myth and legend where ancient trees and mystical creatures roam. This garden is shrouded in mystery and magic, and visitors are advised to tread carefully, for they never know what wonders they may encounter amidst the twisting branches and winding paths."
		self.db.fight = "no"

class celestialarchive(vroom):
	def at_object_creation(self):
		self.db.desc = "The walls are lined with row after row of towering bookcases, each filled with countless volumes, scrolls, and tomes on a wide range of subjects.|/The air is heavy with the scent of old parchment and leather bindings, and the gentle rustling of pages turning echoes throughout the halls.|/The room is illuminated by the soft glow of mystical candles that are hanging from the ceiling, in wall sconces, and in candle holders on the tables.|/Throughout the library, there are alcoves and niches filled with ancient artifacts and mystical relics, each with their own story and significance."
		self.db.fight = "no"

class crossroadisland(vroom):
	def at_object_creation(self):
		self.db.desc = "Suspended high above the clouds, these islands appear as if they are made of crystal, glowing softly in the sunlight.|/Immediately your are struck by the sense of peace and serenity that pervades the air. The island is covered in lush greenery, with trees that seem to sparkle with a gentle light. The sounds of nature, including the chirping of birds and the rustling of leaves, fill the air."
		self.db.fight = "no"

class celestialcollege(vroom):
	def at_object_creation(self):
		self.db.desc = "The campus of the Celestial College is a complex of buildings, stairways, terraces, and gardens, with winding paths leading through lush greenery and bubbling fountains.|/The buildings themselves are ornate and grand, with intricate carvings and stained glass windows depicting scenes from the history of magic."
		self.db.fight = "no"

class boarssnout(vroom):
	def at_object_creation(self):
		self.db.desc = "The docks stretch out like frozen fingers into the icy waters, where the frigid ocean meets the jagged shoreline.|/Built with solid craftsmanship, the wooden planks creak underfoot, evidence of years of enduring harsh winters and relentless sea winds.|/The scent of saltwater mingles with the sharp tang of freshly caught fish, carried by the bracing sea breeze that whips through the harbor.|/Boats of all sizes and shapes bob gently in the frigid waters, tied to wooden posts and anchored securely. Icebreaker ships, specially designed with reinforced hulls and sturdy bows, dominate the scene. These vessels, essential for navigating the treacherous frozen oceans, stand as a testament to the resourcefulness and innovation of the city's shipbuilders."
		self.db.fight = "no"

class boarssnoutifacc(ifaccolade):
	def at_object_creation(self):
		self.db.desc = "The streets are filled with a strange silence where you would expect the sounds of a port city carrying over the icy air. In its place, a dull thrum of thick boots, moving cargo, and the occasional shouted instruction.|/Small rows of houses are fit snugly between large warehouses, all made of the native stone. The aroma of hearth fires and hot spiced beverages and food wafts through the air, offering warmth and comfort to those braving the cold."
		self.db.hasaccoladedesc = "The streets echo with song. Bards and minstrels crow from every corner, music bursts out as a door opens from a building then slowly returns to a muffled rhythm as the door swings shut.|/Small rows of houses are fit snugly between large warehouses, all made of the native stone. The aroma of hot spiced beverages and food wafts through the air, offering warmth and comfort to those braving the cold."
		self.db.accolade = "Finder of the Song"
		self.db.fight = "no"

#temple overworld
class templeofsmallgods(vroom):
	def at_object_creation(self):
		self.db.desc = "A small stone temple stands in the forest clearing.|/Stairs leading to the entrance have slight dips in the rocks where feet have worn them down."
		self.db.fight = "no"

#temples
class templeofsmallgodsinside(iftagviewnf):
	def at_object_creation(self):
		self.db.fight = "no"
		self.tags.add("notravel")
		self.db.desc = "The low ceiling is draped with spiderwebs.|/Tiny spiders dart across the webs, eagerly pouncing as a bug finds itself caught in their trap.|/Broken idols hang suspended, wrapped in webs. You can barely make out the small head of a bull poking out from one of the sacks of webbing."
		self.db.tagdesc = "Disciples of Om scurry about the temple, sweeping, discussing, praying.|/The temple lives up to it's name now, a true temple. New idols fill the coves in the walls, tapestries hang on the wall, some disciples are busy painting new icons.|/The scrit and scribble of disciples copying books fills the air."
		self.db.tagname = "omthemighty"

class templeoftheblindgod(DefaultRoom):
	def at_object_creation(self):
		self.db.fight = "no"
		self.tags.add("notravel")
		self.db.desc = ""
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		newdesc = str()
		desc = self.db.desc
		words = desc.split()
	#holds left eye
		if looker.tags.get("lefteye") and not looker.tags.get("righteye") and not looker.tags.get("centereye"):
			for i in words:
				if len(i) > 1 and not i == "|/":
					newdesc = newdesc + i[0] + ' ' * (len(i) - 1) + " "
				elif i == "|/":
					newdesc = newdesc + "|/"
				else:
					newdesc = newdesc + i + " "
	#Holds right eye
		if looker.tags.get("righteye") and not looker.tags.get("lefteye") and not looker.tags.get("centereye"):
			for i in words:
				if len(i) > 1 and not i == "|/":
					newdesc = newdesc + ' ' * (len(i) - 1) + i[-1] + " "
				elif i == "|/":
					newdesc = newdesc + "|/"
				else:
					newdesc = newdesc + i + " "
	#Holds left and right eye
		if looker.tags.get("righteye") and looker.tags.get("lefteye") and not looker.tags.get("centereye"):
			for i in words:
				if len(i) > 1 and not i == "|/":
					newdesc = newdesc + i[0] + ' ' * (len(i) - 2) + i[-1] + " "
				elif i == "|/":
					newdesc = newdesc + "|/"
				else:
					newdesc = newdesc + i + " "
	#Holds center eye
		if looker.tags.get("centereye") and not looker.tags.get("righteye") and not looker.tags.get("lefteye"):
			for i in words:
				if len(i) > 2:
					newdesc = newdesc + " " + i[1:len(i)-1] + " " + " "
				elif i == "|/":
					newdesc = newdesc + "|/"
				else:
					newdesc = newdesc + i + " "
	#Holds left and center eye.
		if looker.tags.get("lefteye") and looker.tags.get("centereye") and not looker.tags.get("righteye"):
			for i in words:
				if len(i) > 2:
					newdesc = newdesc + i[0:len(i)-1] + " " + " "
				elif i == "|/":
					newdesc = newdesc + "|/"
				else:
					newdesc = newdesc + i + " "
	#Holds center and right eye.
		if looker.tags.get("righteye") and looker.tags.get("centereye") and not looker.tags.get("lefteye"):
			for i in words:
				if len(i) > 2:
					newdesc = newdesc + " " + i[1:len(i)] + " "
				elif i == "|/":
					newdesc = newdesc + "|/"
				else:
					newdesc = newdesc + i + " "
	#Holds all eyes
		if looker.tags.get("righteye") and looker.tags.get("centereye") and looker.tags.get("lefteye"):
			newdesc = desc
	#Holds no eyes
		if not looker.tags.get("righteye") and not looker.tags.get("centereye") and not looker.tags.get("lefteye"):
			newdesc = ""
	#Already defeated temple
		if looker.tags.get("allseeing"):
			newdesc = desc
		if newdesc:
			string += "%s" % newdesc
		if not newdesc:
			string += "You are blind and cannot see anything."
		string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class houseofduality(vroom):
	def at_object_creation(self):
		self.db.desc = "Test Room."
		self.db.fight = "no"
		self.tags.add("notravel")

class pathofsuits(vroom):
	def at_object_creation(self):
		self.db.desc = "Test Room."
		self.db.fight = "no"
		self.tags.add("notravel")
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					pass
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if looker.tags.get(category="SuitPath"):
			desc = self.db.desc + "|/Yours is the path of %s, follow the path." % looker.tags.get(category="SuitPath")
		else:
			desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class dragontemple(iftagviewnf):
	def at_object_creation(self):
		self.db.desc = "No tag"
		self.db.tagdesc = "Tag"
		self.db.tagname = "orthanpass"
		self.db.fight = "no"
		self.tags.add("notravel")

#arena
class titanarena(DefaultRoom):
	def at_object_creation(self):
		self.db.desc = "|mAnnouncer|n says: WELCOME ALL TO THE TITAN ARENA!!!|/The crowd roars."
		self.db.zone = "arenaone"
		self.db.fight = "yes"
		self.tags.add("notravel")
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					pass
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		desc = self.db.desc + "|/|mAnnouncer|n says: OUR CHALLENGER IS %s! LEEEEEEETTTTSSS GET READY TO BATTLE!!!!!|/|mAnnouncer|n says: CHALLENGER |cRING GONG|n TO START THE FIGHT!!!|/The crowd roars." % (looker.key.upper())
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string



#Overworld rooms
class trainingroom(ifnottagviewnf):
	def at_object_creation(self):
		self.db.desc = "Master Roshi's training hut is clean and well organized. Large windows ringing the hut let a cooling breeze blow through.|/Well worn but freshly waxed wooden floors show beneath thick woven grass rugs.|/A training dummy stands silently in the center of the room."
		self.db.tagdesc = "The remains of the training hut creak in warning of collapse at any moment.|/Master Roshi's infamous training dummy still stands in the center of the room, charred."
		self.db.tagname = "beginning"
		self.db.zone = "zone0training"
		self.db.fight = "yes"
		self.tags.add("autofight")

class autofightlow(vroom):
	def at_object_creation(self):
		self.db.desc = ""
		self.db.zone = ""
		self.db.fight = "yes"
		self.tags.add("autofight")
	def at_object_receive(self, character, source_location):
		if not character.permissions.get("player"):
			return
		chance = randint(1, 5)
		if chance == 2:
			character.tags.add("letsfight")
			character.execute_cmd('fight')
		else:
			character.execute_cmd('look')

class autofight(vroom):
	def at_object_creation(self):
		self.db.desc = ""
		self.db.zone = ""
		self.db.fight = "yes"
		self.tags.add("autofight")
	def at_object_receive(self, character, source_location):
		if not character.permissions.get("player"):
			return
		chance = randint(1, 3)
		if chance == 2:
			character.tags.add("letsfight")
			character.execute_cmd('fight')
		else:
			character.execute_cmd('look')

class poisonroom(autofight):
	def at_object_creation(self):
		self.tags.add("poisonroom")
		self.db.poisondamage = 2
		self.db.damagemsg = "The poison air burns you"
		self.db.desc = "Noxious gases rise from the burbling swamp."
		self.db.zone = "unknown"
		self.db.fight = "yes"
		self.tags.add("autofight")

class paphillslf(autofightlow):
	def at_object_creation(self):
		self.db.desc = "The foothills of Papricallah extend to the south and east.|/The shadow of the mountain cools the area, making the difficult terrain tolerable to traverse."
		self.db.zone = "zone1hills"
		self.db.fight = "yes"
		self.tags.add("autofight")

class paphills(autofight):
	def at_object_creation(self):
		self.db.desc = "The Papricallah hills surround the foothills extending to the south and east.|/It is much warmer out of the shadow of the mountain. Long rough grass rolls in waves across the gentle hills as the breeze blows."
		self.db.zone = "zone1hills"
		self.db.fight = "yes"
		self.tags.add("autofight")

class paphillsnofight(vroom):
	def at_object_creation(self):
		self.db.desc = "The Papricallah hills surround the foothills extending to the south and east.|/It is much warmer out of the shadow of the mountain. Long rough grass rolls in waves across the gentle hills as the breeze blows."
		self.db.fight = "no"

class papgrasslandslf(autofightlow):
	def at_object_creation(self):
		self.db.desc = "The rolling grasslands spill out, gently descending to the West. A gentle breeze carries the light briny scent of the ocean."
		self.db.zone = "zone1grasslands"
		self.db.fight = "yes"
		self.tags.add("autofight")

class papgrasslands(autofight):
	def at_object_creation(self):
		self.db.desc = "The rolling grasslands spill out, gently descending to the West. A gentle breeze carries the light briny scent of the ocean."
		self.db.zone = "zone1grasslands"
		self.db.fight = "yes"
		self.tags.add("autofight")

class gadozbeach(autofight):
	def at_object_creation(self):
		self.db.desc = "The clean white sand sparkles in the sun, small waves gently break and roll up onto the sand first pushing the smalls pebbles, then rolling them back.|/Small seashells are scattered about, the occasional crab scuttles past trying to avoid the sea birds circling above."
		self.db.zone = "zone1beach"
		self.db.fight = "yes"
		self.tags.add("autofight")

class papforestpath(autofightlow):
	def at_object_creation(self):
		self.db.desc = "A well worn forest path winds its way lazily the forest.|/Light filters in through the leafy boughs and branches, driving back the murk of the forest proper."
		self.db.zone = "zone1forestpath"
		self.db.fight = "yes"
		self.tags.add("autofight")

class paiprisafezone(vroom):
	def at_object_creation(self):
		self.db.desc = "desc The forest is cleared around the capitol city of Paipri.|/You feel safe.|/Farms, fields, and makeshift markets fill every inch of land from the city walls to the forest."
		self.db.fight = "no"

class papforest(autofight):
	def at_object_creation(self):
		self.db.desc = "The light of the sun has minimal impact on the inky darkness that seems to hang heavy in the forest air.|/There is a feeling of danger, eyes glinting in the darkness followed by low growls and rustling in the brush all around you."
		self.db.zone = "zone1forest"
		self.db.fight = "yes"
		self.tags.add("autofight")

class papforestnofight(vroom):
	def at_object_creation(self):
		self.db.desc = "The light of the sun has minimal impact on the inky darkness that seems to hang heavy in the forest air.|/There is a feeling of danger, eyes glinting in the darkness followed by low growls and rustling in the brush all around you.|/The forest thins revealing a small temple."
		self.db.fight = "no"

class tormarshlf(autofightlow):
	def at_object_creation(self):
		self.db.desc = "The ground is firm, but wet. Tiny ponds and lakes surrounded by blossoming water plants and reeds dot the land as far as the eye can see.|/Insects and critters fill the misty air with their ballads, hoping to attract a mate."
		self.db.zone = "zone2marsh"
		self.db.fight = "yes"
		self.tags.add("autofight")

class tormarsh(autofight):
	def at_object_creation(self):
		self.db.desc = "The ground is firm, but wet. Tiny ponds and lakes surrounded by blossoming water plants and reeds dot the land as far as the eye can see.|/Insects and critters fill the misty air with their ballads, hoping to attract a mate."
		self.db.zone = "zone2marsh"
		self.db.fight = "yes"
		self.tags.add("autofight")

class torswamp(poisonroom):
	def at_object_creation(self):
		self.tags.add("poisonroom")
		self.db.poisondamage = 3
		self.db.damagemsg = "The poison air burns your skin and eyes"
		self.db.desc = "Noxious gases rise from the burbling swamp."
		self.db.zone = "zone2marsh"
		self.db.fight = "yes"
		self.tags.add("autofight")

class swampcastlefirstfloor(autofight):
	def at_object_creation(self):
		self.db.desc = "The crumbling Swamp Castle, stone pitted and cracked overgrown with vines, wooden beams rotting and sprouting mushrooms. Small puddles of fetid water bubble in sunken corners.|/The entire structure seems like it could collapse with a stiff breeze."
		self.db.zone = "zone2marsh"
		self.db.fight = "yes"
		self.tags.add("autofight")

class swampcastlesecondfloor(autofight):
	def at_object_creation(self):
		self.db.desc = "A breeze coming in through the collapsed sections of ceiling and walls doesn't remove the stink of the fetid water, but rather replaces it with the stench from the swamp.|/Missing stone from the floor makes every step treacherous."
		self.db.zone = "zone2marsh"
		self.db.fight = "yes"
		self.tags.add("autofight")

class swampcastlebasement(iftagviewfight):
	def at_object_creation(self):
		self.db.desc = "Disgusting water, you hope it's water, is up to your waist.|/Between the dark and your eyes burning and watering, it is impossible to see anything. If only you had better eyes."
		self.db.tagdesc = "You find yourself waist deep in swamp water.|/Despite the darkness you can see well."
		self.db.tagname = "allseeing"
		self.db.zone = "zone2marsh"
		self.db.fight = "yes"
		self.tags.add("autofight")

swampcastledeathphrases = ["*Rumble Rumble* Uh oh, the roof caves in forcing your face under the feted water. Your death bubbles intermingle with the other gases, making no difference to the world at large.", "A serpentine ripple in the water gains speed as ii heads towards you! OH NO!! SWAMP SHARK!!!!", "Oh goodness, your foot is stuck. You're surely going to lose a boot in all this.|/You feel a sudden tug, then excruciating pain, your leg has been ripped off.|/You manage to escape the horrid indescribable beast, but die from infection mere hours later."]

class swampcastledeath(vroom):
	def at_object_creation(self):
		self.db.startover = "#8416"
		self.db.msg = random.choice(swampcastledeathphrases)
		self.db.travel = "no"
		self.db.fight = "no"
	def at_object_receive(self, character, source_location):
		place = self.db.startover
		character.msg(self.db.msg)
		character.msg("|/|rYou are dead.|n")
		results = search_object(place)
		character.move_to(results[0], quiet=True, move_hooks=False)

class torhighlands(autofight):
	def at_object_creation(self):
		self.db.desc = "Rocky outcrops break through the thick moss covered terrain.|/The occasional earthen house built into the hills blend into the geography easily.|/Once well tended, most have fallen into disrepair or destruction."
		self.db.zone = "zone2highlands"
		self.db.fight = "yes"
		self.tags.add("autofight")

class tolvaj(vroom):
	def at_object_creation(self):
		self.db.desc = "Tolvaj was built on the hidden island of a treacherous swamp and is truly a hub of activity for thieves. Lite but sturdy wooden structures incorporating rubble of the abandoned Swamp Castle strike a careful balance between security and not falling over and sinking into the swamp.|/The balance to the humbleness of the building materials is gold and silver accented street lamps, gilded windows, gem studded statuary. The local craftspersons apparently have no limit to the amount of high end materials to work with."
		self.db.fight = "no"

class castleardismouf(autofight):
	def at_object_creation(self):
		self.db.desc = "The white stone of the castle reflects the candle light from the crystal chandeliers overhead.|/Tapestries and colored glass windows dot the walls.|/As you sneak, the footsteps of patrolling guards echo down the hallways, causing you to frequently and nervously swivel your head."
		self.db.zone = "zone2castle"
		self.db.fight = "yes"
		self.tags.add("autofight")
		self.tags.add("notravel")

class castleardismoufgraveyard(autofight):
	def at_object_creation(self):
		self.db.desc = "A small garden, dotted with gravestones, surrounds a hangmans tree.|/The castle buries their most famous captured criminals here, like a trophy room."
		self.db.zone = "zone2castle"
		self.db.fight = "no"


class kharrocliffs(autofight):
	def at_object_creation(self):
		self.db.desc = "Strong winds from the ocean kick up sand, irritating your eyes.|/Cautiously you look over the edge of the cliff, waves batter and crash into the red stone with a rhythmic roar."
		self.db.zone = "zone3cliffs"
		self.db.fight = "yes"
		self.tags.add("autofight")

class kharrodunes(autofightlow):
	def at_object_creation(self):
		self.db.desc = "Rolling hills of sand stretch down from the Red Cliffs, slowly fading into desert.|/The heat is unbearable, sand swirls in the air blasting your skin.|/Sand slides trickle and build to a rush down the dunes, but what disturbed the sand in the first place?"
		self.db.zone = "zone3dunes"
		self.db.fight = "yes"
		self.tags.add("autofight")

class kharrodesert(autofight):
	def at_object_creation(self):
		self.db.desc = "Heat shimmers on the sands, creating the illusion of waves sparkling like gemstones.|/A sea of parched death interrupted by scraggly thorn bushes and the occasional pile of bleached bones."
		self.db.zone = "zone3desert"
		self.db.fight = "yes"
		self.tags.add("autofight")

class sarlaccpit(vroom):
	def at_object_creation(self):
		self.db.desc = "Heat shimmers on the sands, creating the illusion of waves sparkling like gemstones.|/A sea of parched death interrupted by scraggly thorn bushes and the occasional pile of bleached bones.|/A large sand sculpture stands tall in the desert, a female form, arms open and welcoming. For some reason the wind and sand does not appear to affect it the sculpture the same way the elements have eroded the rest of the natural landscape."
		self.db.sendlocation = "#11532"
		self.db.warning = "|/|rThe sand begins to boil and shift beneath your feet...|n"
		self.db.death = "|/You look down much too late as the sand beneath you begins to flow, a hot putrid wind gusts from beneath you, the sand runs down pulling you into a giant gaping maw in the sand.|/|/|rWhat tragic fate, you spend the rest of your very short life being digested by a Sarlacc. Enjoy becoming Sarlacc poop.|n|/You have brought shame to yourself and your family."
		self.db.welcome = "|g|/A warm and welcoming voice fills your head.|/|mMother of Sands|n says: You return to my embrace, this makes your mother happy.|n|/"
	def at_object_receive(self, obj, source):
		utils.delay(4, self.sendmsg, obj)
	def sendmsg(self, obj):
		for i in self.contents:
			if i.has_account and i.key == obj.key:
				obj.msg(self.db.warning)
				utils.delay(4, self.move, obj)
	def move(self, obj):
		for i in self.contents:
			if i.has_account and i.key == obj.key:
			#Mothers embrace
				if obj.tags.get("seekerofknowledge"):
					destination = search_object(self.db.sendlocation)
					obj.msg(self.db.welcome)
			#Death
				else:
					obj.db.deathcount += 1
					destination = search_object(obj.db.lastcity)
					obj.msg(self.db.death)
					obj.db.hp = int(obj.db.maxhp * .5)
					obj.db.mp = int(obj.db.maxmp * .5)
					obj.db.gold -= int(obj.db.gold * .2)
				obj.move_to(destination[0], quiet=True, move_hooks=False)

class orthangrove(autofightlow):
	def at_object_creation(self):
		self.db.desc = "Thin tall trees with rings of branches are peppered across the area.|/Crystalline rocks jut up from the ground, glowing softly."
		self.db.zone = "zone4grove"
		self.db.fight = "yes"
		self.tags.add("autofight")

class orthanwinterforest(autofight):
	def at_object_creation(self):
		self.db.desc = "Evergreen trees with clear crystalline needles emit soft light pulsing from blue to green, illuminating the snow gathered on their bows.|/The snow crunches softly under your boots as you walk, a deafening roar in the absolute silence of the forest."
		self.db.zone = "zone4winterforest"
		self.db.fight = "yes"
		self.tags.add("autofight")

class thedepthsofknowledge(autofight):
	def at_object_creation(self):
		self.db.desc = "You are somewhere under the library in a twisting turning hallway. An eerie and foreboding atmosphere swirls in the air. Bookcases are lit by flickering torches set into the walls."
		self.db.fight = "yes"
		self.db.zone = "depthsofknowledge"
		self.tags.add("notravel")
		self.tags.add("autofight")

class varkenwastelf(autofightlow):
	def at_object_creation(self):
		self.db.desc = "A barren expanse battered by cold winds unfolds before you.|/The Wastes of Varken, a no-mans-land covered in a blanket deep snow.|/Best to keep moving before you freeze to death."
		self.db.zone = "zone5waste"
		self.db.fight = "yes"
		self.tags.add("autofight")

class varkenwaste(autofight):
	def at_object_creation(self):
		self.tags.add("poisonroomslow")
		self.db.poisondamage = 3
		self.db.damagemsg = "The biting wind saps your strength"
		self.db.desc = "The winds blast you, making your eyes water and then freezing the tears to your face.|/Biting cold sinks deep through you, chilling you to the bone.|/More snow, nothing else but snow, slowing your progress, making your feet ache with every step."
		self.db.zone = "zone5waste"
		self.db.fight = "yes"
		self.tags.add("autofight")

class varkentundra(autofight):
	def at_object_creation(self):
		self.tags.add("poisonroomslow")
		self.db.poisondamage = 6
		self.db.damagemsg = "The jaw rattling cold saps your strength"
		self.db.desc = "Thin stunted trees poke through the snow, standing proud against the wind.|/Pale moss clings to the leeward side of stones big enough to break through the tundra blanket.|/The thin trees do little to break the howling wind, but the deep deep cold negates any relief it brings."
		self.db.zone = "zone5tundra"
		self.db.fight = "yes"
		self.tags.add("autofight")

class varkenfjords(autofight):
	def at_object_creation(self):
		self.db.desc = "The Fjords of Varken run jaggedly into the land.|/The cold and wind are less here, buffered by the steep cliff tops and deep valleys.|/Hearty plants and bushes struggle to reach purchase in the rocky terrain."
		self.db.zone = "zone5fjords"
		self.db.fight = "yes"
		self.tags.add("autofight")

class varkensprings(autofight):
	def at_object_creation(self):
		self.db.desc = "Steam rolls slowly off of the small pools of water gathered in the dips and divots in the black rock.|/A break from the horrid cold of the rest of Varken.|/The warmth of the air slowly seeps into you, chasing away the pains of aching joints and muscles."
		self.db.zone = "zone5springs"
		self.db.fight = "yes"
		self.tags.add("autofight")

class warfront(autofight):
	def at_object_creation(self):
		self.db.desc = "Battle rages all around you.|/You duck, dodge, and strike back as screaming Valaharran's leap through the air, weapons flashing as they streak towards you.|/Steel strikes steel as the Tormeyian soldiers fight to hold their ground.|/Bodies of the fallen litter the ground, bleeding out turning the ground to mud."
		self.db.zone = "zone5warfront"
		self.db.fight = "yes"
		self.tags.add("autofight")

class volcanomaze(autofightlow):
	def at_object_creation(self):
		self.db.desc = "A sulfur stink is thick in the hot air, burning your nose and throat.|/Echoes play tricks on your ears, shadows dart and dance at the corner of your vision in the red miasma."
		self.db.zone = "zone6volcanomaze"
		self.db.fight = "yes"
		self.db.travel = "no"
		self.tags.add("autofight")

volcanotrapwords =["|/|rA fissure opens beneath your feet plunging you into a pool of lava.|n", "|/|rA vent suddenly explodes blasting you with sulfurous steam, boiling you in your skin.|n", "|/|r*Drip-hisss, drip-hisss* You look up right as the ceiling dissolves showering you in molten rock.|n", "|/|r*hhiiisssssSSSSS POP!* A small steam explosion sends obsidian shrapnel speeding through your body. You bleed to death.|n", "|/|rSo many stalactites..mites? Which one goes dow.. AHAAAAAAAAAAAAAAA!!!|/Not paying attention to where you're going you step right into a lava flow and burn your feet off and become trapped. Unable to move, you slowly starve to death.|n", "|/|rA small lava flow blocks your way. You decide to attempt to scale the walls to get across. You've just failed 'The Floor is Lava'|n", "|/|r You decide to do a flip over a stream of lava.|/The judges give you a 10/10 for your Anakin Skywalker on Mustafar impression.|n"]
class volcanomazedeath(vroom):
	def at_object_creation(self):
		self.db.startover = "#5840"
		self.db.msg = random.choice(volcanotrapwords)
		self.db.travel = "no"
	def at_object_receive(self, character, source_location):
		place = self.db.startover
		character.msg(self.db.msg)
		character.msg("|/You are dead.|n")
		results = search_object(place)
		character.move_to(results[0], quiet=True, move_hooks=False)

class volcanomazeteleport(vroom):
	def at_object_creation(self):
		self.db.startover = ["#5991", "#5955", "#6009", "#6024", "#6041", "#6052"]
		self.db.travel = "no"
	def at_object_receive(self, character, source_location):
		place = random.choice(self.db.startover)
		character.msg("|/|r*skuttle skuttle*|n|/Oh no!! LAVA SLOTHS!!!|/A tunnel erupts above you as long claw covered hands veeeeerrry slowly snatch you up and drag you off.")
		results = search_object(place)
		character.msg("|/The Lava Sloth drops you out of one of its tunnels, landing with a painful thump... somewhere.")
		character.move_to(results[0], quiet=True, move_hooks=False)

class bayofblood(autofightlow):
	def at_object_creation(self):
		self.db.desc = "Blood red water oozes out of the sand beneath your feet and fills in your tracks as you walk along the shores of the Bay of Blood.|/Small raiding boats and larger battle ships bob in the bay awaiting the sound of the war drums.|/A red waterfall spills over the wicked mountains pouring into the bay."
		self.db.zone = "zone7bayofblood"
		self.db.fight = "yes"
		self.tags.add("autofight")

class valaharrahinterland(autofight):
	def at_object_creation(self):
		self.db.desc = "Fist sized rocks worn round and smooth from the sea litter the ground and seek to turn your ankle at every step.|/West, the rocky ground turns to mossy loam and Valaharra proper, to the East, the Bay of Blood.|/Decorative displays of exotic animal skins and skulls, skeletons clothed in colorful flowers posed in various dances, and decapitated heads still dripping blood mounted on spikes mark the way to the great roads that lead into the heart of Valaharra."
		self.db.zone = "zone7valaharrabeach"
		self.db.fight = "yes"
		self.tags.add("autofight")

class valaharrahighway(autofight):
	def at_object_creation(self):
		self.db.desc = "The great highway stretches from the Hunterlands inland.|/Paved in gold and silver bricks from captured treasure, the skeletons of those unfortunate enough to not have been deemed worthy of being slaves or sacrifices now point the way west and south to the city gates."
		self.db.zone = "zone7valaharra"
		self.db.fight = "yes"
		self.tags.add("autofight")

class valaharra(autofight):
	def at_object_creation(self):
		self.db.desc = "Wisps of green, yellow, blue, and red light wave high in the air.|/The sky colors tint the land making everything more vibrant."
		self.db.zone = "zone7valaharra"
		self.db.fight = "yes"
		self.tags.add("autofight")

class madnessearlyruins(vroom):
	def at_object_creation(self):
		self.db.desc = "The architectural design, if such a term can be applied, defies all conventional notions of symmetry and rationality. Walls built at unnatural angles, their jagged edges corroded by the passage of centuries and covered in a strange silky moss. Where the stone has resisted the elements, the moss, and plants, it still gleams a dark but vibrant green in the strange light of day. Surfaces appearing perfectly straight yet curved, smooth and perfectly flat, yet seems to writhe and wriggle just beneath the glassy surface."
		self.db.fight = "no"
		self.tags.add("notravel")

class madnessforest(autofight):
	def at_object_creation(self):
		self.db.desc = "You are surrounded by a sprawling expanse of twisted vegetation. Grotesque flora sprawls in tangled masses, their vibrant hues distorted into sickly shades of green and violet. Thorned vines snake through the undergrowth, their serpentine embrace serving as both warning and entrapment. It is a place where nature itself seems to have succumbed to the influence of maddening forces. Partially collapsed walls and structures block your path in varying directions. The stones used, if it is stone, are unnaturally large single pieces. Given their size and shape, your mind struggles to comprehend what possible shape the structures here once took when they were still standing. Whatever this place once was, it has been lost to the world and reclaimed by the island."
		self.db.zone = "madforestlow"
		self.db.fight = "yes"
		self.tags.add("autofight")
		self.tags.add("notravel")

class madnessdangerousforest(autofight):
	def at_object_creation(self):
		self.db.desc = "The air carries a pungent scent of sweet flowers and rotting meat. Grotesque flora sprawls in tangled masses, their vibrant hues distorted into sickly shades of deep green and darkly vibrant violet. Thorned vines snake through the undergrowth, their serpentine embrace serving as both warning and entrapment. Clumps of glowing eyes stare at you from the forest, not just sets of eyes, but clustered multitudes."
		self.db.zone = "madforestdangerous"
		self.db.fight = "yes"
		self.tags.add("autofight")
		self.tags.add("notravel")

class nkomererovtu(autofight):
	def at_object_creation(self):
		self.db.desc = "While the forest has receded, this ancient city is in a state of desolate ruin, a haunting echo of the once-great civilization that thrived within. Crumbling structures and fractured spires reach towards a sky tainted with perpetual twilight, casting long shadows over the decaying streets below. The air is thick with an otherworldly stillness, broken only by the occasional mournful wail of a twisted creature lurking in the shadows. Vines and ivy, suffused with an otherworldly glow, twist and curl around broken pillars and shattered statues, their vibrant colors stark against the backdrop of decay."
		self.db.zone = "vtu"
		self.db.fight = "yes"
		self.tags.add("autofight")
		self.tags.add("notravel")

class vtu(vroom):
	def at_object_creation(self):
		self.db.desc = "Once-majestic spires, now crumbling and overgrown with vines, reach towards the sky like skeletal fingers, casting eerie shadows upon the desolate streets below. The architecture, a blend of arcane artistry and otherworldly aesthetics, hints at a civilization that delved deep into forbidden knowledge and pursued dark arts.|/As you venture through the city's winding alleys and fractured boulevards, you are greeted by an eerie silence broken only by strange whispers on the wind. Are there voices? Is it the wind creating this noise? Is there actually noise or are you hearing this in your head? Time-worn edifices stand as grim reminders of a forgotten past, their intricate carvings and intricate mosaics now faded and weathered. Vines and ivy crawl along the walls, intertwining with the stonework, as nature reclaims what was once man-made."
		self.tags.add("notravel")
		self.tags.add("whisper")
		self.db.fight = "no"

class enigmaroom(vroom):
	def at_object_creation(self):
		self.db.desc = "You do not have enigmas items equipped."
		self.db.equippeddesc = "You have enigmas items equipped."
		self.tags.add("notravel")
		self.db.fight = "no"
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if looker.db.weaponequipped == "Enigma Weapon" and looker.db.armorequipped == "Enigma Armor" and looker.db.shieldequipped == "Enigma Shield":
			desc = self.db.equippeddesc
		else:
			desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class panahon(vroom):
	ancient = ["The Island of Panahon emanates an aura of enchantment, with sprawling forests teeming with magical creatures and ancient ruins shrouded in mystic secrets.", "Hidden within the ancient woods, mystical rituals unfold as druids commune with nature, channeling the raw power of the land to shape reality.", "Ancient spirits whisper secrets among the towering trees, guiding those who seek wisdom in the heart of the enchanted forest.", "Ethereal creatures of myth roam freely, their majestic presence filling the air with magic.", "Ancient spellcasters harness the ancient energies, their incantations echoing through the moss-covered ruins of forgotten civilizations.", "The air is thick with the scent of ancient herbs and the vibrant colors of exotic flora, creating a tapestry of natural wonder."]
	primordial = ["The echoes of a time before time resound in the dense jungles of Panahon, colossal insects reign and the air pulses with primal energy.", "The relentless chirping of exotic insects fills the air as you navigate through the dense jungle, marveling at colossal flora and the eerie calls of unseen creatures.", "The primordial jungles pulse with untamed life, the world is untouched by the hands of man.", "The air resonates with the primal calls of primordial creatures unseen, their existence a testament to the raw power of nature.", "Massive vines entwine with ancient stone, the land is uncleared and wild. A place before civilization."]
	apocalypse = ["The aftermath of cataclysm lingers, leaving scars on the land, as shattered ruins and twisted landscapes serve as haunting reminders of the chaos.", "Amidst the ruins of a shattered city, survivors scavenge for resources, always on guard for the encroaching darkness and the remnants of otherworldly forces.", "Eerie winds carry whispers of lost souls, still smoldering ruins are evidence of the devastation that befell the island.", "Unnatural phenomena manifest in the sky, casting an otherworldly glow upon the desolate landscape. A sickening magic resonance lingers in the air, magical fallout from the fracturing of time.", "The air is heavy with a sense of foreboding, as if the very essence of the island mourns its cataclysmic fate of the tearing of time.", "Shadows dance among the ruins, their ethereal forms a constant reminder of the lingering darkness that engulfs this post-apocalyptic realm."]
	normal = ["Fleeting moments of temporal stability, where time briefly aligns with the present, offering respite and glimpses of normality amid the ever-shifting nature.", "Amidst the temporal shifts, you find yourself in a moment of tranquility.", "Sunlight filters through the dense canopy, casting dappled patterns on the forest floor, creating an ethereal ambiance.", "Serene waterfalls cascade down moss-covered cliffs, their gentle roar harmonizing with the symphony of nature.", "Wildflowers paint the landscape with bursts of color, their delicate petals swaying in the gentle breeze.", "Ancient ruins, remnants of a forgotten civilization, stand as crumbling testaments to the island's mysterious past.", "The tranquil atmosphere of Panahon invites reflection and contemplation, as if time itself has slowed to a mesmerizing crawl. Perhaps it has."]
	war = ["Fierce battles rage, factions locked in a relentless struggle for dominance, clashing swords and casting devastating spells amidst the chaos.", "The clash of steel and crackling of arcane spells reverberate through the battlefield, warriors adorned in battle-worn armor fight tooth and nail for their cause.", "The ground trembles beneath the thundering hooves of cavalry, charging forward with a thunderous force, trampling anything in their path.", "Explosions rend the earth as siege weapons rain destruction upon fortifications, crumbling stone and engulfing the air with smoke and debris. You are showered in falling dirt and debris.", "Arrows blot out the sun as they rain down upon the battlefield, finding their mark amidst the chaos, leaving trails of agony and despair in their wake.", "Mages unleash devastating spells, conjuring walls of fire and torrents of lightning, turning the battleground into a maelstrom of elemental fury.", "Healers rush through the chaos, their hands alight with restorative magic, desperately trying to mend the wounded and keep hope alive amidst the carnage.", "Through the haze of battle, fallen heroes lie in eternal slumber, their sacrifices honored by those who fight on, their memory fueling the flames of vengeance and determination.", "A berserker, fueled by rage and wielding a massive axe, cleaves through enemy ranks with reckless abandon, carving a path of destruction.", "Like a shadow, a rogue assassin darts through the chaos, silently dispatching key targets with precise strikes, vanishing into the shadows before anyone can react.", "A seasoned archer, perched on a high vantage point, unleashes a flurry of arrows that find their marks with deadly accuracy, thinning enemy numbers.", "A group of brave knights, their shields locked together, form an impenetrable wall as they push forward, repelling wave after wave of enemy assaults.", "A powerful mage, surrounded by a shimmering aura, unleashes a devastating spell that engulfs foes in searing flames, leaving nothing but charred remnants.", "A cunning tactician, barking orders with authority, directs his troops in a strategic maneuver, outflanking and encircling the enemy forces.", "A group of valiant healers, amidst the chaos, tend to the wounded, mending broken bones and closing grievous wounds, giving their allies a second chance at life.", "A fleet-footed rogue expertly disarms traps and sabotages enemy equipment, creating chaos and confusion within enemy lines.", "A fearless warrior charges headlong into the fray, deflecting incoming blows with a mighty shield and striking back with unmatched strength and precision.", "A mystical druid, in tune with nature's forces, calls forth a violent storm that unleashes torrents of rain and gusts of wind, disrupting enemy formations and sowing chaos."]
	def at_object_creation(self):
		self.db.desc = random.choice(self.normal)
		self.db.ancient = random.choice(self.ancient)
		self.db.primordial = random.choice(self.primordial)
		self.db.apocalypse = random.choice(self.apocalypse)
		self.db.normal = random.choice(self.normal)
		self.db.war = random.choice(self.war)
		self.db.warmessages = ["*THUNK* An arrow strikes you in the knee.", "Caught in the midst of the temporal shift, a barrage of arrows pierces your armor, leaving you wounded and disoriented.","The clash of steel resonates through your bones as an enemy's sword finds its mark, slashing across your arm.", "A thunderous explosion engulfs the battlefield, flinging you backward with a shockwave and leaving you with ringing ears.", "From out of nowhere, a hail of fireballs descends upon you, scorching your skin and searing your senses.", "A swift and unexpected blow from a mace crashes into your side, knocking the wind out of you and leaving you gasping for breath.", "As time warps around you, a spectral warrior materializes and delivers a devastating blow, sending you sprawling to the ground.", "The ground beneath your feet trembles as a massive boulder hurtles toward you, crashing into your legs and leaving you pinned momentarily.", "A barrage of arcane bolts lances through the air, finding their mark and leaving you dazed and disoriented.", "A sudden surge of dark energy courses through your body, draining your vitality and leaving you weakened.", "An unseen force slams into you with tremendous strength, flinging you across the battlefield and leaving you bruised and battered."]
		self.tags.add("notravel")
		self.db.fight = "no"
	def at_object_receive(self, obj, source):
		descriptions = [self.db.ancient, self.db.primordial, self.db.apocalypse, self.db.normal, self.db.war]
		self.db.desc = random.choice(descriptions)
		utils.delay(randint(2,8), self.sendmsg, obj)
	def sendmsg(self, obj):
		for i in self.contents:
			if i.key == obj.key:
				if obj.location.id == self.id:
					obj.msg("|r|/The air begins to twist and distort, sparking with small arcs of purple electricity. Time is shifting.|/|n")
					descriptions = [self.db.ancient, self.db.primordial, self.db.apocalypse, self.db.normal, self.db.war]
					self.db.desc = random.choice(descriptions)
					if self.db.desc == self.db.ancient:
						damage = randint(3, 11)
						obj.msg("|/|rYou are suddenly thrust forward in time, aging you, sapping %s hp." % int((damage)))
						obj.db.hp -= int(damage)
						if obj.db.hp <= 0:
							obj.msg("|/|rWhat tragic fate, you have died in the wild flow of time.|n|/You have brought shame to yourself and your family.")
							obj.db.deathcount += 1
							obj.db.hp = int(obj.db.maxhp * .5)
							obj.db.mp = int(obj.db.maxmp * .5)
							obj.db.gold -= int(obj.db.gold * .3)
							results = search_object(obj.db.lastcity)
							obj.move_to(results[0], quiet=True, move_hooks=False)
					if self.db.desc == self.db.war:
						obj.msg("|/|rYou find yourself suddenly in the middle of an ancient battle.|n")
						chance = randint(1, 3)
						if chance == 2:
							obj.msg(random.choice(self.db.warmessages))
							damage = randint(3, 11)
							obj.msg("|rYou take %s damage.|n" % str((damage)))
							obj.db.hp -= int(damage)
							if obj.db.hp <= 0:
								obj.msg("|/|rWhat tragic fate, you have fallen in an ancient war.|n|/You have brought shame to yourself and your family.")
								obj.db.deathcount += 1
								obj.db.hp = int(obj.db.maxhp * .5)
								obj.db.mp = int(obj.db.maxmp * .5)
								obj.db.gold -= int(obj.db.gold * .3)
								results = search_object(obj.db.lastcity)
								obj.move_to(results[0], quiet=True, move_hooks=False)
						else:
							harm = ["a sword", "a streaking fireball", "an arrow", "a bloodied axe", "a charging cavalry member", "a spear thrust at your head"]
							obj.msg("|/|gYou deftly dodge %s, avoiding injury.|n" % (random.choice(harm)))
					obj.execute_cmd('look')

class panahonfight(autofight):
	ancient = ["The Island of Panahon emanates an aura of enchantment, with sprawling forests teeming with magical creatures and ancient ruins shrouded in mystic secrets.", "Hidden within the ancient woods, mystical rituals unfold as druids commune with nature, channeling the raw power of the land to shape reality.", "Ancient spirits whisper secrets among the towering trees, guiding those who seek wisdom in the heart of the enchanted forest.", "Ethereal creatures of myth roam freely, their majestic presence filling the air with magic.", "Ancient spellcasters harness the ancient energies, their incantations echoing through the moss-covered ruins of forgotten civilizations.", "The air is thick with the scent of ancient herbs and the vibrant colors of exotic flora, creating a tapestry of natural wonder."]
	primordial = ["The echoes of a time before time resound in the dense jungles of Panahon, colossal insects reign and the air pulses with primal energy.", "The relentless chirping of exotic insects fills the air as you navigate through the dense jungle, marveling at colossal flora and the eerie calls of unseen creatures.", "The primordial jungles pulse with untamed life, the world is untouched by the hands of man.", "The air resonates with the primal calls of primordial creatures unseen, their existence a testament to the raw power of nature.", "Massive vines entwine with ancient stone, the land is uncleared and wild. A place before civilization."]
	apocalypse = ["The aftermath of cataclysm lingers, leaving scars on the land, as shattered ruins and twisted landscapes serve as haunting reminders of the chaos.", "Amidst the ruins of a shattered city, survivors scavenge for resources, always on guard for the encroaching darkness and the remnants of otherworldly forces.", "Eerie winds carry whispers of lost souls, still smoldering ruins are evidence of the devastation that befell the island.", "Unnatural phenomena manifest in the sky, casting an otherworldly glow upon the desolate landscape. A sickening magic resonance lingers in the air, magical fallout from the fracturing of time.", "The air is heavy with a sense of foreboding, as if the very essence of the island mourns its cataclysmic fate of the tearing of time.", "Shadows dance among the ruins, their ethereal forms a constant reminder of the lingering darkness that engulfs this post-apocalyptic realm."]
	normal = ["Fleeting moments of temporal stability, where time briefly aligns with the present, offering respite and glimpses of normality amid the ever-shifting nature.", "Amidst the temporal shifts, you find yourself in a moment of tranquility.", "Sunlight filters through the dense canopy, casting dappled patterns on the forest floor, creating an ethereal ambiance.", "Serene waterfalls cascade down moss-covered cliffs, their gentle roar harmonizing with the symphony of nature.", "Wildflowers paint the landscape with bursts of color, their delicate petals swaying in the gentle breeze.", "Ancient ruins, remnants of a forgotten civilization, stand as crumbling testaments to the island's mysterious past.", "The tranquil atmosphere of Panahon invites reflection and contemplation, as if time itself has slowed to a mesmerizing crawl. Perhaps it has."]
	war = ["Fierce battles rage, factions locked in a relentless struggle for dominance, clashing swords and casting devastating spells amidst the chaos.", "The clash of steel and crackling of arcane spells reverberate through the battlefield, warriors adorned in battle-worn armor fight tooth and nail for their cause.", "The ground trembles beneath the thundering hooves of cavalry, charging forward with a thunderous force, trampling anything in their path.", "Explosions rend the earth as siege weapons rain destruction upon fortifications, crumbling stone and engulfing the air with smoke and debris. You are showered in falling dirt and debris.", "Arrows blot out the sun as they rain down upon the battlefield, finding their mark amidst the chaos, leaving trails of agony and despair in their wake.", "Mages unleash devastating spells, conjuring walls of fire and torrents of lightning, turning the battleground into a maelstrom of elemental fury.", "Healers rush through the chaos, their hands alight with restorative magic, desperately trying to mend the wounded and keep hope alive amidst the carnage.", "Through the haze of battle, fallen heroes lie in eternal slumber, their sacrifices honored by those who fight on, their memory fueling the flames of vengeance and determination.", "A berserker, fueled by rage and wielding a massive axe, cleaves through enemy ranks with reckless abandon, carving a path of destruction.", "Like a shadow, a rogue assassin darts through the chaos, silently dispatching key targets with precise strikes, vanishing into the shadows before anyone can react.", "A seasoned archer, perched on a high vantage point, unleashes a flurry of arrows that find their marks with deadly accuracy, thinning enemy numbers.", "A group of brave knights, their shields locked together, form an impenetrable wall as they push forward, repelling wave after wave of enemy assaults.", "A powerful mage, surrounded by a shimmering aura, unleashes a devastating spell that engulfs foes in searing flames, leaving nothing but charred remnants.", "A cunning tactician, barking orders with authority, directs his troops in a strategic maneuver, outflanking and encircling the enemy forces.", "A group of valiant healers, amidst the chaos, tend to the wounded, mending broken bones and closing grievous wounds, giving their allies a second chance at life.", "A fleet-footed rogue expertly disarms traps and sabotages enemy equipment, creating chaos and confusion within enemy lines.", "A fearless warrior charges headlong into the fray, deflecting incoming blows with a mighty shield and striking back with unmatched strength and precision.", "A mystical druid, in tune with nature's forces, calls forth a violent storm that unleashes torrents of rain and gusts of wind, disrupting enemy formations and sowing chaos."]
	def at_object_creation(self):
		descriptions = [self.ancient, self.primordial, self.apocalypse, self.normal, self.war]
		self.db.desc = random.choice(random.choice(descriptions))
		self.db.zone = "panahon"
		self.db.fight = "yes"
		self.tags.add("autofight")
		self.tags.add("notravel")

class veiloftime(vroom):
	def at_object_creation(self):
		self.db.desc = ""
		self.db.fight = "no"
		self.tags.add("notravel")

#temples
class templeofsmallgodstunnel(iftagviewnf):
	def at_object_creation(self):
		self.db.desc = "Spiderwebs tangle around your arms and legs, stick to your face as you make your way.|/Every step is more difficult as the webs accumulate."
		self.db.tagdesc = "The temple is blessedly free of, most, of the spider webs. The one's that are there now are of the normal everyday variety.|/Disciples fuss at each nook and cranny of the temple, cleaning, polishing, painting."
		self.db.tagname = "omthemighty"
		self.db.fight = "no"

class houseofpirts(autofight):
	def at_object_creation(self):
		self.db.desc = "A massive bath with clear and gently steaming water occupies the majority of the room. Sparkling crystal mosaics cover the walls and meet up with the intricate tile patterned floor. Out of the corner of your eye you think you see the figures in the mosaics move and shift.|/An altar of a woman washing a small child stands semi submerged in the water on the north side of the room."
		#self.db.desc = "The architecture morphs before your eyes. The walls take on an organic quality, resembling the sinuous curves of serpents and twisted vines. Marble statues, once elegant and lifelike, contort into grotesque forms, their eyes seemingly following your every move."
		#self.db.desc = "The warm and inviting atmosphere quickly reveals its sinister undertones. The pools and baths, once peaceful and inviting, now appear murky and ominous. Steam rises from the darkened waters, concealing hidden perils lurking beneath the surface. The gentle trickling of water becomes an unsettling susurration, and the scent of fragrant oils transforms into a sickly sweet aroma that hints at treachery."
		#self.db.desc = "The familiar sights of a bathhouse surround you, but an eerie ambiance hangs in the air. The winding corridors are lined with ornate tiles, adorned with intricate patterns reminiscent of flowing water, and the soft echoes of distant splashes reach your ears."
		self.db.zone = "bathhouse"
		self.db.fight = "yes"
		self.tags.add("autofight")
		self.tags.add("notravel")

class houseofpirtspump(autofight):
	def at_object_creation(self):
		self.db.desc = "Nearly walking off the edge of a sheer drop off, you stand in a dark damp room. What little light is in the room reflects and dances off what must be slightly shifting water far down below.|/A very large main pipe, with dozens of smaller pipes extending from a manifold above, extends down into the water. There is a large wheel attached to the pipe."
		self.db.zone = "bathhouse"
		self.db.fight = "yes"
		self.tags.add("notravel")
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		desc = self.db.desc
		if looker.db.bathhouse['water'] == "on":
			desc += "|/The water gurgles and flows in the pit below."
		if looker.db.bathhouse['water'] == "off":
			desc += "|/The water below is relatively still and quiet."
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class houseofpirtssteam(autofight):
	def at_object_creation(self):
		self.db.desc = "Halting in your tracks, you barely avoid stumbling into what appears to be a steam room. A steam room with a gigantic tentacled creature with hundreds of eyes."
		self.db.steamy = "The path south is obscured by steam, you're not sure how large the room ahead is, if it is a room, or what lays beyond hidden among the steam."
		self.db.zone = "bathhouse"
		self.db.fight = "yes"
		self.tags.add("notravel")
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if looker.db.bathhouse['water'] == "on" and looker.db.bathhouse['pipe'] == "fixed" and looker.db.bathhouse['temp'] == "hot":
			desc = self.db.steamy
		else:
			desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class houseofpirtspipes(autofight):
	def at_object_creation(self):
		self.db.brokendesc = "The room is dark, but you make out that it is filled with twisting turning pipes. You hear water dripping."
		self.db.fixeddesc = "The room is dark, but you make out that it is filled with twisting turning pipes. The water is no longer dripping."
		self.db.fixedwateron = "The room is dark, but you make out that it is filled with twisting turning pipes. You hear water rushing through the pipes."
		self.db.desc = "Something has gone wrong, contact Blakhal0"
		self.db.zone = "bathhouse"
		self.db.fight = "yes"
		self.tags.add("autofight")
		self.tags.add("notravel")
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		if looker.db.bathhouse['pipe'] == "fixed" and looker.db.bathhouse['water'] == "on":
			desc = self.db.fixedwateron
		elif looker.db.bathhouse['pipe'] == "fixed":
			desc = self.db.fixeddesc
		elif looker.db.bathhouse['pipe'] == "broken":
			desc = self.db.brokendesc
		else:
			desc = self.db.desc
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class houseofpirtboiler(autofight):
	def at_object_creation(self):
		self.db.desc = "The many pipes in the ceiling all lead to a large pot bellied boiler in the center of the room."
		self.db.wateron = "|/You hear water flowing through some of the pipes, pouring into the boiler."
		self.db.cold = "|/The boiler is still, the air in the room is damp and cool."
		self.db.warm = "|/The boiler gives off a mild warmth, not enough to take the slight chill out of the air."
		self.db.hot = "|/The boiler gives off a radiant heat, warming the air in the chamber."
		self.db.zone = "bathhouse"
		self.db.fight = "yes"
		self.tags.add("autofight")
		self.tags.add("notravel")
	def return_appearance(self, looker):
		if not looker:
			return ""
		visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
		exits, users, npc, things = [], [], [], []
		for con in visible:
			key = con.get_display_name(looker, pose=True)
			if con.destination:
				exits.append(key)
			elif con.tags.get("specialexit"):
				exits.append(key)
			elif con.tags.get("specialnpc"):
				npc.append(key)
			elif con.permissions.get("player"):
				if con.has_account:
					users.append(key)
			elif con.tags.get("talkative", category="npc"):
				if not con.tags.get("specialobject"):
					npc.append(key)
				else:
					things.append(key)
			elif con.tags.get("evnpc"):
				npc.append(key)
			else:
				things.append(key)
		string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
		desc = str()
		desc = self.db.desc
		if looker.db.bathhouse['water'] == "on":
			desc += self.db.wateron
		if looker.db.bathhouse['temp'] == "cold":
			desc += self.db.cold
		if looker.db.bathhouse['temp'] == "warm":
			desc += self.db.warm
		if looker.db.bathhouse['temp'] == "hot":
			desc += self.db.hot
		if desc:
			string += "%s" % desc
			string += "\n\nYou cast your gaze upon the area:"
		if exits:
			string += "\n|025Exits:|n " + ", ".join(exits)
		if users:
			string += "\n|550Players:|n " + ", ".join(users)
		if npc:
			string += "\n|520NPC's:|n " + ", ".join(npc)
		if things:
			string += "\n|050Objects:|n " + ", ".join(things)
		return string

class sandsweptshrine(autofight):
	def at_object_creation(self):
		#self.db.desc = "You find yourself standing above the abyss, sand pouring off the edges of the platform and the path leading to it. You're not sure how, but you are not falling. You see nothing below or around you."
		#self.db.desc = "A massive statue of Smilsu, the Mother Goddess of Sands, looms in the center of a platform, her visage stern and unyielding.|/The sand slowly pours over the edges of the platform, never diminishing yet always flowing."
		#self.db.desc = "The winding corridors of the shrine are carved from sun-baked stone, their surfaces bear weathered etchings with intricate hieroglyphs that depict tales of power and divine intervention."
		#self.db.desc = "The winding corridors of the shrine are carved from sun-baked stone, their surfaces bear weathered etchings with intricate hieroglyphs that depict tales of power and divine intervention. As you make your way through the shrine you encounter chambers adorned with elaborate carvings of desert creatures and intricate patterns mimicking shifting sands."
		self.db.zone = "sandshrine"
		self.db.fight = "yes"
		self.tags.add("autofight")
		self.tags.add("notravel")

class whisperingglade(autofight):
	def at_object_creation(self):
		self.db.desc = "Nestled within the verdant embrace of nature, is a place of ethereal beauty and untamed wilderness. The canopy of towering trees opens in places to reveal a calm blue sky above you, the forest floor is dappled with sunlight filtering through the lush green foliage above. The air is alive with the melodies of birdsong and the gentle rustling of leaves."
		self.db.zone = "forestshrine"
		self.db.fight = "yes"
		self.tags.add("autofight")
		self.tags.add("notravel")

class tirgusmarket(vroom):
	def at_object_creation(self):
		self.db.desc = "Vibrant fabrics and hanging tapestries create the walls and shade covers of the tents, a kaleidoscope of hues that fills the air with an atmosphere of excitement and delight.|/At every turn, there is an array of amazing goods on display. Silks, jewels, baubles, spices, herbs, meats, sweets, artwork, trinkets, exotic critters, rugs, clothes, and every other possible thing you can imagine.|/As you wander through the market, you are immersed in a sensory extravaganza, with the sounds of merchants haggling, the colorful displays of wares, and the tantalizing scents of spices and delicacies."
		self.db.fight = "no"
		self.tags.add("notravel")

class tirgusmarketstall(vroom):
	def at_object_creation(self):
		self.db.desc = "The merchant stall displays the many wares they offer."
		self.db.fight = "no"
		self.tags.add("notravel")

class yororvik(vroom):
	def at_object_creation(self):
		self.db.desc = "Dozens of streams of smoke rise into the air, the smell of incense and burning flesh fills the air. Funeral pyres everywhere upon which lay the bodies of fallen soldiers, Valaharran and others alike. The air is hot and dry."
		self.db.fight = "no"
		self.tags.add("notravel")

class balheim(vroom):
	def at_object_creation(self):
		self.db.desc = "Stairs climb up and up the temple a dark fusion of bone and fire. Walls constructed from stacked femurs and skulls, decorated with mosaics of dyed bone depicting funeral fires and demonic planes of existence."
		self.db.fight = "no"
		self.tags.add("notravel")