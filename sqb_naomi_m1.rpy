label sqb_naomi_cafe_discussion:

    menu:
        "Juice":
            $ renpy.pause (0.5)
            $ naomi1drink = "juice"
            c "Some juice would be good."
            Ad "Alright. I'll be right back."
            
        "Soda":
            $ renpy.pause (0.5)
            $ naomi1drink = "soda"
            c "Could you get me a soda?"
            Ad "Alright. I'll be right back."
            
        "Beer":
            $ renpy.pause (0.5)
            $ naomi1drink = "beer"
            c "Could you get me a local beer?"
            Ad "Alright. I'll be right back."
            
        "Coffee":
            $ renpy.pause (0.5)
            $ naomi1drink = "coffee"
            c "I'd love some coffee right now."
            Ad "Alright. I'll be right back."
            
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
         $ naomi1mood += 1
         Nm surprisedblush "Oh, thank you."
         c "Are you wary of drinking because of Bryce? Not everyone is like him."
         Nm concern "So, you know about his drinking problem?"
         
         if bryce1played == True:
             c "Yeah, I went drinking with him to get to know him better. Seems that's his favorite pastime."
             Nm stern "Drinking is all he does on his free time. I think he should get other hobbies."
         
         else:
             c "Unfortunately, I do."
             m "(Hold on, how do I know about it? Did someone tell me?)"
             Nm surprised "Oh well. It normally takes longer for people to find out." 
             Nm sad "I worry about him."
             
         c "Same here. He drinks way too much."
         c "Anyway, we shouldn't talk ill of someone who's not present."
         Nm blank "I suppose you're right."
         c "To change the subject, could you tell me more specifically what sort of work you do at the police station?"
         Nm normal "Sure."
    
    else: 
        pass

jump sqb_naomi_cafe_discussion_end

label sqb_naomi_cafe_eating:

    c "You finished fast. Was the food really that tasty, or did you eat it quickly just because you're just a very hungry dragoness?"
    Nm shy "Umm..."
    Nm smile "Both, I guess. It was delicious as always, but like I said, I was starving because I didn't have a lunch break."
    Nm concern "Unfortunately my work is often simply too important to have one."
    m "Since this was the second time she explicitly mentioned being overworked, I felt like I should finally push further on the issue."
    c "That's not good, especially if it happens regularly. Taking a lunch break makes you more efficient for the rest of the day. You can't do cognitively demanding work as effectively if you're hungry." 
    c "For this reason in most workplaces where I come from, lunch breaks used to be mandatory."
    Nm confused "Interesting. I'll keep that in mind."
    c "Also, starving yourself makes you eat too much when you finally have the time, which can lead to gaining weight." 
    c "Not that I think it would happen to you, as you're a big and athletic dragoness who I'm sure needs lots and lots of food to keep herself fed in the first place."
    Nm shy "I'm not sure how to respond to that. Thank you, I guess?"
    Nm surprisedblush "I suppose it's obvious looking at my physique that I work out a lot."   
    m "(Why did I even say that? I'm lucky she didn't take offense.)"
    show naomi normal with dissolve
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
            m "(I'm tired. I want to go back to my apartment before it gets late.)"
            c "So, you miss your lunch breaks often?"
            jump sqb_naomi_cafe_eating_end
    
    Nm confused "Are you sure you're fine watching me eat?"
    c "Of course. I don't mind staying with you a while longer, because then way we could talk some more."
    Nm normal "In that case..."
    Nm "Adine, could you come over here?"
    $ renpy.pause (1.0)
    show naomi normal at right with ease
    show adine normal b flip at left with easeinleft
    Ad "Can I get you two anything else?"
    Nm "I would like some meat snacks with pasta and another glass of juice."
    Ad "Sure. What about you, [player_name]?"
    
    if naomi1drink == "cocktail":
         c "Just another cocktail of the same kind. It was great."
    
    elif naomi1drink == "beer":
         c "Another beer, please. I quite liked it."
    
    else:
         c "I'd like another glass of [naomi1drink]."
    
    Ad "Alright. I'll be back shortly."
    play sound "fx/dishes.wav"
    m "She grabbed our dishes with surprising alacrity and rushed off to the kitchen."
    
    show adine normal b with dissolve
    hide adine with easeoutleft
    hide naomi with dissolve
    show naomi normal with dissolve
    
    Nm blank "So, you said you wanted to talk some more. How about a story while we wait for the food?"
    Nm confused "Did you say lunch breaks used to be mandatory in your world? I'm curious as to what changed that."
    c "It's a long one, so I'll just tell you the short version."
    c "Where to begin..."
    show naomi normal with dissolve
    c "The living standards got significantly worse because our civilization was messed up really badly by a solar flare." 
    c "Nowadays we don't really think about our long-term welfare like we used to."
    show naomi surprised with dissolve
    c "Right now we pretty much live on a day to day basis, barely managing to get by."
    show naomi sad with dissolve
    c "Uhh... anyway, I don't want to ruin the mood, so let's not talk about negative stuff any more than we have to."
    Nm "I'm so sorry to hear about something like that happening to your people. Thinking of humans suffering just breaks my heart."
    c "I appreciate that. In fact, I hope your people can help us."
    Nm confused "How exactly do you think we can help?"
    c "In short we need your production facilities. Right now it's practically impossible for us to build a production chain from scratch. It's very hard for us to make even basic electronic devices, let alone something like computers." 
    c "We really can't even salvage because the flare pretty much destroyed almost everything electronic that wasn't locked away in a electromagnetic shock proof bunker."
    c "The best we can do is try to find some parts that weren't destroyed and hope we can actually build something useful out of them."
    c "With your resources and facilities we could resume production, and benefit both parties. I believe our advanced technology would be a great boon to your people as a part of this exchange." 
    c "In the end I hope all this develops into a mutually beneficial and longstanding relationship."
    
    if naomi1mood > 2:
         Nm smile "I share your sentiment. I have enjoyed myself so far."
         c "Thanks."
    else:
         Nm normal "Sure."
    
    show naomi normal with dissolve
    m "After that, it didn't take long for Adine to bring us our second serving for the evening."
    
    show naomi normal at right with ease
    show adine normal b flip at left with easeinleft
    
    play sound "fx/dishes.wav"
    Ad "Here's your second order. Have fun!"
    c "Thanks again."
    Nm "Thanks, Adine."
    
    show adine normal b with dissolve
    hide adine with easeoutleft
    hide naomi with dissolve
    show naomi smile with dissolve
    
    m "As soon as our plates were in place, Naomi began to eat her meat snacks and pasta, albeit at a slower pace than last time."
    play sound "fx/coffee.wav"
    m "I focused on sipping my drink and watching her eat."
    
    #more?
    
    if naomi1drink == "cocktail":
         #The cocktail glass as a character?
         c "This cocktail is really good. It brings me back to a time when things were less chaotic in my home world."
         Nm normal "How do dragon cocktails compare to human ones?"
         c "It's not the type I normally drink, but it's great cocktail nonetheless."
         c "On top of that, this evening is of course a nice experience to have after all that's happened."
         Nm smile "I'm happy to hear that."
         Nm normal "Care to tell me what your cocktail tastes like?"
         c "Hold on... let me think of how to best describe it."
         c "It's like if the contents of a fruit basket were having an orgy in my mouth."
         Nm surprised "Okay..."
         c "And then its as if the orgy had just ended and everyone climaxed right into my tongue in a gigantic, fruity explosion of tasty juices coming together and swirling around in a dance..."
         Nm "I think I get the idea."
         c "It's a pretty great cocktail."
         Nm confused "Now you got me curious. Mind if I take a sip?"
         c "Not at all."
         play sound "fx/glassdown.wav"
         m "I placed the cocktail over to Naomi's side of the table."
         play sound "fx/slurp.ogg"
         m "She carefully lowered her mouth to the edge of the glass and took a sip."
         Nm smile "You were right." 
         Nm surprisedblush "I need to get one of these next time."
    
    if naomi1drink == "beer":
         c "I like this beer quite a lot. You can't get good quality stuff like this any more in my world."
         Nm normal "That brand is popular around here. How does it compare to human beer?"
         c "It doesn't taste anything like the mass-produced ones we used to have. I'd say it's probably a local high-quality brand."
         c "An important thing to note though is that your beer is quite a bit stronger than what we humans normally drink."
         c "If I had to guess this particular beer is probably about nine to ten percent alcohol, so about twice as strong as regular beer in our world."
         c "Of course we also have beer as strong as this, but people don't drink that stuff as often."
         c "This all does make sense though. You dragons are a lot bigger than humans so you need a lot more alcohol to get drunk."

         if bryce1played == True:
             c "I realized it would take forever for someone like Bryce to get drunk from regular human beer. Even this stronger stuff he has to gulp down really fast."
             #more
             
         Nm surprised "That's an interesting analysis."
         
    else:
        pass
        #an alternate discussion here?
    
    
    c "Anyway, care to tell me more about why you miss your lunch breaks so often?"
    Nm normal "Sure."
    
jump sqb_naomi_cafe_eating_end

label sqb_naomi_cafe_money:
    
    c "I'm just kidding. I don't really care about money. We don't even use it any more where I come from."
    Nm surprised "Really? How does a system like that even work?"
    c "Empirically speaking it seems to work fine for the time being. There even used to be political movements in our world that wanted to abolish the concept money, among other things."
    Nm confused "That's weird."
    c "Well, for us it's more of a necessity dictated by our circumstances instead of a calculated choice."
    c "Money needs to be backed by some kind of party with enough authority to be worth anything. I'm sure it works like that here too."
    c "Some time after the flare hit entire countries fell because of the destruction it had caused, so physical money became pretty much worthless without a reliable backer." 
    c "On top of that most of the rest of our money was stored electronically as a number on some computer. You can guess what happened to that system when the flare hit. Not that it would have mattered long-term anyway."
    show naomi blank with dissolve
    c "Now there's no authority legitimate enough to keep track of how much of it people have."
    c "In the end because we can't print our own money in my city-state, we decided have our markets operate based on need rather than wealth."
    c "Well, even if we could print our own money, that wouldn't really work that well because there are almost no commodities anyone can buy due to what I told you earlier."
    c "Now we kind of just use labor as a currency, and a strict regime allocates resources based on how much you work."
    c "Still, I don't understand why our city-state has to be so authoritarian. Unfortunately dissenting voices are not allowed."
    show naomi sad with dissolve
    c "People just kind of accept the bad situation they're in and believe they are so powerless that they can't do anything to change it."
    c "In general life there is pretty terrible compared to how it used to be, but at least our scarce resources are allocated somewhat efficiently."
    c "Not that it's any better anywhere in our general vicinity at least. In fact, the belief that life is better inside the walls rather than outside is what keeps us going through the hardship."
    Nm "That sounds awful, [player_name]. I wouldn't want to live in a place like that."
    
    if naomi1mood > 6:
         m "Naomi seemed to be thinking about something."
         Nm shy "I just got an idea." 
         Nm "Why don't we invite your people to live here with us? There's plenty of space for everyone."
         m "Her idea caught me off guard."
         c "I... um..."
         c "D-do you think it would work?"
         Nm smile "Of course it would! We like humans and and the benefits would be mutual."
         c "That's...{w} a great idea! I've never even thought of anything like that being realistically achievable."
         c "I'll ask my superiors what they think next the time we're in contact."
         c "Thanks, Naomi."
         Nm "You're welcome."
         $ naomilewd +=1
         show naomi normal with dissolve
         
    else:
         Nm "I hope things get better for your people."
         Nm normal "Let's talk about something else. You're ruining the mood again."
         c "Sorry."
    
    c "Where were we..."
    c "So, have you had any luck finding a boyfriend? Somehow I find that hard to believe."
    m "(Fuck, I did it again.)"
    Nm stern "What do you mean?"
    c "I was just wondering if you would consider me a suitable candidate?"
    show naomi surprisedblush with dissolve
    m "Naomi paused to think for a moment."
    Nm shy "Um... are you sure you would be interested in forming a relationship outside your own species?"
    m "(YES!!! Wait, who was that? What's going on?)"
    c "..."
    c "..."
    show naomi confused with dissolve
    m "Naomi started looking at me curiously, waiting for an answer."
    Nm "Did you space out again? My question wasn't rhetorical."
    c "Oh, right."
    #Choice here?
    c "I wouldn't mind that. Both our species are sentient and we can communicate well so there shouldn't be any problem with that."
    
    if naomi1mood > 2:
         
         $ naomi1mood += 1
         $ naomilewd +=1
         
         Nm surprisedblush "You wouldn't mind either?" 
         Nm smile "I'm so relieved to hear that. After all, now that I have met you in the flesh, I think humans are cute."
         Nm shy "On top of that I like your personality, but still I think we should get to know each other a little better before we get into anything more serious."
         c "I was just speaking hypothetically."
         Nm blank "Yes, of course."
         Nm shy "Even though we are being hypothetical right now, I wouldn't mind having another get-together with you." 
         Nm normal "Since I met you I've felt like there might be something more to you than what meets the eye." 
         Nm shy "I-I want to find out what it is."
         c "I'll do my best to make the time."
         c "After all, if I manage to get you to date me, we're on track to solve what your parents were so worried about."
         Nm stern "..."
         c "Uhh... speaking of your parents, how are they doing?"
         Nm blank "Oh, nothing much."
         Nm normal "They recently moved their business to the big city, and I stayed back here on my own."
    
    else:
    
         Nm normal "I never thought of it like that."
         c "So, what do you think?"
         Nm concern "..."
         c "You do have interspecies dating here, right?"      
         Nm stern "Let's change the topic."
         c "Alright."
         c "How are your parents doing?"
         Nm normal "They recently moved their business to the big city, and I stayed back here on my own."
 
jump sqb_naomi_cafe_money_end

label sqb_naomi_special_question:

     Nm smile "You're asking me that question again? You must be really interested in getting to date me."
     Nm blank "Like I already implied, I don't. I just haven't found the right person yet."
     Nm "For example, the guys at the department are nice, but we finish at different hours, and they have their own hobbies and routines. Bryce goes drinking, Seb is more of an indoor person, and Mav is just... Mav."

jump sqb_naomi_special_question_end
    