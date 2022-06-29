label sqb_naomi_m2_sexskip:
    
    stop music fadeout 1.0
    play sound "fx/system3.wav"
    
    s "Would you like to skip to the cooking, or straight to the ending? If you have NSFW mode enabled, you can also choose to skip to the sex."
        
    menu:
        "Sex" if persistent.nsfwtoggle == True:
            jump sqb_naomi_m2_sexskip2
            
        "Cooking":
            scene black with dissolvemed
            $ renpy.pause (1.0)
            $ naomi2mood = 10
            $ naomiromance += 100
            $ naomilewd = 4
            scene eckannabedroom4 with dissolvemed
            play music "mx/airborne.mp3"
            show naomi normal with dissolve
            jump sqb_naomi_m2_cooking
        
        "Ending":
            s "Alright."
            scene black with dissolvemed
            $ renpy.pause (1.0)
            $ naomi2mood = 10
            $ naomiromance += 100
            $ naomilewd = 4
            scene ecknaomiapt03 with dissolvemed
            play music "mx/airborne.mp3"
            show naomi normal with dissolve
            jump sqb_naomi_m2_ending
            
label sqb_naomi_m2_sexskip2:

    s "Alright."
    scene black with dissolvemed
    $ renpy.pause (1.0)
    $ naomi2mood = 10
    $ naomiromance += 100
    $ naomilewd = 4
    scene eckannabedroom4 with dissolvemed
    play music "mx/treetops.mp3"
    show naomi smile with dissolve

jump sqb_naomi_m2_sexskip2_end

label sqb_naomi_m2_sfwskip: 

jump sqb_naomi_m2_sfwskip_end
            
label sqb_naomi_m2_foodskip:
    
    stop music fadeout 1.0
    play sound "fx/system3.wav"
    
    if persistent.sqbnaomi2cook == True:
        s "Would you like to skip the cooking and eating?"
    else:
        s "A lot of reading ahead. Would you like to skip the cooking and eating?"
        
    menu:
        "Yes":
            s "Alright."
            scene black with dissolvemed
            $ renpy.pause (1.0)
            scene eckannabedroom4 with dissolvemed
            play music "mx/treetops.mp3"
            show naomi shy with dissolve
            jump sqb_naomi_m2_ending
        
        "No":
            s "Alright."
            play music "mx/airborne.mp3"
            jump sqb_naomi_m2_cooking

jump sqb_naomi_m2_foodskip_end

label sqb_naomi_m2_chairs:

    $ renpy.pause (0.5)
    $ naomi2mood += 2
    $ naomilewd +=1
     
    Nm surprised "You mean right now?"
    c "Sure, if they bother you that much. I'd love to help you out."
    c "I think I am better suited for moving furniture around than you are, no offense."
    Nm normal "None taken. Also, thank you for the offer but I want to host you, not put you to work."
    Nm blank "I'll do it myself tomorrow."
    Nm "Enough about my chairs. Let's go rest on the sofa."
    scene ecknaomiapt03 with dissolvemed
    m "She led me to a white sofa in front of the large TV. I took my seat by the armrest on the left, while Naomi settled on her belly on the cushions nearby and shifted her wings slightly."
    show naomi normal with dissolve

jump sqb_naomi_m2_chairs_end

label sqb_naomi_m2_differences:

    c "For example, have you ever considered how big you are compared to a human? If you hugged someone like me, you'd make them feel better in no time."
    show naomi surprisedblush with dissolve
    m "(Why did I say that?)"
    Nm shy "That's a very...{w} interesting point."
    Nm smile "I bet if I caught a puny human like you, they'd never be able to escape my clutches."
    c "Actually, that's what dragons sometimes do to humans in our fiction."
    show naomi confused with dissolve
    c "Although, usually the dragons who deal with humans are assumed to be male and very powerful, and most of the time they only catch humans of the female sex."
    Nm concern "That trope makes no sense at all to me. Female dragons are just as strong as male dragons." 
    Nm blank "I'd be very interested in hearing more about dragons in your fiction, especially why they're usually assumed to be male."
    c "Well, I didn't really study literature at all or specialize in cultural history so I don't know enough about it to make it interesting. Let me think of something..."
    m "Then, I had a sudden urge to say something funny."
    c "Now that I think about it, I agree with you that our dragon trope makes no sense. I'm sure there are a lot of male humans who wouldn't mind being caught by a female dragon."
    Nm confused "I hope you know that I was just being hypothetical."
    c "Yes, of course."
    show naomi blank with dissolve
    c "Anyway, as a sociologist the most fascinating thing to speculate about regarding our species' future relationship is how we could complement each other."
    c "It's going to be kind of a similar adaptation to how your different species of dragons have specialized to be the best at their particular tasks."
    c "Compare humans to runners for example. I know that runners are decent at doing tasks that require precision, but humans are way better. Our limbs and especially nimble and long fingers are much better suited for articulate tasks than anything you've ever seen before."
    show naomi normal with dissolve
    c "Like I implied before, I wouldn't mind moving a few things for you, because it's much easier for me."
    show naomi surprised with dissolve
    c "Then as a sign of reciprocity you could fly me across town or something, if you are comfortable doing that."
    show naomi shy with dissolve
    c "By the way, how long does flying across the town even take you?"

jump sqb_naomi_m2_differences_end

label sqb_naomi_m2_balcony:

    c "Coming on the balcony was a great idea. I really love feeling the sea air again." 
    c "It's been a long time since I've been able to visit a seaside beach because our city-state is in middle of a desert. Wandering outside the walls is very dangerous so we don't do any recreational trips."
    Nm confused "That's very unfortunate. Why would anyone want to live in the middle of a desert?"
    c "Where we live is not really our choice. In order to have a chance at survival, we had to settle within a reasonable distance in a place where at least some of the infrastructure was intact."
    c "Anyway, standing in a peaceful place like this makes me both nostalgic and sad at the same time. I can't help but to think of all the hardship that has been placed upon us."
    show naomi sad with dissolve
    c "Living in my world is like a nightmare that never ends."
    Nm "I'm so sorry to hear that, [player_name]." 
    show naomi shy with dissolve
    m "Naomi seemed to be thinking about something."
    Nm "Just a funny thought..." 
    Nm "I wouldn't mind if you stayed here with me. You're... um... good company."
    Nm smile "You should also invite your friends. Like I said before, I would love to meet more humans. There's plenty of room for everyone."
    m "Naomi caught me off-guard again. I felt a sudden surge of emotions."
    m "Without warning, a tear slid down my cheek and I had to sniff."
    show naomi concern with dissolve
    m "Naomi noticed it, and looked at me worriedly."
    c "Thank you, Naomi."
    show naomi smile with dissolve
    c "I would love to take you up on your offer, if it ever becomes possible."
    Nm "I'm glad to hear that."
    c "To change the topic to something less gruesome, I have to say that in addition to the fresh sea air I really like the view as well."

jump sqb_naomi_m2_balcony_end

label sqb_naomi_m2_movie:

    c "I couldn't agree more."
    c "Anyway, hearing the story of how through an unlikely series of events you became a police analyst was interesting. It's actually similar in some ways to how I ended up becoming an ambassador to your world."
    Nm shy "Oh, really?"
    Nm blank "I sense another story coming up."
    m "(Should I tell her about my past?)"
    menu:
        "Tell her":
            c "My story isn't a happy one. I hope you don't mind."
            $ naomilewd +=1
            $ naomi2mood += 4
            show naomi concern with dissolve
            m "Naomi sighed and looked at me with concern."
            
        "Don't ruin the mood.":
            $ sqbpremounlocked = False
            c "I'm sorry to disappoint you, but I don't want to ruin the mood. The story of how I ended up here is not a happy one."
            Nm sad "Oh well. I'm sorry if that question was too personal."
            Nm normal "Speaking of moods, would you like to shift your focus from the harsh realities of life by watching a fine movie with me? I've got quite a collection."
            c "Sure, what kind of movie do you have in mind?"
            Nm smile "You said you like [ecknaomim2movie] films if I'm not mistaken."
            c "Yeah."
            Nm "I think I know a good one. Let me set everything up."
            hide naomi with dissolve
            play sound "fx/sheet.wav"
            $ renpy.pause (0.5)
            m "Naomi slipped off the cushions in a single fluid move – not unlike a huge cat – and walked up to the device located below the large wall-mounted TV. She fiddled with it for a time and then made a quick trip to the fridge, before returning with two portions of snacks and drinks."
            if naomi2mood > 5:
                m "The dragoness placed them on the glass table nearby and hopped onto the couch, settling next to me."
            else:
                m "The dragoness placed them on the glass table nearby and hopped back onto her previous spot on the couch."
            $ renpy.pause (1.5)
            show naomi smile with dissolve
            Nm "Now, we are all set."
            m "She picked up a sizeable remote and pushed a couple of buttons on it. A second later, the screen lit up."
            stop music fadeout 2.0
            $ renpy.pause (2.5)
            scene black with dissolvemed
            $ renpy.pause (2.5)
            scene ecknaomiapt03 with dissolvemed
            play music "mx/airborne.mp3"
            
            jump sqb_naomi_m2_movie_end
    
    Nm blank "Don't worry, I can take it."
    c "Where to begin..."
    show naomi normal with dissolve
    c "Like I might have alluded to earlier, my world used to be pretty prosperous. Our quality of life and general happiness was dramatically higher than ever before due to technological advances."
    c "Well, I suppose social advances such as decreasing inequality and getting rid of most of human exploitation played a huge part too."
    c "Also, we used our technology to automate most tedious and difficult jobs in order to have more time to do what we actually wanted to do with our lives, like anything related to hobbies or simply just improving ourselves as people."
    show naomi surprised with dissolve    
    c "Our technology was far superior to yours. For example, we had computers everywhere, even on our wrists."
    Nm blank "That sounds like a very inconvenient invention to me. I wouldn't even know how to begin to use a computer on my wrist."
    c "You're in luck, because those are pretty rare nowadays due to the solar flare and high-tech manufacturing being practically impossible."
    c "Anyway, the future seemed pretty bright for all of humanity, but especially for me as well."
    show naomi normal with dissolve
    c "I had gotten myself majors from both biology and sociology. Skills from those fields were in demand at the time due to rapid social advances."
    c "Unfortunately, shortly after my graduation the flare hit our world and my degrees became pretty much worthless in the ensuing aftermath."
    show naomi concern with dissolve
    c "A whole different set of skills would have been far more useful to help me in what I had to go through. Yet somehow, mostly due to sheer luck, I managed to survive."
    show naomi sad with dissolve
    c "I really don't want to get into the uncomfortable details. It suffices to say, if you've ever seen a post-apocalyptic movie, it was like that but worse."
    Nm blank "I've never heard of that genre, although based on the name I can guess what it's probably about. It sounds amazingly interesting to me."
    c "In post-apocalyptic movies...{w} never mind."
    Nm confused "Huh?"
    c "It's not that interesting to explain. Let me continue my story."
    show naomi normal with dissolve
    c "So, somehow I managed to survive and find my way to the city-state, Bastion, where I currently reside in."
    c "Things are quite bad there compared to your world but like I said, the world outside our city walls is basically a hellscape."
    show naomi sad with dissolve
    c "Anyway, before I became ambassador I was just doing odd jobs to survive."
    c "I... uhh...{w} suppose it wasn't all that bad if you look at the big picture."
    c "To fast forward, we found the portal on a scouting mission and sent Reza to investigate your world after the initial contact."
    show naomi blank with dissolve
    c "In his case, there wasn't really any kind of process to select the most suitable person to go since we were desperate for any kind of help or even information. I have to admit that we didn't really care if he had died on the mission."
    c "This was because Reza was known to be a troublemaker, so him dying really wouldn't have been big loss. You wonderful dragons could have been savage, man-eating monsters for all we knew at the time."
    Nm smile "You've seen nothing yet. Just stick around for long enough and I might show you all of my abilities."
    m "Naomi's remark almost made me jump up from the sofa. I managed to mostly control myself but I'm sure she noticed me twitch and shift my position."
    c "I... uhh..."
    m "She winked at me and licked her figurative lips."
    c "Where was I..."
    show naomi normal with dissolve
    c "Anyway, I was selected from a large pool of applicants to be the second person to visit your world. Due to my expertise in both biology and sociology I was uniquely qualified."
    c "Sending someone takes a lot of power so it'll just be me and Reza interacting with you until we get one of the generators."
    c "Reza's behavior leaves a lot to be desired."
    show naomi concern with dissolve    
    c "Well... that would be the understatement of the century, if he is indeed guilty. Murdering someone is unforgivable even in our harsh society."
    c "I hope we catch him soon and find out the truth so we can end this mess."
    Nm smile "I hope so too. We need to get this murder mystery over with because I want to meet many more cute humans and tell them they're welcome with open arms."
    m "(She really seems to like my species a lot.)"
    c "Naomi, you and the other dragons I've met have been much nicer to me than I could have ever anticipated."
    c "I really don't know what to say. You caring about me and my people this much makes me feel very happy."
    m "Suddenly I started to feel another surge of emotions. My throat started feeling dry and I wanted to cry."
    show naomi surprisedblush with dissolve
    c "Your unconditional kindness towards us is somewhat unexpected, because I don't know what we did to deserve it. Being as dependent on technology as we were wasn't good, so the mess we're in is kind of our own making."
    #A check if Naomi likes PC enough
    Nm stern "Don't say that. Everyone needs help sometimes."
    Nm confused "Just make sure you have good friends..." 
    Nm smile "...or something more to help you out."
    play sound "fx/sheet.wav"
    m "Naomi moved a bit closer towards me on the sofa."
    c "Thank you again, Naomi. I really mean it."
    play sound "fx/bed.ogg"
    m "With my accidental encouragement, she shifted yet a little bit closer towards me. From up close I finally fully realized how much bigger than me she was, so I started feeling a little intimidated but also intrigued by her different physique."
    Nm shy "Would you like a hug? I don't want to see a cute little human like you sad like this ever again."
    #A choice to turn her down, PC refuses politely
    m "I already liked her a lot and turning down her offer of comfort would have been rude."
    c "I-I really need a hug right now..."
    stop music fadeout 1.0
    show naomi slsmile with dissolve
    play sound "fx/sheet.wav"
    m "With that, Naomi leaned against me and I returned the show of affection by wrapping my arms around her upper body."
    m "Naomi was softer and cuddlier than I had expected from a dragon. After I had been feeling her for a moment, she secured me in place by hugging me with her arms behind my back."  
    m "Since this was our first time, I was surprised when I felt her strong breathing."
    m "(I suppose an aquatic dragon needs strong lungs to be able to stay underwater for extended periods of time.)"
    Nm smile "Are you feeling any better yet?"
    c "Yes, thank you very much." 
    c "Hugging a big dragoness such as you is certainly a new experience for me. I don't know what to say."
    play sound "fx/sheet.wav"
    m "After the hug, I tried to politely disentangle myself from Naomi, but she wouldn't let me go."
    Nm confused "What's wrong?" 
    Nm slsmile "Let's stay like this so you won't feel sad while you finish your story."
    c "Sure, that works for me. Anyway, to continue..."
    show naomi normal with dissolve    
    c "Like you already know, our most important goal is to get one of your generators. A lot of tech, especially advanced medical equipment was spared in our city. The problem is that soon we won't have enough power to run it properly."
    c "I just hope my city-state is still standing when it's time for me to return."
    show naomi blank with dissolve  
    m "As I said that I was hit by the sudden realization that I might not be able to come back here after I had completed my mission. After all, given the precarious situation we were in, who would care about researching dragon society and culture?"
    play music "mx/flashback.ogg" 
    m "Because of this realization, it was the first time when thinking about having to return made my stomach feel like an endless pit of suffering. An immediate surge of panic was starting up in me, so I had no choice but to confide in Naomi to ease it off even a little bit."
    Nm concern "Something wrong?"
    c "Yes, you could say that. I hate to admit that I am not looking forward to the day when I finally have to go back to my own world."
    c "How should I sum this up...{w} sticking together and working for the greater good has kept my people alive so far."
    show naomi confused with dissolve
    c "Because of the contradiction between this and my own preferences, I suddenly feel completely helpless and too powerless to make myself happy." 
    c "To be sincere, I actually don't want to leave at all because your world is too wonderful."
    show naomi slsmile with dissolve
    play sound "fx/rub2.ogg"
    m "Naomi started carefully rubbing the side of my head with her snout."
    Nm normal "If things are really that bad in your world, you should definitely stay here with me."
    Nm smile "I'm sure they won't miss one human, or other potential like-minded folks who want to live with us instead."
    c "B-but...{w} I have to go back."
    show naomi stern with dissolve    
    c "My superiors might assume you're holding me hostage, and that would ruin everything we've been working towards."
    Nm "Don't be silly. Once you have our generators, they can come here themselves to see that you're okay."
    Nm blank "After all, if what you say is true about your world, why would anyone need to be held hostage in order to make them stay here?"
    m "A conflict inside me was figuratively ripping me apart. I knew duty to my people was important, but a growing part of me wanted to just lead a quiet and simple life."
    m "It probably took her a lot of courage to ask me yet again, considering her usually shy and reserved demeanor. I also didn't want to disappoint Naomi by declining her so I made the final decision to accept what she had suggested twice already." 
    Nm confused "Well?"
    stop music fadeout 1.0
    c "I suppose you are right. I'll still have to make a formal request though, but I don't see why it would be declined if I explained myself well enough."
    show naomi smile with dissolve
    c "Thank you again, Naomi. It seems that your advice has been really useful and thoughtful for me."
    Nm "So, it's settled then. You'll stay here with me and so I can keep you safe forever."
    play sound "fx/bed.ogg"
    m "Before I could think of a witty comeback to get back at her, she shifted me around and slowly started using her body strength to push me down on the sofa. I kind of liked how she handled me so I didn't protest."
    show naomi surprisedblush with dissolve
    play sound "fx/sheet.wav"
    m "Then, while she was pushing me down, she gently turned me to position my back against her chest and then she shifted us both to put her between me and the sofa's backrest."
    show naomi aroused with dissolve 
    play sound "fx/craphug.mp3"    
    m "Then she locked her arms under my armpits to tie me in a tight embrace. At this point, I couldn't have escaped even if I had wanted to try."
    show naomi shy with dissolve
    m "Finally, she placed her right wing over me as some kind of an impromptu dragon-blanket."
    play music "mx/enigma.mp3"
    Nm smile "If you ever try to go back to your horrible world I will capture you before you make it to the portal and hug you until you change your mind."
    m "(Oh well, looks like she already solved my problem for me. Sadly, I won't ever be able to go back to that post-apocalyptic hellhole.)"
    Nm stern "I'll also protect you if they try to take you back by force. I'm a lot of dragon with a few tricks they won't be expecting."
    Nm normal "You will be safe here with me for the rest of your life."
    show naomi smile with dissolve
    m "My mental resistance was waning rapidly in front of Naomi's advances. I was in no mood to refuse anything from her."
    c "T-thanks..."
    Nm smile "When your ambassador duties are over, your new job will be to act as my body pillow whenever I feel like getting a few cuddles."
    c "(Just what have I gotten myself into?)"
    show naomi slsmile with dissolve
    play sound "fx/sheet.wav"
    c "We lied on the sofa for what seemed like forever. Occasionally Naomi shifted and rubbed my body in various ways, as if she was trying to find out where I was the squishiest."
    c "Based on the number of rubs, my lower belly seemed to interest her the most."
    c "Even though I was slowly getting more and more aroused and a little intimidated as her live body pillow, I still felt a peace I hadn't felt in a very long time."
    $ renpy.pause (3.0)
    Nm "You are a very cute and cuddly partner."
    Nm shy "Would you like to watch a movie in this position?"
    c "I think this position is perfect for watching one."
    Nm smile "Likewise. You're the perfect-sized body pillow to for me to cuddle with while enjoying a good story."
    Nm "Just so you know, I actually have one in my bedroom closet..."
    Nm shy "...but now I think I prefer one that's alive."
    m "Again, my throat started feeling unnaturally dry."
    show naomi slsmile with dissolve
    play sound "fx/rub2.ogg"
    m "Naomi started shyly rubbing my upper chest with her hands."
    c "..."
    play sound "fx/bed.ogg"
    m "She moved me a bit so my head was firmly lodged below her chin and then she tightened her grip on me even more to properly lock me in place."
    c "I suppose this means I passed the product testing stage?"
    Nm smile "With flying colors."
    Nm normal "So, you said you like [ecknaomim2movie] films if I'm not mistaken?"
    c "Yeah."
    Nm "You're in luck because I just happen to have a good movie of that genre in the player. I don't want to get off the sofa so let's just watch that one."
    c "Don't you think we should get some snacks or at least something to drink though?"
    Nm smile "Are you trying to escape? Sorry, now that I finally caught myself a human I'm not letting them escape."
    Nm normal "We'll be fine. Also, drinking and snacking might distract us from the more important activities."
    Nm smile "You know what I mean?"
    c "Alright, you win. It's not like I can resist your charms anyway."
    Nm "Good choice. Any escape attempts would have been weak and pathetic anyway."
    play sound "fx/bed.ogg"
    Nm normal "You'd better get comfortable. I'll only let you go after the movie is over."
    m "(This is going to be great.)"
    show naomi smile with dissolve
    m "With those words, Naomi extended her arm and picked up the sizeable remote from the table in front of us."
    m "She pressed a couple of buttons on it, and after a few moments of fiddling with the remote the movie started playing."
    
    stop music fadeout 2.0
    $ renpy.pause (2.5)
    scene black with dissolvemed
    
    m "I focused more on Naomi's large body, breathing and warmth than watching the movie. I felt a strange mix of arousal, terror and submissiveness throughout the entire session."
    m "Thankfully because my back was against her belly she didn't find out about the hard erection I had most of the time the movie was playing." 
    m "It was for the better, because I had no idea how she would have reacted."
    m "The tease was almost unbearable, but I managed to keep any dirty thoughts to myself."
    
    $ renpy.pause (2.5)
    scene ecknaomiapt03 with dissolvemed
    play music "mx/airborne.mp3"

jump sqb_naomi_m2_movie_end

label sqb_naomi_m2_bedroomfun:

    $ naomi2mood += 4
    $ naomiromance += 100
     
    Nm concern "Umm..."
    c "Come on, I like you as well."
    c "Or are you trying to say that the type of cuddling we just did is normally done among friends here?"
    show naomi shy with dissolve
    m "Seems I caught Naomi off-guard. She nervously looked me in the eyes, but then tried avoiding my gaze when I looked back."
    Nm "I... umm..."
    show naomi aroused with dissolve
    m "After a moment of hesitation, she finally looked me in the eyes. Then she stopped for a moment and sighed loudly."
    Nm smile "I suppose I should finally openly admit that I like you as well."
    Nm surprisedblush "I've been thinking about dating you ever since we met. Are you happy now?"
    c "You're-{nw}"
    m "She cut me off before I could say anything."
    Nm confused "You've been persistent in trying to get me to admit I like you. Why else would you obey my every whim?"
    Nm normal "The weird thing about us is that even though we met very recently I feel like we've known each other for a long time." 
    Nm "In addition to that we complement each other nicely. Furthermore, you understand me really well and like me for who I am."
    c "What's not to like in a cute dragon such as yourself?"
    Nm shy "Oh, stop it. You're much cuter than I am."
    Nm smile "Did you know that I've always wanted a partner smaller than myself? That's because I want to be able to easily put them in their place if they misbehave."
    Nm surprisedblush "I..."
    Nm shy "I didn't mean it like that."
    Nm "Well, I did but...{w} not that directly."
    Nm sad "I hope I didn't make you feel uncomfortable in any way."
    c "(This just gets weirder and weirder.)"
    Nm shy "I just hope the feeling's mutual."
    c "You should consider our session on the sofa a sign of my approval."
    c "I really don't mind if you tease me by objectifying me a little bit. Somehow I feel like I can trust you to have my best interests in mind."
    c "I really like you Naomi."
    play sound "fx/kiss.wav"
    show naomi aroused with dissolve
    m "With that, she suddenly kissed me on my right cheek."
    play sound "fx/lewd/lickslow.ogg"
    m "As she was pulling back from the kiss, she licked me with her long tongue, leaving some saliva behind."
    Nm smile "I really like you too."
    Nm "You're the best body pillow I've ever had. We're going to have a great time together."
    c "Yes...{w} uhh... {w}that sounds wonderful."
    c "Dragon hugs are certainly something I've never experienced before."
    Nm normal "I'm so happy you like me even though we're not of the same species."
    Nm smile "I hope you understand that from my perspective, you humans are the cutest."
    m "(Yes, I think I might have gotten that impression.)"    
    Nm "I've never had such a cute and squishy boyfriend before."
    c "You're going to make me blush."
    show naomi shy with dissolve
    m "Naomi looked off to the side and then back at me. She seemed to be thinking about something."
    Nm confused "I just realized there is something that would improve our cuddling experience by a lot."
    Nm normal "I honestly don't understand why you humans cover up your bodies so much."
    Nm blank "Why don't you take your covers off? Having fabric between you and your partner gets in the way of having a properly intimate cuddling experience."
    m "(This escalated faster than I ever could have anticipated. What should I do?)"
    menu:
        "Undress in front of Naomi.":
            pass
            
        "Keep your clothes on.":
            $ sqbpremounlocked = False
            c "I'm sorry, I don't feel comfortable doing that."
            Nm concern "Really? What's the big deal?"
            c "Among humans, taking your clothes off in front of someone is considered an intimate act."
            show naomi confused with dissolve
            c "It's also pretty weird to do in a living room."
            Nm "After all that you still don't...?"
            Nm sad "Oh well. I get it."
            Nm normal "Look at the time. Would you at least like to eat something before you leave?"
            c "Sounds like a plan. I know you said you don't like cooking, but how about I make something instead?"
            Nm confused "You can? I was planning to order a delivery."
            c "Let me see what supplies we have."
            play sound "fx/undress.ogg"
            $ renpy.pause (1.5)
            scene ecknaomiapt02 with dissolvemed
            m "I got off the sofa and headed towards the fridge."
            m "A quick glance over the supplies revealed a rather sizeable selection of fish, chicken and meat snacks, some algae and a wide variety of vegetables."
            c "(Quite decent for someone who doesn't cook at home. She doesn't seem to have oil or anything of sorts, but plenty of sauces to choose from.)"
            m "With most of the food already pre-cooked, preparing something with it wouldn't take a lot of time."
            m "An idea clicked in my mind."
            $ ecknaomim2food = "None"
            menu:
                "Beef and vegetables.":
                    $ renpy.pause (0.5)
                    $ ecknaomim2food = "beef"
                    play sound "fx/veggies.ogg"
                    m "Deciding to go with a tried and tested recipe, I started with chopping up the vegetables I found into smaller pieces while the frying pan was heating up on the stove."
                    m "Once I was done, I mixed up the cut pieces in a bowl with the meat snacks and put it all on the skillet."
                    play sound "fx/fry.ogg" fadein 1.0
            
                "Fried fish with salad and algae.":
                    $ renpy.pause (0.5)
                    $ ecknaomim2food = "fish"
                    $ naomi2mood += 1
                    play sound "fx/veggies.ogg"
                    m "Choosing fish as a base seemed like an obvious solution to preparing something a sea dragoness would enjoy. With the snacks already being breaded, they only needed some heating, a   sauce, and dressing to go with them."
                    play sound "fx/fry.ogg" fadein 1.0
                    m "Mixing up a decent salad proved easy thanks to the selection of vegetables. Unsure what to do with dried algae, I cut off a few pieces and kept them separately."
            
                "Chicken fillet with cheese and ham.":
                    $ renpy.pause (0.5)
                    $ ecknaomim2food = "chicken"
                    $ naomi2mood += 1
                    m "While meat snacks had to substitute actual ham or bacon, the rest of the ingredients were readily available. The chicken \"bits\" – as they were advertised on the package – were in fact full ready-to-eat fillets."
                    m "Using raw counterparts would've been better for overall taste, but I had to make do with what I had. After cutting them open, I added the extra components, hoping for the molten cheese to seal everything together inside."
                    m "Soon, I stuffed the tray with my improvised dish into the oven and set it to the right temperature."
                    
                "Chicken fillet with cheese and ham.":
                    $ renpy.pause (0.5)
                    $ ecknaomim2food = "chicken"
                    $ naomi2mood += 1
                    m "While meat snacks had to substitute actual ham or bacon, the rest of the ingredients were readily available. The chicken \"bits\" – as they were advertised on the package – were in fact full ready-to-eat fillets."
                    m "Using raw counterparts would've been better for overall taste, but I had to make do with what I had. After cutting them open, I added the extra components, hoping for the molten cheese to seal everything together inside."
                    m "Soon, I stuffed the tray with my improvised dish into the oven and set it to the right temperature."
        
            m "From the corner of my eye, I noticed Naomi intently monitoring me from her resting position."
    
            if naomi2mood > 6 and not ecknaomim2food == "salad":
                m "Her tail swished ever so slightly, and her wings remained relaxed – aside from a subtle wavy motion."
            else:
                pass
    
            $ renpy.pause (1.5)
            show ecknaomicg1 at Pan ((250, 230), (620, 50), 15.0) with dissolvemed
            $ renpy.pause (7.5)
    
            if naomi2mood > 6 and not ecknaomim2food == "salad":
                m "When my eyes made contact with hers, she smiled, and the tip of her tail seemed to perk up in response."
            else:
                $ renpy.pause (1.5)
            $ renpy.pause (1.5)
    
            scene black with dissolvemed
            $ renpy.pause (1.0)
            stop sound fadeout 1.0
            scene ecknaomiapt02 with dissolvemed
            m "Eventually, the cooking was finished, and I loaded the fruits of my labor into a single large bowl. Together with it, I grabbed a couple of plates, some bread and returned to Naomi's couch."
            scene ecknaomiapt03 with dissolvemed
            show naomi smile with dissolve
            $ renpy.pause (1.0)
            m "Only then I realized the complete lack of cutlery, save for a lone ladle."
            if ecknaomim2food == "beef" or ecknaomim2food == "fish" or ecknaomim2food == "chicken":
                Nm "Smells delicious, [player_name]."
                c "Thanks. I tried my best."
                m "The dragoness proceeded to merrily devour her portion with little concern about her surroundings. On the other hand, without forks, knives or spoons, I had to wait for my food to cool off."
                c "Hey, no need to rush. We still have time."
                Nm shy "Sorry. Your cooking is just too good."
                Nm confused "Why aren't you eating?"
                c "It's too hot for me – I'd burn my fingers if I grabbed it, and my mouth probably wouldn't fare much better, either."
                Nm normal "Is your skin really that sensitive?"
                c "I don't have scales like you do."
                Nm smile "Alright. Don't worry, I'll make sure to leave you a fair share."
                c "Did you honestly enjoy my cooking so much?"
                Nm shy "I did."
                Nm "It's the first time I got a chance to try out a home meal since my parents moved to the city."
                menu:
                    "I'm glad you liked it.":
                        $ renpy.pause (0.5)
                        Nm smile "I sure did. Thank you, [player_name]."
                        m "Eventually, the food's temperature had dropped, and I was able to finish off my own serving as well. Naomi lazily glanced at the empty plates in front of us."
                        jump sqb_naomi_m2_bedroomfun_end
                
                    "You can have my portion.":
                        $ renpy.pause (0.5)
                        $ naomi2mood += 1
                        Nm "Are you sure that's alright?"
                        c "I can always make myself more when I get back to my apartment. It's fine, just take it."
                        Nm smile "Thank you."
                        show naomi normal with dissolve
                        m "It didn't take long for Naomi to clear out most of the remaining food.{nw}"
                        show naomi shy with dissolve
                        m "It didn't take long for Naomi to clear out most of the remaining food.{fast} She still left a few bites – by then cool enough to handle - and shyly nudged them towards me."
                        Nm "You need to eat something too, [player_name]. I don't feel right stuffing my face while you remain hungry."
                        c "Oh. Don't worry about me. But you have a point – I could use a snack before heading out."
                        Nm smile "Enjoy your meal."
                        show naomi sleep with dissolve
                        m "Once we were both finished, she leaned back and squinted her eyes for a few seconds before glancing back at me."
                        jump sqb_naomi_m2_bedroomfun_end
                
                    "Then learn to cook.":
                        $ renpy.pause (0.5)
                        $ naomi2mood -= 1
                        Nm "I would, but I never had a talent for it or any desire to learn."
                        c "It's never too late to start practicing."
                        Nm smile "I think I'll stick to the cafe and home deliveries."
                        m "Eventually, the food's temperature had dropped, and I was able to finish off my own serving. I noticed that Naomi left a fraction of hers untouched."
                        jump sqb_naomi_m2_bedroomfun_end
                
            else:
                 m "The dragoness put the food on her plate and took a few hesitant bites, mostly concentrating on the algae slices."
                 m "A few minutes later, she glanced at me merrily munching on the salad."
                 Nm blank "Thanks, [player_name]. I think this is enough for me."
                 c "You don't want more?"
                 Nm confused "Oh, I'm fine. Don't worry."
                 m "I finished the rest of my serving a few minutes later. Naomi barely touched hers."
                 jump sqb_naomi_m2_bedroomfun_end
        
    m "A whisper buried deep in my mind told me to just do as she says."
    m "(I suppose because dragons don't wear clothes in the way we do, she doesn't understand the implications of asking me to remove them in front of her.)"
    m "(I'll just take them all off. If it doesn't bother her, it shouldn't bother me either. When in Rome...)"
    Nm confused "Well?"
    c "Sure. In fact, that's a really good point. I've never really thought about it like that before."
    show naomi normal with dissolve
    $ renpy.pause (2.0)
    stop music fadeout 1.0
    play sound "fx/undress.ogg"
    show naomi surprised with dissolve
    #Later on game asks if you're male or female.
    m "Naomi looked at me curiously as I removed my clothes piece by piece."
    show naomi surprisedblush with dissolve
    play sound "fx/undress.ogg"
    m "She was the most attentive when I started to remove my lower garments though. Her eyes fixated on my groin after I had taken my underpants off. A chill entered my spine and I shuddered."
    Nm normal "In addition to your head, have fur even on your chest and between your legs? That must be weird." #Male version
    c "I can shave everything off if it bothers you."
    Nm smile "No, it's kind of cute and different. I was just wondering how it will feel when we cuddle with the covers off."
    c "..."
    #If player is female, Naomi comments on breasts instead.
    Nm normal "Your male parts look pretty squishy. I bet they're very vulnerable because they hang outside of your body like that."
    m "(What have I gotten myself into?)"
    show naomi blank flip with dissolve
    m "Suddenly, Naomi focused her attention away from my groin and looked to her left. I turned to see what she was looking at."
    scene sqbnaomiapt04 with dissolvemed
    hide naomi with dissolve   
    m "She seemed to be eyeing the area right of her fridge. I presumed that the door would lead to her bedroom."
    m "As I realized what she was thinking about, series cold chills went down my spine."
    m "(I hope I can make it undamaged out of this.)"
    show naomi normal with dissolve
    m "Before I had more time to ponder about my fate she walked in front of me."
    play music "mx/campfire.ogg"
    Nm smile "This sofa is awfully small for cuddling. How about we have another session in the bedroom?"
    Nm "If you play it nice, we could even go further than earlier."
    Nm aroused "Please?"
    Nm shy "I hope I'm not moving too quickly for you."
    m "(I guess she doesn't realize that from my perspective she's already asked to have sex with me.)"
    c "I would love some more dragon action."
    Nm smile "In that case...{w} follow me to my bedroom. Who knows, maybe you will be the first one to survive a visit to the dragon's lair intact?"
    m "(Uh oh. That doesn't sound good.)"
    hide naomi with dissolve
    m "Naomi started moving towards her bedroom, beckoning me to follow her."
    m "I wanted to have sex with her but suddenly I was also scared of what that would entail."
    m "This was the last chance to run. If I entered her bedroom, there was no telling what would to happen to me."
    menu:
        "Follow Naomi.":
            m "I decided to resist the the scary thoughts I had."
            $ naomistatus = "girlfriend"
            $ sqbnaomi2sex = True
            pass
         
        "Try to escape while you still can.":
            stop music fadeout 2.0
            m "(If I want to escape, I have to time this correctly.)"
            scene ecknaomiapt02 with dissolvemed
            play sound "fx/sheet.wav"            
            m "As Naomi got closer to her bedroom door, I quietly picked up my clothes and started sneaking towards the exit."
            m "Unfortunately, when I was halfway there Naomi heard me walking in the opposite direction."          
            m "I felt her grab my hand and I was forced to turn around to face her. I was startled, so I dropped some of my clothes on the floor."
            scene ecknaomiapt01 with dissolvemed
            show naomi concern with dissolve            
            m "(Oh no.)"
            Nm "Is something wrong?"
            c "I'm sorry Naomi. I changed my mind about this."
            Nm sad "Oh well. Did I move too quickly for you?"
            Nm "I thought we had a good time together."
            Nm concern "(This always happens to me.)"
            m "(How do I salvage this without upsetting her?)"
            c "Uhh...{w} you've got it all wrong."
            Nm confused "What do you mean?"
            c "You've been good to me so far, and I've enjoyed my time with you."
            Nm concern "Go on."
            c "It's all me, not you. We can meet again some other time."
            c "I'm just leaving because I remembered that I have some urgent ambassador duties that need doing."
            $ renpy.pause (2.0)
            play music "mx/partingsong.ogg"
            Nm stern "Are you being serious right now?"
            Nm sad "That's the kind of thing they always say. Couldn't you at least come up with a less cliché way of dumping me?"
            c "Hey, I really mean what I said."
            c "Anyway, I have to go. We can just meet again some other time."
            $ renpy.pause (1.0)
            Nm "..."
            Nm annoyed "I hate it when you guys patronize me like this. Do you think I am a hatchling?"
            Nm sad "After how nice I was to you, I expected that you would at least be honest with me."
            Nm stern "Did you seriously think I wouldn't notice you trying to sneak out?"
            Nm "Go on, leave. See if I care."
            c "Don't you think you're overreacting just a little bit?"
            c "You have to calm down right now."
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
            m "My dreams that night were full of fire and suffering. I woke up several times trembling in cold sweat."
    
            $ naomistatus = "bad"
            $ naomiavailable = False
            $ naomiscenesfinished = 2
            
            jump ml_date_end               
     
    $ renpy.pause (1.0)
    scene black with dissolvemed
    hide naomi with dissolve
    play sound "fx/sheet.wav"
    queue sound "fx/door/door_open.wav"
    m "I picked up my clothes from the floor and trailed behind Naomi as she walked up to her bedroom door and nudged it open with her snout." 
    scene eckannabedroom4 with dissolvemed
    show naomi normal with dissolve
    Nm smile "Welcome to my lair. When we first met, I didn't expect to invite you here on our second date." 
    Nm shy "Like I said before, I feel like there might be something special between us. I guess we'll find out about that soon enough."
    c "Interesting. Did you finally come around to admitting that our meetups were actually dates from the get-go?"
    Nm stern "Don't ruin the mood by being a smart ass."
    c "Sorry."
    show naomi smile with dissolve
    m "After silently accepting my apology Naomi walked to up to the side of her bed."
    show naomi aroused with dissolve
    m "She turned at me and gave me an inviting look."
    play sound "fx/bed.ogg"
    m "Then she climbed on the bed and rolled on her back, spreading her wings wide."
    show naomi surprisedblush with dissolve
    m "Finally she turned to the right and stretched her legs wide, while still holding my gaze."
    m "(You really notice how much bigger she is compared to a human when she spreads out like that.)"
    show naomi smile with dissolve   
    m "Naomi patted the empty space on her right side with her open palm."  
    Nm "Are you coming or not? My bed feels empty without you."
    m "I gulped and dropped my clothes on the floor, then walked up to the right side of Naomi's bed."
    play sound "fx/undress.ogg"
    m "I sat down on the side, turned and began to lower myself on Naomi's wing, preparing to position myself to have my back against her like before."
    Nm smile "That position won't do at all. I want to feel your squishy belly rub against mine."
    play sound "fx/bed.ogg"
    m "With those words Naomi suddenly turned me around and hugged me tightly before I could protest."
    m "She had me fully tied up in her arms. My head was also lodged firmly under her chin like when we had watched the movie."
    show naomi slsmile with dissolve
    m "She finished the job by wrapping her wings around me."
    Nm shy "Don't hesitate to tell me if I hug you too tightly or make you feel uncomfortable in any way."
    Nm smile "I wouldn't want to damage my human, physically or mentally."
    m "She was very warm and I could now properly feel her powerful heartbeat."
    c "Don't worry about me. This is pretty great."
    m "(I can barely move.)"
    show naomi slsmile with dissolve
    m "Naomi's warm and soft body aroused me to no end. To make things worse, my dick was now hardening up rapidly due to it being in contact with Naomi's lower belly."
    m "(Oh no. I hope her learning more about my mammalian traits won't be too embarrassing.)"
    Nm shy "Have I now convinced you that your place is here with me?"
    c "You convinced me a long time ago. I wouldn't trade being here with you for anything."
    Nm aroused "Likewise. When we first met, somehow I immediately knew we would get along nicely."
    show naomi slsmile with dissolve
    play sound "fx/sheet.wav"
    m "Then suddenly, she locked me in place with her legs, shifting me around a little bit to hold me even more tightly than before."
    play sound "fx/purr.ogg"
    m "After that she purred while tying my ankles together with the end of her tail."
    Nm "Very nicely... in fact."
    m "A terrified feeling washed over me as I realized that due to my position shifting again, the tip of my erect dick was now poking her lower belly directly."
    stop music fadeout 1.0
    stop sound fadeout 1.0
    $ renpy.pause (2.0)
    Nm shy "Is that what I think it is?"
    c "I'm sorry!" 
    c "I can't control my penis. It gets erect on its own whenever I am sexually stimulated."
    Nm surprisedblush "Oh..."
    c "..."
    c "That doesn't weird you out?"
    m "Naomi paused to think for a moment."
    Nm smile "Why would you being aroused weird me out?"
    Nm slsmile "After all it just means that...{w} you know..."
    play sound "fx/lewd/lickslow.ogg"
    m "She licked my forehead with her long tongue."
    play music "mx/treetops.mp3"
    Nm aroused "That you actually want to have sex with me?"
    m "Her remark made me feel like my heart had just jumped to my throat. To make things worse, my face felt so hot, I bet it had turned completely red right in this moment."
     
    if modinfo.has_mod("BangOk?") and bangok_four_bryce1_unplayed == False or bangok_four_xsebastian_unplayed == False or bangok_four_anna2.unplayed == False:
        m "(Why am I feeling so anxious right now? It shouldn't be that much different with Naomi. I need to calm down or I'll embarrass myself again.)"  
    else:
        m "(Why am I feeling so anxious right now? It shouldn't be that much different with a dragon. I need to calm down or I'll embarrass myself again.)"
         
    m "Naomi interrupted my line of thought."
    Nm smile "Have you thought of what other humans would say if they found out that you wanted to have sex with a dragon?"
    $ renpy.pause (2.0)
    m "After a moment of silence, I gulped loudly, which she surely heard."
    c "B-but t-there aren't-{nw}"
    Nm surprisedblush "Oh, so you've fantasized about doing it with a dragon before?"
    show naomi aroused with dissolve
    m "Naomi shifted and I could feel her starting to warm up more."
    Nm slsmile "Wanting have sex with another sentient species..."
    Nm aroused "...now that's a kink I like."
    m "Due to her remarks, my stomach was full of butterflies and I was so embarrassed I felt like I was going to choke. Yet somehow, I managed to speak up yet again."
    c "W-well I-{nw}"
    Nm surprisedblush "Don't worry about it."
    Nm shy "By the way, your face is completely red. Are you feeling okay?"
    m "Naomi moved her maw closer. I could feel her hot and almost steamy breath on my face."
    c "Yes... umm..."
    c "I'm j-just-{nw}"
    Nm smile "Feeling very embarrassed and aroused right now? I'm just teasing you because I knew you would be unbelievably cute flustered like this."
    Nm slsmile "I'm going to keep you safe here with me and never let you you go."
    m "I felt so anxious I was about to have some kind of weird seizure. Fortunately, Naomi was holding me so tightly I couldn't move at all. My resistance was indeed weak and pathetic."
    Nm smile "I know just how to cool your face and calm you down."
    show naomi slsmile with dissolve
    play soundloop "fx/lewd/lickslow.ogg" fadein 1.0
    m "Naomi started licking my entire face in circles with her long tongue, mostly focusing on my presumably red cheeks."
    m "(I don't think she is being genuine in trying to cool me down. Not that I mind her methods.)"
    $ renpy.pause (2.0)
    stop soundloop fadeout 2.0
    c "I like it when you lick me with your long tongue."
    Nm smile "Same, because you're so delicious."
    Nm shy "Do you really want to go further with me?"
    
    if persistent.nsfwtoggle == True:
        pass
        
    else:   
        stop music fadeout 1.0
        play sound "fx/system3.wav"
        show naomi stern with dissolve
        s "Skipping the sex scene since it looks like you have the NSFW mode turned off."
        show naomi normal with dissolve
        play music "mx/airborne.mp3"
        jump sqb_naomi_m2_sfwskip       
    
    m "I felt like I had no choice but to fuck her immediately or I was going to die due to my heart bursting out of my chest."
    show naomi aroused with dissolve
    c "Yes. You are a sexy and wonderful dragoness."
    Nm smile "I'm happy to hear that, [player_name]." 
    Nm normal "When you removed your clothes, I saw where your genitals are located. I don't think our anatomies are too different to make this inconvenient for us."
    
    #Naomi thinks having multiple partners is fine as long as you like her the most
    if modinfo.has_mod("BangOk?") and  bangok_four_anna2.unplayed == False:  
        c "Actually, our anatomies aren't too different. I already had sex with Anna."
        Nm confused "What, really? She hates everyone, but suddenly took a liking to you?"
        Nm stern "Hold on...{w} did she agree do it to experiment on human anatomy?"
        c "Hey, you've been experimenting a lot on me as well."
        c "I just asked her to have sex with me as a wager of a game. She's also rather promiscuous, not that I mind."
        Nm smile "We're all promiscuous over here."
        c "So, how do you want to proceed from here?"
        Nm aroused "First, I have another experiment of my own in mind."
        
    elif modinfo.has_mod("BangOk?") and bangok_four_bryce1_unplayed == False:
        c "Actually, Our anatomies aren't too different. I had sex with Bryce when I went drinking with him."
        #More accurate references
        Nm confused "What, really? I'm surprised you can still walk."
        c "The alcohol helped a lot. And of course lots of lube."
        c "So, how do you want to proceed from here?"
        Nm smile "Let me think..."
    
    elif modinfo.has_mod("BangOk?") and bangok_four_xsebastian_unplayed == False:
        c  "Actually, I already had sex with Sebastian. Our anatomies aren't too different."
        Nm "I'm not surprised, he's kinda cute. I just wish he dropped his dutiful police officer persona once in a while."
        #More
    
    #PC says he came here to establish friendly relations and fucking dragons is one way of achieving that
    elif modinfo.has_mod("BangOk?") and bangok_four_bryce1_unplayed == False or bangok_four_anna2.unplayed == False:
        c "I've already had sex with Anna and Bryce. Our anatomies aren't too different."
        Nm surprised "You've already fucked two people I know since you came here?"
        Nm confused "That can't be a coincidence."
        Nm smile "Are you sure you're not a dragon-fucking sex tourist rather than an ambassador?"
        #More
    
    elif modinfo.has_mod("BangOk?") and bangok_four_xsebastian_unplayed == False or bangok_four_anna2.unplayed == False:
        c "I've already had sex with Anna and Sebastian. Our anatomies aren't too different."
        Nm surprised "You've already fucked two people I know since you came here?"
        Nm confused "That can't be a coincidence."
        Nm smile "Are you sure you're not a dragon-fucking sex tourist rather than an ambassador?"
        #More
    
    elif modinfo.has_mod("BangOk?") and bangok_four_bryce1_unplayed == False or bangok_four_xsebastian_unplayed == False:
        c "I've already had sex with Bryce and Sebastian. Our anatomies aren't too different."
        Nm surprised "You've already fucked two people I know since you came here?"
        Nm confused "That can't be a coincidence."
        Nm smile "Are you sure you're not a dragon-fucking sex tourist rather than an ambassador?"
        #More
    
    else:
        pass
    
    Nm slsmile "I'll try one more thing to get you properly in the mood."
    m "Naomi freed one of her arms and used her claw to nudge my head upwards."
    play sound "fx/lewd/altpen.ogg"    
    m "Then she moved her mouth to mine and tongue kissed me, applying her long tongue."
    play soundloop "fx/lewd/pussy.ogg"     
    m "Then she started tickling the inside of my upper jaw with the tip of her tongue. It was a weird tickling sensation I'd never experienced before."
    show naomi aroused with dissolve
    m "When I leaned toward her to reciprocate the dragon tongue kiss, Naomi opened her eyes to look back at me directly. She looked at me like I was what she treasured the most in the entire world."
    Nm shy "(I love you so much.)"
    show naomi aroused with dissolve
    m "The only things I could do on top of staring back into her beautiful emerald eyes was to focus breathing through my nose and staying as still as possible."
    m "Again, I felt like my chest was going to explode."
    m "(I'm going to die of a heart attack by dragoness. What the hell are they even going to write on my tombstone?)"
    stop soundloop fadeout 2.0
    Nm confused "You're completely powerless to do anything to resist my advances, aren't you?"
    Nm smile "Alright, we've had enough foreplay."   
    Nm "Is fucking me sideways in this position fine by you?"
    m "I was surprised she even asked for my opinion. I managed to mumble up a response."
    c "A-any position with you is going to be amazing."
    Nm "Good little obedient human."
    play sound "fx/sheet.wav"
    m "Naomi released me from the prison of her legs and spread them around."
    Nm shy "Can you see the slit between my legs?"
    
    if modinfo.has_mod("BangOk?") and persistent.bangok_cloacas == False:
        m "I looked down at Naomi's groin, seeing a single vertical slit and an asshole below it."
        m "It seemed that I needed to go down a little bit to reach her pussy and also to have some leverage to thrust inside."        
    else:
        m "As I turned my head to look at Naomi's groin, I now saw an aroused-looking horizontal slit that had been well-hidden previously."
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
        play sound "fx/lewd/pussy.ogg"
        m "I found out that even though Naomi's cloaca looked pretty wide at first glance, it actually narrowed and separated into two passages positioned vertically from each other."
        
        if modinfo.has_mod("BangOk?") and  bangok_four_anna2.unplayed == False:
            c "It's a bit different from Anna's, but I can manage everything because I am the dragon pussy master."
            
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
    Nm normal "No, that won't be necessary since I don't have any STDs and I trust don't have either, otherwise you wouldn't have agreed to have sex with me in the first place."
    c "You're right about that."
    Nm smile "That settles it then. We won't ever have to use protection as long as you handle yourself with care in any other sexual relationships in the future." 
    Nm shy "I'm very eager to get to feel your human cum inside me every time you fuck me."
    Nm aroused "Who knows what might end up happening if we're lucky?"
    m "(What's she even talking about?)"
    m "(Oh...{w} doesn't she know that I can't get her pregnant? Didn't she pay attention in biology class?)"
    m "(That, or she's just testing me to see if I like her enough to impregnate her in case it was even possible. I guess just I'll do my best to satisfy her kinks.)"
    Nm confused "So, will you cum inside me?"
    c "Whatever works for me. I just want to fuck you right now."
    Nm aroused "That's actually the nicest thing you've said to me so far."
    show naomi shy with dissolve
    play sound "fx/sheet.wav"
    m "I moved downwards, my hands trailing behind Naomi's back."
    play sound "fx/bed.ogg"
    m "I moved myself between her muscular legs. Due to our size difference, in this position my face only reached up to her chest."
    m "I placed my hands behind Naomi's lower back in order to get more leverage as I prepared to penetrate her."
    
    if modinfo.has_mod("BangOk?") and persistent.bangok_cloacas == False:
        show naomi aroused with dissolve
        play sound "fx/lewd/pussy.ogg"
        m "Then I used my fingers to spread her pussy and lined the tip of my penis with her opening."        
    else:
        show naomi aroused with dissolve
        play sound "fx/lewd/pussy.ogg"
        m "Then I used my fingers to spread her cloaca and lined the tip of my penis with her vaginal passage."
    
    c "Are you ready?"
    Nm slsmile "I've been ready for a while."
    play sound "fx/lewd/penslow.ogg"
    queue sound "fx/sheet.wav"
    m "As I penetrated her pussy, she locked me tightly in place with her legs."
    Nm smile "Caught you!"
    play sound "fx/lewd/penfast.ogg"
    m "After the shallow initial penetration, I moaned as I bucked myself as far as I could go in a single thrust." 
    m "The sensation of fully plunging yourself into someone much bigger than you was something I had never quite experienced before."
    
    if modinfo.has_mod("BangOk?") and  bangok_four_anna2.unplayed == False:    
        m "(Naomi's tighter than Anna. That's surprising since Naomi much bigger than her.)"
        m "(I suppose Anna really has a preference for larger partners.)"
        m "(I'm still fortunate to have an above average penis, or else I most likely couldn't get Naomi off with it at all.)"
    else:
        m "(Even though Naomi's slit is rather large when aroused, she's a lot tighter from the inside than you would expect.)"
        m "(I suppose she's only had smaller partners, like she alluded to earlier.)"
        m "(I'm still fortunate to have an above average penis, or else I most likely couldn't get her off with it at all.)"
    
    Nm confused "Was that it? Are you going to pump at all?"
    c "Uhh... I was lost in thought."
    Nm stern "This isn't the best time to lose yourself."
    c "Sorry!"
    play soundloop "fx/lewd/penslow.ogg"
    show naomi aroused with dissolve
    m "After having to apologize yet again I started penetrating Naomi's pussy with long, thorough thrusts."
    Nm smile "Good little human." #Rethink
    m "Naomi wrapped her wings around me like before."
    Nm aroused "Keep that pace up."    
    m "In this moment, due to Naomi covering almost my entire field of view, she was the only thing that existed for me in the world."
    Nm smile "You belong to me now. The only way to go is forward." 
    m "She was right, because due to being locked in place by her strong legs, thrusting forward was just about the only movement I could do."
    Nm slsmile "Remember, I'll only let you go after you cum inside me."
    $ renpy.pause (3.0)
    stop soundloop
    play soundloop "fx/lewd/penfast.ogg"
    m "As I got more used to the position I was in, I started thrusting faster into Naomi."
    m "I couldn't last very long though, since the extended tease had exhausted my stamina. Then suddenly without warning, a release started rapidly building up inside me." 
    m "After the realization that I was going to cum soon, I hoped she would be satisfied with my performance or at least be understanding of my predicament."
    c "Naomi... I'm going to cum soon."
    Nm surprisedblush "Already? Fine, but don't even think about pulling out."
    Nm smile "Not that I would let you anyway."
    Nm shy "I thought humans would last longer than this."
    c "It's your fault for teasing me for so long. I've been hard for hours."
    Nm smile "That's what someone with no stamina would say."
    Nm "Finish if you have to. Don't think I'm done with you yet though."
    stop soundloop
    play soundloop "fx/lewd/altpen.ogg"
    m "Since I had gotten the permission to finish, I started preparing to shoot my cum in Naomi by thrusting deeper."
    Nm smile "I feel you're getting ready to release. I won't settle for anything less than a big fat load of your human cum in my deepest place." 
    m "Naomi's comment excited me so much that I came immediately. She sensed that, and used her leg lock to press me even more tightly on her groin."
    stop soundloop fadeout 2.0 
    play sound "fx/lewd/cum.ogg"
    queue sound "fx/lewd/penslow.ogg"
    $ renpy.pause (1.0)
    show naomi aroused with dissolve
    c "Urgh!!!Ahh!!!{nw}" with hpunch
    play sound "fx/lewd/penslow.ogg"
    queue sound "fx/lewd/cum.ogg"
    queue sound "fx/rub2.ogg"
    queue sound "fx/lewd/lickslow.ogg"
    queue sound "fx/lewd/lickslow.ogg"
    queue sound "fx/lewd/lickslow.ogg"
    queue sound "fx/lewd/lickslow.ogg"
    show naomi slsmile with dissolve
    m "I bucked against Naomi for another time to release my second rope of cum. She let out a content sigh and started gently rubbing the back of my neck and licking my face. After she was done petting me, she turned on her back, taking me with her."
    Nm aroused "I can feel a whole lot of your sticky seed inside me. You weren't joking about being pent up."
    Nm shy "Unfortunately, you didn't manage to get me off." 
    Nm smile "If you can't go again you can finish me off with your mouth."
    menu:
        "Use dick.":
            c "I still have another round in me. Just give me a few moments to recover."
            Nm stern "Try to last longer this time."
            c "I promise I'll do better."
            show naomi normal with dissolve
            m "My almost limp dick still rested inside Naomi. After a few moments she released me from the prison of her legs so I pulled out and jerked my dick a couple of times. I breathed in deeply as I was working to get myself erect again."
            #Sound?
            $ renpy.pause (4.0)
            c "Okay, I'm ready for round two."
            Nm smile "Give it your best shot. I know you can get me off this time."
            show naomi surprisedblush with dissolve
            m "I leveraged myself on Naomi's spread-out legs and squeezed her enormous thighs. Based on her expression, she liked it when someone played with her thighs."
            play sound "fx/lewd/penslow.ogg"
            m "With my now increased leverage, I lined the tip of my dick with her cloaca and immediately pushed myself fully inside her vaginal passage."
            Nm aroused "Ohh. This time, I forbid you to cum before me."
            play soundloop "fx/lewd/penslow.ogg"
            m "After her tacit approval, I started penetrating Naomi with slow and deep thrusts."
            c "How about a kiss? You'll have to use your tongue though, because I can't reach that far."
            show naomi smile with dissolve
            play sound "fx/lewd/lickslow.ogg"
            m "As I held my own tongue out, she flicked it and my nose with her long, draconic tongue."
            Nm "I'm going to punish you from afar with tongue lashes if you don't fuck me well enough."
            c "That's so hot. You know just how to press my buttons."
            m "As I kept fucking Naomi, some of my seed seeped out of her pussy. This made me even harder than before since it reminded me of what I had just done a few moments earlier, what I would be doing again soon and hopefully many more times in the future."   
            if modinfo.has_mod("BangOk?") and bangok_four_bryce1_unplayed == False or bangok_four_xsebastian_unplayed == False or bangok_four_anna2.unplayed == False:
                m "(I can't believe Naomi wants me to cum inside her so badly.)"
            else:
                m "(I can't believe I just came inside an actual, living dragon. I think I just broke a pretty important barrier for the sake of advancing humanity.)"
            
            Nm aroused "[player_name]...{w} I'm approaching my limit. Let's see if you're skillful enough to make us both cum at the same time."
            c "I'll try my best." #PC fails
    
            stop soundloop fadeout 1.0
            stop music fadeout 1.0
        
        "Use mouth.":
            c "I'm spent, I'll just use my mouth."
            Nm "Works for me."
    
    #PC puts clothes back on
    
    $ persistent.sqbnaomi2sex = True
    
    play music "mx/airborne.mp3"
    c "That was the best sex I've ever had. I think the hours-long tease had something to do with it."
    Nm normal "It was certainly fun to play with someone who is too weak to resist anything I do to them."
    Nm smile "I'm looking forward to many more sessions like this."
    m "(I'm doomed.{w} Wait no, I'm in heaven.)"
    c "Me too."
    
    c "Naomi, I can't think of a word to describe how much I love you. Do you want to get married?"
    Nm surprised "Is that how it works in your world?"
    Nm confused "We've only had sex once so far. That doesn't mean we should get married yet."
    Nm normal "Marriage is a long-term commitment."
    c "Didn't you say before that you wanted me to stay with you forever?"
    Nm concern "I did...{w} and I really do like you. I just want to be absolutely sure before I start making any actual long-term plans for my future."
    Nm sad "I've had some bad experiences in the past and I'd rather not get hurt like that ever again."
    m "(Seems that her fear of abandonment and self-esteem issues are worse than I initially thought.)"
    c "I'll do my best to prove myself worthy of you, then."
    Nm smile "Thank you for being so understanding."
    show naomi normal with dissolve
    m "(What should we do next?)"
    c "Wanna take a shower together?"
    Nm smile "Sure, let's get cleaned up. We could even have some more fun if you've recovered."
    c "We'll see about that. Let's go."    
    play sound "fx/rumble.ogg"
    $ renpy.pause (4.0)
    show naomi concern with dissolve
    m "(It seems that we forgot to eat.)"
    Nm confused "Oh, you're hungry?"

jump sqb_naomi_m2_cooking

label sqb_naomi_m2_cooking:

    #Inspired by the original ASM's, Adine's shopping spree mod's and Lorem mod's cooking scenes
    
    Nm normal "We could order some food if you wanted. Cooking ourselves works as well if that's something you'd want to do."
    c "Actually, a fun time in the kitchen sounds great right now. I want to return all the hospitality I've gotten here so far by pampering you back."
    Nm shy "You really don't have to. I enjoyed myself as well."
    Nm blank "Wouldn't it be easier if we just phoned in a food order and showered together while waiting for the delivery to arrive?"
    c "Shower can wait. I really feel like cooking right now."
    c "Besides, I also want to find out how similar your food products are to ours. One of my personal reasons for coming here was to learn more about your society and customs."
    c "For now I'll have to say that the food's been pretty similar to ours. Still, I'd be very interested in delving deeper into this by getting some first-hand experience."
    Nm smile "Well, if you put it like that...{w} I suppose I will have to let you sate your curiosity. More importantly, I would never turn down a delicious home-cooked meal." 
    c "Looks like that's settled then. I promise you won't be left hungry, because I'll cook a couple of dishes."
    Nm normal "I can't wait to do some taste testing. What delicious human dishes are you going to cook?"
    c "I don't know yet. I'll have to see what's in the kitchen."
    c "Let's go."
    hide naomi with dissolve
    scene black with dissolvemed
    play sound "fx/door/door_open.wav"
    m "We exited Naomi's bedroom back into the main part of her apartment. For some reason, this time she was trailing behind me instead leading me like before."
    scene ecknaomiapt02 with dissolvemed
    show naomi normal with dissolve
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
    m "(Not a surprise that it's the same stuff my apartment was stocked up with. Yet somehow I still haven't gotten used to how weird it is that so many things even down to tiny details like labels on food products are almost identical to human ones.)"
    m "(I have to admit that while this makes me feel a bit familiar, I'm also very unsettled at the same time.)"
    m "(Oh right, Naomi wanted to drink something. She liked juice, right?)"
    m "I took a carton of juice from the back of the fridge."
    play sound "fx/cabinet.ogg"
    queue sound "fx/pour.ogg"
    queue sound "fx/glassdown.wav"
    m "Then I poured the juice in a large class. After that I added a straw and placed the glass on the kitchen counter."
    m "(I guess I can give it to her when she comes back.)"
    play sound "fx/pour.ogg"
    queue sound "fx/chug.wav"
    queue sound "fx/glassdown.wav"
    m "I took a smaller glass, poured some juice for myself and drank it in one go."
    m "(I really needed that. It tastes a bit like orange and mango juice.)"
    m "Now I was fully prepared to continue figuring out what all the stuff in Naomi's kitchen was."
    play sound "fx/cabinet.ogg"
    m "(It's the mostly the same thing with the produce in her cabinets as well. Also, there's so much stuff you'd think she cooks at home.)"
    m "(Wait, did she buy all this just to impress me? That's very cute.)"
    m "(But how did she know I like cooking? I suppose I should ask her when she comes back.)"
    m "(Back to the main task at hand. I think at first I should move a bunch of stuff on the kitchen counter and sort everything by type.)"
    play sound "fx/rummage.ogg"
    m "With some effort, I moved most of the foodstuffs and ingredients onto Naomi's kitchen counter and organized them."
    m "(This is going to be fun. Still, having only two cooktops might pose a challenge. They're pretty old-fashioned as well.)"
    m "(Anyway, as the second order of business, I'll put back what I won't use. I can always take something back if I need it later)"
    $ renpy.pause (1.0)
    #Placing sound?
    m "(I'm not going to take my chances with the fish. Maybe I'll try some in the future, when I am more familiar with the types of fish here.)"
    #Placing sound?
    m "(Also, I can't be certain what's in some these cans even after reading the labels. I should play it safe, so they'll have to go.)"
    $ renpy.pause (2.0)
    m "(Some of these vegetables don't look familiar at all to me. I'll only use ones that look vaguely similar to what I've used before."
    $ renpy.pause (2.0)
    play sound "fx/crapfridge.mp3"
    queue sound "fx/cabinet.ogg"
    m "(Alright, this looks better. Let's figure out what we actually want to use.)"    
    $ renpy.pause (2.0)
    m "I noticed a pack of egg noodles and a large pack of lightly salted chicken fillets."
    m "(I definitely feel like frying some noodles. I'll use the chicken as well, although I am not yet sure how. They're both very solid picks no matter what I choose to make out of them.)"   
    m "(For example, I like the flexibility of these types fillets because you can always cut them to pieces if you want, but also season them how you like. Noodles are great too, because almost everyone likes them.)"
    play sound "fx/faucet1.ogg"
    queue sound "fx/button_press.ogg"
    m "(To start off, I poured water from the kitchen faucet into an electric teapot and turned it on to heat some water for the noodles.)"
    m "(It's a lot less effort to heat the water with an electric teapot. Also, the water stays hot longer inside it.)"
    play sound "fx/door/door_open.wav"
    queue sound "fx/door/doorclose.ogg" 
    m "As I was pondering on how to proceed, Naomi came out of the bathroom to check on how I was doing."   
    show naomi normal with easeinright
    Nm "Did you manage to find out where everything is?"
    c "Yes, thank you. You seem to have quite a lot of stuff stored in your kitchen. I'd have guessed you usually cooked at home if you already didn't tell me otherwise."
    Nm shy "Well..."
    Nm normal "I wanted to try out something new since you were coming over, so I made an exception and went on a shopping spree after work. It felt just like the right thing to do."
    Nm smile "Looks like my plan worked, since I managed to get you to cook for me."
    c "Oh, you got me with your scheme. This is going to be fun, I promise."
    Nm "I'll hold you to that."
    c "By the way, here's something to drink."
    Nm normal "Thanks a lot. I'll leave you to it." 
    Nm concern "I don't think I would be of much help with my clumsy hands anyway."
    c "I hope they're not too clumsy for eating, or else I'll have to feed you."
    Nm smile "Is that an offer? I would love to have my very own cute little human servant who feeds me every time I am hungry."
    c "Uhh..."
    Nm "You're so cute when flustered."
    Nm normal "Are you sure you're fine doing all this by yourself?"
    c "Sure, it's no problem. Just let me handle everything."
    Nm smile "Thanks a lot, [player_name]."
    show naomi normal flip with dissolve
    hide naomi with easeoutright
    m "With my assurance, Naomi walked past me into the living room and drank some juice."
    m "After that she jumped on the sofa in one smooth motion and started flexing."
    m "I kept watching Naomi as she did it. To me, the flexing made her look like a big scaly cat with wings and cute webbing."
    m "After finishing her exercise and settling back on the sofa, she noticed I was admiring her instead of preparing to cook."    
    show ecknaomicg1 at Pan ((250, 230), (620, 50), 15.0) with dissolvemed
    $ renpy.pause (7.5)
    m "She is so big and muscular...{w} especially her thighs and chest."    
    Nm "Your mouth is gaping. Like what you see?"
    c "I think I already saw plenty in the bedroom. Although...{w} I have to admit that you look very cute lying on the sofa admiring me."
    Nm "Hurry up with the cooking, or I'll have to eat you instead."
    c "..."    
    scene black with dissolvemed
    $ renpy.pause (1.0)
    scene ecknaomiapt02 with dissolvemed    
    m "(Where was I?)"
    m "(Oh right, let's see what else we've got.)"
    play sound "fx/rummage.ogg"
    $ renpy.pause (2.0)
    m "(This white, basil-flavored mouflon and aurochs cheese looks remarkably similar to something we used to have.)"
    #Sound?
    m "I cut open the packaging with a knife and then sliced off a chunk of the cheese into my mouth for a taste test."
    m "(Perfect, I'll cut this into pieces cook it with the fried noodles.)"
    m "(On top of that some of these vegetables will add a nice texture and hopefully good flavor as well. Also, we got soy sauce, wing sauce, brown sugar and ginger powder to season the whole thing.)" 
    m "(Let's start off by heating up a pan first.)"
    play sound "fx/metalbox.ogg"
    m "I took a pan and put it on the cooktop but as I turned on the heat I realized something."
    m "(Wait a minute. Let's first make sure I don't get eaten by a hungry dragoness.)"
    c "Naomi, would you like some bread sticks as appetizers?"
    Nm "Sounds great to me. In fact, I was just going to come over there and eat your ingredients."
    c "If you eat them, I won't be able to prepare them into dishes."
    m "I focused back on the task at hand and quickly picked all the required ingredients for the appetizers."
    m "(Toast, garlic paste, black pepper, salt and herb mix here we go. Wait, where's the olive oil?)"
    play sound "fx/cabinet.ogg"
    queue sound "fx/cabinet.ogg"
    queue sound "fx/rummage.ogg"
    $ renpy.pause (8.0)
    m "After looking through some more of Naomi's kitchen cabinets I found the olive oil hidden behind some boxes."
    m "(There we go.)"
    Nm "Need help finding something?"
    c "I'm fine. I was just looking for some olive oil."
    m "(Finally, we can get started.)"
    play sound "fx/button_unpress.ogg"
    $ renpy.pause (2.0)
    queue sound "fx/metalbox.ogg"
    queue sound "fx/unwrap.ogg"
    m "I turned on the oven and prepared two baking trays with baking paper."
    m "(I suppose I can bake a big pile, since slicing the toast won't take too long if I do it efficiently.)"
    m "(The oven probably isn't ready when I am done with the cutting, but I can always start preparing for something else. Also, I will have even more time when the bread sticks are in the oven.)"
    m "(Oh yeah, I also have to prepare the mix to flavor the bread sticks. Who knows if the oven will be ready after I've done that. Multitasking and planning ahead in the moment is so much fun.)"
    m "I opened a bag of toast and put several slices on top of each other on the cutting board."
    play sound "fx/crapcuttingboard.mp3" #Not perfect but it just works
    m "Then I cut the bread into neat sticks, moved them off to the side and prepared cut another batch of toast."
    play sound "fx/crapcuttingboard.mp3"
    m "After a couple of minutes of knife-work, I managed to slice the entire bag of bread."
    #Sound?
    m "To create the flavor mix, I combined a ton of garlic paste and some olive oil, pepper and salt. After that I arranged all the unbaked bread sticks on the two baking trays and used a spoon to apply the flavor mix."
    m "(Looks like I have some time left after all since the oven isn't ready yet.)"
    m "(I should probably figure out what to do with the chicken next. Let's check again what ingredients we've got.)"
    play sound "fx/rummage.ogg"
    $ renpy.pause (2.0)
    m "(Looks like we have the ingredients for batter plus some herb butter.)"
    m "(Let's stuff the chicken fillets with herb butter and bread and fry them. I've never met anyone who doesn't like that dish.)"
    play sound "fx/metalbox.ogg"
    m "I set a pan to heat up on the cooktop and cut open the large pack of chicken fillets."
    m "(Let's see... {w}the eight chicken fillets in this pack should be enough for both me and Naomi. She can always eat the rest tomorrow if there's any left over.)"
    m "I put a fillet on the cutting board and grabbed a knife."
    play sound "fx/sliceshort.ogg"
    m "In order to create a pocket for the herb butter I cut the fillet horizontally through the middle and then expanded carefully, to make sure I don't create any additional holes that need plugging."
    play sound "fx/sliceshort.ogg"
    queue sound "fx/sliceshort.ogg"
    m "I repeated this arduous process for the seven remaining fillets."
    play sound "fx/crapcuttingboard.mp3"
    m "Next I sliced all of the herb butter into pieces and stuffed it inside the pockets I had just cut. After that I closed the hole in each fillet with a large toothpick."
    m "This was the most tedious part of my cookout, but time went quickly because I knew the effort would be well worth it."
    play sound "fx/salt.ogg"
    m "To finish everything off, I sprinkled some black pepper on the stuffed fillets."
    m "(Finally done. Also, looks like the oven is ready just in time so I don't have to wait.)"
    play sound "fx/door/hallwaydoor.ogg"
    m "I put the baking trays with the bread sticks in the oven and set a timer."
    m "(Our hunger's going to be alleviated soon.)" 
    m "(I think I should figure out a side dish for the breaded chicken fillets before I do anything else.)"
    $ renpy.pause (2.0)
    m "(Looks like we have some higher-starch potatoes for mashing that would go really well as a side. Luckily, I have some hot water already.)"
    play sound "fx/faucet2.ogg"
    queue sound "fx/metalbox.ogg"
    queue sound "fx/faucet1.ogg"
    queue sound "fx/button_press.ogg"
    m "I took a large pot, filled it with water first from the teapot and the rest from the kitchen faucet. Then I set the pot to heat up on the cooktop. Since I still wanted to save time on the noodles, I partially filled the teapot again from the sink and turned it on."
    m "(I wish I had realized this earlier, because boiling the potatoes will still take some time.)"
    m "(Moving on to the potatoes proper. I think if I peel them really fast I'll be on time.)"
    play sound "fx/faucet2.ogg"
    queue sound "fx/rub1.ogg"
    queue sound "fx/rub1.ogg"
    m "I emptied all the potatoes into the sink, then rinsed and rubbed them to get all the dirt off."
    #Peeling sound?
    m "After peeling the potatoes at a lightning speed, I had a large bowl of potatoes ready to be boiled."
    m "(Another tedious step done in my quest to cook for Naomi. The water isn't boiling yet, so I should probably move back to the chicken fillets.)"
    play sound "fx/dishes.wav"
    m "To continue preparing the chicken fillets I took three deep plates and a normal one. I filled the deep plates with flour, egg with a touch of water and finally breadcrumbs. I placed them horizontally on the counter with the normal plate at the end of the production line towards the stove."
    play sound "fx/water1.ogg"
    queue sound "fx/water1.ogg"
    m "I dipped a fillet in first flour, then egg, followed by breadcrumbs and finally egg and breadcrumbs again and placed it on the ready-plate. I repeated this messy process for the rest of the fillets."
    play sound "fx/salt.ogg"
    m "Lastly, I sprinkled some breadcrumbs on all of the fillets on the ready-plate to make sure they were properly breaded everywhere."
    m "(The crunch is very important.)"
    m "(I think I'll time everything correctly if I cook four fillets at a time. The pan is more than big enough for that.)"
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
    m "To not splash any hot water on myself, I took extreme care when dropping the potatoes into the pot, added some salt and set a new timer."
    $ renpy.pause (1.0)
    m "(Looks like the bread sticks are almost done. It doesn't really matter if I take them out a or so minute early so I might as well do it now to stay on schedule.)"
    play sound "fx/door/hallwaydoor.ogg"
    queue sound "fx/salt.ogg"
    queue sound "fx/unwrap.ogg"
    m "I took the trays out of the oven and sprinkled some herb mix on the baked bread sticks. Then I used the baking paper to slide them onto a very large plate."
    play sound "fx/fry.ogg"
    m "Not forgetting about the chicken fillets, I turned them for the first time."
    stop sound fadeout 1.0
    play sound "fx/pizzabite.ogg"
    m "Then I ate a few of the bread sticks sate some of my worst hunger. They were crunchy, spicy and garlicky but also most importantly tasty, like I had expected them to be."
    m "(I'm sure Naomi will love these.)"
    m "My hands got messy from eating with them so I instinctively wiped off the grease on a kitchen towel and realized something."
    m "(I'll have to make sure Naomi doesn't make a mess eating the bread sticks. She'll probably ask me to clean up afterwards if that ends up happening.)"
    scene ecknaomiapt03 with dissolvemed
    m "I picked up the bread stick plate along with some rather large napkins and went off to the living room where Naomi was. She was attentively watching what I presumed to be one of those long series she had earlier told me about."
    show naomi normal with dissolve
    Nm "That was certainly a lot faster than waiting for a food delivery. It seems that we made the correct choice."
    show naomi surprised with dissolve
    m "I presented the appetizer plate to Naomi and it immediately perked up her attention."
    c "So, here's something to start off with. Do you think I made enough so that you won't have to eat me?"
    Nm shy "I hope you understood that I was just joking. In fact, I can go a long time without eating if I really need to. I just need to eat a lot to keep in shape for some of my more physical activities, like long-distance flying or swimming."
    c "I know. I was just playing along with your antics."
    Nm blank "Oh, you got me."
    Nm smile "Thanks a lot, [player_name]. These bread sticks smell delicious."
    c "You're welcome, Naomi. Please remember to use the napkins after you've finished eating them. Also, avoid touching any of the furniture before you've wiped your hands clean."
    Nm shy "You're really thinking of everything for me, aren't you?"
    show naomi surprised with dissolve
    play sound "fx/pizzabite.ogg"
    queue sound "fx/pizzabite.ogg"
    queue sound "fx/pizzabite.ogg"
    m "Naomi had been eyeing the bread stick plate hungrily ever I since I presented it to her, so it didn't come off as a surprise when right after I placed it on the table she stuffed a big handful of them right into her maw and ate them."
    Nm smile "Delicious!"
    Nm normal "Why aren't you eating any? Surely there's enough for both of us."
    c "I already ate a couple in the kitchen, and that was enough for me. You should remember that I can't eat as much as you can so I have to leave room for the other dishes."
    Nm smile "I suppose that just means more for me then."   
    
    if naomi1drink == "cocktail":
    
        Nm confused "By the way, could you fix up a human cocktail for me? I want something to drink with these delicious bread sticks."
        c "I'd love to, but did you happen to buy any liquor on your shopping spree? I didn't see any in the kitchen."
        Nm normal "Yeah, I bought a bottle of something at the store that was recommended to me by the clerk. It's hidden in the fridge's door compartment."
        c "Alright. I'll look at what other cocktail ingredients you have and make the best one I can come up with."
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
    m "(Let's now focus on getting the noodles ready.)"
    m "(Luckily, the water inside the teapot was still hot enough for the noodles.)"
    play sound "fx/pour.ogg"
    m "I emptied the entire pack of noodles into a pot and then poured in some hot water from the teapot."
    m "(I should have enough time to finish the rest of the ingredients while the noodles cook.)"
    play sound "fx/faucet2.ogg"
    queue sound "fx/veggies.ogg"
    m "I washed some of the more familiar-looking vegetables and held them in a neat pile on the cutting board, and then used my knife-work to turn them into pieces of various sizes."
    play sound "fx/crapcuttingboard.mp3"
    m "After finishing up, I meticulously cut the cheese I had selected previously into same-size bits."
    play sound "fx/faucet1.ogg"
    queue sound "fx/faucet2.ogg"
    m "The noodles were ready now, so I took a pot lid and used it together with the pot to carefully pour all the hot water into the sink. Then I poured in some cold water stop the cooking process."
    m "Unfortunately, I didn't have a free cooktop so frying the noodles would have to wait. I poured some olive oil in the noodle pot to make sure the noodles wouldn't stick together."
    
    if naomi1drink == "cocktail":
    
        stop sound fadeout 1.0
        m "(There's enough time to make the cocktail in the meantime.)"
        play sound "fx/crapfridge.mp3"
        m "I took the liquor bottle from the fridge's door compartment and inspected what I had to work with. The bottle's sunny and cheerful-looking label read 'sugar cane liquor'"
        m "(I have an idea what this might compare to. Still, I should probably taste it first.)"
        play sound "fx/uncork.ogg"
        queue sound "fx/pouringwineshort.ogg"
        $ renpy.pause (1.0)
        queue sound "fx/coffee.wav"
        m "I poured some in a glass and drank it in one go."
        play sound "fx/glassdown.wav"
        m "(Tastes like blonde rum.)" 
        m "(To be safe, I'll make something that doesn't taste too different from what I had at Adine's.)"
        m "When looking for additional ingredients, I quickly figured out what cocktail to make as I spotted some limes. As another ingredient I needed simple syrup made with brown sugar, but making that yourself was extremely easy."
        m "(Melting brown sugar will take even less time than normal because I have hot water to speed up the process. Unfortunately, there's only two cooktops.)"
        m "(I think I can take the chicken off for a few moments for the melting.)"
        play sound "fx/pouringwineshort.ogg"
        m "To dissolve the brown sugar, I measured two parts of it and one part of hot water and poured both onto a third pan. Then I took a potholder, put it on the kitchen counter and moved the hot chicken fillet pan on it." 
        play sound "fx/metalbox.ogg"
        #Mixing sound?
        m "Lastly, I quickly grabbed the simple syrup pan and put it on the heat. After not too much time aided by mixing, the simple syrup was ready."
        play sound "fx/pouringwineshort.ogg"
        queue sound "fx/metalbox.ogg"        
        m "I poured the syrup into a large heat-resistant glass. Then I turned the chicken in the chicken pan and put it back on the cooktop."
        play sound "fx/crapcuttingboard.mp3"
        #Juicer sound?
        m "To follow up on the cocktail, I cut some limes in half and juiced them into some delicious, fresh lime juice."
        play sound "fx/cabinet.ogg"
        queue sound "fx/pouringwineshort.ogg"     
        m "Next to chill the cocktail, I luckily found a dragon-sized cocktail shaker in the first cabinet I opened. I poured roughly three portions of fresh lime into the shaker through a sieve."
        m "(Since Naomi seems to be skittish of alcohol, I should be careful with the alcohol content. Better to play it safe, as always.)"
        play sound "fx/cabinet.ogg"
        m "I inspected one of the same types of glasses I had served her juice in."
        m "(She's like two to three times as big as I am, so two portions of alcohol in around a half a liter cocktail should only give her a slight buzz, even if she drank it all in one go.)"
        queue sound "fx/pour.ogg"
        m "I measured two portions of liquor and six portions of simple syrup and poured them into the cocktail shaker."
        play sound "fx/crapfridge.mp3"
        m "Next I opened Naomi's freezer, took some ice and added some in."
        #Shaking sound also?
        play sound "fx/stir.ogg"
        m "I shook the shaker for a short time and poured the cocktail into the large glass, again through a sieve. Finally, I added two straws and used a spoon to do a taste test."
        c "(That's a pretty sweet version, just the way I like it. You can barely taste the alcohol, so I bet Naomi will like it as well.)"
        scene ecknaomiapt03 with dissolvemed
        show naomi normal with dissolve
        play sound "fx/glassdown.wav"
        m "Naomi was intently focused on watching the series so she only noticed me after I had placed the cocktail on the table in front of her."
        #Expand the conversation below
        Nm confused "Oh, hey."
        c "Here's the cocktail you ordered. Enjoy."
        Nm normal "Thanks."
        queue sound "fx/coffee.wav"
        m "Naomi craned her head towards the glass and drank some of the cocktail through the straws."
        Nm smile "It's pretty good! Good job, [player_name]."
        c "I'm happy to hear it. If you'll excuse me, I have to go back to the kitchen. We can talk more after I have brought the rest of the food."
        show naomi normal with dissolve
        play sound "fx/dishes.wav"
        m "Naomi had resumed focusing on the series, so I just grabbed the empty appetizer plate from the table and went back to the kitchen to continue cooking."
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
        Nm smile "Thank you, [player_name]." #Expand
        c "If you'll excuse me, I have to go back to the kitchen."
        play sound "fx/dishes.wav"
        m "Naomi had resumed focusing on the series, so I just grabbed the empty appetizer plate from the table and went back to the kitchen to continue cooking."
        scene ecknaomiapt02 with dissolvemed
        
        play sound "fx/pour.ogg"
        queue sound "fx/chug.wav"
        queue sound "fx/glassdown.wav"
        m "Feeling thirsty from the heat of the kitchen, I emptied the carton of juice into a glass and drank it. There was nothing to do for now, so I waited for the chicken to be ready."
    
    $ renpy.pause (2.0)
    play sound "fx/beeps2.ogg"
    m "After dropping off the appetizer plate at the sink, the timer signaled that the first batch of chicken breasts were ready. I moved them from the pan onto a serving plate, added in the unfried chicken and set the heat higher again."
    play sound "fx/beeps2.ogg"    
    m "After that was done, another timer beeped to tell me that the potatoes were ready."
    m "(Somehow, I've timed this almost to perfection.)"
    play sound "fx/metalbox.ogg" 
    m "To continue making the mashed potatoes, I lifted the boiling pot off the cooktop onto a potholder and added the noodle pan in."    
    #Sound?
    m "After that I took a lid and used it together with the potato pot to pour all the hot water into the sink. Then I grabbed a masher from one of the drawers and proceeded to mash the potatoes."
    play sound "fx/pour.ogg"
    m "After I had mashed for a short time, I poured in some milk."
    m "(That should be enough for now. It's better to be careful to not use too much milk at first because you can always add more later. If you add too much the mashed potatoes will become soggy, like a thick soup.)"
    play sound "fx/crapcuttingboard.mp3"
    m "Then, when I had mashed for a bit longer I opened one of the packages of butter on the counter, cut a lot of large chunks from it and added them to the almost ready mashed potatoes."
    m "To finish off, I mashed a little bit more and finally mixed the entire thing with a scoop and left it in the pot ready for serving."
    play sound "fx/fry.ogg"
    queue sound "fx/salt.ogg"
    m "After that, it was time to turn the chicken. When that was done, I tasted the mashed potatoes, decided to add some salt and tasted it again."
    m "(Perfect. Now on to the next thing.)"
    m "I added a lid to the pot of fresh mashed potatoes to preserve some heat and moved on to fry the noodles."
    m "(Oh well. I suppose olive oil will have to do, because I don't feel like searching for anything.)"    
    play soundloop "fx/fry.ogg"
    m "To start off, I poured some olive oil into the already hot enough frying pan and used my hands to add in the cold noodles."
    play sound "fx/salt.ogg"
    m "Then finally after mixing the noodles a bit, I added in the cut vegetables, cheese and the spices and sauces I had selected earlier."
    m "(That looks pretty good already.)"
    $ renpy.pause (2.0)    
    m "(Actually, let's put in some giant prawns as well, because I love the crunch. Luckily for us, they're already prepared and seasoned.)"
    m "After adding the giant prawns I mixed the noodles again, put on the lid and set yet another timer."
    stop soundloop fadeout 1.0
    m "(Now I'll just have to remember to mix the noodles every once in a while so they cook somewhat evenly.)"   
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
    m "I opened a pack of bacon and sliced some bacon into smaller pieces. Then I took two dragon paprikas, cut all the extra bits off and sliced them too."
    play sound "fx/pour.ogg"
    queue sound "fx/stir.ogg"
    m "As the next order of business I made some omelet mix from a bunch of eggs and milk."
    play sound "fx/faucet1.ogg"
    queue sound "fx/rub1.ogg"
    queue sound "fx/veggies.ogg"
    queue sound "fx/fry.ogg"
    m "After that I took two large potatoes, rinsed them, peeled them and cut them into slices. Then I mixed the noodles again before figuring out what to do next."
    stop sound fadeout 1.0
    m "(I still got some time left before the chicken is ready, so how about a sauce? I think there's a good one I can make from what we have. It'll need a cooktop of course, but I can prepare the ingredients while one frees up.)"
    play sound "fx/pour.ogg"
    queue sound "fx/veggies.ogg"
    m "As preparations for making the sauce, I mixed some white vinegar and water and peeled and cut two onions. Then I separated the yolk from a bunch of eggs and made a bain-marie from a metal bowl and the pot I had used previously."
    play sound "fx/faucet1.ogg"
    queue sound "fx/button_unpress.ogg"
    m "I needed more hot water for this contraption so I poured some more into the electronic teapot and turned it on."
    m "(There's still some time left on the chicken but I probably should take it off to not waste time. They should be ready anyway.)"
    play soundloop "fx/fry.ogg"
    m "I placed the rest of the chicken onto the serving plate, and spread the bacon and potatoes evenly in the same pan to fry for the omelet."   
    m "(Again, I have some time left before the bacon is fried. I should stop inventing new things to cook already, so I'll just start cleaning up what I can, in case we feel too tired to do it after eating.)"
    stop soundloop fadeout 1.0
    play sound "fx/rummage.ogg"
    queue sound "fx/crapfridge.mp3"
    queue sound "fx/cabinet.ogg"
    queue sound "fx/faucet1.ogg"
    m "To clean up, I first put back everything I had taken but not used, back to where they were before. Then I cleaned up all the trash and empty packaging into the garbage can. After that I placed all the dirty kitchen equipment into the sink and rinsed them."
    m "(Unfortunately Naomi doesn't have a dishwasher. I'll have to wash the dishes more thoroughly later, because I really don't feel like washing them properly right now.)"
    play sound "fx/crapspraybottle.mp3"
    queue sound "fx/wipe.ogg"
    m "I finished my tidying-up operation by spraying some cleaning liquid on the kitchen counters and wiping them clean."
    play sound "fx/fry.ogg"
    m "Then I noticed that by now the bacon and potatoes were ready enough, so I added in the omelet mix and paprikas. Wanting to do a good job, I also mixed the noodles again."
    stop sound fadeout 1.0
    m "(The omelet might take a while, but we can just eat it for dessert because it's not going to burn on low heat.)"
    m "I started looking for some tableware for serving the food."
    play sound "fx/cabinet.ogg"
    m "(That large bowl looks perfect for the fried noodles. Also, she also has a saucière for convenient sauce-pouring. Why does she have one if she doesn't cook herself?)"
    play sound "fx/dishes.wav"
    queue sound "fx/crapfridge.mp3"
    m "To prepare, I took the bowl, the saucière, some plates, utensils, glasses, napkins and another carton of juice and placed them in a neat order on the kitchen counter, ready for when I would carry them all into the living room."
    m "(Almost there. The noodles should be fried enough now.)"
    play sound "fx/fry.ogg"
    queue sound "fx/faucet1.ogg"
    queue sound "fx/wipe.ogg"
    queue sound "fx/metalbox.ogg"
    m "I used pasta tongs to lift the fried noodles from the pan into the bowl and stuck two dragon-sized forks in the noodles for me and Naomi.  Then I quickly rinsed and wiped the pan and put it back on the cooktop."
    m "To continue making the sauce, I poured my water-vinegar in the pan and added the cut onions."
    m "(Reducing the water, vinegar and onions into the flavor broth is going to take a minute. I guess I will have to wash the dishes after all. Oh well.)"
    play sound "fx/faucet1.ogg"
    queue sound "fx/dishes.wav"
    queue sound "fx/rub1.ogg"
    queue sound "fx/wipe.ogg"
    m "I begrudgingly washed all the dishes I could at the time. Sadly, we would have to wash some more after eating."
    m "After I had finished washing the dishes, the flavor broth was ready because the ingredients in the pan had reduced to half their volume. I poured it into a heat-resistant glass through a sieve."
    m "Then I took my self-made bain-marie and put it on the cooktop. The water in it started boiling after a few moments, so I added the egg yolks into the bowl and whisked to break them up. The broken yolks started heating up almost immediately, so I started slowly pouring in the flavor broth and whisked even more furiously."   
    m "I kept whisking rapidly until the sauce was even, and then started adding butter bit by bit. When that was done, I seasoned the sauce with tarragon, white pepper, sugar and salt. Finally, I had to let it sit for it to thicken, so I took a small break."
    m "(My arm is tired from the whisking. Worth it though, because I really like this sauce.)"
    m "I emptied the sauce from the bowl into the saucière with the help of a scraper and placed it on the kitchen counter with the rest of the food that was ready to be eaten."
    m "(I can turn the omelet after I have carried all the food to Naomi. Other than that, looks like we're about done here.)"
    m "When I reflected on what I had made, I thought it was a really good meal, even if I said so myself." 
    m "Eight breaded chicken fillets filled with herb butter, a pot full of mashed potatoes, a lot of fried noodles, a delicious sauce and a bacon potato omelet. I only hoped now that Naomi would like everything I had cooked." 
    m "Of course, there was a very small chance of me failing to please Naomi because I was a decent cook, but I still had a small lingering fear that made me dread even the slightest possibility of letting her down."
    m "(I should probably carry all this to the living room all by myself. We don't want Naomi to trip and make a mess, do we?)"
    scene black with dissolvemed
    play sound "fx/dishes.wav"
    m "It took me three trips in all to bring all the food and required tableware into the living room, where we would eat."
    scene ecknaomiapt03 with dissolvemed
    show naomi surprised with dissolve
    m "After I was done, I sat down next to Naomi, and I noticed that she had turned the series off and was instead eyeing all the food I had brought with a curious and hungry look."
    c "Please use the the fork at least for the fried noodles. Otherwise the grease and sauces from the frying will be everywhere."
    Nm blank "If I make a mess you can just clean up for me later, right?"
    c "I would like to avoid any unnecessary work. In fact, if you have any questions or need help plating I'll be happy to accommodate you in that front as well."
    show naomi normal with dissolve
    c "Also use the scoop for the mashed potatoes. Even though we have swapped bodily fluids, I don't want your saliva in my food."
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
    m "I began by taking a huge chunk of the fried noodles with my fork and stuffing some into my mouth."
    Nm "This chicken is so delicious! I especially like the crunchiness."
    c "Same. I love the taste and texture of batter, so I breaded it twice."
    Nm surprisedblush "Actually, even more than the crunchiness I love how the herb butter just bursts inside your mouth when you bite in."
    c "They are indeed a lot juicier than your basic chicken breasts. It must also be a different experience for you because you can eat it whole like that but I can't."
    Nm normal "You're already starting to sound like an expert on how to plan meals for hungry dragons."
    c "Well, I am certainly planning to hone that skill even further, for both of our sake."
    Nm smile "You have no idea how much I am looking forward to that, [player_name]."
    c "You and me both. By the way, I have to go turn the omelet that's still cooking in the kitchen."
    Nm surprised "You're making even more food?"
    c "Well, I didn't want to sit around doing nothing so I used my time as efficiently as possible. I'll be back in a minute."
    scene black with dissolvemed
    hide naomi with dissolve
    play sound "fx/metalbox.ogg"
    m "I went back to the kitchen and used a plate and a potholder to turn the omelet. It was a bit difficult because the equipment, especially the pan was big, but I managed to do it without causing a mess."
    scene ecknaomiapt03 with dissolvemed
    show naomi normal with dissolve
    play sound "fx/eating.wav"
    m "After I came back, we started quietly diving into both of our servings."
    $ renpy.pause (4.0)
    c "So, care to tell me how you have so much kitchen equipment, if you don't cook at home? A sauce-boat like that for example, isn't very common to have around."
    stop sound fadeout 1.0
    Nm blank "My parents bought me most of the stuff. I told them about my skipping meals and overworking predicaments so they encouraged me to start cooking myself."
    Nm confused "To them, it seemed like a perfect way of killing two birds with a single venom spit: to have me do something other than just police work and make sure I eat more regularly." 
    Nm concern "After getting a bunch of of kitchen equipment, looking through some cookbooks and watching some cooking and traveling shows, I thought I was ready to learn how to cook."
    Nm sad "Needless to say, if you've paid any attention to what I've told you, you probably already guessed it didn't go well. I broke some of the equipment and made such a mess, that I had to pay the cleaning services to come and clean up my kitchen for me."
    c "I suppose it just wasn't your thing. You don't have to be great at everything, so don't worry about it."
    c "Always remember that you're already very good at a lot of things, for example analytics, swimming and flying. Besides, now you have me to cook for you."
    Nm smile "You're right. Thank you so much for comforting me, [player_name]."
    play sound "fx/eating.wav"
    m "I nodded, since my mouth was full of fried noodles, and Naomi resumed eating as well."
    show naomi normal with dissolve
    $ renpy.pause (4.0)
    m "After eating enough fried noodles I scooped some mashed potatoes onto my plate, placed a fried chicken fillet in the middle and poured some sauce on it. Then I cut through the fillet, releasing the delicious herb butter into the mix."
    m "I cut the fillet into several smaller pieces. I spread some sauce, herb butter and mashed potatoes on a piece and ate it. It was superbly delicious, with a nice crunchy texture and juiciness to boot."
    c "You should try the chicken with the sauce I made. Let me pour some for you."
    show naomi surprised with dissolve
    play sound "fx/chug.wav"
    m "I took the saucière and poured some of the thick, buttery and slightly bitter sauce on one of the breaded chicken fillets."
    c "There you go."
    m "After eyeing the chicken hungrily the entire time I had been pouring the sauce, Naomi picked it up with the tips of her claws and proceeded to toss it in her maw. Surprisingly, she didn't make a mess, even though the chicken was coated in sauce."
    play sound "fx/pizzabite.ogg"
    Nm surprisedblush "Just wow. Why didn't I try this sooner?" 
    Nm smile "I'm starting to really love human cuisine. It's so familiar but yet a little bit different."
    c "The sauce also works well with mashed potatoes, so you should definitely add it there too."
    play sound "fx/chug.wav"
    m "Naomi happened to be running out, so I scooped some mashed potatoes on her plate and poured some of the sauce on top."
    c "Enjoy."
    Nm "Thank you, [player_name]."
    show naomi normal with dissolve
    m "This was a good break as any, so I decided to go get the potato and bacon omelet. It had surely been ready for some time now."
    hide naomi with dissolve
    scene black with dissolvemed
    play sound "fx/metalbox.ogg"
    m "I turned the heat off, slided the delicious omelet onto a serving tray and brought it back to the living room along with a cake knife."
    scene ecknaomiapt03 with dissolvemed
    show naomi surprised with dissolve
    c "We're having this for dessert."
    Nm shy "You've made so much food, [player_name]. I don't know what to say."
    Nm smile "Thank you so much for this wonderful evening."
    show naomi normal with dissolve
    m "I cut a quarter of the potato omelet with the cake knife and lifted it on Naomi's plate. Feeling a bit full already, I only cut one eight for myself."
    m "The potato and bacon omelet exceeded my expectations: it was moist but at the same time crisp in some places. On top of that the saltiness wasn't overpowering, and it was also slightly sweet due to the dragon paprikas I had decided to add."
    Nm "This omelet is great too. I think I might be warming up to keeping you around a bit longer."
    c "Thanks, Naomi. I'm really happy to hear that."
    Nm shy "But seriously, how did you become such a master chef? I don't think I would ever be able to create a meal like this."
    c "Actually I would call myself pretty much an amateur, because the best food isn't usually overly complicated to make. In my opinion it's better to just focus on using good-quality ingredients and learning recipes for food that most people like to eat." 
    Nm normal "I see. I guess none of these dishes are that complicated when I think about it."
    c "That's why I call my style of cooking simple but delicious. This philosophy leaves more time for eating."
    Nm smile "I love that idea. Eating is of course the most important part."
    c "Now when I think about it, there was also some luck involved in creating our delicious meal. You managed to buy decent ingredients, even though you're not that good at cooking."
    c "By the way, how'd you like the fried noodles?"
    Nm normal "I hope I'm not boring you but I have to say that it was really good, like everything else. I especially liked the different textures it had. Too often people make boring versions of that dish."
    c "Yeah, those prepared giant prawns you bought were a really great pick. I honestly have to give you credit as well."
    m "I looked at Naomi's plate and she had some mashed potatoes with a breaded chicken fillet on top, but it was missing the sauce."
    c "Do you want some sauce?"
    Nm concern "Thank you. I don't think my claws are nimble enough to operate that sauce boat."
    play sound "fx/chug.wav"
    show naomi smile with dissolve    
    m "I poured some sauce for Naomi and since it seemed that we had run out of interesting topics to talk about we continued eating silently until we were both completely full."
    m "I had to pace my eating to be a lot slower than Naomi's since she could eat a lot more than me. After we had stopped eating, there was still a good amount of food left over."    
    show naomi normal with dissolve
    c "What a meal, even if I say so myself."
    Nm smile "Yeah, it was great. I hope you're not getting bored of me constantly complimenting you."
    c "I would never get bored of that. Just remember that there's ways for you to pay me back."
    Nm shy "If you're hinting at what I think you are, do you realize I've stuck a far better bargain than you have since I enjoy having you in bed as well?"
    c "Our feelings go both ways, I enjoy cooking for you."
    Nm blank "Oh well. You got me there."
    Nm normal "By the way, looks like you cooked too much because we couldn't eat everything."
    c "That's fine, because you can take some of the food to work so you don't have to work while hungry. I'm sure a lunch break won't take too long if you don't have to go to a café to eat."
    Nm smile "Do you think that you cooking food for me to eat at work might become a regular occurrence?"
    c "Sure, if you decide to keep me around."    
    c "Actually, I'll go put the leftovers in the fridge right now. Do you think you can wash the dishes later though? I really hate doing that because it makes my hands go dry."
    Nm normal "Sure, I can manage that."
    scene black with dissolvemed
    hide naomi with dissolve
    play sound "fx/crapfridge.mp3"
    m "In two trips, I placed what was left over into Naomi's fridge so she could eat them tomorrow."
    scene ecknaomiapt03 with dissolvemed
    show naomi normal with dissolve
    m "When I came back, Naomi was lying on the sofa, looking tired."
    $ persistent.sqbnaomi2cook = True
    
jump sqb_naomi_m2_ending
 
label sqb_naomi_m2_ending:
    
    c "Such a good meal calls for a rest. Can I come lie next to you?"
    Nm smile "I would love that a lot. I think you deserve a reward for the hard work you did in the kitchen for me."
    play sound "fx/sheet.wav"
    m "I got up on the sofa, laid down sideways next to Naomi. When I had settled in place, she put her arm around me."
    Nm shy "You are so cute, [player_name]."
    c "Mmh..."
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
    c "Also, similar sentient species usually developing along the same lines probably has something to do with it."
    Nm shy "Now that's a point I agree with. I'd like to add that our species are very similar since we're able to have a romantic relationship with each other."
    c "Hey, don't forget about our differences. I think we will make a great team due to them. All in all, interacting with other sentient species is a very exciting time."
    Nm normal "Likewise." 
    c "Anyway, I think I ate way too much. Do you mind if I take a short nap for about half an hour?"
    Nm smile "Not at all. I will keep you safe."
    play sound "fx/bed.ogg"
    stop music fadeout 1.0
    hide naomi with dissolve
    scene black with dissolvemed
    m "Naomi shifted her wing over me. I quickly fell asleep with her as my backrest and blanket."
    m "I felt satisfied and at peace with Naomi at my side. This had been a very good day."
    scene ecknaomiapt03 with dissolvemed
    play sound "fx/lewd/lickslow.ogg"
    m "Just as I had closed my eyes, I woke up to someone nudging the side of my head with their snout and gently kissing my cheek."
    play music "mx/airborne.mp3" #Different music?
    show naomi smile with dissolve
    Nm "Time to wake up."
    play sound "fx/sheet.wav"
    show naomi normal with dissolve
    m "After I had gotten up from the sofa, I noticed it was already very late. I'd stayed for much longer than I'd initially planned for."   
    Nm normal "It's getting very late, so maybe you should get going. Even though my vacation is coming up, I shouldn't stay up too late."
    Nm smile "Unless you want to sleep together with me?"
    c "I can't, sorry. There's some material I have to go over at my apartment tomorrow morning. I have a feeling if I stay the night I won't have any time for that."
    c "Let's just call it a day. We can continue some other time."
    Nm normal "That works for me. We got lots of time to be together, right?"
    Nm confused "Oh, I knew I had forgotten something. I was initially going to buy some supplies after escorting you home, but all the shops have already closed."
    c "That's very unfortunate. You can always do that tomorrow though."
    Nm blank "Yeah, it's not a big deal. I'll escort you home regardless."
    Nm smile "I have to say that we had an excellent time. I'm not very used to having people come over, but this evening was a resounding success."
    Nm normal "Thank you so much for your company, [player_name]."
    c "I had a great time as well. Actually, didn't you just say you had a vacation coming up? Want to meet again then?"
    Nm smile "How considerate of you to suggest that. I might have just the idea on how to make our time together more interesting. I can't tell you right now what it is though, because it's a secret."
    Nm normal "Let's get going already, I'm starting to get pretty tired."
    hide naomi with dissolve
    scene ecknaomiapt01 with dissolvemed
    $ renpy.pause (0.5)
    m "We walked up to the main door and stopped for a moment while Naomi was fiddling with the lock."
    show naomi blank with dissolve
    Nm "I still can't get used to the cursed thing."       
    play sound "fx/door/lock.ogg"
    $ renpy.pause (0.5)
    play sound "fx/door/handle.wav"
    $ renpy.pause (1.5)
    show naomi surprised with dissolve
    m "Upon opening the door, however, we were greeted by Sebastian idly sitting on a couch and leaning back with his eyes shut."
    Nm normal "Seb? What are you doing here? I thought I was the one responsible for [player_name] for today."
    show naomi normal flip at left with ease
    show sebastian normal b at right with easeinright
    Sb smile b "You can't be responsible for any assignment after your shift is over, Naomi."
    Nm shy flip "Oh, right."
    Nm normal flip "Why didn't you let me know that you're here? There's enough room for all three of us."
    Sb "I'm still on the clock, so I decided to patrol the area. I only sat down here to take a breather while guarding your outer door."
    Nm blank flip "How nice of you. Still, you should have at least let us know you were there."
    Nm normal flip "I was just about to escort [player_name] back to their apartment. Care to join us?"
    show naomi blank flip with dissolve
    Sb disapproval b "Naomi, your shift is over, so go get some rest. I'll escort [player_name] instead since I am still working."
    c "Sure. Thanks, Sebastian."
    Nm smile flip "I suppose this is it for today, then. I'm so looking forward to your next visit, [player_name]."
    c "Me too. Bye, Naomi."
    show naomi surprisedblush flip with dissolve
    m "As I was starting to move, I noticed Naomi looking first at me and then at Sebastian. She was clearly up to something."
    show sebastian shy b with dissolve
    show naomi smile flip with dissolve
    play sound "fx/kiss.wav"
    queue sound "fx/lewd/lickslow.ogg"
    m "Then, after a moment's hesitation, Naomi embraced and tongue kissed me like back when we had been together. After she was done with me, she winked at Sebastian."
    m "(Looks like she's starting to be less shy about openly showing she likes me.)"
    Nm smile flip "Don't keep me waiting, [player_name]!"
    c "I won't. See you, Naomi."
    $ renpy.pause (0.5)
    stop music fadeout 2.0
    play sound "fx/door/door_close.ogg"
    queue sound "fx/steps/slowstepsdown.ogg"
    hide naomi with dissolve
    hide sebastian with dissolve
    scene black with dissolveslow
    m "We exited outside through the dark hallway with Sebastian. He didn't comment at all at Naomi's sudden show of affection towards me."
    stop sound fadeout 2.0
    scene eckdarkpathway with dissolveslow
    play soundloop "fx/steps/steps.ogg"
    $ renpy.pause (0.5)
    show sebastian smile b with dissolve
    m "After we had walked for a bit, he finally decided to bring it up."
    Sb smile b "So, you two did it?"
    c "Yes, we had a great time together."
    Sb "I'm so happy for Naomi, and for you too of course. She deserves a good boyfriend who will do right by her."
    c "Thanks, Sebastian. I really appreciate it."
    
    if modinfo.has_mod("BangOk?") and bangok_four_xsebastian_unplayed == False:
        Sb shy b "You know...{w} umm..."
        Sb "Since we've already had sex, is there any chance I could join with you and Naomi? You know what they say: the more the merrier."
        c "I wouldn't mind that, so it's up to her. She did call you cute and she also said she likes smaller partners, so there's a chance she might agree to it."
        Sb smile b "That's wonderful news."
        Sb drop b "I'll ask her when I've mustered up the courage."
        c "Cool."
        
    hide sebastian with dissolve
    scene np5e with dissolveslow
    show sebastian normal b with dissolve
    stop soundloop fadeout 2.0
    m "After some time, we finally made it to my apartment. I was dead tired."
    c "Thanks for escorting me Sebastian. You're as dutiful as ever."
    Sb smile b "See you, [player_name]."
    hide sebastian with dissolve
    play sound "fx/door/handle.wav"
    queue sound "fx/door/door_close.ogg"
    scene o3 with dissolveslow
    $ renpy.pause (2.0)
    scene black with dissolveslow
    m "I dropped on my bed with my clothes still on, and fell asleep almost immediately. This had without a doubt been the best day of my entire life."
    m "When I woke up, I couldn't remember the last time I had slept this well."
    
    $ renpy.pause (0.5)
    $ persistent.naomi2skip = True
    $ naomiscenesfinished = 2
    
jump ml_date_end  