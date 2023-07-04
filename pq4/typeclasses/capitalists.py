from evennia import default_cmds, CmdSet, gametime
from typeclasses.objects import DefaultObject

class chatcapitalists(default_cmds.MuxCommand):
	key = "talk capitalists"
	aliases = ["Talk Capitalists", "Talk capitalists", "talk Capitalists" ]
	auto_help = True
	def func(self):
		if self.caller.tags.get("dockmaster"):
			self.caller.msg("|/|mLady Catherine|n says: Goodness, you've returned... how wonderful. And just in time, the docks project is complete!")
			self.caller.msg("Lady Catherine snaps her fingers and you're shuffled away from the table.")
			self.caller.msg("|mLady Catherine|n says: Surely you're excited to go see what your investment has born. Ta-ta!!")
			return
		elif not self.caller.db.docktimer:
			self.caller.msg("|/|mLord Reginald|n says: Ah, %s, we have a proposition of utmost importance for you. You see, we find ourselves in possession of a once-thriving shipping docks that has fallen into disrepair. We believe that with your expertise and daring spirit, we can restore its former glory." % (self.caller.key))
			self.caller.msg("|mLady Catherine|n says: We seek investors of intrepid spirit to assist the restoration efforts. We believe you are the key to breathing new life into our dilapidated docks.")
			self.caller.msg("|mLord Reginald|n says: Fear not, intrepid soul, for we are prepared to invest, *ehrm* similar amounts to finance the revitalization. We recognize the potential for great returns on this enterprise.")
			self.caller.msg("|mLady Elizabeth|n says: Please rest assured, your dedication shall not go unrewarded. Once the docks are restored and flourishing, you shall have free access to the finest ship in our fleet—the Silver Sun. You will be free to use it anytime, allowing you to explore the vast seas and distant lands at your leisure, free of cost.")
			self.caller.msg("|mLord Reginald|n says: Rest assured, valiant adventurer, we shall not let your efforts go unnoticed. The thriving trade that will flow through the revitalized docks will be felt by all in the city, the country even. Your name shall be directly tied to the prosperity of this venture.")
			self.caller.msg("|mLady Catherine|n says: We have engaged the finest architects, engineers, and specialists to oversee the restoration process. They shall ensure that every obstacle is overcome, and every risk is minimized. Our dedication to this project is unwavering.")
			self.caller.msg("The entire table looks at you.")
			self.caller.msg("|m%s|n says: So... what's all this going to cost?" % (self.caller.key))
			self.caller.msg("|mLord Reginald|n says: *ehrm* Well, *ehrm* you see the financial resources needed are somewhat *ehrm* *uh* significant, you understand. *Ehrm* The quantity put in will show in the quality output, it's not a cost, as such, it's an INVESTMENT!")
			self.caller.msg("|m%s|n says: Uh-huh, right, of course, investment. So... what's all this going to cost?" % (self.caller.key))
			self.caller.msg("|mLady Catherine|n says: Twenty thousand gold.")
			self.caller.msg("|m%s|n says: And my share of the profits from the docks?" % (self.caller.key))
			self.caller.msg("The capitalists share a short glance at each other.")
			self.caller.msg("|mLady Elizabeth|n says: Well surely, being such a well traveled person, you just MUST understand that these type of investments often take a great many years to finally make a return and that the real value comes in the form of recognition and adoration from the, well, the, *cough* the less fortunate. And there's the ship, which will undeniably be of a great value to someone of your, uhh, profession. We would feel just terrible if something unfortunate happened to you on your adventures before you could be paid back in full. Truly, having all that gold tied up for such a long time does bring a terrible ache to ones head. We wouldn't wish that upon you, better for us to bear the burden and suffer that unpleasantness.")
			if self.caller.db.gold < 20000:
				self.caller.msg("|mLady Catherine|n says: Eghads! Reginald, Elizabeth *whispers* i believe they are a poor person, a peasant, lacking in financial resources.")
				self.caller.msg("The entire table recoils from you slightly.")
				self.caller.msg("|mLord Reginald|n says: I fear that perhaps there's been a mistake here. The financial requirements for this venture appear to be well out of your grasp at current. We hope you well on your adventures and if things should pan out well for you, please keep us in mind.")
				self.caller.msg("Lord Reginald snaps their fingers and you're shuffled off away from their table by a couple goons.")
				return
			else:
				answer = yield("|/|mLord Reginald|n says: So how about it, old bean, shall we strike the deal and sign the documents now?|/|gY|nes, |gN|no")
				if answer.lower() in ["y", "yes"]:
					self.caller.db.gold -= 20000
					self.caller.msg("|/|mLord Reginald|n says: Magnificent!! Simply magnificent. We'll make sure the funds go to where they're needed toot sweet. Feel free to stop by the docks and observe the poor, err, laborers well laboring. It will take a good amount of time to complete the project. Go about your adventures and stop back occasionally to check the progress.")
					self.caller.db.docktimer = int(gametime.runtime())
					return
				else:
					self.caller.msg("|/|mLord Reginald|n says: I must say, this is a disappointment. A terrible disappointment. Well, nothing for it I imagine. No need to cry Reg, stiff upper lip.. *Ehrm* Best to you, should you change your mind please come back to see us.")
					return
		elif int(self.caller.db.docktimer) + 1200 >= int(gametime.runtime()):
			self.caller.msg("|/|mLord Reginald|n says: *Ehrm* Oh, well, I do say, you've returned. How... wonderful. The docks projects are well underway, but there is still much to do. Please, continue on your adventures and stop back again... or just go to the docks to check the progress. I'm sure that would be much more convenient for you.")
			self.caller.msg("Lord Reginald snaps their fingers and you're shuffled off away from their table by a couple goons.")
			return
		elif int(self.caller.db.docktimer) + 1200 < int(gametime.runtime()):
			self.caller.msg("|/|mLady Catherine|n says: Goodness, you've returned... how wonderful. And just in time, the docks project is complete!")
			self.caller.msg("Lady Catherine snaps her fingers and you're shuffled away from the table.")
			self.caller.msg("|mLady Catherine|n says: Surely you're excited to go see what your investment has born. Ta-ta!!")
			if not self.caller.tags.get("dockmaster"):
				self.caller.tags.add("dockmaster")
			return
		else:
			self.caller.msg("Something has gone horribly wrong, let blakhal0 know there's an issue at the docks.")
			return

class CapitalistsCmdSet(CmdSet):
	key = "CapitalistsCmdSet"
	def at_cmdset_creation(self):
		self.add(chatcapitalists())

class capitalists(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A group of well dressed fancy folks sit around a private table drinking high end liquor from crystal glasses and smoking cigars and pipes."
		self.tags.add("specialnpc")
		self.cmdset.add_default(CapitalistsCmdSet, permanent=True)
		self.locks.add("get:false()")