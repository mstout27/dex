# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 18:14:40 2016

@author: Matt Stout
"""

import requests

class Pokemon():
    fullName = ''
    type1 = ''
    type2 = ''
    
    total = ''
    hp = ''
    atk = ''
    defs = ''
    spatk = ''
    spdefs = ''
    spd = ''
    
    
    
    #Default weaknesses
    normal = 1
    fire = 1
    water = 1
    electric = 1
    grass = 1
    ice = 1
    fighting = 1
    poison = 1
    ground = 1
    flying = 1
    psychic = 1
    bug = 1
    rock = 1
    ghost = 1
    dragon = 1
    dark = 1
    steel = 1
    fairy = 1
    weakArr = [1] * 18 #array of all weaknesses
    
    def __init__(self,name,firstType,secondType,totalStats,health,attack,defense,specialAttack,specialDefense,speed):
        self.fullName = name
        self.type1 = firstType
        self.type2 = secondType
        self.total = totalStats
        self.hp = health
        self.atk = attack
        self.defs = defense
        self.spatk = specialAttack
        self.spdefs = specialDefense
        self.spd = speed
        
class Maker():
    increment  = 0
    pokearr = []
    file = requests.get('http://pokemondb.net/pokedex/all')
    data = file.text[10000:]


        
        
        
#MAIN PROGRAM: inputs in team of six pokemon, outputs based on type, stats and fills an archetype for a competitive team structure
    def counterPick(mon1,mon2,mon3,mon4,mon5,mon6): #DIJKSTRA'S ALGORITHM
        
        #first, determines counterpick based on type advantages
        weak1 = Maker.weaknesses(mon1.type1,mon1.type2)
        weak2 = Maker.weaknesses(mon2.type1,mon2.type2)
        weak3 = Maker.weaknesses(mon3.type1,mon3.type2)
        weak4 = Maker.weaknesses(mon4.type1,mon4.type2)
        weak5 = Maker.weaknesses(mon5.type1,mon5.type2)
        weak6 = Maker.weaknesses(mon6.type1,mon6.type2)
#        print(weak1)
#        print(weak2)
#        print(weak3)
#        print(weak4)
#        print(weak5)
#        print(weak6)
        superWeaks = [1] *18
        for i in range(18):
            superWeaks[i] = [weak1[i][0], (weak1[i][1] * weak2[i][1] * weak3[i][1] * weak4[i][1] * weak5 [i][1] * weak6[i][1])]
        #multiplies all weaknesses into one array of team weaknesses
#        print(superWeaks)
        
        
        Maker.findAll() #makes full array of all 721 pokemon in Maker.pokearr
        
        #competitive archetypes
        physSweeps = [] #physical sweeper: high attack, high speed
        spSweeps= [] #special sweeper: high special attack, high speed
        physTanks = [] #physical tank: high defense
        spTanks = [] #special tank: high special defense
        walls = [] # wall: high hitpoints, decent defense or special defense
        batPassers = [] #baton passer: any pokemon capable of properly utilizing the move 'baton pass' to improve the capabilities of the rest of the team

        for i in range(721):
            name = Maker.pokearr[i].fullName
            weightType1 = Maker.pokearr[i].type1
            weightType2 = Maker.pokearr[i].type2
            weight = 1
            for j in range(0,18):
                if (weightType1 == superWeaks[j][0]):
                    weight *= superWeaks[j][1]
                elif (weightType2 != ''):
                    if (weightType2 == superWeaks[j][0]):
                        weight *= superWeaks[j][1]             #weight variable now considers type       
            weight *= (float(Maker.pokearr[i].total)/720.0)    #weight variable now considers type and overall statistics   
            
            if(int(Maker.pokearr[i].spd) > 80 and int(Maker.pokearr[i].atk) > 110):
                physSweeps.append([name,weight])
            if(int(Maker.pokearr[i].spd) > 80 and int(Maker.pokearr[i].spatk) > 110):
                spSweeps.append([name,weight])
            if(int(Maker.pokearr[i].defs) > 110):
                physTanks.append([name,weight])
            if(int(Maker.pokearr[i].spdefs) > 110):
                spTanks.append([name,weight])
            if((int(Maker.pokearr[i].hp) > 110) and (int(Maker.pokearr[i].hp) + int(Maker.pokearr[i].defs) or int(Maker.pokearr[i].spdefs) > 185)):
                walls.append([name,weight])  
            if(name == 'venomoth' or name == 'hypno' or name == 'mr-mime' or name == 'scyther' or name == 'vaporeon' or name == 'jolteon' or name == 'zapdos' or name == 'ledian' or name == 'ariados' or name == 'espeon' or name == 'umbreon' or name == 'scizor' or name == 'smeargle' or name == 'celebi' or name == 'blaziken' or name == 'ninjask' or name == 'lunatone' or name == 'solrock' or name == 'absol' or name == 'gorebyss' or name == 'floatzel' or name == 'ambipom' or name == 'drifblim' or name == 'lopunny' or name == 'togekiss' or name == 'leafeon' or name == 'gliscor' or name == 'scolipede'):
                batPassers.append([name,weight])
                #fills out competitive possibilities, team will consist of one of each 
                
#########       #(let pokemon be in more than one array, just to interconnect graph of vertices)   
               
            
        Maker.insertionSort(physSweeps) #ADJUST MERGESORT FOR 2D ARRAYS?
        Maker.insertionSort(spSweeps) 
        Maker.insertionSort(physTanks) 
        Maker.insertionSort(spTanks) 
        Maker.insertionSort(walls) 
        Maker.insertionSort(batPassers) #puts best pokemon at end of arrays       
        
#        print('PHYS SWEEPS:')
#        print(physSweeps)
#        print('\n')
#        print('SP SWEEPS:')
#        print(spSweeps)
#        print('\n')
#        print('PHYS TANKS:')
#        print(physTanks)
#        print('\n')
#        print('SP TANKS:')
#        print(spTanks)
#        print('\n')
#        print('WALLS:')
#        print(walls)
#        print('\n')
#        print('BAT PASSERS:')
#        print(batPassers)
#        print('\n')             
#        
    
        counterMon1 = physSweeps[len(physSweeps)-1][0] #makes final phsySweep, no duplicates
                                 
        counterMon2 = spSweeps[len(spSweeps)-1][0]
        a = 2
        while(counterMon2 == counterMon1):
            counterMon2 = spSweeps[len(spSweeps)-a][0] #makes final spSweep, no duplicates
            a += 1
                           
        b = 2
        counterMon3 = physTanks[len(physTanks)-1][0]
        while(counterMon3 == counterMon1 or counterMon3 == counterMon2):     
            counterMon3 = physTanks[len(physTanks)-b][0]    #makes final phsyTank, no duplicates
            b+=1
            
        c = 2           
        counterMon4 = spTanks[len(spTanks)-1][0]
        while(counterMon4 == counterMon1 or counterMon4 == counterMon2 or counterMon4 == counterMon3):     
            counterMon4 = spTanks[len(spTanks)-c][0]        #makes final spTank, no duplicates
            c+=1
                              
        d = 2
        counterMon5 = walls[len(walls)-1][0]
        while(counterMon5 == counterMon1 or counterMon5 == counterMon2 or counterMon5 == counterMon3 or counterMon5 == counterMon4):     
            counterMon5 = walls[len(walls)-d][0]    #makes final wall, no duplicates
            d+=1
                            
        e = 2
        counterMon6 = batPassers[len(batPassers)-1][0]
        while(counterMon6 == counterMon1 or counterMon6 == counterMon2 or counterMon6 == counterMon3 or counterMon6 == counterMon4 or counterMon6 == counterMon4):     
            counterMon6 = batPassers[len(batPassers)-e][0]    #makes final batPasser, no duplicates
            e+=1
                                 
                                 
        finalCounterTeam = [counterMon1,counterMon2,counterMon3,counterMon4,counterMon5,counterMon6]
        Maker.increment = 0
        print('Best counter team:')
        return(finalCounterTeam)

################DEPTH FIRST SEARCH: bad algorithm to use, doesn't make any sense to use with my data and intended program output       
        def counterPickDFS(mon1,mon2,mon3,mon4,mon5,mon6): 
            #first, determines counterpick based on type advantages
            weak1 = Maker.weaknesses(mon1.type1,mon1.type2)
            weak2 = Maker.weaknesses(mon2.type1,mon2.type2)
            weak3 = Maker.weaknesses(mon3.type1,mon3.type2)
            weak4 = Maker.weaknesses(mon4.type1,mon4.type2)
            weak5 = Maker.weaknesses(mon5.type1,mon5.type2)
            weak6 = Maker.weaknesses(mon6.type1,mon6.type2)
    #        print(weak1)
    #        print(weak2)
    #        print(weak3)
    #        print(weak4)
    #        print(weak5)
    #        print(weak6)
            superWeaks = [1] *18
            for i in range(18):
                superWeaks[i] = [weak1[i][0], (weak1[i][1] * weak2[i][1] * weak3[i][1] * weak4[i][1] * weak5 [i][1] * weak6[i][1])]
            #multiplies all weaknesses into one array of team weaknesses
    #        print(superWeaks)
            
            
            Maker.findAll() #makes full array of all 721 pokemon in Maker.pokearr
            
            #competitive archetypes
            physSweeps = [] #physical sweeper: high attack, high speed
            spSweeps= [] #special sweeper: high special attack, high speed
            physTanks = [] #physical tank: high defense
            spTanks = [] #special tank: high special defense
            walls = [] # wall: high hitpoints, decent defense or special defense
            batPassers = [] #baton passer: any pokemon capable of properly utilizing the move 'baton pass' to improve the capabilities of the rest of the team
    
            for i in range(721):
                name = Maker.pokearr[i].fullName
                weightType1 = Maker.pokearr[i].type1
                weightType2 = Maker.pokearr[i].type2
                weight = 1
                for j in range(0,18):
                    if (weightType1 == superWeaks[j][0]):
                        weight *= superWeaks[j][1]
                    elif (weightType2 != ''):
                        if (weightType2 == superWeaks[j][0]):
                            weight *= superWeaks[j][1]             #weight variable now considers type       
                weight *= (float(Maker.pokearr[i].total)/720.0)    #weight variable now considers type and overall statistics   
                
                if(int(Maker.pokearr[i].spd) > 80 and int(Maker.pokearr[i].atk) > 110):
                    physSweeps.append([name,weight])
                if(int(Maker.pokearr[i].spd) > 80 and int(Maker.pokearr[i].spatk) > 110):
                    spSweeps.append([name,weight])
                if(int(Maker.pokearr[i].defs) > 110):
                    physTanks.append([name,weight])
                if(int(Maker.pokearr[i].spdefs) > 110):
                    spTanks.append([name,weight])
                if((int(Maker.pokearr[i].hp) > 110) and (int(Maker.pokearr[i].hp) + int(Maker.pokearr[i].defs) or int(Maker.pokearr[i].spdefs) > 185)):
                    walls.append([name,weight])  
                if(name == 'venomoth' or name == 'hypno' or name == 'mr-mime' or name == 'scyther' or name == 'vaporeon' or name == 'jolteon' or name == 'zapdos' or name == 'ledian' or name == 'ariados' or name == 'espeon' or name == 'umbreon' or name == 'scizor' or name == 'smeargle' or name == 'celebi' or name == 'blaziken' or name == 'ninjask' or name == 'lunatone' or name == 'solrock' or name == 'absol' or name == 'gorebyss' or name == 'floatzel' or name == 'ambipom' or name == 'drifblim' or name == 'lopunny' or name == 'togekiss' or name == 'leafeon' or name == 'gliscor' or name == 'scolipede'):
                    batPassers.append([name,weight])
                    #fills out competitive possibilities, team will consist of one of each 
                    
    #########       #(let pokemon be in more than one array, just to interconnect graph of vertices)   
                   
                
            Maker.insertionSort(physSweeps) 
            Maker.insertionSort(spSweeps) 
            Maker.insertionSort(physTanks) 
            Maker.insertionSort(spTanks) 
            Maker.insertionSort(walls) 
            Maker.insertionSort(batPassers) #puts best pokemon at end of arrays       
            
    #        print('PHYS SWEEPS:')
    #        print(physSweeps)
    #        print('\n')
    #        print('SP SWEEPS:')
    #        print(spSweeps)
    #        print('\n')
    #        print('PHYS TANKS:')
    #        print(physTanks)
    #        print('\n')
    #        print('SP TANKS:')
    #        print(spTanks)
    #        print('\n')
    #        print('WALLS:')
    #        print(walls)
    #        print('\n')
    #        print('BAT PASSERS:')
    #        print(batPassers)
    #        print('\n')             
    #        
        
             #makes final phsySweep, no duplicates
                                     
            counterMon1 = physSweeps[len(physSweeps)-1][0]
            counterMon2 = physSweeps[len(physSweeps)-2][0]                         
            counterMon3 = physSweeps[len(physSweeps)-3][0]
            counterMon4 = physSweeps[len(physSweeps)-4][0]
            counterMon5 = physSweeps[len(physSweeps)-5][0]
            counterMon6 = physSweeps[len(physSweeps)-6][0]
                                     
            finalCounterTeam = [counterMon1,counterMon2,counterMon3,counterMon4,counterMon5,counterMon6]
            Maker.increment = 0   
            print('Terrible counter team:')
            return(finalCounterTeam)
    





#Helper functions
#
#

    def insertionSort(alist): #switch to less awful sorting method later
        for index in range(1,len(alist)):
            
            currentvalue = alist[index]
            position = index
    
            while position>0 and alist[position-1][1]>currentvalue[1]:
                alist[position]=alist[position-1]
                position = position-1
    
            alist[position]=currentvalue
        return(alist)

#puts in types, gives what is supereffective/not very effective/noneffective against it  
    def weaknesses(typ,typ2):
        if(typ == 'normal'):
            Pokemon.fighting *= 2
            Pokemon.ghost *= .25
        elif(typ == 'fire'):
            Pokemon.water *= 2
            Pokemon.rock *= 2
            Pokemon.ground *= 2
            Pokemon.fire *= .5
            Pokemon.grass *= .5
            Pokemon.ice *= .5
            Pokemon.bug  *= .5
            Pokemon.steel *= .5
            Pokemon.fairy *= .5
        elif(typ == 'water'):
            Pokemon.electric *= 2
            Pokemon.grass *= 2
            Pokemon.fire *= .5
            Pokemon.water *= .5
            Pokemon.ice *= .5
            Pokemon.steel *= .5
        elif(typ == 'electric'):
            Pokemon.ground *= 2
            Pokemon.electric *= .5
            Pokemon.steel *= .5
        elif(typ == 'grass'):
            Pokemon.fire *= 2
            Pokemon.ice *= 2
            Pokemon.bug *= 2
            Pokemon.poison *= 2
            Pokemon.flying *= 2
            Pokemon.water *= .5
            Pokemon.electric *= .5
            Pokemon.grass *= .5
            Pokemon.ground *= .5
        elif(typ== 'ice'):
            Pokemon.fire *= 2
            Pokemon.fighting *= 2
            Pokemon.rock *= 2
            Pokemon.steel *= 2
            Pokemon.ice *=.5
        elif(typ== 'fighting'):
            Pokemon.psychic *= 2
            Pokemon.flying *= 2
            Pokemon.fairy *= 2
            Pokemon.bug *= .5
            Pokemon.rock *= .5
            Pokemon.dark *= .5
        elif(typ== 'poison'):
            Pokemon.ground *= 2
            Pokemon.psychic *= 2
            Pokemon.grass *= .5
            Pokemon.fighting *= .5
            Pokemon.poison *= .5
            Pokemon.bug *= .5
            Pokemon.fairy *= .5
        elif(typ== 'ground'):
            Pokemon.water *= 2
            Pokemon.grass *= 2
            Pokemon.ice *= 2 
            Pokemon.electric *= .25
            Pokemon.poison *= .5
            Pokemon.rock *= .5
        elif(typ== 'flying'):
            Pokemon.electric *= 2
            Pokemon.rock *= 2
            Pokemon.ice *= 2
            Pokemon.ground *= .25
            Pokemon.grass *= .5
            Pokemon.fighting *= .5
        elif(typ== 'psychic'):
            Pokemon.bug *=2
            Pokemon.ghost *=2
            Pokemon.dark *= 2
            Pokemon.fighting *= .5
            Pokemon.psychic *= .5
        elif(typ== 'bug'):
            Pokemon.fire *= 2
            Pokemon.flying *= 2
            Pokemon.rock *= 2
            Pokemon.grass *= .5
            Pokemon.fighting *= .5
            Pokemon.ground *= .5
        elif(typ== 'rock'):
            Pokemon.water *= 2
            Pokemon.grass *= 2
            Pokemon.fighting *= 2
            Pokemon.steel *= 2
            Pokemon.normal *= .5
            Pokemon.fire *= .5
            Pokemon.poison *= .5
            Pokemon.flying *= .5
        elif(typ== 'ghost'):
            Pokemon.ghost *= 2
            Pokemon.dark *= 2
            Pokemon.normal *= .25
            Pokemon.fighting *= .25
            Pokemon.poison *= .5
            Pokemon.bug *= .5
        elif(typ== 'dragon'):
            Pokemon.dragon *= 2
            Pokemon.ice *= 2
            Pokemon.fairy *= 2
            Pokemon.fire *= .5
            Pokemon.water *= .5
            Pokemon.electric *= .5
            Pokemon.grass *= .5
        elif(typ== 'dark'):
            Pokemon.fighting *= 2
            Pokemon.bug *= 2
            Pokemon.fairy *= 2
            Pokemon.psychic *= .25
            Pokemon.ghost *= .5
            Pokemon.dark *= .5
        elif(typ== 'steel'):
            Pokemon.fire *= 2
            Pokemon.fighting *= 2
            Pokemon.ground *= 2
            Pokemon.normal *= .5
            Pokemon.grass *= .5
            Pokemon.ice *= .5
            Pokemon.flying *= .5
            Pokemon.psychic *= .5
            Pokemon.bug = .5
            Pokemon.rock *= .5
            Pokemon.dragon *= .5
            Pokemon.steel *= .5
            Pokemon.fairy *= .5
            Pokemon.poison *= .25
        elif(typ== 'fairy'):
            Pokemon.poison *= 2
            Pokemon.steel *= 2
            Pokemon.fighting *= .5
            Pokemon.bug *= .5
            Pokemon.dark *= .5
            Pokemon.dragon *= .25
        #changes vals of all types' effect on inputted type1

        Pokemon.weakArr = [['normal', Pokemon.normal],['fire',Pokemon.fire],['water',Pokemon.water],['electric',Pokemon.electric],['grass',Pokemon.grass],['ice',Pokemon.ice],['fighting',Pokemon.fighting],['poison',Pokemon.poison],['ground',Pokemon.ground],['flying',Pokemon.flying],['psychic',Pokemon.psychic],['bug',Pokemon.bug],['rock',Pokemon.rock],['ghost',Pokemon.ghost],['dragon',Pokemon.dragon],['dark',Pokemon.dark],['steel',Pokemon.steel],['fairy',Pokemon.fairy]]  
        
        if(typ2 != ''):
            Maker.weaknesses(typ2, '')
        
        Pokemon.normal = 1
        Pokemon.fire = 1
        Pokemon.water = 1
        Pokemon.electric = 1
        Pokemon.grass = 1
        Pokemon.ice = 1
        Pokemon.fighting = 1
        Pokemon.poison = 1
        Pokemon.ground = 1
        Pokemon.flying = 1
        Pokemon.psychic = 1
        Pokemon.bug = 1
        Pokemon.rock = 1
        Pokemon.ghost = 1
        Pokemon.dragon = 1
        Pokemon.dark = 1
        Pokemon.steel = 1
        Pokemon.fairy = 1
        return(Pokemon.weakArr)



#dexNo = 001, 002, 003 etc
    #creates 1-99
    def find(dexNo):
        if (dexNo in Maker.data):
            #NAMEFIND
            while(Maker.data[Maker.increment :Maker.increment +3] != dexNo):
                Maker.increment  += 1
            #brings Maker.increment  to index of first digit of dexNo
            nameStart = Maker.increment  + 73
            fullName = ""
            while (Maker.data[nameStart] != '"'):
                fullName += Maker.data[nameStart]
                nameStart += 1
            #Maker.increment  now at last letter of name 
            #fullName now equals name
                
            #TYPEFIND
            type1 = ''
            while(Maker.data[Maker.increment :Maker.increment +15] != 'type-icon type-'):
                Maker.increment  += 1
            #brings Maker.increment  to first letter of "type-icon type-etc"
            Maker.increment  += 15
            while (Maker.data[Maker.increment ] != '"'):
                type1 += Maker.data[Maker.increment ]
                Maker.increment  += 1   
            #typeStart now at last letter of type1
            #type1 now equals first type
            
            #TYPEFIND2
            type2 = '' 
            if(Maker.data[Maker.increment + 28 + 2*len(type1)] == ' '):
                Maker.increment  +=1
                while(Maker.data[Maker.increment :Maker.increment +15] != 'type-icon type-'):
                    Maker.increment  += 1
                #brings Maker.increment  to first letter of "type-ico type-etc"
                typeStart2 = Maker.increment  + 15 
                while (Maker.data[typeStart2] != '"'):
                    type2 += Maker.data[typeStart2]
                    typeStart2 += 1 
                #type2 now equals second type, if it exists
            
            #FIND STAT TOTAL    
            total = ''
            while(Maker.data[Maker.increment :Maker.increment  +11] != 'num-total">'):
                Maker.increment  += 1   
            Maker.increment  += 11
            #brings Maker.increment  to first number of total stat
            while(Maker.data[Maker.increment ] != '<'):
                total += Maker.data[Maker.increment ]
                Maker.increment  += 1
            #total stats now complete
            
            #FIND HP
            hp = ''
            while(Maker.data[Maker.increment :Maker.increment  +5] != 'num">'):
                Maker.increment  += 1
            Maker.increment  += 5
            #brings Maker.increment  to first number of hp stat
            while(Maker.data[Maker.increment ] != '<'):
                hp += Maker.data[Maker.increment ]
                Maker.increment  += 1
            #hp now complete
            
            #FIND ATK
            atk = ''
            Maker.increment  += 1
            while(Maker.data[Maker.increment :Maker.increment  +5] != 'num">'):
                Maker.increment  += 1
            Maker.increment  += 5
            #brings Maker.increment  to first number of hp stat
            while(Maker.data[Maker.increment ] != '<'):
                atk += Maker.data[Maker.increment ]
                Maker.increment  += 1
            
            #FIND DEFS
            defs = ''
            Maker.increment  += 1
            while(Maker.data[Maker.increment :Maker.increment  +5] != 'num">'):
                Maker.increment  += 1
            Maker.increment  += 5
            #brings Maker.increment  to first number of hp stat
            while(Maker.data[Maker.increment ] != '<'):
                defs += Maker.data[Maker.increment ]
                Maker.increment  += 1
            
            #FIND SPATK
            spatk = ''
            Maker.increment  += 1
            while(Maker.data[Maker.increment :Maker.increment  +5] != 'num">'):
                Maker.increment  += 1
            Maker.increment  += 5
            #brings Maker.increment  to first number of hp stat
            while(Maker.data[Maker.increment ] != '<'):
                spatk += Maker.data[Maker.increment ]
                Maker.increment  += 1
                
            #FIND SPDEFS      
            spdefs = ''
            Maker.increment  += 1
            while(Maker.data[Maker.increment :Maker.increment  +5] != 'num">'):
                Maker.increment  += 1
            Maker.increment  += 5
            #brings Maker.increment  to first number of hp stat
            while(Maker.data[Maker.increment ] != '<'):
                spdefs += Maker.data[Maker.increment ]
                Maker.increment  += 1    
            
            #FIND SPD
            spd = ''
            Maker.increment  += 1
            while(Maker.data[Maker.increment :Maker.increment  +5] != 'num">'):
                Maker.increment  += 1
            Maker.increment  += 5
            #brings Maker.increment  to first number of hp stat
            while(Maker.data[Maker.increment ] != '<'):
                spd += Maker.data[Maker.increment ]
                Maker.increment  += 1
                
                
        fullPokemon = Pokemon(fullName,type1,type2,total,hp,atk,defs,spatk,spdefs,spd)
        return (fullPokemon)
        
        
        
    #creates 100-729
    def find2(dexNo):
        if (dexNo in Maker.data):
            while(Maker.data[Maker.increment :Maker.increment +3] != dexNo):
                Maker.increment  += 1
            Maker.increment  += 1
            while(Maker.data[Maker.increment :Maker.increment +3] != dexNo):
                Maker.increment  += 1
            #brings Maker.increment  to index of first digit of dexNo
            Maker.increment  += 1
            while(Maker.data[Maker.increment :Maker.increment +3] != dexNo):
                Maker.increment  += 1
            nameStart = Maker.increment  + 73
            fullName = ""
            while (Maker.data[nameStart] != '"'):
                fullName += Maker.data[nameStart]
                nameStart += 1
            #Maker.increment  now at last letter of name 
            #fullName now equals name

            #TYPEFIND
            type1 = ''
            while(Maker.data[Maker.increment :Maker.increment +15] != 'type-icon type-'):
                Maker.increment  += 1 
            #brings Maker.increment  to first letter of "type-icon type-etc"
            typeStart = Maker.increment  + 15
            while (Maker.data[typeStart] != '"'):
                type1 += Maker.data[typeStart]
                typeStart += 1     
            #typeStart now at last letter of type1
            #type1 now equals first type
            
            #TYPEFIND2
            type2 = '' 
            if(Maker.data[typeStart+ 28 + 2*len(type1)] == ' '):
                Maker.increment  +=1
                while(Maker.data[Maker.increment :Maker.increment +15] != 'type-icon type-'):
                    Maker.increment  += 1
                #brings Maker.increment  to first letter of "type-icon type-etc"
                typeStart2 = Maker.increment  + 15
                while (Maker.data[typeStart2] != '"'):
                    type2 += Maker.data[typeStart2]
                    typeStart2 += 1   
                #type2 now equals second type, if it exists
            #FIND STAT TOTAL    
            total = ''
            while(Maker.data[Maker.increment :Maker.increment  +11] != 'num-total">'):
                Maker.increment  += 1   
            Maker.increment  += 11
            #brings Maker.increment  to first number of total stat
            while(Maker.data[Maker.increment ] != '<'):
                total += Maker.data[Maker.increment ]
                Maker.increment  += 1
            #total stats now complete
            
            #FIND HP
            hp = ''
            while(Maker.data[Maker.increment :Maker.increment  +5] != 'num">'):
                Maker.increment  += 1
            Maker.increment  += 5
            #brings Maker.increment  to first number of hp stat
            while(Maker.data[Maker.increment ] != '<'):
                hp += Maker.data[Maker.increment ]
                Maker.increment  += 1
            #hp now complete
            
            #FIND ATK
            atk = ''
            Maker.increment  += 1
            while(Maker.data[Maker.increment :Maker.increment  +5] != 'num">'):
                Maker.increment  += 1
            Maker.increment  += 5
            #brings Maker.increment  to first number of hp stat
            while(Maker.data[Maker.increment ] != '<'):
                atk += Maker.data[Maker.increment ]
                Maker.increment  += 1
            
            #FIND DEFS
            defs = ''
            Maker.increment  += 1
            while(Maker.data[Maker.increment :Maker.increment  +5] != 'num">'):
                Maker.increment  += 1
            Maker.increment  += 5
            #brings Maker.increment  to first number of hp stat
            while(Maker.data[Maker.increment ] != '<'):
                defs += Maker.data[Maker.increment ]
                Maker.increment  += 1
            
            #FIND SPATK
            spatk = ''
            Maker.increment  += 1
            while(Maker.data[Maker.increment :Maker.increment  +5] != 'num">'):
                Maker.increment  += 1
            Maker.increment  += 5
            #brings Maker.increment  to first number of hp stat
            while(Maker.data[Maker.increment ] != '<'):
                spatk += Maker.data[Maker.increment ]
                Maker.increment  += 1
                
            #FIND SPDEFS      
            spdefs = ''
            Maker.increment  += 1
            while(Maker.data[Maker.increment :Maker.increment  +5] != 'num">'):
                Maker.increment  += 1
            Maker.increment  += 5
            #brings Maker.increment  to first number of hp stat
            while(Maker.data[Maker.increment ] != '<'):
                spdefs += Maker.data[Maker.increment ]
                Maker.increment  += 1    
            
            #FIND SPD
            spd = ''
            Maker.increment  += 1
            while(Maker.data[Maker.increment :Maker.increment  +5] != 'num">'):
                Maker.increment  += 1
            Maker.increment  += 5
            #brings Maker.increment  to first number of hp stat
            while(Maker.data[Maker.increment ] != '<'):
                spd += Maker.data[Maker.increment ]
                Maker.increment  += 1
                
        fullPokemon = Pokemon(fullName,type1,type2,total,hp,atk,defs,spatk,spdefs,spd)
        return (fullPokemon)
       
    #creates kangaskhan (dexNo 115)    
    def findKang(dexNo):
        if (dexNo in Maker.data):
            while(Maker.data[Maker.increment :Maker.increment +3] != dexNo):
                Maker.increment  += 1
            Maker.increment  += 1
            while(Maker.data[Maker.increment :Maker.increment +3] != dexNo):
                Maker.increment  += 1
            #brings Maker.increment  to index of first instance of 115
            Maker.increment  += 1
            while(Maker.data[Maker.increment :Maker.increment +3] != dexNo):
                Maker.increment  += 1
            #brings Maker.increment  to index of second instance of 115
            Maker.increment  += 1
            while(Maker.data[Maker.increment :Maker.increment +3] != dexNo):
                Maker.increment  += 1
            #brings Maker.increment  to actual index of dexNo
            nameStart = Maker.increment  + 73
            fullName = ""
            while (Maker.data[nameStart] != '"'):
                fullName += Maker.data[nameStart]
                nameStart += 1
            #Maker.increment  now at last letter of name 
            #fullName now equals name
            
            #TYPEFIND
            type1 = ''
            while(Maker.data[Maker.increment :Maker.increment +15] != 'type-icon type-'):
                Maker.increment  += 1 
            #brings Maker.increment  to first letter of "type-icon type-etc"
            typeStart = Maker.increment  + 15
            while (Maker.data[typeStart] != '"'):
                type1 += Maker.data[typeStart]
                typeStart += 1     
            #typeStart now at last letter of type1
            #type1 now equals first type
            
            #TYPEFIND2
            type2 = ''
            total = '490' 
            hp = '105'
            atk = '95'
            defs = '80'
            spatk = '40'
            spdefs = '80'
            spd = '90'
            
        fullPokemon = Pokemon(fullName,type1,type2,total,hp,atk,defs,spatk,spdefs,spd)
        return (fullPokemon)
        
    def findAll():
        Maker.increment  = 0
        for i in range(721):
            if(i<9):
                Maker.pokearr.append(Maker.find('00' + str(i+1)))
            elif(i<99):
                Maker.pokearr.append(Maker.find('0' + str(i+1)))
            elif(i==114):
                Maker.pokearr.append(Maker.findKang(str(i+1)))
            else:
                Maker.pokearr.append(Maker.find2(str(i+1)))

    def main():

        teamFire = Maker.counterPick(Maker.find('004'),Maker.find('005'),Maker.find('037'),Maker.find('038'),Maker.find('077'),Maker.find('078'))
        print(teamFire) #charmander, charmeleon, vulpix, ninetales, growlithe, arcanine

        red = Maker.counterPick(Maker.find('003'),Maker.find('006'),Maker.find('009'),Maker.find('025'),Maker.find2('131'),Maker.find2('143'))
        print(red) #venusaur, charizard, blastoise, pikachu, lapras, snorlax
        
        blue = Maker.counterPick(Maker.find('028'),Maker.find('038'),Maker.find('065'),Maker.find('091'),Maker.find2('103'),Maker.find2('135'))
        print(blue) #sandslash, ninetales, alakazam, cloyster, exeggutor, jolteon
        
        stephen = Maker.counterPick(Maker.find2('227'),Maker.find2('306'),Maker.find2('344'),Maker.find2('346'),Maker.find2('348'),Maker.find2('376'))
        print(stephen) #skarmory, aggron, cradily, armaldo, claydol, metagross
     

Maker.main()