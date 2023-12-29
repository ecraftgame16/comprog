class setting():
    max_health = 100
    current_health = 100
    DEV_PASSWORD = "CATS"
    items_decoration = {
        "Mountain Landscape painting": {
            "description": "A beautiful painting of the Chiba mountainscape",
            "type": "decoration",
            "cost": 50
        },

        "traditional Japanese tea set": {
            "description": "An exquisite handmade Japanese style tea set",
            "type": "decoration",
            "cost": 100
        },

        "Wooden Fox Statue": {
            "description": "A small carved statue of a fox",
            "type": "decoration",
            "cost": 50
        },

        "Ancient scroll": {
            "description": "An old scroll with characters you don't understand",
            "type": "decoration",
            "cost": 60
        },

        "mini tree": {
            "description": "A miniature bonsai tree with delicate cherry blossoms",
            "type": "decoration",
            "cost": 40
        },

        "Rice Paper Lanterns": {
            "description": "Decorative lanterns made of rice paper often seen in festivals",
            "type": "decoration",
            "cost": 20
        },

        "Stone Garden miniature": {
            "description": "A small stone garden you set it in the main living room",
            "type": "decoration",
            "cost": 70
        },

        "Samurai Helmet Replica": {
            "description": "An old samurai helmet no longer suitable for use",
            "type": "decoration",
            "cost": 40
        },

        "Folding Screen with Mountain Art": {
            "description": "A nice folding screen with the mountains of Chiba painted on",
            "type": "decoration",
            "cost": 40
        },

        "Koi Fish Ceramic Bowl": {
            "description": "A beautifully crafted ceramic bowl with a koi fish design",
            "type": "decoration",
            "cost": 40
        }
    }
    l_decoration_items = list(items_decoration)

    items_attack = {
        "ancient_samurai_katana" : {
            "description" : """This is a beautifully crafted katana, once wielded by a legendary samurai of the Chiba region.
            It is known for its sharpness and durability, with intricate designs on the hilt representing the local history and mythology. 
            When used in combat, it strikes with precision and power reflective of the samurai's skill.""",
            "attack_bonus_min" : 10,
            "attack_bonus_max" : 50,
            "cost" : 100,
            "type" : "attack"
        },

        "tachi_long_sword": {
            "description": """A Tachi, the predecessor of the katana, known for its curvature and length. Used primarily by cavalry,
            it is a symbol of the samurai's honor and prowess in battle. Its elongated blade allows for powerful strikes.""",
            "attack_bonus_min": 15,
            "attack_bonus_max": 45,
            "cost": 120,
            "type": "attack"
        },

        "yumi_bow": {
            "description": """The Yumi is a traditional Japanese longbow used by the samurai class of feudal Japan. 
            Made from bamboo and wood, it is exceptionally tall and can shoot arrows with great force and accuracy over considerable distances.""",
            "attack_bonus_min": 8,
            "attack_bonus_max": 35,
            "cost": 80,
            "type": "attack"
        },

        "kanabo_club": {
            "description": """A kanabo is a spiked or studded club used by the samurai and oni (demons) in folklore. 
            Made of heavy wood or iron, it is a symbol of brute strength and is capable of crushing armor and breaking bones.""",
            "attack_bonus_min": 20,
            "attack_bonus_max": 55,
            "cost": 150,
            "type": "attack"
        },

        "naginata_polearm": {
            "description": """The Naginata, a pole weapon that was traditionally used in Japan by members of the samurai class. 
            It has a long shaft with a curved blade on the end. It's well balanced and offers the wielder both reach and agility in combat.""",
            "attack_bonus_min": 12,
            "attack_bonus_max": 40,
            "cost": 110,
            "type": "attack"
        },

        "ono_axe": {
            "description": """An Ono is a type of axe used by the samurai and foot soldiers in feudal Japan. This particular one has a large, curved blade 
            affixed to a wooden handle, designed to deliver devastating blows. Its use requires great strength, but it can break through enemy defenses with ease.""",
            "attack_bonus_min": 25,
            "attack_bonus_max": 60,
            "cost": 130,
            "type": "attack"
        },

        "shuriken_stars": {
            "description": """Shuriken, or throwing stars, are concealed weapons that were used for silent attacks and distraction. Small, edged, and easily 
            concealed, they can be thrown with precision by skilled hands. These particular shuriken are made of steel and have been used by ninja for various covert operations.""",
            "attack_bonus_min": 5,
            "attack_bonus_max": 30,
            "cost": 70,
            "type": "attack"
        },

    }

    l_attack_items = list(items_attack)

    items_defense = {
        "Monk's_woven_bamboo_shield" : {
            "discription" : """A sturdy shield made from tightly woven bamboo and blessed by monks from a local temple.
            It's surprisingly light yet effective against various attacks. The shield is adorned with symbols and prayers for protection, 
            invoking the spiritual strength of the mountains and forests surrounding Chiba.""",
            "defense_bonus_min" : 15,
            "defense_bonus_max" : 30,
            "cost" : 150,
            "type" : "defense"
        },

        "iron_fan_tessen": {
            "description": """The Tessen, or iron fan, was a folding fan with outer spokes made of heavy plates of iron which were used as a defensive weapon. 
            It could be used to guard against attacks or as a discreet weapon. Samurai often carried them, and they were also used by commanders to signal troops.""",
            "defense_bonus_min": 15,
            "defense_bonus_max": 20,
            "cost": 100,
            "type": "defense"
        },

        "samurai_armour_yoroi": {
            "description": """Yoroi is the traditional armor worn by the samurai class and their retainers in feudal Japan. This particular set is crafted with great skill, 
            featuring lacquered plates tied together, ensuring both flexibility and protection. The ornate design symbolizes both the status and the valor of the wearer.""",
            "defense_bonus_min": 20,
            "defense_bonus_max": 50,
            "cost": 200,
            "type": "defense"
        },

        "sode_large_shoulder_guards": {
            "description": """Sode are large rectangular shoulder guards used in traditional samurai armor. They provide excellent protection 
            against downward strikes and are adorned with family crests or symbols of protection. These sode are crafted with reinforced silk and steel, 
            offering both durability and a striking appearance.""",
            "defense_bonus_min": 12,
            "defense_bonus_max": 35,
            "cost": 140,
            "type": "defense"
        },

        "kabuto_helmet": {
            "description": """The Kabuto is a helmet used by samurai, often made of iron or leather, adorned with intricate designs symbolizing the warrior's honor and valor. 
            This particular kabuto includes a protective neck guard and a prominent front crest, offering both intimidation and substantial protection.""",
            "defense_bonus_min": 15,
            "defense_bonus_max": 40,
            "cost": 160,
            "type": "defense"
        },

        "war_fan_gunbai": {
            "description": """The Gunbai, or war fan, was used by samurai officers to direct troops and deflect arrows. Made from solid wood or iron, 
            it is large and sturdy enough to serve as a shield in combat. This gunbai has been in battles for generations and is inscribed with prayers for victory and protection.""",
            "defense_bonus_min": 8,
            "defense_bonus_max": 28,
            "cost": 90,
            "type": "defense"
        },



    }

    l_defense_items = list(items_defense)

    items_heal = {
        "small_heal_pack" : {
            "discription" : "a small medical pack for dresing small wounds",
            "healing power min" : 5,
            "healing power max" : 10,
            "cost" : 50,
            "type" : "healing"
        },

        "medium_heal_pack" : {
            "discription" : "a mediaum size medical pack for helping some more serious wounds.",
            "healing power min" : 10,
            "healing power max" : 15,
            "cost" : 100,
            "type" : "healing"
        },

        "large_heal_pack" : {
            "discription" : "a large medical pack for healing major woulds",
            "healing power min" : 15,
            "healing power max" : 20,
            "cost" : 150,
            "type" : "healing"
        }


    }

    l_healing_items = list(items_heal)

    enemies = {
        "Mountain Tengu": {
            "description": "A mythical looking creature with both human and bird like features",
            "damage minimum": 40,
            "damage maximum": 60,
            "health minimum": 110,
            "health maximum": 130
        },

        "Forest Yokai": {
            "description": "a spirit/demon that appears as a fox",
            "damage minimum": 50,
            "damage maximum": 70,
            "health minimum": 130,
            "health maximum": 140
        },

        "Bandit Gang": {
            "description": "a group of 2 thieves human",
            "damage minimum": 50,
            "damage maximum": 70,
            "health minimum": 160,
            "health maximum": 220
        },

        "Giant Mountain Serpent": {
            "description": "A colossal snake dwelling in caves and along mountain rivers, feared for its strength.",
            "damage minimum": 55,
            "damage maximum": 65,
            "health minimum": 150,
            "health maximum": 200
        },

        "Cursed Samurai": {
            "description": "Armored warrior spirits cursed to guard ancient ruins, relentless in battle.",
            "damage minimum": 45,
            "damage maximum": 60,
            "health minimum": 120,
            "health maximum": 170
        },

        "Elemental Spirit": {
            "description": "A mystical spirit embodying natural elements, its form shifts with the mountain winds.",
            "damage minimum": 40,
            "damage maximum": 55,
            "health minimum": 100,
            "health maximum": 150
        },

        "Rogue Ninja": {
            "description": "Stealthy and dangerous, these exiled ninjas attack swiftly from the shadows.",
            "damage minimum": 50,
            "damage maximum": 70,
            "health minimum": 130,
            "health maximum": 160
        },

        "Jorogumo": {
            "description": "A deceptive spider yokai that can take on the appearance of a beautiful woman.",
            "damage minimum": 40,
            "damage maximum": 60,
            "health minimum": 140,
            "health maximum": 180
        },

        "Wild Mountain Beast": {
            "description": "A massive beast, rumored to be a bear or wolf, that roams the mountain wilderness.",
            "damage minimum": 45,
            "damage maximum": 65,
            "health minimum": 150,
            "health maximum": 200
        },
}


    lEnemies = list(enemies)

    # enemy template
    # "name": {
    #     "description": "",
    #     "damage minimum": 40,
    #     "damage maximum": 60,
    #     "health minimum": 120,
    #     "health maximum": 200
    # },
