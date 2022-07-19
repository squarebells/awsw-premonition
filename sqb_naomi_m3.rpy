label sqb_naomi_m3_norefusal:

    $ sqbnaomim3protect = True
    Nm "Please? I know diving might seem scary at first, but I promise I will protect you with my life if necessary!"
    Nm "Just don't leave me alone. We had a lot of fun last time and I promise you we will this evening as well."
    m "I started feel bad for turning her down so abruptly. I felt like I had to accept, even though I hated being in water."
    c "Fine, I'll go with you."
    Nm smile "Thank you."
    m "She leaned in and suddenly yet gently rubbed the side of her head against mine."
    Nm "With me nearby, you have nothing to worry about."
    
jump eck_naomi_m3_start

label sqb_naomi_m3_tail:

    Nm blank "No, that won't do at all. We are going to need scuba gear and flippers, since you don't have any frills, membranes or even a tail hidden underneath your clothes."
    c "Very attentive of you."
    Nm smile "It's not all bad, since I get to take care of you again."
    c "Sure. Have you looked up a store where we can get some gear?"
    Nm normal "Yeah, I know a good one that can get you geared up. I could probably even help you choose some proper swimming clothes."    

jump sqb_naomi_m3_tail_end

label sqb_naomi_m3_undressing:

    Nm shy "What's the big deal? I have already seen you without your clothes and you even took them off in front me at my apartment."
    c "To me, it would feel kind of weird if you stared at me while I put the gear on, since we're outside and not about to have sex."
    Nm surprisedblush "Wait a second. I thought that back at my apartment you were the one who seduced me."
    Nm smile "When I asked you to take your clothes off in front of me, did you take that as a sign of me wanting to have sex with you?"
    c "Well...{w} yes."
    c "You wanted that too, right?"
    Nm "Of course. Although if you had refused to take your clothes off, that would've been pretty awkward, right?"
    c "Agreed. It all worked out in the end, so I'm not complaining."
    c "Could you please let me put the scuba gear on in privacy now?"
    Nm blank "Sure." 
    hide naomi with dissolve
    m "Naomi laid down on the sand on her belly and covered her head with her wing so she wouldn't be able to see me." 
    Nm normal "Is this good enough for you? I promise I won't look."
    c "Yes, that's fine."
    hide naomi with dissolve
    m "Seeing as I could now change in peace since Naomi wasn't looking, I turned to the opposite direction, towards the forest."
    $ renpy.pause (2.0)
    play sound "fx/undress.ogg"
    $ renpy.pause (2.0)
    m "Done undressing, I hid my clothes in a nearby thick shrub and switched my attention towards the scuba gear. Then I noticed Naomi peeking at me from behind her wing."
    c "Naomi!"
    show naomi smile with dissolve
    Nm "Sorry. I couldn't help but want to find out how you would react." 
    Nm normal "I honestly don't understand what's so different about undressing outside."
    m "(This is starting to be really irritating, and I want to get going already.)"
    c "It's whatever. You can watch if you want."
    play sound "fx/undress.ogg"
    m "I grabbed the wet pants and started putting them on."   
    c "I hope you will at least enjoy the show."
    Nm smile "Of course I will. Teasing you is so much fun."
    $ renpy.pause (2.0)
    Nm normal "What's the whole idea behind clothes in the human society, anyway? You always have a lot of things on, only leaving a small part of the body in the open."
    c "Well, we don't have anything to protect our skin or keep us warm, so clothes were the solution in the prehistoric times."
    c "Eventually, after many centuries of different civilizations developing, covering oneself up became more than simple necessity, a social norm or even a tradition to follow as well. This became especially true in regards to hiding certain – more private – parts of our bodies."
    Nm smile "I see. Is that why you became visibly flustered when I stared at you after you had taken your clothes off? Were you afraid that I would look at your private parts?"
    c "..."
    c "Are you sure you have never met a human before? You know just the correct ways to make me feel as embarrassed as possible to be one."
    Nm shy "N-no...{w} it's just intuition, I guess?"
    Nm normal "Anyway to contrast your people with ours, I'll tell you openly that we don't have a problem walking around as we are, really." 
    Nm "Of course, we have specialized outfits for jobs which require them – but for the most part, it comes down to accessories with extra functionality, like bags, insignias and other minor elements, that are mostly decorative."
    c "Makes sense why you would want to wear a police badge or some protective gear required for your job even if you normally didn't need any clothing." 
    c "In my case it's still going to take some time to get fully used to, because like I already implied, in human society being naked in front of someone is actually a sign of affection or even a request for intimacy."     
    Nm blank "Wait a moment..."
    Nm shy "Hold on."
    Nm surprisedblush "Ever since we met, I've only been wearing my police badge and sometimes the belt pouches for stuff."
    Nm smile "So, because I haven't worn any clothing, have I been unintentionally making you horny all the time by signaling that I want to have sex with you, [player_name]?"
    c "Well... uhh...{w} maybe a little?"
    Nm "So, you've been taking advantage of our society's traditions the entire time you've been here?"
    c "Well, I guess that kind of just happened. In my defense, your private parts are a lot more hidden than ours."
    Nm normal "Yeah, I saw that."
    m "I had almost finished putting the scuba gear on."
    Nm smile "Anyway, this has been a pretty interesting talk. I'm happy to know that I arouse you simply by just being around you. Care to tell which exposed part of me excites you the most when I am going about my day, unaware of you admiring me?"
    c "Naomi...{w} please no more. Can we just go diving already? At least underwater you won't be able to talk to me."
    Nm blank "Fine, but this conversation isn't over. I'm going to find all of your buttons and press them as I please. Rest assured, it's only going to get worse from here on out."
    m "(Did I make a mistake by choosing to stay here with Naomi? Oh well, I recall what she said she would do if I try to leave, so it's too late to regret that decision anyway.)"
    $ renpy.pause (2.0)
    m "(Just kidding, I love her because she teases me like this.)"
    show naomi surprisedblush with dissolve
    m "For the rest of the time of me putting on the gear, Naomi stared at me with intent, but at least she was quiet, save for a few giggles and flicks of her tongue. After a couple of long minutes of being under her gaze, I finally managed to finish putting the gear on."

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
     play sound "fx/system3.wav"
     s "Hint: for now, skip this exploration part only by trying to leave."
            
jump eck_naomi_m3_D1

label sqb_naomi_m3_labteleport:
    
    stop music fadeout 2.0
    $ ecknaomim3earlyleave = False
    scene black with dissolvemed
    play sound "fx/system3.wav"
    s "Looks like you decided to go back or ran out of air." 
    s "Or did you want to skip intentionally? The way I scripted this means I have no way of knowing that. Anyway, since I haven't written an extended worst ending yet, I'm teleporting you straight to the abandoned lab."
    $ renpy.pause (2.0)
    play music "mx/abandonedlab.mp3"
    scene eckoldbiolab with dissolveslow
    $ renpy.pause (2.0)

jump eck_naomi_m3_biolab
     
label sqb_naomi_m3_templabskip:

    play sound "fx/system3.wav"
    s "Alright."
    play sound "fx/system3.wav"
    s "There used to be a choice here for taking the generator or not, but in this mod's alternate timeline, for now, you are forced to take the it. I'm going to write an extended worst ending in the future."        
    scene black with dissolvemed
    $ renpy.pause (1.0)
    $ persistent.skipnumber += 1
    $ naomi3mood += 8
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
    c "No card readers either. Hit it harder!"
    play sound2 "fx/beep.wav"
    s "Error. Hostile environment detected in the transit chamber. Cause: outer door malfunction. Pumps: online. Please wait."
    c "Damn! No way out."
    Nm stern "Quick, think of something. You're much more knowledgeable about mechanical things and computers than I am."
    $ renpy.pause (1.0)
    c "I have to admit that I'm at a loss."
    $ renpy.pause (2.0)
    Nm blank "What if we prevent the backup generator from exploding by shutting it down, and then placing it somewhere safer?"
    c "Do you think that we might be able to do that?"
    Nm normal "Well, in a facility like this there has to be a way to maintain and replace the power source." 
    Nm "We don't know where the generator room is though, so finding out where it is should be our first priority. Could we try to look at the schematics of this complex on the console we saw earlier?"
    c "Alright, let's try that."
    hide naomi with dissolve
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
    $ sqbnaomim3nogiveup = False #Just in case here as well
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
    
    m "We made our way back to the diagnostics console and I brought up the schematics to assess the situation. Finding the area where we were at wasn't hard, but what I saw filled my mind with dread and despair."
    m "The airlock pumps were functioning reasonably well for their age, but same couldn't be said about the drainage system. In fact, it was gone completely, so seawater was dumped straight into the nearest unoccupied area, which in turn was connected with the generator room below."
    m "The program estimated that I had about half an hour before generator rupture. I set the timer up on my PDA as well."
    c "Naomi..."
    show naomi surprised with dissolve
    Nm "Did you find out where the generator room is?"
    c "Yes, it's below us, but I have no idea how to reach it."
    c "The real bad news is that this console also told me that we have only half an hour before the backup generator explodes. I honestly thought we would've had a lot longer but the drainage system is completely destroyed."
    Nm stern "Well, you better hurry up then, since I can't operate computers as fast as you can. See if you can remotely open a maintenance hatch or even extract the generator automatically."
    show naomi blank with dissolve
    c "Yes, Naomi."
    m "Looking around, I noticed another console nearby. I decided to try my luck with it."
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

    c "Naomi, I found out how to get to the backup generator. There's a maintenance hatch somewhere around here, and I need your help to find it."
    
    if sqbnaomim3genhatchtold == True:
        Nm stern "I know, you already told me that. Can we please start looking for it?"
        show naomi blank with dissolve
    else:
        $ sqbnaomim3genhatchtold = True
        Nm normal "Alright."       

jump eck_naomi_m3_panicterminalman

label sqb_naomi_m3_panicdoor:
    
    $ renpy.pause (0.5)
    m "(We can't leave, because we haven't disabled the generator yet. It might explode on our way out, and then we're dead for sure. I better calm myself down and focus as best as I can.)"

jump eck_naomi_m3_panicmenu

label sqb_naomi_m3_nogiveup:
        
    $ renpy.pause (0.5)    
    $ sqbnaomim3nogiveup = True
    c "I give up. I have no ideas left, and time is running out."
    Nm stern "What, seriously? We've come this far, so we can't just give up."
    c "A-alright. I will try to figure out something else."
    show naomi blank with dissolve

jump eck_naomi_m3_panicmenu

label sqb_naomi_m3_labrest:
    
    $ naomi3mood += 3
    hide naomi with dissolve
    m "Naomi sat down in a relatively clean corner of the room and beckoned me to come over. I eagerly made my way to her, sat down next to her and leaned onto her side."
    play sound "fx/undress.ogg"
    queue sound "fx/lewd/lickslow.ogg"
    m "Her large wing slowly unfolded and relaxed, covering me akin to a large warm cloak. I felt her warm up and heard her let out a content sigh. When I looked up at her, she flicked my face with her long tongue."
    m "I twitched a little bit, but decided not to comment."
    $ renpy.pause (2.0)
    show naomi shy with dissolve
    Nm "Hey, [player_name]...{w} I'm feeling strangely hot right now."
    Nm smile "Up for some fun while we're both still excited?"
    c "Naomi...{w} just no. Absolutely not. We just almost died."
    show naomi blank with dissolve     
    c "Also, we have no idea what might happen if we stay here any longer than absolutely necessary. What if we end up disturbing something while we have sex and this entire place collapses on us?"
    Nm normal "What's the big deal? You said it yourself, this place has probably been here a thousand years. I think it will survive a bit longer."
    c "Don't forget that the lights might stop working any minute since we removed the backup generator. Also, we need to conserve as much energy as possible because the swim back to the beach is rather long."
    Nm blank "Fine, have it your way. There's no need to be so fussy about it."
    Nm smile "But let's just say that you owe me one."
    c "Fine, whatever."    
    hide naomi with dissolve
    $ renpy.pause (1.5)
    play sound "fx/bed.ogg"
    m "For the rest of the time, we just stayed close together. Occasionally, Naomi patted my head or rubbed my neck, while letting out satisfied hums."
    $ renpy.pause (2.0)
    m "Eventually I felt that we both had calmed down enough."
    show naomi normal with dissolve
    c "I think we should get going."
    Nm "Yeah, I suppose you are right."
    $ ecknaomim3afboomrest = False
    play sound "fx/undress.ogg"

jump eck_naomi_m3_panicmenu 

label sqb_naomi_m3_ending:

    m "We slowly walked up to the line of bushes separating sand from thick vegetation. I found my everyday clothes still neatly piled in the shade, but had almost no strength left, so I didn't feel like changing back into them."
    
    if ecknaomim3scubaon:
        m "I quickly took off the air tanks, mask, and flippers, anxious to get them off as fast as possible."
            
    else:
        pass
        
    m "We both sat down on the sand very exhausted, happy to finally feel dry land. I was going to take a nap on the beach, but Naomi interrupted my intentions."
    show naomi smile with dissolve
    Nm "You look tired. Do you want to come sleep at my place? It's closer than yours."
    Nm smile "Don't worry, I'll carry you on my back."
    c "I would love that, if you don't mind. I can't believe you still have any energy left after our misadventure."
    Nm blank "Well, I have to admit that I'm in no state to fly with you on my back. Still, keep in mind that you can barely even walk."
    c "Hey, no need to gloat with your physical prowess so much. Can we just be quiet and get going? I feel like I'm going to die from exhaustion."
    Nm normal "Fine. Hop on my back when you're ready to go."
    hide naomi with dissolve
    play sound "fx/sheet.wav"
    m "As Naomi got down to rest on her belly to prepare to take me on as a passenger, I went to put both the scuba gear and my clothes in the same bag I had brought the scuba gear in."
    m "Then, I walked over to Naomi and positioned myself on her back, fastening three of my limbs on her sides to be able to hold onto her, while carrying the equipment and clothing bag in one hand."
    scene black with dissolvemed
    play soundloop "fx/steps/steps.ogg"
    m "When I was secure enough, she got off from the ground and started carrying me on her back slowly, but steadily."
    Nm normal "Now when I am carrying you, I realize that you're much fatter than you look or even feel in bed."
    c "Naomi...{w} please not now. I'm going to die from any more exertion."
    Nm smile "Fine. You know I can't help but tease you, because you're so cute?"
    $ renpy.pause (1.0)
    m "She was quiet for the rest of the trip, but I knew she wasn't done with me yet. I would be surprised though, because she would react differently than how I expected her to based on this day's events so far."
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
    m "When we had gotten into Naomi's bedroom, I immediately dropped my plastic bag on the floor and then she carried me over to her bed. She lowered me on it slowly on my back, taking extra care so I was able to lay my head on one of the pillows."
    show naomi blank with dissolve
    Nm "What an evening."
    Nm concern "Are you okay, [player_name]?"
    c "No." 
    c "That was a terrible date. Never again please."
    $ renpy.pause (1.0)
    show naomi sad with dissolve
    $ renpy.pause (2.0)
    Nm "I'm so sorry for ruining what was supposed to be a fun evening for just the two of us."
    c "Naomi, I was just joking. It was my stupid idea to insist on exploring such an unknown and dangerous place."
    Nm concern "But I could've stopped you."
    c "No, it's mostly my fault, not yours."
    c "Remember that you have no authority to order me around. The most you could really do is offer me friendly advice. I take full responsibility for the disastrous decision to go exploring where I shouldn't have."
    c "It was very fortunate for me that you followed me, since I couldn't have gotten to the generator without your help."
    Nm shy "I saved you then, didn't I?"   
    c "Yes, but we worked together. I remember you saying I should be the one to handle the computers and mechanical things."
    Nm blank "You're right as always." 
    Nm smile "Now it's my job to nurse you back to good health."
    hide naomi with dissolve
    stop music fadeout 1.0
    play sound "fx/bed.ogg"
    m "Naomi got on the bed and laid down on top of me so that her head was next to mine. Then she lifted me up a little bit and tied her arms around to hug me. As she lodged my head under her chin, I turned slightly to the right to accommodate myself in this close position."
    $ renpy.pause (2.0)
    show naomi shy with dissolve
    Nm "Are you feeling comfortable? Am I pressing you down with too much force?"
    c "It's fine. Human bodies can take a lot of pressure when lying down, especially when there is support and cushioning."    
    Nm smile "Good to know."
    show naomi normal with dissolve
    $ renpy.pause (2.0)
    show naomi slsmile with dissolve
    m "We laid down in this position for a while. Naomi shifted herself occasionally to rub me and take comfort in me."
    $ renpy.pause (4.0)
    show naomi hurt with dissolve
    m "Then, after some time I felt and heard that Naomi had started crying quietly."
    Nm "Hey, [player_name]..."
    m "I comforted her by scratching the frills behind her horns."
    c "What's wrong, Naomi?"
    play music "mx/lily.mp3"
    show naomi cry with dissolve
    $ renpy.pause (2.0)
    Nm "You're the best thing that has ever happened to me."
    c "I feel the same way. Please always be there for me."
    Nm "I-I don't know what I would have done if you had...{w} had died."    
    c "There's no need to speculate about something like that. You saved my life, and we will both be happy for the rest of our lives that you were there for me when it counted the most."
    
    if sqbnaomim3protect == True:
        Nm crysmile "I promised I would protect you with my life, didn't I?"
        Nm "You did the same thing for me, like I always knew you would."
    else:
        Nm crysmile "I went in with the full intention of protecting you with my life if needed."
        Nm "You would do the same thing for me."
    
    m "I grabbed Naomi's chin to direct it towards mine and I kissed her deeply."
    c "There isn't anything I wouldn't do for you."
    hide naomi with dissolve
    play sound "fx/sheet.wav"
    m "Naomi leaned her head off to my left and wiped her eyes on one of the pillows."
    show naomi smile with dissolve
    Nm "Thank you, [player_name]. You have no idea how much I like being with you." 
    Nm shy "In more ways than just one..."
    $ renpy.pause (2.0)
    Nm aroused "I can't believe my luck. A human that came to our world took a liking to me and and they're also nicer than the nicest human or dragon that I have ever met."
    Nm smile "I suppose that after living a life without a meaningful purpose for such a long time and then being stressed and overworked I deserved to get my fair share of happiness as well."
    c "Hey, I consider myself luckier than you. A few weeks ago I couldn't have even imagined that another sentient species as interesting as dragons were actually real. On top of that, I got to be the second person to come visit them." 
    c "Also, I survived a near-apocalyptical solar flare event and its aftermath even though I realistically shouldn't have."
    Nm concern "I agree about the solar flare, but do remember that the thing regarding dragon-human relations used to be the exact same case for us as well."
    c "Well...{w} yes. Good point. I still consider myself luckier than you."
    Nm smile "Yes, you're lucky to be cute and caring enough to deserve me."
    $ renpy.pause (2.0)
    c "Anyway, I'm very impressed by how you figured out so quickly what to do when the alarms went off. Honestly, I was completely stumped then."
    show naomi shy with dissolve
    c "To me it felt like you knew almost exactly what we should do. How did you manage to figure out the solution so quickly?"    
    Nm "I don't know. How I felt at that moment is hard to explain."
    Nm smile "The best I could explain it is that I have never felt that determined to find a solution in my entire life. I think you being in mortal danger made me brave."    
    c "Thank you, Naomi. I feel assured to be able to count on you like that. Let's still agree to not go on an adventure like that ever again, right?"
    Nm normal "Deal."
    $ renpy.pause (2.0)
    c "But yeah, I'm pretty exhausted. Could you stay in bed with me for a while longer?"
    Nm smile "Of course. Such a hectic evening calls for some rest with your favorite partner."
    hide naomi with dissolve
    scene black with dissolvemed
    play sound "fx/bed.ogg"
    m "We lay together in bed enjoying each other's company and after some time I fell asleep due to the exertion I had been through today. When I woke up from my nap it was already getting late."
    scene eckannabedroom3 with dissolvemed
    show naomi sleep with dissolve
    m "Naomi was still sleeping soundly, partially on top of me."
    $ renpy.pause (1.0)
    c "Hey, Naomi."
    $ renpy.pause (1.0)
    Nm slsmile "Huh?"
    m "I tugged her a little bit."
    c "Naomi, it's getting late. I should get back to my apartment."
    $ renpy.pause (2.0)
    Nm smile "Nonsense. You're staying here with me."
    c "Won't Bryce and Sebastian get worried if I don't go back to my apartment before dark?"
    Nm blank "No, it's fine. I asked them to give you permission to stay over at my place since we're, you know, intimate."
    Nm stern "I'm more than strong enough to protect you from Reza. Also, I have a security system so I doubt he's even going to be able to break in here without us noticing."
    c "But I don't want to put you at risk."
    show naomi surprised with dissolve
    c "I'll just get going."
    $ renpy.pause (2.0)
    play sound "fx/bed.ogg"
    m "I slowly disentangled myself myself from Naomi and tried to stand up next to the bed."
    show naomi concern with dissolve
    m "(Ouch!)" with vpunch
    m "My thighs, and especially calves hurt quite a bit. Suddenly, I didn't feel like going back to my apartment for the night."
    c "You're right. My legs are so sore that I would probably hurt myself even more if I walked back to my apartment. I'll stay with you."
    Nm smile "Trust me, I know what's best for you."
    $ renpy.pause (2.0)
    show naomi normal with dissolve
    c "Actually, even though I don't normally go to bed this early, I still feel like I could sleep for at least twelve hours right now."
    c "Could you please hug me to sleep?"
    $ renpy.pause (2.0)
    Nm shy "Actually... umm...{w} I don't feel that tired anymore. I would like to ease off my mind from what happened today by continuing on the series I was watching earlier today."
    Nm smile "I will come to sleep next to you the first moment I start feeling tired though. I promise you will have the sweetest dreams when I get back."
    Nm shy "If you need some more comforting you could always come watch the series with me."
    c "It's fine, go ahead. I seriously can't focus on any entertainment right now. Could you bring me a tall glass of cold water before you start a late-night binge on your series?"
    Nm normal "Sure."
    play sound "fx/sheet.wav"
    m "Naomi got off the bed, pushed her bedroom door open with her snout and walked out."
    show naomi normal flip with dissolve
    hide naomi flip with easeoutright
    play sound "fx/door/door_open.wav"
    $ renpy.pause (4.0)
    m "While waiting for Naomi to come back, I rest my head on one of the pillows and shut my eyes."
    scene black with dissolvemed
    m "(Seems that I dodged a bullet yet again. I'm happy to be still alive, but I want this just to stop.)"
    $ renpy.pause (8.0)
    play sound "fx/door/door_open.wav"
    scene eckannabedroom3 with dissolvemed
    show naomi normal with easeinright
    m "After a few moments, Naomi came back with my glass of water. She had also put some ice in it for me, to make the it even colder."
    play sound "fx/glassdown.wav"
    Nm "Here's your water."
    c "Thank you."
    $ renpy.pause (2.0)
    show naomi smile with dissolve
    play sound "fx/lewd/lickslow.ogg"
    queue sound "fx/lewd/lickslow.ogg"
    m "After setting down the glass, Naomi started licking the sides of her mouth with her long, draconic tongue."
    Nm "Would you like a little bit of something else before I go? I've noticed you like my tongue quite a lot."
    play sound "fx/system3.wav"
    s "Optional oral sex scene not written yet, come back later."
    c "Sorry, no. I just want to sleep."
    Nm blank "Alright, some other time then."
    Nm smile "Sleep well, [player_name]."
    c "Thanks."
    show naomi normal flip with dissolve
    hide naomi flip with easeoutright
    play sound "fx/door/door_open.wav"
    $ renpy.pause (2.0)
    play sound "fx/chug.wav"
    queue sound "fx/glassdown.wav"
    queue sound "fx/bed.ogg"
    stop music fadeout 1.0
    m "I drank some ice cold water and positioned myself for a well-deserved night's rest. It didn't take me very long to fall asleep."       
    scene black with dissolvemed
    $ renpy.pause (8.0)
    scene eckannabedroom4 with dissolvemed
    play music "mx/sail.ogg"
    m "I woke up a lot later than I usually did. I must have actually slept for over twelve hours, like I had wanted to. Judging by the dragon-sized shape next to me on the bedsheet, Naomi had already gotten up."
    play sound "fx/sheet.wav"
    m "My body was still sore all over, but at least I wasn't dead tired anymore. I got off the bed, slowly put my clothes on from the plastic bag and wandered carefully into the living room."
    play sound "fx/undress.ogg"
    queue sound "fx/door/door_open.wav"
    $ renpy.pause (4.0)
    scene black with dissolvemed
    $ renpy.pause (2.0)
    scene ecknaomiapt03 with dissolve
    show naomi normal with dissolve
    m "Naomi was lying on the sofa on her belly, seemingly just finishing up with her breakfast."
    Nm "Good morning, [player_name]. I made some scrambled eggs and bacon for you. Also, please help yourself to the juice. You need to get your strength up, and it has a lot of beneficial vitamins for you."
    c "Woah, you're able to cook?"
    Nm stern "Come on. Even someone with as clumsy hands as mine can make scrambled eggs and bacon."
    c "I appreciate you seeing the effort. Thanks a lot, Naomi."
    Nm smile "You're welcome."
    Nm blank "I don't really have any time to chat, because I am going to be late from work if I don't leave soon. Actually, you woke up just in time to see me off." 
    Nm normal "I have a much safer date planned for later, so give me a call once you're available. I promise you will love it."
    c "Sure." 
    c "Somehow, despite yesterday's disaster, I can't wait to go on a date with you again. I hope there are no bombs waiting for us where you're going to take me."
    Nm concern "Very funny."
    $ renpy.pause (1.0)
    Nm normal "Oh, I really have to go now. Bye!"
    c "Have fun at work. See you later, Naomi."
    hide naomi with dissolvemed
    play sound "fx/door/lock.ogg"
    $ renpy.pause (0.5)
    play sound "fx/door/handle.wav"
    $ renpy.pause (2.0)
    play sound "fx/door/doorclose3.wav"
    m "(She's in a very cheerful mood today. I guess she loves her job that much.)"
    m "(And me, of course.)"
    $ renpy.pause (2.0)
    m "(I'm starving.)"
    play sound "fx/eating.wav"
    m "I put all my attention to eating the scrambled eggs Naomi had lovingly cooked for me. The portion was rather large, dragon-sized in fact, but I ate it all since I needed the energy and nutrition to get back on my feet."
    play sound "fx/pour.ogg"
    queue sound "fx/gulp4.wav"
    queue sound "fx/glassdown.wav"    
    m "I washed my breakfast down with a full carton of cold juice. Even though this breakfast was very simple, it tasted like the best thing I had ever eaten, because Naomi had made it for me."
    stop sound fadeout 1.0
    m "With this hearty breakfast, I was ready to face whatever misadventures were going to come at me today. I dropped off my dishes at Naomi's sink, and exited to start the journey back to my apartment."
    stop music fadeout 1.0
    play sound "fx/door/lock.ogg"
    scene black with dissolvemed
    $ renpy.pause (0.5)
    play sound "fx/door/handle.wav"
    queue sound "fx/steps/slowstepsdown.ogg"
    $ renpy.pause (4.0)
    stop sound fadeout 1.0
    play soundloop "fx/steps/steps.ogg"
    scene ecknaomiaptoutside with dissolvemed
    $ renpy.pause (2.0)    
    scene town6 with dissolvemed
    stop soundloop fadeout 1.0
    #Inspired by Freefall's terrifying flashback scene
    m "When I had reached the park I was feeling a bit drowsy, so I decided to sit on one of the benches to take a short rest."
    m "(Just a short one, and I can continue the journey back to my apartment.)"
    $ renpy.pause (2.0)
    m "I relaxed myself on the bench's backrest and shut my eyes for a moment."
    $ renpy.pause (2.0)
    scene black with dissolve
    $ renpy.pause (4.0)
    scene eckoldbiolabsep with flash
    show naomi cry sep with dissolve
    $ renpy.pause (2.0)
    c "{cps=5}Naomi?{/cps}{w=2.0}{nw}"
    play sound "fx/snarl.ogg"
    $ renpy.pause (0.5)
    play sound2 "fx/explosion.ogg"
    show naomi scared sep with dissolve and hpunch
    $ renpy.pause (0.5)  
    scene black with flash
    scene black with vpunch
    $ renpy.pause (1.0)
    m "I felt incredible pain as my body was first engulfed and then disintegrated by a shockwave of fire in what felt like forever."
    c "NAOMI!!! NO!!!{w=8.0}{nw}"
    $ renpy.pause (4.0)
    stop sound fadeout 1.0
    scene ecknaomiapt01sep with flash
    show naomi hurt sep with dissolve
    $ renpy.pause (1.0)
    play sound "fx/rev.ogg"
    m "I woke up in Naomi's living room, pointing a gun upwards under her chin.{w=8.0}{nw}"
    scene black with dissolveslow
    c "{cps=15}It's okay, Naomi. It wasn't your{/cps}{nw}"
    $ renpy.pause (0.1)
    play sound "fx/gunshot2.wav"
    $ renpy.pause (0.5)
    play sound2 "fx/silence.ogg"
    queue sound2 "fx/silence.ogg"
    queue sound2 "fx/silence.ogg"
    queue sound2 "fx/silence.ogg"
    queue sound2 "fx/impact3.ogg"
    c "{cps=10}...fault.{/cps}{w=2.0}{nw}"
    $ renpy.pause (2.0)
    m "({b}WHAT HAVE I DONE?!{/b}){w=4.0}{nw}" with vpunch
    $ renpy.pause (4.0)
    m "(I don't want to live after doing this.){w=8.0}{nw}"
    $ renpy.pause (2.0)
    play sound "fx/rev.ogg"
    $ renpy.pause (4.0)
    play sound "fx/gunshot2.wav"
    $ renpy.pause (1.0)
    play sound "fx/impact.ogg"
    m "My entire body went limp and I fell face down on the cold, hard floor."
    $ renpy.pause (8.0)
    m "When I had finally snapped out of it, I found myself lying on the ground next to the bench I had sat on. My hair and shirt were wet, because my entire upper body had sweated profusely."
    scene town6 with dissolvemed
    m "A group of dragons had gathered around me to see if I was okay, but by some miracle I hadn't hurt myself badly when I had fallen down. I was still confused, so I started getting up without paying them any mind."
    m "(What the hell was that!? It felt...{w} so real. Could it even be real?)"
    $ renpy.pause (2.0)
    m "After a moment, I finally managed to get up from the ground. I said nothing, still bewildered by this horrifying experience, patted my clothes and continued making my way back to my apartment."
    play soundloop "fx/steps/steps.ogg"
    scene town7 with dissolve
    m "Since nothing like this obviously had happened to me before, and because dreams could sometimes show your worst fears, I decided to shrug off what I had just seen. I had more important things to worry about right now, like catching Reza."    
    scene town1 with dissolvemed 
    $ renpy.pause (2.0)
    scene eckplayeraptextra1 with dissolvemed
    $ renpy.pause (2.0)
    stop soundloop fadeout 1.0
    scene black with dissolvemed
    play sound "fx/door/handle.wav"
    $ renpy.pause (2.0)
    play sound "fx/door/doorclose3.wav"

jump ml_date_end  
