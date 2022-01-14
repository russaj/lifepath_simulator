#Changed familial and family fate to empty strings from booleans

playerCharacter = {
"Info" : {
"Name" : "",
"Race" : "",
"Profession" : ""
},
#lets start stats as a list and then MAKE it a dict, will explain why (JH)
"Stats" : [
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
],
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
