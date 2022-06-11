label sqb_naomi_m6_discussion_reality:

#The basic idea I had for this scene was to make things contrary to how it is too often in video games. This time the PC has a problem that gets solved. It's basically the overarching idea of this mod.
#More specifically I don't like how in most games NPCs are basically encyclopedias for the player to use and therefore they have almost no input of their own.
#In this case the PC is having problems with duty and guilt and most importantly, doubts of his own existence. Somehow he figured out he might not be real.
#These topics were mentioned in the base game and some mods (I can't remember which from the top of my head), or at least I was thinking about them while playing. Doesn't matter.
#I did my best to try to figure out what the PC might be struggling with after accumulating these fragments of collective experience through different timelines from both mods and the base game.
#The conclusion the PC and Naomi come to together is what I would tell them in this specific situation. Keep in mind that unlike in real life, there's actually nothing the PC and Naomi can do.
#There's three possibilities (actually four but the last one is not relevant here). 
#1. The PC is in a Platonic simulation (like in the Matrix).
#2. The PC and everything in the game is just lines of code/artificial intelligence in a kind of meta sense. Obviously it's this to us, but what about the relation between our worlds?
#4. Everything is as it seems. In other words the PC is insane.
#It is up to you to decide which one you think is most likely. I leave things ambiguous and radically uncertain on purpose. I haven't decided on an answer myself.
    stop music fadeout 1.0
    
    scene black with dissolvemed
    
    play sound "fx/system3.wav"
    s "Now when that's out of the way, would you like to preview a scene from chapter 6?"
    menu:
        "Yes":
            s "Alright."
            pass
        
        "No":
            s "Alright."
            $ renpy.pause (1.0)
            scene ecknaomiapt03 with dissolvemed
            play music "mx/airborne.mp3"
            show naomi smile with dissolve
            jump sqb_naomi_m6_discussion_reality_end
            
#Part 1, PC comes home from work
    
    $ renpy.pause (2.0)
    
    scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed
    
    play music "mx/sail.ogg"
    play sound "fx/door/handle.wav"
    $ renpy.pause (2.0)
    play sound "fx/door/doorclose3.wav"
    $ renpy.pause (1.0)
    
    m "(Another great day at work. Regardless of that, I hope I can soon start doing something other than just cataloging information from the PDAs.)"
    m "I had asked Naomi to come over after her shift to try out some of the new dishes I had come up with during my time here."
    m "(Time to take a shower.)"
    play sound "fx/door/door_open.wav"
    scene bath with dissolve
    $ renpy.pause (2.0)
    play sound "fx/undress.ogg"
    $ renpy.pause (2.0)
    play sound "fx/shower.ogg"
    m "(Ahhh.)"
    stop sound
    m "(That was refreshing.)"
    scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed
    m "I went back to the living room to relax after the shower."
    play sound "fx/book.ogg"
    m "I picked up a book from the bookshelf and started reading."
    play sound "fx/pages.ogg"
    m "(I really need to stop procrastinating and go buy a television. I like reading but I need more variety in my life.)"
    scene o2 at Pan((0, 250), (0, 250), 0.1) with dissolvemed
    m "I read for a while until I realized I would have to start cooking soon."
    m "(Look at the time. I need to start cooking already.)"
    scene eckkitchenx at Pan((0, 250), (0, 250), 0.1) with dissolvemed
    stop music fadeout 1.0
    m "(Now, what should I start off with first?)"
    play music "mx/mysteryambience.ogg"    
    m "But as I was about to start to cook, the already familiar feeling of dread suddenly came back."
    m "(I feel like shit.)"
    scene o2 at Pan((0, 250), (0, 250), 0.1) with dissolvemed
    m "I went back to the living room and sat on the couch."
    m "I adjusted my position on the couch to help me calm down and to reflect on the feeling of impending doom."
    m "(Why is this happening to me?)"
    m "(There are so many things about my actions that make no sense.)" 
    m "(Did I do the right things after all?)" 
    m "(How do I figure out what's real?)"
    m "..."
    stop music fadeout 1.0
    play sound "fx/steps/rough_gravel.ogg"
    m "After some time my thoughts were interrupted by the sound of Naomi walking outside my apartment. She entered with the key I had given her."
    
    play sound "fx/door/handle.wav"
    $ renpy.pause (2.0)
    play sound "fx/door/doorclose3.wav"
    $ renpy.pause (1.0)
    
    show naomi flip normal at left with easeinleft
    Nm normal flip "What a day at work. It suffices to say that the case would have been left unsolved for some time without me."
    c "Hey, Naomi."
    Nm "Hey, [player_name]. Is the food ready?"
    show naomi surprised flip at left with dissolve
    m "She noticed me resting on the couch, with my arms spread out and my head hanging limply over the backrest."
    Nm "Are you okay? You look worried."
    m "I stretched my arms upwards, then leaned forward, followed by placing my elbows on my knees and finally resting my head in my hands."
    c "I've just been deep in thought. Because of that I forgot to cook like I had promised."
    Nm concern flip "That sounds serious. Are you feeling down because of the thing we talked about earlier?"
    m "I straightened my back, placed my arms on both sides of the backrest, sighed and looked at Naomi."
    play music "mx/darkrock.ogg"
    c "You could say that."
    c "Going through this ordeal who knows how many times has really taken its toll on me. I can only remember glimpses of previous timelines but clearly even that's too much for me to handle."
    c "I second guess everything I do and sometimes I get this feeling of dread deep in my stomach that won't go away no matter what I do."
    show naomi surprised flip at left with dissolve
    c "The weird thing is that I have never been this happy in my entire life. Even pre-flare earth wasn't as good as this place." 
    c "What I'm going through is something entirely different than just simply feeling down."
    c "You could say that the problem for me right now is that because of after everything that's happened, I sometimes feel like I don't even know what's real anymore."
    c "Remembering things that my alternate selves have done and acting on urges caused by those memories without even thinking it through has left me to question which of my actions are my own."
    c "Are any them though?"
    c "Obviously things turned out great in this timeline regardless of my agency. Is everything what happens to me predetermined? How would I even go about figuring that out?"
    Nm confused flip "Those are some difficult things to think about."
    stop music fadeout 1.0
    Nm smile flip "I'm here for you if need help figuring out what's real."
    c "You have no idea how much you saying that helps me right now."
    Nm "Do you want to see what would help even more?"
    hide naomi with dissolve
    m "With those words, Naomi walked up to my couch and climbed on it. She rested her belly on it and lifted her tail over the armrest on the opposite side. When she had finished positioning herself, her face was next to mine."
    show naomi normal flip at center with dissolve
    play sound "fx/sheet.wav"
    m "Lastly, she shifted herself closer to me and planted her hands on my right thigh."
    show naomi smile flip with dissolve
    m "That was my signal. I placed my arms around her upper body and hugged her. She leaned towards me."
    show naomi slsmile flip with dissolve
    play music "mx/serene.ogg"
    c "Thank you for always being there to cheer me up whenever I have a hard time."
    Nm smile flip "You're too cute to be left in a sad mood."
    m "I released my hug and shifted back to my previous position, still looking at her."
    Nm normal flip "Would you like to talk more about your problem now that you've calmed down?"
    Nm "You know you can talk to me about anything."
    c "Thank you. Maybe if I get all of this baggage off my back I can start to forget."
    
#Part 2, trying to move on
    c "Firstly, what do you think about the outcome of this timeline?"
    c "Even though we saved this world, somehow I still feel like I failed. I wonder if there was something more we could have done."
    c "Maybe I'm just not good enough?"
    Nm blank flip "We did what we could, given the circumstances."
    c "I keep telling myself that very thing, but sometimes I just can't help but recalculate everything I've done."
    #more, explanation
    Nm concern flip "I don't think you should be dwelling in the past this much."
    Nm normal flip "What's done is done. We should focus on the future."
    c "You're right. Maybe we should be happy we're alive in the first place."
    Nm "Exactly."
    c "But even if I tried my best, do I deserve all this?"

#Part 3, the guilt
    
    c "A life like this is something I could have only dreamed of a few weeks ago. Living in the city-state I came from was awful, but it was the safest place to live in the post-flare world that I knew of."
    c "Like I've already told you multiple times, living here has been great for me. I'm looking forward to spending the rest of my life here with you."
    Nm smile flip "You know I feel the same way."
    c "Still, what makes me the saddest about this whole situation, is that I'm not able to share this wonderful experience with the rest of my people."
    Nm sad flip "You and me both."
    c "I know we humans have our faults, but I'm sure most of us would have loved to meet you dragons." 
    c "We aren't all like Reza."
    Nm stern flip "I would like to think that all humans are as nice as you are. It's hard to believe you used to be friends with someone like Reza." 
    Nm annoyed flip "He's is such a horrible person. How could he personally murder all those dragons and then intend to abandon us all to die?"
    Nm blank flip "I'm still glad we stopped Maverick from killing him. He doesn't deserve to die no matter how evil he is." 
    Nm "I hope we can rehabilitate him so that he'll change for the better."
    c "Agreed. Anyway, to continue my line of thought, I had initially placed great hopes in our inter-species cooperation. Your immigration idea was a stroke of genius."
    show naomi surprisedblush flip with dissolve
    c "It's unfortunate that some from our leadership didn't see it the same way. Reza confirmed that he wasn't acting alone."
    c "I wouldn't be stuck here if it hadn't been for the plot that Reza was a part of. I would have still preferred to stay here of course, but I wish the connection between our worlds hadn't been severed."
    show naomi confused flip with dissolve
    c "I think Izumi's reasons for severing the connection were understandable, even though the repercussions were terrible." #Or were they?
    c "If everything had gone well, over time we could have even relocated the majority of my people here, like you said before." 
    c "We could have left a heavily armed force to guard the portal to enable us to gradually let in any humans who managed get to there." 
    c "In the end, I just want to help as many people as possible."
    c "Some time after that, we could have started to really rebuild."
    Nm concern flip "You're always trying to save everyone. You have such a big heart, [player_name]. "
    Nm "I like that about you, but ultimately you should focus more on taking care of yourself." 
    Nm sad flip "Seeing you like this breaks my heart."
    c "You are right, but like I said, sometimes I can't stop thinking about what could have been. I know it's all in the past and that there's nothing we can do to change it."
    c "I still can't shake the feeling of guilt caused by my failure, even though in the end it wasn't my fault." 
    c "What bothers me, is that I get to have a wonderful life, while my city-state and the people I knew slowly wither away from existence."
    m "Naomi sighed loudly."
    Nm stern flip "Don't feel bad about it. You should remember that the task you were given was nigh-impossible due to circumstances outside of your control."
    Nm normal flip "We did the best we could."  
    c "I guess I should accept that. Is it time to finally let go?"
    c "Let's just focus on us from now on."
    show naomi smile flip with dissolve
    c "Anyway, one more thing and I'm done unpacking all my problems onto you."
    Nm confused flip "Go on."    
    c "So, before I learned that the multiverse theory was real and realized its implications, I used to think that I had the tools to figure out what's real."
    c "In other words trying to figure out what's actually real is right now a futile effort." 
    c "Now I can't help but think that all of what we experience might be a simulation. This realization is the most unsettling of them all."
    c "I've noticed that there is so much about my behavior that doesn't any make sense at all."
    show naomi concern flip with dissolve
    c "From a scientific standpoint, remembering things from alternate realities is highly implausible."
    
    #if lorem2played == True:
         #c "One of Anna's co-workers did tell me some things about this but honestly it all sounds just like what a simulation would come up with."
         
    #else:
        #pass
    
    c "In addition to this, I feel like my life is on rails; there are things I can't force myself to do, no matter how hard I try."
    c "For example, whenever we go out, why can we only go to the places where Adine or Zhong work at?"
    Nm surprised flip "...what?"
    c "Naomi, I know I sound crazy, but I have no idea how to break from these figurative chains."
    c "I understand how reification works and we should fight against it whenever we can, but honestly for the first time in my life I'm in a situation in which there is absolutely nothing I can do to resist the powers that control my life."
    c "In the end the most shocking realization is that I can't be entirely sure if even my life before arriving through the portal is real."
    show naomi concern flip with dissolve    
    c "Anyway, if we're in the type of simulation I think we might be in, we won't ever be able to break out of it." 
    c "Even trying would probably have us lose our sanity."
    show naomi confused flip with dissolve
    m "Naomi was getting visibly bored with my antics."    
    c "Uhh... in the end it doesn't seem like I'm getting anywhere with this line of thought."
    c "Because of this I guess I have to come to the conclusion that I should stop theorizing before I lose my mind." 
    c "Let's just focus on what we experience, especially on experiences that make both of us happy."
    Nm normal flip "That I can agree with." 
    c "I'm just very tired. Maybe it's finally the time to stop." 
    c "After all this hardship I just want to live in peace and forget all the negative things that happened in the past."
    c "I'm finished. That was quite a lot to unpack."
    Nm confused flip "You've were philosophical as usual." 
    Nm blank flip "I didn't fully understand everything you said but I got the general idea."
    Nm normal flip "I'm happy you managed to come to a satisfactory conclusion even though I don't share these feelings of uncertainty you have. Both of us being happy is all that matters from now on." 
    Nm shy flip "I can think of an experience that would do just that, especially after a long day at work."
    c "I'm up for it. We should eat first because I'm starving." 
    c "Since I didn't feel like cooking, how about we have food delivered to us instead?"
    Nm normal flip "That works for me. Don't feel sad about not being able to cook. We all have our bad days."

#Part 4, the eating

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
    m "(This is perfect. With this much, we won't have to cook tomorrow.)"
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
    c "I still feel a bit down. Could I please get a dragon hug before I go?"
    stop music fadeout 1.0
    Nm smile "Of course."
    m "I got off the couch and walked up to her. As I placed my arms around her neck and she shifted herself closer to hug me back."
    m "She held me tightly and placed her wings around me. Lastly, she wrapped her tail loosely around my ankles."
    play music "mx/enigma.mp3"
    Nm slsmile "Looks like I caught my favorite human again. I might eat you because the dinner wasn't ready when I came over."
    Nm smile "I think I'll eat you in a different way. I like having you around for cuddling."
    Nm "What if I pushed you to the floor and we had sex right now?" #Rethink?
    c "Naomi... that will have to be later because we haven't eaten yet. I need the energy and hydration to perform."
    c "You seem to be eager so you can be on top later if you just wait a bit longer."
    Nm surprisedblush "Aww... what a buzzkill. I guess I'll wait if you insist."
    m "A funny thought came into my mind."
    c "Hey, if you consider all the different timelines, we've probably waited quite a while get to this point in the first place."
    c "In addition to that, if we're in a simulation, every time we have sex someone or something had to program it. Really makes you think, huh?"
    stop music fadeout 1.0
    Nm stern "Is that supposed to be an attempt at a joke?"
    Nm "Your new jokes aren't funny at all. Why can't you just revert to your old jokes, like saying you've always wanted to lay the dragon?"
    m "I had no idea how to respond. I knew I had just said something I shouldn't have."
    c "Can we just calm down and wait for the food?"
    Nm "Only if you stop implying in a roundabout way that I'm not real." 
    Nm annoyed "Don't you understand how that makes me feel!?"
    c "I'm sorry! I didn't mean to upset you."
    c "I promise I will never joke about that ever again."
    Nm concern "I'm relieved. Remember, listening to me is for your own good."
    c "Yes... Naomi. I'll listen to you even more from now on."
    show naomi smile with dissolve
    play music "mx/treetops.mp3"
    m "With those words, she finally tied my ankles with the narrow part of her tail. I was already familiar with this position, so I I wasn't feeling uncomfortable in the slightest."
    Nm slsmile "Remember, you're mine now. Obeying me will do you some good because I only have your well-being in mind."
    m "She finished staking another claim on me by licking the left side of my face."
    play soundloop "fx/lewd/lickslow.ogg" fadein 1.0
    m "She gently licked up and down with her long tongue, always stopping at the bottom of my eyelid, just mere millimeters short of my eyeball."
    m "I was aroused but also terrified as the result of being dragonhandled like this. The licking went on until I interjected about the drinking glasses."
    c "Umm..."
    stop soundloop fadeout 2.0
    Nm smile "Feeling comfortable?"
    c "Sure... but can I go get the glasses now? I'm thirsty and I bet you are as well."
    Nm surprisedblush "Are you again looking for an excuse to escape? I'm not finished with you yet."
    c "I'll be back, I promise."
    
    #The PC and Naomi eating
    
    scene black with dissolvemed
    
    $ renpy.pause (2.0)
    
    scene ecknaomiapt01 with dissolvemed
    play music "mx/airborne.mp3"
    show naomi smile with dissolve

jump sqb_naomi_m6_discussion_reality_end    
    
    