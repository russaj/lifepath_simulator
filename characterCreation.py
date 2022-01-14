import witcherCharacter
import lifepath_easyMode
import random

#commenting this out for now as i test the other stuff below
#
# print ("Hello and welcome to the Witcher TTRP Character Creation Assistant. We will be using information from the FREE Easy Mode Document, which is a truncated version of the full Life Path process.")
# witcherCharacter.playerCharacter["Info"]["Name"] = input("Let's get started by you saying your name? \n")
# print(witcherCharacter.playerCharacter["Info"]["Name"] + ", an interesting name to be sure...")
#
# #print(lifepath_easyMode.raceChoice)
# race = input("Would you like to select your race or have it randomly selected? 'A' for Choose or 'B' for Random: \n")
# #print(race.upper())
# if race.upper() == "A":
#     print("So you shall choose...")
#     print(lifepath_easyMode.raceChoice)
#     print(witcherCharacter.playerCharacter["Info"]["Race"])
#     race = input("Which shall it be: Human, Elf, Dwarf, or Witcher?\n")
#     print(f'You entered {race.capitalize()}')
#
#     if race.capitalize() in lifepath_easyMode.raceChoice:
#         race = int(str(lifepath_easyMode.raceChoice.index(race.capitalize())));
#         print(f'You have chosen {lifepath_easyMode.raceChoice[race]}')
#         witcherCharacter.playerCharacter["Info"]["Race"] = lifepath_easyMode.raceChoice[race]
#     else:
#         print("Hmm, I don't quite recognize that.")
#         print(witcherCharacter.playerCharacter["Info"])
# elif race.upper() == "B":
#     print("You shall let fate decide! Brave.")
#     #i think this might be index out of bounds, below?
#     r = random.randint(1, 4)
#     #print(r)
#     print(lifepath_easyMode.raceChoice[r])
#     witcherCharacter.playerCharacter["Info"]["Race"] = lifepath_easyMode.raceChoice[r]
#     race = witcherCharacter.playerCharacter["Info"]["Race"]
#     print(f'a {race}, a race of surprise as it were?')
# else:
#     print("Please type 'A' or 'B'.")

print(witcherCharacter.playerCharacter["Info"])

print(f'Well, {witcherCharacter.playerCharacter["Info"]["Name"]}, now we must select rawStatNums.')
rawStatNums = []
actualStats = {} #combine the 2 lists into a dictionary
#randomly select numbers for 9 rawStatNums, rerolling 1's and 2's
for i in range(0,9):
    n = random.randint(3,9)
    rawStatNums.append(n)
print('The dice have been rolled. These are the numbers you get to choose from!')
print(rawStatNums)

i = 0
#cycle through rawStatNums list using User input to add specific number to Stat in character dictionary.
#while i <= 9:
#    for i in rawStatNums:
#        statChoice = input(f'where should {rawStatNums[i]} go? \n')
#        if statChoice.upper() in lifepath_easyMode.rawStatNums:
#            print(rawStatNums[i])
#            print(f'You have chosen {rawStatNums[i]} for {statChoice}')
#            witcherCharacter.playerCharacter["Stats"][statChoice] = int(rawStatNums[i])
#            #remove specific stat from list once it has be selected.
#            del rawStatNums[i]
#            print(rawStatNums)
#        else:
#            print("Hmm, I don't quite recognize that.")
#        #show current breakdown of selected rawStatNums
#        print(witcherCharacter.playerCharacter["Stats"])
#        i = i + 1
#    break
#print(f'How do these look? {witcherCharacter.playerCharacter["Stats"]}')
#dictionary version still needs to have numbers removed from rawStatNums list
counter = 0
print(f'Your currents rawStatNums are: {witcherCharacter.playerCharacter["Stats"]}, \n You got to start somewhere, I suppose.')
while counter <= 9: #changing to < as opposed to <=, otherwise indexoutofrange
    print('TEST, what is counter at: ' + str(counter))
    print('TEST of counter, should start at pos 1: ' + str(rawStatNums[counter]))
    while True: #trying to deal with bad input
        statChoice = input(f'where should {rawStatNums[counter]} go? \n')
        if statChoice.upper() in witcherCharacter.StatsAsList:
            #print(rawStatNums[counter])
            print(f'You have chosen {rawStatNums[counter]} for {statChoice}')
            witcherCharacter.playerCharacter["Stats"][statChoice] = int(rawStatNums[counter])
            statRemove = rawStatNums[counter]
            rawStatNums.remove(statRemove)
            witcherCharacter.StatsAsList.remove(statChoice.upper())
            print('Stats that still need to be filled out: ')
            print(witcherCharacter.StatsAsList)
            print("stat number choices remaining: ")
            print(rawStatNums)
            counter = counter + 1
            print(witcherCharacter.playerCharacter["Stats"])
            break
        print('Have ye no brains? Enter a proper stat, you fool!')




#trying to randomly select from a list in lifepath_easyMode
#famFateLength = len(lifepath_easyMode.familiarFateRoll)
#print('TEST, how many familiar fate rolls: ' + str(famFateLength))
#r =random.randint(1, (famFateLength-1))
#print('TEST, the random number is: ' + str(r))
#yourFamilyFate = lifepath_easyMode.familiarFateRoll[r]
#print('Your family\'s fate:')
#print(yourFamilyFate)
#where should we store this?
#print("BEFORE TEST: " + witcherCharacter.playerCharacter["lifePath"]["Familial Fate"])
#witcherCharacter.playerCharacter["lifePath"]["Familial Fate"] = yourFamilyFate
#print("AFTER TEST: " + (witcherCharacter.playerCharacter["lifePath"]["Familial Fate"]))

#parentsFateLength = len(lifepath_easyMode.parentalFateRoll)
#r2 = random.randint(1, (parentsFateLength-1))
#print('TEST, the random number is: ' + str(r2))
#yourParentsFate = lifepath_easyMode.parentalFateRoll[r2]
#print('Your parent\'s fate:')
#print(yourParentsFate)
#where should we store this?
#print("BEFORE TEST: " + witcherCharacter.playerCharacter["lifePath"]["Parental Fate"])
#witcherCharacter.playerCharacter["lifePath"]["Parental Fate"] = yourParentsFate
#print("AFTER TEST: " + witcherCharacter.playerCharacter["lifePath"]["Parental Fate"])

#famStatusLength = len(lifepath_easyMode.familyStatus)
#r3 = random.randint(1, (famStatusLength-1))
#yourFamStatus= lifepath_easyMode.familyStatus[r3]
#print('Your family\'s status:')
#print(yourFamStatus)
#where should we store this?
#print("BEFORE TEST: " + witcherCharacter.playerCharacter["lifePath"]["Family Status"])
#witcherCharacter.playerCharacter["lifePath"]["Family Status"] = yourFamStatus
#print("AFTER TEST: " + witcherCharacter.playerCharacter["lifePath"]["Family Status"])
