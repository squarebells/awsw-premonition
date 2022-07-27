label sqb_naomi_m2_skip:
    
    stop music fadeout 1.0
    play sound "fx/system3.wav"    
    s "Would you like to skip to the cooking, or straight to the ending? If you have NSFW mode enabled, you can also skip to the fun."       
    menu:
        "Fun." if persistent.nsfwtoggle == True:
            s "Alright."
            $ renpy.pause (0.5)
            scene black with dissolvemed
            $ renpy.pause (1.0)
            $ naomi2mood = 12
            $ naomiromance += 100
            $ sqbnaomilewd = 6
            scene eckannabedroom4 with dissolvemed
            play music "mx/treetops.mp3"
            show naomi smile with dissolve
            jump sqb_naomi_m2_sexskip_end
            
        "Cooking.":
            s "Alright."
            $ renpy.pause (0.5)
            scene black with dissolvemed
            $ renpy.pause (1.0)
            $ naomi2mood = 12
            $ naomiromance += 100
            $ sqbnaomilewd = 6
            $ sqbnaomi2hadsex = True
            scene eckannabedroom4 with dissolvemed
            play music "mx/airborne.mp3"
            show naomi normal with dissolve
            jump sqb_naomi_m2_cooking
        
        "Ending.":
            s "Alright."
            $ renpy.pause (0.5)
            scene black with dissolvemed
            $ renpy.pause (1.0)
            $ naomi2mood = 12
            $ naomiromance += 100
            $ sqbnaomilewd = 6
            $ sqbnaomi2hadsex = True
            scene ecknaomiapt03 with dissolvemed
            play music "mx/airborne.mp3"
            show naomi normal with dissolve
            jump sqb_naomi_m2_ending

label sqb_naomi_m2_chairs:

    $ renpy.pause (0.5)
    $ naomi2mood += 2
    $ sqbnaomilewd +=1     
    Nm surprised "You mean right now?"
    c "Sure, if those chairs bother you. I wouldn't mind helping you out."
    c "I think I am better suited for moving furniture around than you are, no offense."
    Nm normal "None taken. Thank you for the offer but I want to host you, not put you to work."
    Nm blank "I'll do it myself tomorrow."
    Nm "Enough about my chairs. Let's go rest on the sofa."
    scene ecknaomiapt03 with dissolvemed

jump sqb_naomi_m2_chairs_end

label sqb_naomi_m2_differences:

    c "Also, have you ever considered how much bigger you are compared to a human, or some of the smaller species of dragons? That brings up some interesting dynamics for people who appreciate differences."
    show naomi confused with dissolve
    m "(Let's tease Naomi a bit. Her squirming was really cute to watch last time.)" #Oops, it "backfires" on the PC
    c "Just speaking hypothetically, I bet someone as big as you would give excellent hugs to someone smaller than them."
    $ renpy.pause (1.0)
    Nm shy "..."
    $ renpy.pause (2.0)
    
    if naomi2mood > 2 and sqbnaomilewd > 3:
        $ sqbnaomilewd +=1
        Nm smile "Also, just speaking hypothetically, if I caught a puny human such as yourself, they would never be able to escape my clutches." 
        c "Actually, that's what dragons sometimes do to humans in our fiction."
        show naomi confused with dissolve
        c "Although, usually the dragons who deal with humans are assumed to be male and very powerful, and most of the time they only catch humans of the female sex."
        Nm concern "That trope makes no sense at all to me. Female dragons need representation too because we are just as strong as males."
        $ renpy.pause (2.0)    
        Nm blank "I would be very interested in hearing more about dragons in your fiction, especially why they're usually assumed to be male."
        c "Well, I didn't really study literature at all or specialize in cultural history so I don't really know enough to break it down for you."
        show naomi concern with dissolve
        m "Naomi looked visibly disappointed."
        c "Fine, I'll try to think of something interesting to tell you."
        show naomi normal with dissolve
        $ renpy.pause (4.0)
        m "My mind was completely blank. Then suddenly, I had an urge to tell Naomi something funny."
        c "Now that I think about it, I agree with you that our dragon trope makes no sense. I'm sure there are a lot of male humans who wouldn't mind being caught by a female dragon."
        Nm confused "I hope you realized that I was just being hypothetical."
        c "Yes, of course. I have been hypothetical this entire time too."
        show naomi blank with dissolve
        c "Anyway, as a sociologist the most fascinating thing to speculate about regarding our species' future relationship is how we could complement each other." 
        c "It's going to be kind of an adaptation similar to how your different species of dragons have done their best to specialize to be as efficient as possible in their particular areas of expertise."
        c "But compare humans to runners for example. I know that they are decent at doing tasks that require precision, but humans are way better. Our limbs and especially nimble and long fingers are much better suited for articulate tasks than anything you've ever seen before."
        show naomi normal with dissolve
        c "Like I implied before, I wouldn't mind moving a few things for you, because it's much easier for me. Then, as a sign of reciprocity you could fly me across town or something, of course if you are comfortable doing that."
        show naomi shy with dissolve
        c "By the way, how long does flying across the town even take you?"
    else:
        Nm blank "I suppose that's true. Although, can you please tell me what your point is?"
        c "It's just a funny observation. Sorry if I offended you in any way, I was just being quirky."
        Nm normal "It's fine." 
        Nm concern "Hugs aside, being this big is quite an annoyance to me. I often have problems with just picking up or operating small things. Being a runner or even a human would make simple everyday life much easier for me." 
        c "How long does it take you to cross the town, though?"        

jump sqb_naomi_m2_differences_end

label sqb_naomi_m2_balcony:

    c "Coming on the balcony was a great idea. I really love feeling the sea air again." 
    c "It's been a long time since I have been able to visit a seaside beach because my city-state is in middle of a desert. Wandering outside the walls is very dangerous so recreational trips are out of the question."
    Nm confused "That's very unfortunate. I don't understand why anyone want to live in the middle of a desert when there are lush tropical forests and beaches everywhere."
    c "Where we live is not really our choice. In order to have even a chance at survival, we had to settle within a reasonable distance in a place where at least some of the infrastructure was intact."
    c "Anyway, standing in a peaceful place like this makes me both nostalgic and sad at the same time. I can't help but to think of all the hardship that has been placed upon us."
    show naomi sad with dissolve
    c "Living in my world is like a nightmare that never ends."
    Nm "I'm so sorry to hear that, [player_name]."
    show naomi shy with dissolve    
    m "Naomi seemed to be thinking about something."
    
    if naomi2mood > 3 and sqbnaomilewd > 4:
        $ sqbnaomilewd +=1
        Nm "Just a funny thought..." 
        Nm "I wouldn't mind if you stayed here with me. You're... um... good company."
        Nm smile "You should also invite as many people as possible from your city state. Like I've already said before, I would love to meet more humans. There's plenty of room for everyone."
        m "Naomi caught me off-guard, which caused me to feel an unexpected surge of emotions. Then, a tear slid down my cheek and I had to wipe it with my hand."
        show naomi concern with dissolve
        m "Naomi noticed it, and looked at me worriedly."
        c "Thank you, Naomi. You saying that makes me feel very happy."
        show naomi smile with dissolve
        c "I would love to take you up on your offer, if it ever becomes possible."
        Nm "I'm delighted to hear that. I know we would get along nicely."
        $ renpy.pause (1.0)
        c "To change the topic to something less gruesome, I have to say that in addition to the fresh sea air I really like the view as well."    
    else:
        Nm blank "I just hope things get better for your people. Do you mind if we changed the topic?"
        c "Not at all. This view from your balcony is nice, isn't it?"

jump sqb_naomi_m2_balcony_end

label sqb_naomi_m2_movie:

    c "I couldn't agree more."
    c "Anyway, hearing the story of how through an unlikely series of events you became a police analyst was interesting. It's actually similar in some ways to how I ended up becoming an ambassador to your world."
    Nm surprised "Oh, really?" 
    Nm normal "I would be very interested in hearing some more about you."
    menu:
        "Tell Naomi about my past.":
            $ renpy.pause (0.5)
            c "Unfortunately, my life story isn't a happy one. I hope you don't mind."
            $ sqbnaomilewd +=1
            $ naomi2mood += 1 
            
        "Don't ruin the mood.":
            $ renpy.pause (0.5)
            $ sqbpremounlocked = False #Just in case, might be redundant
            c "I'm sorry to disappoint, but I don't want to ruin the mood. The story of how I ended up here is not a happy one."
            Nm sad "Oh well. I'm sorry if my inquiry into your past was too personal."
            c "It's fine. I just don't feel like talking about myself right now."
            $ renpy.pause (1.0)
            Nm normal "Speaking of moods, would you like to shift your focus from the harsh realities of everyday life by watching a fine movie with me? I've got quite the collection."
            c "I would like that a lot. What kind of movie do you have in mind?"
            jump sqb_naomi_m2_origmovie_end
       
    show naomi concern with dissolve
    m "Naomi sighed and looked at me with concern."
    Nm blank "Don't worry, I can take it."
    c "Alright. Where to begin..."
    show naomi normal with dissolve
    $ renpy.pause (1.0)
    c "Like I might have alluded to earlier, my world used to be pretty prosperous. Our quality of life and general happiness were dramatically higher than ever before due to technological advances."
    c "Well, I suppose social advances such as decreasing inequality and getting rid of most of human exploitation played a huge part too."
    c "Also, we used our technology to automate most tedious and difficult jobs in order to have more time to do what we actually wanted to do with our lives, like anything related to hobbies or simply just improving ourselves as people."
    show naomi surprised with dissolve    
    c "Our technology was far superior to yours. I suppose it still is, but just very hard to come by. For example, we had computers everywhere, even on our wrists."
    Nm blank "That sounds like a very inconvenient invention to me. I wouldn't even know how to begin to use a computer on my wrist."
    c "Then you're in luck, because those are pretty rare nowadays due to what I told you about earlier."
    show naomi normal with dissolve
    c "Anyway, the future seemed pretty bright for all of humanity, but especially for me as well, because I had gotten myself majors from both biology and sociology. Skills from those fields were in demand at the time due to rapid social advances."
    c "Unfortunately, not that long after my graduation the flare hit our world and my degrees became pretty much worthless in the ensuing aftermath."
    show naomi concern with dissolve
    c "A whole different set of skills would've been far more useful to help me in what I had to go through. Yet somehow, mostly due to sheer luck, I managed to stay alive."
    show naomi sad with dissolve
    c "I really don't want to get into the uncomfortable details. It suffices to say, if you have ever seen a post-apocalyptic movie, it was like that but worse."
    Nm blank "I have never heard of that genre, although based on the name I can guess what it's most likely about. It sounds amazingly interesting to me."
    c "In post-apocalyptic movies...{w} never mind."
    Nm confused "Huh?"
    c "It's not that interesting to explain. Let me continue my story."
    show naomi normal with dissolve
    c "So, somehow I managed to survive and find my way to the city-state, Bastion, where I currently reside in. Things are quite bad there compared to your world but like I said, the world outside our city's walls is basically a hellscape."
    show naomi sad with dissolve
    c "Anyway, before I became ambassador I was just doing odd jobs to survive. I suppose things weren't all that bad if you look at the big picture."
    c "To fast forward, we found the portal on a scouting mission and sent Reza, who had volunteered, to investigate your world after the initial contact."
    show naomi blank with dissolve
    c "In his case, there wasn't really any kind of process to select the most suitable person to go since we were desperate for any kind of help or even information. I have to admit that we didn't really care if he had died on the mission."
    c "This was because Reza was known to be a troublemaker, so him dying really wouldn't have been big loss. You wonderful dragons could've been savage, man-eating monsters for all we knew at the time."
    Nm smile "You have seen nothing yet. Just stick around for long enough and I might show you all of my abilities."
    play sound "fx/sheet.wav"
    m "Naomi's strange remark and simultaneous shift towards me on the sofa almost made me jump up from my sitting position. I managed to mostly control myself but I'm sure she noticed me twitch and change my own posture a little bit."
    c "I... uhh..."
    play sound "fx/lewd/lickslow.ogg"
    m "She winked at me and licked her figurative lips."
    c "Where was I..."
    show naomi normal with dissolve
    c "Anyway, I was selected from a large pool of applicants to be the second person to visit your world. Due to having degrees in both biology and sociology I was uniquely qualified."
    c "Sending someone takes a lot of power so it'll just be me and Reza interacting with you until we get one of the generators. His behavior leaves a lot to be desired."
    show naomi concern with dissolve    
    c "Well... that would be the understatement of the century, if he is indeed guilty. Murdering someone is unforgivable even in our harsh society. I hope we catch him soon and find out the truth so we can end this mess."
    Nm smile "I hope so too. We need to get this murder mystery over with because I want to meet many more cute humans and tell them they're welcome with open arms."
    m "(She seems to like humans a lot.)"
    c "Naomi, you and the other dragons I have met have been much nicer to me than I could have ever anticipated. I really don't know what to say." 
    c "You caring about my people makes me feel very happy."
    m "Suddenly I started to feel another surge of emotions. My throat started feeling dry and I wanted to cry."
    show naomi surprisedblush with dissolve
    c "Your unconditional kindness towards us is somewhat unexpected, because I don't know what we did to deserve it. Being as dependent on technology as we were wasn't good, so the mess we're in is kind of our own making."
    
    if naomi2mood > 7 and sqbnaomilewd > 5:
        Nm stern "Don't say that. Everyone needs help sometimes."    
        Nm confused "Just make sure you have good friends..." 
        Nm smile "...or something more to help you out."
        play sound "fx/sheet.wav"
        m "Naomi moved a bit closer towards me on the sofa."
        c "Thank you again, Naomi. I really mean it."
        play sound "fx/bed.ogg"
        m "With my encouragement, she got up a little bit and shifted even closer towards me. Up close from my sitting position I finally fully realized how big she was. I started feeling a little intimidated but also intrigued by her different and powerful physique."
        Nm shy "Would you like a hug? I don't want to see a cute little human like you sad like this ever again."        
        menu:
            "Hug Naomi.":
                $ renpy.pause (0.5)
                m "(I already like her a lot and turning down her offer of comfort would be downright rude.)"
        
            "Back off.":
                $ renpy.pause (0.5)
                $ sqbpremounlocked = False
                m "(This didn't turn the way I expected it to. Also, I think I can solve my problems on my own without needing hugs from Naomi.)"
                c "Sorry, no. I don't feel like having one right now."        
                Nm sad "Oh well."
                $ renpy.pause (1.0)
                Nm blank "Would you at least allow me ease your mind off by watching a fine movie with you?"
                c "Sure, what kind of movie do you have in mind?"
                jump sqb_naomi_m2_origmovie_end
    else:
        Nm normal "I sincerely hope your people will get the help you need."
        $ renpy.pause (2.0)
        Nm "I think a fine movie is just what you need right now. It'll help you focus on something other than the harsh realities of reality."
        c "That works for me. What kind of a movie do you have in mind?"
        jump sqb_naomi_m2_origmovie_end
               
    c "Thank you. I really do need a hug right now."
    stop music fadeout 1.0
    show naomi slsmile with dissolve
    play sound "fx/sheet.wav"
    m "With that, Naomi leaned against me and I returned the show of affection by wrapping my arms around her upper body."
    m "Naomi was softer and cuddlier than I had expected from a water dragon. I was also surprised when I felt her strong breathing."  
    m "(I suppose an aquatic dragon needs strong lungs to be able to stay underwater for extended periods of time.)"
    play sound "fx/craphug.mp3"
    queue sound "fx/rub2.ogg"
    m "After I had been feeling her for a moment, she returned my hug by tying her arms behind my back and gently rubbing the side of my head with her snout."
    $ renpy.pause (2.0)
    Nm smile "Are you feeling better yet?"
    c "Yes, thank you very much. Hugging a big, cuddly dragoness is certainly a soothing experience."
    $ renpy.pause (2.0)
    play sound "fx/sheet.wav"
    m "After hugging Naomi for a moment, I tried to politely disentangle myself from her, but she wouldn't let me go."
    Nm surprisedblush "What's wrong?" 
    Nm slsmile "Let's stay like this so you won't feel sad while finishing your story."
    c "Sure, that works for me. Anyway, to continue..."
    show naomi normal with dissolve    
    c "Like you already know, our most important goal is to get one of your generators. Our need is urgent because soon we won't have enough power to run our hospital properly." 
    c "It's pretty advanced because luckily, a decent amount of tech, especially medical equipment was spared in our city due to precautions taken before the flare. I just hope the hospital or even our entire city to be honest is still standing by the time I have completed my mission."
    show naomi blank with dissolve  
    m "As I said that I was hit by the realization that I might not be able to come back here from my own world after completing my mission. After all, given the precarious situation we were in, who would care about researching dragon society and culture?"
    play music "mx/flashback.ogg" 
    m "Because of this sudden insight, it was the first time when even thinking about having to return through the portal made my stomach feel like an endless pit. A surge of panic was brewing up in me, so I thought about confiding in Naomi to ease it off."
    $ renpy.pause (1.0)
    show naomi concern with dissolve
    m "Then, she made that choice for me by interjecting about my sniffing and stopping the story."
    $ renpy.pause (1.0)
    Nm "Is something wrong?"
    $ renpy.pause (1.0)
    c "..."
    c "Yes, you could say that. I hate to admit that I am not looking forward to the day when I finally have to go back to my own world."
    c "How should I sum this up...{w} sticking together and working for the greater good has kept my people alive so far."
    show naomi confused with dissolve
    c "Because of the contradiction between this and my own preferences, I suddenly feel too helpless and powerless to make myself happy."
    $ renpy.pause (1.0)
    m "(That sounded weird.)"     
    c "What I'm trying to say is that, I sincerely don't want to leave at all because your world is so much better than mine."
    show naomi slsmile with dissolve
    play sound "fx/rub2.ogg"
    m "Again, Naomi started rubbing the side of my head with the side of her snout."
    Nm smile "If you really feel that bad about returning, you should definitely stay here with me."
    Nm normal "I'm sure they won't miss one human, or other potential like-minded folks who want to live with us instead."
    c "B-but...{w} I have to go back."
    show naomi stern with dissolve    
    c "My superiors might assume you're holding me hostage, and that would ruin everything we have been working towards."
    Nm "Don't be silly. Once you have our generators, they can come here themselves to see that you're okay."
    Nm blank "After all, if what you say is true about your world, why would anyone need to be held hostage in order to make them stay here?"
    m "A conflict inside me was ripping me apart figuratively. I knew duty to my people was important, but a growing part of me wanted to just lead a quiet and simple life in Dragonworld."
    m "It probably took Naomi a lot of courage to ask me yet again, considering her usually shy and reserved demeanor. I also didn't want to disappoint her in any way so I decided to accept the offer." 
    Nm confused "Well?"
    stop music fadeout 1.0
    c "I suppose you are right. I'll still have to make a formal request though, but I don't see why it would be declined if I explained myself well enough."
    show naomi smile with dissolve
    c "Thank you again, Naomi. Your advice is really thoughtful."
    play music "mx/enigma.mp3"
    Nm "So, it's settled then. You'll stay here with me so I can keep you safe forever."
    play sound "fx/bed.ogg"
    m "Before I could think of a witty comeback to throw at Naomi, she started using her body to slowly push me down on the sofa. I didn't protest because I still needed some comfort, so she then took one of the pillows that were lying around, put it down and lowered both of our heads on it."
    show naomi surprisedblush with dissolve
    play sound "fx/sheet.wav"
    m "Then, when we were down on the pillow, Naomi turned us both a little bit so that her back was against the sofa's backrest and mine was against her belly."
    $ renpy.pause (2.0)
    c "I feel a lot better now. Thank you, Naomi."
    Nm smile "Likewise, [player_name]. I couldn't resist pushing you down because your body is just too soft and cute."
    show naomi aroused with dissolve 
    play sound "fx/craphug.mp3"    
    m "As the response to my approval of her methods, Naomi then locked her arms under my armpits to tie me in a tight embrace. At this point, I couldn't have escaped even if I had wanted to try."
    show naomi slsmile with dissolve
    m "Finally, she placed her wing over me as some kind of an impromptu dragon-blanket."
    $ renpy.pause (4.0)
    Nm smile "If you ever try to go back to your horrible world I will capture you before you make it to the portal and hug you until you change your mind."
    m "(Oh well, looks like she solved my problem for me. Sadly, I won't ever be able to go back to that post-apocalyptic hellhole.)"
    Nm stern "I'll also protect you if they try to take you back by force. I'm a lot of dragon with a few tricks they won't be expecting."
    Nm normal "You will be safe here with me for the rest of your life."
    c "I promise I won't try to escape your clutches."
    Nm smile "Good choice. You should always remember that I only have your well-being in mind."
    Nm smile "Also, when your ambassador duties are over, your new job will be to act as my body pillow whenever I feel like it."
    c "(This is getting very interesting. I wonder what I have just gotten myself into.)"
    show naomi slsmile with dissolve
    play sound "fx/sheet.wav"
    m "We lied on the sofa for what seemed like forever. Occasionally Naomi shifted and rubbed my body in various ways, as if she was trying to find out where I was the squishiest. Based on the number of rubs, my belly seemed to interest her the most."
    m "Even though I was slowly getting more and more aroused and a little intimidated as well as Naomi's live body pillow, I still felt a peace I hadn't felt in a very long time."
    $ renpy.pause (3.0)
    Nm "You are a very cute and cuddly partner."
    Nm normal "Would you like to watch a fine movie with me?"
    c "Of course, I think this position is perfect for watching one."
    Nm smile "Likewise. You're the perfect-sized body pillow to for me to cuddle with while enjoying a well-written story."
    Nm "I actually have a large body pillow in my bedroom closet, but now I think I prefer one that's alive."
    m "Again, my throat started feeling unnaturally dry and I coughed."
    show naomi slsmile with dissolve
    play sound "fx/rub2.ogg"
    m "To calm me down, Naomi started gently rubbing my upper chest with her hands."
    c "Ohh..."
    play sound "fx/bed.ogg"
    m "Then she moved me a bit so my head was firmly lodged below her chin. After that she tightened her grip on me even more to properly lock me in place."
    c "I suppose this means I passed the product testing stage?"
    Nm smile "With flying colors."
    Nm normal "So, you said you like [ecknaomim2movie] films if I'm not mistaken?"
    c "Yeah."
    Nm "You're in luck because I just happen to have a good movie of that genre in the player. I don't want to get off the sofa so let's just watch that one."
    c "Don't you think we should get some snacks or at least something to drink though?"
    Nm smile "Are you trying to escape? Sorry, now that I finally caught myself a human I'm not letting them go."
    Nm normal "We'll be fine. Also, drinking and snacking might distract us from the more important part of watching films with someone you like."
    Nm smile "You know what I mean?"
    c "Alright, you win. It's not like I can resist your charms anyway."
    Nm "Good choice. Any escape attempts would've been weak and pathetic anyway."
    play sound "fx/bed.ogg"
    Nm normal "You better get comfortable. I'll only let you go after the movie is over."
    m "Naomi extended her arm and picked up the sizable remote from the table in front of us. She then pressed a couple of buttons and after she had fiddled a few more moments with it, the movie finally started playing."   
    stop music fadeout 2.0
    $ renpy.pause (2.5)
    scene black with dissolvemed  
    m "I focused more on Naomi's large body, breathing and warmth than watching the movie. My thoughts were a strange mix of arousal, submissiveness and terror throughout the entire session."
    m "Thankfully, because my back was against her belly she didn't find out how aroused I was for most of the time the movie was playing. It was for the better, because I had no idea how she would've reacted."
    m "The tease was almost unbearable, but I managed to keep any dirty thoughts to myself. When the credits started rolling, Naomi released me and we sat up next to each other on the sofa."   
    $ renpy.pause (2.5)
    scene ecknaomiapt03 with dissolvemed
    play music "mx/airborne.mp3"

jump sqb_naomi_m2_movie_end

label sqb_naomi_m2_bedroomfun:
    
    c "Well, you forgot that you have me to keep you company from now on. After my duties are done, I could come watch movies or series with you every day if that's something you would like."
    Nm shy "T-thanks...{w} but you don't have to stay with me {b}all{/b} the time, if you don't actually want to."
    c "Hey, there's no problem with us seeing each other as many times as we want. I think we have already had a lot of fun together."
    show naomi smile with dissolve
    $ renpy.pause (2.0)
    c "I have to admit that for being such a great person to hang around with, I'm very surprised to hear that you don't have an official special someone yet."
    Nm surprisedblush "Oh? How so?"
    c "Well, it's hard to believe that no dragon has ever tried to swoon you, because you're so cute."
    $ naomi2mood += 1
    Nm smile "My police badge might be scaring them off."
    Nm normal "But even if it doesn't, my schedule and lifestyle don't involve meeting a lot of new faces."
    Nm shy "I haven't had the chance to meet a person I'd consider for such a role in my life. Or maybe I'm just not trying hard enough, because..."
    Nm concern "...because I'm too afraid."
    c "What's there for you to be afraid of?"
    Nm "Getting rejected or humiliated, and then having said person think less of me for the rest of my life."
    c "Oh. That sounds rather extreme. I doubt anyone would actually do that to you."
    Nm "I know. But then, there's another fear. Something I once almost fell a victim to."
    Nm "The fear that said person would lie to me and fake acceptance, only to use me one way or another. Once bitten, twice shy."
    c "Oh. You did mention that earlier, but you talked about it so lightly, that I didn't think it had been anything serious."
    Nm blank "I've long moved on, but I just can't trust people in such matters anymore. Maybe not yet."
    c "There is no need to rush things. I'm sure that if someone likes you a lot they will let you take their time. Just look for different signs of affection to find out if they are really the right person for you."
    Nm smile "That sounds like a good plan, [player_name]."
    Nm "Are you speaking from experience?"
    menu:
        "Yeah, I've had a few affairs.":
            $ renpy.pause (0.5)
            $ naomi2mood -= 1
            Nm normal "They didn't last though, did they?"
            c "I guess not."
            c "But my method worked out pretty well, and you should try it, too."
            Nm "I'll consider it."
            
        "A little. Only tried it once before.":
            $ renpy.pause (0.5)
            Nm normal "But what happened later? Are you still seeing that person?"
            c "No, I'm not."
            Nm blank "Why? What happened?"
            c "This isn't the best time to talk about something like that."
            Nm normal "Alright. I'll think about using your method."
            
        "No. It was merely an assumption.":
            $ renpy.pause (0.5)
            $ naomi2mood += 1
            Nm smile "Didn't you say earlier that you don't have anyone waiting for you back home?"
            c "Yeah, you remember correctly."
            Nm normal "I see. I'll try your method and see if it works."
    
    $ renpy.pause (2.0)
    c "Actually, I really have to ask, do you at least have someone in mind? I hope it's not a secret."
    Nm concern "..."
    c "Come on, I like you as well. There's no need to hide your feelings if they are indeed mutual."
    c "Or are you trying to say that the type of cuddling we just did is normally done among just friends here?"   
    show naomi shy with dissolve
    m "Seems it was my turn to catch Naomi off-guard. She nervously looked me in the eyes, but then tried avoiding my gaze when I smiled and stared back."
    Nm "I... umm..."
    $ renpy.pause (2.0)
    
    if naomi2mood > 9 and sqbnaomilewd > 5:
        $ naomiromance += 100
        show naomi smile with dissolve
        m "After a moment of hesitation, Naomi finally looked back at me. Then she looked as if she was going to say something, but then stopped and sighed audibly."
        Nm "..."
        $ renpy.pause (2.0)
        Nm shy "I suppose it's time to finally openly admit that I like you as well."
        Nm smile "I've been thinking about dating you ever since we met. Are you happy now?"
        c "You're-{nw}"
        m "She cut me off as soon as I started to reply."
        Nm confused "You've been so persistent in trying to get me to admit I like you. Why else would you obey my every whim?"
        Nm normal "The weird thing about us is that even though we met very recently I feel like we have known each other for a long time. Also, we complement each other nicely because you understand me really well and also like me for who I am."
        c "What's not to like in a cute dragoness such as yourself?"
        Nm shy "Oh, stop it. You're much cuter than I am."
        $ renpy.pause (2.0)
        Nm smile "Did you know that I have always looked for a partner much smaller than myself? That's because I want to be able to easily put them in their place if they misbehave."
        Nm surprisedblush "I..."
        Nm shy "I didn't mean it like that."
        Nm "Well, I did but...{w} not that directly."
        Nm sad "I hope I didn't make you feel uncomfortable in any way."
        c "(This just gets weirder and weirder.)"
        Nm shy "I just hope that these kinds of feelings from you are mutual towards me."
        Nm concern "(Please...)"
        c "You should consider our session on the sofa a sign of my approval."
        show naomi smile with dissolve
        c "I really don't mind if you tease me by objectifying me a little bit. Somehow I feel like I can trust you to have my best interests in mind."
        c "I like you a lot, Naomi."
        play sound "fx/kiss.wav"
        show naomi aroused with dissolve
        m "With that, she suddenly kissed me on my left cheek."
        play sound "fx/lewd/lickslow.ogg"
        m "As she was pulling back from the kiss, she licked my cheek with her long tongue, leaving some saliva behind."
        Nm smile "I really like you too."
        Nm "You're the best body pillow I have ever had. We're going to have a lot of fun times together."
        c "That sounds wonderful." 
        m "(Being used as a body pillow by a dragoness is certainly something no human has ever experienced before.)"
        Nm normal "I'm so happy that you like me even though we're not of the same species."
        Nm smile "I hope you already realized that from my perspective, you humans are the cutest."
        m "(Yes, I think I might have gotten that impression.)"    
        Nm "I have never had such an adorable and squishy boyfriend before."
        c "You're making me blush just for being myself."
        Nm "That's my intention."
        $ renpy.pause (2.0)
        show naomi shy with dissolve
        m "Naomi looked off to the side and then back at me. She was clearly thinking about something."
        Nm confused "I just realized there is something that would improve our body pillow experience by a lot."
        Nm normal "I honestly don't understand why you humans cover your bodies up so much."
        Nm blank "Why don't you take your covers off? Having fabric between you and your partner kind of gets in the way."
        m "(This escalated faster than I ever could have anticipated.)"
        menu:
            "Undress in front of Naomi.":
                $ renpy.pause (0.5)  
                pass
            
            "Keep your clothes on.":
                $ renpy.pause (0.5)
                c "I don't feel comfortable doing that."
                Nm concern "Really? What's the big deal?"
                c "Among humans, taking your clothes off in front of someone is considered a very intimate, even a sexual act."
                show naomi confused with dissolve
                c "It's also pretty weird to do in a living room."
                Nm "After all that you still don't...?"
                Nm sad "Oh well. I get it."
                $ renpy.pause (2.0)
                Nm normal "Look at the time. Would you at least eat something before you leave?"
                jump sqb_naomi_m2_cooking_orig_end
                
    elif naomi2mood > 4:
        Nm normal "I like you too, but don't over-analyze what we did. I was just comforting you, because you clearly needed it."
        Nm smile "As for a special someone, I might have one in mind. They're a very nice person."     
        c "Oh, that's interesting to hear. May I ask who you're talking about?"
        Nm "It's a secret. That's all you will get from me for now."
        c "Alright. Let's keep it a secret then."
        jump sqb_naomi_m2_kiss_orig_end
    else:
        Nm blank "I was just comforting you, because you were so sad. Please don't read anything else into it."
        Nm smile "As for a special someone, not really."
        c "That's unfortunate. I thought someone as cute as you would easily find someone suitable."
        show naomi stern with dissolve
        $ renpy.pause (2.0)
        jump sqb_naomi_m2_kiss_orig_end        
        
    m "A whisper coming from deep in my mind told me to just do as she says."
    m "(I suppose because dragons don't wear clothes in the way we humans do, Naomi doesn't understand the implications of asking me to remove them in front of her.)"
    m "(We're indoors, so what does it even matter if I take all of my clothes off in front of her? It's about time to get adjusted to dragon culture already, so if it doesn't bother her, it shouldn't bother me either. When in Rome...)"
    Nm confused "Well?"
    c "Sure. In fact, that's a really good point. I have never thought about my clothes like that."
    show naomi normal with dissolve
    $ renpy.pause (2.0)
    stop music fadeout 1.0
    play sound "fx/undress.ogg"
    show naomi surprised with dissolve
    #Male or female?
    m "I got off the sofa and started taking my clothes off in front of Naomi. She looked at me curiously as I slowly removed them piece by piece."
    play sound "fx/undress.ogg"
    $ renpy.pause (2.0)
    show naomi surprisedblush with dissolve
    m "She was the most attentive when I started to remove my lower garments though. Her eyes fixated on my groin after I had taken my underpants off. The stare caused a chill to enter my spine and I shuddered, hopefully not visibly."
    Nm normal "In addition to your head, have fur even on your chest and between your legs? That must be weird." #Male version
    c "I can shave off my extra hair if it bothers you."
    Nm smile "No, I like it because it's kind of cute but also different from what I've seen before. I was mostly just wondering how it will feel when I hug you."
    c "..."
    #If player is female, Naomi comments on breasts instead.
    Nm normal "Also, your male parts look pretty squishy. I bet they're very vulnerable because they hang outside of your body like that."
    m "(Just what have I gotten myself into?)"
    $ renpy.pause (2.0)
    show naomi blank flip with dissolve
    m "Then, Naomi focused her attention away from my groin and looked to her left. I turned to see what she was looking at."
    scene sqbnaomiapt04 with dissolvemed
    hide naomi with dissolve   
    m "She seemed to be eyeing the area right of her fridge. I presumed that the door over there would lead to her bedroom. As I realized what she was thinking about, an another series cold chills went down my spine."
    m "(I hope I can make it undamaged out of this. She was already pretty rough with me.)"
    show naomi normal with dissolve
    m "Before I had more time to ponder about my fate she came in close on the sofa, looming right over me."
    play music "mx/campfire.ogg"
    Nm smile "This sofa is awfully small for cuddling. How about we have another session in the bedroom? If you play it nice, we could even go further than earlier."
    Nm aroused "Please?"
    Nm shy "I hope I'm not moving too quickly for you."
    m "(I guess she doesn't realize that from my perspective she's already asked to have sex with me.)"
    c "I would love to know dragons a lot better, if you know what I mean."
    Nm smile "If that's the case, please follow me to my bedroom. Who knows, maybe you will be the first one to survive a visit to the dragon's lair intact?"
    m "(Uh oh. That doesn't sound good.)"
    hide naomi with dissolve
    m "Naomi started moving towards her bedroom, beckoning me to follow her. I wanted to have sex with her but suddenly I was also scared of what that would entail."
    m "This was the last chance to run. If I entered her bedroom, there was no telling what would happen to me."
    menu:
        "Follow Naomi.":
            $ renpy.pause (0.5)
            m "I decided to ignore the the scared thoughts I had."
            $ naomistatus = "girlfriend"
            pass
         
        "Try to escape while you still can.":
            $ renpy.pause (0.5)
            stop music fadeout 2.0
            m "(If I want to escape, I have to time this correctly.)"
            scene ecknaomiapt02 with dissolvemed
            play sound "fx/sheet.wav"            
            m "As Naomi got closer to her bedroom door, I quietly picked up my clothes and started sneaking towards the exit."
            $ renpy.pause (2.0)
            m "Unfortunately, when I was halfway there Naomi heard me walking in the opposite direction. I felt her grab my hand and I was forced to turn around to face her. This startled me, so I dropped some of my clothes on the floor."
            scene ecknaomiapt01 with dissolvemed
            show naomi concern with dissolve            
            m "(Oh no.)"
            Nm "Is something wrong?"
            c "I'm sorry, Naomi. I changed my mind about this."
            $ renpy.pause (1.0)
            Nm sad "Oh well. Did I move too quickly for you?"
            Nm "I thought we had a good time together."
            Nm concern "(This always happens to me.)"
            m "(Hmm, how do I salvage this without upsetting her? She could be an useful asset in the future.)"
            m "I came up with a genius plan, that would work for sure."
            c "Uhh...{w} you got it all wrong."
            Nm confused "What do you mean?"
            c "You have been good to me so far, and I have enjoyed my time with you."
            show naomi concern with dissolve
            m "Naomi sighed loudly."
            $ renpy.pause (1.0)
            Nm "Go on."
            c "It's all me, not you. We can meet again some other time."
            c "I'm just leaving because I remembered that I have some urgent ambassador duties that need doing."
            $ renpy.pause (2.0)
            play music "mx/partingsong.ogg"
            Nm stern "Are you being serious right now?"
            Nm sad "That's the kind of thing they always say. Couldn't you at least come up with a less cliché way of dumping me?"
            c "Hey, I really mean what I said."
            $ renpy.pause (1.0)
            c "Anyway, I have to go. We can just meet again some other time."
            $ renpy.pause (1.0)
            Nm "..."
            Nm annoyed "I hate it when you guys patronize me like this. Do you think I am a hatchling?"
            Nm sad "After how nice I was to you, I expected that you would at least be honest with me."
            Nm stern "Did you seriously think I wouldn't notice you trying to sneak out?"
            Nm "Go on, leave. See if I care."
            c "Don't you think you're overreacting at least a little bit? You have to calm down right now."
            Nm annoyed "Shut up!"
            c "..."
            Nm stern "Take your stupid covers and leave."
            c "So, you're going to order me around just like that? This is really it for you then."
            c "Or did you forget who I am?"
            Nm "I hate your condescending flat-face so much."
            show naomi annoyed with dissolve
            m "Naomi's body language was screaming that she was preparing to attack me."
            Nm "Get out NOW!"
            hide naomi with dissolve
            scene ecknaomiapt02 with dissolvemed
            m "Not wanting to get paralyzed, I quickly grabbed what clothes I could from the floor and walked up to the door to escape."
            show naomi cry with dissolve
            play sound "fx/door/handle.wav"
            m "As I turned to look at Naomi for one last time, I could see that she was crying."
            m "(I fucked up really badly.)"
            $ renpy.pause (0.5)
            scene black with dissolveslow
            $ renpy.pause (0.5)
            play sound "fx/door/door_close.ogg"
            queue sound "fx/steps/slowstepsdown.ogg"
            m "At this point of escalation had no other choice but to just leave her alone."           
            m "Somehow I knew that due to being this rude to Naomi, she wouldn't ever want to see me again."
            m "Shocked at what had just happened, I didn't even notice Sebastian napping outside Naomi's apartment."
            stop music fadeout 1.0
            stop sound fadeout 1.0
            play sound "fx/steps/steps.ogg"
            m "Not even bothering to put my clothes on, I slowly wandered back to my apartment and went straight to bed."
            stop sound fadeout 1.0
            m "My dreams that night were full of fire and suffering. I woke up several times, trembling in cold sweat." 
            $ naomistatus = "bad"
            $ naomiavailable = False
            $ naomiscenesfinished = 2           
            jump ml_date_end               
     
    $ renpy.pause (1.0)
    scene black with dissolvemed
    hide naomi with dissolve
    play sound "fx/sheet.wav"
    m "I picked up my clothes from the floor and quickly trailed behind Naomi as she walked up to her bedroom door and nudged it open with her snout."
    play sound "fx/door/door_open.wav"
    $ renpy.pause (1.0)    
    scene eckannabedroom4 with dissolvemed
    show naomi smile with dissolve
    Nm "Welcome to my bedroom. Consider yourself lucky to see it so early into our dating." 
    c "Did you finally come around to admitting that our meetups were actually dates from the get-go?"
    Nm stern "Don't ruin the mood by trying to be a smart ass. From now on, always remember that in the bedroom, I'm in control."
    c "S-sorry."
    show naomi smile with dissolve
    m "After silently accepting my apology with a nod, Naomi walked to up to the side of her bed. There, she turned at me to give an inviting look."
    show naomi aroused with dissolve
    play sound "fx/bed.ogg"
    m "Then she climbed on the bed and rolled on her back, spreading her wings wide."
    show naomi surprisedblush with dissolve
    m "Finally, she turned herself slightly towards me and stretched her legs wide, while still holding my gaze."
    m "(Naomi looks huge on that bed. You really notice how much bigger she is compared to a human when she spreads out like that.)"
    show naomi normal with dissolve   
    m "Naomi patted the empty space on her right side with her hand."  
    Nm shy "My bed feels so empty right now."
    c "I think I can fix that."
    m "I dropped my clothes on the floor and walked up to the right side of Naomi's bed."
    play sound "fx/undress.ogg"
    m "I sat down, turned and began to lower myself on Naomi's wing, preparing to position myself to have my back against her belly like before."
    Nm smile "That position won't do. I want to feel your squishy belly rub against mine."
    play sound "fx/bed.ogg"
    m "Then, Naomi suddenly grabbed my sides, turned me around and hugged me lovingly."
    c "Ooh."
    play sound "fx/craphug.mp3"
    m "After a few more maneuvers, Naomi had me fully tied up against her body. She lodged my head under her chin, kind of similarly to when we had watched the movie."
    show naomi slsmile with dissolve
    play sound "fx/rub2.ogg"
    m "Naomi finished the job by wrapping her wings around me and rubbing my back. She was very warm and I could now properly feel her powerful heartbeat."
    $ renpy.pause (2.0)
    Nm shy "Don't hesitate to tell me if I hug you too tightly or make you feel uncomfortable in any way."
    Nm smile "I don't want to damage the human I have caught, physically or mentally."
    c "No worries, I'm feeling very comfortable and relaxed in this position."
    
    if persistent.nsfwtoggle == False:
        stop music fadeout 1.0
        show naomi stern with dissolve
        $ renpy.pause (2.0)
        play sound "fx/system3.wav"
        s "Skipping the lewd scene since it looks like you have the NSFW mode turned off."
        show naomi normal with dissolve
        play music "mx/airborne.mp3"
        $ renpy.pause (2.0)        
    else:
        pass

    show naomi slsmile with dissolve
    #Female version later
    $ renpy.pause (2.0)
    m "Naomi's rubbing combined with her warm and soft body started to arouse me a lot. To make things even worse than before, due of my different position and because I wasn't wearing any clothing, my now hardening penis was in unobstructed contact with her soft belly."
    m "(Oh no. I hope her learning more about my mammalian traits won't be too embarrassing.)"
    Nm shy "Have I now convinced you that your place is here with me?"
    c "You convinced me a long time ago. I wouldn't trade being here with you for anything."
    Nm aroused "Likewise. When we first met, somehow I immediately knew we would get along nicely."
    show naomi slsmile with dissolve
    play sound "fx/sheet.wav"
    m "Then suddenly, Naomi locked me in place with her legs, shifting me around a little bit to hold me even more tightly than before."
    play sound "fx/purr.ogg"
    m "After that she purred while tying my ankles together with the end of her tail."
    Nm "Very nicely... in fact."
    $ renpy.pause (1.0)
    m "A terrified feeling washed over me as I realized that due to my position shifting again, my tip was now directly poking her belly."
    stop music fadeout 1.0
    stop sound fadeout 1.0
    $ renpy.pause (2.0)
    show naomi surprisedblush with dissolve
    m "Naomi dislodged my head from under her chin, lowered her draconic snout in front of my face and stared me in the eyes with an awkward look."
    m "(Oh no no no.)"
    $ renpy.pause (1.0)
    Nm shy "Is that what I think it is?"
    c "I can't control my penis. It gets erect on its own with sexual stimulation."
    Nm surprisedblush "Oh..."
    c "..."
    c "I take it that it doesn't weird you out?"
    $ renpy.pause (2.0)
    Nm smile "Why would you being sexually aroused by me weird me out?"
    Nm slsmile "After all it just means that...{w} you know..."
    play sound "fx/lewd/lickslow.ogg"
    m "She licked my forehead with her long tongue."
    play music "mx/treetops.mp3"
    Nm aroused "...that you actually want to have sex with me."
    m "For some reason, Naomi's forwardness made me feel like my heart had just jumped to my throat. To make things worse, my face felt so hot, I would have bet that it had turned completely red."
     
    if modinfo.has_mod("BangOk") and bangok_four_bryce1_unplayed == False or bangok_four_xsebastian_unplayed == False or bangok_four_anna2.unplayed == False:
        m "(Why am I feeling so anxious right now? It shouldn't be that much different with Naomi.)"  
    else:
        m "(Why am I feeling so anxious right now? It shouldn't be that much different with a dragon.)"
    
    $ renpy.pause (2.0)    
    Nm smile "Have you thought of what other humans would say if they found out that you wanted to have sex with a dragon?"
    $ renpy.pause (1.0)
    m "After a moment of silence, I gulped loudly, which she surely heard."
    c "But there aren't-{nw}"
    Nm surprisedblush "Oh, so you've fantasized about doing it with a dragon before?"
    show naomi smile with dissolve
    play sound "fx/bed.ogg"
    m "Naomi shifted her arms behind my back to move me up a little bit. I could feel her starting to warm up more."
    Nm slsmile "Wanting have sex with someone who's of a different sentient species, now that's something..."
    Nm aroused "...that makes me excited as well."
    m "Due to her teasing remarks, my stomach was now full of butterflies and I was so embarrassed I felt like I was going to choke. Yet somehow, I managed to speak up again."
    c "Well I-{nw}"
    Nm surprisedblush "Don't worry about it."
    $ renpy.pause (1.0)
    m "Naomi craned her head forward, so that her maw was almost pressed to my face. I could feel her hot breath."
    Nm smile "By the way, your face is completely red. Are you feeling okay?"
    c "Yes... umm..."
    c "I'm just-{nw}"
    Nm "Feeling embarrassed and aroused? I'm teasing you because I knew you would be unbelievably cute flustered like this."
    $ renpy.pause (1.0)
    Nm "Your face looks tasty."
    play soundloop "fx/lewd/lickslow.ogg"
    hide naomi
    scene black with dissolve
    m "Naomi backed her head a little bit and I moaned in surprised and was forced to close my eyes as she started applying the full length of her serpentine tongue across my face."
    c "Aahh!"
    $ renpy.pause (2.0)
    stop soundloop fadeout 1.0
    $ renpy.pause (1.0)
    scene eckannabedroom4 with dissolvemed
    $ renpy.pause (1.0)
    show naomi slsmile with dissolve
    Nm "I'm going to keep you safe here with me and never let you you go."
    m "At this point my anxiety had gotten to the level that I felt like I was about to have some kind of seizure. Fortunately, Naomi was holding me so tightly that I could barely move at all. My resistance turned out to be indeed weak and pathetic."
    $ renpy.pause (1.0)
    Nm smile "Your face still looks hot. Let's cool it down some more."
    show naomi slsmile with dissolve
    play soundloop "fx/lewd/lickslow.ogg" fadein 1.0
    m "Again, Naomi started licking my face, this time mostly focusing on my presumably red cheeks."
    m "(I don't think she is being genuine in trying to cool me down. Not that I mind her playing with me like this.)"
    $ renpy.pause (2.0)
    stop soundloop fadeout 2.0
    c "I never thought I would say this but like it when my face is being licked, especially by someone as skillful as you."
    Nm smile "Thank you, [player_name]. I'm doing it because you're so delicious."
    $ renpy.pause (2.0)
    show naomi aroused with dissolve
    m "Naomi pressed her snout to my face and stared me in the eyes, again."
    Nm shy "Do you really want to go further with me?"      
    m "I felt like I had no choice but to fuck her immediately or I was going to die due to my heart bursting out of my chest."
    show naomi aroused with dissolve
    c "I would love to so much, if you will have me. You are a sexy and wonderful dragoness."
    Nm smile "I'm happy to hear that, my cute and vulnerable human. Let's see how well your species can perform." 
    Nm normal "When you removed your clothes, I saw where your genitals are located. I don't think our anatomies are too different to make this inconvenient for us."
    
    #Note to self for later: Naomi thinks having multiple partners is fine as long as you like her the most
    if modinfo.has_mod("BangOk") and  bangok_four_anna2.unplayed == False:  
        c "Actually, our anatomies aren't too different. I already had sex with Anna."
        Nm confused "What, really? She hates everyone, but suddenly took a liking to you?"
        Nm stern "Hold on...{w} did she agree do it to experiment on human anatomy?"
        c "Hey, you have been experimenting a lot on me as well."
        c "I just asked her to have sex with me as a wager for a game. It was that easy, because she is rather promiscuous. Not that I mind, of course."
        Nm smile "We're all promiscuous over here." #Meta, she means compared to humans
        c "So, how do you want to proceed from here?"
        Nm "First, I have another experiment of my own in mind."
        
    elif modinfo.has_mod("BangOk") and bangok_four_bryce1_unplayed == False:
        c "Actually, Our anatomies aren't too different. I had sex with Bryce when I went drinking with him."
        #More accurate references
        Nm confused "What, really? I'm surprised you can still walk."
        c "The alcohol helped a lot. And of course lots of lube."
        c "So, how do you want to proceed from here?"
        Nm smile "Let me think..."
        play sound "fx/system3.wav"
        s "Dialogue unfinished, for now."
    
    elif modinfo.has_mod("BangOk") and bangok_four_xsebastian_unplayed == False:
        c  "Actually, I already had sex with Sebastian. Our anatomies aren't too different."
        Nm "I'm not surprised, he's kinda cute. I just wish he dropped his dutiful police officer persona once in a while."
        play sound "fx/system3.wav"
        s "Dialogue unfinished, for now."
    
    #Note to self for later: PC is going to say he came here to establish friendly relations and fucking dragons is one way of achieving that
    elif modinfo.has_mod("BangOk") and bangok_four_bryce1_unplayed == False or bangok_four_anna2.unplayed == False:
        c "I have already had sex with Anna and Bryce. Our anatomies aren't too different."
        Nm surprised "You've already fucked two people I know since you came here?"
        Nm confused "That can't be a coincidence."
        Nm smile "Are you sure you're not a dragon-fucking sex tourist rather than an ambassador?"
        play sound "fx/system3.wav"
        s "Dialogue unfinished, for now."
    
    elif modinfo.has_mod("BangOk") and bangok_four_xsebastian_unplayed == False or bangok_four_anna2.unplayed == False:
        c "I have already had sex with Anna and Sebastian. Our anatomies aren't too different."
        Nm surprised "You've already fucked two people I know since you came here?"
        Nm confused "That can't be a coincidence."
        Nm smile "Are you sure you're not a dragon-fucking sex tourist rather than an ambassador?"
        play sound "fx/system3.wav"
        s "Dialogue unfinished, for now."
    
    elif modinfo.has_mod("BangOk") and bangok_four_bryce1_unplayed == False or bangok_four_xsebastian_unplayed == False:
        c "I have already had sex with Bryce and Sebastian. Our anatomies aren't too different."
        Nm surprised "You've already fucked two people I know since you came here?"
        Nm confused "That can't be a coincidence."
        Nm smile "Are you sure you're not a dragon-fucking sex tourist rather than an ambassador?"
        play sound "fx/system3.wav"
        s "Dialogue unfinished, for now."
    
    else:
        c "You're right about that. I know for almost certain where yours are as well."
    
    $ renpy.pause (2.0)
    Nm slsmile "I'll try one more thing to get us properly in the mood."
    m "Naomi freed one of her arms and used her claw to nudge my head upwards."
    play sound "fx/lewd/altpen.ogg"    
    m "Then she moved her mouth to mine and tongue kissed me, applying her long tongue inside my mouth. I almost coughed in surprise, but managed to hold it back."
    play soundloop "fx/lewd/pussy.ogg"     
    m "To tease me, she started tickling the inside of my upper jaw with the tip of her tongue. It was a weird tickling sensation I had never experienced before."
    show naomi aroused with dissolve
    m "When I leaned toward her to reciprocate the dragon tongue kiss, Naomi opened her eyes to look back at me directly. She looked at me like I was what she treasured the most in the entire world."
    Nm shy "(I love you so much.)"
    show naomi aroused with dissolve
    m "The only things I could do on top of staring back into her beautiful emerald eyes was to focus breathing through my nose and staying as still as possible."
    $ renpy.pause (2.0)
    m "Again, I was feeling like my chest was going to explode at any time."
    m "(I'm going to die of a heart attack by dragoness. What the hell are they even going to write on my tombstone?)"
    $ renpy.pause (2.0)
    stop soundloop fadeout 2.0
    Nm confused "You're completely powerless to do anything to resist my advances, aren't you?"
    Nm smile "I think we've had enough foreplay. It's time for me to move onto the main course."   
    Nm "Is fucking me sideways in this position fine by you?"
    m "I was surprised she even asked for my opinion. I managed to mumble up a response."
    c "A-any position with you is going to be amazing."
    Nm "Good little obedient human."
    play sound "fx/sheet.wav"
    m "Naomi released me from the prison of her legs and spread them a bit."
    Nm shy "Can you see the slit between my legs?"
    
    if modinfo.has_mod("BangOk") and persistent.bangok_cloacas == False:
        m "I looked down at Naomi's groin, seeing a single vertical slit and an asshole below it."
        m "It seemed that I needed to go down a little bit to reach her pussy and also to have some leverage to thrust inside."        
    else:
        m "As I turned my head to look at Naomi's groin, I now saw an aroused horizontal slit that had been well-hidden previously."
        play sound "fx/sheet.wav"
        show naomi smile with dissolve
        m "She freed some of her grip on me for me move my arm enough in order to feel what I was dealing with."
        show naomi surprisedblush with dissolve
        play sound "fx/lewd/penfast.ogg"
        m "As I fingered Naomi's cloaca for the first time, she shuddered in arousal and some of her love juices spilled onto my hand."
        play sound "fx/lewd/penslow.ogg"
        show naomi aroused with dissolve
        m "(Yep, she's certainly very aroused right now. I don't blame her, because I know I am an irresistible human.)"
        play sound "fx/lewd/penfast.ogg"
        m "I explored her dragon pussy some more with my fingers."
        $ renpy.pause (1.0)
        play sound "fx/lewd/pussy.ogg"
        m "I found out that even though Naomi's cloaca looked pretty wide at first glance, later on it narrowed and separated into two passages positioned vertically from each other."
        
        if modinfo.has_mod("BangOk") and bangok_four_anna2.unplayed == False or bangok_anon_anna4.unplayed == False:
            c "It's a bit different from Anna's, but I can manage everything because I am the dragon pussy master." #Cringe
            
        Nm smile "Like what you feel?"
        c "You want me to penetrate your upper passage, right?"
        Nm shy "Well yes..."
        show naomi smile with dissolve
        play sound "fx/lewd/lickslow.ogg"
        m "Suddenly, Naomi flicked my nostrils with her long tongue. I barely managed to receive it without shuddering uncontrollably."
        Nm aroused "...because that's where my eggs come from."
        m "(What kind of fantasies is she having right now?)"
        m "Looking down again after regaining my composure, it seemed that I needed to go down a little bit to reach her vaginal passage but also to have some leverage to be able to thrust inside properly."       
 
    Nm normal "Did you figure out what to do yet?"
    c "I can't really penetrate you in this position. My testicles are in the way of bending my dick downwards properly."
    Nm smile "Oh. That sounds like a problem we can't have, can we?"
    c "So, could you fully loosen your grip on me so I can go down to get a better position?"
    Nm "Anything for you."
    c "Also, shouldn't I put on a condom before we start getting into it?" 
    Nm normal "No, that won't be necessary since I don't have any STDs and I trust you don't have either. Otherwise you wouldn't have agreed to have sex with me in the first place."
    c "You guessed correctly, I don't have any STDs."
    Nm smile "That settles it then. We won't ever have to use protection as long as you handle yourself with care in any other sexual relationships in the future." 
    Nm shy "More importantly, I'm very eager to get to feel your human cum inside me every time you fuck me."
    Nm aroused "Who knows what might end up happening if we're lucky?"
    m "(What's she even talking about?)"
    $ renpy.pause (2.0)
    m "({cps=5}Oh...{/cps}{w} doesn't she know that I can't get her pregnant? Didn't she pay any attention in biology class?)"
    m "(That, or she's just teasing me to see if I like her enough to impregnate her in case that was even possible.)" 
    m "(I guess just I'll do my best to satisfy her kinks, because there is no possible way humans and dragons could crossbreed.)"
    Nm confused "So, will you cum inside me?"
    c "Whatever works for me. I just want to fuck you right now."
    Nm aroused "That's actually the nicest thing you have ever said to me."
    show naomi shy with dissolve
    play sound "fx/sheet.wav"
    m "I moved downwards between Naomi's muscular legs, my hands trailing behind her back all the way."
    play sound "fx/bed.ogg"
    m "Due to our size difference, in this position my face only reached up to her chest." 
    m "To finally put myself in position to penetrate Naomi, I secured my hands behind her lower back."
    
    if modinfo.has_mod("BangOk") and persistent.bangok_cloacas == False:
        show naomi aroused with dissolve
        play sound "fx/lewd/pussy.ogg"
        m "Then I used my fingers to spread her pussy and lined the tip of my erect penis with her opening."        
    else:
        show naomi aroused with dissolve
        play sound "fx/lewd/pussy.ogg"
        m "Then I used my fingers to spread her cloaca and lined the tip of my erect penis with her vaginal passage."
    
    c "Are you ready?"
    Nm slsmile "I've been ready for a while."
    play sound "fx/lewd/penslow.ogg"
    queue sound "fx/sheet.wav"
    m "When I had penetrated her hot and wet pussy one third of the way, she locked me tightly in place with her legs."
    Nm smile "Caught you!"
    play sound "fx/lewd/penfast.ogg"
    m "After the shallow initial penetration, I moaned as I bucked myself rest of the way in a single thrust. The sensation of fully plunging yourself into someone soft and bigger than you was exciting."
    
    if modinfo.has_mod("BangOk") and bangok_four_anna2.unplayed == False or bangok_anon_anna4.unplayed == False:    
        m "(Naomi's tighter than Anna. That's surprising since Naomi much bigger than her. I suppose Anna really has a preference for larger partners.)"
        m "(I'm still fortunate to have an above average penis, or else I most likely couldn't get Naomi off with it at all.)"
    else:
        if modinfo.has_mod("BangOk") and persistent.bangok_cloacas == False:
            m "(Even though Naomi is rather large, her pussy a lot tighter than you would expect. I suppose she's only had smaller partners, like she alluded to earlier.)"
        else:
            m "(Even though Naomi's slit is rather large when aroused, she's a lot tighter from the inside than you would expect. I suppose she's only had smaller partners, like she alluded to earlier.)"

        m "(I'm still fortunate to have an above average penis, or else I most likely couldn't get her off with it at all.)"
    
    Nm confused "Is that all you've got? Are you going to pump at all?"
    c "Uhh... I was lost in thought."
    Nm stern "This isn't the best time to lose yourself."
    c "Sorry!"
    play soundloop "fx/lewd/penslow.ogg"
    show naomi aroused with dissolve
    m "After having to apologize yet again I started penetrating Naomi's pussy with long, thorough thrusts."
    Nm smile "I like being with someone who obeys my whims."
    $ renpy.pause (1.0)
    m "Naomi wrapped her wings around me like before."
    Nm aroused "Keep that pace up. You're doing a good job."    
    m "In this moment, due to Naomi covering almost my entire field of view, she was the only thing that existed for me in the entire world."
    Nm smile "You belong to me now.{w} The only way to go is forward." 
    m "She was right, because due to being locked in place by her strong legs, thrusting forward with my pelvis was just about the only movement I could do."
    Nm slsmile "Remember, I'll only let you go after you cum inside me."
    $ renpy.pause (3.0)
    stop soundloop
    play soundloop "fx/lewd/penfast.ogg"
    m "As I got more used to the position I was in, I started thrusting faster into Naomi. I couldn't last very long though, since the extended tease had exhausted my stamina. Then, suddenly without a warning, a release started rapidly building up inside me." 
    m "After the realization that I was going to cum soon, I hoped she would be satisfied with my performance or at least be understanding of my predicament."
    c "Naomi... I'm going to cum soon."
    Nm surprisedblush "Already? Fine, but don't even think about pulling out."
    Nm smile "Not that I would let you anyway."
    Nm shy "I thought humans would last longer than this."
    c "It's your fault for teasing me for so long."
    Nm smile "That's just what someone with no stamina would say. Finish if you have to, but don't think that I'm done with you yet."
    stop soundloop fadeout 1.0
    play soundloop "fx/lewd/altpen.ogg"
    m "Since my body had gotten the permission from Naomi to finish, I instinctively started preparing to shoot my cum in her by thrusting deeper."
    Nm smile "I feel you're getting ready to release. I won't settle for anything less than a big fat load of your human cum in my deepest place." 
    m "Naomi's demand excited me so much that I came immediately. She sensed that, and used her leg lock to press me even more tightly onto her lower body."
    stop soundloop fadeout 2.0
    play sound "fx/lewd/penslow.ogg"    
    play sound2 "fx/lewd/cum.ogg"
    queue sound "fx/lewd/penslow.ogg"
    $ renpy.pause (1.0)
    show naomi aroused with dissolve
    c "Urgh!!!Ahh!!!{nw}" with hpunch
    $ renpy.pause (1.0)
    play sound "fx/lewd/penslow.ogg"
    queue sound "fx/lewd/cum.ogg"
    queue sound "fx/rub2.ogg"
    play sound2 "fx/lewd/lickslow.ogg"
    queue sound "fx/lewd/lickslow.ogg"
    queue sound "fx/lewd/lickslow.ogg"
    queue sound "fx/lewd/lickslow.ogg"
    queue sound "fx/sheet.wav"
    show naomi slsmile with dissolve
    m "I bucked against Naomi for one last time time to release my second rope of cum. After I was finished emptying myself into her, she let out a content sigh and started gently rubbing the back of my neck and licking my face. Then, when she was done petting me, she rolled on her back, taking me along with her."
    Nm aroused "I can feel a whole lot of your sticky seed inside me. You weren't joking about being pent up."
    Nm shy "Unfortunately, you didn't manage to get me off." 
    Nm smile "If you can't go again you can finish me off with your mouth."
    menu:
        "Use dick.":
            $ sqbnaomi2sexroundtwo = True
            c "I still have another round in me. Just give me a few moments to recover."
            Nm stern "Try to last longer this time."
            c "I promise I'll do better."
            show naomi normal with dissolve
            play sound "fx/rub2.ogg"
            m "My now almost limp dick still rested inside Naomi. After a few moments she released me from the prison of her legs so I pulled out and jerked my dick a couple of times. I breathed in deeply as I was working to get myself erect again."
            play sound "fx/rub2.ogg"
            $ renpy.pause (4.0)
            c "Okay, I'm ready for round two."
            Nm smile "Give it your best shot, pun intended. I know you can get me off this time."
            show naomi surprisedblush with dissolve
            m "I steadied myself on Naomi's spread-out legs and squeezed her enormous thighs. Based on her expression, she liked it when someone played with them."
            play sound "fx/lewd/penslow.ogg"
            
            if modinfo.has_mod("BangOk") and persistent.bangok_cloacas == False:
                show naomi smile with dissolve
                m "With my now increased leverage, I lined the tip of my dick with her vagina and immediately pushed myself fully inside her."
            else:
                show naomi smile with dissolve
                m "With my now increased leverage, I lined the tip of my dick with her cloaca and immediately pushed myself fully inside her vaginal passage."
                
            Nm aroused "Ohh. This time, I forbid you to cum before me."
            play soundloop "fx/lewd/penslow.ogg"
            m "After her approval of my methods, I started penetrating her with the same slow and deep thrusts as before."
            $ renpy.pause (1.0)
            c "How about a kiss? You'll have to use your tongue though, because I can't reach that far."
            show naomi smile with dissolve
            play sound "fx/lewd/lickslow.ogg"
            play sound2 "fx/lewd/lickslow.ogg"
            queue sound "fx/lewd/lickslow.ogg"
            m "I held out my tongue and Naomi flicked it and my nose with her own long, serpentine tongue."
            Nm "I'm going to punish you from afar with tongue lashes if you don't fuck me well enough."
            c "That's so hot and weird. You know just how to press my buttons."
            $ renpy.pause (2.0)
            m "As I kept fucking Naomi, some of my seed seeped out of her pussy. This made me even harder than before since it reminded me of what I had just done a few moments earlier. I hoped I would be able to do it many more times in the future, not just for the rapidly approaching second time."
            
            if modinfo.has_mod("BangOk") and bangok_anon_anna4.unplayed == False:
                $ renpy.pause (2.0)
            else:
                m "(I can't believe I just came inside a dragon's pussy. Doing that broke a pretty important barrier for the sake of advancing humanity.)"
            
            $ renpy.pause (2.0)
            Nm aroused "[player_name]...{w} I'm approaching my limit. Let's see if you're skillful enough to make us both cum at the same time."
            c "Urghh... I'll try my best."
            $ renpy.pause (2.0)
            stop soundloop fadeout 1.0
            play soundloop "fx/lewd/penfast.ogg"
            show naomi surprisedblush with dissolve
            m "To have some fun exploring Naomi's body, I grabbed her thighs and spread them to get a firmer access to her pussy. This time I hoped she wouldn't lock me in place, because I wanted to be in control for once." 
            m "Luckily she didn't protest, even though she could have stopped me easily."
            $ renpy.pause (1.0)            
            Nm smile "Almost there..."
            c "My naughty dragoness has been a good girl today. Does she want to know what the reward for good behavior is?"
            Nm aroused "W-what is it?"
            c "A huge, fat dose of my virile seed deep in her pussy. A massive human creampie!"
            $ renpy.pause (0.5)
            show naomi surprisedblush with dissolve
            m "As soon what I had just said had registered in Naomi, she looked at me, rolled her eyes and came with a cry of pleasure."
            play sound "fx/snarl.ogg"
            show naomi cums with dissolve
            play sound2 "fx/lewd/pussy.ogg"
            queue sound2 "fx/lewd/pussy.ogg"
            queue sound2 "fx/lewd/pussy.ogg"
            m "Naomi's vaginal walls clamped around my dick and she released a copious amount of girl-cum on me. After her high she slumped on her back, with her tongue lolling out." 
            show naomi slsmile with dissolve
            m "As I kept pounding her through her orgasm, and I noticed mine and her cum had already made a huge mess on the bed."
            $ renpy.pause (4.0)
            m "I shifted my hands behind Naomi's lower back for more intimate fucking, as she was clearly out of energy for the time being. Due to my shifting position, she mumbled something at me."
            Nm shy "H-hurry up and g-give me my treat for the second time."
            c "I'm almost there."
            $ renpy.pause (2.0)
            show naomi aroused with dissolve
            m "I started achieving my release more rapidly than before, since Naomi had commanded me to cum. My dick found newfound energy from somewhere deep in and became even harder than before."
            stop soundloop fadeout 1.0
            play soundloop "fx/lewd/altpen.ogg"
            m "As I switched to more shallow penetrations, my balls clenched and the tip of my dick exploded without warning inside Naomi. I grunted to let her hear my orgasm."
            show naomi surprisedblush with dissolve
            stop soundloop fadeout 2.0
            $ renpy.pause (0.5)
            play sound "fx/lewd/penslow.ogg"
            queue sound "fx/lewd/penfast.ogg"            
            play sound2 "fx/lewd/cum.ogg"
            queue sound "fx/lewd/penslow.ogg"
            queue sound "fx/lewd/penslow.ogg"
            queue sound "fx/lewd/penfast.ogg"
            show naomi slsmile with dissolve
            c "{cps=10}Hnnghh!{/cps}{nw}" with hpunch
            $ renpy.pause (1.0)
            queue sound "fx/lewd/pussy.ogg"
            queue sound "fx/craphug.mp3"
            m "After I had come, I collapsed on top of Naomi's soft underbelly, my completely spent dick still inside her. I felt both of our bodily fluids ooze our of her pussy."
            stop music fadeout 1.0
            $ renpy.pause (2.0)
            show naomi aroused with dissolve
            m "I raised my head to look at Naomi. She was watching me with a sublimely satisfied and happy face."
            Nm "That was amazing. Did I mention how I love when you males do exactly what I say?"
            c "I think you did." 
            c "This was amazing. Fucking someone with a physique different from yours is hot."
            Nm smile "Likewise. I especially liked how you tried to tame my legs. Don't fool yourself into thinking that I didn't let you do it on purpose though."
            c "Yes, we both know how much stronger you are compared to me."
            $ renpy.pause (2.0)
            play sound "fx/lewd/pussy.ogg"
            queue sound "fx/craphug.mp3"
            m "I removed my flaccid cock out of Naomi and crawled upwards on the bed to hug her neck. Then, I pulled myself up to kiss her on the mouth."            
        
        "Use mouth.":
            c "I'm spent, I'll just use my mouth."
            Nm "That works for me, since you already came inside."
            play sound "fx/system3.wav"
            s "Scene unfinished, come back later."
    
    $ sqbnaomi2hadsex = True
    $ persistent.sqbnaomi2sex = True
    show naomi surprisedblush with dissolve
    play sound "fx/kiss.wav"
    c "I love you so much Naomi. You're the only thing I want from life."
    Nm shy "Thank you."
    hide naomi with dissolve
    scene black with dissolvemed
    play sound "fx/bed.ogg"
    queue sound "fx/rub2.ogg"
    m "Being happier than I had ever been before, steadied myself on top of Naomi, closed my eyes and listened to her breathing and heartbeat in silence. She started rubbing my back with her hand."
    $ renpy.pause (8.0)
    m "After a while of absolute bliss, Naomi nudged my side with her arm."
    scene eckannabedroom4 with dissolvemed
    show naomi concern with dissolve
    Nm "I love cuddling with you, but don't you think we should get ourselves washed? Let's continue after a trip to the shower."
    Nm blank "On the sofa, though. Not in my bed right now."
    c "Of course. Showering sounds like a fun time."
    show naomi normal with dissolve
    play sound "fx/sheet.wav"
    m "To clean myself at least a little bit before getting off, I wiped my groin on the bed sheets. They were going straight to the washing machine anyways."
    play sound "fx/bed.ogg"
    show naomi surprisedblush with dissolve
    m "Then I rolled myself off the bed, and started putting my clothes back on. Naomi watched me the entire time, because I suppose she was interested to see how humans put  on their clothes."
    Nm confused "Why are you putting your clothes back on?"
    c "Habit, I guess. Also, there's a chance that someone might come over and I'm not comfortable being naked around just anyone."
    Nm normal "That's interesting. I have to admit that your customs make no sense at all to me."
    m "I decided to not make a snarky comment about her own customs. After a minute or so, I had almost put all my clothes back on."
    $ renpy.pause (2.0)
    play music "mx/airborne.mp3" 
    c "That was the best sex I have ever had. I think the hours-long tease had something to do with it." 
    Nm normal "It was certainly fun to play with someone who is too weak to resist anything I do to them."
    Nm smile "I'm looking forward to many more sessions like this."
    m "(I'm doomed.{w} Wait no, I'm in heaven.)"
    c "Me too."
    $ renpy.pause (2.0)
    m "After I had finished up by buttoning my shirt, decided to I approach Naomi with a proposal. I had already chosen she was the person I would want to be with for the rest of my life."
    c "Naomi, I can't think of a word to describe how much I love you. Do you want to get married?"
    Nm surprised "Umm...{w} is that how it works in your world?"
    Nm confused "We've only had sex once so far. That doesn't mean we should get married yet."
    Nm normal "Marriage is a long-term commitment."
    c "Didn't you say before that you wanted me to stay with you forever?"
    Nm concern "I did...{w} and I really do like you. I just want to be absolutely sure before I start making any actual long-term plans for my future."
    Nm sad "Like I mentioned earlier, I have had some bad experiences with relationships in the past and I would rather not get hurt like that ever again."
    m "(Seems that her fear of abandonment and self-esteem issues are worse than I initially thought.)"
    c "I'll do my best to prove myself worthy of you, then."
    Nm smile "Thank you for being so understanding."
    show naomi normal with dissolve
    $ renpy.pause (1.0)
    c "So, let's take a shower together?"
    Nm smile "Yeah, let's get ourselves cleaned up. We could even have some more fun there if you've recovered."
    c "We'll see about that. Let's go."    
    play sound "fx/rumble.ogg"
    $ renpy.pause (4.0)
    show naomi concern with dissolve
    m "(It seems that we forgot to eat.)"
    Nm confused "Oh, you're hungry?"
    $ renpy.pause (1.0)
    stop music fadeout 1.0
    play sound "fx/system3.wav"
    
    if persistent.sqbnaomi2cook == True:
        s "Would you like to skip the cooking and eating?"
    else:
        s "A lot of reading ahead. Would you like to skip the cooking and eating?"
        
    menu:
        "Yes":
            s "Alright."
            $ renpy.pause (1.0)
            hide naomi with dissolve
            scene black with dissolvemed
            $ renpy.pause (1.0)
            scene ecknaomiapt03 with dissolvemed
            play music "mx/airborne.mp3"
            show naomi normal with dissolve
            jump sqb_naomi_m2_ending
        
        "No":
            s "Alright."
            play music "mx/airborne.mp3"
            pass

jump sqb_naomi_m2_cooking

label sqb_naomi_m2_cooking:

    #Inspired by the original ASM's, Adine's shopping spree mod's and Lorem mod's cooking scenes
    #I know that some of the stuff cooks/prepares faster than in real life, but hey, this is fiction
    
    Nm normal "We could order some food if you wanted. Cooking ourselves works as well if that's something you'd want to do."
    c "Actually, a fun time in the kitchen sounds just like what I need right now. I want to return all the hospitality I have gotten here by pampering you back."
    Nm shy "You really don't have to. I enjoyed myself as well."
    Nm blank "Wouldn't it be easier if we just phoned in a food order and showered together while waiting for the delivery dragon to arrive?"
    c "Shower can wait. I really feel like cooking right now."
    c "Besides, I also want to find out how similar your food products are to ours. One of my personal reasons for coming here was to learn more about your society and customs."
    c "For now I'll have to say that the food's been pretty similar to ours. Still, I would be very interested in delving deeper into this by getting some first-hand experience."
    Nm smile "Well, if you put it like that...{w} I suppose I will have to let you sate your curiosity. More importantly, I would never turn down a delicious home-cooked meal." 
    c "Looks like that's settled then. I promise you won't be left hungry like you are sometimes, because I'll cook a couple of dishes."
    Nm normal "What delicious human dishes are you going to cook?"
    c "I don't know yet. I'll have to see what you have in the kitchen."
    c "Let's go."
    hide naomi with dissolve
    scene black with dissolvemed
    play sound "fx/door/door_open.wav"
    m "We exited Naomi's bedroom back into the main part of her apartment. For some reason, this time she was trailing behind me instead leading me like before."
    scene ecknaomiapt02 with dissolvemed
    show naomi normal at Position (xpos = 0.9) with dissolve
    c "First, I really need drink a liter of water, or two. Would you like something to drink as well?"
    Nm "Sure. The glasses are in the kitchen cabinets." 
    Nm blank "I'll go wash myself while you get set up. If you need any help figuring out where everything is just give me a shout."
    show naomi normal flip with dissolve
    hide naomi with easeoutright
    play sound "fx/door/door_open.wav"
    queue sound "fx/door/doorclose.ogg"
    m "Naomi hurried off to what I presumed to be the bathroom."
    m "(Let's see what kind of stuff she has in the fridge.)"
    play sound "fx/crapfridge.mp3"
    m "As I started looking inside, yet again I noticed that a lot of the packaging had familiar shapes and even labels."
    m "(Not a surprise that it's mostly the same stuff my apartment was stocked up with. Still, somehow I haven't gotten used to how weird it is that so many things even down to tiny details like labels on food products are so similar compared to human ones.)"
    m "(I have to admit that while this makes me feel a bit familiar, I'm also slightly unsettled at the same time.)"
    m "(Oh right, Naomi wanted to drink something. She liked juice, right?)"
    m "I took a carton of juice from the back of the fridge."
    play sound "fx/cabinet.ogg"
    queue sound "fx/pour.ogg"
    queue sound "fx/glassdown.wav"
    m "Then I poured the juice in a large glass. After that I added a straw and placed the glass on the kitchen counter."
    m "(I guess I can give it to her when she comes back.)"
    play sound "fx/pour.ogg"
    queue sound "fx/chug.wav"
    queue sound "fx/glassdown.wav"
    m "I took a smaller glass, poured some juice for myself and drank it in one go."
    m "(I really needed that. The juice tastes a bit like orange and mango.)"
    m "After getting some sugar and starting to re-hydrate myself, I was prepared to continue figuring out what all the stuff in Naomi's kitchen was."
    play sound "fx/cabinet.ogg"
    m "(It's the mostly the same thing with the produce in her cabinets as well. Also, there's so much stuff that you would think she cooks at home.)"
    m "(Wait, did she buy all this just to impress me? That's very cute.)"
    m "(Anyway, back to the main task at hand. I think at first it would be good to move a bunch of stuff on the kitchen counter and sort everything by type.)"
    play sound "fx/rummage.wav"
    m "With some effort, I moved most of the foodstuffs and ingredients onto the kitchen counter and organized them as best I could."
    m "(This is going to be fun. Still, having only two cooktops might pose a challenge. They're pretty old-fashioned as well.)"
    m "(As the second order of business, I'll put back what I won't use. I can always take something back if I need it later)"
    $ renpy.pause (1.0)
    m "(I'm not going to take my chances with the fish. Maybe I'll try some in the future, when I am more familiar with the types of fish here. Also, I can't be certain what's in some these cans even after reading the labels. I should play it safe, so they'll have to go.)"
    $ renpy.pause (2.0)
    m "(Some of these vegetables don't look familiar at all to me. I'll only use ones that look at least vaguely similar to what I have used before.)"
    $ renpy.pause (2.0)
    play sound "fx/crapfridge.mp3"
    queue sound "fx/cabinet.ogg"
    m "(Alright, this looks better. Let's figure out what we actually want to use.)"    
    $ renpy.pause (2.0)
    m "(Frying some noodles is definitely a pretty good idea. I'll use some lightly salted chicken fillets as well, although I am not yet sure how. Both are very solid picks no matter what I end up making.)"   
    m "(For example, I like the flexibility of these types fillets because you can always cut them to pieces if you want, but also season them how you like because there's only a small amount of salt on them. Noodles are great too, because almost everyone likes them.)"
    play sound "fx/faucet1.ogg"
    queue sound "fx/button_press.ogg"
    m "To start off, I poured water from the kitchen faucet into an electric teapot and turned it on to heat some water for the noodles."
    m "(It's a lot less effort to heat the water with an electric teapot. Also, the water stays hot longer inside it.)"
    play sound "fx/door/door_open.wav"
    queue sound "fx/door/doorclose.ogg" 
    m "As I was pondering on how to proceed, Naomi came out of the bathroom to check on how I was doing."   
    show naomi normal at Position (xpos = 0.9) with easeinright
    Nm "Did you manage to find out where everything is?"
    c "Yes, thank you. You seem to have quite a lot of stuff stored in your kitchen. I would have guessed you usually cooked at home if you didn't already tell me otherwise."
    Nm shy "Well..."
    Nm normal "I wanted to try out something new since you were coming over, so I made an exception and went on a shopping spree after work. It felt just like the right thing to do."
    Nm smile "Looks like my plan worked, since I managed to get you to cook for me."
    c "Oh, you got me with your scheme. This is going to be fun, I promise."
    Nm "I'll hold you to that. Don't let me down, [player_name]."
    c "By the way, here's something to drink."
    Nm normal "Thanks a lot. I'll leave you to it." 
    Nm concern "I don't think I would be of much help with my clumsy hands anyway."
    c "I hope they're not too clumsy for eating, or else I'll have to feed you."
    Nm smile "Is that an offer? I would love to have my very own cute little human servant who feeds me every time I am hungry."
    c "Uhh..."
    Nm "Did I mention that you're so cute when flustered?"
    Nm normal "Anyway, are you sure you're fine doing all this by yourself?"
    c "Sure, it's no problem. Just let me handle everything."
    Nm smile "Thanks a lot, [player_name]. I'll go watch some television while you cook."
    show naomi normal flip with dissolve
    hide naomi with easeoutright
    m "Satisfied with my assurance, Naomi walked past me into the living room. After that she jumped on the sofa in one smooth motion and started flexing."
    m "I kept watching Naomi as she did it. To me, the flexing made her look like a big scaly cat with wings and cute webbing. After finishing her exercise and settling back on the sofa on her belly, she noticed I was admiring her instead of preparing to cook."    
    show ecknaomicg1 at Pan ((250, 230), (620, 50), 15.0) with dissolvemed
    $ renpy.pause (7.5)
    m "She is so big and muscular...{w} especially her thighs and chest."
    $ renpy.pause (1.0)    
    Nm "Your mouth is gaping. Like what you see?"
    c "I think I already saw plenty in the bedroom. Although, I have to admit that you look very cute lying on the sofa admiring me."
    Nm "Hurry up with the cooking, or I'll have to eat you instead."
    c "..."    
    scene black with dissolvemed
    $ renpy.pause (1.0)
    scene ecknaomiapt02 with dissolvemed    
    m "(Where was I?)"
    m "(Oh right, let's see what else we have got.)"
    play sound "fx/rummage.wav"
    $ renpy.pause (2.0)
    m "(This white, basil-flavored mouflon and aurochs cheese looks remarkably similar to something we used to have.)"
    m "I cut open the packaging with a knife and then sliced off a chunk of the cheese into my mouth for a taste test."
    m "(Perfect taste. I'll cut this into pieces fry it with the noodles. On top of that some of these vegetables will add a nice texture and hopefully good flavor as well." 
    m "Also, we got soy sauce, wing sauce, brown sugar and ginger powder to season the whole thing. Let's start off by heating up a pan first.)"
    play sound "fx/metalbox.ogg"
    m "I took a pan and put it on the cooktop but as I turned on the heat I realized something."
    m "(Wait a minute. Let's first make sure I don't get eaten by a hungry dragoness.)"
    c "Naomi, would you like some bread sticks as appetizers?"
    Nm "Sounds great to me. In fact, I was just going to come over and eat your ingredients."
    c "Hey, if you eat them, I won't be able to prepare them into delicious dishes."
    m "I focused back on the task at hand and quickly picked all the required ingredients for the appetizers."
    m "(Toast, garlic paste, black pepper, salt and herb mix here we go. Wait, where's the olive oil?)"
    play sound "fx/cabinet.ogg"
    queue sound "fx/cabinet.ogg"
    queue sound "fx/rummage.wav"
    $ renpy.pause (8.0)
    m "After looking through some more of Naomi's kitchen cabinets I found the olive oil hidden behind some boxes."
    Nm "Need help finding something?"
    c "I'm fine. I was just looking for some olive oil."
    play sound "fx/button_unpress.ogg"
    $ renpy.pause (2.0)
    queue sound "fx/metalbox.ogg"
    queue sound "fx/unwrap.ogg"
    m "Next I turned on the oven and prepared two baking trays with baking paper."
    m "(I suppose I can bake a big pile, since slicing the toast won't take too long if I do it efficiently.)"
    m "(The oven probably isn't ready when I am done with the cutting, but I can always start preparing for something else. Also, I will have even more time when the bread sticks are in the oven.)"
    m "(Oh yeah, I also have to prepare the mix to flavor the bread sticks. Who knows if the oven will be ready after I have done that. Multitasking and planning ahead in the moment is so much fun.)"
    m "I opened a bag of toast and put several slices on top of each other on the cutting board."
    play sound "fx/crapcuttingboard.mp3" #Not perfect but it just works
    m "Then I cut the bread into neat sticks, moved them off to the side and started cutting another batch of toast."
    play sound "fx/crapcuttingboard.mp3"
    m "After a couple of minutes of knife-work, I managed to slice the entire bag of bread."
    m "Then to create the flavor mix, I combined a ton of garlic paste with some olive oil, pepper and salt. After that I arranged all the unbaked bread sticks on the two baking trays and used a spoon to apply the flavor mix."
    m "(Looks like I have some time left after all since the oven isn't ready yet. Let's figure out next what to do with the chicken.)"
    play sound "fx/rummage.wav"
    $ renpy.pause (2.0)
    m "(Looks like we have the ingredients for batter plus some herb butter. I'll stuff the chicken fillets with the herb butter and bread and fry them. I have never met someone who doesn't like that dish.)"
    play sound "fx/metalbox.ogg"
    m "I set a pan to heat up on the cooktop and cut open the large pack of chicken fillets."
    m "(Let's see... the eight chicken fillets in this pack should be enough for both me and Naomi. She can always eat the rest tomorrow if there's any left over.)"
    m "I placed a fillet on the cutting board and grabbed a knife."
    play sound "fx/sliceshort.ogg"
    m "In order to create a pocket for the herb butter I cut into the fillet horizontally through the middle and then expanded carefully, to make sure I don't create any additional holes that need plugging."
    play sound "fx/sliceshort.ogg"
    queue sound "fx/sliceshort.ogg"
    m "I repeated this arduous process for the seven remaining fillets."
    play sound "fx/crapcuttingboard.mp3"
    m "Next I sliced all of the herb butter into pieces and stuffed it inside the pockets I had just cut. After that I closed the hole in each fillet with a large toothpick. The most tedious part of my cookout was almost over, but time went quickly because I knew the effort I put in would be well worth it."
    play sound "fx/salt.ogg"
    m "To finish everything off, I sprinkled some black pepper on the stuffed fillets."
    m "(Finally done. Also, looks like the oven is ready just in time so I don't have to wait.)"
    play sound "fx/door/hallwaydoor.ogg"
    m "I put the baking trays with the bread sticks in the oven and set a timer. Our hunger was going to be alleviated soon."
    m "(I think I should figure out a side dish for the breaded chicken fillets before I do anything else. It might take a while to make.)"
    play sound "fx/rummage.wav"
    $ renpy.pause (2.0)
    m "(Looks like we have some higher-starch potatoes for mashing that would go really well as a side. Luckily, I have some hot water ready.)"
    stop sound fadeout 1.0
    play sound "fx/faucet2.ogg"
    queue sound "fx/metalbox.ogg"
    queue sound "fx/faucet1.ogg"
    queue sound "fx/button_press.ogg"
    m "I took a large pot, filled it with water first from the teapot and the rest from the kitchen faucet. Then I set the pot to heat up on the cooktop. Since I still wanted to save time on the noodles, I partially filled the teapot again from the sink and turned it on."
    m "(I wish I had realized this earlier, because boiling the potatoes will still take some time. I think if I peel them really fast I'll be on schedule for everything else.)"
    play sound "fx/faucet2.ogg"
    $ renpy.pause (1.0)
    play sound2 "fx/rub1.ogg"
    queue sound2 "fx/rub1.ogg"
    queue sound2 "fx/rub1.ogg"
    m "I emptied all the potatoes into the sink, then rinsed and rubbed them to get all the dirt off."
    $ renpy.pause (2.0)
    stop sound fadeout 1.0
    m "Then, after peeling the potatoes at a lightning speed, I had a large bowl of them ready to be boiled."
    m "(Another tedious step done in my quest to cook for Naomi. The water isn't boiling yet, so I should probably move back to the chicken fillets.)"
    play sound "fx/dishes.wav"
    m "To continue preparing the chicken fillets I took three deep plates and a flat one. I filled the deep plates with flour, egg with a touch of water and finally breadcrumbs. I placed them in a line on the counter with the empty flat plate at the end towards the stove."
    play sound "fx/water1.ogg"
    queue sound "fx/water1.ogg"
    m "I dipped a fillet in first flour, then egg, followed by breadcrumbs and finally egg and breadcrumbs again and placed it on the flat ready-plate. I repeated this messy process for the rest of the fillets."
    $ renpy.pause (2.0)
    play sound "fx/salt.ogg"
    m "Lastly, I sprinkled some breadcrumbs on all of the fillets on the ready-plate to make sure they were properly breaded everywhere."
    m "(The crunch is very important.)"
    m "(I think I'll time everything correctly if I cook four fillets at a time. The pan we got is more than big enough for that.)"
    play sound "fx/fry.ogg"
    m "I poured some olive oil into the hot pan, carefully placed four fillets in and put the lid on."
    stop sound fadeout 1.0
    m "(The proper way is to cook both sides with higher heat at first. That means it would be good if I remembered to turn them and then lowered the heat after both sides have been fried. Preparing them more slowly should also leave me time to focus on other stuff.)"
    play sound "fx/crapfridge.mp3"
    m "I set another timer for the chicken fillets. I used this free time to put some of the unneeded stuff back into the fridge."
    $ renpy.pause (2.0)
    m "(That was quick. The water for the potatoes is boiling already.)"
    play sound "fx/water1.ogg"
    queue sound "fx/salt.ogg"
    m "To not splash any hot water on myself, I took extreme care when dropping the potatoes into the pot and added some salt and set a new timer."
    $ renpy.pause (1.0)
    m "(Looks like the bread sticks are almost done. It doesn't really matter if I take them out a or so minute early so I might as well do it now to stay on schedule.)"
    play sound "fx/door/hallwaydoor.ogg"
    queue sound "fx/salt.ogg"
    queue sound "fx/unwrap.ogg"
    m "I took the trays out of the oven and sprinkled some herb mix on the baked bread sticks. Then I used the baking paper to slide them onto a very large plate and turned off the timer."
    play sound "fx/fry.ogg"
    m "Not forgetting about the chicken fillets, I turned them for the first time."
    stop sound fadeout 1.0
    play sound "fx/pizzabite.ogg"
    m "I ate a few of the bread sticks ward off my worst hunger. They were crunchy, spicy and garlicky but also most importantly tasty, like I had expected them to be."
    m "(I'm sure Naomi will love these.)"
    m "My hands got messy from eating with them so I instinctively wiped off the grease on a kitchen towel and realized something."
    m "(I'll have to make sure Naomi doesn't make a mess eating the bread sticks. She'll probably ask me to clean up afterwards if that ends up happening.)"
    scene ecknaomiapt03 with dissolvemed
    m "I picked up the bread stick plate along with some rather large napkins and went off to the living room where Naomi was lying on the sofa. She was attentively watching what I presumed to be one of those long series she had told me about earlier."
    show naomi normal with dissolve
    Nm "That was certainly a lot faster than waiting for a food delivery. It seems that we made the correct choice."
    show naomi surprised with dissolve
    m "I presented the appetizer plate to Naomi and it immediately perked up her attention."
    c "So, here's something to start off with. Do you think I made enough so that you won't have to eat me?"
    Nm shy "I hope you understood that I was just joking. In fact, I can go a long time without eating if I really need to. I just need to eat a lot to keep in shape for some of my more physical activities, like long-distance flying or swimming."
    c "I know. I was just playing along with your antics."
    Nm blank "Oh, you got me."
    Nm smile "Thanks a lot, [player_name]. These bread sticks smell delicious."
    c "You're welcome, Naomi. Please remember to use the napkins after you have finished eating. Also, avoid touching any of the furniture before you have wiped your hands clean."
    Nm shy "You're really thinking of everything for me, aren't you?"
    $ renpy.pause (1.0)
    show naomi surprised with dissolve
    play sound "fx/glassdown.wav"
    queue sound "fx/pizzabite.ogg"
    queue sound "fx/pizzabite.ogg"
    queue sound "fx/pizzabite.ogg"
    m "Naomi had been occasionally eyeing the bread stick plate hungrily ever I since I presented it to her, so it didn't come off as a surprise when right after I placed it on the table she stuffed a big handful of them right into her maw, which was followed by several audible crunches."
    Nm smile "Delicious!"
    $ renpy.pause (1.0)
    Nm normal "Why aren't you eating any? Surely there's enough for both of us."
    c "I already ate a couple in the kitchen, and that was enough for me. You should remember that I can't eat as much as you can so I have to leave some room for all the other dishes."
    Nm smile "That just means more for me then."
    c "I guess so."    
    
    if naomi1drink == "cocktail":
    
        Nm confused "By the way, could you make a human cocktail for me? I want something to drink with these delicious bread sticks."
        c "I would love to, but did you happen to buy any liquor on your shopping spree? I didn't find any in the kitchen."
        Nm normal "Yeah, I bought a bottle of something at the store that was recommended to me by the clerk. It's hidden in the fridge's door compartment."
        c "Alright. I'll check what cocktail ingredients you have and make the best one I can come up with."
        Nm smile "Thanks a lot. I knew I could count on you on that front."
    
    else:
        Nm "Could I get some more juice with these delicious bread sticks?"    
    
    c "I'll go back to the kitchen now."
    Nm normal "I'm really looking forward to what else you can come up with."
    hide naomi with dissolve    
    scene ecknaomiapt02 with dissolvemed
    play sound "fx/fry.ogg"
    m "After getting back, I turned the chicken breasts again and lowered the heat."    
    stop sound fadeout 1.0
    m "(Let's now focus on getting the noodles ready. Luckily, the water inside the teapot seems to still be hot enough for the noodles.)"
    play sound "fx/pour.ogg"
    m "I emptied the entire pack of noodles into a pot and then poured in some hot water from the teapot."
    m "(I should have enough time to finish the rest of the ingredients while the noodles cook.)"
    play sound "fx/faucet2.ogg"
    queue sound "fx/veggies.ogg"
    m "I rinsed some of the more familiar-looking vegetables and put them in a neat pile on the cutting board and then used my knife-work to turn them into pieces of various sizes."
    $ renpy.pause (2.0)
    stop sound fadeout 1.0
    play sound "fx/crapcuttingboard.mp3"
    m "After finishing up, I cut the cheese I had selected previously, taking extra care to make sure all the bits were of the same size."
    play sound "fx/faucet1.ogg"
    queue sound "fx/faucet2.ogg"
    m "The noodles were ready now, so I took a pot lid and used it together with the pot to carefully pour all the hot water into the sink. Then I poured in some cold water stop the cooking process."
    m "Unfortunately, I didn't have a free cooktop so frying the noodles would have to wait. I poured some olive oil into the noodle pot to make sure the noodles wouldn't stick together."
    
    if naomi1drink == "cocktail":
    
        stop sound fadeout 1.0
        m "(There's enough time to make the cocktail in the meantime.)"
        play sound "fx/crapfridge.mp3"
        m "I took the liquor bottle from the fridge's door compartment and inspected what I had to work with. The liquid inside was clear and the bottle's sunny and cheerful-looking label read 'sugar cane liquor'"
        m "(I have an idea what this might compare to. Still, I should probably taste it first.)"
        play sound "fx/uncork.ogg"
        queue sound "fx/pouringwineshort.ogg"
        $ renpy.pause (1.0)
        queue sound "fx/coffee.wav"
        m "I poured some in a glass and drank it in one go."
        play sound "fx/glassdown.wav"
        m "(Yeah, tastes like blonde rum. To be safe, I'll make something that doesn't taste too different from what I had at Adine's.)"
        m "When looking for additional ingredients, I quickly figured out what cocktail to make as I spotted some lime-looking fruits. As another ingredient I needed simple syrup made with brown sugar, but making that yourself was extremely easy."
        m "(Melting brown sugar will take even less time than normal because I have hot water to speed up the process. Unfortunately, there's only two cooktops.)"
        m "(Well, I think taking the chicken off for a few moments won't hurt.)"
        play sound "fx/pouringwineshort.ogg"
        m "To dissolve the brown sugar, I measured two parts of it and one part of hot water and poured both onto a third pan. Then I took a potholder, put it on the kitchen counter and moved the hot chicken fillet pan on it." 
        play sound "fx/metalbox.ogg"
        m "Next, I quickly grabbed the simple syrup pan and put it on the heat. After not too much time aided by mixing, the simple syrup was ready."
        play sound "fx/pouringwineshort.ogg"
        queue sound "fx/metalbox.ogg"        
        m "I poured the syrup into a large heat-resistant glass. Then I turned the chicken in the pan and put it back on the cooktop."
        play sound "fx/crapcuttingboard.mp3"
        m "To follow up on the cocktail, I cut some of the fruit in half and juiced them. I drank a small amount and luckily, the taste was pretty close to that of lime juice."
        play sound "fx/cabinet.ogg"
        queue sound "fx/pouringwineshort.ogg"     
        m "Next, to chill the cocktail, I found a dragon-sized cocktail shaker in the next cabinet I opened. I poured roughly three portions of fresh dragon lime juice into it through a sieve."
        m "(Since Naomi seems to be skittish of alcohol, I should be careful with the alcohol content. Better to play it safe, as always.)"
        play sound "fx/cabinet.ogg"
        m "I inspected one of the same types of glasses I had served her juice in."
        m "(Naomi's like three to four times as big as I am, so two portions of alcohol in this at least over half a liter glass should only give her a slight buzz, even if she drank the cocktail in one go.)"
        queue sound "fx/pour.ogg"
        m "I measured two portions of liquor and six portions of simple syrup and poured them into the cocktail shaker."
        play sound "fx/crapfridge.mp3"
        m "Next I opened Naomi's freezer, took a bunch of ice and added some in."
        play sound "fx/stir.ogg"
        m "I shook the shaker for a short time and poured the cocktail into the large glass, again through a sieve. Finally, I added two straws and used a spoon to do a taste test."
        c "(That's a pretty sweet version, just the way I like it. You can barely taste the liquor, so I hope Naomi will like it as well.)"
        scene ecknaomiapt03 with dissolvemed
        show naomi normal with dissolve
        m "Naomi was intently focused on watching the series so she only noticed me after I had placed the cocktail on the table in front of her."
        play sound "fx/glassdown.wav"
        Nm confused "Oh, hey."
        c "Here's the cocktail you ordered."
        Nm normal "Thanks."
        queue sound "fx/coffee.wav"
        m "Naomi craned her head towards the glass and drank some of the cocktail through the straws."
        Nm smile "It's pretty good! Good job, my human servant."
        c "I'm happy to hear that you like it. If you'll excuse me, I have to go back to the kitchen. We can talk some more after I have brought the rest of the food."
        show naomi normal with dissolve
        play sound "fx/dishes.wav"
        m "Naomi had already resumed watching the series, so I just grabbed the empty appetizer plate from the table and went back into the kitchen to continue cooking."
        hide naomi with dissolve
        scene ecknaomiapt02 with dissolvemed

    else:
    
        m "(I have to wait a little bit for the chicken, so I should probably bring Naomi her juice now.)"
        play sound "fx/pour.ogg"
        m "I took another of the large glasses and poured some juice in it. This time I added two straws for ease of drinking."
        scene ecknaomiapt03 with dissolvemed
        show naomi normal with dissolve
        play sound "fx/glassdown.wav"
        c "Here's your juice, as ordered. I added two straws this time so you can drink it faster."
        Nm smile "Thank you, [player_name]."
        c "If you'll excuse me, I have to go back to the kitchen. We can talk more after I have brought the rest of the food."
        play sound "fx/dishes.wav"
        m "Naomi had resumed watching the series, so I just grabbed the empty appetizer plate from the table and went back to the kitchen to continue cooking."
        scene ecknaomiapt02 with dissolvemed       
        play sound "fx/pour.ogg"
        queue sound "fx/chug.wav"
        queue sound "fx/glassdown.wav"
        m "Feeling thirsty from the heat of the kitchen, I emptied the carton of juice into a glass and drank all of it. There was nothing to do for now, so I waited for the chicken to be ready."
        $ renpy.pause (4.0)
    
    $ renpy.pause (2.0)
    play sound "fx/beeps2.ogg"
    queue sound "fx/fry.ogg"
    m "After dropping off the appetizer plate at the sink, the timer signaled that the first batch of chicken breasts were ready. I moved them from the pan onto a serving plate, added in the unfried chicken and set the heat higher again."
    play sound "fx/beeps2.ogg"  
    m "After that was done, another timer beeped to tell me that the potatoes were ready."
    m "(Somehow, I have timed this almost to perfection.)"
    play sound "fx/metalbox.ogg" 
    m "To continue making the mashed potatoes, I lifted the boiling pot off the cooktop onto a potholder. Then, I added the noodle pan on the now free cooktop."    
    m "After that I took a lid and used it together with the potato pot to pour all the hot water into the sink. Then I grabbed a masher from one of the drawers and proceeded to mash the potatoes."
    play sound "fx/pour.ogg"
    m "After I had mashed for a time, I poured in some milk."
    m "(That should be enough for now. It's better to be careful to not use too much milk at first because you can always add more later. With too much the mashed potatoes will become a soggy, thick potato soup.)"
    play sound "fx/crapcuttingboard.mp3"
    m "Then, when I had mashed for a bit longer I opened one of the packages of butter on the counter, cut a lot of large chunks from it and added them into the pot."
    m "To complete the side, I then mashed a little bit more and finally mixed the entire thing with a scoop and left it in the pot ready for serving."
    play sound "fx/fry.ogg"
    queue sound "fx/salt.ogg"
    m "After that, it was time to turn the chicken. When that was done, I tasted the mashed potatoes, decided to add some salt and tasted it again. It was very buttery, with a slightly starchy texture and just the right amount of salt."
    m "(This turned out perfectly. Now on to the next thing.)"
    stop sound fadeout 1.0
    m "I added a lid to the pot of fresh mashed potatoes to preserve some heat and moved on to fry the noodles."
    m "(Oh well. I suppose olive oil will have to do, because I don't feel like searching for alternatives. It should be fine.)"    
    play soundloop "fx/fry.ogg"
    m "To start off, added in the cold noodles with my hands into the already hot enough frying pan and poured in some oil."
    play sound "fx/salt.ogg"
    m "Then finally after mixing the noodles a bit, I added in the cut vegetables, cheese and the spices and sauces I had selected earlier."
    $ renpy.pause (2.0)
    m "(That looks and smells pretty good already.)"
    $ renpy.pause (2.0)    
    m "(Actually, let's put in some giant prawns as well, because I love the crunch. Luckily for us, they're already prepared and seasoned.)"
    m "After adding the giant prawns I mixed the noodles again and put on the lid."
    stop soundloop fadeout 1.0
    m "(Now I'll just have to remember to mix every once in a while so the noodles cook somewhat evenly.)"
    $ renpy.pause (2.0)     
    m "(I don't feel like just waiting around. Could I make something simple but delicious in the mean time?)"
    $ renpy.pause (2.0)
    m "(How about a potato and bacon omelet? I could also use some other ingredients like these paprika-resembling vegetables for the texture and flavor.)"
    play sound "fx/metalbox.ogg"
    queue sound "fx/fry.ogg"
    m "I grabbed another pan and set it off to the side because both cooktops were occupied right now. Then I turned the chicken for the final time and lowered the heat, already anxious to be done with it."
    m "(I should probably get all the ingredients ready for the omelet while the chicken is frying.)"
    play sound "fx/sliceshort.ogg"
    queue sound "fx/crapcuttingboard.mp3"
    queue sound "fx/veggies.ogg"
    m "I took some bacon from a pack and sliced all of it into smaller pieces. Then I grabbed two dragon paprikas, cut all the extra bits off and sliced them as well."
    play sound "fx/egg.ogg"
    queue sound "fx/pour.ogg"
    queue sound "fx/stir.ogg"
    m "As the next order of business I made an omelet mix from a bunch of eggs and milk."
    play sound "fx/faucet1.ogg"
    queue sound "fx/rub1.ogg"
    queue sound "fx/veggies.ogg"
    queue sound "fx/fry.ogg"
    m "After that I took two large potatoes, rinsed them, peeled them and cut them into slices. Then I mixed the noodles again before figuring out what to do next."
    stop sound fadeout 1.0
    m "(I still got some time left before the chicken is ready, so how about a sauce? I think there's a good one I can make from what we have. It'll need a cooktop of course, but I can prepare the ingredients while one frees up.)"
    play sound "fx/pour.ogg"
    queue sound "fx/veggies.ogg"
    queue sound "fx/egg.ogg"
    m "As preparations for making the sauce, I mixed some white vinegar and water and peeled and cut two onions. Then I separated the yolk from a bunch of eggs and made a bain-marie from a metal bowl and the pot I had used previously."
    play sound "fx/faucet1.ogg"
    queue sound "fx/button_unpress.ogg"
    m "I needed more hot water for this contraption so I poured some more into the electronic teapot and turned it on."
    m "(There's still some time left on the chicken but I probably should take it off to not waste time. They should be ready anyway.)"
    play soundloop "fx/fry.ogg"
    m "I slid the rest of the chicken onto the serving plate, and spread the bacon and potatoes evenly in the same pan to fry for the omelet."   
    m "(Again, I have some time left. I should stop inventing new things to cook already, so I'll just start cleaning up what I can, in case we feel too tired to do it after eating.)"
    stop soundloop fadeout 1.0
    play sound "fx/rummage.wav"
    queue sound "fx/crapfridge.mp3"
    queue sound "fx/cabinet.ogg"
    queue sound "fx/faucet1.ogg"
    m "To clean up, I first put back everything I had taken but not used. Then I cleaned up all the trash and empty packaging into the garbage can. After that I placed all the dirty kitchen equipment into the sink and rinsed them."
    m "(Unfortunately, Naomi doesn't have a dishwasher. I'll have to wash the dishes more thoroughly later, because I really don't feel like washing them properly right now.)"
    play sound "fx/crapspraybottle.mp3"
    queue sound "fx/wipe.ogg"
    queue sound "fx/wipe.ogg"
    m "I finished my tidying-up operation by spraying some cleaning liquid on the kitchen counters and wiping them clean."
    play sound "fx/fry.ogg"
    m "Then I noticed that by now the bacon and potatoes were ready enough, so I added in the omelet mix, paprikas and some seasoning. Wanting to do a good job, I also mixed the noodles again."
    stop sound fadeout 1.0
    m "(The omelet might take a while, but we can just eat it for dessert because it's not going to burn on low heat.)"
    m "I started looking for some tableware for serving the food."
    play sound "fx/cabinet.ogg"
    m "(That large bowl looks perfect for the fried noodles. Also, Naomi has a saucière for convenient sauce-pouring. That's strange, since she said she doesn't cook herself.)"
    play sound "fx/dishes.wav"
    queue sound "fx/crapfridge.mp3"
    m "To prepare, I took the bowl, the saucière, some plates, utensils, glasses, napkins and another carton of juice and placed them in a neat order on the kitchen counter, ready for when I would carry everything into the living room."
    m "(Almost there. The noodles should be fried enough now.)"
    play sound "fx/fry.ogg"
    queue sound "fx/faucet1.ogg"
    queue sound "fx/wipe.ogg"
    queue sound "fx/metalbox.ogg"
    m "I used pasta tongs to lift the fried noodles from the pan into the bowl and stuck two dragon-sized forks in the noodles for me and Naomi. Then I quickly washed and wiped the pan and put it back on the cooktop."
    m "Now moving on to making the sauce, I poured my water-vinegar mix in the pan and also added the sliced onions."
    m "(Reducing the water, vinegar and onions into the flavor broth is going to take a minute. I guess I will have to wash the dishes after all. Oh well.)"
    play sound "fx/faucet1.ogg"
    queue sound "fx/dishes.wav"
    queue sound "fx/rub1.ogg"
    queue sound "fx/wipe.ogg"
    m "I begrudgingly washed all the dishes I had accumulated so far. Even worse, we would have to wash some more after eating."
    m "After I had finished, the flavor broth was ready because the ingredients in the pan had reduced to half their volume. I poured it into a heat-resistant glass through a sieve."
    m "Then I took my self-made bain-marie and put it on the cooktop. The water in it boiled only after a few moments, so I added the egg yolks into the bowl and whisked to break them up. The broken yolks started heating up almost immediately, so I slowly poured in the flavor broth and whisked even more furiously."
    $ renpy.pause (1.0)    
    m "I kept whisking rapidly until the sauce was even, and then started adding butter bit by bit. When that was done, I seasoned the sauce with tarragon, white pepper, sugar and salt. Finally, I had to let it sit for it to thicken, so I took a small break."
    m "(My arm is tired from the whisking. Worth it though, because I really like this sauce.)"
    $ renpy.pause (2.0) 
    m "After the short break, I emptied the sauce from the bowl into the saucière with the help of a scraper and placed it on the kitchen counter with the rest of the food that was ready to be eaten."
    m "(I can turn the omelet after I have carried all the food to Naomi. Other than that, looks like we're about done here.)"
    m "When I reflected on what I had made, I thought it was a really good meal, even if I said so myself. Eight breaded chicken fillets filled with herb butter, a pot full of mashed potatoes, a lot of fried noodles, a delicious sauce and a bacon potato omelet. I only hoped now that Naomi would like everything I had cooked." 
    m "Of course, there was a very small chance of me failing to please Naomi because I was a decent cook, but I still had a small lingering fear that made me dread even the slightest possibility of letting her down."
    m "(I should probably carry all this to the living room on my own. We don't want Naomi to trip and make a mess, do we?)"
    scene black with dissolvemed
    play sound "fx/dishes.wav"
    m "It took me three round trips in total to bring all the food and tableware into the living room, where we would eat together."
    scene ecknaomiapt03 with dissolvemed
    show naomi surprised with dissolve
    m "After I was done, I sat down next to Naomi, and I noticed that she had put the series on pause and was instead eyeing all the food I had brought with a curious and hungry look."
    $ renpy.pause (1.0)
    c "Please use the the fork at least for the fried noodles. Otherwise all the grease and sauces will be everywhere."
    Nm blank "If I make a mess you can just clean it up for me later, right?"
    c "I would like to avoid any unnecessary work. In fact, if you have any questions or need help plating I'll be happy to accommodate you in that front as well."
    show naomi normal with dissolve
    c "Also, use the scoop for the mashed potatoes. Even though we have swapped bodily fluids, I don't want your saliva in my food."
    Nm smile "Fine, fine. It's very cute how fussy you are being with me."
    c "I appreciate it. I'm just trying to teach you how to eat less messily."
    play sound "fx/dishes.wav"
    m "I set a plate with the required utensils in front of both me and Naomi, and adjusted the positions of all the food containers for ease of access."
    c "Without further ado, bon appétit!"
    Nm confused "What?"
    c "We can finally start eating."
    play sound "fx/pizzabite.ogg"
    show naomi normal with dissolve    
    m "Naomi dove straight in by tossing one of the breaded chicken fillets into her mouth, to eat it whole."
    show naomi smile with dissolve
    play sound "fx/eating.wav"
    m "I began by taking a huge chunk of the fried noodles with my fork and then stuffing some into my mouth."
    Nm "This chicken is so delicious! I especially like the crunchiness."
    c "Same. I love the taste and texture of batter, so I breaded it twice."
    Nm surprisedblush "Actually, even more than the crunchiness I love how the herb butter just bursts inside your mouth when you bite in."
    c "They are indeed a lot juicier than your basic chicken breasts. It must also be a different experience for you because you can eat it whole like that but I can't."
    Nm normal "You're already starting to sound like an expert on how to cook feasts for hungry dragons."
    c "Well, I am certainly planning to hone that skill even further."
    Nm smile "You have no idea how much I am looking forward to that, [player_name]."
    c "You and me both. By the way, I have to go turn the omelet that's still cooking in the kitchen."
    Nm surprised "You're making even more food?"
    c "I didn't want to sit around doing nothing so I used my time as efficiently as possible. I'll be back in a minute."
    scene black with dissolvemed
    hide naomi with dissolve
    play sound "fx/metalbox.ogg"
    m "I went back to the kitchen and used a large plate and a potholder to turn the omelet. It was a bit difficult because the equipment, especially the pan, was big, but I managed to do it without causing a mess."
    scene ecknaomiapt03 with dissolvemed
    show naomi normal with dissolve
    play sound "fx/eating.wav"
    m "After I came back, we both continued diving into our respective servings."
    $ renpy.pause (4.0)
    c "So, care to tell me how you have so much kitchen equipment, if you don't cook at home? A sauce boat like that for example, isn't very common to have around."
    stop sound fadeout 1.0
    Nm blank "My parents bought me most of the stuff. I told them about my skipping meals and overworking predicaments so they encouraged me to start cooking myself."
    Nm confused "To them, it seemed like a perfect way of catching two birds with a single venom spit: to have me do something other than just police work and make sure I eat more regularly." 
    Nm concern "After getting a bunch of of kitchen equipment, looking through some cookbooks and watching some cooking and traveling shows, I thought I was ready to learn how to cook."
    Nm sad "Needless to say, if you've paid any attention to what I've told you, you probably already guessed it didn't go well. I broke some of the equipment and made such a mess, that I had to pay the cleaning services to come and clean up my kitchen for me."
    c "I suppose it just wasn't your thing. You don't have to be great at everything, so don't worry about it."
    c "Always remember that you're already very good at a lot of things, for example analytics, swimming and flying. Besides, now you have me to cook for you."
    Nm smile "You're right. Thank you so much, [player_name]."
    play sound "fx/eating.wav"
    m "I only nodded, since my mouth was full of fried noodles, and Naomi resumed eating as well."
    show naomi normal with dissolve
    $ renpy.pause (4.0)
    m "After eating enough fried noodles I scooped some mashed potatoes onto my plate, placed a fried chicken fillet in the middle and poured some sauce on it. Then I cut the fillet through the middle, releasing the delicious herb butter into the mix."
    m "I proceeded by cutting the fillet into several smaller pieces. Then I spread some sauce, herb butter and mashed potatoes on a piece and ate it. It was superbly delicious, with buttery sauce and mashed potatoes, a very nice crunchy texture and juicy chicken."
    c "You should try the chicken with the sauce I made. Let me pour some for you."
    show naomi surprised with dissolve
    play sound "fx/chug.wav"
    m "I took the saucière and poured some of the thick, buttery and slightly bitter sauce on one of the breaded chicken fillets."
    stop sound fadeout 1.0
    c "There you go."
    m "After eyeing the chicken hungrily the entire time I had been pouring the sauce, Naomi picked it up with the tips of her claws and proceeded to toss it in her maw. Surprisingly, she didn't make a mess, even though the chicken fillet was coated in sauce."
    play sound "fx/pizzabite.ogg"
    Nm surprisedblush "Just wow. Why didn't I try this sooner?" 
    Nm smile "I'm starting to really love human cuisine. It's so familiar but yet a little bit different."
    c "The sauce also works well with mashed potatoes, so you should definitely add it there too."
    play sound "fx/chug.wav"
    m "Naomi happened to be running out, so I scooped some mashed potatoes on her plate and poured some of the sauce on top."
    c "Enjoy."
    Nm "Thank you, [player_name]."
    show naomi normal with dissolve
    m "This was a good time as any to take a break, so I decided to go get the potato and bacon omelet. It surely had been ready for some time now."
    hide naomi with dissolve
    scene black with dissolvemed
    play sound "fx/metalbox.ogg"
    m "I turned the heat off, slid the delicious omelet onto a serving tray and brought it back to the living room along with a cake knife."
    scene ecknaomiapt03 with dissolvemed
    show naomi surprised with dissolve
    c "We're having this for dessert."
    Nm shy "You've made so much food, [player_name]. I don't know what to say."
    Nm smile "Thank you so much for this wonderful evening."
    show naomi normal with dissolve
    m "I cut a quarter of the potato omelet with the cake knife and lifted it on Naomi's plate. Feeling a bit full already, I only cut one eight for myself."
    $ renpy.pause (2.0)
    m "The potato and bacon omelet exceeded my expectations: it was moist but at the same time crisp in some places where the potatoes or bacon had fried. On top of that the saltiness wasn't overpowering, and it was also slightly sweet due to the dragon paprikas I had added."
    Nm smile "This omelet is great too. I think I might be warming up to keeping you around a bit longer, [player_name]."
    c "Thanks, Naomi. I'm really happy to hear that."
    Nm shy "But seriously, how did you become such a master chef? I don't think I would ever be able to create a meal like this."
    c "Actually I would call myself pretty much an amateur, because the best food isn't usually overly complicated to make. In my opinion it's better to just focus on using good-quality ingredients and learning recipes for food that most people like to eat."
    $ renpy.pause (1.0)    
    Nm normal "I see. I guess none of these dishes are that complicated when I think about it in more detail."
    c "That's why I call my style of cooking simple but delicious. This philosophy leaves more time for eating."
    Nm smile "I love that idea. Eating is of course the most important part."
    c "Now when I think about it, there was also some luck involved in creating our delicious meal. You managed to buy decent ingredients, even though you're not that good at cooking."
    c "By the way, how did you like the fried noodles?"
    Nm normal "I hope I'm not boring you but I have to say that it was really good, like everything else you made. I especially liked the different textures it had. Too often people make boring versions of that dish."
    c "Yeah, those prepared giant prawns you bought were a really great pick. I honestly have to give you credit as well."
    m "I looked at Naomi's plate and she had some mashed potatoes with a breaded chicken fillet on top, but it was missing the sauce."
    c "Do you want some sauce?"
    Nm concern "Thank you. I don't think my claws are nimble enough to operate that sauce boat."
    play sound "fx/chug.wav"
    show naomi smile with dissolve    
    m "I poured some sauce for Naomi. Then, since apparently we had run out of interesting topics to talk about we continued eating silently until we were both completely full."
    m "I had to pace my eating to be a lot slower than Naomi's since she could eat a lot more than me. After we had finished eating our fill, there was still a good amount of food left over."    
    show naomi normal with dissolve
    c "What a meal, even if I say so myself."
    Nm smile "It was great. I hope you're not getting bored of me constantly complimenting you."
    c "I would never get bored of that. Just remember that there's always ways for you to pay me back."
    Nm shy "If you're hinting at what I think you are, do you realize that I have stuck a far better bargain than you, since I enjoy having you in bed as well?"
    c "Our feelings go both ways, because I enjoy cooking for you."
    Nm blank "Oh well. You got me there."
    Nm normal "By the way, looks like you cooked too much because we couldn't eat everything."
    c "That's fine, because you can take some of the food to the police station so you don't have to work while hungry. I'm sure a lunch break won't take too much time from your investigations if you don't have to go to a café to eat."
    Nm smile "Do you think that you cooking food for me to eat at work might become a regular occurrence?"
    c "Sure, if you decide to keep me around."
    $ renpy.pause (1.0)     
    c "I'll go put the leftovers in the fridge. Do you think you can wash the dishes later though? I really hate doing that because it makes my hands go dry."
    Nm normal "Sure, I can manage that."
    scene black with dissolvemed
    hide naomi with dissolve
    play sound "fx/crapfridge.mp3"
    m "In two round trips, I placed what was left over into Naomi's fridge so she could eat well tomorrow, and maybe even the day after that if she wasn't too much of a glutton."
    scene ecknaomiapt03 with dissolvemed
    show naomi normal with dissolve
    m "When I came back, Naomi was lying on the sofa, looking tired. I sat down next to her and patted her scaly back."
    $ persistent.sqbnaomi2cook = True
    
jump sqb_naomi_m2_ending
 
label sqb_naomi_m2_ending:
    
    c "Such a good meal calls for some down-time. Could I come rest next to you on the sofa?"
    Nm smile "I would love that a lot. I think you deserve a reward for all the hard work you did in the kitchen for me."
    $ renpy.pause (2.0)
    play sound "fx/sheet.wav"
    m "I lifted my legs on the sofa and laid down sideways next to Naomi. When I had settled properly in place, she tied her arm around me."
    Nm shy "You are so cute, [player_name]."
    c "Mmh... Naomi..."
    $ renpy.pause (2.0)
    m "I had eaten way too much, so I started quickly falling asleep. Unfortunately, Naomi interrupted me with a question."
    Nm normal "I almost forgot to ask. How did our foodstuffs compare to human ones?"
    c "Well..."
    c "How should I put this...{w} it's really weird that everything is almost exactly the same even down to labeling, with small differences."
    show naomi confused with dissolve
    c "Some things taste a little different though. If I was being conspiratorial I would say that you were trying to imitate our food products to the best of your abilities with what's available to you."
    Nm concern "That's a very strange theory. How would it even be possible for us to imitate you without any prior contact?"
    c "Well if I had to guess, the human that allegedly visited your world a long time ago had a bigger impact on your development than you think."
    Nm normal "Oh yes, that thing from the history class. I had completely forgotten about it."
    c "Also, similar sentient species usually developing along the same lines probably has something to do with it. I never believed that to be true but it at least seems like a plausible theory after all."
    Nm shy "Now that's a point I agree with. I also would like to add that our species are actually very similar since we're able to have a romantic relationship with each other."
    c "That's true, but don't forget about our differences. I think we will make a great partners due to them. All in all, interacting with other sentient species is a very exciting time."
    Nm normal "Likewise." 
    c "Anyway, I think I ate way too much. Do you mind if I take a short nap for about half an hour?"
    Nm smile "Not at all. I will keep you safe."
    play sound "fx/bed.ogg"
    stop music fadeout 1.0
    hide naomi with dissolve
    scene black with dissolvemed
    m "Naomi lowered her wing over me. After closing my eyes, I quickly fell asleep with her as my warm backrest and blanket."
    $ renpy.pause (1.0)
    m "I felt satisfied and at peace with Naomi at my side. This had been a very good day."
    scene ecknaomiapt03 with dissolvemed
    play sound "fx/lewd/lickslow.ogg"
    m "Just as I had closed my eyes, I woke up to someone nudging the side of my head with their snout and gently kissing my cheek."
    play music "mx/airborne.mp3" #Different music?
    show naomi smile with dissolve
    Nm "It's been half an hour. Time to wake up."
    play sound "fx/sheet.wav"
    show naomi normal with dissolve
    m "After I had gotten up from the sofa, I noticed it was already very late. I had stayed for much longer than I had initially planned to."   
    Nm normal "It's getting very late, so maybe you should get going. Even though my vacation is coming up, I don't want to stay up for too long."
    Nm smile "Unless you want to sleep together with me?"
    c "I can't, sorry. There's some material I have to go over at my apartment tomorrow morning. I have a feeling if I stay the night I won't have any time for that."
    c "Let's just call it a day. We can continue some other time."
    Nm normal "That works for me. We got lots of time to be together, right?"
    $ renpy.pause (1.0)
    Nm concern "Oh, I knew I had forgotten something. I was initially going to buy some supplies after escorting you home, but all the shops have already closed."
    c "That's very unfortunate. You can always do that tomorrow though."
    Nm blank "Yeah, it's not a big deal. I'll escort you home regardless."
    Nm normal "I have to say that we had an excellent time. I'm not very used to having people come over, but this evening was a resounding success."
    Nm smile "Thank you so much for your company, [player_name]."
    c "I had a great time as well. Actually, didn't you just say you had a vacation coming up, so do you want to meet again then? We can have the entire day to spend with each other."
    Nm "How considerate of you to suggest that. Actually, I might have just the idea on how to make our time together more interesting. I can't tell you right now what it is though, because it's a secret."
    c "I'm intrigued."
    Nm normal "Let's get going already, because I'm starting to get pretty tired."
    hide naomi with dissolve
    scene sqbnaomiapt04 with dissolvemed
    $ renpy.pause (0.5)
    m "We walked up to the main door and stopped for a moment while Naomi was fiddling with the lock."
    show naomi blank with dissolve
    Nm "I still can't get used to the cursed thing."       
    play sound "fx/door/lock.ogg"
    $ renpy.pause (0.5)
    play sound "fx/door/handle.wav"
    $ renpy.pause (1.5)
    show naomi surprised with dissolve
    m "Upon opening the door, however, we were greeted by Sebastian idly sitting on a bench and leaning back with his eyes shut."
    Nm normal "Seb? What are you doing here? I thought I was the one responsible for [player_name] for today."
    show naomi normal at right with ease
    show sebastian normal b flip at left with easeinleft
    Sb smile b flip "You can't be responsible for any assignment after your shift is over, Naomi."
    Nm shy "Oh, right."
    Nm normal "Why didn't you let me know that you're here? There's enough room for all of us."
    Sb "I'm still on the clock, so I decided to patrol the area. I only sat down here to take a breather while guarding your outer door."
    Nm blank "How nice of you. Still, you should have at least let us know you were around."
    Nm normal "I was just about to escort [player_name] back to their apartment. Care to join us?"
    show naomi blank with dissolve
    Sb disapproval b flip "Naomi, your shift is over, so go get some rest. I'll escort [player_name] instead since I'm still on duty."
    c "Sure. Thanks, Sebastian."
    Nm smile "I suppose this is it for today, then. I'm so looking forward to your next visit, [player_name]."
    c "Me too. Bye, Naomi."
    show naomi surprisedblush with dissolve
    m "As I was starting to leave, I noticed Naomi looking first at me and then at Sebastian. She was clearly up to something, so I decided to not go yet."
    $ renpy.pause (1.0)
    show sebastian shy b flip with dissolve
    show naomi smile with dissolve
    play sound "fx/kiss.wav"
    queue sound "fx/lewd/lickslow.ogg"
    m "Then, after a moment's hesitation, Naomi embraced and tongue kissed me like back when we had been together. After she was done with me, she winked at Sebastian."
    m "(Looks like she's starting to be less shy about openly showing she likes me.)"
    Nm smile "Don't keep me waiting, [player_name]!"
    c "I promise I won't. See you later, Naomi."
    $ renpy.pause (0.5)
    stop music fadeout 2.0
    play sound "fx/door/door_close.ogg"
    queue sound "fx/steps/slowstepsdown.ogg"
    hide naomi with dissolve
    hide sebastian with dissolve
    scene black with dissolveslow
    m "We exited outside through the dark hallway with Sebastian. At first, he didn't comment at all on Naomi's sudden show of affection towards me."
    stop sound fadeout 2.0
    scene eckdarkpathway with dissolveslow
    play soundloop "fx/steps/steps.ogg"
    $ renpy.pause (0.5)
    show sebastian smile b with dissolve
    m "After we had walked for a while, he finally decided to bring it up."
    Sb smile b "So, you two did it?"
    c "Yes, we had a great time together."
    Sb "I'm so happy for Naomi, and for you too of course. She deserves a good boyfriend who will do right by her."
    c "Thanks, Sebastian. I really appreciate it."
    
    if modinfo.has_mod("BangOk") and bangok_four_xsebastian_unplayed == False:
        Sb shy b "You know...{w} umm..."
        Sb "Since we've already had sex, is there any chance I could join you and Naomi? You know what they say: the more the merrier."
        c "I wouldn't mind that, so it's entirely up to her. She did call you cute and she also said she likes smaller partners, so there's a chance she might agree to it."
        Sb smile b "That's wonderful news."
        Sb drop b "I'll ask her when I've mustered up the courage."
        c "Cool."
        
    hide sebastian with dissolve
    scene np5e with dissolveslow
    show sebastian normal b with dissolve
    stop soundloop fadeout 2.0
    m "After walking for some time, we had finally made it to my apartment. Not too soon, since I was dead tired at this point."
    c "Thanks for escorting me to back my apartment, Sebastian. You're as dutiful as ever."
    Sb smile b "Alright. See you, [player_name]."
    hide sebastian with dissolve
    play sound "fx/door/handle.wav"
    queue sound "fx/door/door_close.ogg"
    scene o3 with dissolveslow
    $ renpy.pause (2.0)
    scene black with dissolveslow
    m "I dropped on my bed with my clothes still on, and fell asleep almost immediately. This, without a doubt, had been the best day of my entire life."
    $ renpy.pause (2.0)
    m "When I woke up in the morning, I couldn't remember the last time I had slept this well."    
    $ renpy.pause (0.5)
    $ persistent.naomi2skip = True
    $ naomiscenesfinished = 2
    
jump ml_date_end  