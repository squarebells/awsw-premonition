label sqb_naomi_endingcheck:

    m "While I was focusing too much on what was happening outside..."   
    menu:
        "I was suddenly interrupted.":
             $ renpy.pause (0.5)
             m "...my observations were suddenly interrupted."
             $ renpy.pause (0.5)
             jump sqb_naomi_endingcheck_end
        
        "I had the strangest feeling.":
             $ renpy.pause (0.5)
             m "...I felt a strange and also a somewhat unsettling feeling in the back of my head."
             $ sqbpremounlocked = True
             $ renpy.pause (0.5)
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
    $ renpy.pause (1.0)
    m "My head felt weird, as if my brain was trying very hard to remember something."
    c "A large blue dragon?"
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
    m "I was also dumbfounded by what I had just said because we had never met before." 
    m "(Maybe Sebastian mentioned her on the way here and I just forgot about it?)"
    Nm sad b "I'm so sorry for bumping onto you. I hope you're not hurt."
    Nm concern b "It took you a while to get up, so you should get yourself checked, just in case. Thankfully, due to where we're at, you won't have to go far to find a doctor."
    c "I'm fine."
    Nm "But what if you have a concussion? You might feel fine now, but you never really know with them. I would be in big trouble if I ended up hurting you badly."
    c "Don't worry about it. I should have paid more attention to where I was going."
    show naomi normal b with dissolve
    $ renpy.pause (1.0)
    c "Since I somehow already know your name, it would be fair to let you know mine. I'm [player_name]."
    Nm smile b "Nice to meet you, [player_name]."
    
jump sqb_naomi_premostart_end