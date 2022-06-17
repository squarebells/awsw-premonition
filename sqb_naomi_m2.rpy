label sqb_naomi_m2_foodskip:
    
    stop music fadeout 1.0
    play sound "fx/system3.wav"
    s "A lot of reading ahead. Would you like to skip the cooking and eating?"
    menu:
        "Yes":
            s "Alright."
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

jump sqb_naomi_m2_foodskip_end

label sqb_naomi_m2_chairs:

    $ renpy.pause (0.5)
    $ naomi2mood += 2
    $ naomilewd +=1
     
    Nm surprised "You mean right now?"
    c "Sure, if they bother you that much. I'd love to help you out."
    c "I think I am better suited for moving furniture around than you are, no offense."
    Nm normal "None taken. Thank you for the offer, but I want to host you, not put you to work."
    Nm blank "I'll do it myself tomorrow."
    Nm "Enough about my chairs. Let's go rest on the sofa."
    scene ecknaomiapt03 with dissolvemed

jump sqb_naomi_m2_chairs_end

label sqb_naomi_m2_differences:

    c "For example, have you ever considered how big you are compared to a human? If you hugged someone like me, you'd make them feel better in no time."
    show naomi surprisedblush with dissolve
    m "(Why did I say that?)"
    Nm shy "That's a very...{w} interesting point."
    Nm smile "I bet if I caught a puny human like you, they'd never be able to escape my clutches."
    c "That's what dragons sometimes do to humans in our fiction."
    show naomi confused with dissolve
    c "Although, usually the dragons who deal with humans are assumed male, and most of the time they only catch humans of the female sex."
    Nm concern "That makes no sense at all to me. Female dragons are just as strong as male dragons." 
    Nm shy "Actually, I'd be really interested in hearing why dragons are usually assumed to be male in your fictional stories."
    c "Well, I didn't really study literature or specialize in cultural history so I don't know for certain."
    m "I had a sudden urge to say something funny."
    c "Now that I think about it, I agree with you that our dragon trope makes no sense. I'm sure there are a lot of male humans who wouldn't mind being caught by a dragoness."
    Nm confused "I hope you know that I was just being hypothetical."
    c "Yes, of course."
    show naomi blank with dissolve
    c "Anyway, as a sociologist the most fascinating thing about our species' future relationship is how we could complement each other."
    c "Similarly to how your different species of dragons are best suited for different kinds of tasks."
    c "Compare humans to runners for example. I know that runners are decent at doing tasks that require precision, but humans are way better. Our limbs are much better suited for articulate tasks than anything you've ever seen before."
    show naomi normal with dissolve
    c "Like I implied before, I wouldn't mind moving a few things for you, because it's much easier for me."
    show naomi surprised with dissolve
    c "Then as a sign of reciprocity you could fly me across town or something, if you are comfortable doing that."
    show naomi shy with dissolve
    c "How long does flying across the town even take you?"

jump sqb_naomi_m2_differences_end

label sqb_naomi_m2_balcony:

    c "Coming on the balcony was a great idea. I really love feeling the sea air again." 
    c "It's been a long time since I've been able to visit a seaside beach because our city-state is in middle of a desert. Wandering outside the walls is very dangerous so we don't do any recreational trips."
    Nm confused "That's very unfortunate. Why would anyone want to live in the middle of a desert?"
    c "It's not really our choice. Most of us had to settle within a reasonable distance in a place where at least some of the infrastructure was intact."
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
    c "Anyway, in addition to the fresh sea air I really like the view as well."

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
    c "Also, we used our technology to automate most tedious and difficult jobs in order to have more time to do what we actually wanted to do with our lives, like things related to hobbies or simply just improving ourselves."
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
    Nm blank "I've never heard of that genre, although I can guess what it's about. It sounds amazingly interesting."
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
    c "In his case, there wasn't really any kind of process to select the most suitable person to go since we were desperate for any kind of help or even information. I have to admit that we didn't really care if he died on the mission."
    c "This was because Reza was known to be a troublemaker, so him dying really wouldn't have been big loss. You wonderful dragons could have been savage, man-eating monsters for all we knew at the time."
    Nm smile "You've seen nothing yet. Just stick around for long enough and I might show you all of my abilities."
    m "Naomi's remark almost made me jump up from the sofa. I managed to mostly control myself but I'm sure she noticed me twitch and shift my position."
    c "I... uhh..."
    m "She winked at me and licked her lips."
    c "Where was I..."
    show naomi normal with dissolve
    c "Anyway, I was selected from a large pool of applicants to be the second person to visit your world. Due to my expertise in both biology and sociology I was uniquely qualified."
    c "Sending someone takes a lot of power so it'll just be me and Reza interacting with you until we get one of your generators."
    c "Reza's behavior leaves a lot to be desired." 
    c "Well... that would be the understatement of the century, if he is indeed guilty. Murdering someone is unforgivable even in our harsh society."
    c "I hope we catch him soon and find out the truth so we can end this mess."
    Nm smile "I hope so too. We need to get this murder mystery over with because I want to meet more cute humans and say we'll welcome all of them with open arms."
    m "(She really seems to like my species a lot.)"
    c "Naomi, you and the other dragons I've met have been much nicer to me than I could have ever anticipated."
    c "I really don't know what to say. You caring about me and my people this much makes me feel very happy."
    m "Suddenly I started to feel another surge of emotions. My throat started feeling dry and I wanted to cry."
    show naomi surprisedblush with dissolve
    c "Your unconditional kindness towards us is somewhat unexpected, because I don't know what we did to deserve it. Being as dependent on technology as we were wasn't good, so the mess we're in is kind of our own making."
    Nm stern "Don't say that. Everyone needs help sometimes."
    Nm confused "Just make sure you have good friends..." 
    Nm smile "...or something more to help you out."
    play sound "fx/sheet.wav"
    m "Naomi moved a bit closer towards me on the sofa."
    c "Thank you again, Naomi. I really mean it."
    m "She leaned yet a little bit closer. Since she was a lot bigger than me, I started feeling a little intimidated but also intrigued."
    Nm shy "Would you like a hug? I don't want to see a cute little human like you sad like this ever again."
    m "(She's right, I really need a hug right now.)"
    m "Also, I already liked her a lot and turning down her offer would have been rude."
    c "Uhh...{w} sure."
    stop music fadeout 1.0
    show naomi slsmile with dissolve
    play sound "fx/sheet.wav"
    m "With that, Naomi leaned in and I returned the gesture by wrapping my arms around her upper body."
    m "Naomi was softer and cuddlier than I had expected. After I had been feeling her for a moment, she secured me in place by hugging me with her arms behind my back."  
    m "Since this was our first time, I was surprised when I felt her strong breathing."
    m "(I suppose an aquatic dragon needs strong lungs to be able to stay underwater for extended periods of time.)"
    Nm smile "Are you feeling any better yet?"
    c "Yes, thank you very much." 
    c "Hugging a big dragoness such as you is certainly a new experience for me. I don't know what to say."
    play sound "fx/sheet.wav"
    m "After the hug, I tried to politely disentangle myself from Naomi, but she wouldn't let me go."
    Nm confused "What's wrong?" 
    Nm slsmile "Let's stay like this so you won't feel sad while you finish your story."
    c "Sure, that works for me."
    c "Anyway to continue..."
    show naomi normal with dissolve    
    c "Like you already know, our most important goal is to get one of your generators."
    c "A lot of tech, especially advanced medical equipment was spared in our city. The problem is that soon we won't have enough power to run it properly."
    c "I just hope my city-state is still standing when it's time for me to return."
    show naomi blank with dissolve
    stop music fadeout 1.0   
    m "As I said that I was hit by the sudden realization that I might not be able to come back here after I had completed my mission. After all, given the precarious situation we were in, who would care about researching dragon society and culture?"
    play music "mx/flashback.ogg" 
    m "Because of this realization, it was the first time when thinking about having to return made my stomach feel like an endless pit of suffering. An immediate feeling of panic was surging up in me, so I had no choice but to confide in Naomi to ease it off even a little bit."
    Nm concern "Something wrong?"
    c "Sorry, I got lost in thought."
    c "Anyway, I hate to admit that I am not looking forward to the day when I finally have to go back to my own world."
    c "How should I put this..."
    c "Sticking together and working for the greater good has kept my people alive so far."
    show naomi confused with dissolve
    c "Because of the contradiction between this and my own preferences, I suddenly have a weird feeling of dread and helplessness." 
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
    m "Also, I didn't want to disappoint Naomi by declining her so I made the final decision to accept what she had suggested twice already." 
    m "It probably took her a lot of courage to ask me yet again, considering her usually shy and reserved demeanor."
    Nm confused "Well?"
    stop music fadeout 1.0
    c "I suppose you are right. I'll still have to make a formal request though, but I don't see why it would be declined if I explained myself well enough."
    show naomi normal with dissolve
    c "Thank you again, Naomi. It seems that your advice is always really thoughtful."
    Nm smile "So it's settled then. You'll stay here with me and so I can keep you safe forever."
    m "Before I could think of a witty comeback to calm her down, she pushed me down on the sofa."
    stop music fadeout 2.0
    play sound "fx/sheet.wav"
    m "Naomi turned me around to position my back on her chest while shifting us both down to put her between me and the sofa's backrest." #Rethink this
    show naomi aroused with dissolve    
    m "Then she locked her arms under my armpits to tie me in a tight embrace. I couldn't have escaped even if I had wanted to try."
    play sound "fx/bed.ogg"
    m "Finally, she placed her right wing over me as some kind of an impromptu dragon-blanket."
    Nm smile "Look at what a tasty morsel I have caught for my enjoyment."
    play music "mx/enigma.mp3"
    Nm "If you ever try to go back to your horrible world I will capture you before you make it to the portal and hug you until you change your mind."
    m "(Oh well, looks that's settled then. Sadly, I won't ever be able to go back to that apocalyptic hellhole.)"
    Nm stern "I'll also protect you if they try to take you back by force. I'm a lot of dragon with a few tricks they won't be expecting."
    Nm normal "You will be safe here with me for the rest of your life."
    show naomi smile with dissolve
    m "My mental resistance was waning rapidly in front of Naomi's advances. I was in no mood to refuse anything from her."
    c "T-thanks...{w} t-that's an offer I don't think I can refuse."
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
    Nm "Just so you know...{w} I actually have one in my bedroom closet..."
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
    Nm "Good choice. Your attempts would have been weak and pathetic anyway."
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

label sqb_naomi_m2_sexandeating:

    $ naomi2mood += 4
    $ naomiromance += 10
     
    Nm concern "Umm..."
    c "Come on, I like you as well."
    c "Or are you trying to say that the type of cuddling we just did is normally done among friends here?"
    show naomi shy with dissolve
    m "Seems I caught Naomi off-guard. She nervously looked me in the eyes, but then tried avoiding my gaze when I looked back."
    Nm "I... umm..."
    show naomi aroused with dissolve
    m "After a moment of hesitation, she finally looked me in the eyes."
    m "Then she stopped for a moment and sighed loudly."
    Nm smile "I suppose I should finally openly admit that I like you as well."
    Nm surprisedblush "I've been thinking about dating you ever since we met. Are you happy now?"
    c "You're-{nw}"
    m "She cut me off before I could say anything."
    Nm confused "You've been persistent in trying to get me to admit I like you. Why else would you obey my every whim?"
    Nm normal "The weird thing about us is that even though we met very recently I feel like we've known each other for a long time." 
    Nm "I think we complement each other nicely. Also, you understand me really well and like me for who I am."
    c "What's not to like in a cute dragon such as yourself?"
    Nm shy "Oh, stop it. You're much cuter than I am."
    Nm smile "Did you know that I've always wanted a partner smaller than myself?" 
    Nm "That's so I can easily put them in their place if they misbehave."
    Nm surprisedblush "I..."
    Nm shy "I didn't mean it like that."
    Nm "Well, I did but...{w} not that directly."
    Nm sad "Sorry! I hope I didn't make you feel uncomfortable."
    c "(This just gets weirder and weirder.)"
    Nm shy "I just h-hope the feeling's mutual."
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
    Nm "I've never had such a pink and squishy boyfriend before."
    c "You're going to make me blush."
    show naomi shy with dissolve
    m "Naomi looked off to the side and then back at me. She seemed to be thinking about something."
    Nm confused "I just realized there is something that would improve our cuddling experience by a lot."
    Nm normal "I honestly don't understand why you humans cover up your bodies so much."
    Nm blank "Why don't you take your covers off? Having fabric between you and your partner gets in the way of having a properly intimate cuddling experience."
    m "(This escalated faster than I ever could have anticipated.)" 
    m "(How should I respond?)"
    menu:
        "Undress in front of Naomi.":
            pass
            
        "Keep your clothes on.":
            c "I'm sorry, I don't feel comfortable doing that."
            Nm concern "Really? What's the big deal?"
            c "Among humans, taking your clothes off in front of someone is considered an intimate act."
            show naomi confused with dissolve
            c "It's also pretty weird to do in a living room."
            Nm "After all that you still don't...?"
            Nm sad "Oh well. I get it."
            Nm normal "Look at the time. Would you at least like to eat something before you go?"
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
            
                "A vegetarian salad with algae.":
                    $ renpy.pause (0.5)
                    $ naomi2mood -= 1
                    $ ecknaomim2food = "salad"
                    play sound "fx/veggies.ogg"
                    m "After brief consideration, I went with an idea of a light vegetable salad with some algae on the side."
                    m "It required no heating of any sort. However, cutting up all the components and properly mixing them up was about to take some time."
        
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
                        jump sqb_naomi_apt_sexandeating_end
                
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
                        jump sqb_naomi_apt_sexandeating_end
                
                    "Then learn to cook.":
                        $ renpy.pause (0.5)
                        $ naomi2mood -= 1
                        Nm "I would, but I never had a talent for it or any desire to learn."
                        c "It's never too late to start practicing."
                        Nm smile "I think I'll stick to the cafe and home deliveries."
                        m "Eventually, the food's temperature had dropped, and I was able to finish off my own serving. I noticed that Naomi left a fraction of hers untouched."
                        jump sqb_naomi_apt_sexandeating_end
                
            else:
                 m "The dragoness put the food on her plate and took a few hesitant bites, mostly concentrating on the algae slices."
                 m "A few minutes later, she glanced at me merrily munching on the salad."
                 Nm blank "Thanks, [player_name]. I think this is enough for me."
                 c "You don't want more?"
                 Nm confused "Oh, I'm fine. Don't worry."
                 m "I finished the rest of my serving a few minutes later. Naomi barely touched hers."
                 jump sqb_naomi_apt_sexandeating_end
        
    m "A whisper buried deep in my mind told me to just do as she says."
    m "(I suppose because dragons don't wear clothes in the way we do, she doesn't understand the implications of asking me to remove them in front of her.)"
    m "(I'll just take them all off. If it doesn't bother her, it shouldn't bother me either. When in Rome...)"
    Nm confused "Well?"
    c "Sure. In fact that's a really good point."
    show naomi normal with dissolve
    $ renpy.pause (2.0)
    stop music fadeout 1.0
    play sound "fx/undress.ogg"
    show naomi surprised with dissolve
    #Later on game asks if you're male or female.
    m "Naomi looked at me curiously as I removed my clothes piece by piece."
    show naomi surprisedblush with dissolve
    play sound "fx/undress.ogg"
    m "She was the most attentive when I started to remove my lower garments though. Her eyes fixated on my groin after I had taken my underpants off."
    Nm normal "You have fur even between your legs? That must be weird."
    c "It's called pubic hair. I can shave it off completely if it bothers you."
    Nm smile "No, it's kind of cute. I was just wondering how it will feel when we cuddle."
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
    Nm smile "In that case...{w} follow me to my lair."
    Nm "Who knows, maybe you will be the first one to survive intact?"
    m "(That doesn't sound good.)"
    hide naomi with dissolve
    m "Naomi turned and started moving towards her bedroom."
    m "I wanted to have sex with her but suddenly I was also scared of what that would entail."
    m "This was the last chance to run. If I entered her bedroom, there was no telling what would to happen to me."
    menu:
        "Follow Naomi to her bedroom.":
            m "I decided to resist the the scary thoughts I had."
            $ naomistatus = "girlfriend"
            $ naomi2sex = true
            pass
         
        "Escape while you still can.":
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
            m "(Looks like I fucked up really badly.)"
            $ renpy.pause (0.5)
            hide naomi with dissolve
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
    Nm smile "Welcome to my bedroom. When we first met, I didn't expect to invite you here on our second date." 
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
    m "Finally she turned to the right and straightened her legs, while still holding my gaze."
    m "(You really notice how much bigger she is compared to a human when she spreads out like that.)"
    show naomi smile with dissolve   
    m "Naomi patted the empty space on her right side with her open palm."  
    Nm "Are you coming or not? My bed feels so empty without you."
    m "I gulped and dropped my clothes on the floor, then walked up to the right side of Naomi's bed."
    play sound "fx/undress.ogg"
    m "I sat down on the side, turned and began to lower myself on Naomi's wing, preparing to position myself to have my back against her like before."
    Nm smile "That position won't do at all. I want to feel your squishy belly rub against mine."
    play sound "fx/bed.ogg"
    m "With those words Naomi suddenly turned me around and hugged me tightly before I could protest."
    m "She had me fully tied up in her arms. My head was also lodged firmly under her chin like when we watched the movie."
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
    m "After that she purred while tying my ankles together with the narrow part of her tail."
    Nm "Very nicely... in fact."
    m "A terrified feeling washed over me as I realized that due to my position shifting again, my erect cock was now poking her lower belly directly."
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
    Nm aroused "Why would you being aroused weird me out?"
    Nm slsmile "After all it just means that...{w} you know..."
    play sound "fx/lewd/lickslow.ogg"
    m "She licked my forehead with her long tongue."
    play music "mx/treetops.mp3"
    Nm smile "That you actually want to have sex with me?"
    m "Her remark made me feel like my heart had just jumped to my throat. To make things worse, my face instantly felt so hot, I bet it had turned completely red in this moment."
     
    if modinfo.has_mod("BangOk?") and bangok_four_bryce1_unplayed == False or bangok_four_xsebastian_unplayed == False or bangok_four_anna2.unplayed == False:
        m "(Why am I feeling so anxious right now? It shouldn't be that much different with Naomi.)"  
    else:
        m "(Why am I feeling so anxious right now? It shouldn't be that much different with a dragon.)"
         
    m "(I need to calm down or I'll embarrass myself again.)"
    m "Naomi interrupted my line of thought."
    Nm normal "Have you thought of what other humans would say if they found out that you wanted to have sex with a dragon?"
    $ renpy.pause (2.0)
    m "After a moment of silence, I gulped loudly, which she surely heard."
    c "B-but t-there aren't-{nw}"
    Nm surprisedblush "Oh, so you've fantasized about doing it with a dragon before?"
    show naomi aroused with dissolve
    m "I could feel Naomi starting to warm up more."
    Nm slsmile "Wanting have sex with another sentient species..."
    Nm aroused "...now that's a kink I like."
    m "Due to her remarks, my stomach was full of butterflies and I was so embarrassed I felt like I was going to choke. Yet somehow, I managed to speak up yet again."
    c "W-well I-{nw}"
    Nm surprisedblush "Don't worry about it."
    Nm shy "By the way, your face is completely red. Are you feeling okay?"
    m "Naomi moved her maw closer. I could feel her hot and almost steamy breath on my face."
    c "Yes... umm..."
    c "I'm j-just-{nw}"
    Nm smile "Feeling very embarrassed and aroused right now? I'm teasing you because I knew you would be unbelievably cute flustered like this."
    Nm slsmile "I'm going to keep you safe with me and never let you you go."
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
    m "I felt like I had no choice but to fuck her immediately or I was going to die due to my heart bursting out of my chest."
    show naomi aroused with dissolve
    c "Yes. You are a sexy and wonderful dragoness."
    Nm smile "I'm happy to hear that, you cute human." 
    Nm normal "When you removed your covers, I saw where your genitals are located. I don't think our anatomies are too different to make this inconvenient for us."
    
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
    m "When I leaned toward her to reciprocate the dragon tongue kiss, Naomi opened her eyes to look back at me. She looked at me like I was what she treasured the most in the entire world."
    m "The only things I could do on top of staring back into her beautiful eyes was to focus breathing through my nose and staying as still as possible."
    m "Again, I felt like my chest was going to explode."
    m "(I'm going to die of a heart attack.)"
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
    Nm smile "That settles it then. We won't ever have to use protection as long as you handle yourself with care if you have any other sexual relationships in the future." 
    Nm shy "I'm very eager to get to feel your human cum inside me every time you fuck me."
    Nm aroused "Who knows what might end up happening if we're lucky?"
    m "(What's she even talking about?)"
    m "(Oh...{w} doesn't she know that I can't get her pregnant? Didn't she pay attention in biology class?)"
    m "(That, or she's just testing me to see if I like her enough to go through with that in case it was possible.)"
    m "(I guess I'll do my best to satisfy her kinks.)"
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
    
    #PC comes almost immediately? Move some of the stuff into optional round two?
    c "Are you ready?"
    Nm slsmile "I've been ready for a while."
    play sound "fx/lewd/penslow.ogg"
    queue sound "fx/sheet.wav"
    m "As I penetrated her pussy, she locked me tightly in place with her legs."
    Nm smile "Caught you!"
    play sound "fx/lewd/penfast.ogg"
    m "After the initial penetration, I moaned as I bucked myself as far as I could go in a single thrust." 
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
    m "In this moment, she was the only thing that existed for me in the world."
    Nm smile "I love you. You belong to me now. The only way to go is forward." 
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
    m "Since I had gotten the permission to finish, I started preparing to shoot my cum inside Naomi by thrusting deeper."
    c "I'm going to paint your insides white with human cum!"
    Nm surprisedblush "Did you come up with that line all on your own?"
    Nm smile "Anyway, I doubt your output is enough to accomplish that. You're welcome to try your best anyway." 
    $ renpy.pause (2.0)
    m "I couldn't hold it any longer."
    stop soundloop fadeout 2.0 
    play sound "fx/lewd/cum.ogg"
    queue sound "fx/lewd/penslow.ogg"
    $ renpy.pause (1.0)
    m "I grunted as I came."
    c "Urgh!!!Ahh!!!{nw}" with hpunch
    play sound "fx/lewd/penslow.ogg"
    queue sound "fx/lewd/cum.ogg"
    queue sound "fx/rub2.ogg"
    show naomi slsmile with dissolve
    m "I bucked against Naomi for another time to release my second rope of cum. She let out a content sigh and started gently rubbing the back of my neck."
    Nm smile "Well done, tiny pink human."
    Nm aroused "I can feel a whole lot of your sticky seed inside me. You weren't joking about being pent up."
    Nm shy "Unfortunately, you didn't manage to get me off." 
    Nm normal "If you can't go again you can finish me off with your mouth."
    menu:
        "Use dick.":
            c "I still have another round in me. Just give me a few moments to recover."
            Nm stern "Try to last longer this time."
            c "I promise I'll do better."
            
            show naomi smile with dissolve
            play soundloop "fx/lewd/penslow.ogg"
            m "Some of my seed seeped out of Naomi's pussy as I fucked her, which aroused me to no end since it reminded me of what I had just done a few moments earlier."   
            if modinfo.has_mod("BangOk?") and bangok_four_bryce1_unplayed == False or bangok_four_xsebastian_unplayed == False or bangok_four_anna2.unplayed == False:
                m "(I can't believe Naomi wants me to cum inside her so badly.)"
            else:
                m "(I can't believe I just came inside a dragon.)"
    
            stop soundloop fadeout 1.0
            stop music fadeout 1.0
        
        "Use mouth.":
            c "I'm spent, I'll just use my mouth."
            Nm "Works for me. Your mouth looks different from what I've seen."
    
    #PC puts clothes back on
    
    c "That was the best sex I've ever had. I think the hours-long tease had something to do with it."
    Nm normal "It was certainly fun to play with someone who is too weak to resist anything I do to them."
    Nm smile "I'm looking forward to many more sessions like this."
    m "(I'm doomed.)"
    c "M-me too."
    
    play music "mx/airborne.mp3"
    c "Naomi, I can't think of a word to describe how much I love you. Do you want to get married?"
    Nm surprised "Is that how it works in your world?"
    Nm confused "We've only had sex once so far. That doesn't mean we should get married yet."
    Nm normal "Marriage is a long-term commitment."
    c "I'll prove myself worthy of you."
    m "(What should we do next?)"
    c "Wanna take a shower together?"
    Nm smile "Sure, we should get cleaned up."
    c "Let's go."    
    play sound "fx/rumble.ogg"
    $ renpy.pause (4.0)
    show naomi concern with dissolve
    m "(It seems that we forgot to eat.)"
    Nm confused "Oh, you're hungry?"        
    Nm normal "We could order some food if you wanted. Cooking ourselves works as well if that's something you'd want to do."
    c "Actually, a fun time in the kitchen sounds great right now. I want to return all the hospitality I've gotten here so far by pampering you back."
    Nm shy "You really don't have to. I enjoyed myself too."
    Nm normal "Wouldn't it be easier if we just placed a food delivery and showered together while waiting for it to arrive?"
    c "Shower can wait. I really feel like cooking right now."
    c "Besides, I also want to find out how similar your food products are to ours. One of my personal reasons for coming here was to learn more about your society and customs."
    c "For now I'll have to say that the food's been pretty similar to ours. Still, I'd be very interested in delving deeper into this by getting some first-hand experience."
    Nm smile "Well, if you put it like that...{w} I suppose I will have to let you sate your curiosity. More importantly, I would never turn down a delicious home-cooked meal." 
    Nm normal "I suppose I'd also be very interested in finding out how different human cooking is from to ours."
    c "Looks like that's settled then. I'll cook a couple of dishes for you to try out."
    Nm smile "I can't wait to do some proper taste tests."
    c "Me neither."
    scene black with dissolvemed
    play sound "fx/door/door_open.wav"
    m "As I nodded in agreement, we exited Naomi's bedroom back into the living room. For some reason, this time she was trailing behind me instead of it being the other way around like before."
    scene ecknaomiapt02 with dissolvemed
    show naomi normal with dissolve
    c "First, I really need drink a liter of water, or two. Would you like something to drink as well?"
    Nm "Sure. The glasses are in the kitchen cabinets." 
    Nm blank "I'll go wash myself while you get set up. If you need any help figuring out where everything is just give me a shout."
    show naomi blank flip with dissolve
    hide naomi with easeoutright
    play sound "fx/door/door_open.wav"
    queue sound "fx/door/doorclose.ogg"
    m "Naomi hurried off to what I presumed to be the bathroom."
    m "(Let's see what kind of stuff she has in the fridge.)"
    play sound "fx/crapfridge.mp3"
    m "As I started looking inside, yet again I noticed that a lot of the packaging had familiar shapes and even labels."
    m "(I still haven't gotten used to how weird it is that so many things even down to tiny details like labels on food products are almost identical in a world inhabited by dragons.)"
    m "(They're just like what my apartment was stocked with. I have to admit that it makes me feel a bit familiar, but also unsettled at the same time.)"
    m "(Oh right, she wanted to drink something. She liked juice, right?)"
    m "I took a carton of juice from the back of the fridge."
    play sound "fx/cabinet.ogg"
    queue sound "fx/pour.ogg"
    queue sound "fx/glassdown.wav"
    m "I took a large glass and poured juice in it. Then I added a straw and placed it on the kitchen counter."
    m "(I guess I can give it to her when she comes back.)"
    play sound "fx/pour.ogg"
    queue sound "fx/chug.wav"
    queue sound "fx/glassdown.wav"
    m "I took a smaller glass, poured some juice for myself and drank it in one go."
    m "(I really needed that. It tastes a bit like orange and mango juice.)"
    m "Now I was fully prepared to continue figuring out what all the stuff in Naomi's kitchen was."
    play sound "fx/cabinet.ogg"
    m "(It's the mostly the same thing with the produce in her cabinets as well. Also, there's so much stuff you'd think she cooks at home.)"
    m "(Wait, did she buy all this stuff just to impress me? That's very cute.)"
    m "(But how did she know I like cooking? I suppose I should ask her when she comes back.)"
    m "(Back to the main task at hand. I think at first I should move everything on the kitchen counter and sort by type.)"
    play sound "fx/rummage.ogg"
    m "With some effort, I moved most of the foodstuffs and ingredients onto Naomi's kitchen counter and then organized them."
    m "(This is going to be fun. Although, having only two cooktops will might pose a challenge. They're pretty old-fashioned as well.)"
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
    m "(Alright, this looks better. Let's figure out what we actually want to use.)"    
    $ renpy.pause (2.0)
    m "I noticed a pack of egg noodles and a large pack of lightly salted chicken fillets."
    m "(I definitely feel like frying some noodles. I'll use the chicken as well, although I am not yet sure how.)"   
    m "(I like the flexibility of these fillets because you can always cut them to pieces if you want, but also season them how you like. Fried noodles are a solid pick too, because almost everyone likes them.)"
    play sound "fx/faucet1.ogg"
    queue sound "fx/button_press.ogg"
    m "(I poured in water from the kitchen faucet into an electric teapot and turned it on to heat water for the noodles.)"
    m "(It's a lot less effort to heat the water like this. Also, the water stays hot longer inside the teapot.)"
    play sound "fx/door/door_open.wav"
    queue sound "fx/door/doorclose.ogg"
    m "As I was pondering on how to proceed, Naomi came back to check on what I was doing."
    show naomi normal flip with dissolve    
    show naomi normal with easeinright
    Nm "Did you manage to find out where everything is?"
    c "Yes, thank you. You seem to have quite a lot of stuff stored in your kitchen. I'd have guessed you usually cooked at home if you already didn't tell me otherwise."
    Nm shy "Well..."
    Nm normal "I wanted to try out something new since you were coming over, so I made an exception and went on a shopping spree after work. It felt just like the right thing to do."
    Nm smile "Anyway, looks like my plan worked, since I managed to bribe you into cooking for me."
    c "Oh, you got me with your scheme." 
    c "This is going to be fun, I promise."
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
    hide naomi with easeoutright
    m "With my assurance, Naomi walked past me to the living room and placed the glass of juice on the table."
    m "After that she jumped on the sofa in one smooth motion and started flexing."
    m "I kept watching Naomi as she flexed. She looked like a big scaly cat with wings and cute webbing."
    m "After finishing her exercise and settling on the sofa, she noticed I was admiring her instead of preparing to cook."    
    show ecknaomicg1 at Pan ((250, 230), (620, 50), 15.0) with dissolvemed
    $ renpy.pause (7.5)
    m "She is so massive...{w} especially her thighs and tail."    
    Nm "Your mouth is gaping. Like what you see?"
    c "I think I already saw plenty in the bedroom. Although...{w} I have to admit that you look very cute lying on the sofa like that."
    Nm "Get back to the cooking, or I'll have to eat you instead."
    c "..."    
    scene black with dissolvemed
    $ renpy.pause (1.0)
    scene ecknaomiapt02 with dissolvemed    
    m "(Where was I?)"
    m "(Oh right, let's see what else we've got.)"
    $ renpy.pause (2.0)
    m "(This white, basil-flavored mouflon and aurochs cheese looks remarkably similar to something we used to have.)"
    #Sound?
    m "I cut open the packaging with a knife and then sliced off some cheese into my mouth for a taste test."
    m "(Perfect, I'll cut this to pieces and add it to the fried noodles.)"
    m "(On top of that some of these vegetables will add a nice texture and hopefully good flavor as well. Also, we got soy sauce, wing sauce, brown sugar and ginger powder to season the whole thing.)" 
    m "(Let's start off by heating up a pan first.)"
    play sound "fx/metalbox.ogg"
    m "I began by putting a pan on the cooktop but as I turned on the heat I realized something."
    m "(Wait a minute.)"
    m "(Let's first make sure I don't get eaten by a hungry dragoness.)"
    c "Naomi, would you like some bread sticks as appetizers?"
    Nm "Sounds great to me. In fact, I was just going to come over there and eat your ingredients."
    c "If you eat them, I won't be able to prepare them into dishes."
    m "I focused back on the task at hand and quickly picked all the required ingredients for the appetizers."
    m "(Toast, garlic, black pepper, salt and herb mix here we go.)"
    m "(Wait, where's the olive oil?)"
    play sound "fx/cabinet.ogg"
    queue sound "fx/cabinet.ogg"
    queue sound "fx/rummage.ogg"
    $ renpy.pause (8.0)
    m "After looking through some of Naomi's kitchen cabinets I found it hidden behind some boxes."
    m "(There we go.)"
    Nm "Need help finding something?"
    c "I'm fine. I was just looking for some olive oil."
    m "(Finally, we can get started.)"
    play sound "fx/button_unpress.ogg"
    $ renpy.pause (2.0)
    queue sound "fx/metalbox.ogg"
    queue sound "fx/unwrap.ogg"
    m "I turned on the oven and prepared two baking trays with baking paper."
    m "(I suppose I can bake a big pile. Slicing the toast won't take too long if I do it efficiently.)"
    m "(The oven probably isn't ready when I am done with the cutting but I can always start preparing for something else. Also, I will have even more time when the bread sticks are in the oven.)"
    m "(Oh yeah, I also have to prepare the mix to flavor the bread sticks. Who knows if the oven will be ready after I've done that.)"
    m "(Multitasking and planning ahead is so much fun.)"
    m "I opened a bag of toast and put several slices on top of each other on the cutting board."
    play sound "fx/crapcuttingboard.mp3" #Not perfect but it just works
    m "Then I cut the bread into neat sticks, moved them off to the side and prepared cut another batch of toast."
    m "After a couple of minutes, I managed to slice the entire bag of bread."
    #Sound?
    m "To create the flavoring mix, I peeled all of the garlic, crushed it into a bowl with a pestle and mixed in some olive oil, pepper and salt."
    m "After that I placed all the bread sticks on the two baking trays and used a spoon to apply the fresh mix."
    m "(Looks like I have some time left after all since the oven isn't ready yet.)"
    m "(I should probably figure out what to do with the chicken next. Let's check again what ingredients we've got.)"
    $ renpy.pause (2.0)
    m "(We have all the ingredients for batter plus some herb butter.)"
    m "(Let's stuff the chicken fillets with some herb butter and bread and fry them. I've never met anyone who doesn't like that dish.)"
    play sound "fx/metalbox.ogg"
    m "I set a pan to heat up on the cooktop and cut open the large pack of chicken fillets."
    m "(Let's see... {w}the eight chicken fillets in this package should be enough for me and Naomi. She can always eat the rest tomorrow if there's any left over.)"
    m "I put a fillet on the cutting board and grabbed a knife."
    play sound "fx/sliceshort.ogg"
    m "In order to create a pocket for the herb butter I cut the fillet horizontally through the middle and then expanded carefully, to make sure I don't create any additional holes that need plugging."
    play sound "fx/sliceshort.ogg"
    m "I repeated this arduous process for the seven remaining fillets."
    play sound "fx/crapcuttingboard.mp3"
    m "Next I sliced all of the herb butter into pieces and stuffed it inside the pockets I had just cut. After that I closed the hole in each fillet with a large toothpick."
    m "This was the most tedious part of my cookout, but time went quickly because I knew the effort would be well worth it."
    play sound "fx/salt.ogg"
    m "To finish everything off, I sprinkled some black pepper on the stuffed fillets."
    m "(Finally done. Also, looks like the oven is ready just in time so I don't have to wait.)"
    play sound "fx/door/hallwaydoor.ogg"
    m "I put the baking trays with the bread sticks in the oven and set a timer."
    m "(Our hunger's going to be alleviated soon. Next we need a side dish for the breaded chicken fillets.)"
    $ renpy.pause (2.0)
    m "(Looks like we have some higher-starch potatoes. I think mashed potatoes would go really well as a side. Luckily, I have some hot water already.)"
    play sound "fx/faucet2.ogg"
    queue sound "fx/metalbox.ogg"
    queue sound "fx/faucet1.ogg"
    queue sound "fx/button_press.ogg"
    m "I took a large pot, filled it with water first from the teapot and the rest from the kitchen faucet. Then I set the pot to heat up on the cooktop. Since I still wanted to save time on the noodles, I filled the teapot again and turned it on."
    m "(I wish I had realized this earlier, because boiling the potatoes will still take some time.)"
    m "(Moving on to the potatoes proper. I think if I peel them really fast I'll be on time.)"
    play sound "fx/faucet2.ogg"
    queue sound "fx/rub1.ogg"
    m "I emptied all the potatoes into the sink, then rinsed and rubbed them to get all of the dirt off."
    #Peeling sound?
    m "After peeling the potatoes at a lightning speed, I had a large bowl of potatoes ready to be boiled."
    m "(Another tedious step done in my quest to cook for Naomi. The water isn't boiling yet, so I should probably move back to the chicken fillets.)"
    play sound "fx/dishes.wav"
    m "To continue preparing the chicken fillets I took three deep plates and a normal one. I filled the deep plates with flour, egg with a touch of water and finally breadcrumbs. I placed them horizontally on the counter with the normal plate at the end of the production line towards the stove."
    m "I dipped a fillet in first flour, then egg, followed by breadcrumbs and finally egg and breadcrumbs again and placed it on the ready-plate. I repeated this messy process for the rest of the fillets."
    m "Lastly, I sprinkled some breadcrumbs on all of the fillets on the ready-plate to make sure they were properly breaded everywhere."
    m "(The crunch is very important.)"
    m "(I think I'll time everything correctly if I cook four fillets at a time. The pan is more than big enough for that.)"
    play sound "fx/fry.ogg"
    m "I poured some olive oil into the hot pan, carefully placed four fillets in and put the lid on."
    stop sound fadeout 1.0
    m "(The proper way is to cook both sides with higher heat at first. That means it would be good if I remembered to turn them and then lowered the heat after both sides have been fried. Cooking them more slowly should also leave me time to focus on other stuff.)"
    m "I set another timer for the chicken fillets."
    $ renpy.pause (2.0)
    m "(Looks like the water for the potatoes is boiling already.)"
    play sound "fx/water1.ogg"
    queue sound "fx/salt.ogg"
    m "To not splash any hot water on myself, I took extreme care when dropping the potatoes into the pot, added some salt and set a new timer."
    $ renpy.pause (1.0)
    m "(Looks like the bread sticks are almost done. It doesn't really matter if I take them out a minute early so I might as well do it now to stay on schedule.)"
    play sound "fx/door/hallwaydoor.ogg"
    queue sound "fx/salt.ogg"
    queue sound "fx/unwrap.ogg"
    m "I took the trays out of the oven and sprinkled some herb mix on the bread sticks. Then I used the baking paper to slide them onto a very large plate."
    m "Not forgetting about the chicken fillets, I turned them for the first time."
    play sound "fx/pizzabite.ogg"
    m "Then I ate a few of the bread sticks offset my worst hunger. They were crunchy, oily, garlicky but most importantly tasty, like I had expected them to be."
    m "(I'm sure Naomi will love these.)"
    m "My hands got messy from eating with them so I instinctively wiped off the grease on the kitchen towel."
    m "(Oh yeah, I'll have to make sure Naomi doesn't make a mess eating these. She'll probably ask me to clean it up afterwards if she ends up doing that.)"
    m "I picked up the bread stick plate along with some rather large napkins and went off to the living room where Naomi was. She was attentively watching what I presumed to be one of those long series she had told me earlier about."
    scene ecknaomiapt03 with dissolvemed
    show naomi normal with dissolve
    Nm "That was certainly a lot faster than waiting for a food delivery. It seems that we made the correct choice."
    show naomi surprised with dissolve
    m "I presented the appetizer plate to Naomi and it immediately perked up her attention."
    c "So, here's something to start off with. Do you think I made enough so that you won't have to eat me?"
    Nm shy "I hope you understood that I was just joking. In fact, I can go a long time without eating if I really need to. I just need to eat a lot to keep in shape for some of my more physical activities, like long-distance flying or swimming."
    Nm smile "Thanks a lot, [player_name]. These bread sticks smell delicious."
    c "You're welcome, Naomi. Please use the napkins after you've finished eating them. Also, avoid touching any of the furniture before you've wiped your hands clean."
    Nm shy "You're really thinking of everything for me, aren't you?"
    show naomi surprised with dissolve
    m "Naomi had been eyeing the bread stick plate hungrily ever I since I presented it to her, so it didn't come off as a surprise when right after I placed it on the table she stuffed a big handful of them right into her maw."
    play sound "fx/pizzabite.ogg"
    queue sound "fx/pizzabite.ogg"
    queue sound "fx/pizzabite.ogg"
    Nm smile "Delicious!"
    Nm normal "Why aren't you eating any? Surely there's enough for both of us."
    c "I already ate a couple in the kitchen, and that was enough for me. You should remember that I can't eat as much as you can so I have to leave room for the other dishes."
    Nm smile "I suppose that just means more for me then."   
    
    if naomi1drink == "cocktail":
    
        Nm confused "By the way, could you fix up a human cocktail for me? I want something to drink with these delicious bread sticks."
        c "I'd love to." 
        c "Did you buy any liquor on your shopping spree? I didn't see any in the fridge or in the cabinets."
        Nm normal "Yeah, I bought a bottle of something at the store that was recommended to me by the clerk. It's hidden in the fridge's door compartment."
        c "Alright. I'll look at what other cocktail ingredients you have and make the best one I can come up with."
        Nm smile "Thanks a lot. I knew I could count on you on that front."
    
    else:
        Nm "Could I get some more juice with these delicious bread sticks?"    
    
    c "I'll go back to the kitchen now."
    Nm normal "I'm really looking forward to what else you can come up with."   
    scene ecknaomiapt02 with dissolvemed
    play sound "fx/fry.ogg"
    m "After getting back, I turned the chicken breasts again and lowered the heat."    
    stop sound fadeout 1.0
    m "(Let's now focus on getting the noodles ready.)"
    m "(Luckily, the water inside the teapot was still hot enough for the noodles.)"
    play sound "fx/pour.ogg"
    m "I emptied the entire pack of noodles into a pot and then poured in some hot water from the teapot."
    m "(There's no need to use a timer for this. Also, I should have enough time to finish the rest of the ingredients while the noodles cook.)"
    play sound "fx/faucet2.ogg"
    queue sound "fx/veggies.ogg"
    m "I washed some of the more familiar-looking vegetables and held them in a neat pile on the cutting board, then using my knife-work to turn them into pieces of various sizes."
    play sound "fx/crapcuttingboard.mp3"
    m "After finishing up, I meticulously cut the cheese I had selected previously."
    play sound "fx/faucet1.ogg"
    queue sound "fx/faucet2.ogg"
    m "The noodles were ready now, so I took a pot lid and used it together with the pot to carefully pour all the hot water into the sink. Then I poured in some cold water stop the cooking process."
    m "Unfortunately, I didn't have a free cooktop so frying the noodles would have to wait. I poured some olive oil in the noodle pot to make sure they wouldn't stick together."
    
    if naomi1drink == "cocktail":
    
        stop sound fadeout 1.0
        m "(There's enough time to make a cocktail in the meantime.)"
        play sound "fx/crapfridge.mp3"
        m "I took the liquor bottle from the fridge's door compartment and inspected what I had to work with. The bottle's sunny and cheerful-looking label read 'sugar cane liquor'"
        m "(I have an idea what this might compare to. Still, I should probably taste it first.)"
        play sound "fx/uncork.ogg"
        queue sound "fx/pouringwineshort.ogg"
        $ renpy.pause (1.0)
        queue sound "fx/coffee.wav"
        m "I poured some in a small glass and took a large sip."
        play sound "fx/glassdown.wav"
        m "(Tastes like rum.)" 
        m "(To be safe, I'll make something that doesn't taste too different from what I had at Adine's.)"
        m "When looking for additional ingredients, I quickly figured out what cocktail to make as I spotted some limes. I also needed simple syrup made with brown sugar for the cocktail I had decided on, but making that yourself was extremely easy."
        m "(Making it will take even less time than normal, because I have some hot water to speed up the process. Unfortunately, there's only two cooktops.)"
        m "(I think I can take the chicken off for a few moments.)"
        play sound "fx/pouringwineshort.ogg"
        m "To dissolve the brown sugar, I measured two parts of it and one part of hot water and poured both into a third pan. Then I took a potholder, put it on the kitchen counter and placed the chicken fillet pan on it." 
        play sound "fx/metalbox.ogg"
        #Mixing sound?
        m "Lastly, I quickly grabbed the simple syrup pan and put it on the heat. After not too many seconds and some mixing, the simple syrup was ready."
        play sound "fx/pouringwineshort.ogg"
        queue sound "fx/metalbox.ogg"        
        m "I poured the contents of the pan it into a large heat-resistant glass. Then I turned the chicken and put the pan back on the cooktop."
        play sound "fx/crapcuttingboard.mp3"
        #Juicer sound?
        m "Then I cut some limes in half and juiced them into some delicious, fresh lime juice for the cocktail."
        play sound "fx/cabinet.ogg"
        queue sound "fx/pouringwineshort.ogg"     
        m "Next, to chill the cocktail, I quickly found a dragon-sized cocktail shaker in one of the cabinets. I poured roughly three portions of fresh lime into the shaker through a sieve."       
        m "(Since Naomi seemed to be skittish of alcohol, I should be careful with the alcohol content. Better to play it safe, as always.)"
        m "I inspected one of the same types of glasses I had served her juice in."
        m "(She's like two to three times as big as I am, so two portions of alcohol in around a half a liter cocktail should only give her a slight buzz, even if she drank it all in one go.)"
        queue sound "fx/pour.ogg"
        m "I measured two portions of liquor and six portions of simple syrup and poured them into the cocktail shaker."
        play sound "fx/crapfridge.mp3"
        m "Next I opened Naomi's freezer, took some ice and added them in."
        #Shaking sound?
        m "I shook the shaker for a short time and poured the cocktail into the large glass, again through a sieve."
        m "Finally, I added two straws and used a spoon to do a taste test."
        c "(That's a pretty sweet version. Just the way I like it, and you can barely even taste the alcohol. I bet Naomi will like it as well.)"
        scene ecknaomiapt03 with dissolvemed
        show naomi normal with dissolve
        play sound "fx/glassdown.wav"
        m "Naomi was intently focused on watching the series so she only noticed me after I had placed the cocktail on the table in front of her."
        #Expand the conversation below
        Nm confused "Oh, hey."
        c "Here's the cocktail you ordered. Enjoy."
        Nm normal "Thanks."
        queue sound "fx/coffee.wav"
        m "Naomi craned her head towards the glass and tried the cocktail."
        Nm smile "It's pretty good! Good job, [player_name]."
        c "I'm happy to hear it. If you'll excuse me, I have to go back to the kitchen. We can talk more after I have brought the rest of the food."
        show naomi normal with dissolve
        play sound "fx/dishes.wav"
        m "Naomi had resumed focusing on the series, so I just grabbed the empty appetizer plate from the table and went back to the kitchen to continue cooking."
        scene ecknaomiapt02 with dissolvemed

    else:
    
        m "(I have to wait a little bit for the chicken, so I should probably bring Naomi her juice now.)"
        play sound "fx/pour.ogg"
        m "I took another of the large glasses and poured some juice in it. This time I added two straws for ease of drinking."
        scene ecknaomiapt03 with dissolvemed
        show naomi normal with dissolve
        play sound "fx/glassdown.wav"
        c "Here's your juice, as ordered. I added two straws this time so you can drink it faster."
        Nm smile "Thank you." #Expand
        c "If you'll excuse me, I have to go back to the kitchen."
        play sound "fx/dishes.wav"
        m "Naomi had resumed focusing on the series, so I just grabbed the empty appetizer plate from the table and went back to the kitchen to continue cooking."
        scene ecknaomiapt02 with dissolvemed
        
        play sound "fx/pour.ogg"
        queue sound "fx/chug.wav"
        queue sound "fx/glassdown.wav"
        m "Feeling thirsty from the heat of the kitchen, I emptied the carton of juice into a glass and drank it. There was nothing to do for now, so I waited a few minutes for the chicken timer to beep."
    
    $ renpy.pause (2.0)
    play sound "fx/beeps2.ogg"
    m "The first batch of chicken breasts were ready, so I took them off the pan onto a serving plate, added the rest of them in and set the heat higher again. After that was done, a timer beeped to tell me that the potatoes were ready."
    play sound "fx/metalbox.ogg" 
    m "I took the boiling pot off the cooktop and added the noodle pan in."    
    #Sound?
    m "To continue preparing the mashed potatoes, I then took a lid and used it together with the potato pot to pour all the hot water out into the sink. Then I grabbed a masher from one of the drawers and proceeded to mash the potatoes."
    play sound "fx/pour.ogg"
    m "After I had mashed for a short time, I poured in some milk."
    m "(That should be enough for now. It's better to be careful to not use too much milk at first because you can always add more later. If you add too much the mashed potatoes will become soggy, like a thick soup.)"
    play sound "fx/crapcuttingboard.mp3"
    m "Then, when I had mashed for a bit longer I opened one of the packages of butter on the counter, cut some pieces from it and added them to the almost ready mashed potatoes."
    play sound "fx/fry.ogg"
    m "To finish off, I mashed a little bit more and finally mixed the entire thing with a scoop and left it in the pot ready for a serving. I also remembered to turn the chicken."
    play sound "fx/salt.ogg"
    m "After doing that I tasted the mashed potatoes, decided to add some salt and tasted it again."
    m "(Perfect. Now on to the next thing.)"
    m "I added a lid to the pot of fresh mashed potatoes to preserve some heat and moved on to fry the noodles."   
    play soundloop "fx/fry.ogg"
    m "To start off, I poured some oil into the already hot enough frying pan and used my hands to add in the cold noodles."
    play sound "fx/salt.ogg"
    m "Then finally after mixing the noodles a bit, I added in the cut vegetables, cheese and the spices and sauces I had selected earlier."
    m "(That looks pretty good already.)"
    $ renpy.pause (2.0)    
    m "(Actually, let's put in some giant prawns as well, because I love the crunch. Luckily for us, they're already prepared and seasoned.)"
    m "After adding the prawns I mixed the noodles again, put on the lid and set yet another timer."
    stop soundloop fadeout 1.0
    m "(Now I'll just have to remember to mix the noodles every once in a while so they cook somewhat evenly.)"   
    m "(I don't feel like just waiting around. Could I make something simple but delicious in the mean time?)"
    $ renpy.pause (2.0)
    m "(How about a potato and bacon omelet? I could also use some other ingredients like these paprika-resembling vegetables for the texture and flavor.)"
    m "(Sounds great to me.)"
    play sound "fx/metalbox.ogg"
    m "I grabbed another pan and put it off to the side because both cooktops were occupied right now. Then I turned the chicken for the final time and lowered the heat, already anxious to be done with it."
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
    m "(I still got some time left before the chicken is ready, so how about a sauce? I think there's a good one I can make from what's available. It'll need a cooktop of course, but I can prepare the ingredients meanwhile.)"
    play sound "fx/veggies.ogg"
    m "To prepare for the sauce, first I mixed some white vinegar and water and peeled and cut two onions. Next I separated the yolk from a bunch of eggs and made a bain-marie from the pot I had used previously and a metal bowl."
    play sound "fx/faucet1.ogg"
    queue sound "fx/button_unpress.ogg"
    m "I needed hot water for this contraption so I poured some more into the electronic teapot and turned it on."
    m "(There's some time left on the chicken timer but probably I should take the fillets off to not waste time. They should be ready anyway.)"
    m "I placed the rest of the chicken onto the serving plate, and spread the bacon and potatoes evenly in the same pan to fry for the omelet."   
    m "(I still have some time left before the bacon is fried. I should stop inventing new things to cook already, so I'll just start cleaning up what I can, in case we feel too tired to do it after eating.)"
    play sound "fx/rummage.ogg"
    queue sound "fx/cabinet.ogg"
    queue sound "fx/crapfridge.mp3"
    queue sound "fx/faucet1.ogg"
    m "First, I put back everything I had taken from the cabinets and fridge. Then I put all the dirty kitchen equipment into the sink and rinsed, so they could be washed mo thoroughly later."
    m "(Washing the dishes can wait. I really don't feel like doing that right now.)"
    play sound "fx/crapspraybottle.mp3"
    queue sound "fx/wipe.ogg"
    m "I finished my tidying-up operation by spraying some cleaning liquid on the kitchen counters and wiping them clean."
    stop sound fadeout 1.0
    play sound "fx/fry.ogg"
    m "By now the bacon and potatoes were ready, so I added in the rest of the ingredients. Wanting to do a good job, I also mixed the noodles again."
    m "(The omelet might take a while, but we can just eat it for dessert because it's not going to burn on low heat.)"
    m "I started looking for some tableware to help us eat more easily."
    play sound "fx/cabinet.ogg"
    m "(That large bowl looks perfect for the fried noodles. Oh nice, she also has a saucière for convenient sauce-pouring. Why does she have it if she doesn't cook?)"
    play sound "fx/dishes.wav"
    queue sound "fx/crapfridge.mp3"
    m "To prepare for our meal, I took the bowl, saucière, some plates, utensils, glasses, napkins and another carton of juice and placed them in a neat order on the kitchen counter."
    m "(Almost there. The noodles should be fried enough now.)"
    m "I used pasta tongs to move the fried noodles from the pan into the bowl and stuck two dragon-sized forks on it for me and Naomi.  Then I quickly rinsed and wiped the pan and put it back on the cooktop."
    play sound "fx/faucet1.ogg"
    queue sound "fx/wipe.ogg"
    m "To continue making the sauce, I poured my water-vinegar mix on the pan and added the onions."
    m "(Damn, I just realized that reducing the water, vinegar and onions into a flavor broth is going to take a minute. I guess I will have to wash the dishes after all. Oh well."
    
    m "After that I placed my self-made bain-marie on the cooktop, and poured the egg yolks in the bowl. The yolks started heating up almost immediately after had broken them by whisking , so I started adding the flavor broth and whisked furiously."
    
    m "I was so proud of myself. Eight breaded chicken fillets filled with herb butter, a pot full of mashed potatoes, a lot of fried noodles, a delicious sauce and a bacon potato omelet, although it was still cooking."
    m "I kept whisking rapidly until the sauce was even, and then I started adding butter bit by bit. When that was done, I finished off the sauce with tarragon, white pepper, sugar and salt."
    m "(Finally, my arm is pretty tired. Worth it, because I really love this sauce.)"
    m "I poured the sauce from the bowl into the saucière and placed it with the rest of the food."
    m "(I can turn the omelet after I have carried all the food to Naomi. Other than that, looks like we're about done here.)"
    
    #Order of carrying
    
    #Naomi's parents tried to encourage her to cook by buying equipment, didn't go well and she hates cooking herself now
    #PC tells Naomi they should take the leftover food to work so they don't have to skip lunch
    scene ecknaomiapt03 with dissolvemed
    show naomi normal with dissolve
    c "Please use the the fork at least for the fried noodles. Otherwise the grease and sauces from the frying will be everywhere."
    show naomi blank with dissolve
    c "Oh yeah, also use scoop for the mashed potatoes. Even though we have swapped saliva, I don't want it in my food."
    Nm smile "Fine, fine. There's no need to be this fussy with me."
    Nm shy "Actually...{w} I think it's very cute."
    c "I appreciate it."
    
    c "Without further ado, bon appétit!"
    Nm confused "What?"
    c "We can start eating."
    play sound "fx/pizzabite.ogg"
    queue sound "fx/eating.wav"
    m "I began by taking a little bit of everything. Naomi dove straight in by tossing one of the breaded chicken breasts in her mouth to eat it whole."
    Nm smile "This chicken is so delicious. I especially like the crunchiness."
    c "Same. I love the taste and texture of batter, so I breaded it twice."
    Nm surprisedblush "Actually, even more than the crunchiness I love how the herb butter just bursts inside your mouth when you bite in."
    c "They are indeed a lot juicier than your basic chicken breasts. It must also be a different experience for you because you can eat it whole like that but I can't."
    Nm normal "That's an interesting point. You're already starting to sound like an expert on how to cook for hungry dragons."
    c "Well, I am certainly planning to hone that skill even further for both of our sake."
    Nm smile "I'm really looking forward to that, [player_name]."
    
    c "I think I will call my style of cooking simple but delicious. This philosophy leaves more time for eating."
    Nm "I love that idea. Eating is of course the most important part."
    c "Anyway, you should try the chicken with the sauce I made."
    show naomi normal with dissolve
    play sound "fx/chug.wav"
    m "I took the saucière and poured some of the thick, buttery and slightly bitter sauce on one of the breaded chicken fillets."
    show naomi surprised with dissolve
    c "There you go."
    m "After eyeing the chicken hungrily while I had poured the sauce, Naomi picked it up with the tips of her claws and proceeded to toss it in her maw."
    play sound "fx/pizzabite.ogg"
    Nm surprisedblush "This sauce is great with the chicken!" 
    Nm smile "I'm starting to really love human cuisine. It's so familiar but yet a little bit different."
    c "The sauce also works well with mashed potatoes, so you should definitely add it there too."
    
jump sqb_naomi_m2_ending
 
label sqb_naomi_m2_ending:
 
    Nm normal "I almost forgot to ask. How did our foodstuffs compare to human ones?"
    c "Well..."
    c "How should I put this...{w} it's really weird that everything is almost exactly the same even down to labeling, with only minor differences."
    show naomi confused with dissolve
    c "Some things taste a little different though. If I was being conspiratorial I would say that you were trying to imitate our food products to the best of your abilities with what's available to you."
    Nm surprised "Wait, really?"
    c "As for a reason, if I had to guess, the human that allegedly visited your world a long time ago had a bigger impact on your development than you think."
    Nm normal "Oh yes, that thing from the history class. I had completely forgotten about it until you mentioned it now."
    c "Also, similar sentient species usually developing along the same lines probably has something to do with it."
    Nm shy "I'd say despite physical differences our species are pretty similar because we're able to have a romantic relationship with each other."
    c "You make a good point as usual. Also, I think we will make a great team due to our of differences combined with important similarities."
    Nm smile "Likewise." #Expand
     
    stop music fadeout 1.0
    hide naomi with dissolve
    scene black with dissolvemed
    
    #It's rather late when the PC leaves, since he and Naomi did more stuff in this timeline
    #Copy some text from the original and edit it
    #Naomi kisses PC instead of flicking with her tongue and Sebastian comments on it after he and PC leave
    
    $ naomiscenesfinished = 2
    
jump ml_date_end  