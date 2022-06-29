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
          .link_from("sqb_naomi_endingcheck_end")
      
      ml.find_label("eck_naomi_introduction") \
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
           .link_from("sqb_naomi_cafe_discussion_end")
            
       ml.find_label("eck_naomi_m1") \
           .search_say("You're also working on the latest case, I assume") \
           .search_say("For me it's more of a personal thing") \
           .search_say("To make things worse, when I submitted those documents") \
           .search_say("What would you like") \
           .search_say("What about drinks?") \
           .search_say("Soon, her plate") \
           .hook_to("sqb_naomi_cafe_eating", condition='sqbpremounlocked == True') \
           .search_say("It happens sometimes") \
           .link_from("sqb_naomi_cafe_eating_end")
            
       ml.find_label("eck_naomi_m1") \
           .search_say("You're also working on the latest case, I assume") \
           .search_say("For me it's more of a personal thing") \
           .search_say("To make things worse, when I submitted those documents") \
           .search_say("What would you like") \
           .search_say("What about drinks?") \
           .search_say("...") \
           .hook_to("sqb_naomi_cafe_money", condition='sqbpremounlocked == True') \
           .search_say("Of course, we haven't") \
           .link_from("sqb_naomi_cafe_money_end")
            
       ml.find_label("eck_naomi_m1") \
           .search_say("You're also working on the latest case, I assume") \
           .search_say("For me it's more of a personal thing") \
           .search_say("To make things worse, when I submitted those documents") \
           .search_say("What would you like") \
           .search_say("What about drinks?") \
           .search_say("...") \
           .search_say("Do you have any specific places") \
           .search_say("Don't you have friends") \
           .hook_to("sqb_naomi_special_question", condition='sqbpremounlocked == True') \
           .search_say("I know what you mean") \
           .link_from("sqb_naomi_special_question_end")

def sqb2naomi(ml):

       ml.find_label("_call_skiptut_eckn21") \
            .search_menu("Yes. I want to skip ahead.").branch() \
            .hook_to("sqb_naomi_m2_sexskip", condition='sqbpremounlocked ==  True and persistent.sqbnaomi2sex == True') \
            
       ml.find_label("sqb_naomi_m2_bedroomfun") \
            .search_say("I hope you understand that") \
            .search_say("I picked up my clothes") \
            .search_say("Her remark made me feel") \
            .search_say("Alright, we've had enough foreplay") \
            .search_say("As I got more used") \
            .search_say("It was certainly fun") \
            .link_from("sqb_naomi_m2_sfwskip_end")
            
       ml.find_label("sqb_naomi_m2_bedroomfun") \
            .search_say("I hope you understand that") \
            .search_say("I picked up my clothes") \
            .search_say("Her remark made me feel") \
            .search_say("Alright, we've had enough foreplay") \
            .link_from("sqb_naomi_m2_sexskip2_end")

       ml.find_label("sqb_naomi_m2_bedroomfun") \
           .search_say("I hope you understand that") \
           .search_say("I picked up my clothes") \
           .search_say("Her remark made me feel") \
           .search_say("So, could you fully") \
           .search_say("Finish if you have to") \
           .search_say("It was certainly fun to") \
           .search_say("Oh, you're hungry") \
           .hook_to("sqb_naomi_m2_foodskip", condition='sqbpremounlocked == True') \

       ml.find_label("eck_naomi_m2") \
           .search_menu("I can imagine.") \
           .add_choice(text="I could move them for you.", condition='sqbpremounlocked == True', jump="sqb_naomi_m2_chairs") \
           .search_say("She led me") \
           .link_behind_from("sqb_naomi_m2_chairs_end")
       
       ml.find_label("eck_naomi_m2") \
           .search_say("We all have drawbacks") \
           .hook_to("sqb_naomi_m2_differences", condition='sqbpremounlocked == True') \
           .search_say("Naomi eyed my legs") \
           .link_from("sqb_naomi_m2_differences_end")
           
       ml.find_label("eck_naomi_m2") \
           .search_say("We all have drawbacks") \
           .search_say("I was met by a light gust") \
           .hook_to("sqb_naomi_m2_balcony", condition='sqbpremounlocked == True') \
           .search_say("Beautiful, isn't it?") \
           .link_from("sqb_naomi_m2_balcony_end")
        
       ml.find_label("eck_naomi_m2") \
           .search_say("We all have drawbacks") \
           .search_say("I was met by a light gust") \
           .search_say("Of course, he meant no harm") \
           .search_say("Sounds uncomfortable.") \
           .hook_to("sqb_naomi_m2_movie", condition='sqbpremounlocked == True') \
           .search_say("A couple of hours later") \
           .link_from("sqb_naomi_m2_movie_end")
           
       ml.find_label("eck_naomi_m2") \
           .search_say("We all have drawbacks") \
           .search_say("I was met by a light gust") \
           .search_say("Of course, he meant no harm") \
           .search_say("Sounds uncomfortable.") \
           .search_say("A couple of hours later") \
           .search_say("Do you have anyone in mind") \
           .hook_to("sqb_naomi_m2_bedroomfun", condition='sqbpremounlocked == True and naomi2mood > 8 and naomilewd > 4') \
           .search_say("I guess we should get going") \
           .link_from("sqb_naomi_m2_bedroomfun_end")
           
def sqb3naomi(ml):
       
       ml.find_label("eck_naomi_m3_startchoice") \
            .search_menu("Not interested.").branch() \
            .search_say("I never liked water") \
            .search_say("Just have fun without me") \
            .hook_to("sqb_naomi_m3_norefusal", condition='sqbpremounlocked ==  True') \
       
       ml.find_label("eck_naomi_m3_start") \
            .search_say("Uh, probably a minute") \
            .hook_to("sqb_naomi_m3_tail", condition='sqbpremounlocked ==  True') \
            .search_say("Really? I thought your people") \
            .link_from("sqb_naomi_m3_tail_end")
       
       ml.find_label("eck_naomi_m3_start") \
            .search_say("Um... do you mind") \
            .hook_to("sqb_naomi_m3_undressing", condition='sqbpremounlocked ==  True') \
            .search_say("So, how are your preparations") \
            .link_from("sqb_naomi_m3_undressing_end")
       
       ml.find_label("eck_naomi_m3_start") \
            .search_say("Um... do you mind") \
            .search_say("The way you swim") \
            .search_say("A large metal doorframe") \
            .search_say("I'm responsible for your security") \
            .hook_to("sqb_naomi_m3_explorationforce", condition='sqbpremounlocked ==  True') \

       ml.find_label("_call_skiptut_eckn32") \
            .search_menu("Yes. I want to skip ahead.").branch() \
            .hook_to("sqb_naomi_m3_templabskip", condition='sqbpremounlocked ==  True') \
       
       ml.find_label("eck_naomi_m3_early_leave") \
            .search_scene("beach") \
            .hook_to("sqb_naomi_m3_labteleport", condition='sqbpremounlocked ==  True') \
       
       ml.find_label("eck_naomi_m3_biolabalert") \
            .search_say("Be advised, prolonged") \
            .hook_to("sqb_naomi_m3_biolabalert", condition='sqbpremounlocked ==  True') \

       ml.find_label("eck_naomi_m3_panicmenu") \
            .search_menu("Get some rest.").branch() \
            .search_say("Sure thing") \
            .hook_to("sqb_naomi_m3_labrest", condition='sqbpremounlocked == True') \
            
       #ml.find_label("eck_naomi_m3_panicmenu") \
            #.search_menu("Snuggle up with Naomi and surrender to your fate.").branch() \
            #.search_python("renpy.pause (0.5)") \
            #.hook_to("sqb_naomi_m3_nogiveup", condition='sqbpremounlocked == True') \
            
       ml.find_label("eck_naomi_m3_panicmenu") \
            .search_menu("Snuggle up with Naomi and surrender to your fate.") \
            .edit_choice(text="Snuggle up with Naomi and surrender to your fate.", condition='sqbnaomim3nogiveup == False and sqbpremounlocked == True and ecknaomim3boomstop == False' ).branch() \
            .search_python("renpy.pause (0.5)") \
            .hook_to("sqb_naomi_m3_nogiveup") \
            
       ml.find_label("eck_naomi_m3_panicmenu") \
            .search_menu("Check on the entrance.").branch() \
            .hook_to("sqb_naomi_m3_panicdoor", condition='sqbpremounlocked ==  True and ecknaomim3boomstop == False') \
       
       ml.find_label("eck_naomi_m3_panicterminalman") \
            .search_menu("Maintenance.").branch() \
            .search_say("There were several more pages") \
            .hook_to("sqb_naomi_m3_panicterminal", condition='sqbpremounlocked == True') \
       
       ml.find_label("eck_naomi_m3_escape") \
            .search_say("I'd say we swim") \
            .hook_to("sqb_naomi_m3_ending", condition='sqbpremounlocked ==  True') \

def sqb4naomi(ml):

    ml.find_label("eck_naomi_m4") \
    .search_say("Oh well. I don't need") \
    .hook_to("sqb_naomi_m4_clothes", condition='sqbpremounlocked ==  True') \
    .search_say("She swam a few quick laps") \
    .link_from("sqb_naomi_m4_clothes_end") 

#def sqb6naomi(ml):      

        #ml.find_label("") \
        #.search_say("") \
        #.search_say("") \
        #.hook_to("sqb_naomi_m6_discussion_reality", condition='sqbpremounlocked == True') \
        #.search_say("") \
        #.link_from("sqb_naomi_m6_discussion_reality_end")      