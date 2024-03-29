from itertools import permutations
import os
import random
import sys

def banner(bannernum):
    if bannernum==0:
        print("""
                .██╗    ██╗ ██████╗ ██████╗ ██████╗       ██╗     
                .██║    ██║██╔═══██╗██╔══██╗██╔══██╗      ██║     
                .██║ █╗ ██║██║   ██║██████╔╝██║  ██║█████╗██║     
                .██║███╗██║██║   ██║██╔══██╗██║  ██║╚════╝██║     
                .╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝      ███████╗
                ..╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝       ╚══════╝""")
    elif bannernum==1:
        print("""
                .                                        █████            █████      
                .                                       ░░███            ░░███       
                ..█████ ███ █████  ██████  ████████   ███████             ░███       
                .░░███ ░███░░███  ███░░███░░███░░███ ███░░███  ██████████ ░███       
                ..░███ ░███ ░███ ░███ ░███ ░███ ░░░ ░███ ░███ ░░░░░░░░░░  ░███       
                ..░░███████████  ░███ ░███ ░███     ░███ ░███             ░███      █
                ...░░████░████   ░░██████  █████    ░░████████            ███████████
                ....░░░░ ░░░░     ░░░░░░  ░░░░░      ░░░░░░░░            ░░░░░░░░░░░ 
                                                                    """)
    elif bannernum==2:
        print("""
                .:::       :::  ::::::::  :::::::::  :::::::::                :::        
                .:+:       :+: :+:    :+: :+:    :+: :+:    :+:               :+:        
                .+:+       +:+ +:+    +:+ +:+    +:+ +:+    +:+               +:+        
                .+#+  +:+  +#+ +#+    +:+ +#++:++#:  +#+    +:+ +#++:++#++:++ +#+        
                .+#+ +#+#+ +#+ +#+    +#+ +#+    +#+ +#+    +#+               +#+        
                ..#+#+# #+#+#  #+#    #+# #+#    #+# #+#    #+#               #+#        
                ...###   ###    ########  ###    ### #########                ########## """)
    elif bannernum==3:
        print("""                                 
                        ..:                ED.                               
                        .t#,               E#Wi                              
                        ;##W.   j.         E###G.                        i   
            ;          :#L:WE   EW,        E#fD#W;                      LE   
        ...DL         .KG  ,#D  E##j       E#t t##L                    L#E   
..f.     :K#L     LWL EE    ;#f E###D.     E#t  .E#K,                 G#W.   
..EW:   ;W##L   .E#f f#.     t#iE#jG#W;    E#t    j##f  .......      D#K.    
..E#t  t#KE#L  ,W#;  :#G     GK E#t t##f   E#t    :E#K: GEEEEEEf.   E#K.     
..E#t f#D.L#L t#K:    ;#L   LW. E#t  :K#E: E#t   t##L             .E#E.      
..E#jG#f  L#LL#G       t#f f#:  E#KDDDD###iE#t .D#W;             .K#E        
..E###;   L###j         f#D#;   E#f,t#Wi,,,E#tiW#G.             .K#D         
..E#K:    L#W;           G#t    E#t  ;#W:  E#K##i              .W#G          
..EG      LE.             t     DWi   ,KK: E##D.              :W##########Wt 
..;       ;@                               E#t                :,,,,,,,,,,,,,.
                                        ...L:                                """)
    else:
        print("""
                                                                    
@@@  @@@  @@@   @@@@@@   @@@@@@@   @@@@@@@              @@@       
@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@             @@@       
@@!  @@!  @@!  @@!  @@@  @@!  @@@  @@!  @@@             @@!       
!@!  !@!  !@!  !@!  @!@  !@!  @!@  !@!  @!@             !@!       
@!!  !!@  @!@  @!@  !@!  @!@!!@!   @!@  !@!  @!@!@!@!@  @!!       
!@!  !!!  !@!  !@!  !!!  !!@!@!    !@!  !!!  !!!@!@!!!  !!!       
!!:  !!:  !!:  !!:  !!!  !!: :!!   !!:  !!!             !!:       
:!:  :!:  :!:  :!:  !:!  :!:  !:!  :!:  !:!              :!:      
.:::: :: :::   ::::: ::  ::   :::   :::: ::              :: ::::  
..:: :  : :     : :  :    :   : :  :: :  :              : :: : :  
                                                                """)

def bannernummaker():
    return random.randint(0,4)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def nooutput():
    keywordstr=sys.argv[2]
    keywordlist=keywordstr.split(",")
    iterwordlist=permutations(keywordlist)

    wordlist=[]
    for i in iterwordlist:
        str=''
        for item in i:
            str=str+item
            wordlist.append(str)
    
    for i in wordlist:
        print(i)

def cli():
    banner(bannernummaker())

    #takin keywords as string
    print("usage: word1,word2,word3,...")
    keywordstr=input("keywords\n>>>")
    saveloc=input("save location\nex: ./wordlist.txt\n>>>")
    clear()

    #adding keywords to keywordlist with split
    keywordlist=keywordstr.split(",")
    #doing permutation
    iterwordlist=permutations(keywordlist)

    #after permutation adding elements from iterwordlist to wordlist
    wordlist=[]
    for i in iterwordlist:
        str=''
        for item in i:
            str=str+item
            wordlist.append(str)

    #for i in wordlist:
    #    print(i)

    #writing everythin into wordlist.txt file
    with open(saveloc,"w",encoding="utf-8") as file:
        for i in wordlist:
            file.write(i+"\n")
    print("Thank you for choosing us. Have a good day sir.")


if "-h" in sys.argv or "--help" in sys.argv:
    print("""
USAGE:
        python3 word-L.py                            open cli and save wordlist as text
        python3 word-L.py -h                         open this help page
        python3 word-L.pt -w word1,word2,word3...    print all the outputs to the terminal""")
elif "-w" in sys.argv:
    nooutput()
else:
    cli()