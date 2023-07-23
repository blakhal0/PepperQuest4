from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class chatgreeter(default_cmds.MuxCommand):
	key = "talk greeter"
	aliases = ["Talk Greeter", "Talk greeter", "talk Greeter"]
	auto_help = True
	def func(self):
		self.caller.msg("|/|mGreeter|n says: Hey, welcome to the Eternal Bazaar, I love you.")
		self.caller.msg("|mGreeter|n says: Now listen up hear now, this is the Eternal Bazaar, we don't take no alternate reality fibbity fobbity gold here, we're an advanced and financially independent market not tethered to minerals ripped from the earth. We use Pepper Coin.")
		self.caller.msg("The Greeter hands you 50 Pepper Coin tokens.")
		self.caller.msg("|mGreeter|n says: And you're gonna need something to put all your stuff in so you're going to need this.")
		self.caller.msg("You receive THE sweetest, most excellent, tubular, BOMB-ASS fanny pack.")
		self.caller.msg("|mGreeter|n says: Compliments of the Goddess Tirgus and the Eternal Bazaar. You'll need to turn it back in before you go.")
		self.caller.msg("|mGreeter|n says: Hey, HEY! You listening? Good, listen up real good. The stuff here in the market, it only exists on this plane of reality, you don't get to take it with ya when you leave. Now, I don't want to hear no belly aching about it. That's just the way it is.")
		self.caller.msg("|mGreeter|n says: Now, should you want to LEAVE our fine market, being as eternal as it is, you gotta do something about it, you can't just walk out. IT'S ETERNAL, you mopping up what I'm spilling? I'm telling you there ain't no way out excepting you decide to leave, or you impress the Goddess. So if you wanna leave you gotta |cLeave Market|n. You'll turn in your fanny pack and all Pepper Coins you've made as well as any purchases will cease to exist.")
		self.caller.msg("|mGreeter|n says: Speaking of that sick bomb diggity article of holding. If you wanna check how many Pepper Coins you have and the stuff you've purchased you can |cCheck Pack|n. It's magical, so you can cram as much stuff as you want in there. Go to town, it's a market. Plenty of stuff to buy.")
		while 1 > 0:
			answer = yield("|/|mGreeter|n says: Alright, you ready to head into the market?|/|cY|nes, |cN|no")
			if answer.lower() in ["y", "yes"]:
				break
			else:
				self.caller.msg("|mGreeter|n says: .... okaaaaay. Howboutnow?")
				continue
		self.caller.db.tirgusmarket ={'foolsgold': 50}
		safp_proto = {
		"key": "Fanny Pack",
		"typeclass": "typeclasses.fannypack.fannypack",
		"location": self.caller
		}
		spawn(safp_proto)
		results = search_object("#12752")
		self.caller.move_to(results[0], quiet=True, move_hooks=True)


class GreeterCmdSet(CmdSet):
	key = "GreeterCmdSet"
	def at_cmdset_creation(self):
		self.add(chatgreeter())

class greeter(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A smiling old man in a green vest reading 'Welcome to the Eternal Bazaar'."
		self.cmdset.add_default(GreeterCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")