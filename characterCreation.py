import witcherCharacter
import lifepath_easyMode
import random

#commenting this out for now as i test the other stuff below
#
#print ("Hello and welcome to the Witcher TTRP Character Creation Assistant. We will be using information from the FREE Easy Mode Document, which is a truncated version of the full Life Path process.")
#witcherCharacter.playerCharacter["Info"]["Name"] = input("Let's get started by you saying your name? ")
#print(witcherCharacter.playerCharacter["Info"]["Name"])


#trying to randomly select from a list in lifepath_easyMode
famFateLength = len(lifepath_easyMode.familiarFateRoll)
print('TEST, how many familiar fate rolls: ' + str(famFateLength))
r =random.randint(1, (famFateLength-1))
print('TEST, the random number is: ' + str(r))
yourFamilyFate = lifepath_easyMode.familiarFateRoll[r]
print('Your family\'s fate:')
print(yourFamilyFate)
