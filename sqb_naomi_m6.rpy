label sqb_naomi_m6_discussion_reality:
    
    $ renpy.pause (2.0)
    scene black with dissolvemed
    $ renpy.pause (8.0)
    show naomi smile with dissolve
    Nm "I bet you expected it to be over, huh?"
    $ renpy.pause (2.0)
    Nm normal "Would you like to preview an unfinished scene from the upcoming chapter 6?"
    menu:
        "Yes, please.":
            Nm smile "I hope you enjoy it!"
            $ renpy.pause (1.0)
            hide naomi with dissolve
        
        "No, take me back to the main menu.":
            Nm blank "Alright."
            Nm smile "I hope you come back soon!"
            $ renpy.pause (1.0)
            hide naomi with dissolve
            $ renpy.pause (2.0)
            return
    
    $ save_name = _("Chapter 6 - Naomi")
    $ _game_menu_screen = "navigation"
    $ renpy.pause (2.0)    
    scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed
    $ renpy.pause (1.0)
    play music "mx/sail.ogg"
    play sound "fx/door/handle.wav"
    $ renpy.pause (2.0)
    play sound "fx/door/doorclose3.wav"
    $ renpy.pause (1.0)    
    m "(Yay, another great day at work. Still, I hope I can soon start doing something other than just cataloging information from the PDAs, because it's already getting monotonous.)"
    m "(Naomi's coming over this evening to try out some of the new dishes I had come up with. So first, it's time to take a shower.)"
    play sound "fx/door/door_open.wav"
    scene bath with dissolve
    $ renpy.pause (2.0)
    play sound "fx/undress.ogg"
    $ renpy.pause (2.0)
    play sound "fx/shower.ogg"
    m "(Ahhh.)"
    stop sound
    m "(That was refreshing.)"
    play sound "fx/door/door_open.wav"
    scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed
    play sound "fx/book.ogg"
    m "I wanted to relax after the shower so I went back to the living room and picked up a book from the bookshelf and started reading."
    play sound "fx/pages.ogg"
    m "(I really need to stop procrastinating and buy a television. I like reading but I need some more variety in entertainment.)"
    $ renpy.pause (2.0)
    scene o2 at Pan((0, 250), (0, 250), 0.1) with dissolvemed
    m "I read for a while until I realized I would have to start cooking soon."
    $ renpy.pause (1.0)
    scene eckkitchenx at Pan((0, 250), (0, 250), 0.1) with dissolvemed
    stop music fadeout 1.0
    m "(Now, what should I start off with first?)"
    play music "mx/mysteryambience.ogg"    
    m "But as I was about to start to cook, the already familiar feeling of dread suddenly came back."
    m "(I feel like shit.)"
    scene o2 at Pan((0, 250), (0, 250), 0.1) with dissolvemed
    m "I went back to the living room and sat on the couch. Then I adjusted my position on it to help me calm down and to reflect on the feeling of impending doom."
    m "(Why is this happening to me? I just want to be happy.)"
    m "(There are so many things about my actions that make no sense. Did I do the right things after all?)"
    $ renpy.pause (4.0)
    stop music fadeout 1.0
    m "After some time my thoughts were interrupted by the sound of Naomi fiddling with my outer door's handle. She entered with her own key, in high spirits."   
    play sound "fx/door/handle.wav"
    $ renpy.pause (2.0)
    play sound "fx/door/doorclose3.wav"
    $ renpy.pause (1.0)   
    show naomi flip normal at left with easeinleft
    Nm normal flip "What a day at work. It suffices to say that the case would've been left unsolved for some time without my important contributions."
    c "Hey, Naomi."
    Nm "Hey, [player_name]. Is the food ready?"
    show naomi surprised flip at left with dissolve
    m "She noticed me resting on the couch, with my arms spread out and my head hanging limply over the backrest."
    Nm "Are you okay? You look worried."
    m "I stretched my arms upwards, then leaned forward, followed by placing my elbows on my knees and finally resting my head in my hands."
    c "I have been deep in thought. Because of that I forgot to cook like I had promised."
    Nm concern flip "That sounds serious. Are you feeling down because of the thing we talked about earlier?"
    m "I straightened my back, placed my arms on both sides of the backrest, sighed and looked at Naomi."
    play music "mx/darkrock.ogg"
    c "Unfortunately."
    c "My alternate selves going through this multiverse ordeal who knows how many times has taken its toll on me. I'm certain that my thoughts and feelings being affected by alternate timelines is real." 
    c "For example, I can sometimes see glimpses of previous timelines in my dreams. The worst parts are how I second guess everything I do and how I sometimes get a sudden feeling of dread deep in my stomach that won't go away for a while. Sadly, these effects on me are clearly too much to handle."
    show naomi surprised flip at left with dissolve
    c "The weird thing about all this is that somewhat objectively, I have never been this happy in my entire life. Even most of pre-flare earth wasn't as good as this place. On top of all this, I have you, so I should be doing great but for some reason I'm not." 
    c "What I'm going through is something entirely different than just simply feeling down. You could say that a big part of the problem for me right now is that because of after everything that's happened, I sometimes feel like I don't even know what's real anymore."
    c "Remembering things that my alternate selves have done and acting on urges caused by those memories without even thinking it through has left me to question which of my actions are my own."
    c "Are any them though?"
    c "Obviously things turned out great in this timeline regardless of my agency. Is everything what happens to me predetermined? How would I even go about figuring that out?"
    Nm confused flip "Those are some difficult things to think about."
    stop music fadeout 1.0
    Nm smile flip "I'm here for you if need help figuring out what's real."
    c "Thank you, Naomi. You saying that helps me a lot right now."
    Nm "Do you know what would help even more?"
    hide naomi with dissolve
    play sound "fx/bed.ogg"
    m "Naomi climbed on the couch next to me, resting her belly on it. To be able to fit, she lifted her tail and legs over the armrest on the opposite side. After that, she leaned herself closer to me and planted her elbows on my right thigh."
    show naomi smile flip with dissolve
    play sound "fx/sheet.wav"
    m "Finally, when she had fully finished positioning herself, her snout was in front of my face. I placed my arms around her upper body and hugged her, which she reciprocated"
    show naomi slsmile flip with dissolve
    play music "mx/serene.ogg"
    c "Thank you for always being there to cheer me up whenever I have a hard time."
    Nm smile flip "You're too cute to be left in a sad mood."
    m "I released the hug and changed back to my previous sitting position"
    Nm normal flip "Would you like to talk more about your problem now that you have calmed down? You know you can talk to me about anything."
    c "I would like to do that very much. Maybe if I get all of this baggage off my back I can start to forget. Where to start..."
    $ renpy.pause (2.0) 
    c "Firstly, what do you think about the outcome of this timeline?"
    Nm blank flip "It seems pretty good to me. What's wrong with it?"
    c "Well, even though we saved this world, I still have the feeling of failure lingering in me. I just wonder if there was something more we could have done. Maybe I didn't try hard enough?"
    Nm confused flip "We did what we could, given the bad circumstances. You've done more than what could be reasonably expected."
    c "I keep telling myself that very thing, but sometimes I just can't help but recalculate everything I have done."
    Nm normal flip "I really like your conscientiousness and good nature. You're always trying to achieve the perfect solution."
    Nm blank flip "But if I am being completely honest, I'll have to tell you that I don't think you should be dwelling in the past this much."
    Nm concern flip "We can't change what's already happened, not anymore at least. Let's just focus on the future."
    c "You're right. Maybe we should be happy we're alive in the first place."
    Nm normal flip "Exactly."
    c "Still, even if I tried my best, do I deserve all this?"
    Nm "Of course, we saved the world."
    c "I suppose so, but a life like this is something I could have only dreamed of a few weeks ago. Living in the city-state I came from was awful, even though it was the safest place to live in the post-flare world that I knew of."
    c "Well, what I am trying to say is that I'm sad because I'm not able to share this wonderful experience with the rest of my people."
    Nm sad flip "You and me both. I know that a lot of dragons would have been really excited to meet more humans."
    c "I know we humans have our faults, but I'm confident that most of us would've loved to meet you dragons. We aren't all like Reza or our leadership."
    Nm stern flip "It's still hard for me to believe that you used to be friends with someone like Reza. How could he personally murder all those dragons and then intend to abandon us all to die?"
    Nm "On top of all this, he even tried to hurt me with his long-range weapon."
    c "Yeah, I remember."
    Nm blank flip "I'm still glad I stopped Maverick from killing him, since he doesn't deserve to die no matter how evil he is. I hope we can rehabilitate him so that he'll change for the better."
    c "Agreed. Anyway, to continue my line of thought, I had initially placed great hopes in our interspecies cooperation. Your immigration idea was a stroke of genius."
    show naomi smile flip with dissolve
    c "It's unfortunate that some from our leadership didn't see it that way. Honestly, now when I have thought about it more, Reza was probably lying about coming up with his plan all by himself. Someone as narcissistic as him will make up all sorts of lies in order to inflate their ego."
    c "Also, the fact that I wouldn't be stuck here if it hadn't been for the plot that Reza was a part of still upsets me a little bit. I just wish the connection between our worlds hadn't been severed."
    show naomi blank flip with dissolve
    c "I think Izumi's reasons for severing the connection were understandable, even though the repercussions were terrible."
    c "If everything had gone well, over time we could have even relocated the majority of my people here, like you said before. We could have left a heavily armed force to guard the portal to enable us to gradually let in any humans who managed get to there. In the end, I just want to help as many people as possible."
    c "And some time after that, we could have started to really rebuild."
    Nm concern flip "Again, you're trying to save everyone. You have such a big heart, [player_name]. "
    Nm "Still, you should focus more on taking care of yourself." 
    Nm sad flip "Seeing you sad like this upsets me a little bit."
    c "You're right, but like I said, sometimes I can't stop thinking about what could have been. I know it's all in the past and that there's nothing we can do to change it. I still can't shake the feeling of guilt caused by my failure, even though in the end it really wasn't my fault, like you pointed it."
    show naomi blank flip with dissolve
    c "What bothers me, is that I get to have a wonderful life, while my city-state and the people I knew slowly wither away from existence."
    show naomi concern flip with dissolve
    m "Naomi sighed loudly."
    Nm stern flip "Stop feeling bad about it already. Do I need to remind you that the task you were given was nigh-impossible due to circumstances outside of your control?"
    Nm normal flip "We did the best we could."  
    c "I guess I should finally accept that. Is it really the time to finally let go?"
    $ renpy.pause (2.0)
    c "Alright, let's just focus on us from now on."
    show naomi smile flip with dissolve
    c "Anyway, one more thing and I'm done unpacking all my problems onto you. I hope you don't mind, since I need to get this off my chest."
    Nm confused flip "Go on."    
    c "So, before I learned that the multiverse theory was real and realized its implications, I used to think that I had the tools to figure out what's real." 
    c "What I mean to say is that trying to figure out what's actually real is right now a futile effort. Now I can't help but think that all of what we experience might be a simulation. This realization is the most unsettling of them all that I have had."
    c "Firstly, I have noticed that there is so much about my behavior that doesn't any make sense at all." 
    c "Secondly, I think that from a scientific standpoint, remembering things from alternate realities is highly implausible. Also, I feel like my life is on rails; there are things I can't force myself to do, no matter how hard I try."
    c "A good example would be that whenever we go out, we only seem to be able to go to the places where Adine or Zhong work at."
    Nm surprised flip "Uhh... what?"
    c "Naomi, I know I sound crazy, but I have no idea how to break from these chains."
    c "I understand how reification works and we should fight against it whenever we can, but honestly for the first time in my life I'm in a situation in which there is absolutely nothing I can do to resist whatever it is that controls my life."
    c "The most shocking realization is that I can't even be entirely sure if my life before arriving through the portal is real."
    show naomi concern flip with dissolve    
    c "Anyway, if we're in the type of simulation I think we might be in, we won't ever be able to break out of it. Even trying would probably have us lose our sanity."
    show naomi confused flip with dissolve
    m "Naomi was getting visibly bored with my antics."    
    c "I suppose in the end it doesn't seem like I'm getting anywhere with this line of thought. Because of this I guess I have to come to the conclusion that I should stop theorizing before I lose my mind." 
    c "Let's just focus on what we experience, especially on experiences that make both of us happy."
    Nm normal flip "That I can agree with." 
    c "I'm just very tired of all this, so maybe I should take your advice and finally stop. After all this hardship I just want to live in peace and forget all the negative things that happened in the past."
    $ renpy.pause (2.0)
    c "I'm finished. That was quite a lot to unpack."
    Nm confused flip "You were philosophical as usual." 
    Nm blank flip "I didn't fully understand everything you said but I got the general idea."
    Nm normal flip "I have to say I am relieved you managed to come to a satisfactory conclusion even though I don't at all share these feelings of uncertainty you have. Just remember that both of us being happy is all that mattered ever since we stopped Reza and the comet." 
    Nm shy flip "I can think of an experience that would do just that, especially after a long day at work."
    c "I'm up for it, but we should eat first because I'm starving. Since I didn't feel like cooking, how about we have food delivered to us instead?"
    Nm normal flip "That works for me. Don't feel sad about not being able to cook. We all have our bad days."
    Nm "I'll get us something to drink while you order the food. I trust your food ordering abilities."
    c "Thanks."
    hide naomi with easeoutright
    play sound "fx/door/door_open.wav"
    queue sound "fx/door/doorclose.ogg"
    m "As as I was starting to pick up the phone, Naomi got up from the couch and went to the kitchen."
    play sound "fx/phonepickup.ogg"
    m "As I picked up the phone, I realized something."
    m "(For some reason I can only ever order food from the café where Adine works at or Pantoli's.)"
    m "(Oh well, I promised Naomi I would stop thinking about this.)"
    m "(Hmm... I don't feel like eating greasy pizza tonight.)"
    m "I selected the café where Adine worked at from the speed dial."
    m "(I'm going to need a lot of comfort food. Nobody can tell me all the food I manage to eat tonight isn't real.)"
    m "I ordered some fried cheese, two boxes of fried chicken, several hamburgers and two dragon-sized portions of fried noodles with aurochs meat and steamed vegetables."
    m "(Perfect. With this much, we won't have to cook tomorrow.)"
    play sound "fx/sheet.wav"
    m "After I had placed the order, I lied down on the couch."
    m "(I guess right now it's better to just keep my eyes ahead and do my best to avoid going crazy.)"
    $ renpy.pause (1.0)
    m "(I wonder if Naomi actually went to just raid my fridge?)"
    $ renpy.pause (2.0)
    m "(I can't wait to eat.)"
    m "After a couple more minutes Naomi returned, moving carefully while carrying a pitcher full of juice in her free hand."
    play sound "fx/glassdown.wav"
    show naomi blank at center with easeinright
    m "As she placed the pitcher on the table I got off the couch."
    c "Thank you. I'll go get the glasses."
    Nm "Sure."
    $ renpy.pause (2.0)
    c "By the way, I still feel a bit down. Could I please get a dragon hug before I go?"
    stop music fadeout 1.0
    Nm smile "Of course."
    m "I got off the couch and walked up to her and placed my arms around her upper body. She leaned herself closer to hold me tightly and covered me with her wings. Lastly, she wrapped her tail loosely around my ankles."
    play music "mx/enigma.mp3"
    Nm slsmile "Looks like I caught my favorite human again."
    Nm smile "What if I pushed you to the floor and we had sex right now?"
    c "Naomi, please remember that the floor isn't a good place for me to have sex with someone as large as you on top. Also, we should eat first, since I need the energy and hydration to perform."
    c "You seem to be eager so you can be on top all night if you want to. Please, just wait a bit longer."
    Nm blank "You're such a letdown. I guess I'll wait if you insist."
    m "To get back at Naomi, I replied with the funny thought that had just come into my mind."
    c "Hey, if you consider all the different timelines, we've probably waited quite a while get to this point in the first place."
    c "Even more interesting is the fact that if we're in a simulation, every time we have sex someone or something had to program it beforehand. Really makes you think, huh?"
    $ renpy.pause (2.0)
    stop music fadeout 1.0
    Nm stern "Is that supposed to be an attempt at a joke? Why can't you just tell some of your old jokes that are actually funny?"
    m "I had no idea how to respond. I knew I had just said something I shouldn't have."
    c "Can we just calm down and wait for the food?"
    Nm "Only if you stop implying in a roundabout way that I'm not real." 
    Nm annoyed "Don't you understand how that makes me feel!?"
    c "I'm sorry! I didn't mean to upset you. I promise I will never joke about that ever again."
    Nm concern "I'm relieved. Remember, listening to me is for your own good."
    c "Yes... Naomi. I'll listen to you even more from now on."
    show naomi smile with dissolve
    play music "mx/treetops.mp3"
    m "After my submission to her, she finally tied my ankles with the narrow part of her tail."
    Nm slsmile "Remember, you're mine now. Obeying me will do you some good because I only have your well-being in mind."
    m "Naomi staked another of her claims on me by starting to lick the left side of my face."
    play soundloop "fx/lewd/lickslow.ogg" fadein 1.0
    m "She gently licked up and down with her long tongue, always stopping at my eyelid, just mere millimeters short of my eyeball."
    m "I was aroused but also terrified as the result of being dragon-handled like this. The licking went on until I interjected about the drinking glasses."
    c "Umm..."
    stop soundloop fadeout 2.0
    Nm smile "Feeling comfortable?"
    c "Sure... but can I go get the glasses now? I'm thirsty and I bet you are as well."
    Nm blank "You're always looking for an excuse to escape. I'm not finished with you yet."
    c "I'll be back, I promise."
    
    #PC and Naomi eating, sex later
    
    $ renpy.pause (2.0)
    stop music fadeout 1.0
    scene black with dissolvemed
    $ renpy.pause (2.0)   
    play sound "fx/system3.wav"
    s "Thank you for playing!"
    $ renpy.pause (2.0)

jump ml_main_menu    
    
    