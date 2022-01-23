import witcherCharacter
import random

def initiative(REF):
    #Initiative is calculated by 1d10 + a characters Reflex score
  print(f'{witcherCharacter.playerCharacter["Info"]["Name"]} rolls for initiative! \nYour REF score is {witcherCharacter.playerCharacter["Stats"]["REF"]}.')
  initiativeRoll = random.randint(1,10) + REF
  print(f'Your initative for this encounter is {initiativeRoll}')
  return initiativeRoll

print(initiative(witcherCharacter.playerCharacter["Stats"]["REF"]))
