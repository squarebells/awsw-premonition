label sqb_naomi_m4_skip:
    
    stop music fadeout 1.0
    play sound "fx/system3.wav"    
    s "Would you like to skip to the fun or straight to the ending? If you have NSFW mode disabled, you won't be able to see the fun though."       
    menu:
        "Fun.":
            s "Alright."
            scene black with dissolvemed
            $ renpy.pause (1.0)
            play music "mx/treetops.mp3"
            scene eckswimmingpool with dissolvemed
            show naomi smile with dissolve
            jump eck_naomi_m4_skip    
        
        "Ending.":
            s "Alright."
            $ renpy.pause (1.0)
            $ sqbnaomi4hadsex = True
            jump eck_naomi_m4_morning

label sqb_naomi_m4_start:

    Nm smile "Oh, well, hopefully that won't be an issue for you tonight. I would be very disappointed if you couldn't perform."
    show sebastian shy b flip with dissolve
    m "Sebastian was about to say something, but then he stopped and looked away from us."
    $ renpy.pause (1.0)
    Nm normal "Anyway, we discovered this ancient sunken facility, explored it for a while and found some stuff. But then, its generator was about to blow up due to seawater we let in by accident. Thankfully, by working together we managed to find a solution in time."

jump sqb_naomi_m4_start_end

label sqb_naomi_m4_pool: #Just straight copy pasting a lot of ECK's script because I don't want to make a million hooks and labels

    c "Also, there's no lockers or containers for my clothes. I guess I'll just have to drop them on the floor."
    Nm blank "Is that a problem?"
    c "They might get wet or dirty. Wet clothes aren't very nice to wear, especially if it's cold. We have to leave this place at some point, you know."
    Nm normal "Just put them on the lounge chair over there. I think it's far enough from the pool, so I can easily avoid splashing any water over there."
    c "I guess that will work."
    Nm smile "Oh, I got you another wetsuit just in case, but could I suggest that you'll put us on equal footing by swimming naked as well?" 
    Nm "Those windows are almost completely opaque to anyone trying to look in from the outside, so you won't have to worry about any flying dragons or someone using binoculars to peek at your private parts."
    c "Sure, that works for me. You're right that I would be a little hesitant to be here naked with you if anyone could see me from the outside."
    Nm normal "We don't need the wetsuit then."
    m "Naomi pulled out a small plastic package from her belt bag, which presumably held the wetsuit, and placed it on the floor."
    c "No, it's actually very useful. I can store my clothing in that package, so they won't get wet."
    Nm smile "I guess I am prepared for everything."
    play sound "fx/undress.ogg"
    hide naomi with dissolve   
    m "I took all my clothes off and started stuffing them in the plastic package with the wetsuit."
    play sound "fx/watersurface.ogg"
    m "Meanwhile, Naomi had dropped her own bag on the floor and happily jumped into the water. I expected a huge splash, but her entry was surprisingly smooth."
    m "She swam a few quick laps around the perimeter and then stopped at the corner opposite from the panoramic windows. Propping her back against both walls, she leaned back and relaxed in the shallow end."
    m "Done with storing my clothes in the package, I joined her in the pool."
    play sound "fx/watersurface.ogg"
    show naomi normal with dissolve    
    c "Enjoying yourself?"
    Nm smile "Naturally."
    Nm "Clean warm water, a quiet evening, nice company. After all the recent craziness, what's there not to like, [player_name]?"
    c "Yeah. A moment to take a breather for us both."
    Nm blank "I should've brought us some drinks, but I'm a little wary of alcohol."
    c "Yeah, I've noticed. I like a bit of alcohol every now and then, especially in good company. Drinking almost every day like Bryce does is very bad for you both physically and mentally though."
    Nm concern "I agree. He drinks way too much for his own good, and in a way, I'm rather afraid of ending up like him." #Skipping condition since Bryce can't be dead in this timeline, unless you did something weird
    c "Based on your personality, I doubt that would happen to you. Also, you have me to help keep you on the right track."
    show naomi blank with dissolve
    c "Now, I'm not saying this because I want you to drink more alcohol, I just think that you evidently have more self-control than he does. I could never work as late as you do or regularly skip my lunch breaks."
    show naomi normal with dissolve
    c "Those are obviously not good things to do, but they're still something that most people don't have the willpower for."
    Nm smile "I understand your point. From your perspective, that's a strange yet nice compliment."
    Nm normal "Anyway, a part of me wants to tell Bryce to look after himself better and cut down on alcohol, but I can't bring myself to invade his personal life with unsolicited advice."
    c "Nothing is stopping you from doing so. You are friends, and it's natural that you would be concerned about his well-being. Just remember that if you bring it up too often your good intentions might backfire and cause him to drink even more."
    Nm smile "That's a good point."
    Nm shy "Still, I'm hesitant because he hasn't really changed, despite all the time he has spent spent in the local bar. And... and maybe, it's just not my business after all. He does what he does to cope with the stress."
    c "I think you could try to speak up. In fact, we could mention this to him together next time we meet him on his free time."
    Nm normal "I'll think about it."
    Nm "But for now, it's just you and me here, so I would rather focus on the pleasant stuff."
    c "Sounds like a fine idea."
    Nm smile "I'm glad we share this sentiment."    
    c "Though, I'm surprised you haven't invited anyone else to join us."
    Nm surprisedblush "I didn't know you wanted to move onto threesomes already. You're way kinkier than I thought."
    $ renpy.pause (2.0)
    c "Naomi, that's not what I meant."
    Nm smile "I know, I was just teasing you."
    Nm normal "Actually, this meeting is sort of an apology to you for what happened during our last date."
    Nm "And since I honestly don't know how well you get along with the others, I decided against taking any risks of ruining this one."
    c "Hey, it's all good. We have also had some really fun times with just the two of us, right? Besides, this pool is certainly too small for more than two people."
    Nm smile "Yeah. We've already done so much together. I can't wait to find out what the future holds."
    hide naomi with dissolve    
    m "Naomi beckoned me to come closer, which I did, swimming up to her side."
    scene eckswimmingpool2 with dissolvemed
    m "She unfolded her wing and gently pressed it against my back, giving it some extra support. I wrapped my right arm around her shoulders."
    $ renpy.pause (1.5)
    show ecknaomicg2 at Pan ((0, 0), (180, 130), 8.0) with dissolvemed
    $ renpy.pause (7.5)
    Nm normal "The evening sky is quite beautiful today, isn't it?"
    c "Yeah. I really like the view and atmosphere of this place."
    Nm shy "On the way here, I was a little nervous, to be honest. Had some doubts about the penthouse section being the right choice for our meeting. But, I'm happy you're enjoying it."
    c "Well, the glass being almost opaque to anyone looking from the outside helps a lot. I'm happy that you're concerned about my privacy, even though I might seem to be a bit prudish to you. Thank you for respecting the traditions of my people." 
    Nm smile "Maybe one day you'll walk around naked in public like most of us."
    c "You wish."
    hide ecknaomicg2 with dissolvemed
    show naomi smile with dissolve
    $ renpy.pause (1.0)
    m "Naomi tied her own arm around me and turned her snout close to my face, looking at me with a cute smile."
    Nm "So, how about a little kiss?"
    c "Always."
    play sound "fx/kiss.wav"
    $ renpy.pause (1.0)
    show naomi aroused with dissolve
    queue sound "fx/lewd/lickslow.ogg"
    queue sound "fx/lewd/pussy.ogg"
    m "I leaned over and kissed Naomi. When we made contact, she penetrated my lips with her long tongue and wriggled it inside my mouth. As I pulled back, I gently sucked on her tongue, and after I was done she flicked my nose and temple with it."
    Nm smile "You're so cute. I love being around you so much."
    c "Me too. Being with you is the best thing that has ever happened to me."
    $ renpy.pause (2.0)

jump sqb_naomi_m4_pool_end

label sqb_naomi_m4_meetinghumans:

    Nm smile "And if I hadn't started working there, I never would've had the chance to get to know you so very intimately, [player_name]."        
    c "I bet a lot of dragons would've been happy to meet a human, let alone have sex with one."
    Nm smile "Very true. I can't believe how lucky I am."
    Nm normal "I never was a big fan of the human mythos personally, to be honest. But an alien from another world is no less exciting. We aren't alone in the universe, after all."
    c "I agree. For a sociologist, visiting the world of another species is a seemingly impossible dream come true."
    
jump sqb_naomi_m4_meetinghumans_end

label sqb_naomi_m4_returndiscussion:

    #I've been waiting for so long to write this
    $ renpy.pause (2.0)    
    Nm shy "This whole talk made me even more concerned about your safety. You're still going to stay here with me, right?"
    c "I don't think I have a choice, because you said you wouldn't even let me leave."
    Nm confused "You know that I was just joking, right? If you want to leave, it's up to you, but I would urge you to really think it through before you make that choice."
    $ renpy.pause (2.0)
    c "I know, I was just joking as well. Of course I'll stay with you."
    show naomi smile with dissolve
    c "To be honest, no sane person would ever want to go back to that post-apocalyptic hellhole, even if they were bound by duty to their people, like me." 
    c "Besides, if your conclusions are correct it seems that I basically have been betrayed by some in the leadership doing shady operations behind my back that might end up jeopardizing my mission."
    show naomi blank with dissolve
    c "So fuck them. All this would have been so easy if some of them hadn't been so greedy and hostile towards your people. They're really just a bunch of authoritarian assholes who only care about staying in power no matter the cost."
    show naomi surprised with dissolve
    c "To be completely honest, I don't really give a shit about what happens to my city-state anymore." 
    c "If this mission fails and the relations between our peoples go hostile, it would be unreasonable to expect me to fix it because none of this is my fault in the first place. I have been doing everything in my power to establish friendly relations."
    c "It's unfortunate that innocent people will have to suffer, but at the same time it's also unfair to saddle some random guy with two college degrees with the responsibility of fixing everything."
    c "All this said, after we stop Reza I'm just going to chill out in your world and not give a fuck anymore. There is only so much hardship one can take."
    Nm concern "That's a very difficult decision to make. Are you sure you want to abandon your people like that?"
    c "I've been through a lot, so I just don't care anymore. I'll just stay here, and they can fix the problems of their own world by themselves. To me it almost feels like they're just trying to hinder my sincere and good-willed efforts every step of the way."
    Nm smile "Alright. It seems you have really thought this through, and I trust your judgment."
    Nm "Like you already know, we'll be very happy to have you, especially me. Also, there's still a possibility for my dream of humans migrating here coming true."
    c "Sure. Actually, that's a goal I could still work towards."   
    Nm normal "Also, I realized that if Reza succeeds in his mission, your rulers wouldn't want to leave an uncomfortable witness. If we apprehend and convict Reza, they wouldn't take kindly to someone who played a crucial role in foiling their plans."   
    c "Good point."
    Nm stern "Yeah, they need the generators, like you have said on occasion. They don't need you."    
    Nm shy "Sorry, if I sounded too harsh."
    c "It's fine, because you're right. It seems that the only way for me to stay on good terms with my city-state's leadership would be to help Reza complete whatever plan he has and that's never going to happen." 
    c "I'm in danger in my own world no matter what reasonable course of action I choose to take."
    Nm stern "Yeah, I bet they'd just drop a stone on your head and call it an accident. These kinds of people will step over as many dead bodies as necessary to reach their goals."
    c "I agree. I would like to avoid getting assassinated, thank you very much."  
    c "Also, let me remind you that even if they don't murder me right away they would still most likely make up some arbitrary reason to justify never letting me come back."
    Nm sad "There's a high chance of that happening as well, yes. If you go through the portal I will most likely never see you again."
    c "Don't worry, I will stay with you no matter what happens."
    Nm smile "Thank you so much for making the correct choice. You have no idea how relieved I am, mostly for your sake though."
    $ renpy.pause (2.0)
    c "It's settled then, once and for all. Let's just agree for now that our first priority is stopping Reza. Only then we can start planning what to do next, together."
    Nm normal "Sounds like a plan."

jump sqb_naomi_m4_returndiscussion_end

label sqb_naomi_m4_interspecies:
    
    $ renpy.pause (0.5)
    c "To our lovely interspecies relationship, and let's hope many others experience one as well!"
    Nm smile "I'm with you on that. If we manage to start a migration plan there will be a lot of dragons interested in forming relationships with humans."
    c "There's a small problem though, since from what I know, there aren't that many of us left in my city state compared to you. If my calculations are correct, the dragon-to-human ratio is already hundred to one. On top of that you need to keep in mind that not everyone will agree to migrate."
    c "I just hope that there will be enough humans to go around."
    Nm aroused "{cps=20}There's a solution for that...{/cps}"
    m "I shuddered at the thought of what she was implying."
    c "Oh."
    $ renpy.pause (2.0)
    show naomi smile with dissolve
    c "Let's drink."
    play sound "fx/gulping.wav"   
    m "I took another long sip of my drink, mindful to keep enough of it at least for one final round."

jump sqb_naomi_m4_interspecies_end

label sqb_naomi_m4_funparts:
   
    Nm smile "This place is all ours until morning. You can sleep on top of me."    
    c "Sounds like a plan."
    show naomi aroused with dissolve
    play sound "fx/craphug.mp3"
    m "Instead of responding verbally, Naomi tied me in a big dragon hug, and pressed me down on the floor. While most of her weight was shifted to her arms and legs, I was still practically pinned down by her soft underside."
    m "Her draconic hand supported the back of my head and neck, acting as a small pillow. I looked up at her face. Our eyes met, and we kissed."
    play sound "fx/kiss.wav"
    queue sound "fx/lewd/lickslow.ogg"
    $ renpy.pause (2.0)    
    c "Ever since we got here, I have been waiting for this part."
    Nm smile "You can say that again."
    
    if persistent.nsfwtoggle == False:
        $ renpy.pause (2.0)
        stop music fadeout 1.0
        play sound "fx/system3.wav"
        show naomi stern with dissolve
        s "Skipping the lewd scene since it looks like you have the NSFW mode turned off."
        $ sqbnaomim4hadsex = True
        hide naomi with dissolve
        jump eck_naomi_m4_morning       
    else:
        pass 

    Nm "Are you fine with me being on top this time?"
    c "Depends. Do they have any mattresses we can use?"
    Nm blank "There aren't any here at the pool, and the receptionist is probably still asleep. Why do we need a one, though?"
    c "I'm actually not very comfortable right now because the tiled floor is rather cold and hard. Also, you weigh a lot more than me. I know I said my body can take some pressure but just to be safe we should try some other position."
    c "Some broken bones in case you get a little bit too excited doesn't sound like a good time to me."
    $ renpy.pause (2.0)
    hide naomi with dissolve
    m "Naomi got off of me and sat down on her rump."
    show naomi shy with dissolve
    Nm shy "I suppose I still have some more to learn about human physiology. Let's try something else then."
    Nm smile "How about this?"
    $ renpy.pause (2.0)
    hide naomi with dissolve
    m "Naomi got up on all fours, turned around and lifted her backside and tail up. I could see her glistening and aroused dragon pussy."
    show naomi smile with dissolve
    Nm "Well?"
    c "Alright, let's try this."
    hide naomi with dissolve
    m "I walked up to her and used one hand to support myself by grabbing her tail and the other to work my dick in order to fuck her."
    m "As I started positioning myself closer in order to penetrate Naomi from behind, my foot slipped a little bit because of the wet floor. I managed to stop myself from falling by holding onto Naomi's tail."
    show naomi confused with dissolve
    Nm "Phew, that was close. Are you okay?"
    c "I'm fine, but I just found out that since the floor is wet this position doesn't really work either because I might slip again when we start really getting into it. Let's try to figure out something else." 
    Nm surprisedblush "So fussy. Oh well, I should trust you to know your bodily limits."   
    c "Yeah, I don't want to hurt myself, since that would really ruin this evening. I think we should try new positions next time we do it in bed. There we can experiment safely."
    Nm blank "Alright. How about you decide the position then?"
    c "How about you lie down on your back and I'll fuck you from the front? I don't think those lounge chairs are big enough so it will have to be on the floor."
    Nm normal "Fine. That works for me."
    hide naomi with dissolve
    m "Naomi turned around again, laid down on her back and spread her wings for balance. After that she spread her legs, giving me unobstructed access to her draconic pussy."
    show naomi aroused with dissolve    
    m "Then she gestured for me to come and get her by wagging a finger at me." 
    Nm smile "Come show me a good time, my human lover."
    c "I'd be right happy to!"
    m "I stroked my dick to harden it as I got over to Naomi. I positioned myself between her large thighs, sitting on the base of her tail."
    c "You asked me at the beach which exposed part of you I like the most, and I have to admit that from a human perspective I like your thighs. They're so big and naughty."
    show naomi surprisedblush with dissolve
    c "They're my favorite, if we don't count your dragon pussy."
    Nm shy "Oh. Thank you for the compliment."
    Nm normal "Since my species is not as good at flying like Maverick for example, I had to compensate by training my body harder." 
    Nm "My strong thighs for example, allow me to run and jump well enough so that I don't always have to take off from the top of a building or some other high place."
    Nm "I can also land at higher speeds much more safely than someone of my species that hasn't trained."
    c "You training your body to become strong makes you very hot. Still, you forgot how your thighs are great toys for squeezing while I fuck you."
    
    if sqbnaomi2sexroundtwo == True:
        c "Remember last time?"
    else:
        pass
    
    show naomi shy with dissolve    
    c "I'll be sure to feed and exercise you a lot so you stay in a cute and cuddly shape."
    Nm smile "Please feed my egg-hole a lot of your human seed as well."
    $ renpy.pause (1.0)
    Nm blank "I'm incredibly horny right now. Start getting into it already."
    
    if modinfo.has_mod("BangOk?") and persistent.bangok_cloacas == False:
        play sound "fx/lewd/pussy.ogg"
        show naomi smile with dissolve
        m "After being given permission, I spread Naomi's pussy with my fingers and lined the tip of my dick to penetrate her."
        play sound "fx/lewd/penslow.ogg"
    else:
        play sound "fx/lewd/pussy.ogg"
        show naomi smile with dissolve
        m "After being given permission, I spread Naomi's cloaca with my fingers and lined the tip of my dick with her vaginal passage."
        play sound "fx/lewd/penslow.ogg"
        
    play sound "fx/lewd/penfast.ogg"
    show naomi surprisedblush with dissolve
    m "With my dick ready in this proper place, I supported myself by placing my arms around Naomi's lower back. Then, without hesitation I plunged myself as far as I could go into her."
    play sound "fx/lewd/penslow.ogg"
    m "Being prepared, Naomi locked me in place with her legs the moment I penetrated her. From our last time, I knew that there was no escape until I had released my human seed into her most special place."   
    Nm aroused "Remember, don't pull out."
    c "I know the drill."
    play soundloop "fx/lewd/penslow.ogg"
    show naomi smile with dissolve
    m "I lowered my body on Naomi and started fucking her pussy with slow, deep thrusts. She tied her arms around my upper body, tying me to her completely."
    $ renpy.pause (4.0)
    Nm "You're so cute when you cling to me, holding for dear life."
    c "That's because your belly is just that soft and cuddly. I realize now that a live dragon-cushion is all I ever should have wanted in life."
    $ renpy.pause (1.0)
    m "I used my other hand to squeeze Naomi's well-defined thigh. This gave rise to a pleasant shudder in her."
    show naomi shy with dissolve
    c "I can feel the muscles, Naomi. You have worked really hard for this."
    Nm "T-thank you."
    $ renpy.pause (4.0)
    stop soundloop fadeout 1.0
    play soundloop "fx/lewd/penfast.ogg"
    m "I shifted my position as I started fucking Naomi faster. As a response, she started moaning silently and gently rubbing the back of my neck with her hand."
    Nm aroused "Ahh...{w} your dick feels so good inside me. You can fuck me faster if you want."
    m "I was at the limit of my fucking ability, but I decided to not say anything. I just kept fucking her the same way as before because it seemed to be working fine."
    $ renpy.pause (2.0)
    Nm shy "[player_name]...{w} I'm going to come soon."
    c "Already?"    
    m "To think of it, throughout our intimate session I had felt hints of Naomi being a lot more sensitive this time. Realizing one of the possible reasons for that made me shudder and feel a strange tingle in the back of my head."
    m "I stopped myself from obsessing about the extremely unlikely but still possible implications of that, and instead focused on making Naomi feel as good as possible."
    c "I'm still some ways off from coming myself."
    Nm aroused "Then I want you to keep fucking me through my orgasm. Just shoot your seed inside me as soon as possible."
    $ renpy.pause (2.0)
    m "As I kept pounding Naomi's dragon-pussy, suddenly I felt her starting to shake subtly. She pressed my entire body into her even more strongly than before. When I was as close as I could get to her, I could feel that something powerful was building up in her."
    c "Careful, Naomi!"
    Nm shy "I'm..."
    m "Naomi came with a cry of ecstasy. Her vaginal walls clamped on my dick, desperate to milk me dry. Thankfully, even though she was already holding me tightly, she didn't break any of my bones in her excitement."
    play sound "fx/snarl.ogg"
    play sound2 "fx/lewd/pussy.ogg"
    stop soundloop fadeout 1.0
    play soundloop "fx/lewd/penslow.ogg"
    Nm cums "...coming!"
    $ renpy.pause (2.0)
    show naomi aroused with dissolve
    stop soundloop fadeout 1.0
    play soundloop "fx/lewd/penfast.ogg"
    m "After her orgasm, Naomi released her full-body grip on me as she went half-limp. Even though she was out of it for the time being, I resumed fucking her rapidly, in order to reach my own release."
    show naomi slsmile with dissolve
    $ renpy.pause (4.0)
    m "Then, after a few more moments of fucking Naomi's dragon pussy, my dick started to erupt. I hoped my balls were churning a very virile and extra-thick dose of human seed in order to satisfy her."
    $ renpy.pause (2.0)
    stop soundloop fadeout 1.0
    play sound "fx/lewd/altpen.ogg"
    $ renpy.pause (1.0)
    play sound "fx/lewd/altpen.ogg"
    queue sound "fx/lewd/altpen.ogg"
    play sound2 "fx/lewd/cum.ogg"
    queue sound2 "fx/lewd/cum.ogg"
    queue sound "fx/lewd/altpen.ogg"
    m "I reached my absolute limit, plunged myself inside Naomi as deep as possible, and exploded inside her."
    $ renpy.pause (2.0)
    show naomi aroused with dissolve
    m "I was proud of myself, as I had managed to shoot two large loads of my cum into Naomi's most feminine place. If she wasn't superbly satisfied after this, I would be completely at a loss on how to perform well enough for her."
    m "My dick went limp inside Naomi and so did I, as I slumped on top of her." 
    m "I had come so much that some of my semen had already started seeping out of Naomi's pussy. Thankfully due to where we were at, washing ourselves would be easy."
    $ renpy.pause (2.0)
    play sound "fx/lewd/pussy.ogg"
    queue sound "fx/kiss.wav"
    show naomi shy with dissolve
    m "Naomi pulled me out of her and lifted me up in front of her snout. Then she kissed me passionately."
    show naomi smile with dissolve
    play sound "fx/lewd/lickslow.ogg"
    queue sound "fx/rub2.ogg"    
    m "As she was doing her work inside my mouth, she hugged me tightly with one arm and rubbed her lower belly with the other one."
    Nm "That was amazing. You came almost as much as a dragon, and that certainly satisfied me."
    c "Anything for my beautiful and cute dragoness."
    Nm "Oh thank you, my cuddly and virile human."
    $ renpy.pause (2.0)
    Nm normal "I'm completely beat, so no second rounds this time. Right now I just want to hug you to sleep while fantasizing about our future together."
    m "(I guess we will wash ourselves in the morning.)"
    c "Sure. That's just what I was thinking of as well."
    show naomi slsmile with dissolve
    play sound "fx/craphug.mp3"
    m "With my agreement, Naomi wrapped her wings around me and supported my head with her draconic hand, in order to make sure I would stay still while I slept on top of her. Lastly, she shifted her lower body upwards slightly, presumably to stop most of my semen from flowing out of her pussy."   
    m "(She's really trying as hard as possible to conceive, isn't she? I'm afraid I'm going to have to break the bad news to her some time. Not right now though."
    play sound "fx/purr.ogg"
    play sound2 "fx/rub2.ogg"
    m "Then, she closed her eyes and started humming contently and quietly as she gently and slowly rubbed my body against hers."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    c "You're the best, Naomi. I love you so much."
    Nm "Shh...{w} I love you too [player_name], but no talking any more. Let's just feel each other's bodies and drift off to sleep."
    c "Fine."
    scene black with dissolveslow
    m "Obeying Naomi, I shut my eyes and steadied myself on her body in a slightly more comfortable sleeping position."
    $ renpy.pause (4.0)
    m "Even though I didn't feel tired, it didn't take me very long to fall asleep in her loving embrace."
    $ renpy.pause (2.0)
    $ sqbnaomim4hadsex = True
    $ persistent.sqbnaomi4sex = True

jump eck_naomi_m4_morning

label sqb_naomi_m4_fun_orig:

    $ renpy.pause (1.0)
    show naomi sad with dissolve
    play sound "fx/system3.wav"
    s "Under construction, check back later. Meanwhile, you can enjoy the new timeline date 2 and 4 fun scenes."
    $ renpy.pause (1.0)
    show naomi slsmile with dissolve
    m "For a time, I forgot about everything. There was only she, I and the warmth we shared."
    $ naomiromance += 100
        
jump eck_naomi_m4_morning

label sqb_naomi_m4_fun_orig2:

    $ renpy.pause (1.0)
    show naomi sad with dissolve
    play sound "fx/system3.wav"
    s "Under construction, check back later. Meanwhile, you can enjoy the new timeline date 2 and 4 fun scenes."
    $ renpy.pause (1.0)
    show naomi slsmile with dissolve
    m "For a time, I forgot about everything. There was only she, I and the warmth we shared."
    $ naomiromance += 50
        
jump eck_naomi_m4_morning

