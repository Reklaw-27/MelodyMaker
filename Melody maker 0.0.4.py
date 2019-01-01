import random
import time
import math
import configparser
import sys

VERSION = "0.0.4"

#To-do list
    #Start on 1,3,5 resolve on 1 or 3
        #when doing a half melody end on 5 almost always
        #Right now it resolves on 6th sometimes
    #4 must resolve on 3 and 7 must resolve on 1
    #Get rid of tritones
    #Right now I have natural minor, harmonic is more common
    #

    #decide if octave leaps are good
    #make two leaps in a row, bottom heavy
    #add travelling an octave with lead up/cool down
    #add possibility to resolve, but not always

###################################################################

keys = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B","Cmin","C#min","Dmin","D#min","Emin","Fmin","F#min","Gmin","G#min","Amin","A#min","Bmin"]

yes = ['yes','y','yep','yesh','yeah','i guess','yup','']

TEST_N = ["test"]

A_N = ['A','A major','a','a major','Amaj','amaj','A maj','a maj']
AS_N = ['A#','a#','A #','a #','A sharp','a sharp','A Sharp','a Sharp',]
AF_N = ['Ab','ab','A b','a b','A flat','a flat','A Flat','a Flat',]
Amin_N = ['Am','am','A minor','a minor','Amin','amin','A min','a min']
ASmin_N = ['A#min','a#min','A#m','a#m''A#minor','a#minor','A# min','a# min']
AFmin_N = ['Abmin','abmin','Abm','abm','Abminor','abminor','Ab min','ab min']
B_N = ['B','B major','b','b major','Bmaj','bmaj','B maj','b maj']
BS_N = ['B#','b#','B #','b #','B sharp','b sharp','B Sharp','b Sharp',]
BF_N = ['Bb','bb','B b','b b','B flat','b flat','B Flat','b Flat',]
Bmin_N = ['Bm','bm','B minor','b minor','Bmin','bmin','B min','b min']
BSmin_N = ['B#min','b#min','B#m','b#m','B#minor','b#minor','B# min','b# min']
BFmin_N = ['Bbmin','bbmin','Bbm','bbm','Bbminor','bbminor','Bb min','bb min']
C_N = ['C','C major','c','c major','Cmaj','cmaj','C maj','c maj']
CS_N = ['C#','c#','C #','c #','C sharp','c sharp','C Sharp','c Sharp',]
CF_N = ['Cb','cb','C b','c b','C flat','c flat','C Flat','c Flat',]
Cmin_N = ['Cm','cm','C minor','c minor','Cmin','cmin','C min','c min']
CSmin_N = ['C#min','c#min','C#m','c#m','C#minor','c#minor','C# min','c# min']
CFmin_N = ['Cbmin','cbmin','Cbm','cbm','Cbminor','cbminor','Cb min','cb min']
D_N = ['D','D major','d','d major','Dmaj','dmaj','D maj','d maj']
DS_N = ['D#','d#','D #','d #','D sharp','d sharp','D Sharp','d Sharp',]
DF_N = ['Db','db','D b','d b','D flat','d flat','D Flat','d Flat',]
Dmin_N = ['Dm','dm','D minor','d minor','Dmin','dmin','D min','d min']
DSmin_N = ['D#min','d#min','D#m','d#m','D#minor','d#minor','D# min','d# min']
DFmin_N = ['Dbmin','dbmin','Dbm','dbm','Dbminor','dbminor','Db min','db min']
E_N = ['E','E major','e','e major','Emaj','emaj','E maj','e maj']
EF_N = ['Eb','eb','E b','e b','E flat','e flat','E Flat','e Flat',]
ES_N = ['E#','e#','E #','e #','E sharp','e sharp','E Sharp','e Sharp',]
Emin_N = ['Em','em','E minor','e minor','Emin','emin','E min','e min']
EFmin_N = ['Ebmin','ebmin','Ebm','ebm','Ebminor','ebminor','Eb min','eb min']
ESmin_N = ['E#min','e#min','E#m','e#m','E#minor','e#minor','E# min','e# min']
F_N = ['F','F major','f','f major','Fmaj','fmaj','F maj','f maj']
FS_N = ['F#','f#','F #','f #','F sharp','f sharp','F Sharp','f Sharp',]
FF_N = ['Fb','fb','F b','f b','F flat','f flat','F Flat','f Flat',]
Fmin_N = ['Fm','fm','F minor','f minor','Fmin','fmin','F min','f min']
FSmin_N = ['F#min','f#min','F#m','f#m','F#minor','f#minor','F# min','f# min']
FFmin_N = ['Fbmin','fbmin','Fbm','fbm','Fbminor','fbminor','Fb min','fb min']
G_N = ['G','G major','g','g major','Gmaj','gmaj','G maj','g maj']
GS_N = ['G#','g#','G #','g #','G sharp','g sharp','G Sharp','g Sharp',]
GF_N = ['Gb','gb','G b','g b','G flat','g flat','G Flat','g Flat',]
Gmin_N = ['Gm','gm','G minor','g minor','Gmin','gmin','G min','g min']
GSmin_N = ['G#min','g#min','G#m','g#m','G#minor','g#minor','G# min','g# min']
GFmin_N = ['Gbmin','gbmin','Gbm','gbm','Gbminor','gbminor','Gb min','gb min']

#############################################################################

TEST_m = ["I3","II3","III3","IV3","V3","VI3","VII3","I4","II4","III4","IV4","V4","VI4","VII4","I5","II5","III5","IV5","V5","VI5","VII5"]

C_m = ["C3","D3","E3","F3","G3","A3","B3","C4","D4","E4","F4","G4","A4","B4","C5","D5","E5","F5","G5","A5","B5"]
CS_m = ["C#3","D#3","F3","F#3","G#3","A#3","C3","C#4","D#4","F4","F#4","G#4","A#4","C4","C#5","D#5","F5","F#5","G#5","A#5","C5","C#5"]
D_m = ["D3","E3","F#3","G3","A3","B3","C#4","D4","E4","F#4","G4","A4","B4","C#5","D5","E5","F#5","G5","A5","B5","C#6"]
DS_m = ["D#3","F3","G3","G#3","A#3","C4","D4","D#4","F4","G4","G#4","A#4","C5","D5","D#5","F5","G5","G#5","A#5","C6","D6"]
E_m = ["E3","F#3","G#3","A3","B3","C#4","D#4","E4","F#4","G#4","A4","B4","C#5","D#5","E5","F#5","G#5","A5","B5","C#6","D#6"]
F_m = ["F3","G3","A3","A#3","C4","D4","E4","F4","G4","A4","A#4","C5","D5","E5","F5","G5","A5","A#5","C6","D6","E6"]
FS_m = ["F#3","G#3","A#3","B3","C#4","D#4","F4","F#4","G#4","A#4","B4","C#5","D#5","F5","F#5","G#5","A#5","B5","C#6","D#6","F6"]
G_m = ["G3","A3","B3","C4","D4","E4","F#4","G4","A4","B4","C5","D5","E5","F#5","G5","A5","B5","C6","D6","E6","F#6"]
GS_m = ["G#3","A#3","C4","C#4","D#4","F4","G4","G#4","A#4","C5","C#5","D#5","F5","G4","G#5","A#5","C6","C#6","D#6","F6","G6"]
A_m = ["A3","B3","C#4","D4","E4","F#4","G#4","A4","B4","C#5","D5","E5","F#5","G#5","A5","B5","C#6","D6","E6","F#6","G#6"]
AS_m = ["A#3","C4","D4","D#4","F4","G4","A4","A#4","C5","D5","D#5","F5","G5","A5","A#5","C6","D6","D#6","F6","G6","A6"]
B_m = ["B3","C#4","D#4","E4","F#4","G#4","A#4","B4","C#5","D#5","E5","F#5","G#5","A#5","B5","C#6","D#6","E6","F#6","G#6","A#6"]

Cmin_m = ["C3","D3","D#3","F3","G3","G#3","A#3","C4","D4","D#4","F4","G4","G#4","A#4","C5","D5","D#5","F5","G5","G#5","A#5"]
CSmin_m = ["C#3","D#3","E3","F#3","G#3","A3","B3","C#4","D#4","E4","F#4","G#4","A4","B4","C#5","D#5","E5","F#5","G#5","A5","B5"]
Dmin_m = ["D3","E3","F3","G3","A3","A#3","C4","D4","E4","F4","G4","A4","A#4","C5","D5","E5","F5","G5","A5","A#5","C6"]
DSmin_m = ["D#3","F3","F#3","G#3","A#3","B3","C#4","D#4","F4","F#4","G#4","A#4","B4","C#5","D#5","F5","F#5","G#5","A#5","B5","C#6"]
Emin_m = ["E3","F#3","G3","A3","B3","C4","D4","E4","F#4","G4","A4","B4","C5","D5","E5","F#5","G5","A5","B5","C6","D6"]
Fmin_m = ["F3","G3","G#3","A#3","C4","C#4","D#4","F4","G4","G#4","A#4","C5","C#5","D#5","F5","G5","G#5","A#5","C6","C#6","D#6"]
FSmin_m = ["F#3","G#3","A3","B3","C#4","D4","E4","F#4","G#4","A4","B4","C#5","D5","E5","F#5","G#5","A5","B5","C#6","D6","E6"]
Gmin_m = ["G3","A3","A#3","C4","D4","D#4","F4","G4","A4","A#4","C5","D5","D#5","F5","G5","A5","A#5","C6","D6","D#6","F6"]
GSmin_m = ["G#3","A#3","B3","C#4","D#4","E4","F#4","G#4","A#4","B4","C#5","D#5","E5","F#5","G#5","A#5","B5","C#6","D#6","E6","F#6"]
Amin_m = ["A3","B3","C4","D4","E4","F4","G4","A4","B4","C5","D5","E5","F5","G5","A5","B5","C6","D6","E6","F6","G6"]
ASmin_m = ["A#3","C4","C#4","D#4","F4","F#4","G#4","A#4","C5","C#5","D#5","F5","F#5","G#5","A#5","C6","C#6","D#6","F6","F#6","G#6"]
Bmin_m = ["B3","C#4","D#4","E4","F#4","G#4","A4","B4","C#5","D#5","E5","F#5","G#5","A5","B5","C#6","D#6","E6","F#6","G#6","A6"]

############################################################################################################################################

"""MODES"""

ionian = 0
dorian = 1
phrygian = 2
lydian = 3
mixolydian = 4
aeolian = 5
locrian = 6

############################################################################################################################################

moves_1 = ("u3u2","d3d2","d2u3","u2d3","u3d2","d3u2","d2u3d2","u2d3u2","d2d2u3","u2u2d3","u3d2d2","d3u2u2","d2u4d2","u2d4u2","d2d2u4","u2u2d4","u4d2d2","d4u2u2","d2d2u4d2","u2u2d4u2","d2u4d2d2","u2d4u2u2","d2u5d2","u2d5u2","d2u5d2d2","u2d5u2u2","d2d2u5d2","u2u2d5u2","d2u4u3d2","u2d4d3u2","d2u5u3d2","u2d5d3u2","d2d2d2u6d2","u2u2u2d6u2","d2u6d2d2d2","u2d6u2u2u2")
moves_2 = ("u3u2","d3d2","d2u3","u2d3","u3d2","d3u2","d2u3d2","u2d3u2","d2d2u3","u2u2d3","u3d2d2","d3u2u2","d2u4d2","u2d4u2","d2d2u4","u2u2d4","u4d2d2","d4u2u2","d2d2u4d2","u2u2d4u2","d2u4d2d2","u2d4u2u2","d2u5d2","u2d5u2","d2u5d2d2","u2d5u2u2","d2d2u5d2","u2u2d5u2","d2u4u3d2","u2d4d3u2","d2u5u3d2","u2d5d3u2")
moves_3 = ("u3u2","d3d2","d2u3","u2d3","u3d2","d3u2","d2u3d2","u2d3u2","d2d2u3","u2u2d3","u3d2d2","d3u2u2","d2u4d2","u2d4u2","d2d2u4","u2u2d4","u4d2d2","d4u2u2")
#possible additions to move list go here
"u2u2u2u2u2d2d6","d2d2d2d2d2u2u6"

#outlawed moves
"u2d2u2","d2u2d2"

############################################################################################################################################

print("Welcome to MelodyMaker™ " + VERSION + "\n")

def rotate(l, n): #Sets up the rotate function that the modes use
    return l[n:] + l[:n]

def questions_m():

    global key_response_m
    global key_m
    global money
    global mode_r

    key_response_m = input("What key do you want the Melody™ in? ")#asks user questions about parameters
    key_response_m = key_response_m.lower()

    mode_r = input("What mode do you want the scale in? ")
    mode_r = mode_r.lower()

    money = input("How much Melody Money™ do you want? ")#the melody will usually be 2 notes longer than the value of MM but not always
    melody_money = int(money)

def MelodyMaker_basic():

    melodic_line = []
    embezzle = False #When embezzle is true, key is minor

    if key_response_m in TEST_N:
       key_m =  TEST_m
    elif key_response_m in C_N:
        key_m = C_m
    elif key_response_m in CS_N or key_response_m in DF_N:
        key_m = CS_m
    elif key_response_m in D_N:
        key_m = D_m
    elif key_response_m in DS_N or key_response_m in EF_N:
        key_m = DS_m
    elif key_response_m in E_N:
        key_m = E_m
    elif key_response_m in F_N:
        key_m = F_m
    elif key_response_m in FS_N or key_response_m in GF_N:
        key_m = FS_m
    elif key_response_m in G_N:
        key_m = G_m
    elif key_response_m in GS_N or key_response_m in AF_N:
        key_m = GS_m
    elif key_response_m in A_N:
        key_m = A_m
    elif key_response_m in AS_N or key_response_m in BF_N:
        key_m = AS_m
    elif key_response_m in B_N:
        key_m = B_m
        
    elif key_response_m in Cmin_N:
        key_m = Cmin_m
        embezzle = True
    elif key_response_m in CSmin_N or key_response_m in DFmin_N:
        key_m = DSmin_m
        embezzle = True
    elif key_response_m in Dmin_N:
        key_m = Dmin_m
        embezzle = True
    elif key_response_m in DSmin_N or key_response_m in EFmin_N:
        key_m = DSmin_m
        embezzle = True
    elif key_response_m in Emin_N:
        key_m = Emin_m
        embezzle = True
    elif key_response_m in Fmin_N:
        key_m = Fmin_m
        embezzle = True
    elif key_response_m in FSmin_N or key_response_m in GFmin_N:
        key_m = FSmin_m
        embezzle = True
    elif key_response_m in Gmin_N:
        key_m = Gmin_m
        embezzle = True
    elif key_response_m in GSmin_N or key_response_m in AFmin_N:
        key_m = GSmin_m
        embezzle = True
    elif key_response_m in Amin_N:
        key_m = Amin_m
        embezzle = True
    elif key_response_m in ASmin_N or key_response_m in BFmin_N:
        key_m = ASmin_m
        embezzle = True
    elif key_response_m in Bmin_N:
        key_m = Bmin_m
        embezzle = True
    else:
        print ('\nSorry, I did not understand that, I can only write in minor and major keys. I may know the key you are trying to write in by another name.\n')
##############################################
    if mode_r == "ionian" or mode_r == "": #changes the mode if necessary
        mode = ionian
    elif mode_r == "dorian":
        mode = dorian
    elif mode_r == "phrygian":
        mode = phrygian
    elif mode_r == "lydian":
        mode = lydian
    elif mode_r == "mixolydian":
        mode = mixolydian
    elif mode_r == "aeolian":
        mode = aeolian
    elif mode_r == "locrian":
        mode = locrian

    key_m = rotate(key_m, mode)
##############################################
    starter = random.randint(1,3)#picks the first note from the tonic chord

    if starter == 1:
        first_note = 5
    elif starter == 2:
        first_note = 7
    elif starter == 3:
        first_note = 9

    #first_note = 7

    melodic_line.append(key_m[first_note])

    melody_money = int(money)
        
#Appending the move to the progression

    #-------------------------------------------------#

    while melody_money > 0:
            
        if melody_money <= 3:
            move = random.choice(moves_3)
        elif melody_money <= 5:
            move = random.choice(moves_2)
        elif melody_money >= 6:
            move = random.choice(moves_1)#change how much melody money is needed to buy these chunks of meledies
        
        if move == "u3u2":
            melody_money = melody_money - 2
            
            second_note = first_note + 2
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note + 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
        elif move == "d3d2":
            melody_money = melody_money - 2
            
            second_note = first_note - 2
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note - 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note  
        elif move == "d2u3":
            melody_money = melody_money - 2
            
            second_note = first_note - 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note + 2
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
        elif move == "u2d3":
            melody_money = melody_money - 2
            
            second_note = first_note + 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note - 2
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
        elif move == "u3d2":
            melody_money = melody_money - 2
            
            second_note = first_note + 2
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note - 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
        elif move == "d3u2":
            melody_money = melody_money - 2
            
            second_note = first_note - 2
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note + 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
        elif move == "d2u4d2":
            melody_money = melody_money - 3
            
            second_note = first_note - 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note + 3
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note - 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
        elif move == "u2d4u2":
            melody_money = melody_money - 3
            
            second_note = first_note + 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note - 3
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note + 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
        elif move == "d2u5d2":
            melody_money = melody_money - 3
            
            second_note = first_note - 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note + 4
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note - 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
        elif move == "u2d5u2":
            melody_money = melody_money - 3
            
            second_note = first_note + 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note - 4
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note + 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
        elif move == "d2d2u6d2":
            melody_money = melody_money - 4
            
            second_note = first_note - 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note - 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note + 5
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note - 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
        elif move == "u2u2d6u2":
            melody_money = melody_money - 4
            
            second_note = first_note + 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note + 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note - 5
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note + 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
        elif move == "d2u4u3d2":
            melody_money = melody_money - 4
            
            second_note = first_note - 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note + 3
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note + 2
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note - 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
        elif move == "u2d4d3u2":
            melody_money = melody_money - 4
            
            second_note = first_note + 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note - 3
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note - 2
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note + 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
        elif move == "d2u5u3d2":
            melody_money = melody_money - 4
            
            second_note = first_note - 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note + 4
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note + 2
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note - 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
        elif move == "u2d5d3u2":
            melody_money = melody_money - 4
            
            second_note = first_note + 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note - 4
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note - 2
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note + 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
        elif move == "d2u6d2d2":
            melody_money = melody_money - 4
            
            second_note = first_note - 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note + 5
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note - 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note - 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
        elif move == "u2d6u2u2":
            melody_money = melody_money - 4
            
            second_note = first_note + 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note - 5
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note + 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = first_note + 1
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note

        if melody_money <= 2:
            break
    #-------------------------------------------------#

    coin_flip = random.randint(0,1) #decides if the resolving notes go to the 2nd note or 7th note

    if first_note == 0 or first_note == 7 or first_note == 14:
        pass
    elif first_note == 6:
        second_note = 7
        melodic_line.append(key_m[second_note % len (key_m)])
        first_note = second_note
    elif first_note == 1:
        second_note = 0
        melodic_line.append(key_m[second_note % len (key_m)])
        first_note = second_note
    elif first_note >= 1 and first_note <= 3:
        second_note = 1
        melodic_line.append(key_m[second_note % len (key_m)])
        first_note = second_note
        second_note = 0
        melodic_line.append(key_m[second_note % len (key_m)])
        first_note = second_note
    elif first_note >= 4 and first_note <= 10:
        if coin_flip > 0:
            second_note = 6
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = 7
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
        else:
            second_note = 8
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
            second_note = 7
            melodic_line.append(key_m[second_note % len (key_m)])
            first_note = second_note
    elif first_note >= 10 and first_note < 13:
        second_note = 13
        melodic_line.append(key_m[second_note % len (key_m)])
        first_note = second_note
        second_note = 14
        melodic_line.append(key_m[second_note % len (key_m)])
        first_note = second_note
    elif first_note == 13:
        second_note = 14
        melodic_line.append(key_m[second_note % len (key_m)])
        first_note = second_note
    else:
        print("An error has occured. error code 001")

    #if embezzle == True:
    print(melodic_line[::-1])#for some reason, minor melodies sound a lot better backwards, I do not know why
    #else:
    #print(melodic_line)

    regen_m = input("regenerate? ")
    regen_m = regen_m.lower()

    if regen_m in yes: #creates a new melody with the same parameters
        melodic_line = []
        MelodyMaker_basic()
    else:
        again_m = input("Do you want another melody? ")
        again_m = again_m.lower()

        if again_m in yes:
            questions_m()
            MelodyMaker_basic()
        else:
            print("\nThank you for using MelodyMaker™ " + VERSION)
            time.sleep(2.5)
            sys.exit()






        
    
questions_m()
MelodyMaker_basic()


    

