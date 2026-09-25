screen options():
    key "w" action Preference("display", "window")
    key "f" action Preference("display", "fullscreen")

screen timer:
    timer 0.05 repeat True action If(time > 0, true=SetVariable('time', time - 0.05), false=[Hide('timer'), Jump(timejump)])

screen title:

    imagemap:
        ground "images/title/pointtitle ground.png"
        hover "images/title/pointtitle hover.png"
        hotspot (0,0,2000,2000) action Jump("development") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

label points:

    screen trailer:

        imagemap:
            xpos 650 ypos 380
            ground "images/point ground.png"
            hover "images/point hover.png"
            hotspot (0,0,2000,2000) action Jump("pointtrailer") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        imagemap:
            xpos 1280 ypos 200
            ground "images/point ground.png"
            hover "images/point hover.png"
            hotspot (0,0,2000,2000) action Jump("pointtrailer") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        imagemap:
            xpos 1100 ypos 600
            ground "images/point ground.png"
            hover "images/point hover.png"
            hotspot (0,0,2000,2000) action Jump("pointtrailer") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    screen hallpoint:

        if pointa == 0:
            imagemap:
                xpos 930 ypos 610
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointrobes") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointb == 0:
            imagemap:
                xpos 820 ypos 535
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointlimbs") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointc == 0:
            imagemap:
                xpos 935 ypos 265
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointhead") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointd == 0:
            imagemap:
                xpos 980 ypos 320
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointtear") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointe == 0:
            imagemap:
                xpos 280 ypos 430
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointeyes") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointf == 0:
            imagemap:
                xpos 930 ypos 135
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointmural") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointg == 0:
            imagemap:
                xpos 520 ypos 310
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointcell") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointh == 0:
            imagemap:
                xpos 1315 ypos 410
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointnature") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointi == 0:
            imagemap:
                xpos 1547 ypos 325
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointcharm") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointx == 0:
            imagemap:
                xpos 1691 ypos 581
                ground "images/scrawl ground.png"
                hover "images/scrawl hover.png"
                hotspot (0,0,2000,2000) action Jump("hallscrawl") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    screen infirmarypoint:

        if pointa == 0:
            imagemap:
                xpos 1550 ypos 280
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointnurse") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointb == 0:
            imagemap:
                xpos 978 ypos 95
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointcamera") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointc == 0:
            imagemap:
                xpos 510 ypos 490
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointbones") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointd == 0:
            imagemap:
                xpos 110 ypos 240
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointcurtain") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointe == 0:
            imagemap:
                xpos 450 ypos 190
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointexam") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointx == 0:
            imagemap:
                xpos 934 ypos 113
                ground "images/scrawl ground.png"
                hover "images/scrawl hover.png"
                hotspot (0,0,2000,2000) action Jump("infirmaryscrawl") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    screen wardrobepoint:

        if pointa == 0:
            imagemap:
                xpos 320 ypos 230
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointragfoole") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointb == 0:
            imagemap:
                xpos 530 ypos 560
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointragdoctor") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointc == 0:
            imagemap:
                xpos 780 ypos 490
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointragwarrior") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointd == 0:
            imagemap:
                xpos 920 ypos 410
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointragbeggar") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointe == 0:
            imagemap:
                xpos 1085 ypos 235
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointragstudent") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointf == 0:
            imagemap:
                xpos 1360 ypos 520
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointragsaege") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointg == 0:
            imagemap:
                xpos 1540 ypos 220
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointragkeeper") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointx == 0:
            imagemap:
                xpos 1683 ypos 347
                ground "images/scrawl ground.png"
                hover "images/scrawl hover.png"
                hotspot (0,0,2000,2000) action Jump("wardrobescrawl") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointx == 0:
            imagemap:
                xpos 195 ypos 347
                ground "images/scrawl ground.png"
                hover "images/scrawl hover.png"
                hotspot (0,0,2000,2000) action Jump("wardrobescrawl") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    screen wearpoint:
        
        imagemap:
            xpos 320 ypos 230
            ground "images/point ground.png"
            hover "images/point hover.png"
            hotspot (0,0,2000,2000) action Jump("wearfoole") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        imagemap:
            xpos 530 ypos 560
            ground "images/point ground.png"
            hover "images/point hover.png"
            hotspot (0,0,2000,2000) action Jump("weardoctor") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        imagemap:
            xpos 780 ypos 490
            ground "images/point ground.png"
            hover "images/point hover.png"
            hotspot (0,0,2000,2000) action Jump("wearnoble") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        imagemap:
            xpos 920 ypos 410
            ground "images/point ground.png"
            hover "images/point hover.png"
            hotspot (0,0,2000,2000) action Jump("wearbeggar") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        imagemap:
            xpos 1085 ypos 235
            ground "images/point ground.png"
            hover "images/point hover.png"
            hotspot (0,0,2000,2000) action Jump("wearstudent") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        imagemap:
            xpos 1360 ypos 520
            ground "images/point ground.png"
            hover "images/point hover.png"
            hotspot (0,0,2000,2000) action Jump("wearsaege") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        imagemap:
            xpos 1540 ypos 220
            ground "images/point ground.png"
            hover "images/point hover.png"
            hotspot (0,0,2000,2000) action Jump("wearkeeper") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointx == 0:
            imagemap:
                xpos 1683 ypos 347
                ground "images/scrawl ground.png"
                hover "images/scrawl hover.png"
                hotspot (0,0,2000,2000) action Jump("wardrobescrawl") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointx == 0:
            imagemap:
                xpos 195 ypos 347
                ground "images/scrawl ground.png"
                hover "images/scrawl hover.png"
                hotspot (0,0,2000,2000) action Jump("wardrobescrawl") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    screen gallerypoint:

        if pointa == 0:
            imagemap:
                xpos 660 ypos 275
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointstar") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointb == 0:
            imagemap:
                xpos 800 ypos 405
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointmachine") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointc == 0:
            imagemap:
                xpos 955 ypos 270
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointbeast") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointd == 0:
            imagemap:
                xpos 1070 ypos 405
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointslime") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointe == 0:
            imagemap:
                xpos 1170 ypos 230
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointbug") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointf == 0:
            imagemap:
                xpos 1330 ypos 380
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointdivine") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointg == 0:
            imagemap:
                xpos 1540 ypos 280
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointshadow") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointx == 0:
            imagemap:
                xpos 1572 ypos 508
                ground "images/scrawl ground.png"
                hover "images/scrawl hover.png"
                hotspot (0,0,2000,2000) action Jump("galleryscrawl") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    screen favoritepoint:

        imagemap:
            ground "images/gallery/pointstar ground.png"
            hover "images/gallery/pointstar hover.png"
            hotspot (0,0,2000,2000) action Jump("galleryend") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        imagemap:
            ground "images/gallery/pointmachine ground.png"
            hover "images/gallery/pointmachine hover.png"
            hotspot (0,0,2000,2000) action Jump("galleryend") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        imagemap:
            ground "images/gallery/pointbeast ground.png"
            hover "images/gallery/pointbeast hover.png"
            hotspot (0,0,2000,2000) action Jump("galleryend") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        imagemap:
            ground "images/gallery/pointslime ground.png"
            hover "images/gallery/pointslime hover.png"
            hotspot (0,0,2000,2000) action Jump("galleryend") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        imagemap:
            ground "images/gallery/pointbug ground.png"
            hover "images/gallery/pointbug hover.png"
            hotspot (0,0,2000,2000) action Jump("galleryend") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        imagemap:
            ground "images/gallery/pointdivine ground.png"
            hover "images/gallery/pointdivine hover.png"
            hotspot (0,0,2000,2000) action Jump("galleryend") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        imagemap:
            ground "images/gallery/pointshadow ground.png"
            hover "images/gallery/pointshadow hover.png"
            hotspot (0,0,2000,2000) action Jump("galleryend") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointx == 0:
            imagemap:
                ground "images/empty.png"
                hover "images/gallery/scrawl.png"
                hotspot (0,0,2000,2000) action Jump("gallleryend") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    screen vaultpoint:

        if pointa == 0:
            imagemap:
                xpos 1130 ypos 490
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointcorpse") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointb == 0:
            imagemap:
                xpos 670 ypos 290
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointspider") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointc == 0:
            imagemap:
                xpos 1390 ypos 100
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointeyez") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointd == 0:
            imagemap:
                xpos 1640 ypos 275
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointlightbulb") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"
                
        if pointx == 0:
            imagemap:
                xpos 1586 ypos 316
                ground "images/scrawl ground.png"
                hover "images/scrawl hover.png"
                hotspot (0,0,2000,2000) action Jump("thoughtwarden") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    screen bathpoint:

        if pointa == 0:
            imagemap:
                xpos 1490 ypos 100
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointjelly") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointb == 0:
            imagemap:
                xpos 1015 ypos 555
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointwater") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointc == 0:
            imagemap:
                xpos 607 ypos 250
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointwaterfalls") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointd == 0:
            imagemap:
                xpos 1590 ypos 490
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointbubbles") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointx == 0:
            imagemap:
                xpos 1404 ypos 578
                ground "images/scrawl ground.png"
                hover "images/scrawl hover.png"
                hotspot (0,0,2000,2000) action Jump("bathscrawl") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    screen theaterpoint:

        if pointa == 0:
            imagemap:
                xpos 390 ypos 550
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointfoolemask") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointb == 0:
            imagemap:
                xpos 150 ypos 45
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointfrytes") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointc == 0:
            imagemap:
                xpos 1235 ypos 610
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointaudience") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointd == 0:
            imagemap:
                xpos 940 ypos 480
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointexit") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointx == 0:
            imagemap:
                xpos 1641 ypos 321
                ground "images/scrawl ground.png"
                hover "images/scrawl hover.png"
                hotspot (0,0,2000,2000) action Jump("theaterscrawl") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    screen cathedralpoint:

        if pointa == 0:
            imagemap:
                xpos 935 ypos 600
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointstained") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointb == 0:
            imagemap:
                xpos 1235 ypos 520
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointshards") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointc == 0:
            imagemap:
                xpos 525 ypos 230
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointcandles") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointd == 0:
            imagemap:
                xpos 935 ypos 10
                ground "images/point ground.png"
                hover "images/point hover.png"
                hotspot (0,0,2000,2000) action Jump("pointglasseyefoole") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

        if pointx == 0:
            imagemap:
                xpos 383 ypos 166
                ground "images/scrawl ground.png"
                hover "images/scrawl hover.png"
                hotspot (0,0,2000,2000) action Jump("cathedralscrawl") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

screen conmenu:

    if conhand == 0:
        imagemap:
            ground "images/empty.png"
            hover "images/terrace/conhand h.png"
            hotspot (0,0,2000,2000) action Jump("conhand") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    if concane == 0:
        imagemap:
            ground "images/empty.png"
            hover "images/terrace/concane h.png"
            hotspot (0,0,2000,2000) action Jump("concane") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    if conhill == 0:
        imagemap:
            ground "images/empty.png"
            hover "images/terrace/conhill h.png"
            hotspot (0,0,2000,2000) action Jump("conhill") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    if conline == 0:
        imagemap:
            ground "images/empty.png"
            hover "images/terrace/conline h.png"
            hotspot (0,0,2000,2000) action Jump("conline") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    if constar == 0:
        imagemap:
            ground "images/empty.png"
            hover "images/terrace/constar h.png"
            hotspot (0,0,2000,2000) action Jump("constar") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    if conflower == 0:
        imagemap:
            ground "images/empty.png"
            hover "images/terrace/conflower h.png"
            hotspot (0,0,2000,2000) action Jump("conflower") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    if conhat == 0:
        imagemap:
            ground "images/empty.png"
            hover "images/terrace/conhat h.png"
            hotspot (0,0,2000,2000) action Jump("conhat") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    if conhouse == 0:
        imagemap:
            ground "images/empty.png"
            hover "images/terrace/conhouse h.png"
            hotspot (0,0,2000,2000) action Jump("conhouse") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    if congun == 0:
        imagemap:
            ground "images/empty.png"
            hover "images/terrace/congun h.png"
            hotspot (0,0,2000,2000) action Jump("congun") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    if conhour == 0:
        imagemap:
            ground "images/empty.png"
            hover "images/terrace/conhour h.png"
            hotspot (0,0,2000,2000) action Jump("conhour") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"

    if pointx == 0:
        imagemap:
            xpos 104 ypos 100
            ground "images/scrawl ground.png"
            hover "images/scrawl hover.png"
            hotspot (0,0,2000,2000) action Jump("terracescrawl") hover_sound "choice_hover.mp3" activate_sound "choice_click.mp3"