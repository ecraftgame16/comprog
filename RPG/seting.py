class setting():
    max_health = 100
    current_health = 100
    items_decoration = {
        "Mountain Landscape painting": {
            "description": "A beautiful painting of the Chiba mountainscape",
            "type": "decoration",
            "value": 50
        },
        "traditional Japanese tea set": {
            "description": "An exquisite handmade Japanese style tea set",
            "type": "decoration",
            "value": 100
        },
        "Wooden Fox Statue": {
            "description": "A small carved statue of a fox",
            "type": "decoration",
            "value": 50
        },
        "Ancient scroll": {
            "description": "An old scroll with characters you don't understand",
            "type": "decoration",
            "value": 60
        },
        "mini tree": {
            "description": "A miniature bonsai tree with delicate cherry blossoms",
            "type": "decoration",
            "value": 40
        },
        "Rice Paper Lanterns": {
            "description": "Decorative lanterns made of rice paper often seen in festivals",
            "type": "decoration",
            "value": 20
        },
        "Stone Garden miniature": {
            "description": "A small stone garden you set it in the main living room",
            "type": "decoration",
            "value": 70
        },
        "Samurai Helmet Replica": {
            "description": "An old samurai helmet no longer suitable for use",
            "type": "decoration",
            "value": 40
        },
        "Folding Screen with Mountain Art": {
            "description": "A nice folding screen with the mountains of Chiba painted on",
            "type": "decoration",
            "value": 40
        },
        "Koi Fish Ceramic Bowl": {
            "description": "A beautifully crafted ceramic bowl with a koi fish design",
            "type": "decoration",
            "value": 40
        }
    }
    lDecorationItems = list(items_decoration)

    enemies = {
        "Mountain Tengu": {
            "description": "A mythical looking creature with both human and bird like features",
            "damage minimum": 40,
            "damage maximum": 60,
            "health minimum": 120,
            "health maximum": 200
        },
        "Forest Yokai": {
            "description": "a spirit/demon that appears as a fox",
            "damage minimum": 50,
            "damage maximum": 70,
            "health minimum": 130,
            "health maximum": 200
        },
        "Bandit Gang": {
            "description": "a group of 3 thieves human",
            "damage minimum": 50,
            "damage maximum": 70,
            "health minimum": 130,
            "health maximum": 250
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
