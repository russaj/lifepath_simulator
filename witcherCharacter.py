#Changed familial and family fate to empty strings from booleans

playerCharacter = {
"Info" : {
"Name" : "",
"Race" : "",
"Profession" : ""
},
 "Stats" :{"INT": 0,
"REF": 0,
"DEX": 0,
"BODY": 0,
"SPD" : 0,
"EMP" : 0,
"CRA" : 0,
"WILL" : 0,
"LUCK" : 0,
"VIGOR": 0,
"SAVE" : 0,
"LEAP" : 0,
"HP" : 0,
"STA" : 0,
"REC": 0,
} ,
"lifePath": {
"Familial Fate": "",
"Family Northern Status": 0,
"Parental Fate" : "",
"Parent Northern Status": 0,
"Family Status" : ""
},
"Armor" : {
"Head" : 0,
"Upper Body" : 0,
"Lower Body" : 0
},
"Weapon" : {
"Name" : "",
"WA" : 0,
"DMG" : 0,
"Effect" : ""}
}

#lets start stats as a list and then MAKE it a dict, i will explain why (JH)
StatsAsList = [
"INT",
"REF",
"DEX",
"BODY",
"SPD" ,
"EMP" ,
"CRA" ,
"WILL" ,
"LUCK" ,
"VIGOR",
"SAVE" ,
"LEAP" ,
"HP" ,
"STA" ,
"REC"
]