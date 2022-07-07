label sqb_naomi_cafe_discussion:

    menu:
        "Juice":
            $ renpy.pause (0.5)
            $ naomi1drink = "juice"
            c "Some juice would be good."
            
        "Soda":
            $ renpy.pause (0.5)
            $ naomi1drink = "soda"
            c "Could you get me a soda?"
            
        "Beer":
            $ renpy.pause (0.5)
            $ naomi1drink = "beer"
            c "Could you get me a local beer?"
            
        "Coffee":
            $ renpy.pause (0.5)
            $ naomi1drink = "coffee"
            c "I would love some coffee right now."
            
        "Cocktail":
            $ renpy.pause (0.5)
            $ naomi1drink = "cocktail"
            c "For drink, could I have a cocktail?"
            Ad "Sure, what kind?"
            c "Since I'm new here, just get me the one that you think is the most popular."
            
    Ad "Alright. I'll be right back."        
    show adine normal b with dissolve
    hide adine with easeoutleft
    hide naomi with dissolve
    show naomi normal with dissolve           

    if naomi1drink == "beer" or naomi1drink == "cocktail":       
         Nm blank "Are you sure it's a good time to drink?"
         c "What's the problem?"
         c "It's evening and we're eating out together. Having a drink or two can be relaxing, if you're in good company."
         $ naomi1mood += 2
         Nm surprisedblush "Oh, thank you."
         c "Are you wary of drinking because of Bryce? Not everyone is like him."
         Nm concern "You know about his drinking problem?"
         
         if bryce1played == True:
             c "Yeah, I went drinking with him in order to get to know him a little bit better. I ended up finding out that it's his favorite pastime."
             Nm stern "Drinking is almost all he does on his free time. I think he should get other hobbies."         
         else:
             c "Unfortunately, I do."
             m "(Hold on, how do I know about it? Did someone tell me?)"
             Nm sad "Oh well. It normally takes longer for people to find out." 
             Nm "I worry about him. I think he should get hobbies other than drinking."
             
         c "I agree with that. It's obvious to me that he drinks way too much."
         c "Anyway, we shouldn't talk ill of someone who's not present."
         Nm blank "I suppose you're right."
         c "To change the subject, could you tell me more specifically what sort of work you do at the police station?"
         Nm normal "Sure."  
    else: 
        pass

jump sqb_naomi_cafe_discussion_end

label sqb_naomi_cafe_eating:

    c "Wow, you finished your portion pretty quickly. Was the food really that tasty, or did you eat it quickly just because you're just a very hungry dragoness?"
    Nm shy "Umm..."
    Nm smile "Both, I guess. It was delicious like it is always, but like I said, I was starving because I didn't have a lunch break today."
    Nm concern "Quite often my work is simply too important to set aside some time for one."
    m "Since this was the second time she explicitly mentioned being overworked, I felt like I should finally push further on the issue."
    c "Naomi, that's not good at all, especially if it happens regularly. Taking a lunch break makes you more efficient for the rest of the day. You can't do cognitively demanding work as effectively if you're hungry." 
    c "For this reason in most workplaces where I come from, lunch breaks used to be mandatory."
    Nm confused "That's an interesting point, I'll keep it in mind."
    c "Also, starving yourself can make you eat too much when you finally have the time, which might lead to gaining weight." 
    c "Not that I think it would happen to you, as you're a big and athletic dragoness who I'm sure needs lots and lots of food to keep herself fed in the first place."
    Nm shy "I'm not sure how to respond to that. Thank you, I guess?"
    Nm surprisedblush "I suppose it's obvious looking at my physique that I work out a lot."   
    m "(Why did I even say that? I'm lucky she didn't take offense.)"
    show naomi normal with dissolve
    $ renpy.pause (2.0) 
    m "(I just realized something. She might still be hungry because her portion was about the same size as mine.)"
    m "(Since she needs to eat more than I do, should I ask her if she wants to order again?)"
    
    menu:
        "Order some more food.":
            $ renpy.pause (0.5)
            $ naomi1mood += 1
            $ naomilewd +=1
            c "If you want to eat some more, we could place another order. I'm full enough, so I'll just have another drink."
        
        "Don't.":        
            $ renpy.pause (0.5)
            m "(I'm already feeling tired. I just want to go back to my apartment before it gets late.)"
            c "So, you really do miss your lunch breaks often?"
            jump sqb_naomi_cafe_eating_end
    
    Nm confused "Are you sure you're fine watching me eat?"
    c "Of course. I don't mind staying with you a while longer, because then we could talk some more."
    Nm normal "In that case... {w}Adine, could you come over here?"
    $ renpy.pause (2.0)
    show naomi normal at right with ease
    show adine normal b flip at left with easeinleft
    Ad "Can I get you two anything else?"
    Nm "I would like some meat snacks with pasta and another glass of juice."
    Ad "Sure. What about you, [player_name]?"
    
    if naomi1drink == "cocktail":
         c "Just another cocktail of the same kind. It was great."   
    elif naomi1drink == "beer":
         c "Another beer, please. I liked it a lot."   
    else:
         c "I would like another [naomi1drink]."
    
    Ad "Alright. I'll be back shortly."
    play sound "fx/dishes.wav"
    m "Adine grabbed our dishes with surprising alacrity and rushed off to the kitchen."   
    show adine normal b with dissolve
    hide adine with easeoutleft
    hide naomi with dissolve
    show naomi normal with dissolve   
    Nm blank "So, you said you wanted to talk some more with me. How about a story while we wait for the food?"
    Nm confused "Did you really say that lunch breaks used to be mandatory in your world? I'm curious as to what changed that."
    c "It's a long one, so I'll just tell you the short version. Where to begin..."
    show naomi normal with dissolve
    c "Our living standards got significantly worse because we got messed up badly by a solar flare. Nowadays we don't really think about our long-term welfare like we used to."
    show naomi concern with dissolve
    c "Right now we pretty much live on a day to day basis, most of the time just barely managing to get by."
    show naomi sad with dissolve
    c "Uhh... anyway, I don't want to ruin the mood, so let's not talk about negative stuff any more than we have to."
    Nm "I'm so sorry to hear about something like that happening to your people. Hearing of humans suffering just breaks my heart."
    c "I appreciate that a lot. In fact, I hope your people can help us."
    Nm confused "How exactly do you think we would be able to help?"
    c "In short, we need your production facilities. Right now it's practically impossible for us to build an entire production chain from scratch. It's very hard for us to make even basic electronic devices, let alone something like computers." 
    c "We really can't even salvage because the flare pretty much destroyed almost everything electronic that wasn't locked away in a electromagnetic shock proof bunker. The best we can do is try to find some parts that weren't destroyed and hope we can actually build something useful out of them."
    c "With your resources and facilities we could resume production, while of course benefiting both parties. I believe our advanced technology would be a great boon to your people as a part of this exchange." 
    c "In the end, I hope the meeting of our peoples develops over time into a mutually beneficial and longstanding relationship."
    
    if naomi1mood > 0:
         Nm smile "That's a sentiment I share. I have enjoyed the relationship between our peoples so far."
         c "Thanks a lot. I'm glad I have made a good impression."
    else:
         Nm blank "Sure."
    
    show naomi normal with dissolve
    $ renpy.pause (2.0)
    m "After that exchange, it didn't take long for Adine to bring us our second serving of the evening."    
    show naomi normal at right with ease
    show adine normal b flip at left with easeinleft   
    play sound "fx/dishes.wav"
    Ad "Here's your second order. Have fun!"
    c "Thanks a lot."
    Nm "Thanks, Adine."    
    show adine normal b with dissolve
    hide adine with easeoutleft
    hide naomi with dissolve
    show naomi smile with dissolve
    play sound "fx/eating.wav"    
    m "As soon as our plates were in place, Naomi began to devour her meat snacks and pasta, albeit at a slower pace than last time."
    play sound2 "fx/coffee.wav"
    m "I focused on sipping my drink and watching her eat."   
    #more?
    
    if naomi1drink == "cocktail":
         c "This cocktail is really good. It brings me back to a time when things were less chaotic back in my home world."
         Nm normal "That's nice to hear. How do dragon cocktails compare to human ones?"
         c "It's not the type of cocktail I normally drink, but it's great one nonetheless. On top of that, this evening is of course a nice and peaceful experience to have after all that's happened to me."
         Nm smile "I'm happy to hear that."
         $ renpy.pause (2.0)
         Nm normal "Care to tell me what your cocktail tastes like?"
         c "Hmm...{w} that's a complicated question. Let me think of a way how to best describe it."
         $ renpy.pause (1.0)
         c "It's like if the contents of a fruit basket were having an orgy in my mouth."
         Nm surprised "Okay..."
         c "And then it's as if the orgy had just ended and everyone climaxed right into my tongue in a gigantic, fruity explosion of tasty juices coming together and swirling around in a dance..."
         Nm "I think I get the idea."
         c "It's a pretty great cocktail."
         $ renpy.pause (1.0)
         Nm confused "Now you got me curious. Mind if I take a sip?"
         c "Not at all."
         play sound "fx/glassdown.wav"
         m "I placed the cocktail over to Naomi's side of the table."
         play sound "fx/slurp.ogg"
         m "She carefully lowered her mouth to the edge of the glass and took a careful sip."
         $ renpy.pause (1.0)
         Nm surprisedblush "You were right." 
         Nm smile "I need to get one of these next time."
    
    if naomi1drink == "beer":
         c "I like this beer quite a lot. You can't get good quality stuff like this any more in my world."
         Nm normal "That brand is popular around here. How does it compare to human beer?"
         c "It doesn't taste anything like the mass-produced ones we used to have. I would say it's probably a local high-quality brand."
         c "An important thing to note though is that your beer is quite a bit stronger than what we humans normally drink. If I had to guess this particular beer is probably about nine to ten percent alcohol, so about twice as strong as regular beer in our world."
         show naomi blank with dissolve
         c "Of course we also have beer as strong as this, but people don't drink that stuff very often."
         c "This all does make sense though. You dragons are a lot bigger than humans so you need a lot more alcohol to get drunk."

         #if bryce1played == True:
             #c "I realized it would take forever for someone like Bryce to get drunk from regular human beer. Even this stronger stuff he has to gulp down really fast."
             #more
             
         Nm surprised "That's an interesting analysis."
         
    else:
        pass
        #an alternate discussion here?
        
    $ renpy.pause (2.0)
    c "To chat some more, would you care to tell me more about why you miss your lunch breaks so often?"
    Nm normal "Why not?"
    
jump sqb_naomi_cafe_eating_end

label sqb_naomi_cafe_money:
    
    c "I'm just kidding, because I don't really even care about money. We don't even use it any more in my city-state."
    Nm surprised "Really? How does a system like that even work?"
    c "Empirically speaking it seems to work fine for the time being. There even used to be political movements in our world that wanted to abolish the concept money, among other things."
    Nm confused "That sounds really weird to me. How did the people of your city-state conclude that they should get rid of money?"
    c "Well, for us it's more of a necessity dictated by our circumstances rather than a calculated choice." 
    c "Money needs to be backed by an institution with enough authority to be worth anything. I'm sure it works like that here too. Some time after the flare hit entire countries fell because of the destruction that it had caused, so physical money became pretty much worthless without a reliable backer." 
    c "On top of that, most of our money was stored electronically as a number on computer servers. You can probably guess what happened to that system when the flare hit. Not that it would have mattered long-term anyway."
    show naomi blank with dissolve
    c "Now there's no authority legitimate enough to keep track of how much of money people have. In the end because we couldn't print our own in my city-state, we decided have our markets operate based on pure labor power rather than accumulated wealth."
    c "Well, even if we could print our own money, that wouldn't really work because there aren't very many different consumer products anyone can buy due to what I told you about earlier." 
    c "Housing is pretty much free due to the amount of empty space. Also, most of the time only absolutely necessary utilities work. To avoid discontent, we decided to not charge anything for them."
    c "Due to these circumstances, introducing money again would probably just cause inflation and more inequality. So, now we just use labor as a currency, and a strict regime allocates important resources like food and water based on how much you work."
    c "Still, I don't understand why our city-state has to be so authoritarian. Unfortunately, dissenting voices are not allowed." #Dissenters get sent straight to the gulag
    show naomi sad with dissolve
    c "People just kind of accept the bad situation they're in and believe they are so powerless that they can't do anything to change it."
    c "In general life there is pretty terrible compared to how it used to be, but at least our scarce resources are allocated somewhat efficiently."
    c "Not that it's any better anywhere in our general vicinity at least. In fact, the belief that life is better inside the walls rather than outside is what keeps us going through the hardship."
    Nm "That sounds awful, [player_name]. I wouldn't want to live in a place like that."
    c "Yeah, I wouldn't either. Unfortunately, we don't have a choice."
    $ renpy.pause (2.0)
    
    if naomi1mood > 2:
         $ naomilewd +=1
         show naomi shy with dissolve
         m "Naomi seemed to be thinking about something."
         Nm "I just got an idea. Don't you think that a better choice opened up for your people when we were connected through the portal?" 
         Nm surprisedblush "Why don't we invite your people to live here with us?" 
         Nm smile "There's plenty of room for everyone. I know leaving your home behind can be hard, but the living conditions here are so much better compared to your world that I'm sure a lot of humans would be up for it."
         m "Her idea caught me off guard."
         c "I... um...{w} Do you think it could work?"
         Nm "Of course! Most of us already like humans and those in need should always be helped."
         c "That's a great idea! I haven't even thought of anything like that, even though the portal has been open for a time already."
         c "I'll ask my superiors what they think next the time we're in contact. Thanks a lot, Naomi."
         Nm "You're welcome."
         show naomi normal with dissolve
         $ renpy.pause (2.0)        
    else:
         Nm normal "I hope things get better for your people."
         Nm blank "Let's talk about something else."
         c "Alright."
         $ renpy.pause (2.0)
    
    c "Where were we..."
    c "Did you say you have had trouble finding a suitable boyfriend? I find that hard to believe."
    m "(Fuck, I did it again.)"
    Nm stern "What's that supposed to mean?"
    c "Oh, I was just wondering if you would consider me a suitable candidate."
    show naomi surprisedblush with dissolve
    $ renpy.pause (2.0)
    m "Naomi paused to think for a moment."
    Nm shy "Um...{w} are you sure you would be interested in forming a relationship outside your own species?"
    m "(YES!!! Wait, who was that? What's going on?)"
    c "..."
    c "..."
    show naomi confused with dissolve
    m "Naomi started looking at me curiously, waiting for an answer."
    Nm concern "Did you space out? My question wasn't rhetorical."
    c "Oh, right."
    c "That sounds fine to me. Both of our species are sentient and we can communicate verbally with each other so there aren't any problems with having one."
    
    if naomi1mood > 4:       
         $ naomi1mood += 1
         $ naomilewd +=1         
         Nm surprisedblush "You wouldn't mind either?" 
         Nm smile "I'm so relieved to hear that. After all, now that I have met you in the flesh, I think humans are cute."
         Nm shy "On top of that I like your personality, but still I think we should get to know each other a little better before we get into anything more serious."
         c "Of course, being pushy wasn't my intent. I was just speaking hypothetically, for now."
         Nm blank "Yes, of course."
         $ renpy.pause (1.0)
         Nm shy "Even though we are being hypothetical right now, I wouldn't mind having another get-together with you. Since I met you I have felt like there might be something more to you than what meets the eye at first meeting" 
         Nm normal "I want to find out what it is."
         c "I'll do my best to make the time. After all, to be on track to solve the problem that your parents were so worried about, I should get you to date me as soon as possible."
         Nm stern "..."
         Nm "Careful, you're pushing it."
         $ renpy.pause (1.0)
         c "Uhh...{w} speaking of your parents, what are they up to these days?"
         Nm blank "Oh, not much."
         Nm normal "They recently moved their business to the big city, and I stayed back here on my own."    
    else:   
         Nm normal "I never thought of it like that."
         c "So, what do you think?"
         Nm concern "..."
         c "You do have interspecies dating here, right?"
         $ renpy.pause (1.0)         
         Nm stern "Let's change the topic."
         c "Alright. What are your parents doing these days?"
         Nm blank "Oh, not much."
         Nm normal "They recently moved their business to the big city, and I stayed back here on my own."
 
jump sqb_naomi_cafe_money_end

label sqb_naomi_special_question:

     Nm smile "You're asking me that question again? You must be really interested in getting to date me."
     Nm blank "Like I already implied, I don't. I just haven't found the right person yet."
     Nm "For example, the guys at the department are nice, but we finish at different hours, and they have their own hobbies and routines. Bryce goes drinking, Seb is more of an indoor person, and Mav is just... Mav."

jump sqb_naomi_special_question_end
    