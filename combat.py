import witcherCharacter
import random

def initiative(REF):
    #Initiative is calculated by 1d10 + a characters Reflex score
  print(f'{witcherCharacter.playerCharacter["Info"]["Name"]} rolls for initiative! \nYour REF score is {witcherCharacter.playerCharacter["Stats"]["REF"]}.')
  initiativeRoll = random.randint(1,10) + REF
  print(f'Your initative for this encounter is {initiativeRoll}')
  RUN = witcherCharacter.playerCharacter["Stats"]["SPD"]*3
  LEAP = round(RUN/5)
  witcherCharacter.playerCharacter["derivedStats"]["RUN"] = RUN
  witcherCharacter.playerCharacter["derivedStats"]["LEAP"] = LEAP
  print(f'your run score is {RUN} for this encounter.\nAnd your leap score is {LEAP}.')
  return initiativeRoll

print(initiative(witcherCharacter.playerCharacter["Stats"]["REF"]))

print(witcherCharacter.playerCharacter["derivedStats"]["LEAP"])
