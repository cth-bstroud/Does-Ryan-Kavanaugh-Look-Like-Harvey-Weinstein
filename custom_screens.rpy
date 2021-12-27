screen statsUI:
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        right_padding 10
        left_padding 10
        text ("Score: %d" % score)
        

label call_mapUI:
    call screen MapUI

screen MapUI:
    add im.Scale("images/imagemap.jpg", 1920, 1080)
    if visitFarm == False:
        imagebutton:
            xpos 618
            ypos 570
            idle "images/F.png"
            hover im.Scale("images/F.png", 150, 150)
            action Jump("farm")
    if visitJungle == False:
        imagebutton:
            xpos 233
            ypos 420
            idle "images/J.png"
            hover im.Scale("images/J.png", 150, 150)
            action Jump("jungle")
    if visitWiki == False:
        imagebutton:
            xpos 1000
            ypos 140
            idle "images/w.png"
            hover im.Scale("images/W.png", 150, 150)
            action Jump("Wikipedia")

    if (visitWiki == True) and (visitJungle == True ) and (visitFarm == True):
        $first_three = True
    
    if first_three == True:
        imagebutton:
            xalign 0.5
            yalign 0.5
            idle "images/mb.png"
            hover im.Scale("images/mb.png", 150, 150)
            action Jump("basement")

screen boss_health:
    bar value StaticValue(bossHealth, 100):
        xalign 0.5 yalign 0.4
        xmaximum 700 
        ymaximum 15
        left_bar Frame("gui/bar/right.png", 10, 0) 
        right_bar Frame("gui/bar/left.png", 10, 0)
        #thumb "gui/window_icon.png" 
        thumb_shadow None

screen player_health:
    text 'HP' xalign 0.33 yalign 0.61
    bar value StaticValue(your_health, 100):
        xalign 0.5 yalign 0.7
        xmaximum 700 
        ymaximum 15
        left_bar Frame("gui/bar/right.png", 10, 0) 
        right_bar Frame("gui/bar/left.png", 10, 0)
        #thumb "gui/window_icon.png" 
        thumb_shadow None

screen hkrw_boss_head:
    bar value StaticValue(hk_rw_value, 100):
        xalign 0.5 yalign 0.0
        xmaximum 279
        ymaximum 386
        left_bar Frame('images/rkhead.png', 10, 0)
        right_bar Frame('images/hwhead.png', 10, 0)
        thumb_shadow None
        

screen wallet:
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 90
        right_padding 10
        left_padding 10
        text ("$%d" % your_wallet)

transform movedown:
    linear 0.9 ypos 1.0

transform flipped:
    subpixel True
    xalign 0.5
    ypos (-175)
    linear 5 rotate 180
    

screen lawsuitCount:
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 150
        right_padding 10
        left_padding 10
        text ("Number of lawsuits against you: %d" % lawsuit_count)

screen lawyerCount:
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 210
        right_padding 10
        left_padding 10
        text ("Lawyers on your side: %d" % lawyer_count)

            