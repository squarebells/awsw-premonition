#This was initially only going to be a lewd mod for Naomi, but then I realized I need to find a justification for why she would want to have sex with the player on date 2.
#I came up with the idea of this being an alternate timeline after ASM's ending A. 
#Because of how the the multiverse operates here, the PC and eventually Naomi feel like they have already met before, leading to different dialogue.
#Thanks to this I can show some of my other ideas I had while playing the game. I felt like there were some things you could have talked about more.
#TI project a few of my ideas into the PC's lines in chapter 6.
#The PC most likely talks about things you can only be guaranteed to know if you've completed the base game's true ending, so maybe add a check for that.
#Actually it would probably take a lot of effort to check for that, so better be safe than spoil the game.
#As always, everyone should thank ECK for his great mods and character.
  
label sqb_naomi_endingcheck:

    m "While I was focusing too much on what was happening outside..."
    
    menu:
        "I was suddenly interrupted.":
             $ renpy.pause (0.5)
             play sound "fx/impact3.ogg"
             m "My observations, however, were suddenly interrupted."
             jump sqb_naomi_endingcheck_end
        
        "I had the strangest feeling.":
             $ renpy.pause (0.5)
             # It's kind of redundant to also put the original line here. It goes without saying that the PC gets suddenly interrupted at the same he has this feeling.
             m "I felt a strange and somewhat unsettling feeling in the back of my head."
             play sound "fx/impact3.ogg"
             $ sqbpremounlocked = True
    
jump sqb_naomi_endingcheck_end

label sqb_naomi_premostart:

    $ naomilewd +=1

    m "When I looked back at her, the first thing that popped into my mind was how gigantic she looked from my perspective on the floor."
    c "Y-you're big!"
    show naomi confused b with dissolve
    "???" "Thanks?"
    m "I was very confused. I had no idea what had just happened. I could only stare back at the dragon looming over me."
    c "..."
    c "..."
    show naomi concern b with dissolve
    m "The large blue dragon started staring back at me with a worried look while still holding her hand out to me."
    m "My head felt weird, as if my brain was trying very hard to remember something."
    c "A large blue dragon?"
    show naomi confused b with dissolve
    "???" "Huh? Are you okay?"
    m "She extended her hand closer to me."
    m "After looking at her once more, I grabbed her hand, and she effortlessly pulled me back onto my feet."
    show naomi stern b with dissolve
    "???" "By the way, I have a name, you small pink human."
    m "I blurted out the next words instinctively, without thinking."
    c "You're Naomi from the police station, right?"
    Nm smile b "That's me!"
    Nm concern b "Wait... how do you know my name?" 
    Nm "What's going on?"
    m "She was right. I was dumbfounded because we had never met before." 
    m "(Maybe Sebastian mentioned her on the way here?)"
    c "..."
    Nm sad b "Again, I'm so sorry. I hope you're not hurt."
    Nm shy b "It took you a while to get up, so you should get yourself checked. You might have a concussion."
    c "I'm fine."
    Nm concern b "You might feel fine now, but you never know with concussions. I would be in big trouble if I ended up hospitalizing you."
    c "Don't worry about it. I should have paid more attention to where I was going."
    c "Since I already know your name, it would be fair to let you know mine. I'm [player_name]."
    Nm smile b "Nice to meet you, [player_name]."
    
jump sqb_naomi_premostart_end