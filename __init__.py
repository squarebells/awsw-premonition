from modloader import modast, modinfo
from modloader.modclass import Mod, loadable_mod
import jz_magmalink as ml
import renpy.ast as ast
import renpy.parser as parser

@loadable_mod
class Premonition(Mod):
    name = "Premonition"
    version = "1.0"
    author = "squarebells"
    dependencies = ["MagmaLink", "A Solitary Mind", "Chaos_Knight core mod.", "CRAP", "?BangOk?"]
    nsfw = True
    
    @classmethod
    def mod_load(cls):
         sqbnaomistatus(ml)
         sqbintronaomi(ml)
         sqb1naomi(ml)
         sqb2naomi(ml)
         sqb3naomi(ml)
         sqb4naomi(ml)
         #sqb5naomi(ml)
         #sqb6naomi(ml)
         
    @staticmethod
    def mod_complete():
        pass

def sqbnaomistatus(ml):

      ml.StatusBox("naomiscenesfinished", condition="persistent.naomimet") \
          .add_status("image/ui/status/naomigf.png", "Girlfriend", "naomistatus == \"girlfriend\"") \
          .build()
          
def sqbintronaomi(ml):
    
      ml.find_label("eck_naomi_introduction") \
          .search_say("As I was passing through") \
          .hook_to("sqb_naomi_endingcheck", condition='persistent.ecknaomiendingseena == "A"') \
          .search_say("Before I knew it") \
          .link_from("sqb_naomi_endingcheck_end") \
          .search_say("Let me help.") \
          .hook_to("sqb_naomi_premostart", condition='sqbpremounlocked == True') \
          .search_say("I read the reports") \
          .link_from("sqb_naomi_premostart_end")
       
def sqb1naomi(ml):
       ml.find_label("eck_naomi_m1") \
           .search_say("You're also working on the latest case, I assume") \
           .search_say("For me it's more of a personal thing") \
           .search_say("To make things worse, when I submitted those documents") \
           .search_say("What would you like") \
           .search_say("What about drinks?") \
           .hook_to("sqb_naomi_cafe_discussion", condition='sqbpremounlocked == True') \
           .search_say("I'm the analyst.") \
           .link_from("sqb_naomi_cafe_discussion_end") \
           .search_say("Soon, her plate") \
           .hook_to("sqb_naomi_cafe_eating", condition='sqbpremounlocked == True') \
           .search_say("It happens sometimes") \
           .link_from("sqb_naomi_cafe_eating_end") \
           .search_say("...") \
           .hook_to("sqb_naomi_cafe_money", condition='sqbpremounlocked == True') \
           .search_say("Of course, we haven't") \
           .link_from("sqb_naomi_cafe_money_end") \
           .search_say("Do you have any specific places") \
           .search_say("Don't you have friends") \
           .hook_to("sqb_naomi_special_question", condition='sqbpremounlocked == True') \
           .search_say("I know what you mean") \
           .link_from("sqb_naomi_special_question_end")

def sqb2naomi(ml):

       ml.find_label("_call_skiptut_eckn21") \
            .search_menu("Yes. I want to skip ahead.").branch() \
            .hook_to("sqb_naomi_m2_skip", condition='sqbpremounlocked ==  True') \
            
       ml.find_label("sqb_naomi_m2_bedroomfun") \
            .search_say("I hope you understand that") \
            .search_say("I picked up my clothes") \
            .search_say("Her remark made me feel") \
            .search_say("Alright, we've had enough foreplay") \
            .link_from("sqb_naomi_m2_sexskip_end")
            
       ml.find_label("eck_naomi_m2") \
           .search_menu("I can imagine.") \
           .add_choice(text="I could move them for you.", condition='sqbpremounlocked == True', jump="sqb_naomi_m2_chairs") \
           .search_say("She led me") \
           .link_behind_from("sqb_naomi_m2_chairs_end") \
           .search_say("We all have drawbacks") \
           .hook_to("sqb_naomi_m2_differences", condition='sqbpremounlocked == True') \
           .search_say("Naomi eyed my legs") \
           .link_from("sqb_naomi_m2_differences_end") \
           .search_say("I was met by a light gust") \
           .hook_to("sqb_naomi_m2_balcony", condition='sqbpremounlocked == True') \
           .search_say("Beautiful, isn't it?") \
           .link_from("sqb_naomi_m2_balcony_end") \
           .search_say("Of course, he meant no harm") \
           .search_say("Sounds uncomfortable.") \
           .hook_to("sqb_naomi_m2_movie", condition='sqbpremounlocked == True') \
           .search_say("A couple of hours later") \
           .link_from("sqb_naomi_m2_movie_end") \
           .search_say("Do you have anyone in mind") \
           .hook_to("sqb_naomi_m2_bedroomfun", condition='sqbpremounlocked == True and naomi2mood > 8 and naomilewd > 4') \
           .search_say("I guess we should get going") \
           .link_from("sqb_naomi_m2_bedroomfun_end")
           
       n = ml.find_label("sqb_naomi_m2_bedroomfun") \
           .search_say("I hope you understand that") \
           .search_say("I picked up my clothes") \
           .search_say("Her remark made me feel") \
           .search_say("Do you really want to go further with me") \
           .search_if("persistent.nsfwtoggle == False").branch() \
           .search_play("mx/airborne.mp3")
       n.search_say("Can you see the slit") \
           .search_say("Finish if you have to") \
           .search_say("It was certainly") \
           .hook_from_node(n)
           
def sqb3naomi(ml):
       
       ml.find_label("eck_naomi_m3_startchoice") \
            .search_menu("Not interested.").branch() \
            .search_say("I never liked water") \
            .search_say("Just have fun without me") \
            .hook_to("sqb_naomi_m3_norefusal", condition='sqbnaomi2hadsex ==  True')
       
       ml.find_label("eck_naomi_m3_start") \
            .search_say("Uh, probably a minute") \
            .hook_to("sqb_naomi_m3_tail", condition='sqbnaomi2hadsex ==  True') \
            .search_say("Really? I thought your people") \
            .link_from("sqb_naomi_m3_tail_end") \
            .search_say("Um... do you mind") \
            .hook_to("sqb_naomi_m3_undressing", condition='sqbnaomi2hadsex ==  True') \
            .search_say("So, how are your preparations") \
            .link_from("sqb_naomi_m3_undressing_end") \
            .search_say("The way you swim") \
            .search_say("A large metal doorframe") \
            .search_say("I'm responsible for your security") \
            .hook_to("sqb_naomi_m3_explorationforce", condition='sqbnaomi2hadsex ==  True')

       ml.find_label("_call_skiptut_eckn32") \
            .search_menu("Yes. I want to skip ahead.").branch() \
            .hook_to("sqb_naomi_m3_templabskip", condition='sqbnaomi2hadsex ==  True')
       
       ml.find_label("eck_naomi_m3_early_leave") \
            .search_scene("beach") \
            .hook_to("sqb_naomi_m3_labteleport", condition='sqbnaomi2hadsex ==  True')
       
       ml.find_label("eck_naomi_m3_biolabalert") \
            .search_say("Be advised, prolonged") \
            .hook_to("sqb_naomi_m3_biolabalert", condition='sqbnaomi2hadsex ==  True')
            
       ml.find_label("eck_naomi_m3_panicmenu") \
            .search_menu("Snuggle up with Naomi and surrender to your fate.") \
            .edit_choice(text="Snuggle up with Naomi and surrender to your fate.", condition='sqbnaomim3nogiveup == False and sqbnaomi2hadsex == True and ecknaomim3boomstop == False' ).branch() \
            .search_python("renpy.pause (0.5)") \
            .hook_to("sqb_naomi_m3_nogiveup")
            
       ml.find_label("eck_naomi_m3_panicmenu") \
            .search_menu("Check on the entrance.").branch() \
            .hook_to("sqb_naomi_m3_panicdoor", condition='sqbnaomi2hadsex ==  True and ecknaomim3boomstop == False')
       
       ml.find_label("eck_naomi_m3_panicterminalman") \
            .search_menu("Maintenance.").branch() \
            .search_say("There were several more pages") \
            .hook_to("sqb_naomi_m3_panicterminal", condition='sqbnaomi2hadsex == True')
       
       ml.find_label("eck_naomi_m3_escape") \
            .search_say("I'd say we swim") \
            .hook_to("sqb_naomi_m3_ending", condition='sqbnaomi2hadsex == True')

def sqb4naomi(ml):

       ml.find_label("_call_skiptut_eckn41") \
            .search_menu("Yes. I want to skip ahead.").branch() \
            .hook_to("sqb_naomi_m4_skip", condition='sqbpremounlocked ==  True') \

       ml.find_label("eck_naomi_m4") \
            .search_if("ecknaomim3earlyleave").branch_else() \
            .search_if("brycedead").branch_else() \
            .search_if("naomiromance > 2").branch() \
            .hook_to("sqb_naomi_m4_start", condition='sqbnaomi2hadsex == True') \
            .search_show("sebastian drop b flip") \
            .link_from("sqb_naomi_m4_start_end") \
            .search_say("Oh well. I don't need") \
            .hook_to("sqb_naomi_m4_pool", condition='sqbnaomi2hadsex == True') \
            .search_say("Peace and quiet") \
            .link_from("sqb_naomi_m4_pool_end") \
            .search_say("Things could've been better, of course.") \
            .hook_to("sqb_naomi_m4_meetinghumans", condition='sqbnaomi2hadsex == True') \
            .search_say("Come to think of it") \
            .link_from("sqb_naomi_m4_meetinghumans_end") \
            .search_say("I sure hope so.") \
            .hook_to("sqb_naomi_m4_returndiscussion", condition='sqbnaomi2hadsex == True') \
            .search_say("Can't wait to see what") \
            .link_from("sqb_naomi_m4_returndiscussion_end") \
            .search_say("Go ahead") \
            .search_menu() \
            .add_choice(text="To interspecies relationships.", condition='sqbnaomi2hadsex == True', before="To our friendship.") \
            .hook_to("sqb_naomi_m4_interspecies", condition='sqbnaomi2hadsex == True') \
            .search_say("Our cups are almost dry") \
            .link_from("sqb_naomi_m4_interspecies_end") \
            
       ml.find_label("eck_naomi_m4_skip") \
            .search_say("It's getting late") \
            .hook_to("sqb_naomi_m4_funparts", condition='sqbnaomi2hadsex == True')

#def sqb6naomi(ml):      

        #ml.find_label("") \
        #.search_say("") \
        #.search_say("") \
        #.hook_to("sqb_naomi_m6_discussion_reality", condition='sqbpremounlocked == True') \
        #.search_say("") \
        #.link_from("sqb_naomi_m6_discussion_reality_end")      