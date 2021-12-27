define r = Character('Ryan Kavanugh', color="#c8ffc8")
define h = Character('Harvey', color='#fff000')
define m = Character('Me', color="#c8c8ff")
define s = Character('Suit', color='#c9c9ee')
define n = Character('Narrator', color='#fee0d3')
define f = Character('Farmer', color='#aaa03f')
define l = Character('Leemstar', color='#f45a00')
define lawyer = Character('Lawyer', color='#25f301')
define rwhk = Character('Ryan Weinstein Harvey Kavanugh', color='#69420f')

image ryan happy = 'images/Ryan-Kavanugh-Microphone-187x300.png'
image harvey happy = 'images/cropped-does-ryan-kavanaugh-look-like-harvey-weinstein-LOGO-192x192.png'
image suit = 'images/suit2.png'

image harvey photo = 'images/hw1photo.png'
image farmer normal = 'images/farmer.png'
image gnome leemstar = 'images/gnomefix.png'
image harvey boss = 'images/rkboss.png'

image item lawsuit = im.FactorScale("images/lawsuittxt.png", .75)
image item article = im.FactorScale("images/rk_article.png", .75)

image bg city = ('images/city.jpg')
image bg farm = ('images/farm.jpg')
image bg jungle = im.Scale('images/monkey.jpg', 1920, 1080)
image bg wikipedia = im.Scale('images/wikipedia.png', 1920, 1080)
image bg basement = im.Scale('images/basement.jpg', 1920, 1080)
image bg hollywood = im.Scale('images/bbhollywood.jpg', 1920, 1080)
image bg gameover = 'images/gameover.png'
image bg gamewin = im.Scale('images/medow.jpeg', 1920, 1080)

default book = False

label start:
    play music "audio/alex preston - windy wendy.webm"
    queue music 'audio/grvsh - 808windy fartbeat.webm'
    queue music 'audio/just - windy williams.webm'
    queue music 'audio/tom hale - windy.webm'


    n "Are you ready to find out if Ryan Kavanaugh looks like Harvey Weinstein?"
    
    menu:
        'Yes':
            pass
        'No':
            n 'Goodbye. '
            return

    scene bg city with fade
    show screen statsUI

    show suit at right
    with dissolve

    #show ryan happy at center
    #with dissolve

    show harvey photo at truecenter with dissolve

    init python:
        score = 0
        visitWiki = False
        visitJungle = False
        visitFarm = False
        growing = False
        first_three = False
        battlePhase = False
        drkllhw = False
        battlePhase = True
        bossHealth = 100
        your_health = 100
        your_wallet = 20
        player_dmg = 1
        lawyer_charge = 0
        lawyer_count = 0
        asshole = False
        lawsuit_count = 0
        boss_dmg = 10

    menu:
        s 'Have you seen this man?'

        "Yeah, that's Harvey Weinstein":
            jump first_choice_harvey

        "Yeah, that's Ryan Kavanaugh":
            jump first_choice_ryan

label first_choice_ryan:
    play sound 'audio/wrong.webm'
    with hpunch
    $score -= 1

    n 'Sorry but that was Ryan Kavanaugh.'
    
    menu:
        n 'Where should we look for Ryan Kavanaugh next?'

        'Jungle':
            jump jungle
        
        'Farm':
            jump farm
        
        'Wikipedia':
            jump Wikipedia

label first_choice_harvey:
    play sound 'audio/correct.webm'
    $score += 1
    $drkllhw = True
    menu:
        n "You're right! But we need to find Ryan Kavanaugh. Where to next?"
        'Jungle':
            jump jungle
        
        'Farm':
            jump farm
        
        'Wikipedia':
            jump Wikipedia


label farm:
    $visitFarm = True
    scene bg farm with fade
   
    show farmer normal at left with dissolve
    f 'Welcome to my farm.'

    menu:
        'What do you grow here?':
            pass
            $ growing = True
        'Have you seen this man? {i}You show the farmer an image.{/i}':
            pass
            
    if growing:
        f "Weed. Why are you a cop? Because legally you have to tell me if you're a cop."
        n 'Maybe we should just ask about Ryan Kavanaugh.'
        menu:
            'Have you seen this man? {i}You show the farmer an image.{/i}':
                pass

    show harvey photo at truecenter with dissolve
    f 'Yeah thats Ryan Kavanaugh'

    if first_three:
        f "Did you check Mom's Basement?"
        f 'See ya around'
        jump call_mapUI
    else:
        f "He's not here. But you should get going and check else where."
        jump call_mapUI
   

label jungle:
    $visitJungle = True
    scene bg jungle with fade
    n "Oh shit it's a monkey!"
    n "Well technically we won't find Ryan Kavanaugh in a jungle full of monkeys."
    n "Let's see if we unlocked any new locations."

    jump call_mapUI

label Wikipedia:
    $visitWiki = True
    scene bg wikipedia with fade
    n "Uh-oh what's this?"
    n "Oh no we shouldn't be here."
    n "Trust me you won't find RK777713 here. "

    #show screen MapUI
    jump call_mapUI

label basement:
    scene bg basement with fade
    show gnome leemstar at truecenter
    
    l "I know why you're here. "
    l "You're on {i}The Quest To Find Out If Ryan Kavanaugh Looks Like Harvey Weinstein.{/i}"
    l "But I'm not gonna help you!"
    l "Ryan Kavanaugh is by best friend and he looks nothing like Harvey Weinstein."
    l "LEAVE BEFORE I CALL SUSAN!!!"
    play sound 'audio/sof.mp3' 

    with Pause(2)
    jump after_4_places

label after_4_places:
    scene bg city
    n "Man, we've been all over the place. I'm not sure where we should go next."
    n "How are we ever going to find out does Ryan Kavanaugh look like Harvey Weinstein?"
    n "I have an idea. What if we started a poll?"
    n "No we can't do that this is a single player game. Also, I don't wanna get sued for a public poll."
    n "How about turning this game into the game found on drkllhw.com?"
    n "No, you're right that would be lame."
    n 'I have a great idea.'
    n 'How about a boss battle with poorly edited images of Ryan Kavanaugh?'

    menu:
        'Yes':
            jump boss_battle
        "Hell yes!":
            jump boss_battle

label boss_battle:
    n 'Yo check out this sick boss battle.'

    scene bg hollywood with irisin
    show harvey boss at top
    
    

    r "So you've finally found me. Looks like you little quest is over."
    r "Maybe we should end this little dance of yours."
    r "Ha take this!"

    
    show screen boss_health
    show screen wallet
    show screen player_health
    show screen lawyerCount
    show screen lawsuitCount
    

    while bossHealth > 0:

        show item lawsuit:
            yalign 0.0
            xalign 0.5
            movedown

        python:
            dmg_calc = boss_dmg + (lawsuit_count * 5)
            your_health -= dmg_calc
        #$dmg_calc = boss_dmg + (lawsuit_count * 5)
        #$your_health -= dmg_calc
        $your_wallet -= 1000000
        $lawsuit_count += 1
        with hpunch
        if your_health < 0:
            jump game_over


        r "What are you gonna do now?"
        menu:
            'Attack':
                $bossHealth -= player_dmg
                if bossHealth < 0:
                    jump boss_battle2
                r "HAHA you think that puny little attack can hurt me?!"
            'Lawyer up!':
                $player_dmg += 5
                $your_health += 10
                $your_wallet -= 500000
                $lawyer_charge += 20
                $lawyer_count += 1

                lawyer "I shall add my power to yours but it'll cost ya."
                n "You've gained +5 attack and restored 10hp."
            'Block':
                n 'How are you gonna block a lawsuit?'
            'Flee':
                n "You can't run from the law."

        r "You're ugly."

        n 'Emotional damage! It crits for 3x damage!'

        menu:
            'Ouch':
                $your_health -= 30
                if your_health < 0:
                    jump game_over
            'Why do I care what some elite Hollywood asshole thinks of me?':
                $asshole = True
                n "Good point no damage taken"

        if asshole == True:
            r "I'm not an asshole! That's defamation!"
            r 'Here take this!'
            show item lawsuit:
                yalign 0.0
                xalign 0.5
                movedown

            python:
                dmg_calc = boss_dmg + (lawsuit_count * 5)
                your_health -= dmg_calc
            #$dmg_calc = boss_dmg + (lawsuit_count * 5)
            #$your_health -= dmg_calc
            $your_wallet -= 1000000
            $lawsuit_count += 1
            with hpunch
            if your_health < 0:
                jump game_over
        
        if drkllhw == True:
            r "That is defamation! I look nothing like Harvey Weinstein "
            r 'Here take this!'
            #$lawsuitCount += 1
            show item lawsuit:
                yalign 0.0
                xalign 0.5
                movedown

            $your_health -= 10
            $your_wallet -= 1000000
            $lawsuit_count += 1
            with hpunch
            if your_health < 0:
                jump game_over
        
        menu:
            'Attack':
                $bossHealth -= player_dmg
                if bossHealth < 0:
                    jump boss_battle2
                r "HAHA you think that puny little attack can hurt me?!"
            'Lawyer up!':
                $player_dmg += 5
                $your_health += 10
                $your_wallet -= 500000
                $lawyer_charge += 20
                $lawyer_count += 1

                lawyer "I shall add my power to yours but it'll cost ya."
                n "You've gained +5 attack and restored 10hp."
            'Block':
                n 'How are you gonna block a lawsuit?'
            'Flee':
                n "You can't run from the law."

        r "Wikipedia says I'm the 27th best producer in Hollywood!"
        $your_health -= 20
        with hpunch
        if your_health < 0:
            jump game_over
        r "I also single handedly started the MCU!"
        $your_health -= 10
        with hpunch
        if your_health < 0:
            jump game_over

        menu:
            'According to whom, your mom?':
                $bossHealth -= 50
            "Editing your Wikipedia articles doesn't make it true.":
                $bossHealth -= 20
            "Yeah but you still look like Harvey Weinstein":
                $bossHealth -= 100


        if your_health < 0:
            jump game_over
    
        if bossHealth < 0:
            jump boss_battle2


label boss_battle2:
    hide screen wallet
    hide screen player_health
    hide screen lawyerCount
    hide screen lawsuitCount
    hide screen boss_health

    $boss_def = 10
    $bossHealth = 100
    $score += 1
    scene bg hollywood
    
    n 'Good job kid you got him.'


    show harvey boss with dissolve:
        xalign 0.5
        yalign 0.0
        flipped
        

    n "Wait, why is he back?"
    r "You may have defeated my first form. But you're not matched for my FLIPPED FORM! AHAHAHAHAHAH"

    hide screen wallet
    hide screen player_health
    hide screen lawyerCount
    hide screen lawsuitCount
    hide screen boss_health

    
    r 'Prepare for you will never finish {i}The Quest To Find Out If Ryan Kavanaugh Looks Like Harvey Weinstein.{/i}'
    show screen wallet
    show screen player_health
    show screen lawyerCount
    show screen lawsuitCount
    show screen boss_health
    with Pause(2)

    while bossHealth > 0 or your_health > 0:
        r '!siht ekat ereH'
        show item article:
                yalign 0.0
                xalign 0.5
                movedown
        python:
            dmg_calc = boss_dmg + (lawsuit_count * 2)
            your_health -= dmg_calc
            bossHealth -= 10

        $your_wallet -= 1000000
        $lawsuit_count += 1
            
        with hpunch
        if your_health < 0:
            jump game_over
        
        n 'Wait why did he take damage? Could it be because only an insane person would write an article like that? What are you going to do now?'
        menu:
            'Attack':
                $bossHealth -= (player_dmg - boss_def)
                if bossHealth < 0:
                    jump boss_battle3
                r "HAHA you think that puny little attack can hurt me?!"
            'Lawyer up!':
                $player_dmg += 5
                $your_health += 20
                $your_wallet -= 500000
                $lawyer_charge += 20
                $lawyer_count += 1

                lawyer "I shall add my power to yours but it'll cost ya."
                n "You've gained +5 attack and restored 10hp."
            'Block':
                n 'How are you gonna block a lawsuit?'
            'Flee':
                n "You can't run from the law."
            'Lawyer Blast' if lawyer_charge >= 100:
                $bossHealth = 0
                $your_health = 100
                $your_wallet += 694200000000
                r '?!?SREYWAL YNAM OS TEG UOY DID WOH ON'
                r  '!DETAEFED EB TON LLIW I'
                jump boss_battle3

        r '.ekaf era selcitra esohT ?em tuoba eil uoy tsum yhW'
        r '!nem gnoma dog a ma I'

        menu:
            'Talking to you is so frustrating. Ugh your shit is flipped.':
                $bossHealth -= 50
            'What?':
                $bossHealth -= 20
            'Why are you writing fake articles?':
                $bossHealth += 20
        r 'EM OT KAEPS UOY ERAD WOH'

        if your_health < 0:
            jump game_over
        if bossHealth < 0:
            jump boss_battle3

label boss_battle3:
    r "!detaefed eb ton lliw I !!!oN"
    $score += 1

    hide screen wallet
    hide screen player_health
    hide screen lawyerCount
    hide screen lawsuitCount
    hide screen boss_health
    hide harvey boss with fade

    $bossHealth = 100
    $your_health = 100
    
    n 'We did it.'
    n "Wait why isn't the game over?"
    n "Oh no."
    n "It's phase 3"

    $hk_rw_value = 50

    show screen hkrw_boss_head with dissolve
    rwhk 'BEHOLD IT IS I, GOD!'

    show screen wallet
    show screen player_health
    show screen lawyerCount
    show screen lawsuitCount
    show screen boss_health
    
    menu:
        "How do I go to a different Universe where you're not god":
            rwhk 'By dying!'

        "Wait you look the same. I'm confused?":
            rwhk 'WE ARE NOT THE SAME!'

        "I mean you're pretty washed up. Can you even do anything relevant?":
            rwhk 'Yeah take this!'
            show item article:
                yalign 0.0
                xalign 0.5
                movedown
            $your_wallet -= 1000000
            $lawsuit_count += 1
            with hpunch
            if your_health < 0:
                jump game_over

        "Do you still have the weird thing in your pants or....?":
            rwhk 'DEFAMATION!'
            show item article:
                yalign 0.0
                xalign 0.5
                movedown
            $your_wallet -= 1000000
            $lawsuit_count += 1
            with hpunch
            if your_health < 0:
                jump game_over
    
    rwhk "It looks like you've made it this far. I guess you've completed {i}The Quest To Find Out If Ryan Kavanaugh Looks Like Harvey Weinstein.{/i}"
    $hk_rw_value = 90
    rwhk "I should congratulate you on making it this far. "
    $hk_rw_value = 70
    rwhk "But you're nothing and I won't waste my breath."
    $hk_rw_value = 99
    rwhk "I'm taking off the kid gloves now. No longer will I hit you with petty lawsuits that I have no way of possibly winning."
    $hk_rw_value = 44
    rwhk "You shall face the wrath of my pimp hand and petty insults. Prepare thyself!"
    $hk_rw_value = 23

    $tutorial = False
    $boss_def = 50

    while your_health > 0 or boss_health > 0 or lawyer_count < 7:
        rwhk 'Pimp Slap!'
        $your_health -= 40
        with hpunch
        $hk_rw_value = 75
        if your_health < 1:
            jump game_over

        if not tutorial:
            n 'Hold on buddy some things have changed this time around.'
            n 'Now you can heal. It is based on the amount of lawyers you have.'
            n 'Your attack attack option is also based on the number of lawyers you have plus your lawyer charge.'
            n 'Good luck kiddo.'
            $tutorial = True
        
        menu:
            'Heal':
                $your_health += (lawyer_charge + lawyer_count)
            'Attack':
                $bossHealth -= ((player_dmg + lawyer_charge + lawyer_count) - boss_def)
                if bossHealth < 1:
                    jump game_win
            'Lawyer Up':
                $player_dmg += 5
                $your_health += 20
                $your_wallet -= 500000
                $lawyer_charge += 20
                $lawyer_count += 1

                lawyer "I shall add my power to yours but it'll cost ya."
                n "You've gained +5 attack and restored 10hp."

            'Lawyer Blast' if lawyer_charge >= 100:
                $bossHealth = 0
                jump game_win
                

        rwhk "You're ugly!"
        $hk_rw_value = 25
        $your_health -= 50
        with vpunch
        if your_health < 1:
            jump game_over

        menu:
            'Heal':
                $your_health += (lawyer_charge + lawyer_count)
            'Attack':
                $bossHealth -= ((player_dmg + lawyer_charge + lawyer_count) - boss_def)
            'Lawyer Up':
                $player_dmg += 5
                $your_health += 20
                $your_wallet -= 500000
                $lawyer_charge += 20
                $lawyer_count += 1

                lawyer "I shall add my power to yours but it'll cost ya."
                n "You've gained +5 attack and restored 10hp."

            'Lawyer Blast' if lawyer_charge >= 100:
                $bossHealth = 0
                jump game_win



label game_win:
    $score += 1
    rwhk 'No how could this be?'
    rwhk 'Defeated by some nobody?'

    hide screen wallet
    hide screen player_health
    hide screen lawyerCount
    hide screen lawsuitCount
    hide screen boss_health
    hide screen hkrw_boss_head with dissolve

    scene bg gamewin with fade
    n 'nice'
    n 'You did it.'
    n 'The world is free from Ryan Kavanaugh and Harvey Weinstein.'
    n 'Well until they get millions of dollars again an start more frivolous lawsuits.'
    n 'But who knows how long that will take?'

    if score >= 4:
        n 'Oh hey you got the best score in the game.'
        n 'Congratulations'
    if score <= 3:
        n "You didn't get the best score but maybe you could try again?"
        n 'Congratulations on beating the game.'

    return

    


label game_over:
    scene bg gameover
    $your_wallet = 0
    $score = 0
    $lawyer_charge = 0
    $lawyer_count = 0
    n "no no no no you can't die we still don't know if Ryan Kavanaugh looks like Harvey Weinstein"
    return