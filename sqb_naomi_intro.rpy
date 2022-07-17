label sqb_naomi_endingcheck:

    c "As I was focusing too much on what was happening outside..."
    
    menu:
        "I was suddenly interrupted.":
             $ renpy.pause (0.5)
             play sound "fx/impact3.ogg"
             m "My observations, however, were suddenly interrupted."
             jump sqb_naomi_endingcheck_end
        
        "I had the strangest feeling.":
             $ renpy.pause (0.5)
             m "I felt a strange and also a somewhat unsettling feeling in the back of my head."
             play sound "fx/impact3.ogg"
             $ sqbpremounlocked = True
    
jump sqb_naomi_endingcheck_end

label sqb_naomi_premostart:

    m "When I looked again at the dragon, the first thing that popped into my mind was how big she looked from my perspective on the floor."
    c "You're big!"
    show naomi confused b with dissolve
    "???" "Thanks?"
    m "I had no idea what had just happened. I was only able to stare at the dragoness looming over me."
    c "..."
    show naomi concern b with dissolve
    m "She stared back at me worriedly while still holding her hand out to me."
    m "My head felt weird, as if my brain was trying very hard to remember something."
    c "A large blue dragoness?"
    show naomi confused b with dissolve
    "???" "Are you okay?"
    m "She leaned towards me and extended her hand closer."
    $ renpy.pause (1.0)
    m "After taking another glance, I grabbed her hand, and she effortlessly pulled me back onto my feet."
    show naomi stern b with dissolve
    "???" "By the way I have a name, you small and squishy human."
    m "I blurted out the next words instinctively, without thinking."
    c "You're Naomi from the police station, right?"
    Nm smile b "That's me!"
    Nm concern b "Wait...{w} how do you know my name? What's going on?"
    m "She was right. I was also dumbfounded because we had never met before." 
    m "(Maybe Sebastian mentioned her on the way here and I forgot about it?)"
    Nm sad b "I'm so sorry for bumping into you. I hope you're not hurt."
    Nm concern b "It took you a while to get up, so you should get yourself checked, just in case. Thankfully, you won't have to go far."
    c "I'm fine."
    Nm "But what if you have a concussion? You might feel fine now, but you never really know with them. I would be in big trouble if I ended up causing you harm."
    c "Don't worry about it. I should have paid more attention to where I was going."
    show naomi normal b with dissolve
    c "Since I already know your name, it would be fair to let you know mine. I'm [player_name]."
    Nm smile b "Nice to meet you, [player_name]."
    
jump sqb_naomi_premostart_end