import numpy as np
import re
import copy
from sympy import Interval

# First line : Seeds to plant
# Destination range start | Source range start | Range length


# 50 | 98 | 2 
# 52 | 50 | 48
## -> Seed number 98 correspond to soil number 50
## -> Seed number 99 cirresoibd to soil number 51

## -> Seed number 50 correspond to soil number 52
## -> And so one for Seed (51-97) and oil (53-99)

#! If not mapped, source goes to same destination number.


'''
Find the lowest location number that corresponds to any 
of the initial seeds.

What is the lowest location number that corresponds 
to any of the initial seed numbers ?
'''

Seeds = "1778931867 1436999653 3684516104 2759374 1192793053 358764985 1698790056 76369598 3733854793 214008036 4054174000 171202266 3630057255 25954395 798587440 316327323 290129780 7039123 3334326492 246125391".split()
Seeds = [int(seed) for seed in Seeds]

Seed_Soil = [re.split(' ', line) for line in """1965922922 2387203602 59808406
2540447436 434094583 220346698
2217992666 1677013102 149631368
0 700424909 25332775
2488189883 199146916 52257553
1096820417 2512808179 247985955
25332775 725757684 113904366
4167057552 3534307691 127909744
1787863383 0 33562512
2947958449 3662217435 64182733
2907785302 3360301224 40173147
3774943096 4218385602 76581694
693455216 1273647901 403365201
380961654 1909017232 171283127
139237141 1031923388 241724513
2367624034 251404469 38193087
3038180364 3429533867 104773824
2484064707 1826644470 4125176
1344806372 128789319 70357597
3012141182 3109705711 26039182
1821425895 289597556 144497027
598228409 33562512 95226807
2405817121 1830769646 78247586
552244781 654441281 45983628
3641222276 3255639900 104661324
3851524790 3726400168 315532762
2025731328 839662050 192261338
3464769604 4041932930 176452672
1480960140 2080300359 306903243
1415163969 2447012008 65796171
3142954188 2787890295 321815416
3745883600 3400474371 29059496
2787890295 3135744893 119895007""".split('\n')]

Seed_Soil = [[int(elem) for elem in line] for line in Seed_Soil]
print("Seed_Soil_1 : " , Seed_Soil)

Soil_Fertilizer = [re.split(' ', line) for line in """974611207 822914672 41736646
1617020803 484683369 227984726
2936246728 1897199618 22236339
1599589242 1541299272 17431561
897092117 484593057 90312
2958483067 3614284126 70951194
3636585470 2567424345 5451325
0 2712467888 73845937
2654331234 1997195625 281915494
3241974258 3685235320 31499686
3642036795 3512208003 74698211
1092039278 1347003830 194295442
790747225 1558730833 106344892
897182429 42121154 77428778
1845005529 380881656 29170315
313046856 3156899567 355308436
1952497963 410051971 74541086
3043555623 2369005710 198418635
2040295599 119549932 261331724
3630375808 2279111119 6209662
3383720521 1665075725 217219287
2301627323 2670771541 41696347
1515904313 2285320781 83684929
73845937 1076160024 239200919
2343323670 864651318 182031257
2027039049 3601027576 13256550
2622688347 1315360943 31642887
2525354927 2572875670 19573752
1286334720 1076118575 41449
4007771416 3743620838 287195880
668355292 0 42121154
1286376169 1882295012 14904606
3600939808 1046682575 29436000
2544928679 1919435957 77759668
3273473944 712668095 110246577
3029434261 3586906214 14121362
3743620838 4030816718 264150578
710476446 2786313825 80270779
1016347853 3081208142 75691425
1874175844 2592449422 78322119
1301280775 2866584604 214623538""".split('\n')]

Soil_Fertilizer = [[int(elem) for elem in line] for line in Soil_Fertilizer]

Fertilizer_Water = [re.split(' ', line) for line in """2256462238 272868806 222756596
2883874475 1945255196 178320531
1025753868 1262393928 220069640
2780673998 2532762404 101990486
222030751 1026223684 236170244
828766276 1895857025 35481787
3755107810 3521770115 3468846
2048518620 2246637941 74827173
550785854 2716185082 5650779
1819399513 252684903 20183903
4134370427 3177062502 147573242
1893363918 2365324803 45336497
458200995 495625402 92584859
3472537931 3557968177 35060837
122101104 2962265359 99929647
2192091098 2172374449 64371140
3538267850 3324635744 184110744
3758576656 3169743127 7319375
0 2410661300 122101104
4281943669 3508746488 13023627
1849504229 2321465114 43859689
3722378594 3525238961 32729216
1245823508 588210261 161392539
878164447 2814675938 147589421
864248063 1931338812 13916384
1938700415 749602800 109818205
2123345793 2745930633 68745305
3765896031 3826310364 218680395
747334084 2634752890 78853599
3984576426 4075659841 149794001
2882664484 1482463568 1209991
723239312 2721835861 24094772
3169743127 3593029014 233281350
1839583416 252656442 28461
2479218834 0 252656442
3507598768 4044990759 30669082
826187683 2713606489 2578593
1839611877 2236745589 9892352
556436633 859421005 166802679
3403024477 4225453842 69513454
2731875276 2123575727 48798722
1407216047 1483673559 412183466""".split('\n')]

Fertilizer_Water = [[int(elem) for elem in line] for line in Fertilizer_Water]

Water_Light = [re.split(' ', line) for line in """2717406339 2056643664 131336656
2149066749 0 164219220
3368552624 3554596203 347071357
648177882 2187980320 58382041
2313285969 387274540 87651626
1956244903 880459831 74655597
630498803 2299352502 17679079
2030900500 1938477415 118166249
2958998106 3901667560 109063910
0 2317031581 376289577
1862852214 809822482 58007210
3962172007 3368255348 186340855
1920859424 164219220 35385479
829057433 474926166 334896316
2848742995 867829692 12630139
3068062016 3067764740 300490608
2628314327 1849385403 89092012
1363807094 955115428 499045120
441461908 1660348508 189036895
1195755118 2693321158 168051976
706559923 199604699 122497510
3824390615 4010731470 137781392
2400937595 2246362361 21188772
3715623981 2958998106 108766634
1163953749 2267551133 31801369
2422126367 1454160548 2061879
376289577 322102209 65172331""".split('\n')]

Water_Light = [[int(elem) for elem in line] for line in Water_Light]

Light_Temperature = [re.split(' ', line) for line in """356025838 1142133666 189347695
155231063 1824123064 78066821
3486401291 3916497965 63138309
3054537751 3004205340 53510430
545373533 1910851890 39759630
43898462 1414278470 16090003
233297884 608643392 7876607
0 1051586050 43898462
3108048181 3669777676 160948090
3567273965 3979636274 194976344
146569058 1902189885 8662005
1423483364 1430368473 110560056
2195994218 3468690397 201087279
2497560353 2680093671 17356840
2667148760 3057715770 80634162
2747782922 2697450511 306754829
585133163 1540928529 283194535
1534043420 440260576 168382816
3762250309 2063919656 446944788
3318335889 3300624995 168065402
1308588274 1331481361 82797109
74539638 616519999 1422739
2546794082 4174612618 120354678
3268996271 3201674123 49339618
2127243847 2611343300 68750371
59988465 1095484512 14551173
2397081497 2510864444 100478856
1391385383 1110035685 32097981
1702426236 1016254966 35331084
3549539600 3282890630 17734365
2063919656 3138349932 63324191
1737757320 803400766 212854200
2514917193 3251013741 31876889
4209195097 3830725766 85772199
1003769840 135442142 304818434
241174491 617942738 114851347
868327698 0 135442142
75962377 732794085 70606681""".split('\n')]

Light_Temperature = [[int(elem) for elem in line] for line in Light_Temperature]

Temperature_Humidity = [re.split(' ', line) for line in """3056037605 2829211160 523334807
321779731 0 47068359
3924298564 3372771457 370668732
1103457901 562085848 156691500
0 240306117 321779731
368848090 1020196358 239953043
2829211160 3743440189 226826445
608801133 718777348 301419010
3579372412 3970266634 324700662
3915140668 3363613561 9157896
910220143 232146746 8159371
3904073074 3352545967 11067594
918379514 47068359 185078387""".split('\n')]

Temperature_Humidity = [[int(elem) for elem in line] for line in Temperature_Humidity]

Humidity_Location = [re.split(' ', line) for line in """1384411009 3878276792 140553103
3206048776 3137400006 12882465
2370337851 2414914902 179202838
23738616 0 161914533
0 262282387 23738616
840681798 3768356904 109919888
2340008493 3054171079 26130417
1524964112 840681798 815044381
3130048499 2668879895 76000277
185653149 548908967 81490523
3465042209 3687267183 62255927
367511526 286021003 262887964
3005762489 2744880172 124286010
1025363841 2357768227 57146675
2549540689 1901546427 456221800
3218931241 4018829895 240309425
1101344310 2869166182 185004897
1286349207 1655726179 98061802
2366138910 1753787981 4198941
3459240666 4259139320 5801543
950601686 2594117740 74762155
3584396646 1757986922 143559505
267143672 161914533 100367854
3527298136 3080301496 57098510
1082510516 3749523110 18833794
3727956151 3150282471 536984712""".split('\n')]

Humidity_Location = [[int(elem) for elem in line] for line in Humidity_Location]
location_results = []

"""
for seed in Seeds:
    # for Table in Table_list:
    for S_S in Seed_Soil:
        if (int(S_S[1]) <= seed < int(S_S[1]) + int(S_S[2])) :
            seed = int(S_S[0]) + (int(seed) - int(S_S[1]))
            break
    for S_F in Soil_Fertilizer:
        if (int(S_F[1]) <= seed < int(S_F[1]) + int(S_F[2])) :
            seed = int(S_F[0]) + (seed - int(S_F[1]))
            break
    for F_W in Fertilizer_Water:
        if (int(F_W[1]) <= seed < int(F_W[1]) + int(F_W[2])) :
            seed = int(F_W[0]) + (seed - int(F_W[1]))
            break
    for W_L in Water_Light:
        if (int(W_L[1]) <= seed < int(W_L[1]) + int(W_L[2])) :
            seed = int(W_L[0]) + (seed - int(W_L[1]))
            break
    for L_T in Light_Temperature:
        if (int(L_T[1]) <= seed < int(L_T[1]) + int(L_T[2])) :
            seed = int(L_T[0]) + (seed - int(L_T[1]))
            break
    for T_H in Temperature_Humidity:
        if (int(T_H[1]) <= seed < int(T_H[1]) + int(T_H[2])) :
            seed = int(T_H[0]) + (seed - int(T_H[1]))
            break
    for H_L in Humidity_Location:
        if (int(H_L[1]) <= seed < int(H_L[1]) + int(H_L[2])) :
            seed = int(H_L[0]) + (seed - int(H_L[1]))
            break

    location_results.append(int(seed))
    
    result1 = min(location_results)    # Too high 348254968  | # Too high 297654125 | (Forgot 1 line in 2 table) | 
"""
#print("This is Location_results : ", location_results)
#print("This is the result : ", result1)


### Part 2 : 
# Idea, maybe it will be needed to reverse (starting from lower location) for matching performance requirements

# First elem : Min values that will go through the filter in the map 1.
# Second elem : Max values that whill go through the filter in the map 1.
# Third elem : Const value applied to the values that go through this filter in map 1.


# Table_list = ["Seed_Soil", "Soil_Fertilizer", "Fertilizer_Water", "Water_Light", "Light_Temperature", "Temperature_Humidity", "Humidity_Location"]

# A original value will go through filter in map 2 IF 
    # value going through filter in map 1 AND intersection between output map 1 - input map 2
    # OR value not going through filter in map 1 AND in range filter map 2

# SI A_1+c = A_2 et B_1+c = B_2 
#    -> Intervalle identique mais actualiser la valeur de c (continue)
# SI A_1+c > B_2 OU B1+C < A_2
#   -> Pas de modifications (pass)
# SI A2 < A1+c < B2 
#   -> Nouveaux intervalles : A2-A1 (+c) | A1-B2 (+c) | B2-B1 (+c)
# SI A2 < B1+c < B2
#   -> Nouveaux intervalles : A1-A2 (+c) | A2-B1 (+c) | B1-B2 (+c)

New_seeds = [[Seeds[i], Seeds[i] + Seeds[i+1]] for i in range(0, len(Seeds), 2)]
# print(New_seeds)


# Table_list = ["Seed_Soil", "Soil_Fertilizer", "Fertilizer_Water", "Water_Light", "Light_Temperature", "Temperature_Humidity", "Humidity_Location"]

### Step 1 : Formattage de chaque table sous forme:  Start, End, Const

SS_Part1 = {line[1]:line[0]-line[1] for line in Seed_Soil}
SS_Part2 = {line[1] + line[2]:0 for line in Seed_Soil}
Dict_SeedToSoil = dict(sorted(SS_Part1.items() | SS_Part2.items()))

### Step 2 : 
Range_Global = sorted(copy.deepcopy(Seed_Soil), key=lambda x:x[1])
Dict_Global = copy.deepcopy(Dict_SeedToSoil)
Range_Global.append([4294967296, 4294967296, 5705032703])

print("Length after Table 1 : ", len(Dict_Global),  "\n", "\n")
print("This is Range Global : ", Range_Global,  "\n", "\n")
print("This is Dict Global : ", Dict_Global,  "\n", "\n")

print(Dict_Global)

# 2ème table
for Range in Range_Global:
    for Line in Soil_Fertilizer:
        DebRange = Range[1]
        FinRange = Range[1] + Range[2]
        ConstRange = Range[0] - Range[1]
        DebLine = Line[1]
        FinLine = Line [1] + Line[2]
        ConstLine = Line[0] - Line[1]
        if (Interval(DebRange + ConstRange, FinRange + ConstRange).intersect(Interval(DebLine, FinLine))):
            if DebLine >= DebRange + ConstRange:
                Dict_Global[DebLine - ConstRange] = ConstRange + ConstLine
            if FinLine <= FinRange + ConstRange :
                Dict_Global[FinLine - ConstRange] = ConstRange + ConstLine

print("Length after Table 2 : ", len(Dict_Global),  "\n", "\n")
print("This is Dict_Global After Table 2 : ", Dict_Global, "\n", "\n")

# Conversion de dict en list
Swap_Global = []
Range_Global = sorted(list(Dict_Global.items()))

for i in range(0, len(Range_Global)-1, 1):
    Swap_Global.append([Range_Global[i][0]+Range_Global[i][1], Range_Global[i][0], Range_Global[i+1][0]-Range_Global[i][0]]) 
Swap_Global.append([Range_Global[-1][1], Range_Global[-1][1], 5705032703])

print("This is Swap_Global 2 : ", Swap_Global, "\n", "\n")

## 3ème table

for Range in Swap_Global:
    for Line in Fertilizer_Water:
        DebRange = Range[1]
        FinRange = Range[1] + Range[2]
        ConstRange = Range[0] - Range[1]
        DebLine = Line[1]
        FinLine = Line [1] + Line[2]
        ConstLine = Line[0] - Line[1]
        if (Interval(DebRange + ConstRange, FinRange + ConstRange).intersect(Interval(DebLine, FinLine))):
            if DebLine >= DebRange + ConstRange:
                Dict_Global[DebLine - ConstRange] = ConstRange + ConstLine
            if FinLine <= FinRange + ConstRange :
                Dict_Global[FinLine - ConstRange] = ConstRange + ConstLine

print("Length after Table 3 : ", len(Dict_Global),  "\n", "\n")

# Conversion de dict en list
Range_Global = []
Swap_Global = sorted(list(Dict_Global.items()))

for i in range(0, len(Swap_Global)-1, 1):
    Range_Global.append([Swap_Global[i][0]+Swap_Global[i][1], Swap_Global[i][0], Swap_Global[i+1][0]-Swap_Global[i][0]])
Range_Global.append([Swap_Global[-1][1], Swap_Global[-1][1], 5705032703])

print("This is Range_Global 3 : ", Range_Global, "\n", "\n")

## 4ème table

for Range in Range_Global:
    for Line in Water_Light:
        DebRange = Range[1]
        FinRange = Range[1] + Range[2]
        ConstRange = Range[0] - Range[1]
        DebLine = Line[1]
        FinLine = Line [1] + Line[2]
        ConstLine = Line[0] - Line[1]
        if (Interval(DebRange + ConstRange, FinRange + ConstRange).intersect(Interval(DebLine, FinLine))):
            if DebLine >= DebRange + ConstRange:
                Dict_Global[DebLine - ConstRange] = ConstRange + ConstLine
            if FinLine <= FinRange + ConstRange :
                Dict_Global[FinLine - ConstRange] = ConstRange + ConstLine

print("Length after Table 4 : ", len(Dict_Global),  "\n", "\n")

# Conversion de dict en list
Swap_Global = []
Range_Global = sorted(list(Dict_Global.items()))

for i in range(0, len(Range_Global)-1, 1):
    Swap_Global.append([Range_Global[i][0]+Range_Global[i][1], Range_Global[i][0], Range_Global[i+1][0]-Range_Global[i][0]])
Swap_Global.append([Range_Global[-1][1], Range_Global[-1][1], 5705032703])

print("This is Swap_Global 4 : ", Swap_Global, "\n", "\n")

## 5ème table 

for Range in Swap_Global:
    for Line in Light_Temperature:
        DebRange = Range[1]
        FinRange = Range[1] + Range[2]
        ConstRange = Range[0] - Range[1]
        DebLine = Line[1]
        FinLine = Line [1] + Line[2]
        ConstLine = Line[0] - Line[1]
        if (Interval(DebRange + ConstRange, FinRange + ConstRange).intersect(Interval(DebLine, FinLine))):
            if DebLine >= DebRange + ConstRange:
                Dict_Global[DebLine - ConstRange] = ConstRange + ConstLine
            if FinLine <= FinRange + ConstRange :
                Dict_Global[FinLine - ConstRange] = ConstRange + ConstLine

print("Length after Table 5 : ", len(Dict_Global),  "\n", "\n")

# Conversion de dict en list
Range_Global = []
Swap_Global = sorted(list(Dict_Global.items()))

for i in range(0, len(Swap_Global)-1, 1):
    Range_Global.append([Swap_Global[i][0]+Swap_Global[i][1], Swap_Global[i][0], Swap_Global[i+1][0]-Swap_Global[i][0]])
Range_Global.append([Swap_Global[-1][1], Swap_Global[-1][1], 5705032703])
print("This is Range_Global 5 : ", Range_Global, "\n", "\n")


## 6ème table 

for Range in Range_Global:
    for Line in Temperature_Humidity:
        DebRange = Range[1]
        FinRange = Range[1] + Range[2]
        ConstRange = Range[0] - Range[1]
        DebLine = Line[1]
        FinLine = Line [1] + Line[2]
        ConstLine = Line[0] - Line[1]
        if (Interval(DebRange + ConstRange, FinRange + ConstRange).intersect(Interval(DebLine, FinLine))):
            if DebLine >= DebRange + ConstRange:
                Dict_Global[DebLine - ConstRange] = ConstRange + ConstLine
            if FinLine <= FinRange + ConstRange :
                Dict_Global[FinLine - ConstRange] = ConstRange + ConstLine

print("Length after Table 6 : ", len(Dict_Global),  "\n", "\n")

# Conversion de dict en list
Swap_Global = []
Range_Global = sorted(list(Dict_Global.items()))

for i in range(0, len(Range_Global)-1, 1):
    Swap_Global.append([Range_Global[i][0]+Range_Global[i][1], Range_Global[i][0], Range_Global[i+1][0]-Range_Global[i][0]])
Swap_Global.append([Range_Global[-1][1], Range_Global[-1][1], 5705032703])
print("This is Swap_Global 6 : ", Swap_Global, "\n", "\n")


## 7ème table (et dernière)

for Range in Swap_Global:
    for Line in Humidity_Location:
        DebRange = Range[1]
        FinRange = Range[1] + Range[2]
        ConstRange = Range[0] - Range[1]
        DebLine = Line[1]
        FinLine = Line [1] + Line[2]
        ConstLine = Line[0] - Line[1]
        if (Interval(DebRange + ConstRange, FinRange + ConstRange).intersect(Interval(DebLine, FinLine))):
            if DebLine >= DebRange + ConstRange:
                Dict_Global[DebLine - ConstRange] = ConstRange + ConstLine
            if FinLine <= FinRange + ConstRange :
                Dict_Global[FinLine - ConstRange] = ConstRange + ConstLine

print("Length after Table 7 : ", len(Dict_Global),  "\n", "\n")

# Conversion de dict en list
Range_Global = []
Swap_Global = sorted(list(Dict_Global.items()))

for i in range(0, len(Swap_Global)-1, 1):
    Range_Global.append([Swap_Global[i][0]+Swap_Global[i][1], Swap_Global[i][0], Swap_Global[i+1][0]-Swap_Global[i][0]])
Range_Global.append([Swap_Global[-1][1], Swap_Global[-1][1], 5705032703])
print("This is Range_Global 7 : ", Range_Global, "\n", "\n")


### Final Step : Testing all the starting values to find the minimun

location_results2 = []
Seeds2 = [line[1] for line in Range_Global]
print("This is the acceptable input range : ", New_seeds, "\n", "\n")
print("This is Seed2 before filtering : ", Seeds2, "\n", "\n")

Seeds2_Filtered = [0]
for seed in Seeds2:
    for PLEASE in New_seeds:
        if(PLEASE[0] <= seed < PLEASE[1]):
            Seeds2_Filtered.append(seed)
            break

print("This is the testable inputs : ", Seeds2_Filtered, "\n", "\n")



for seed in Seeds2_Filtered:
    # for Table in Table_list:
    for S_S in Seed_Soil:
        if (int(S_S[1]) <= seed < int(S_S[1]) + int(S_S[2])) :
            seed = int(S_S[0]) + (int(seed) - int(S_S[1]))
            break
    for S_F in Soil_Fertilizer:
        if (int(S_F[1]) <= seed < int(S_F[1]) + int(S_F[2])) :
            seed = int(S_F[0]) + (seed - int(S_F[1]))
            break
    for F_W in Fertilizer_Water:
        if (int(F_W[1]) <= seed < int(F_W[1]) + int(F_W[2])) :
            seed = int(F_W[0]) + (seed - int(F_W[1]))
            break
    for W_L in Water_Light:
        if (int(W_L[1]) <= seed < int(W_L[1]) + int(W_L[2])) :
            seed = int(W_L[0]) + (seed - int(W_L[1]))
            break
    for L_T in Light_Temperature:
        if (int(L_T[1]) <= seed < int(L_T[1]) + int(L_T[2])) :
            seed = int(L_T[0]) + (seed - int(L_T[1]))
            break
    for T_H in Temperature_Humidity:
        if (int(T_H[1]) <= seed < int(T_H[1]) + int(T_H[2])) :
            seed = int(T_H[0]) + (seed - int(T_H[1]))
            break
    for H_L in Humidity_Location:
        if (int(H_L[1]) <= seed < int(H_L[1]) + int(H_L[2])) :
            seed = int(H_L[0]) + (seed - int(H_L[1]))
            break

    location_results2.append(int(seed))
    
result2 = min(location_results2)            
# 894303567 -- Too High  | 6577901 -- Too low  | 27009985 -- Too high | 23738616 !!!!!!!!!!!!!!!!!!!!!


print("This is supposedly the final result : ", result2, "\n", "\n")


Alternative = sorted([line[0] for line in Range_Global])
Check = [(line[0], line[1], line[2]) for line in Range_Global if line[0] == 23738616]
print("This is just a test...   :", Alternative, "\n")
print("WTF : Check :  ", Check, "\n")