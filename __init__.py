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
         sqb5naomi(ml)
         
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
           .hook_to("sqb_naomi_m2_skip", condition='sqbpremounlocked ==  True')
            
       ml.find_label("eck_naomi_m2") \
           .search_menu("I can imagine.") \
           .add_choice(text="I could move them for you.", condition='sqbpremounlocked == True', jump="sqb_naomi_m2_chairs") \
           .search_scene("ecknaomiapt03") \
           .link_behind_from("sqb_naomi_m2_chairs_end") \
           .search_say("We all have drawbacks") \
           .hook_to("sqb_naomi_m2_differences", condition='sqbpremounlocked == True') \
           .search_say("Naomi eyed my legs") \
           .link_from("sqb_naomi_m2_differences_end") \
           .search_say("I was met by a light gust") \
           .hook_to("sqb_naomi_m2_balcony", condition='sqbpremounlocked ==  True') \
           .search_say("Beautiful, isn't it?") \
           .link_from("sqb_naomi_m2_balcony_end") \
           .search_say("Of course, he meant no harm") \
           .search_say("Sounds uncomfortable.") \
           .hook_to("sqb_naomi_m2_movie", condition='sqbpremounlocked ==  True') \
           .search_say("You said you like") \
           .link_from("sqb_naomi_m2_origmovie_end") \
           .search_say("A couple of hours later") \
           .link_from("sqb_naomi_m2_movie_end") \
           .search_say("Do you have anyone in mind") \
           .hook_to("sqb_naomi_m2_bedroomfun", condition='sqbpremounlocked ==  True and naomi2mood > 5 and sqbnaomilewd > 3') \
           .search_show("naomi blank") \
           .link_from("sqb_naomi_m2_kiss_orig_end") \
           .search_say("Sounds like a plan") \
           .link_from("sqb_naomi_m2_cooking_orig_end")
           
           
       ml.find_label("sqb_naomi_m2_bedroomfun") \
           .search_say("A whisper coming from") \
           .search_say("I picked up my clothes") \
           .search_say("Have you thought of what") \
           .search_say("I think we've had enough foreplay") \
           .link_from("sqb_naomi_m2_sexskip_end")
       
       n = ml.find_label("sqb_naomi_m2_bedroomfun") \
           .search_say("A whisper coming from") \
           .search_say("I picked up my clothes") \
           .search_if("persistent.nsfwtoggle == False").branch() \
           .search_python("renpy.pause (2.0)") \
           .search_python("renpy.pause (2.0)")
       n.search_say("After a moment of silence") \
           .search_say("Can you see the slit") \
           .search_say("That's just what someone") \
           .search_say("I can't understate how much fun") \
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
            .hook_to("sqb_naomi_m4_skip", condition='sqbnaomi2hadsex == True')

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
            .link_from("sqb_naomi_m4_interspecies_end")
            
       ml.find_label("eck_naomi_m4_skip") \
            .search_say("It's getting late") \
            .hook_to("sqb_naomi_m4_funparts", condition='sqbnaomi2hadsex == True') \
            .search_if("naomiromance > 11").branch() \
            .search_menu("Accept.").branch() \
            .search_say("We were reunited in our") \
            .hook_to("sqb_naomi_m4_fun_orig", condition='persistent.nsfwtoggle == True')
              
       ml.find_label("eck_naomi_m4_takingitslow") \
            .search_menu("Accept.").branch() \
            .search_menu("Caress her neck and chest.").branch() \
            .search_menu("Kiss her.").branch() \
            .search_menu("Take things further.").branch() \
            .search_say("We were reunited in our") \
            .hook_to("sqb_naomi_m4_fun_orig2", condition='persistent.nsfwtoggle == True')
            
def sqb5naomi(ml):

       ml.find_label("eck_naomi_m5") \
            .search_say("This might be our only chance") \
            .search_say("Since when do you") \
            .hook_to("sqb_naomi_m5_rezatalk1", condition='sqbnaomim4hadsex == True') \
            .search_say("Just let me through") \
            .link_from("sqb_naomi_m5_rezatalk1_end") \
            .search_say("As long as you can") \
            .hook_to("sqb_naomi_m5_rezatalk2", condition='sqbnaomim4hadsex == True') \
            .search_say("I mean, what are you going to") \
            .link_from("sqb_naomi_m5_rezatalk2_end")
            
       ml.find_label("eck_naomi_m5_betterend") \
            .search_say("Waiting for a special") \
            .hook_to("sqb_naomi_m5_rezatalk3", condition='sqbnaomim4hadsex == True') \
            .search_say("Looks like your friends") \
            .link_from("sqb_naomi_m5_rezatalk3_end") \
            .search_play("fx/box1.wav") \
            .hook_to("sqb_naomi_m5_rezafight", condition='sqbnaomim4hadsex == True') \
            .search_say("As long as you stay true") \
            .link_from("sqb_naomi_m5_rezafight_end") \
            .search_say("You are good at reading others") \
            .hook_to("sqb_naomi_m5_maverick", condition='sqbnaomim4hadsex == True') \
            .search_say("Maverick lifted his arm") \
            .link_from("sqb_naomi_m5_maverick_end") \
            .search_say("I gasped and took a step back") \
            .hook_to("sqb_naomi_m5_ending", condition='sqbnaomim4hadsex == True')
            
       ml.find_label("eck_naomi_m5_betterend_aftermath") \
            .search_say("Hey.") \
            .hook_to("sqb_naomi_m5_aftermath", condition='sqbnaomim4hadsex == True')
            