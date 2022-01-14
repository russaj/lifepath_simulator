import witcherCharacter
import lifepath_easyMode
import random

#commenting this out for now as i test the other stuff below
#
print ("Hello and welcome to the Witcher TTRP Character Creation Assistant. We will be using information from the FREE Easy Mode Document, which is a truncated version of the full Life Path process.")
witcherCharacter.playerCharacter["Info"]["Name"] = input("Let's get started by you saying your name? \n")
print(witcherCharacter.playerCharacter["Info"]["Name"] + ", an interesting name to be sure...")

#print(lifepath_easyMode.raceChoice)
race = input("Would you like to select your race or have it randomly selected? 'A' for Choose or 'B' for Random: \n")
#print(race.upper())
if race.upper() == "A":
    print("So you shall choose...")
    print(lifepath_easyMode.raceChoice)
    print(witcherCharacter.playerCharacter["Info"]["Race"])
    race = input("Which shall it be: Human, Elf, Dwarf, or Witcher?\n")
    print(f'You entered {race.capitalize()}')

    if race.capitalize() in lifepath_easyMode.raceChoice:
        race = int(str(lifepath_easyMode.raceChoice.index(race.capitalize())));
        print(f'You have chosen {lifepath_easyMode.raceChoice[race]}')
        witcherCharacter.playerCharacter["Info"]["Race"] = lifepath_easyMode.raceChoice[race]
    else:
        print("Hmm, I don't quite recognize that.")
        print(witcherCharacter.playerCharacter["Info"])
elif race.upper() == "B":
    print("You shall let fate decide! Brave.")
    r = random.randint(1, 4)
    #print(r)
    print(lifepath_easyMode.raceChoice[r])
    witcherCharacter.playerCharacter["Info"]["Race"] = lifepath_easyMode.raceChoice[r]
    race = witcherCharacter.playerCharacter["Info"]["Race"]
    print(f'a {race}, a race of surprise as it were?')
else:
    print("Please type 'A' or 'B'.")

print(witcherCharacter.playerCharacter["Info"])

print(f'Well, {witcherCharacter.playerCharacter["Info"]["Name"]}, now we must select stats.')
stats = []
#randomly select numbers for 9 stats, rerolling 1's and 2's
for i in range(0,9):
    n = random.randint(3,9)
    stats.append(n)
print(stats)

i = 0
#cycle through stats list using User input to add specific number to Stat in character dictionary.
#while i <= 9:
#    for i in stats:
#        statChoice = input(f'where should {stats[i]} go? \n')
#        if statChoice.upper() in lifepath_easyMode.stats:
#            print(stats[i])
#            print(f'You have chosen {stats[i]} for {statChoice}')
#            witcherCharacter.playerCharacter["Stats"][statChoice] = int(stats[i])
#            #remove specific stat from list once it has be selected.
#            del stats[i]
#            print(stats)
#        else:
#            print("Hmm, I don't quite recognize that.")
#        #show current breakdown of selected stats
#        print(witcherCharacter.playerCharacter["Stats"])
#        i = i + 1
#    break
#print(f'How do these look? {witcherCharacter.playerCharacter["Stats"]}')
#dictionary version still needs to have numbers removed from stats list
print(f'Your currents stats are: {witcherCharacter.playerCharacter["Stats"]}, \n You got to start somewhere, I suppose.')
while i <= 9:
    for i in stats:
        statChoice = input(f'where should {stats[i]} go? \n')
        if statChoice.upper() in witcherCharacter.playerCharacter["Stats"].keys():
            print(stats[i])
            print(f'You have chosen {stats[i]} for {statChoice}')
            witcherCharacter.playerCharacter["Stats"][statChoice] = int(stats[i])
            statRemove = stats[i]
            stats.remove(statRemove)
            print(stats)
            i = i + 1
        print(witcherCharacter.playerCharacter["Stats"])


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
