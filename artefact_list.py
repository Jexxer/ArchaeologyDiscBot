def artefact_calc(quantity, artefact):
    for key in artefact_dict[artefact]:
        materials_dict[key] += (artefact_dict[artefact][key] * quantity)


artefacts = [
    "'Animate Dead' spell scroll",
    "'Consensus ad Idem' painting",
    "'Da Boss Man' sculpture",
    "'Disorder' painting",
    "'Exsanguinate' spell scroll",
    "'Forged in War' sculpture",
    "'Frying pan'",
    "'Hallowed Be the Everlight' painting",
    "'Incite Fear' spell scroll",
    "'Lust' metal sculpture",
    "'Nosorog!' sculpture",
    "'Pandemonium' tapestry",
    "'Possession' metal sculpture",
    "'Prima Legio' painting",
    "'Raksha' idol",
    "'Smoke Cloud' spell scroll",
    "'Solem in Umbra' painting",
    "'The Enlightened Soul' scroll",
    "'The Eudoxian Elements' tablet",
    "'The Lake of Fire' painting",
    "'The Lord of Light' painting",
    "'The Pride of Padosan' painting",
    "'Torment' metal sculpture",
    "Amphora",
    "Ancient globe",
    "Ancient magic tablet",
    "Ancient timepiece",
    "Avian song-egg player",
    "Aviansie dreamcoat",
    "Battle plans",
    "Beastkeeper helm",
    "Blackfire lance",
    "Branding iron",
    "Bronze Dominion medal",
    "Centurion's dress sword",
    "Centurion's seal",
    "Ceremonial dragonkin device",
    "Ceremonial dragonkin tablet",
    "Ceremonial mace",
    "Ceremonial plume",
    "Ceremonial unicorn ornament",
    "Ceremonial unicorn saddle",
    "Chaos Elemental trophy",
    "Chaos star",
    "Chuluu stone",
    "Crest of Dagon",
    "Dayguard shield",
    "Death Mask",
    "Decorative vase",
    "Dominarian device",
    "Dominion discus",
    "Dominion javelin",
    "Dominion pelte shield",
    "Dominion torch",
    "Dorgeshuun spear",
    "Doru spear",
    "Dragon burner",
    "Dragon scalpel",
    "Dragonkin calendar",
    "Dragonkin staff",
    "Drogokishuun hook sword",
    "Ekeleshuun blinder mask",
    "Everlight harp",
    "Everlight trumpet",
    "Everlight violin",
    "Fishing trident",
    "Flat cap",
    "Folded-arm figurine (female)",
    "Folded-arm figurine (male)",
    "Garagorshuun anchor",
    "Gold dish",
    "Golem heart",
    "Golem instruction",
    "Greater demon mask",
    "Hallowed lantern",
    "Hallowed lantern",
    "Hawkeye lens multi-vision scope",
    "Hellfire haladie",
    "Hellfire katar",
    "Hellfire zaghnal",
    "High priest crozier",
    "High priest mitre",
    "High priest orb",
    "Hobgoblin mansticker",
    "Hookah pipe",
    "Horogothgar cooking pot",
    "Huzamogaarb chaos crown",
    "Idithuun horn ring",
    "Ikovian gerege",
    "Imp mask",
    "Kal-i-kra chieftain crown",
    "Kal-i-kra mace",
    "Kal-i-kra warhorn",
    "Kantharos cup",
    "Keshik drum",
    "Kilaya",
    "Kontos lance",
    "Kopis dagger",
    "Larupia trophy",
    "Legatus Maximus figurine",
    "Legatus pendant",
    "Legionary gladius",
    "Legionary square shield",
    "Lesser demon mask",
    "Lingam stone",
    "Lion trophy",
    "Manacles",
    "Master control",
    "Meditation pipe",
    "Morin khuur",
    "Narogoshuun 'Hob-da-Gob' ball",
    "Necromantic focus",
    "Night owl flight goggles",
    "Nightguard shield",
    "Ogre Kyzaj axe",
    "Opulent wine goblet",
    "Order of Dis robes",
    "Ork cleaver sword",
    "Orthenglass flask",
    "Ourg megahitter",
    "Ourg tower/goblin cower shield",
    "Pasaha",
    "Patera bowl",
    "Peacocking parasol",
    "Personal totem",
    "Pontifex censer",
    "Pontifex crozier",
    "Pontifex Maximus figurine",
    "Pontifex mitre",
    "Pontifex signet ring",
    "Portable phylactery",
    "Praetorian hood",
    "Praetorian robes",
    "Praetorian staff",
    "Primis Elementis standard",
    "Protective goggles",
    "Prototype godbow",
    "Prototype godstaff",
    "Prototype godsword",
    "Prototype gravimeter",
    "Quintessence counter",
    "Rekeshuun war tether",
    "Ritual bell",
    "Ritual dagger",
    "Rod of Asclepius",
    "Saragorgak star crown",
    "She-wolf trophy",
    "Silver Dominion medal",
    "Singing bowl",
    "Songbird recorder",
    "Spear of Annihilation",
    "Spherical astrolabe",
    "Spiked dog collar",
    "Stormguard gerege",
    "Talon-3 razor wing",
    "Tetracompass",
    "Thorobshuun battle standard",
    "Toy glider",
    "Toy war golem",
    "Trishula",
    "Tsutsaroth helm",
    "Tsutsaroth pauldron",
    "Tsutsaroth piercing",
    "Tsutsaroth urumi",
    "Vazara",
    "Venator dagger",
    "Venator light crossbow",
    "Vigorem vial",
    "Virius trophy",
    "Xiphos short sword",
    "Xolo hard hat",
    "Xolo pickaxe",
    "Xolo shield",
    "Xolo spear",
    "Yurkolgokh stink grenade",
    "Zaros effigy",
    "Zarosian ewer",
    "Zarosian stein",
    "Zarosian training dummy"
]

materials_dict = {
    "Aetherium alloy": 0,
    "Ancient vis": 0,
    "Animal furs": 0,
    "Armadylean yellow": 0,
    "Blood of Orcus": 0,
    "Cadmium red": 0,
    "Carbon black": 0,
    "Chaotic brimstone": 0,
    "Cobalt blue": 0,
    "Compass rose": 0,
    "Demonhide": 0,
    "Dragon metal": 0,
    "Everlight silvthril": 0,
    "Eye of Dagon": 0,
    "Felt": 0,
    "Fossilised bone": 0,
    "Goldrune": 0,
    "Hellfire metal": 0,
    "Imperial iron": 0,
    "Imperial steel": 0,
    "Keramos": 0,
    "Leather scraps": 0,
    "Malachite green": 0,
    "Mark of the Kyzaj": 0,
    "Orgone": 0,
    "Orthenglass": 0,
    "Purpleheart wood": 0,
    "Quintessence": 0,
    "Samite silk": 0,
    "Soapstone": 0,
    "Star of Saradomin": 0,
    "Stormguard steel": 0,
    "Third Age iron": 0,
    "Tyrian purple": 0,
    "Vellum": 0,
    "Vulcanised rubber": 0,
    "Warforged bronze": 0,
    "White marble": 0,
    "White oak": 0,
    "Wings of War": 0,
    "Yu'biusk clay": 0,
    "Zarosian insignia": 0,
    "Sapphire": 0,
    "Emerald": 0,
    "Ruby": 0,
    "Diamond": 0,
    "Dragonstone": 0,
    "Bronze bar": 0,
    "Phoenix feather": 0,
    "Clockwork": 0,
    "Black mushroom ink": 0,
    "White candle": 0,
    "Death rune": 0,
    "Silver bar": 0,
    "Rope": 0,
    "Molten glass": 0,
    "Weapon poison (3)": 0,
    "Tetracompass piece (left)": 0,
    "Tetracompass piece (right)": 0,
    "Tetracompass piece (dial)": 0,
    "Tetracompass piece (needle)": 0,
    "Experience": 0
}
# refactored dict to be within pep8 guidelines
# has the added effect of being more readable
artefact_dict = {
    "'Animate Dead' spell scroll": {
        "Vellum": 40,
        "Ancient vis": 24,
        "Blood of Orcus": 40,
        "Experience": 27000.0
    },

    "'Consensus ad Idem' painting": {
        "White oak": 10,
        "Samite silk": 10,
        "Tyrian purple": 50,
        "Experience": 5600.0
    },

    "'Da Boss Man' sculpture": {
        "Yu'biusk clay": 50,
        "Malachite green": 44,
        "Soapstone": 44,
        "Experience": 45000.0
    },

    "'Disorder' painting": {
        "Samite silk": 6,
        "White oak": 6,
        "Vellum": 6,
        "Cadmium red": 14,
        "Experience": 646.2
    },

    "'Exsanguinate' spell scroll": {
        "Vellum": 40,
        "Blood of Orcus": 36,
        "Experience": 9333.3
    },

    "'Forged in War' sculpture": {
        "Warforged bronze": 50,
        "Yu'biusk clay": 42,
        "Emerald": 1,
        "Experience": 18666.7
    },

    "'Frying pan'": {
        "Third Age iron": 20,
        "White marble": 20,
        "Experience": 1073.3
    },

    "'Hallowed Be the Everlight' painting": {
        "Cobalt blue": 52,
        "White oak": 16,
        "Samite silk": 16,
        "Vellum": 16,
        "Experience": 24500.0
    },
        
    "'Incite Fear' spell scroll": {
        "Vellum": 20,
        "Ancient vis": 18,
        "Blood of Orcus": 18,
        "Experience": 2193.3
    },

    "'Lust' metal sculpture": {
        "Third Age iron": 16,
        "Eye of Dagon": 24,
        "Goldrune": 24,
        "Ruby": 1,
        "Experience": 3500.0
    },

    "'Nosorog!' sculpture": {
        "Yu'biusk clay": 30,
        "Malachite green": 24,
        "Warforged bronze": 30, 
        "Experience": 13333.3
    },

    "'Pandemonium' tapestry": {
        "White oak": 12,
        "Samite silk": 12,
        "Vellum": 12,
        "Cadmium red": 42, 
        "Experience": 10500.0
    },

    "'Possession' metal sculpture": {
        "Eye of Dagon": 24,
        "Chaotic brimstone": 30,
        "Third Age iron": 44,
        "Experience": 23333.3
    },

    "'Prima Legio' painting": {
        "White oak": 20,
        "Samite silk": 20,
        "Tyrian purple": 74,
        "Zarosian insignia": 20,
        "Experience": 43333.3
    },

    "'Raksha' idol": {
        "Orgone": 56,
        "Dragon metal": 44,
        "Goldrune": 40,
        "Experience": 46666.7
    },

    "'Smoke Cloud' spell scroll": {
        "Vellum": 40,
        "Ancient vis": 20,
        "Blood of Orcus": 32,
        "Experience": 18666.7
    },

    "'Solem in Umbra' painting": {
        "Samite silk": 8,
        "White oak": 10,
        "Experience": 664.1
    },

    "'The Enlightened Soul' scroll": {
        "Star of Saradomin": 50,
        "Vellum": 60,
        "Experience": 29666.7
    },

    "'The Eudoxian Elements' tablet": {
        "White marble": 60,
        "Goldrune": 50,
        "Experience": 29666.7
    },

    "'The Lake of Fire' painting": {
        "Samite silk": 10,
        "White oak": 10,
        "Vellum": 10,
        "Cadmium red": 34,
        "Experience": 3500.0
    },
        
    "'The Lord of Light' painting": {
        "Cobalt blue": 52,
        "White oak": 16,
        "Samite silk": 16,
        "Vellum": 16,
        "Experience": 24500.0
    },

    "'The Pride of Padosan' painting": {
        "Cobalt blue": 52,
        "White oak": 16,
        "Samite silk": 16,
        "Vellum": 16,
        "Experience": 24500.0
    },

    "'Torment' metal sculpture": {
        "Eye of Dagon": 20,
        "Third Age iron": 20,
        "Hellfire metal": 38,
        "Experience": 10500.0
    },

    "Amphora": {
        "Everlight silvthril": 34,
        "Keramos": 46,
        "Experience": 11666.7
    },

    "Ancient globe": {
        "White oak": 20,
        "Tyrian purple": 54,
        "Ancient vis": 60,
        "Experience": 43333.3
    },


    "Ancient magic tablet": {
        "Ancient vis": 40,
        "Blood of Orcus": 64,
        "Experience": 27000.0
    },

    "Ancient timepiece": {
        "Goldrune": 12,
        "Imperial steel": 16,
        "Ancient vis": 18,
        "Experience": 1423.3
    },

    "Avian song-egg player": {
        "Stormguard steel": 36,
        "Armadylean yellow": 32,
        "Diamond": 1,
        "Experience": 6066.7
    },
        
    "Aviansie dreamcoat": {
        "Armadylean yellow": 20,
        "Samite silk": 30,
        "Animal furs": 22,
        "Experience": 7388.9
    },
        
    "Battle plans": {
        "Vellum": 40,
        "Tyrian purple": 60,
        "Ancient vis": 34,
        "Experience": 43333.3
    },
        
    "Beastkeeper helm": {
        "Warforged bronze": 16,
        "Vulcanised rubber": 24,
        "Animal furs": 20,
        "Fossilised bone": 24,
        "Experience": 13333.3
    },
        
    "Blackfire lance": {
        "Aetherium alloy": 50,
        "Quintessence": 46,
        "Experience": 22166.7
    },

    "Branding iron": {
        "Third Age iron": 14,
        "Eye of Dagon": 12,
        "Hellfire metal": 20,
        "Experience": 1283.3
    },

    "Bronze Dominion medal": {
        "Everlight silvthril": 36,
        "Star of Saradomin": 26,
        "Bronze bar": 1,
        "Experience": 4433.3
    },

    "Centurion's dress sword": {
        "Imperial iron": 5,
        "Purpleheart wood": 5,
        "Experience": 250.0
    },

    "Centurion's seal": {
        "Third Age iron": 6,
        "Zarosian insignia": 2,
        "Experience": 430.8
    },

    "Ceremonial dragonkin device": {
        "Orthenglass": 66,
        "Experience": 4666.7
    },

    "Ceremonial dragonkin tablet": {
        "Orthenglass": 79,
        "Experience": 10888.9
    },

    "Ceremonial mace": {
        "Imperial steel": 20,
        "Third Age iron": 20,
        "Goldrune": 28,
        "Experience": 5600.0
    },

    "Ceremonial plume": {
        "Armadylean yellow": 38,
        "Goldrune": 34,
        "Phoenix feather": 1,
        "Experience": 7388.9
    },

    "Ceremonial unicorn ornament": {
        "Keramos": 26,
        "Cobalt blue": 20,
        "Experience": 1493.3
    },

    "Ceremonial unicorn saddle": {
        "Leather scraps": 24,
        "Cobalt blue": 22,
        "Experience": 1493.3
    },

    "Chaos Elemental trophy": {
        "Chaotic brimstone": 52,
        "White oak": 30,
        "Hellfire metal": 30,
        "Experience": 31000.0
    },

    "Chaos star": {
        "Chaotic brimstone": 28,
        "Hellfire metal": 36,
        "Experience": 4200.0
    },

    "Chuluu stone": {
        "Aetherium alloy": 40,
        "Quintessence": 30,
        "Soapstone": 40,
        "Goldrune": 24,
        "Experience": 43333.3
    },

    "Crest of Dagon": {
        "Goldrune": 14,
        "Orthenglass": 18,
        "Experience": 646.2
    },

    "Dayguard shield": {
        "Stormguard steel": 36,
        "Wings of War": 28,
        "White oak": 20,
        "Experience": 14166.7
    },

    "Death mask": {
        "Orgone": 56,
        "Soapstone": 34,
        "Experience": 17500
    },

    "Decorative vase": {
        "White marble": 36,
        "Cobalt blue": 30,
        "Experience": 5133.3
    },

    "Dominarian device": {
        "Everlight silvthril": 30,
        "Keramos": 22,
        "Third Age iron": 22,
        "Clockwork": 1,
        "Experience": 8555.6
    },

    "Dominion discus": {
        "Keramos": 34,
        "Star of Saradomin": 28,
        "Experience": 2566.7
    },

    "Dominion javelin": {
        "Keramos": 32,
        "Third Age iron": 30,
        "Experience": 2566.7
    },

    "Dominion pelte shield": {
        "Star of Saradomin": 34,
        "Samite silk": 28,
        "Experience": 2566.7
    },

    "Dominion torch": {
        "Goldrune": 12,
        "Orthenglass": 12,
        "Everlight silvthril": 20,
        "Star of Saradomin": 18,
        "Experience": 4433.3
    },

    "Dorgeshuun spear": {
        "Warforged bronze": 50,
        "White oak": 42,
        "Experience": 18666.7
    },

    "Doru spear": {
        "Everlight silvthril": 70, 
        "White oak": 62, 
        "Experience": 41666.7
    },

    "Dragon burner": {
        "Dragon metal": 52, 
        "Orgone": 42, 
        "Experience": 21000
    },

    "Dragon scalpel": {
        "Dragon metal": 52, 
        "Felt": 42, 
        "Experience": 19833.3
    },

    "Dragonkin calendar": {
        "Orgone": 34, 
        "Carbon black": 28, 
        "Compass rose": 28, 
        "Experience": 17500
    },

    "Dragonkin staff": {
        "Orgone": 56, 
        "Compass rose": 34, 
        "Experience": 17500
    },

    "Drogokishuun hook sword": {
        "Warforged bronze": 44, 
        "Malachite green": 36, 
        "Fossilised bone": 32, 
        "Experience": 31000.0
    },

    "Ekeleshuun blinder mask": {
        "Vulcanised rubber": 24, 
        "Malachite green": 20, 
        "Vellum": 24, 
        "Experience": 6066.7
    },

    "Everlight harp": {
        "Everlight silvthril": 30, 
        "White oak": 22, 
        "Experience": 1703.3
    },

    "Everlight trumpet": {
        "Everlight silvthril": 28, 
        "Goldrune": 24, 
        "Experience": 1703.3
    },

    "Everlight violin": {
        "Star of Saradomin": 16, 
        "White oak": 20, 
        "Samite silk": 16, 
        "Experience": 1703.3}
    ,

    "Fishing trident": {
        "Star of Saradomin": 22, 
        "Third Age iron": 30, 
        "Goldrune": 22, 
        "Experience": 8555.6
    },

    "Flat cap": {
        "Armadylean yellow": 60, 
        "Samite silk": 54, 
        "Experience": 32333.3
    },

    "Folded-arm figurine (female)": {
        "White marble": 30, 
        "Goldrune": 24, 
        "Experience": 2053.3
    },

    "Folded-arm figurine (male)": {
        "White marble": 30, 
        "Goldrune": 24, 
        "Experience": 2053.3
    },

    "Garagorshuun anchor": {
        "Warforged bronze": 32, 
        "Mark of the Kyzaj": 26, 
        "Third Age iron": 30, 
        "Experience": 15833.3
    },

    "Gold dish": {
        "Goldrune": 86, 
        "Dragon metal": 54, 
        "Experience": 46666.7
    },

    "Golem heart": {
        "Aetherium alloy": 34, 
        "Quintessence": 24, 
        "Orthenglass": 16, 
        "Soapstone": 16, 
        "Experience": 16666.7
    },

    "Golem instruction": {
        "Quintessence": 46, 
        "Vellum": 44, 
        "Black mushroom ink": 1, 
        "Experience": 16666.7
    },

    "Greater demon mask": {
        "Third Age iron": 6, 
        "Leather scraps": 6, 
        "Chaotic brimstone": 8, 
        "Demonhide": 12, 
        "Experience": 735.9
    },

    "Hallowed lantern": {
        "Third Age iron": 20, 
        "Keramos": 24, 
        "White candle": 1, 
        "Experience": 1073.3
    },

    "Hawkeye lens multi-vision scope": {
        "Stormguard steel": 40, 
        "Orthenglass": 34, 
        "Experience": 8944.4
    },

    "Hellfire haladie": {
        "Hellfire metal": 26, 
        "Third Age iron": 26, 
        "Leather scraps": 20, 
        "Experience": 16666.7
    },

    "Hellfire katar": {
        "Hellfire metal": 50, 
        "Leather scraps": 40, 
        "Experience": 16666.7
    },

    "Hellfire zaghnal": {
        "Hellfire metal": 38, 
        "White oak": 26, 
        "Orthenglass": 26, 
        "Experience": 16666.7
    },

    "High priest crozier": {
        "Mark of the Kyzaj": 26, 
        "Malachite green": 24, 
        "Goldrune": 28, 
        "Experience": 10500.0
    },

    "High priest mitre": {
        "Mark of the Kyzaj": 26, 
        "Malachite green": 24, 
        "Samite silk": 28, 
        "Experience": 10500.0
    },

    "High priest orb": {
        "Mark of the Kyzaj": 26, 
        "Malachite green": 24, 
        "Goldrune": 28, 
        "Experience": 10500.0
    },

    "Hobgoblin mansticker": {
        "Warforged bronze": 66, 
        "Fossilised bone": 46, 
        "Experience": 31000.0
    },

    "Hookah pipe": {
        "Third Age iron": 10, 
        "Goldrune": 12, 
        "Orthenglass": 8, 
        "Experience": 574.4
    },

    "Horogothgar cooking pot": {
        "Yu'biusk clay": 60, 
        "Malachite green": 38, 
        "Soapstone": 40, 
        "Experience": 45000.0
    },

    "Huzamogaarb chaos crown": {
        "Warforged bronze": 44, 
        "Third Age iron": 34, 
        "Eye of Dagon": 20, 
        "Experience": 23333.3
    },

    "Idithuun horn ring": {
        "Yu'biusk clay": 40, 
        "Vulcanised rubber": 44, 
        "Experience": 13333.3
    },

    "Ikovian gerege": {
        "Third Age iron": 36, 
        "Wings of War": 30, 
        "Experience": 4666.7
    },

    "Imp mask": {
        "Leather scraps": 10, 
        "Chaotic brimstone": 10, 
        "Demonhide": 12, 
        "Experience": 735.9
    },

    "Kal-i-kra chieftain crown": {
        "Yu'biusk clay": 66, 
        "Animal furs": 60, 
        "Experience": 38333.3
    },

    "Kal-i-kra mace": {
        "Vulcanised rubber": 42, 
        "Third Age iron": 44, 
        "Fossilised bone": 40, 
        "Experience": 38333.3
    },

    "Kal-i-kra warhorn": {
        "Vulcanised rubber": 44, 
        "Fossilised bone": 42, 
        "Animal furs": 40, 
        "Experience": 38333.3
    },

    "Kantharos cup": {
        "Everlight silvthril": 30, 
        "Orthenglass": 36, 
        "Sapphire": 1, 
        "Experience": 5133.3
    },

    "Keshik drum": {
        "Wings of War": 16, 
        "Animal furs": 16, 
        "White oak": 20, 
        "Leather scraps": 16, 
        "Experience": 6066.7
    },

    "Kilaya": {
        "Dragon metal": 46, 
        "Compass rose": 40, 
        "Experience": 15000
    },

    "Kontos lance": {
        "Everlight silvthril": 70, 
        "Samite silk": 62, 
        "Experience": 41666.7
    },

    "Kopis dagger": {
        "Everlight silvthril": 50, 
        "Leather scraps": 42, 
        "Experience": 18666.7
    },

    "Larupia trophy": {
        "Cadmium red": 18, 
        "Animal furs": 28, 
        "Orthenglass": 26, 
        "Experience": 7388.9
    },

    "Legatus Maximus figurine": {
        "Goldrune": 8, 
        "Zarosian insignia": 14, 
        "Ancient vis": 10, 
        "Experience": 664.1
    },

    "Legatus pendant": {
        "Third Age iron": 16, 
        "Goldrune": 18, 
        "Ancient vis": 12, 
        "Dragonstone": 1, 
        "Experience": 1423.3
    },

    "Legionary gladius": {
        "Third Age iron": 10, 
        "Zarosian insignia": 6, 
        "Imperial steel": 12, 
        "Experience": 430.8
    },

    "Legionary square shield": {
        "Third Age iron": 8, 
        "Zarosian insignia": 8, 
        "Imperial steel": 12, 
        "Experience": 430.8
    },

    "Lesser demon mask": {
        "Leather scraps": 6, 
        "Chaotic brimstone": 8, 
        "Demonhide": 12, 
        "Cadmium red": 6, 
        "Experience": 735.9
    },

    "Lingam stone": {
        "Orgone": 44, 
        "Carbon black": 30, 
        "Compass rose": 32, 
        "Experience": 28333.3
    },

    "Lion trophy": {
        "Cadmium red": 18, 
        "Animal furs": 28, 
        "White oak": 26, 
        "Experience": 7388.9
    },

    "Manacles": {
        "Third Age iron": 14, 
        "Chaotic brimstone": 18, 
        "Eye of Dagon": 14, 
        "Experience": 1283.3
    },

    "Master control": {
        "Orgone": 30, 
        "Carbon black": 32, 
        "Compass rose": 44, 
        "Experience": 28333.3
    },

    "Meditation pipe": {
        "Orgone": 60, 
        "Dragon metal": 40, 
        "Experience": 25666.7
    },

    "Morin khuur": {
        "Armadylean yellow": 36, 
        "White oak": 32, 
        "Experience": 6066.7
    },

    "Narogoshuun 'Hob-da-Gob' ball": {
        "Vulcanised rubber": 36, 
        "Mark of the Kyzaj": 32, 
        "Experience": 6066.7
    },

    "Necromantic focus": {
        "Imperial steel": 20, 
        "Blood of Orcus": 26, 
        "Ancient vis": 30, 
        "Experience": 9333.3
    },

    "Night owl flight goggles": {
        "Armadylean yellow": 44, 
        "Leather scraps": 40, 
        "Orthenglass": 30, 
        "Experience": 32333.3
    },

    "Nightguard shield": {
        "Stormguard steel": 30, 
        "Wings of War": 36, 
        "White oak": 30, 
        "Experience": 22166.7
    },

    "Ogre Kyzaj axe": {
        "Warforged bronze": 28, 
        "Mark of the Kyzaj": 20, 
        "Fossilised bone": 24, 
        "Experience": 7388.9
    },

    "Opulent wine goblet": {
        "Third Age iron": 14, 
        "Goldrune": 16, 
        "Experience": 574.4
    },

    "Order of Dis robes": {
        "Samite silk": 16, 
        "Cadmium red": 10, 
        "Eye of Dagon": 14, 
        "Experience": 861.5
    },

    "Ork cleaver sword": {
        "Warforged bronze": 36, 
        "Fossilised bone": 36, 
        "Experience": 7388.9
    },

    "Orthenglass flask": {
        "Dragon metal": 34, 
        "Orthenglass": 60, 
        "Experience": 21000
    },

    "Ourg megahitter": {
        "White oak": 20, 
        "Leather scraps": 20,
        "Orthenglass": 26, 
        "Malachite green": 22, 
        "Experience": 15833.3
    },

    "Ourg tower/goblin cower shield": {
        "Mark of the Kyzaj": 20, 
        "Third Age iron": 26, 
        "Leather scraps": 22, 
        "White oak": 20, 
        "Experience": 15833.3
    },

    "Pasaha": {
        "Felt": 40, 
        "Goldrune": 38, 
        "Experience": 10888.9
    },

    "Patera bowl": {
        "Keramos": 36, 
        "Goldrune": 30, 
        "Sapphire": 1, 
        "Experience": 5133.3
    },

    "Peacocking parasol": {
        "Armadylean yellow": 22, 
        "Samite silk": 30, 
        "White oak": 20, 
        "Experience": 7388.9
    },

    "Personal totem": {
        "Orgone": 48, 
        "Carbon black": 26, 
        "Compass rose": 26, 
        "Experience": 25666.7
    },

    "Pontifex censer": {
        "Third Age iron": 20, 
        "Ancient vis": 20, 
        "Goldrune": 32, 
        "Dragonstone": 1, 
        "Experience": 7388.9
    },

    "Pontifex crozier": {
        "Imperial steel": 20, 
        "Zarosian insignia": 20, 
        "Goldrune": 32, 
        "Experience": 7388.9
    },

    "Pontifex Maximus figurine": {
        "Zarosian insignia": 24, 
        "Ancient vis": 16, 
        "Goldrune": 28, 
        "Dragonstone": 1, 
        "Experience": 5600.0
    },

    "Pontifex mitre": {
        "Samite silk": 32,
        "Ancient vis": 20, 
        "Zarosian insignia": 20, 
        "Experience": 7388.9
    },

    "Pontifex signet ring": {
        "Third Age iron": 16, 
        "Goldrune": 18, 
        "Ancient vis": 22, 
        "Dragonstone": 1, 
        "Experience": 2193.3
    },
        
    "Portable phylactery": {
        "Imperial steel": 48, 
        "Blood of Orcus": 36, 
        "Ancient vis": 20, 
        "Experience": 27000.0
    },

    "Praetorian hood": {
        "Ancient vis": 36, 
        "Samite silk": 48, 
        "Zarosian insignia": 40, 
        "Death rune": 30, 
        "Experience": 36666.7
    },

    "Praetorian robes": {
        "Ancient vis": 30, 
        "Samite silk": 54, 
        "Zarosian insignia": 40, 
        "Death rune": 50, 
        "Experience": 36666.7
    },

    "Praetorian staff": {
        "Imperial steel": 36, 
        "Ancient vis": 58, 
        "Zarosian insignia": 30, 
        "Death rune": 100, 
        "Experience": 36666.7
    },

    "Primis Elementis standard": {
        "Samite silk": 16, 
        "Third Age iron": 12, 
        "Experience": 430.8
    },

    "Protective goggles": {
        "Felt": 42, 
        "Orthenglass": 52, 
        "Experience": 19833.3
    },

    "Prototype godbow": {
        "Aetherium alloy": 50, 
        "Quintessence": 34, 
        "Wings of War": 34, 
        "Experience": 33666.7
    },

    "Prototype godstaff": {
        "Aetherium alloy": 50, 
        "Quintessence": 34, 
        "Wings of War": 34, 
        "Experience": 33666.7
    },

    "Prototype godsword": {
        "Aetherium alloy": 50, 
        "Wings of War": 34, 
        "Goldrune": 34, 
        "Experience": 33666.7
    },

    "Prototype gravimeter": {
        "Quintessence": 34, 
        "Leather scraps": 20, 
        "Third Age iron": 26, 
        "Experience": 11277.8
    },

    "Quintessence counter": {
        "Quintessence": 54, 
        "Stormguard steel": 40, 
        "White oak": 40, 
        "Experience": 43333.3
    },

    "Rekeshuun war tether": {
        "Warforged bronze": 20, 
        "Vulcanised rubber": 22, 
        "Leather scraps": 26, 
        "Experience": 6066.7
    },

    "Ritual bell": {
        "Goldrune": 40, 
        "Compass rose": 38, 
        "Experience": 10888.9
    },

    "Ritual dagger": {
        "Goldrune": 16, 
        "Hellfire metal": 24, 
        "Ruby": 1, 
        "Experience": 861.5
    },

    "Rod of Asclepius": {
        "White marble": 30, 
        "Star of Saradomin": 24, 
        "Goldrune": 26, 
        "Experience": 11666.7
    },

    "Saragorgak star crown": {
        "Warforged bronze": 44, 
        "Third Age iron": 34, 
        "Star of Saradomin": 20, 
        "Experience": 23333.3
    },

    "She-wolf trophy": {
        "Cadmium red": 18, 
        "Animal furs": 28, 
        "Chaotic brimstone": 26, 
        "Experience": 7388.9
    },

    "Silver Dominion medal": {
        "Everlight silvthril": 36, 
        "Star of Saradomin": 26, 
        "Silver bar": 1, 
        "Experience": 4433.3
    },

    "Singing bowl": {
        "Orgone": 60, 
        "Dragon metal": 40, 
        "Experience": 25666.7
    },

    "Songbird recorder": {
        "Stormguard steel": 44, 
        "Orthenglass": 36, 
        "Diamond": 1, 
        "Experience": 11277.8
    },

    "Spear of Annihilation": {
        "Vulcanised rubber": 500, 
        "Malachite green": 500, 
        "Goldrune": 500, 
        "Experience": 38333.3
    },

    "Spherical astrolabe": {
        "Aetherium alloy": 46, 
        "Armadylean yellow": 40, 
        "Orthenglass": 48, 
        "Experience": 43333.3
    },

    "Spiked dog collar": {
        "Third Age iron": 24, 
        "Leather scraps": 24, 
        "Chaotic brimstone": 16, 
        "Experience": 4200.0
    },

    "Stormguard gerege": {
        "Stormguard steel": 36, 
        "Wings of War": 28, 
        "Goldrune": 20, 
        "Experience": 14166.7
    },

    "Talon-3 razor wing": {
        "Aetherium alloy": 40, 
        "Wings of War": 34, 
        "Rope": 1, 
        "Experience": 8944.4
    },

    "Thorobshuun battle standard": {
        "Mark of the Kyzaj": 16, 
        "Malachite green": 22, 
        "White oak": 16, 
        "Samite silk": 20, 
        "Experience": 8166.7
    },

    "Toy glider": {
        "Stormguard steel": 36, 
        "White oak": 30, 
        "Experience": 4666.7
    },

    "Toy war golem": {
        "Third Age iron": 36, 
        "White oak": 30, 
        "Clockwork": 1, 
        "Experience": 4666.7
    },

    "Trishula": {
        "Hellfire metal": 48, 
        "Eye of Dagon": 30, 
        "Third Age iron": 20, 
        "Experience": 23333.3
    },

    "Tsutsaroth helm": {
        "Hellfire metal": 50, 
        "Eye of Dagon": 40, 
        "Goldrune": 40, 
        "Experience": 40000.0
    },

    "Tsutsaroth pauldron": {
        "Hellfire metal": 40, 
        "Goldrune": 50, 
        "Eye of Dagon": 40, 
        "Experience": 40000.0
    },

    "Tsutsaroth piercing": {
        "Hellfire metal": 44, 
        "Chaotic brimstone": 30, 
        "Cadmium red": 24, 
        "Experience": 23333.3
    },

    "Tsutsaroth urumi": {
        "Hellfire metal": 50, 
        "Eye of Dagon": 40, 
        "Third Age iron": 40, 
        "Experience": 40000.0
    },

    "Vazara": {
        "Dragon metal": 30, 
        "Compass rose": 28, 
        "Goldrune": 28, 
        "Experience": 15000
    },

    "Venator dagger": {
        "Third Age iron": 16, 
        "Zarosian insignia": 12, 
        "Experience": 305.1
    },

    "Venator light crossbow": {
        "Third Age iron": 12, 
        "Zarosian insignia": 16, 
        "Experience": 305.1
    },

    "Vigorem vial": {
        "Imperial steel": 54, 
        "Ancient vis": 38, 
        "Molten glass": 1, 
        "Experience": 18666.7
    },

    "Virius trophy": {
        "Demonhide": 44, 
        "White oak": 34, 
        "Orthenglass": 34, 
        "Experience": 31000.0
    },

    "Xiphos short sword": {
        "Everlight silvthril": 46, 
        "Leather scraps": 46, 
        "Experience": 18666.7
    },

    "Xolo hard hat": {
        "Goldrune": 54, 
        "Dragon metal": 66, 
        "Experience": 35000
    },

    "Xolo pickaxe": {
        "Goldrune": 36, 
        "Dragon metal": 50, 
        "Orgone": 34, 
        "Experience": 35000
    },

    "Xolo shield": {
        "Goldrune": 52, 
        "Orgone": 44, 
        "Felt": 42, 
        "Experience": 45000
    },

    "Xolo spear": {
        "Dragon metal": 74, 
        "Orgone": 64, 
        "Experience": 45000
    },

    "Yurkolgokh stink grenade": {
        "Yu'biusk clay": 38, 
        "Vulcanised rubber": 36, 
        "Weapon poison (3)": 1, 
        "Experience": 8166.7
    },

    "Zaros effigy": {
        "Samite silk": 8, 
        "White oak": 10, 
        "Zarosian insignia": 12, 
        "Experience": 520.5
    },

    "Zarosian ewer": {
        "Third Age iron": 52, 
        "Zarosian insignia": 30, 
        "Experience": 12500.0
    },

    "Zarosian stein": {
        "Third Age iron": 52, 
        "Imperial steel": 36, 
        "Zarosian insignia": 30, 
        "Experience": 12500.0
    },

    "Zarosian training dummy": {
        "Third Age iron": 16, 
        "White oak": 14, 
        "Experience": 520.5
    },

    "Tetracompass": {
        "Tetracompass piece (left)": 1,
        "Tetracompass piece (right)": 1,
        "Tetracompass piece (dial)": 1,
        "Tetracompass piece (needle)": 1,
        "Malachite green": 1,
        "Cadmium red": 1,
        "Cobalt blue": 1,
        "Armadylean yellow": 1,
        "Tyrian purple": 1,
        "Experience": 2065.0
    }
}
