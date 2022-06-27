label sqb_naomi_m3_norefusal:

    Nm "Please? I know diving might seem scary at first, but I promise I will protect you with my life if necessary!"
    Nm "Just...{w} don't leave alone for this evening. We had a lot of fun last time and I guarantee we will now as well."
    m "I started feel bad for turning her down so abruptly. I had to accept, even though I hated being around water."
    c "Fine, I'll go with you."
    Nm smile "Thank you."
    m "She leaned in and suddenly yet gently rubbed the side of her head against mine."
    Nm "With me nearby, you have nothing to worry about."
    
jump eck_naomi_m3_start

label sqb_naomi_m3_tail:

    Nm blank "No, that won't do. We are going to need scuba gear and flippers then, since you don't have any frills, membranes or even a tail hidden underneath your clothes."
    c "Very attentive of you."
    Nm smile "Actually that's for the better, if you recall what we discussed about our differences earlier. This way I get to be the one to take care of you again."
    c "Yes, I'll definitely need some gear even with you at my side. Do you know where we can get some?" 

jump sqb_naomi_m3_tail_end

label sqb_naomi_m3_undressing:

    Nm shy "What's the big deal? I've already seen you without your clothes and you undressed in front me at my apartment."
    c "Yes, but it would feel kind of weird if you stared at me while I put the scuba gear on. Also, we're outside and not about to have sex."
    Nm surprisedblush "Hold on." 
    Nm "I thought that back at my apartment you were the one who seduced me."
    Nm smile "When I asked you to take your clothes off in front of me, did you take that as a sign of me wanting to have sex with you?"
    c "Well...{w} yes."
    c "You wanted that too, right?"
    Nm "Of course. Although if you had refused to take your clothes off, that would have been pretty awkward, right?"
    c "Agreed. It all worked out in the end, so I'm not complaining."
    c "Could you please let me put the scuba gear on now?"
    Nm blank "Sure." 
    hide naomi with dissolve
    m "Naomi laid down on the sand and hid her head under her wing so she wouldn't be able to see me." 
    Nm normal "Is this good enough for you? I promise I won't look."
    c "Yes, that's fine."
    hide naomi with dissolve
    m "Seeing as I could now change in peace since Naomi wasn't looking, I turned to the opposite direction, towards the forest."
    $ renpy.pause (1.0)
    play sound "fx/undress.ogg"
    $ renpy.pause (1.0)
    m "Done undressing, I hid my clothes in a nearby thick shrub and switched my attention towards the scuba gear, when I noticed Naomi peeking at me from under her wing."
    c "Naomi!"
    show naomi smile with dissolve
    Nm "Sorry. I couldn't help but find out how you would react." 
    Nm normal "I honestly don't understand what's so different about undressing outside."
    m "(This is starting to be really irritating, and and I want to get going already.)"
    c "It's whatever. You can watch if you want."
    m "I grabbed the wet pants and started putting them on."   
    c "I hope you will at least enjoy the show."
    Nm smile "Of course I will. Teasing you is so much fun."
    $ renpy.pause (2.0)
    Nm normal "What's the whole idea behind clothes in the human society, anyway? You always have a lot of things on, only leaving a small part of the body in the open."
    c "We don't have anything to protect our skin or keep us warm, so clothes were the solution in the prehistoric times."
    c "Eventually, after many centuries of civilization development, covering oneself up became more than simple necessity, but rather a norm or a tradition to follow as well. Especially when it came to hiding certain – more private – parts of our bodies."
    Nm smile "I see. Is that why you were so flustered back at my apartment when I stared at you after you took your clothes off? Were you afraid that I would see your private parts?"
    c "..."
    c "Are you sure you've never met a human before? You know just the correct ways to make me feel as embarrassed as possible to be a human."
    Nm shy "N-no... it's just intuition, I guess?"
    Nm normal "Anyway to contrast us with humans, I'll tell you that we don't have a problem walking around as we are, really. Of course, we have specialized outfits for jobs which require them – but for the most part, it comes down to accessories with extra functionality, like bags, insignias and other minor elements, mostly decorative."
    c "I see. Makes sense why you'd want to wear a police badge or some protective gear required for your job even if you normally didn't need any clothing. Like I already implied, in human society being naked in front of someone is actually a sign of affection or even a request for intimacy."     
    Nm blank "Wait a moment..."
    Nm shy "Hold on."
    Nm surprisedblush "Ever since we met, I've only been wearing my police badge and sometimes the belt pouches for stuff."
    Nm smile "So, because I haven't worn any clothing, have I been unintentionally making you horny all the time by signaling that I want to have sex with you, [player_name]?"
    c "Well... uhh...{w} maybe a little?"
    Nm "So, you've been taking advantage of our society's traditions the entire time you've been here?"
    c "Well, I guess that kind of just happened. In my defense, your genitalia is a lot more hidden than ours."
    Nm normal "Yeah, I saw that."
    m "I had almost finished putting the scuba gear on."
    Nm smile "Anyway, this has been a pretty interesting talk. I'm happy to know that I arouse you simply by the virtue of being around you. Care to tell me which exposed part of me excites you the most?"
    c "Naomi... please. Can we just go diving?"
    Nm blank "Fine, but this conversation isn't over. I'm going to find all of your buttons and press them as I please. Rest assured, it's only going to get worse from here on out."
    m "(Did I make a mistake by choosing to stay with Naomi? Oh well, it's probably too late to regret that decision.)"
    m "(Just kidding, I love her precisely for this reason.)"
    show naomi surprised with dissolve
    m "For the rest of the time of me putting on the gear, Naomi stared at me with intent, but at least she was quiet, save for a few giggles. After a couple of long minutes, I finally managed to put the gear on."

jump sqb_naomi_m3_undressing_end

label sqb_naomi_m3_explorationforce:

     c "Let's see what inside that facility, then."
     $ renpy.pause (0.5)
     Nm smile "I'm with you."
     m "I put my rebreather back on and went to the cave entrance at the seafloor."
     play sound "fx/watersurface.ogg"
     hide naomi with easeoutbottom
     play sound "fx/watersurface.ogg"
     stop music fadeout 2.0
     $ renpy.pause (2.5)
     play music "mx/underwaterprison.mp3" fadein 2.0
     scene eckunderwatertransition01 with dissolvemed
     $ renpy.pause (2.0)
     scene eckunderwater02 with dissolvemed
     $ renpy.pause (2.0)
     scene eckunderwatertunnel with dissolvemed
     $ renpy.pause (2.0)
     show naomi normal flip at Position (xpos = 0.10) with dissolve            
     show screen eckextrainfo
     $ eckextradisplay = 2            
     $ eckdisplayvar1name = "Naomi's breath:"
     $ eckdisplayvar2name = "Air tank supply:"
     $ eckdisplayvar1unit = "min"
     $ eckdisplayvar2unit = "min"
            
jump eck_naomi_m3_D1

label sqb_naomi_m3_labteleport:
    
    stop music fadeout 2.0
    $ ecknaomim3earlyleave = False
    scene black with dissolvemed
    play sound "fx/system3.wav"
    s "Looks like you decided to go back or ran out of air. Since I haven't written an extended worst ending yet, I'm teleporting you to the lab."
    $ renpy.pause (2.0)
    play music "mx/abandonedlab.mp3"
    scene eckoldbiolab with dissolveslow
    $ renpy.pause (2.0)

jump eck_naomi_m3_biolab
     
label sqb_naomi_m3_templabskip:

    play sound "fx/system3.wav"
    s "Alright."
    play sound "fx/system3.wav"
    s "In this mod's timeline, for now, you are forced to take the old generator. I'm going to write an extended worst ending in the future."    
    
    scene black with dissolvemed
    $ renpy.pause (1.0)
    $ persistent.skipnumber += 1
    $ naomi3mood += 8
    $ naomiromance += 1
    $ ecknaomim3scubaon = True
    $ ecknaomim3boomstop = True
    $ naomigoodending = True
    play music "mx/neptune.mp3" fadein 2.0               
    scene beach at Pan ((0, 0), (300, 0), 5.0) with dissolveslow               
    $ renpy.pause (0.5)

jump sqb_naomi_m3_ending

label sqb_naomi_m3_biolabalert:

    Nm stern "We have to get out of here! Quick!"
    c "Agreed."
    hide naomi with dissolve
    m "We rushed back to the entrance. I started putting on my scuba gear while Naomi pushed the button to get the airlock doors open. But they didn't move."
    show naomi annoyed with dissolve
    Nm "This cursed thing won't work!"
    c "No card readers either. Hit it harder."
    play sound2 "fx/beep.wav"
    s "Error. Hostile environment detected in the transit chamber. Cause: outer door malfunction. Pumps: online. Please wait."
    c "Damn! No way out."
    Nm stern "Quick, think of something. You're much better with mechanical things than I am."
    c "I have to admit that I'm at a loss."
    Nm "What if we prevent the generator from exploding by shutting it down?"
    c "Do you think that might work?"
    Nm normal "We have to try. We don't know where the generator is though, so use that console and try to shut it down remotely."
    c "Alright, I'll try that."
    $ renpy.pause (2.0)
    $ naomi3moodtmp = naomi3mood

label sqb_naomi_m3_panicmenureset:

    $ ecknaomim3boom = 300
    $ naomi3mood = naomi3moodtmp
    $ naomidead = False
    $ ecknaomim3srcheck = 0
    $ ecknaomim3doorbutt = 0
    $ ecknaomim3termavail = True
    $ ecknaomim3genhatch = False
    $ ecknaomim3genhatchfound = False
    $ ecknaomim3genhatchopen = False
    $ sqbnaomim3genhatchtold = False
    $ ecknaomim3naomifound = True
    $ ecknaomim3naomifound2 = False
    $ ecknaomim3naomijoin = True
    $ ecknaomim3dooropen = False
    $ ecknaomim3doorbutheld = False
    $ ecknaomim3scubaon = False
    $ ecknaomim3scubaonmlt = 1
    $ ecknaomim3boomstop = False
    $ ecknaomim3afboomrest = True
    $ ecknaomim3genhatchav = True
    $ ecknaomim3timeoutfail = False
    $ ecknaomim3currentloc = "power unit"
    $ ecknaomim3currentlocexplr = 0
    $ ecknaomim3hatchloc = renpy.random.choice(['testing', 'computer', 'storage', 'workshop', 'corridors'])
    $ ecknaomim3dragonessloc = "power unit"
    
    $ ecknaomim3testexplr = 0
    $ ecknaomim3compexplr = 0
    $ ecknaomim3storexplr = 0
    $ ecknaomim3workexplr = 0
    $ ecknaomim3powrexplr = 0
    $ ecknaomim3correxplr = 0
    
    m "I looked again at the diagnostics console and first decided to bring up the schematics to assess the situation. Finding the area where we were at wasn't hard, but what I saw filled my mind with dread and despair."
    m "The airlock pumps were functioning reasonably well for their age, but same couldn't be said about the drainage system. In fact, it was gone completely, so seawater was dumped straight into the nearest unoccupied area, which in turn was connected with the generator room below."
    m "The program estimated that I had about half an hour before generator rupture. I set the timer up on my PDA as well."
    c "Naomi..."
    Nm surprised "Did you shut down the generator yet?"
    c "No, but this console just told me that we have only half an hour before the generator explodes."
    Nm stern "Well, hurry up then. I can't operate computers as well as you can."
    show naomi blank with dissolve
    m "As I looked around, I noticed another console nearby. I decided to try my luck with it."
    $ renpy.pause (2.0)
    
    show screen eckextrainfo
    $ eckextradisplay = 11
    $ eckdisplayvar1name = "Approximate remaining time:"
    $ eckdisplayvar2name = "Location:"
    $ eckdisplayvar3name = "Of which explored:"
    $ eckdisplayvar3unit = "%"
    $ eckdisplayvar4name = "Naomi's location:"

jump eck_naomi_m3_panicterminal

label sqb_naomi_m3_panicterminal:

    c "Naomi, I found out how to shut down the generator. There's a maintenance hatch somewhere around here, and I need your help to find it."
    
    if sqbnaomim3genhatchtold == True:
        Nm stern "I know, you already told me that. Can we please start looking for it?"
        show naomi blank with dissolve
    else:
        $ sqbnaomim3genhatchtold = True
        Nm "Alright."       

jump eck_naomi_m3_panicterminalman

label sqb_naomi_m3_panicdoor:

    m "(We can't leave, because we haven't disabled the generator yet.)"

jump eck_naomi_m3_panicmenu

label sqb_naomi_m3_labrest:

    hide naomi with dissolve
    m "She sat down in a relatively clean corner of the room and beckoned me to come over. I eagerly made my way to her."
    $ naomiromance += 1
    $ naomi3mood += 3
    m "I sat down nearby and leaned onto her side."
    play sound "fx/undress.ogg"
    m "Her large wing slowly unfolded and relaxed, covering me akin to a large warm cloak. I felt her warm up and heard her let out a content sigh. When I looked up at her, she flicked my face with her long tongue."
    m "I twitched a little bit, but decided not to comment."
    $ renpy.pause (2.0)
    show naomi shy with dissolve
    Nm "Hey, [player_name]...{w} I'm feeling hot."
    Nm smile "Up for some fun while we're both still excited?"
    c "Naomi...{w} just no. We almost died a few minutes ago."
    show naomi blank with dissolve     
    c "Also, we have no idea what might happen if we stay here any longer than absolutely necessary. What if we end up disturbing something while we have sex and this entire place collapses on us?"
    Nm normal "What's the big deal? You said it yourself, this place has probably been here a thousand years. I think it'll survive a bit longer."
    c "Absolutely not. We also need to conserve as much energy as possible because the swim back to the beach is rather long."
    Nm blank "Fine, have it your way. There's no need to be so fussy about it."
    Nm smile "But let's just say that you owe me one."
    c "Fine, whatever."    
    hide naomi with dissolve
    $ renpy.pause (1.5)
    play sound "fx/bed.ogg"
    m "For the rest of the time, we just stayed close together. Occasionally, Naomi patted my head or rubbed my neck, while letting out satisfied hums."
    $ ecknaomim3afboomrest = False
    m "Eventually Naomi felt that I had calmed down enough."
    show naomi normal with dissolve
    c "I think we should get going."
    Nm "Yeah, I suppose you are right. We should conserve our energy to make our way back to the shore in a timely manner, before it gets too late."
    $ ecknaomim3afboomrest = False
    play sound "fx/undress.ogg"

jump eck_naomi_m3_panicmenu 

label sqb_naomi_m3_ending:

    #Had to copy more of ECK's script than necessary because otherwise dissolveslow wouldn't work properly

    c "Mind hauling me? I don't think I can make it otherwise."
    if naomi3mood > 6:
        Nm smile "Of course. Climb onto my back."
        c "That sounds quite personal."
        Nm "It's fine, [player_name]. You need rest."
        
    elif naomi3mood > 0:
        Nm smile "Sure thing. You know what to do – grab my tail and hang on."
        c "Got it."
        
    else:
        Nm "I guess. Grab my tail."
        c "Alright."
        
    $ renpy.pause (2.0)
    scene beach at Pan ((0, 0), (300, 0), 5.0) with dissolveslow
    play sound "fx/wading.ogg"
    $ renpy.pause (0.5)
    play sound2 "fx/wading.ogg"
    m "Soon, we were back on the beach. The very same spot we left hours earlier."
    m "We slowly walked up to the line of bushes separating sand from thick vegetation. I found my daily clothes still neatly piled in the shade, but had almost no strength left, so I didn't really feel like changing back to them."
    
    if ecknaomim3scubaon:
        m "I quickly took off the air tanks, mask, and flippers, anxious to get them off as fast as possible."
            
    else:
        pass
        
    m "We both sat down on the sand very exhausted, happy to finally feel dry land. I was going to take a nap on the beach, but Naomi interrupted my intentions."
    show naomi smile with dissolve
    Nm "You look tired. Do you want to come sleep at my place? It's closer than yours."
    Nm smile "Don't worry, I'll carry you on my back."
    c "I would love that. I can't believe you still have any energy left after our adventure."
    Nm blank "Well, I have to admit that I'm in no state to fly you back. Still, keep in mind that you can barely even walk."
    c "Hey, no need to gloat your physical prowess so much. Can we just get going already?"
    Nm normal "Fine. Hop on my back when you're ready to go."
    hide naomi with dissolve
    play sound "fx/sheet.wav"
    m "As Naomi got down to rest on her belly to prepare to take me on as a passenger, I went to put both the scuba gear and my clothes in the same bag I had brought the scuba gear in."
    m "Then, without saying anything I walked over to Naomi and positioned myself on her back, fastening my three available limbs on her sides to be able to hold onto her, while carrying the equipment and clothing bag in one hand."
    scene black with dissolvemed
    play soundloop "fx/steps/steps.ogg"
    m "When I was secure enough, she got off from the ground and started carrying me to her apartment slowly but steadily."
    Nm blank "I realize that now when I am carrying you, that you're much fatter than you look at first glance."
    c "Naomi...{w} please not now. I'm going to die from any more exertion."
    Nm normal "Fine. I can't help but tease you."
    m "She was quiet for the rest of the trip, but I knew I would get an earful when we got to her apartment."
    scene ecknaomiaptoutside with dissolvemed
    $ renpy.pause (2.0)
    stop soundloop fadeout 1.0
    scene black with dissolvemed
    play sound "fx/door/handle.wav"
    $ renpy.pause (2.0)
    play sound "fx/door/doorclose3.wav"
    scene ecknaomiapt01 with dissolvemed
    $ renpy.pause (2.0)
    play sound "fx/door/door_open.wav"
    scene eckannabedroom4 with dissolvemed
    $ renpy.pause (2.0)
    m "When we had gotten to her bedroom, Naomi moved over to the side of her bed and slowly lowered me on it on my back. I had finally made it back to absolute safety."
    show naomi blank with dissolve
    Nm "What an evening."
    Nm concern "Are you okay, [player_name]?"
    c "No."
    
    #PC wakes up, his limbs hurt
    
    stop music fadeout 1.0

jump ml_date_end  
