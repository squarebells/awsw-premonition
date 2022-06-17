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

       ml.find_label("sqb_naomi_m2_sexandeating") \
           .search_say("I hope you understand that") \
           .search_say("I picked up my clothes") \
           .search_say("Her remark made me feel") \
           .search_say("So, could you fully") \
           .search_say("Finish if you have to") \
           .search_say("It was certainly fun to") \
           .search_say("Oh, you're hungry") \
           .hook_to("sqb_naomi_m2_foodskip", condition='sqbpremounlocked == True') \
           .search_say("We could order some food") \
           .link_from("sqb_naomi_m2_foodskip_end")

       ml.find_label("sqb_naomi_m2_ending") \
           .search_say("You make a good point") \
           .hook_to("sqb_naomi_m6_discussion_reality", condition='sqbpremounlocked == True') \
           .search_say("Likewise") \
           .link_from("sqb_naomi_m6_discussion_reality_end")

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
           .hook_to("sqb_naomi_m2_sexandeating", condition='sqbpremounlocked == True and naomi2mood > 8 and naomilewd > 4') \
           .search_say("I guess we should get going.") \
           .link_from("sqb_naomi_m2_sexandeating_end")