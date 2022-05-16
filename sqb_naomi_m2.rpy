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
    c "If you hugged someone smaller, you'd make them feel better in no time with your sheer hugging power."
    show naomi surprisedblush with dissolve
    m "(Why did I say that?)"
    Nm shy "I suppose you have a point."
    Nm smile "I bet if I caught a puny human like you, they'd never be able to escape my clutches."
    c "Actually that's what dragons sometimes do to humans in our fiction."
    c "Usually the dragons who catch humans are considered male though and they catch humans of the opposite sex."
    Nm confused "That sounds weird. Do you know why?"
    c "Well, I didn't really study literature or specialize in cultural history so I don't know."
    m "I had a sudden urge to say something funny."
    c "Actually that trope makes no sense to me because I wouldn't mind being caught by a female dragon."
    Nm stern "Don't get any funny ideas about my remark."
    Nm normal "I was just being hypothetical."
    c "Yes, of course."
    m "(What have I done?)"
    c "Anyway, as a sociologist the most fascinating thing about our species' future relationship is how we can complement each other."
    c "Kind of like how your different species of dragons are best suited for different kinds of tasks."
    show naomi blank with dissolve
    c "I know runners are better at doing tasks that require precision than other dragons, but humans would be way better."
    c "For articulate tasks, our limbs are much better than anything you've seen before."
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
    c "It wasn't our choice. Most of us had to settle within a reasonable distance in a place where at least some of the infrastructure was intact."
    c "Standing in a peaceful place such as this makes me both nostalgic and sad."
    c "Why did things have to go so wrong? What did we do to deserve such hardship?"
    show naomi sad with dissolve
    c "Living in my world is like a nightmare that never ends."
    Nm "I'm so sorry to hear that, [player_name]." 
    show naomi shy with dissolve
    m "Naomi seemed to be thinking about something."
    Nm "Just a funny thought..." 
    Nm "I wouldn't mind if you stayed here with me. You're... um... good company."
    Nm smile "You should also invite your friends. I would love to meet more humans. Like I said before, there's plenty of room for everyone."
    m "Naomi caught me off-guard again. I felt a surge of emotions."
    m "A tear slid down my cheek and I sniffed."
    c "Thank you, Naomi."
    c "I would love to take you up on your offer, if I can."
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
            Nm normal "Don't worry, I can take it."
            
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
    c "Before I became ambassador I was just doing odd jobs to survive. It wasn't all that bad if you look at the big picture."
    c "To fast forward, we found our portal on a scouting mission and sent Reza to investigate after the initial contact."
    c "In his case, there wasn't really any kind of process to select the most suitable person to go since we were desperate for any kind of help or even information." 
    c "I have to admit that we didn't really care if he died on the mission."
    c "Reza was known to be a troublemaker so him dying really wouldn't have been big loss. You wonderful dragons could have been savage, man-eating monsters for all we knew."
    Nm smile "You've seen nothing yet. Just stick around for long enough and I might show you all my capabilities."
    m "Her remark almost made me jump up from the sofa. I managed to mostly control myself but I'm sure Naomi saw me twitch."
    c "I... uhh..."
    c "Where was I..."
    show naomi normal with dissolve
    c "Anyway, I was selected from a large pool of applicants to be the second person to visit your world. Due to my expertise in both biology and sociology I was uniquely qualified."
    c "Sending someone takes a lot of power so it'll just be me and Reza interacting with you until we get one of your generators."
    c "Reza's behavior leaves a lot to be desired." 
    c "Well... that would be the understatement of the century. Murdering someone is unforgivable even in our harsh world."
    c "I hope we catch him soon and end this mess."
    Nm smile "I hope so too. I want to meet some more cute humans and tell them we'll welcome all of them with open arms."
    c "Thank you Naomi. You caring about us so much makes me feel very happy."
    m "Suddenly I started to feel another surge of emotions. My throat started feeling dry and I wanted to cry."
    show naomi surprisedblush with dissolve
    c "H-honestly your unconditional kindness is unexpected. I don't know what we did to deserve it."
    c "Being as dependent on technology as we were wasn't good. The mess we're in is of our own making."
    Nm stern "Don't say that, [player_name]. Everyone needs help sometimes."
    Nm confused "Just make sure you have good friends..." 
    Nm smile "...or something more to help you out."
    m "Naomi moved closer towards me on the sofa."
    c "Thank you again, Naomi. I really mean it."
    m "After those words, she leaned towards me a little bit more."
    Nm shy "Would you like a hug? I don't want to see a cute human like you to be sad like this ever again."
    m "I agreed, because I liked her and turning her down would have been rude."
    c "Uhh... sure."
    show naomi slsmile with dissolve
    m "With that, Naomi leaned in closer and I returned the gesture by wrapping my arms around her upper body."
    m "She was warmer than I had expected and I could hear her strong breathing while we hugged."
    Nm smile "Feeling better yet?"
    c "Yes, thank you." 
    c "Being hugged by a dragon really made me feel better. I don't know what to say."
    m "After the hug, I tried disentangling myself from her, but she wouldn't let me go."
    Nm confused "What's wrong?" 
    Nm slsmile "Let's stay like this so you won't feel sad while finishing your story."
    c "That works for me."
    c "Anyway to continue..."
    show naomi normal with dissolve    
    c "Like you already know, our most important goal is to get one of your generators."
    c "A lot of tech, especially advanced medical equipment, was spared in our city. The problem is that soon we won't have enough power to run them properly." #Thanks for the lore, MBS
    c "I just hope my city-state is still standing when it's time to go back."
    m "As I said that I was hit by the sudden realization that I might not be able to return here after my mission was completed."
    m "After all, given the precarious situation we were in, who would care about researching dragon society and culture?"
    m "Because of this realization, it was the first time when thinking about having to return made my stomach feel like an endless pit."
    m "A kind of panic was setting in me, so I decided to confide in Naomi."
    show naomi blank with dissolve  
    c "Sorry, I got lost in thought."
    c "Anyway, I hate to admit that I am not looking forward to the day when I finally have to go back to my own world"
    show naomi concern with dissolve
    c "Because of that I have a constant feeling of dread and helplessness in the back of my head that just won't go away." 
    c "I know I shouldn't say this but if I am frank, I don't want to leave at all because your world is too wonderful."
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
    c "Uh... you're right. I'll still have to make a formal request though, but I don't see why it would be declined if I explain myself well enough."
    show naomi normal with dissolve
    c "Thank you again, Naomi. I don't know what I would do without your advice."
    Nm smile "So it's settled then. You'll stay here with me and so I can keep you safe forever."
    m "I was confused again by how direct she was. Before I could think of a response she pushed me down on the sofa."
    stop music fadeout 2.0
    play sound "fx/sheet.wav"
    m "Naomi turned me around to position my back on her chest while shifting herself between me and the sofa's backrest."
    show naomi slsmile with dissolve    
    m "Then she locked her arms under my armpits to tie me in a tight embrace."
    m "I couldn't have escaped even if I had tried."
    m "Finally, she placed her right wing over me as some kind of an impromptu dragon-blanket."
    Nm smile "Look at what a tasty morsel I have caught for my enjoyment."
    Nm "If you ever try to go back to your horrible world I will capture you before you make it to the portal and hug you until you change your mind."
    Nm stern "I'll also protect you if they try to take you back by force. I'm a lot of dragon with a few tricks they won't be expecting."
    Nm normal "You will be safe here with me for the rest of your life."
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
    c "I wouldn't mind that. I'm now feeling much better thanks to you."
    Nm smile "Likewise."
    Nm "You're the perfect sized body pillow to for me to cuddle with while watching a movie."
    Nm "I actually have one in my bedroom closet..."
    Nm shy "...but I think I prefer one that's alive."
    m "Again, my throat started feeling unnaturally dry."
    show naomi slsmile with dissolve
    m "Naomi started shyly rubbing my upper chest with her arms."
    c "..."
    m "She moved me a bit so my head was firmly lodged below her chin and then she tightened her grip on me even more."
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
    c "Are you trying to say that the type of cuddling we just did is normally done among friends?"
    show naomi shy with dissolve
    m "It seems I caught Naomi off-guard. She nervously looked me in the eyes, but then tried avoiding my gaze when I looked back."
    Nm "I... umm..."
    m "Naomi looked me in the eyes."
    m "She stopped for a moment and then sighed loudly."
    Nm surprisedblush "I suppose it's not a secret any more that I like you."
    Nm smile "I've had you in mind for some time. There, I finally admitted it officially."
    Nm confused "You've been persistent in trying to get me to admit I like you. Why else would you obey my every whim and try to serve me whenever you can?"
    Nm normal "The weird thing about us is that even though we met very recently I feel like we've known each other for a long time." 
    Nm "I think we complement each other nicely. Also you understand me really well and like me for what I am."
    c "What's not to like in a cute dragon such as yourself?"
    Nm shy "Oh, stop it. You're much cuter than I am."
    Nm smile "I've always wanted a partner smaller than myself. That's because I can easily put them in their place if they misbehave."
    Nm surprisedblush "I..."
    Nm shy "I didn't mean it like that."
    Nm "Well, I did but...{w} not that directly."
    Nm sad "Sorry! I hope I didn't make you feel uncomfortable."
    c "(Is the same thing that's been happening to me, happening to her as well?)"
    c "(This just gets weirder and weirder.)"
    Nm shy "I just h-hope the feeling's mutual."
    c "Consider our session on the sofa a sign of my approval to that."
    c "I don't mind if you tease me by objectifying me a little bit. Somehow I feel like I can trust you have my best interests in mind."
    c "I like you a lot, Naomi."
    play sound "fx/kiss.wav"
    show naomi slsmile with dissolve
    m "With that, she kissed me on my right cheek."
    play sound "fx/lewd/lickslowlouderlonger.ogg"
    m "As she was pulling back from the kiss, she licked me with her long tongue, leaving some saliva behind."
    Nm smile "I love you."
    Nm "You're the best body pillow. We're going to have a great time together."
    c "That sounds wonderful."
    c "Dragon hugs are certainly something I've never experienced before."
    Nm normal "I'm so happy you like me. I've never had such a cute and squishy boyfriend."
    show naomi shy with dissolve
    m "Naomi looked to the side and then back at me. She seemed to be thinking about something."
    Nm confused "I just realized there is something that would improve our cuddling experience by a lot."
    Nm normal "I honestly don't understand why you humans cover up your bodies."
    Nm blank "Why don't you take your covers off? Having fabric between you and your partner gets in the way of having a properly intimate experience."
    m "(This escalated faster than I ever could have anticipated.)" 
    m "(How should I respond?)"
    #A choice for the sake of it?
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
    m "Her eyes fixated on my crotch after I had taken my underpants off."
    Nm normal "You have fur even between your legs? That must be weird."
    c "It's called pubic hair."
    c "I can shave it off completely if it bothers you."
    Nm smile "No, it's kind of cute. I was just wondering how it must feel."
    c "..."
    Nm normal "Your male parts look pretty squishy. I bet they're very vulnerable because they hang outside of your body like that."
    m "(What have I gotten myself into?)"
    show naomi blank flip with dissolve
    m "Naomi focused her attention away from my genitals and looked to her left."
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
    Nm surprisedblush "This sofa is awfully small for cuddling. How about we have another session in the bedroom?"
    Nm smile "If you play it nice, we could even go further than earlier."
    Nm shy "I hope I'm not moving too quickly for you."
    m "(I guess she doesn't realize that from my perspective she's already asked to go in the bed with me.)"
    c "No, not at all. I like you very much."
    Nm normal "In that case...{w} follow me please."
    $ renpy.pause (1.0)
    scene black with dissolvemed
    hide naomi with dissolve
    play sound "fx/door/door_open.wav"
    m "She walked up to the door and nudged it open with her snout."
    m "I followed her, barely resisting the urge of grabbing my clothes and getting the hell out of here." 
    m "Sure, I wanted to have sex with her but I was also scared of what that would entail."
    scene eckannabedroom4 with dissolvemed
    show naomi normal with dissolve
    Nm "Here we are."
    Nm smile "When we first met I didn't think I would invite you to my bedroom on our second date." 
    Nm "Like I said before, there might be something special between us."
    Nm shy "I guess we'll find out about that soon enough."
    c "Interesting. Did you finally come around to admitting that our get-togethers were actually dates from the beginning?"
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
    m "With those words she turned me around and hugged me tightly before I could protest."
    m "She had her arms around me and my head was lodged firmly under her chin like before."
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
    m "After that she tied my ankles with the narrow part of her tail."
    Nm "Very nicely... in fact."
    m "A terrified feeling washed over me as I realized that due to my position shifting again, my erect cock was now poking her belly."
    Nm "..."
    stop music fadeout 1.0
    Nm shy "Is that what I think it is?"
    c "I'm sorry!" 
    c "I can't control it. It gets erect on its own whenever I am sexually stimulated."
    Nm surprisedblush "Oh..."
    c "It doesn't weird you out?"
    m "Naomi paused to think for a moment."
    Nm smile "Why would a normal human bodily function weird me out?"
    Nm slsmile "After all it just means that...{w} you know..."
    play sound "fx/lewd/lickslowlouderlonger.ogg"
    m "She licked my forehead with her long tongue."
    play music "mx/treetops.mp3"
    Nm smile "That you actually want to have sex with me?"
    m "I felt like my heart had jumped to my throat. To make things worse, my face was feeling so hot, I bet it had turned completely red."
    m "(Why am I so anxious?)"
     
    if modinfo.has_mod("BangOk?") and bangok_four_bryce1_unplayed == False or bangok_four_xsebastian_unplayed == False or bangok_four_anna2.unplayed == False:
        m "(It shouldn't be that much different with Naomi.)"  
    else:
        m "(It shouldn't be that much different with a dragon.)"
         
    m "(I need to calm down.)"
    m "She interrupted my line of thought."
    Nm normal "Have you thought of what other humans would think if they found out that you wanted to have sex with a dragon?"
    m "After a moment of silence, I gulped loudly, and she surely heard it."
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
    play soundloop "fx/lewd/lickslowlouderlonger.ogg" fadein 1.0
    m "Suddenly Naomi started licking my entire face in circles with her long tongue, mostly focusing on my presumably red cheeks."
    m "(I don't think she is being genuine in trying to cool me down.)"
    m "(Not that I mind.)"
    $ renpy.pause (2.0)
    stop soundloop fadeout 2.0
    Nm smile "You're delicious."
    Nm shy "D-do you really want to go further with me?"
    m "I felt like I had no choice but to say yes or my heart was going to burst."
    c "Yes..."
    Nm normal "I saw earlier where your genitals are located. I don't think our anatomies are too different to make it inconvenient for us."
    
    #References to BangOk if you had sex with Anna, Bryce or Sebastian
    
    Nm slsmile "Let me try out more thing to get you properly in the mood."
    m "Naomi freed one of her arms a little bit and used her claw to nudge my head upwards."     
    m "Then she moved her mouth to mine, kissing me..."
    play sound "fx/lewd/altpenlouderlonger.ogg"
    m "...but also going through my lips with her long tongue."
    play soundloop "fx/lewd/pussylouder.ogg"     
    m "Then she started penetrating my mouth and tickling the inside of my upper jaw with the tip of her tongue."
    m "It was an intimate tickling sensation I'd never quite had before."
    m "The only thing I could do was to focus on breathing through my nose and to try to stay as still as possible."
    m "I felt like my chest was going to burst."
    m "(I'm going to die of a heart attack.)"
    stop soundloop fadeout 2.0
    Nm confused "You're completely powerless to do anything to resist my advances, aren't you?"
    Nm smile "Alright, we've already had enough foreplay."
    Nm "Is fucking me sideways in this position fine by you?"
    m "At first I was surprised she even asked for my opinion. I managed to mumble up a response."
    c "I would love to."
    Nm "Good little human."
    m "Naomi released me from the prison of her legs and spread them a bit."
    Nm shy "Can you see the slit between my legs?"
    m "I looked at"
    m "It seemed that I needed to go down a little bit to reach her pussy and also to have some leverage to thrust inside."
    c "Yes, but I can't penetrate you from this position. My testicles are in the way of bending my dick downwards properly."
    Nm normal "Oh."
    c "Could you loosen your grip on me so I can go down to get a better position?"
    Nm smile "Anything for you."
     
    #More lines to complete the "puzzle"
    play sound "fx/lewd/penslowlouder.ogg"
    m "As I penetrated her pussy, she locked me tightly in place with her powerful legs."
    play soundloop "fx/lewd/penslowlouder.ogg"
    m "After the surprise of the initial thrust I continued eagerly."
    Nm smile "You belong to me now. The only way is forward."
    Nm "I'll only let you go if you cum inside me."
    
    stop soundloop
    play soundloop "fx/lewd/penfastlouder.ogg"
    m "A release was rapidly building up inside me. The long tease had exhausted my stamina."
    c "Naomi... I'm going to cum."
    Nm surprisedblush "So soon? Fine, but don't even think about pulling out."
    Nm smile "I thought humans would last longer than this."
    c "It's your fault for teasing me so much. I've been hard for hours."
    Nm surprisedblush "That's what someone with no stamina would say."
     
    c "I'm going to paint your insides white with human cum!"
    Nm confused "Did you come up with that line all on your own? Pun intended, of course."
    Nm smile "Anyway, I doubt your output is enough to accomplish that." 
    Nm "You're welcome to try your best."
    c "I'll show you what humans can do!"
    
    stop soundloop fadeout 2.0 
    play sound "fx/lewd/cumlouder.ogg"
    queue sound "fx/lewd/penslowlouder.ogg"
    $ renpy.pause (1.0)
    m "I grunted loudly."
    c "Urgh!!!Ahh!!!{nw}" with vpunch
    play sound "fx/lewd/penslowlouder.ogg"
    queue sound "fx/lewd/cumlouder.ogg"
    show naomi slsmile with dissolve
    m "As I bucked against Naomi for the last time and released my final rope of cum, she let out a content sigh."
    Nm smile "Well done, tiny pink human."
    Nm "I can feel your sticky seed inside me. You must have been pent up."
    Nm shy "Unfortunately you didn't manage to get me off. If you can't go again you can always finish me off with your mouth."
    c "I still have another round in me. Just give me a few moments to recover."
    Nm stern "Try to last longer this time."
    c "I-I'm sorry. I promise I'll do better."
     
    c "That was the best sex I've ever had. I think the hours-long tease had something to do with that."
    Nm normal "It was certainly fun to play with someone who is too weak to resist anything I do to them."
    Nm smile "I'm looking forward to many more sessions like this."
    m "(I'm doomed.)"
    c "M-me too."
     
    c "I want to marry you and stay with you forever."
    Nm surprised "Is that how it works in your world?"
    Nm confused "We've only had sex once so far. That doesn't mean we should get married."
    Nm normal "Marriage is a long-term commitment."
    c "I'll prove myself worthy of you, just wait."
    
    stop music fadeout 2.0
    play sound "fx/rumble.ogg"
    $ renpy.pause (5.0)
    show naomi concern with dissolve
    m "(Looks like we forgot to eat.)"
    Nm normal "Oh, you're hungry?" 
    Nm "I've got some stuff we could cook together or we can order some food if you don't feel like doing that."
     
    #PC cooks a feast
     
    stop music fadeout 1.0
    hide naomi with dissolve
    scene black with dissolvemed
    $ renpy.pause (1.0)
    play music "mx/airborne.mp3"
    scene ecknaomiapt01 with dissolvemed
    show naomi normal with dissolve
     
jump sqb_naomi_apt_sexandeating_end
