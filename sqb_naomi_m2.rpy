label sqb_naomi_apt_chairs:

    $ renpy.pause (0.5)
    $ naomi2mood += 2
    $ naomilewd +=1
     
    c "I could move them for you if you want."
    Nm surprised "You mean right now?"
    c "Sure, if they bother you. I'd love to help you."
    c "I think I am better suited for articulately moving things around than you are."
    Nm normal "Thank you for the offer, but I want to host you, not put you to work."
    Nm blank "I'll do it myself tomorrow."
    Nm "Enough about my chairs. Let's go sit on the sofa."
    scene ecknaomiapt03 with dissolvemed

jump sqb_naomi_apt_chairs_end

label sqb_naomi_apt_differences:

    c "More importantly, have you considered how big you are compared to humans?"
    c "If you hugged someone smaller than yourself, you'd make them feel better in no time with your sheer hugging power."
    show naomi surprisedblush with dissolve
    m "(Why did I say that?)"
    Nm shy "I suppose you have a point."
    Nm smile "I bet if I caught a puny human like you, they'd never be able to escape my clutches."
    c "Actually that's what dragons sometimes do to humans in our fiction."
    show naomi confused with dissolve
    c "Although usually the dragons who mingle with humans are assumed male, and most of the time they only catch humans of the opposite sex."
    Nm normal "That sounds pretty weird. Why is that?"
    c "Well, I didn't really study literature or specialize in cultural history so I don't know for certain."
    m "I had a sudden urge to say something funny."
    c "Actually that trope makes no sense to me because I wouldn't mind being caught by a female dragon."
    Nm stern "I hope you know I was just being hypothetical."
    c "Yes, of course."
    c "Anyway, as a sociologist the most fascinating thing about our species' future relationship is how we can complement each other."
    show naomi blank with dissolve
    c "Kind of like how your different species of dragons are best suited for different kinds of tasks."
    c "I know runners are better at doing tasks that require precision than other dragons, but humans would be way better."
    c "I bet that for articulate tasks, our limbs are much better than anything you've seen before."
    show naomi normal with dissolve
    c "Like I implied before, I wouldn't mind moving a few things for you, because it's much easier for me."
    show naomi surprised with dissolve
    c "Then as a sign of reciprocity you could fly me across town or something, if you are comfortable doing that."
    show naomi shy with dissolve
    c "How long does flying across the town even take you?"

jump sqb_naomi_apt_differences_end

label sqb_naomi_apt_balcony:

    c "I love feeling the sea air again." 
    c "It's been a long time since I've been able to visit a seaside beach because our city-state is in middle of a desert."
    c "Wandering outside the walls is very dangerous so we don't do any recreational trips."
    Nm confused "That's very unfortunate." 
    Nm "Why would anyone want to live in the middle of a desert?"
    c "It's not really our choice. Most of us had to settle within a reasonable distance in a place where at least some of the infrastructure was intact."
    c "Anyway, standing in a peaceful place like this makes me both nostalgic and sad at the same time."
    c "I can't help but to think of all the hardship that has been placed upon us."
    show naomi sad with dissolve
    c "Living in my world is like a nightmare that never ends."
    Nm "I'm so sorry to hear that, [player_name]." 
    show naomi shy with dissolve
    m "Naomi seemed to be thinking about something."
    Nm "Just a funny thought..." 
    Nm "I wouldn't mind if you stayed here with me. You're... um... good company."
    Nm smile "You should also invite your friends. I would love to meet more humans. Like I said before, there's plenty of room for everyone."
    m "Naomi caught me off-guard again. I felt a sudden surge of emotions."
    m "Without warning, a tear slid down my cheek and had to sniff."
    show naomi concern with dissolve
    m "Naomi noticed it, and looked at me worriedly."
    c "Thank you, Naomi."
    c "I would love to take you up on your offer, if it's ever possible."
    c "I really like this place, especially the view from this balcony."

jump sqb_naomi_apt_balcony_end

label sqb_naomi_apt_movie:

    c "I couldn't agree more."
    c "Anyway, hearing the story of how through an unlikely series of events you became a police analyst was interesting."
    c "It's actually similar in some ways to how I ended up becoming an ambassador to your world."
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
            Nm normal "Don't you worry, I can take it."
            
        "Don't ruin the mood.":
            c "I'm sorry to disappoint you, but I don't want to ruin the mood. The story of how I ended up here is not a happy one."
            Nm sad "I'm sorry if I asked too much."
            Nm "Oh well."
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
            
            jump sqb_naomi_apt_movie_end
    
    c "Where to begin..."
    show naomi normal with dissolve
    #Music from when PC tells everyone the story?
    c "Like I alluded to earlier, my world used to be pretty prosperous. Our quality of life and general happiness was dramatically higher than ever before due to advances in technology."
    c "Well, I suppose social advances such as decreasing inequality and getting rid of most of human exploitation played a huge part too."
    c "But anyway, we used our technology automate most tedious and difficult jobs to have more time to do what we actually want to do, like hobbies or improving ourselves." 
    c "Our technology was far superior to yours. For example, we had computers everywhere, even on our wrists."
    show naomi blank with dissolve
    c "I suppose our technology is still superior, but manufacturing anything high-tech is quite hard these days."
    c "The future seemed pretty bright for all of humanity, but especially for me as well."
    c "I had gotten myself majors from both biology and sociology. Skills from those fields were in demand at the time due to rapid social advances."
    c "Unfortunately shortly after my graduation the flare hit us and my degrees became pretty much worthless in the ensuing aftermath." 
    c "A whole different set of skills would have been far more useful to help me in what I had to go through. Yet somehow, mostly due to sheer luck, I managed to survive."
    show naomi sad with dissolve
    c "I really don't want to get into the details. It suffices to say, if you've ever seen a post-apocalyptic movie, it was like that but worse."
    Nm blank "I've never heard of that genre."
    c "In post-apocalyptic movies...{w} never mind."
    Nm confused "Huh?"
    c "It's not that interesting to explain. Let me continue my story."
    show naomi normal with dissolve
    c "So, somehow I managed to survive and find my way to the city-state, Bastion, where I currently reside in."
    c "Things are quite bad there compared to your world but like I said, the world outside our city walls is basically a hellscape."
    show naomi sad with dissolve
    c "Before I became ambassador I was just doing odd jobs to survive."
    c "I supposed it wasn't all that bad if you look at the big picture."
    c "To fast forward, we found our portal on a scouting mission and sent Reza to investigate after the initial contact."
    c "In his case, there wasn't really any kind of process to select the most suitable person to go since we were desperate for any kind of help or even information." 
    c "I have to admit that we didn't really care if he died on the mission."
    c "Reza was known to be a troublemaker so him dying really wouldn't have been big loss. You wonderful dragons could have been savage, man-eating monsters for all we knew at the time."
    Nm smile "You've seen nothing yet. Just stick around for long enough and I might show you all my capabilities."
    m "Naomi's remark almost made me jump up from the sofa. I managed to mostly control myself but I'm sure she saw me twitch."
    c "I... uhh..."
    c "Where was I..."
    show naomi normal with dissolve
    c "Anyway, I was selected from a large pool of applicants to be the second person to visit your world. Due to my expertise in both biology and sociology I was uniquely qualified."
    c "Sending someone takes a lot of power so it'll just be me and Reza interacting with you until we get one of your generators."
    c "Reza's behavior leaves a lot to be desired." 
    c "Well... that would be the understatement of the century. Murdering someone is unforgivable even in our harsh world."
    c "I hope we catch him soon and end this mess."
    Nm smile "I hope so too. I want to meet some more cute humans and tell them we'll welcome all of them with open arms."
    c "I don't know what to say. You caring about humans this much makes me very happy."
    m "Suddenly I started to feel another surge of emotions. My throat started feeling dry and I wanted to cry."
    show naomi surprisedblush with dissolve
    c "H-honestly your unconditional kindness is unexpected. I don't know what we did to deserve it."
    c "Being as dependent on technology as we were wasn't good. The mess we're in is of our own making."
    Nm stern "Don't say that. Everyone needs help sometimes."
    Nm confused "Just make sure you have good friends..." 
    Nm smile "...or something more to help you out."
    m "Naomi moved closer towards me on the sofa."
    c "Thank you again, Naomi. I really mean it."
    m "After those words, she leaned towards me a little bit more."
    Nm shy "Would you like a hug? I don't want to see a cute human like you to be sad like this ever again."
    m "I liked her and turning her down would have been rude so I accepted her offer."
    c "Uhh... sure."
    show naomi slsmile with dissolve
    play sound "fx/sheet.wav"
    m "With that, Naomi leaned in closer and I returned the gesture by wrapping my arms around her upper body."
    m "She was cuddlier than I had expected." 
    m "This was the first time I could feel her strong breathing."
    Nm smile "Feeling better yet?"
    c "Yes, thank you." 
    c "Being hugged by a big dragon is really something else to calm you down."
    c "I don't know what to say."
    play sound "fx/sheet.wav"
    m "After the hug, I tried disentangling myself from her, but she wouldn't let me go."
    Nm confused "What's wrong?" 
    Nm slsmile "Let's stay like this so you won't feel sad while you finish the story."
    c "Sure, that works for me."
    c "Anyway to continue..."
    show naomi normal with dissolve    
    c "Like you already know, our most important goal is to get one of your generators."
    c "A lot of tech, especially advanced medical equipment, was spared in our city. The problem is that soon we won't have enough power to run anything properly." #Thanks for the lore, MBS
    c "I just hope my city-state is still standing when it's time for me to go back."
    show naomi blank with dissolve  
    m "As I said that I was hit by the sudden realization that I might not be able to return here after I had completed my mission."
    m "After all, given the precarious situation we were in, who would care about researching dragon society and culture?"
    m "Because of this realization, it was the first time when thinking about having to return made my stomach feel like an endless pit of suffering."
    m "An immediate feeling of panic was settling in me, so I had no choice but to confide in Naomi."
    Nm concern "Something wrong?"
    c "Sorry, I got lost in thought."
    c "Anyway, I hate to admit that I am not looking forward to the day when I finally have to go back to my own world."
    c "Sticking together and working for the greater good has kept us alive so far."
    show naomi concern with dissolve
    c "Because of this contradiction, I suddenly have a weird feeling of dread and helplessness." 
    c "If I am being frank, I actually don't want to leave at all because your world is too wonderful."
    show naomi slsmile with dissolve
    m "Naomi started carefully rubbing the side of my head with her snout."
    Nm normal "If things are that bad in your world, why don't you just stay here?"
    Nm "I'm sure they won't miss one human, or other potential like-minded folks who want to live with us instead."
    c "B-but...{w} I have to go back."
    show naomi stern with dissolve    
    c "My superiors might assume you're holding me hostage, and that would ruin everything we've been working towards."
    Nm "Don't be silly. Once you have our generators, they can come here themselves to see that you're okay."
    Nm blank "After all, if what you say is true about your world, why would anyone need to be held hostage in order to make them stay here?"
    m "A conflict inside me was figuratively ripping me apart. I knew duty to my people was important, but a growing part of me wanted to just have a quiet and happy life."
    m "Another reason for wanting to say yes was that I didn't want to disappoint Naomi by declining her." 
    m "It probably took her a lot of courage to ask me, considering her usually shy and reserved demeanor."
    Nm confused "Well?"
    c "Uh... you're right. I'll still have to make a formal request though, but I don't see why it would be declined if I explained myself well enough."
    show naomi normal with dissolve
    c "Thank you again, Naomi. It seems that your advice is really good for me."
    Nm smile "So it's settled then. You'll stay here with me and so I can keep you safe forever."
    m "Before I could think of a witty response, she pushed me down on the sofa."
    stop music fadeout 2.0
    play sound "fx/sheet.wav"
    m "Naomi turned me around to position my back on her chest while shifting us both to put her between me and the sofa's backrest."
    show naomi aroused with dissolve    
    m "Then she locked her arms under my armpits to tie me in a tight embrace."
    m "I couldn't have escaped even if I had tried."
    m "Finally, she placed her right wing over me as some kind of an impromptu dragon-blanket."
    Nm smile "Look at what a tasty morsel I have caught for my enjoyment."
    Nm "If you ever try to go back to your horrible world I will capture you before you make it to the portal and hug you until you change your mind."
    Nm stern "I'll also protect you if they try to take you back by force. I'm a lot of dragon with a few tricks they won't be expecting."
    Nm normal "You will be safe here with me for the rest of your life."
    show naomi smile with dissolve
    m "My mental resistance was waning rapidly in front of Naomi's advances. I was in no mood to refuse anything from her."
    c "T-thanks...{w} t-that's an offer I don't think I can refuse."
    #New music?
    Nm smile "When your ambassador duties are over, your new job will be to act as my body pillow whenever I feel like getting a few cuddles."
    c "(Just what have I gotten myself into?)"
    show naomi slsmile with dissolve
    c "We lied on the sofa for what seemed like forever. Occasionally Naomi shifted and rubbed my body in various ways, as if she was trying to find out where I was the squishiest."
    c "Based on the number of rubs, my lower belly seemed to interest her the most."
    c "Even though I was slowly getting more and more aroused and a little intimidated as her live body pillow, I still felt a peace I hadn't felt in a very long time."
    $ renpy.pause (3.0)
    Nm "You are a very relaxing toy."
    Nm shy "Would you like to watch a movie in this position?"
    c "I wouldn't mind that."
    Nm smile "Likewise."
    Nm "You're the perfect-sized body pillow to for me to cuddle with while watching a movie."
    Nm "I actually have one in my bedroom closet..."
    Nm shy "...but I think I prefer one that's alive."
    m "Again, my throat started feeling unnaturally dry."
    show naomi slsmile with dissolve
    m "Naomi started shyly rubbing my upper chest with her arms."
    c "..."
    m "She moved me a bit so my head was firmly lodged below her chin and then she tightened her grip on me even more to properly lock me in place."
    c "I suppose this means I passed the product testing stage?"
    Nm smile "With flying colors."
    Nm normal "So, you said you like [ecknaomim2movie] films if I'm not mistaken?"
    c "Yeah."
    Nm "You're in luck because I just happen to have a good movie of that genre in the player. I don't want to move let's just watch that one."
    c "Don't you think we should get some snacks or at least something to drink though?"
    Nm smile "Are you trying to escape?"
    Nm "Sorry, now that I finally caught myself a human I'm not letting go."
    Nm normal "We'll be fine. Also, drinking and snacking might distract us from the more important stuff."
    Nm smile "You know what I mean?"
    c "Alright, you win. It's not like I can resist anyway."
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

jump sqb_naomi_apt_movie_end

label sqb_naomi_apt_sexandeating:

    $ naomi2mood += 4
    $ naomiromance += 10
     
    Nm concern "Umm..."
    c "Come on, I like you as well."
    c "Or are you trying to say that the type of cuddling we just did is normally done among friends here?"
    show naomi shy with dissolve
    m "Seems I caught Naomi off-guard. She nervously looked me in the eyes, but then tried avoiding my gaze when I looked back."
    Nm "I... umm..."
    show naomi surprisedblush with dissolve
    m "After a moment of hesitation, she finally looked me in the eyes."
    m "She stopped for a moment and sighed loudly."
    Nm smile "I suppose it's not a secret any more that I like you as well."
    Nm "I've been thinking about dating you ever since we met."
    Nm surprisedblush "There, I finally admitted it. Are you happy now?"
    c "You're-{nw}"
    m "She cut me off before I could say anything."
    Nm confused "You've been persistent in trying to get me to admit I like you. Why else would you obey my every whim by trying to serve me whenever you can?"
    Nm normal "The weird thing about us is that even though we met very recently I feel like we've known each other for a long time." 
    Nm "I think we complement each other nicely. Also, you understand me really well and like me for what I am."
    c "What's not to like in a cute dragon such as yourself?"
    Nm shy "Oh, stop it. You're much cuter than I am."
    Nm smile "Did you know that I've always wanted a partner smaller than myself?" 
    Nm "It's so I can easily put them in their place if they misbehave."
    Nm surprisedblush "I..."
    Nm shy "I didn't mean it like that."
    Nm "Well, I did but...{w} not that directly."
    Nm sad "Sorry! I hope I didn't make you feel uncomfortable."
    c "(This just gets weirder and weirder.)"
    Nm shy "I just h-hope the feeling's mutual."
    c "Consider our session on the sofa a sign of approval."
    c "I don't mind if you tease me by objectifying me a little bit. I feel like I can trust you to have my best interests in mind."
    c "I really like you Naomi."
    play sound "fx/kiss.wav"
    show naomi aroused with dissolve
    m "With that, she suddenly kissed me on my right cheek."
    play sound "fx/lewd/lickslow.ogg"
    m "As she was pulling back from the kiss, she licked me with her long tongue, leaving some saliva behind."
    Nm smile "I really like you too."
    Nm "You're the best body pillow I've ever had. We're going to have a great time together."
    c "Yes...{w} uhh..."
    c "That sounds wonderful."
    c "Dragon hugs are certainly something I've never experienced before."
    Nm normal "I'm so happy you like me even though we're not of the same species."
    Nm smile "I hope you understand that from my perspective, you humans are the cutest."    
    Nm aroused "I've never before had such a pink and squishy boyfriend."
    c "You're going to make me blush."
    show naomi shy with dissolve
    m "Naomi looked to the side and then back at me. She seemed to be thinking about something."
    Nm confused "I just realized there is something that would improve our cuddling experience by a lot."
    Nm normal "I honestly don't understand why you humans cover up your bodies so much."
    Nm blank "Why don't you take your covers off? Having fabric between you and your partner gets in the way of having a properly intimate cuddling experience."
    m "(This escalated faster than I ever could have anticipated.)" 
    m "(How should I respond?)"
    menu:
        "Undress in front of Naomi.":
            pass
            
        "Decline.":
            c "I'm sorry, I don't feel comfortable doing that."
            Nm normal "Really? What's the big deal?"
            c "Among humans, taking your clothes off in front of someone is considered an intimate act."
            show naomi confused with dissolve
            c "It's also pretty weird to do in a living room."
            Nm "You don't...?"
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
    c "Sure. That sounds wonderful."
    show naomi normal with dissolve
    $ renpy.pause (2.0)
    stop music fadeout 1.0
    play sound "fx/undress.ogg"
    show naomi surprised with dissolve
    m "Naomi looked at me curiously as I removed my clothes piece by piece."
    show naomi surprisedblush with dissolve
    m "She was the most attentive when I started to remove my lower garments though."
    play sound "fx/undress.ogg"
    m "Her eyes fixated on my groin after I had taken my underpants off."
    Nm normal "You have fur even between your legs? That must be weird."
    c "It's called pubic hair."
    c "I can shave it off completely if it bothers you."
    Nm smile "No, it's kind of cute. I was just wondering how it must feel."
    c "..."
    Nm normal "Your male parts look pretty squishy. I bet they're very vulnerable because they hang outside of your body like that."
    m "(What have I gotten myself into?)"
    show naomi blank flip with dissolve
    m "Suddenly, Naomi focused her attention away from my groin and looked to her left."
    m "I turned to see what she was looking at."
    scene sqbnaomiapt04 with dissolvemed
    hide naomi with dissolve   
    m "She seemed to be eyeing the area right of her fridge." 
    m "I presumed that the door over there would lead to her bedroom."
    m "As I realized what she was thinking about, series cold chills went down my spine."
    m "(I hope I can make it undamaged out of this.)"
    show naomi normal with dissolve
    m "Before I had more time to ponder about my fate she walked in front of me."
    play music "mx/campfire.ogg"
    Nm smile "This sofa is awfully small for cuddling. How about we have another session in the bedroom?"
    Nm aroused "If you play it nice, we could even go further than earlier."
    Nm shy "I hope I'm not moving too quickly for you."
    m "(I guess she doesn't realize that from my perspective she's already asked to have sex with me.)"
    c "I would love some more dragon action."
    Nm smile "In that case...{w} follow me to my lair."
    Nm "Who knows, maybe you will be the first one to survive intact?"
    m "(That doesn't sound good.)"
    hide naomi with dissolve
    m "Naomi turned around and started walking towards her bedroom."
    m "I wanted to have sex with her but suddenly I was also scared of what that would entail."
    m "This was the last chance to run. If I entered her bedroom, there was no telling what would to happen to me."
    menu:
        "Follow Naomi to her bedroom.":
            m "I decided to resist the sudden, unexplained urge I had."
            pass
         
        "Escape while you still can.":
            stop music fadeout 2.0
            m "(I have to time this correctly.)"
            scene ecknaomiapt02 with dissolvemed
            play sound "fx/sheet.wav"            
            m "As Naomi got closer to her bedroom door, I quietly picked up my clothes and started sneaking towards the exit."
            m "Unfortunately, when I was halfway there Naomi heard me walking in the opposite direction."          
            m "I felt her grab my hand and I was forced to turn around to face her. I was startled, so I dropped some of my clothes on the floor."
            scene ecknaomiapt01 with dissolvemed
            show naomi concern with dissolve            
            m "(Oh no.)"
            Nm "Is something wrong?"
            c "I-I'm sorry Naomi. This is too much for me." 
            c "I changed my mind."
            Nm sad "Oh well. Did I move too quickly for you?"
            Nm "I thought we had a good time together."
            Nm concern "(This always happens to me.)"
            #music
            m "(I need to try to salvage this somehow)"
            c "Uhh...{w} you've got it all wrong."
            Nm confused "What do you mean?"
            c "You've been good to me so far, and I've enjoyed my time with you."
            Nm concern "Go on."
            c "It's all me, not you. We can meet again some other time."
            c "Also, I just remembered that I have some urgent ambassador duties that need doing."
            $ renpy.pause (2.0)
            Nm stern "Are you being serious right now?"
            Nm "That's the kind of thing they always say. Couldn't you at least come up with a less cliché way of dumping me?"
            c "Hey, I really mean what I said."
            c "Anyway, I have to go. We can just meet again some other time."
            $ renpy.pause (1.0)
            Nm "..."
            Nm annoyed "I hate it when you guys patronize me like this. Do you think I am a hatchling?"
            Nm sad "After how nice I was to you, I expected that you would at least be honest with me."
            Nm stern "Did you seriously think I wouldn't notice you trying to sneak out?"
            Nm "Go on, leave. See if I care."
            c "Don't you think you're overreacting just a little bit?"
            c "You have to calm down right now!"
            Nm annoyed "Shut up!"
            c "..."
            Nm stern "Take your stupid covers and leave."
            c "Huh, you're going to order me around just like that? This is really it for you then."
            c "Or did you forget who I am?"
            Nm "I hate your condescending flat-face so much."
            show naomi annoyed with dissolve
            m "Naomi looked like she was going to get violent."
            Nm "Get out NOW!"
            hide naomi with dissolve
            scene ecknaomiapt02 with dissolvemed
            m "Fearing for my life, quickly walked up to the door and grabbed the handle."
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
            m "At this point of escalation had no choice but to just leave her alone."           
            m "Somehow I knew that due to being this rude to Naomi, she wouldn't ever want to see me again."
            stop sound fadeout 1.0
            play sound "fx/steps/steps.ogg"
            m "Shocked at what had just happened, I didn't even notice Sebastian napping outside Naomi's apartment."
            m "Not even bothering to put my of my clothes on, I slowly wandered back to my apartment and went straight to bed."
            stop sound fadeout 1.0
            m "My dreams were full of fire and suffering, and I woke up several times during the night in cold sweat."
    
            $ naomistatus = "bad"
            $ naomiavailable = False
            $ naomiscenesfinished = 2
            if chapter4unplayed == False:
                 jump chapter4chars
            elif chapter3unplayed == False:
                 jump chapter3chars
            elif chapter2unplayed == False:
                 jump chapter2chars
            else:
                 jump chapter1chars      
     
    $ renpy.pause (1.0)
    scene black with dissolvemed
    hide naomi with dissolve
    play sound "fx/door/door_open.wav"
    m "I followed Naomi as she walked up to her bedroom door and nudged it open with her snout." 
    scene eckannabedroom4 with dissolvemed
    show naomi normal with dissolve
    Nm "Here we are."
    Nm smile "When we first met I didn't think I would invite you to my bedroom on our second date." 
    Nm "Like I said before, there might be something special between us."
    Nm shy "I guess we'll find out about that soon enough."
    c "Interesting. Did you finally come around to admitting that our get-togethers were actually dates from the get-go?"
    Nm stern "Don't ruin the mood by being a smart ass."
    c "Sorry."
    show naomi smile with dissolve
    m "After my apology Naomi walked to up to the bed and gave me an inviting look."
    play sound "fx/bed.ogg"
    m "She climbed on the bed and rolled on her back, spreading her wings wide."
    show naomi surprisedblush with dissolve
    m "Then she turned to the right and straightened her legs, while still holding my gaze."
    m "(You really realize how much bigger she is compared to a human when she straightens up like that.)"
    show naomi smile with dissolve   
    m "Naomi patted the empty space on her right side with her open palm."  
    Nm "Are you coming or not? This bed feels empty without you."
    m "I gulped, and without saying anything I walked up to the right side of the bed."
    play sound "fx/sheet.wav"
    m "I sat down on the side, turned and began to lower myself on Naomi's wing, preparing to position myself to have my back against her like before."
    Nm smile "That won't do at all. I want to feel your squishy belly rub against mine."
    play sound "fx/bed.ogg"
    m "With those words she turned me around and hugged me tightly before I could protest."
    m "This time she had her arms around me and my head was lodged firmly under her chin like before."
    show naomi slsmile with dissolve
    m "She finished the job by wrapping her wings around me."
    Nm shy "Don't hesitate to tell me if I hug you too tightly or make you feel uncomfortable in any way."
    Nm smile "I wouldn't want to damage my toy, physically or mentally."
    m "She was very warm and I could now properly feel her powerful heartbeat and rumbling breath."
    c "I'm fine. This feels great."
    m "(I can barely move.)"
    m "This position aroused me to no end. To make things worse, my dick was rubbing against Naomi's even warmer lower belly." 
    m "I was hardening up rapidly."
    m "(Oh no. I hope her learning more about my mammalian traits won't be too embarrassing.)"
    Nm shy "Have I now convinced you that your place is here with me?"
    c "You convinced me a long time ago. I wouldn't trade being here with you for anything."
    Nm smile "Likewise. When we first met, somehow I immediately knew we would get along nicely."
    show naomi slsmile with dissolve
    m "Suddenly, she locked me in place with her legs, shifting me around a little bit to hold me even more tightly than before."
    play sound "fx/purr.ogg"
    m "After that she purred while tying my ankles together with the narrow part of her tail."
    Nm "Very nicely... in fact."
    m "A terrified feeling washed over me as I realized that due to my position shifting again, my erect cock was now poking her belly."
    Nm "..."
    stop music fadeout 1.0
    stop sound fadeout 1.0
    Nm shy "Is that what I think it is?"
    c "I'm sorry!" 
    c "I can't control it. My penis gets erect on its own whenever I am sexually stimulated."
    Nm surprisedblush "Oh..."
    c "..."
    c "This doesn't weird you out?"
    m "Naomi paused to think for a moment."
    Nm smile "Why would you being aroused in a way normal to you weird me out?"
    Nm slsmile "After all it just means that...{w} you know..."
    play sound "fx/lewd/lickslow.ogg"
    m "She licked my forehead with her long tongue."
    play music "mx/treetops.mp3"
    Nm smile "That you actually want to have sex with me?"
    m "Her remark made me feel like my heart had just jumped to my throat. To make things worse, my face was feeling so hot, I bet it had turned completely red."
    m "(Why am I so anxious?)"
     
    if modinfo.has_mod("BangOk?") and bangok_four_bryce1_unplayed == False or bangok_four_xsebastian_unplayed == False or bangok_four_anna2.unplayed == False:
        m "(It shouldn't be that much different with Naomi.)"  
    else:
        m "(It shouldn't be that much different with a dragon.)"
         
    m "(I need to calm down.)"
    m "She interrupted my line of thought."
    Nm normal "Have you thought of what other humans would think if they found out that you wanted to have sex with a dragon?"
    m "After a moment of silence, I gulped loudly, which she surely heard."
    c "B-but t-there aren't-{nw}"
    Nm surprisedblush "Oh, you've fantasized about doing it with a dragon before?"
    m "I could feel Naomi starting to heat up."
    Nm slsmile "Wanting have sex with another sentient species...{w} now that's a kink I like."
    m "My stomach was full of butterflies and I was so embarrassed I felt like I was going to choke."
    m "Somehow I managed to speak up yet again."
    c "W-well I-{nw}"
    Nm surprisedblush "Don't worry about it."
    Nm smile "By the way, your face is completely red. Are you feeling okay?"
    m "Naomi moved her maw closer. I could feel her hot and almost steamy breath on my face."
    c "Yes... umm..."
    c "I'm j-just-{nw}"
    Nm "Feeling embarrassed and aroused? That's exactly why I'm teasing you."
    Nm "I knew you would be so unbelievably cute flustered like this."
    Nm slsmile "I'm going to keep you safe here with me and never let you you go."
    m "I felt so anxious I was about to have some kind of weird seizure. Fortunately, Naomi was holding me so tightly I couldn't move at all."
    m "My resistance was indeed weak and pathetic."
    Nm smile "I know just how to cool your face and calm you down."
    show naomi slsmile with dissolve
    play soundloop "fx/lewd/lickslow.ogg" fadein 1.0
    m "Suddenly Naomi started licking my entire face in circles with her long tongue, mostly focusing on my presumably red cheeks."
    m "(I don't think she is being genuine in trying to cool me down.)"
    m "(Not that I mind.)"
    $ renpy.pause (2.0)
    stop soundloop fadeout 2.0
    c "I like it when you lick me like this."
    Nm smile "Same, because you're so delicious."
    Nm shy "Do you really want to go further with me?"
    m "I felt like I had no choice but to fuck her immediately or I was going to die due to my heart bursting out of my chest due to a lack of release."
    c "Yes..."
    Nm normal "So, I saw earlier where your genitals are located. I don't think our anatomies are too different to make fucking inconvenient for us."
    
    if modinfo.has_mod("BangOk?") and  bangok_four_anna2.unplayed == False:  
        c "Actually, our anatomies aren't too different. I already had sex with Anna."
        Nm confused "What, really? How'd you manage to get her to like you enough for that?"
        Nm smile "Hold on...{w} did she do it for science?"
        c "Maybe, but she's also rather promiscuous. Not that I mind, of course."
        c "So, how do you want to proceed from here?"
        Nm normal "I have an experiment of my own in mind."
     
    elif modinfo.has_mod("BangOk?") and bangok_four_bryce1_unplayed == False:
        c "Actually, Our anatomies aren't too different. I had sex with Bryce after I went drinking with him."
        #More accurate references
        Nm confused "What, really? I'm surprised you can still walk."
        c "The alcohol helped a lot. And of course lots of lube."
        c "So, how do you want to proceed from here?"
        Nm smile "Let me think..."
    
    elif modinfo.has_mod("BangOk?") and bangok_four_xsebastian_unplayed == False:
        c  "Actually, I already had sex with Sebastian. Our anatomies aren't too different."
        Nm "Really? I'm not surprised, he's kinda cute."
        #More
    
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
    
    Nm slsmile "I'll try more thing to get you properly in the mood."
    m "Naomi freed one of her arms a little bit and used her claw to nudge my head upwards."     
    m "Then she moved her mouth to mine, kissing me..."
    play sound "fx/lewd/altpen.ogg"
    m "...but also going through my lips with her long tongue."
    play soundloop "fx/lewd/pussy.ogg"     
    m "Then she started penetrating my mouth and tickling the inside of my upper jaw with the tip of her tongue."
    m "It was an intimate tickling sensation I'd never quite had before."
    m "The only thing I could do was to focus on breathing through my nose and to try to stay as still as possible."
    m "Again, I felt like my chest was going to explode."
    m "(I'm going to die of a heart attack.)"
    stop soundloop fadeout 2.0
    Nm confused "You're completely powerless to do anything to resist my advances, aren't you?"
    Nm smile "Alright, we've had enough foreplay."
    Nm "Is fucking me sideways in this position fine by you?"
    m "I was surprised she even asked for my opinion. I managed to mumble up a response."
    c "I would love to."
    Nm "Good little obedient toy."
    play sound "fx/sheet.wav"
    m "Naomi released me from the prison of her legs and spread them a bit."
    Nm shy "Can you see the slit between my legs?"
    
    if modinfo.has_mod("BangOk?") and persistent.bangok_cloacas == False:
        m "I looked down at Naomi's groin, seeing a single vertical slit and an asshole below it."
        m "It seemed that I needed to go down a little bit to reach her pussy and also to have some leverage to thrust inside."        
    else:
        m "I looked closely at Naomi's groin, now seeing a previously well-hidden horizontal slit."
        m "She freed her grip enough on me so I could move my arm around in order to spread her slit to feel what I was dealing with."
        show naomi aroused with dissolve
        play sound "fx/lewd/penfast.ogg"
        m "As I did it, Naomi shuddered in arousal and some love juices escaped from her cloaca onto my hand."
        play sound "fx/lewd/penslow.ogg"
        m "Going a little bit deeper, I could feel two separate passages positioned vertically from each other."
        
        if modinfo.has_mod("BangOk?") and  bangok_four_anna2.unplayed == False:
            c "It's a bit different from Anna's."
            
        Nm smile "Like what you see?"
        c "You want me to penetrate your upper passage, right?"
        Nm shy "Well yes..."
        show naomi smile with dissolve
        play sound "fx/lewd/lickslow.ogg"
        m "Suddenly, Naomi flicked my nostrils with her long tongue. I barely managed to receive it without shuddering uncontrollably."
        Nm aroused "...because that's where my eggs come from."
        m "(What kind of fantasies is she having right now?)"
        m "Looking down again after regaining my composure, it seemed that I needed to go down a little bit to reach her vaginal passage and also to have some leverage to thrust inside."       
 
    Nm normal "Did you figure out what to do?"
    c "Yes, but I can't penetrate you from this position. My testicles are in the way of bending my dick downwards properly."
    Nm shy "Oh."
    c "Could you fully loosen your grip on me so I can go down to get a better position?"
    Nm smile "Anything for you."
    c "Also, shouldn't we be using a condom?"
    Nm confused "No, that won't be necessary."
    Nm normal "I don't have any STDs and I trust don't have either, otherwise you wouldn't have agreed to have sex with me."
    Nm shy "Besides, I want to feel your human cum inside me."
    m "(I suppose another reason we don't need to use a condom is that I can't get her pregnant due to us being of different species.)"
    m "(Did she neglect to mention that because it's too obvious?)"
    m "(I suppose I'll just have to do my best to satisfy her kinks.)"
    Nm confused "So, will you cum inside me?"
    c "Whatever works for me. I just want to fuck you right now."
    Nm shy "That's actually the nicest thing you've said to me so far."
    m "I moved downwards, my hands trailing behind Naomi's back."
    m "I positioned myself between her strong legs. Due to our size difference, in this position my face only reached up to her chest."
    m "I placed my hands behind Naomi's lower back in order to get more leverage as I prepared to penetrate her."
    c "H-here I go."
    Nm slsmile "Good, I've been waiting for this."
    play sound "fx/lewd/penslow.ogg"
    m "As I penetrated her opening, she locked me tightly in place with her legs."
    Nm smile "Caught you!"
    play sound "fx/lewd/penfast.ogg"
    m "After the initial penetration, I moaned as I bucked myself as far as I could go in a single thrust." 
    m "The sensation of fully plunging yourself into someone much bigger than you was something I had never quite experienced before."
    
    if modinfo.has_mod("BangOk?") and  bangok_four_anna2.unplayed == False:    
        m "(Naomi's a lot tighter than Anna. That's surprising since Naomi is so big.)"
        m "(I suppose Anna really has had a lot of larger partners.)"
        m "(I'm still fortunate to have an above average penis, or else I most likely couldn't get her off with it at all.)"
    else:
        m "(Naomi's a lot tighter than I would expect from someone much bigger than me.)"
        m "(I suppose she's only had smaller partners, like she implied before.)"
        m "(I'm still fortunate to have an above average penis, or else I most likely couldn't get her off with it at all.)"
    
    Nm confused "Was that it? Are you going to pump at all?"
    c "Uhh... I was lost in thought."
    Nm stern "This isn't the best time to get lost."
    c "Sorry!"
    play soundloop "fx/lewd/penslow.ogg"
    show naomi normal with dissolve
    m "After having to apologize yet again I started penetrating Naomi's pussy with long, thorough thrusts."
    Nm smile "Good little human."
    m "Naomi wrapped her wings around me like before." 
    m "In this moment, she was the only thing that existed for me in the world."
    Nm aroused "You belong to me now." 
    Nm "The only way to go is forward."
    m "She was right, because due to being locked in place by her strong legs, thrusting forward was just about the only movement I could do."
    Nm slsmile "I'll only let you go if you cum inside me."
    $ renpy.pause (5.0)
    stop soundloop
    play soundloop "fx/lewd/penfast.ogg"
    m "As I got more used to the position I was in, I started thrusting faster into Naomi."
    m "I couldn't last very long though. The extended tease had exhausted my stamina."
    m "Suddenly without warning, a release started rapidly building up inside me." 
    m "After the realization that I was going to cum soon, I hoped she would be satisfied with my performance or at least be understanding of my predicament."
    c "Naomi... I'm going to cum."
    Nm surprisedblush "So soon? Fine, but don't even think about pulling out."
    Nm shy "N-not that I would let you anyway."
    Nm smile "I thought humans would last longer than this."
    c "It's your fault for teasing me so much. I've been hard for hours."
    Nm surprisedblush "That's what someone with no stamina would say."
    stop soundloop
    play soundloop "fx/lewd/altpen.ogg"
    m "Since I had gotten the permission to finish, I started preparing to shoot my cum inside Naomi by thrusting deeper."
    c "I'm going to paint your insides white with human cum!"
    Nm confused "Did you come up with that line all on your own?"
    Nm smile "Pun intended, of course."
    Nm "Anyway, I doubt your output is enough to accomplish that." 
    Nm "You're welcome to try your best regardless."
    $ renpy.pause (2.0)
    m "I couldn't hold out any longer."
    stop soundloop fadeout 2.0 
    play sound "fx/lewd/cum.ogg"
    queue sound "fx/lewd/penslow.ogg"
    $ renpy.pause (1.0)
    m "I grunted loudly as I came."
    c "Urgh!!!Ahh!!!{nw}" with hpunch
    play sound "fx/lewd/penslow.ogg"
    queue sound "fx/lewd/cum.ogg"
    show naomi slsmile with dissolve
    m "I bucked against Naomi for the last time to release my second rope of cum, and she let out a content sigh."
    Nm smile "Well done, tiny pink human."
    Nm "I can feel a whole lot of your sticky seed inside me. You really didn't lie about being pent up."
    Nm shy "Unfortunately, you didn't manage to get me off." 
    Nm normal "If you can't go again you can finish me off with your mouth."
    #Choice between oral or another round of the same
    
    #Another round
    c "I still have another round in me. Just give me a few moments to recover."
    Nm stern "Try to last longer this time."
    c "I-I'm sorry. I promise I'll do better."
    
    show naomi smile with dissolve
    play soundloop "fx/lewd/penslow.ogg"
    m "Some of my seed seeped out of Naomi's pussy as I fucked her, which aroused me even further since it reminded me of what I had just done a few moments earlier."   
    if modinfo.has_mod("BangOk?") and bangok_four_bryce1_unplayed == False or bangok_four_xsebastian_unplayed == False or bangok_four_anna2.unplayed == False:
         m "(I can't believe Naomi let me cum in her.)"
    else:
         m "(I can't believe I just came inside a dragon.)"
    
    stop soundloop fadeout 1.0
    c "That was the best sex I've ever had. I think the hours-long tease had something to do with it."
    Nm normal "It was certainly fun to play with someone who is too weak to resist anything I do to them."
    Nm smile "I'm looking forward to many more sessions like this."
    m "(I'm doomed.)"
    c "M-me too."
     
    c "Naomi, I am unable express with words how much I like you."
    c "I want to marry you and stay with you forever."
    Nm surprised "Is that how it works in your world?"
    Nm confused "We've only had sex once so far. That doesn't mean we should get married."
    Nm normal "Marriage is a long-term commitment."
    c "I'll prove myself worthy of you."
    c "What should we do next?"
    c "Wanna take a shower together?"
    Nm "Sure. I need to get cleaned up and I bet you do too."
    c "Alright."    
    stop music fadeout 2.0
    play sound "fx/rumble.ogg"
    $ renpy.pause (5.0)
    show naomi concern with dissolve
    m "(Looks like we forgot to eat.)"
    Nm normal "Oh, you're hungry?" 
    Nm "I've got some stuff we could cook together or we can order some food if you don't feel like doing that."
    c "Let me handle it. I would love to cook for you."
    c "I want to somehow pay back all the hospitality I've gotten here so far."
    Nm shy "Oh, you don't have to. I enjoyed myself too."
    c "I insist. I love cooking."
    c "Besides, I want to find out how similar your food products are to ours." 
    c "Personally, I came here to learn more about your people after all."
    Nm smile "Well, if you put it like that...{w} I won't turn down a delicious meal. I also would love to find out if human cooking is different from ours."
    c "Don't worry, I'll cook a a few dishes. We have plenty of time left after all."
    scene black with dissolvemed
    play sound "fx/door/door_open.wav"
    m "With those words, I walked up to the door and exited the room back to Naomi's living room. She followed behind me."
    scene ecknaomiapt02 with dissolvemed
    play music "mx/airborne.mp3"
    show naomi normal with dissolve
    c "First things first, after our session I really need drink a liter of water, or two. Would you like something to drink as well?"
    Nm "Sure, put it on the table over there." 
    Nm "I'll go clean myself up in the bathroom while you get set up. If you need any help figuring out where everything is just give me a shout."
    hide naomi with dissolve
    play sound "fx/door/door_open.wav"
    m "Naomi walked in to what I presumed to be the bathroom."
    m "(Let's see what kind of stuff she has in the fridge.)"
    play sound "fx/crapfridge.mp3"
    m "As I opened the fridge, I noticed that a lot of the packaging had familiar shapes and also somewhat similar labels to ours."
    m "(Oh right, she wanted to drink something.)"
    #Sound?
    m "I picked a carton of orange juice from the back of the fridge."
    m "(She liked juice, right?)"
     
    
    m "(There's so much stuff in her kitchen you'd think she cooks at home.)"
    m "(Did she buy all this stuff just to impress me? That's cute.)"
    m "(Wait, how did she know I like cooking?)"
    
    #Sound?
    m "With some effort, I piled all the foodstuffs and ingredients on Naomi's kitchen counter in an organized fashion."
    m "(This is going to be a challenge.)"
    m "(I think at first I should just move everything on the counter and separate what I definitely want to use.)"
    m "(Second, I'll put back what I don't think I want to use.)"
    m "(I can always take something back if I need it after all.)"
    $ renpy.pause (2.0)
    m "(I am definitely going to fry some noodles. I'll use chicken as well, although I am not yet sure how.)"
    #Sound?
    m "(I'll take a pack of egg noodles and some lightly salted chicken fillets.)" 
    m "(I like the flexibility of these fillets because you can always cut them to pieces if you want, but also season them yourself.)"
    m "While I was pondering, Naomi came to check on what I was doing."   
    show naomi normal with dissolve
    Nm "So, you found where everything was?"
    c "Yes, thank you."
    c "You have so much stuff in your kitchen that I'd have guessed you cook a lot if you already didn't tell me otherwise."
    Nm shy "Well..."
    Nm normal "I wanted to try something new since you were coming over. Going on a shopping spree just felt like the right thing to do."
    Nm smile "Anyway, looks like my plan worked. I managed to bribe you into cooking for me."
    c "Oh, you got me. This is going to be fun, I promise."
    Nm "I'll hold you to that."
    hide naomi with dissolve
    m "With that, she walked up to the sofa and jumped on it in one, smooth motion."
    m "I watched her as she flexed herself, not unlike a big cat."
    
    $ renpy.pause (1.5)
    show ecknaomicg1 at Pan ((250, 230), (620, 50), 15.0) with dissolvemed
    $ renpy.pause (7.5)
    
    Nm "Like what you see?"
    c "You're very cute."
    Nm "Hurry up with the cooking, or I'll have to eat you instead."
    c "..."
    
    scene black with dissolvemed
    $ renpy.pause (1.0)
    scene ecknaomiapt02 with dissolvemed
    m "(Where was I?)"
    m "(Oh right, what else I should pick to cook with? Let's see what we got.)"
    m "(This white, mint-flavored mouflon and aurochs cheese looks remarkably similar to something we used to have. I'll cut it to pieces and cook it with the noodles.)"
    m "Nice, we got soy sauce, wing sauce, brown sugar and ginger power to season the fried noodles. Let's start by heating up the pan first.)"
    #Sound?
    m "I put a pan on the cooktop and as I was going to turn on the stove I realized something.)"
    m "(Wait a minute.)"
    m "(Let's first make sure I don't get eaten by a hungry dragoness.)"
    c "Naomi, would you like some bread sticks as appetizers?"
    Nm "Sounds great to me. I was just going to come over there and eat you."
    c "If you eat me, I won't be able to cook for you."
    m "I focused back on the task at hand and quickly picked all the required ingredients for the appetizers."
    m "(Toast, garlic, black pepper, salt and oregano here we go.)"
    m "(Wait, where's the olive oil?)"
    #Sound
    m "I searched all her cabinets and found it hidden behind some boxes."
    m "(There we go.)"
    Nm "Need help finding something?"
    c "I'm fine. I was just looking for some olive oil."
    m "(Finally, we can get started.)"
    m "I turned on the oven and prepared two baking trays with baking paper."
    m "(I suppose I'll have to cook a big pile. Luckily, slicing the toast won't take too long if I do it efficiently.)"
    m "(The oven probably isn't ready after I am done with the cutting but I can always start preparing for something else.)"
    m "(Then, when the bread sticks are baking I can start planning for the main courses."
    m "(Oh yeah, I have to also prepare the mix that is used to flavor the bread sticks. Who knows if the oven will be ready when I've done that."
    m "(Multitasking and planning ahead is so much fun.)"
    m "I opened a bag of toast and put several slices on top of each other on the cutting board."
    play sound "fx/crapcuttingboard.mp3"
    m "Then I cut the bread into neat little sticks, moved them to the side and prepared cut another batch of toast."
    m "After a couple of minutes, I managed to slice the entire bag of bread."
    #Sound?
    m "I peeled the garlic and crushed them into a bowl with a pestle and mixed in some olive oil, pepper and salt to create the flavoring mix."
    m "I placed all the bread sticks on the two baking trays and used a spoon to apply the flavoring mix."
    m "(Yep, looks like I have some time left since the oven isn't ready yet.)"
    
    play sound "fx/fry.ogg"
    m "(Let's put in some giant prawns as well. Luckily they are already prepared and seasoned.)"
    m "After adding the prawns I put the lid on the pan and set another timer to 8 minutes."
    m "(I'll have to remember to mix the noodles every once in a while. What should I do next?)"
    
    m "(Perfect, we have all the ingredients for batter plus some herb butter. The last one is really lucky for us, because obviously I wouldn't have had the time to make some myself.)"
    m "(I know what to do with the chicken fillets now.)"
    
    m "(Eight chicken breasts should be enough for both of us. She can always eat the rest tomorrow if there's some left over.)"
    m "This was the most time-consuming part of my cookout, but it was over quickly because I knew the effort would be well worth it."
    
    m "As I was mashing the potatoes, I poured in some milk."
    m "(That should be enough for now. It's better to be careful to not use too much milk at first because I can always put more later.)"
    
    m "I stuck a dragon-sized fork for Naomi in the very large bowl of fried noodles."
    
    Nm "I really like the crunchiness of your chicken."
    c "I love the taste of batter too, so I breaded the chicken breasts twice."
    Nm smile "Interesting. Even more than that I love how the herb butter just bursts inside your mouth when you bite in."
    c "Thank you. They are indeed a lot juicier than your basic chicken breasts."
    
    c "I call it simple but delicious. This cooking philosophy leaves more time for eating."
    Nm smile "I love it. That's the most important part."
     
    stop music fadeout 1.0
    hide naomi with dissolve
    scene black with dissolvemed
    $ renpy.pause (1.0)
    play music "mx/airborne.mp3"
    scene ecknaomiapt01 with dissolvemed
    show naomi normal with dissolve
    
    #Make it so that its very late when the PC leaves, since he and Naomi did a lot more stuff in this timeline
     
jump sqb_naomi_apt_sexandeating_end

