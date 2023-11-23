
init:

    $ sqbnaomilewd = 0
    $ sqbpremounlocked = False
    $ sqbnaomim1flirted = False
    $ sqbnaomi2hadsex = False
    $ sqbnaomim3nogiveup = False
    $ sqbnaomim3entrchkblk = False
    $ sqbnaomim3protect = False
    $ sqbnaomim4hadsex = False
    
    image sqbnaomiapt04 = "bg/sqbnaomiapt04.png"
    image sqbcreditsnm = "cg/sqbcreditsnm.png"
    image sqbendings = "cg/sqbendingsnm.png"
    image rezalayingdown = "cg/rezalayingdown.png"
    image eckoldbiolabsep = im.Sepia("bg/eckoldbiolab.jpg")
    image ecknaomiapt01sep = im.Sepia("bg/ecknaomiapt01.jpg")
    image naomi cry sep = im.Sepia("cr/naomi_cry.png")
    image naomi scared sep = im.Sepia("cr/naomi_scared.png")
    image naomi hurt sep = im.Sepia("cr/naomi_hurt.png")
    image naomi aroused = "cr/naomi_aroused.png"
    image naomi aroused flip = im.Flip("cr/naomi_aroused.png", horizontal=True)
    image side naomi aroused = im.Flip(im.Scale(im.Crop("cr/naomi_aroused.png",(70,80,500,600)),250,300),horizontal=True)
    image naomi cums = "cr/naomi_cums.png"
    image naomi cums flip = im.Flip("cr/naomi_cums.png", horizontal=True)
    image side naomi cums = im.Flip(im.Scale(im.Crop("cr/naomi_cums.png",(70,80,500,600)),250,300),horizontal=True)
    
#Doppelganger
    define Nm1 = Character(_("Naomi 1"), color="#64b9b9", image="naomi")
    define Nm2 = Character(_("Naomi 2"), color="#64b9b9", image="naomi2")
    define Nmb = Character(_("Both Naomis"), color="#64b9b9", image="naomi2")
    image naomi2 normal = "cr/naomi_normal.png"
    image naomi2 normal flip = im.Flip("cr/naomi_normal.png", horizontal=True)
    image naomi2 normal b = "cr/naomi_normal_b.png"
    image naomi2 normal b flip = im.Flip("cr/naomi_normal_b.png", horizontal=True)
    image naomi2 normal d = "cr/naomi_normal_d.png"
    image naomi2 normal d flip = im.Flip("cr/naomi_normal_d.png", horizontal=True)
    image naomi2 angry = "cr/naomi_angry.png"
    image naomi2 angry flip = im.Flip("cr/naomi_angry.png", horizontal=True)
    image naomi2 angry b = "cr/naomi_angry_b.png"
    image naomi2 angry b flip = im.Flip("cr/naomi_angry_b.png", horizontal=True)
    image naomi2 angry c = "cr/naomi_angry_c.png"
    image naomi2 angry c flip = im.Flip("cr/naomi_angry_c.png", horizontal=True)
    image naomi2 annoyed = "cr/naomi_annoyed.png"
    image naomi2 annoyed flip = im.Flip("cr/naomi_annoyed.png", horizontal=True)
    image naomi2 annoyed b = "cr/naomi_annoyed_b.png"
    image naomi2 annoyed b flip = im.Flip("cr/naomi_annoyed_b.png", horizontal=True)
    image naomi2 bacon = "cr/naomi_bacon.png"
    image naomi2 bacon flip = im.Flip("cr/naomi_bacon.png", horizontal=True)
    image naomi2 blank = "cr/naomi_blank.png"
    image naomi2 blank flip = im.Flip("cr/naomi_blank.png", horizontal=True)
    image naomi2 blank b = "cr/naomi_blank_b.png"
    image naomi2 blank b flip = im.Flip("cr/naomi_blank_b.png", horizontal=True)
    image naomi2 blank d = "cr/naomi_blank_d.png"
    image naomi2 blank d flip = im.Flip("cr/naomi_blank_d.png", horizontal=True)
    image naomi2 cry = "cr/naomi_cry.png"
    image naomi2 cry flip = im.Flip("cr/naomi_cry.png", horizontal=True)
    image naomi2 cry b = "cr/naomi_cry_b.png"
    image naomi2 cry b flip = im.Flip("cr/naomi_cry_b.png", horizontal=True)
    image naomi2 cry d = "cr/naomi_cry_d.png"
    image naomi2 cry d flip = im.Flip("cr/naomi_cry_d.png", horizontal=True)
    image naomi2 crysmile = "cr/naomi_crysmile.png"
    image naomi2 crysmile flip = im.Flip("cr/naomi_crysmile.png", horizontal=True)
    image naomi2 crysmile b = "cr/naomi_crysmile_b.png"
    image naomi2 crysmile b flip = im.Flip("cr/naomi_crysmile_b.png", horizontal=True)
    image naomi2 concern = "cr/naomi_concern.png"
    image naomi2 concern flip = im.Flip("cr/naomi_concern.png", horizontal=True)
    image naomi2 concern b = "cr/naomi_concern_b.png"
    image naomi2 concern b flip = im.Flip("cr/naomi_concern_b.png", horizontal=True)
    image naomi2 concern d = "cr/naomi_concern_d.png"
    image naomi2 concern d flip = im.Flip("cr/naomi_concern_d.png", horizontal=True)
    image naomi2 confused = "cr/naomi_confused.png"
    image naomi2 confused flip = im.Flip("cr/naomi_confused.png", horizontal=True)
    image naomi2 confused b = "cr/naomi_confused_b.png"
    image naomi2 confused b flip = im.Flip("cr/naomi_confused_b.png", horizontal=True)
    image naomi2 confused d = "cr/naomi_confused_d.png"
    image naomi2 confused d flip = im.Flip("cr/naomi_confused_d.png", horizontal=True)
    image naomi2 hurt = "cr/naomi_hurt.png"
    image naomi2 hurt flip = im.Flip("cr/naomi_hurt.png", horizontal=True)
    image naomi2 hurt b = "cr/naomi_hurt_b.png"
    image naomi2 hurt b flip = im.Flip("cr/naomi_hurt_b.png", horizontal=True)
    image naomi2 hurt d = "cr/naomi_hurt_d.png"
    image naomi2 hurt d flip = im.Flip("cr/naomi_hurt_d.png", horizontal=True)
    image naomi2 sad = "cr/naomi_sad.png"
    image naomi2 sad flip = im.Flip("cr/naomi_sad.png", horizontal=True)
    image naomi2 sad b = "cr/naomi_sad_b.png"
    image naomi2 sad b flip = im.Flip("cr/naomi_sad_b.png", horizontal=True)
    image naomi2 sleep = "cr/naomi_sleep.png"
    image naomi2 sleep flip = im.Flip("cr/naomi_sleep.png", horizontal=True)
    image naomi2 sleep b = "cr/naomi_sleep_b.png"
    image naomi2 sleep b flip = im.Flip("cr/naomi_sleep_b.png", horizontal=True)
    image naomi2 slsmile = "cr/naomi_slsmile.png"
    image naomi2 slsmile flip = im.Flip("cr/naomi_slsmile.png", horizontal=True)
    image naomi2 slsmile b = "cr/naomi_slsmile_b.png"
    image naomi2 slsmile b flip = im.Flip("cr/naomi_slsmile_b.png", horizontal=True)
    image naomi2 shy = "cr/naomi_shy.png"
    image naomi2 shy flip = im.Flip("cr/naomi_shy.png", horizontal=True)
    image naomi2 shy b = "cr/naomi_shy_b.png"
    image naomi2 shy b flip = im.Flip("cr/naomi_shy_b.png", horizontal=True)
    image naomi2 scared = "cr/naomi_scared.png"
    image naomi2 scared flip = im.Flip("cr/naomi_scared.png", horizontal=True)
    image naomi2 scared b = "cr/naomi_scared_b.png"
    image naomi2 scared b flip = im.Flip("cr/naomi_scared_b.png", horizontal=True)
    image naomi2 smile = "cr/naomi_smile.png"
    image naomi2 smile flip = im.Flip("cr/naomi_smile.png", horizontal=True)
    image naomi2 smile b = "cr/naomi_smile_b.png"
    image naomi2 smile b flip = im.Flip("cr/naomi_smile_b.png", horizontal=True)
    image naomi2 smile d = "cr/naomi_smile_d.png"
    image naomi2 smile d flip = im.Flip("cr/naomi_smile_d.png", horizontal=True)
    image naomi2 stern = "cr/naomi_stern.png"
    image naomi2 stern flip = im.Flip("cr/naomi_stern.png", horizontal=True)
    image naomi2 stern b = "cr/naomi_stern_b.png"
    image naomi2 stern b flip = im.Flip("cr/naomi_stern_b.png", horizontal=True)
    image naomi2 stern c = "cr/naomi_stern_c.png"
    image naomi2 stern c flip = im.Flip("cr/naomi_stern_c.png", horizontal=True)
    image naomi2 surprised = "cr/naomi_surprised.png"
    image naomi2 surprised flip = im.Flip("cr/naomi_surprised.png", horizontal=True)
    image naomi2 surprisedblush = "cr/naomi_surprisedblush.png"
    image naomi2 surprisedblush flip = im.Flip("cr/naomi_surprisedblush.png", horizontal=True)
    image naomi2 cry sep = im.Sepia("cr/naomi_cry.png")
    image naomi2 scared sep = im.Sepia("cr/naomi_scared.png")
    image naomi2 hurt sep = im.Sepia("cr/naomi_hurt.png")
    image naomi2 aroused = "cr/naomi_aroused.png"
    image naomi2 cums = "cr/naomi_cums.png"
    image naomi2 cums flip = im.Flip("cr/naomi_cums.png", horizontal=True)
    
    image side naomi2 normal = im.Flip(im.Scale(im.Crop("cr/naomi_normal.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 normal b = im.Flip(im.Scale(im.Crop("cr/naomi_normal_b.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 normal d = im.Flip(im.Scale(im.Crop("cr/naomi_normal_d.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 angry = im.Flip(im.Scale(im.Crop("cr/naomi_angry.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 angry b = im.Flip(im.Scale(im.Crop("cr/naomi_angry_b.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 angry c = im.Flip(im.Scale(im.Crop("cr/naomi_angry_c.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 annoyed = im.Flip(im.Scale(im.Crop("cr/naomi_annoyed.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 annoyed b = im.Flip(im.Scale(im.Crop("cr/naomi_annoyed_b.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 bacon = im.Flip(im.Scale(im.Crop("cr/naomi_bacon.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 blank = im.Flip(im.Scale(im.Crop("cr/naomi_blank.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 blank b = im.Flip(im.Scale(im.Crop("cr/naomi_blank_b.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 blank d = im.Flip(im.Scale(im.Crop("cr/naomi_blank_d.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 cry = im.Flip(im.Scale(im.Crop("cr/naomi_cry.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 cry b = im.Flip(im.Scale(im.Crop("cr/naomi_cry_b.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 cry d = im.Flip(im.Scale(im.Crop("cr/naomi_cry_d.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 crysmile = im.Flip(im.Scale(im.Crop("cr/naomi_crysmile.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 crysmile b = im.Flip(im.Scale(im.Crop("cr/naomi_crysmile_b.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 concern = im.Flip(im.Scale(im.Crop("cr/naomi_concern.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 concern b = im.Flip(im.Scale(im.Crop("cr/naomi_concern_b.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 concern d = im.Flip(im.Scale(im.Crop("cr/naomi_concern_d.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 confused = im.Flip(im.Scale(im.Crop("cr/naomi_confused.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 confused b = im.Flip(im.Scale(im.Crop("cr/naomi_confused_b.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 confused d = im.Flip(im.Scale(im.Crop("cr/naomi_confused_d.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 hurt = im.Flip(im.Scale(im.Crop("cr/naomi_hurt.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 hurt b = im.Flip(im.Scale(im.Crop("cr/naomi_hurt_b.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 hurt d = im.Flip(im.Scale(im.Crop("cr/naomi_hurt_d.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 sad = im.Flip(im.Scale(im.Crop("cr/naomi_sad.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 sad b = im.Flip(im.Scale(im.Crop("cr/naomi_sad_b.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 slsmile = im.Flip(im.Scale(im.Crop("cr/naomi_slsmile.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 slsmile b = im.Flip(im.Scale(im.Crop("cr/naomi_slsmile_b.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 shy = im.Flip(im.Scale(im.Crop("cr/naomi_shy.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 shy b = im.Flip(im.Scale(im.Crop("cr/naomi_shy_b.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 scared = im.Flip(im.Scale(im.Crop("cr/naomi_scared.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 scared b = im.Flip(im.Scale(im.Crop("cr/naomi_scared_b.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 smile = im.Flip(im.Scale(im.Crop("cr/naomi_smile.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 smile b = im.Flip(im.Scale(im.Crop("cr/naomi_smile_b.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 smile d = im.Flip(im.Scale(im.Crop("cr/naomi_smile_d.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 stern = im.Flip(im.Scale(im.Crop("cr/naomi_stern.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 stern b = im.Flip(im.Scale(im.Crop("cr/naomi_stern_b.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 stern c = im.Flip(im.Scale(im.Crop("cr/naomi_stern_c.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 surprised = im.Flip(im.Scale(im.Crop("cr/naomi_surprised.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 surprisedblush = im.Flip(im.Scale(im.Crop("cr/naomi_surprisedblush.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 = 'side naomi normal'
    image side naomi2 cums = im.Flip(im.Scale(im.Crop("cr/naomi_cums.png",(70,80,500,600)),250,300),horizontal=True)
    image side naomi2 aroused = im.Flip(im.Scale(im.Crop("cr/naomi_aroused.png",(70,80,500,600)),250,300),horizontal=True)

