class seting():
    max_health = 100
    curent_helth = 100
    items_decoration = {
        "Mountain Landscape painting" : {
            "description" : "A butifull painting of the Chiba mountainscape",
            "type" : "decoration",
            "value" : 50
        },
        "traditional Japanese tea set" : {
            "description" : "An exquisit handmade japanese style tea set",
            "type" : "decoration",
            "value" : 100
        },
        "Wodden Fox Statue" : {
            "description" : "A small carved statue of a fox",
            "type" : "decoration",
            "value" : 50
        },
        "Anchien scrool" : {
            "description" : "an old school with chareters you dont understand",
            "type" : "decoration",
            "value" : 60
        },
        "mini tree" : {
            "description" : "a minuture bonsai tree with delacate cherry blosims",
            "type" : "decoration",
            "value" : 40
        },
        "Rice Papper Lanterns" : {
            "description" : "Decorative lanterns made of rice papper often seen in festivals",
            "type" : "decoration",
            "value" : 20
        },
        "Stone Garden minaiture" : {
            "description" : "A small stone garden you sit it in the main living room",
            "type" : "decoration",
            "value" : 70
        },
        "Samuri Helmit Replica" : {
            "description" : "An old samuri helment no longer sutable for use",
            "type" : "decoration",
            "value" : 40
        },
        "Folding Screen with Mountain Art" : {
            "description" : "A nice folding screen with the mountains of chiba painted on",
            "type" : "decoration",
            "value" : 40
        },
        "Koi Fish Ceramic Bowl" : {
            "description" : "A butifuly crafted ceramic boel with a koi fish design",
            "type" : "decoration",
            "value" : 40
        }
        
    }
    lDecorationItems = list(items_decoration)

    enimies = {
        "Mountain Tengu" : {
            "discription" : "A mythical looking creature with both human and bird like features",
            "dammage minum" : 40,
            "dammage maximum" : 60,
            "health minumim" : 120,
            "health maxumim" : 200
        },
        "Forest Yokai" : {
            "discription" : "a spirit/demon that aperes as a fox",
            "dammage minum" : 50,
            "dammage maximum" : 70,
            "health minumim" : 130,
            "health maxumim" : 200
        },
        "Bandit Gang" : {
            "discription" : "a group of 3 thieves human",
            "dammage minum" : 50,
            "dammage maximum" : 70,
            "health minumim" : 130,
            "health maxumim" : 250
        },
    }
    lEnimies = list(enimies)
    
        # enimie
        # "name" : {
        #     "discription" : "",
        #     "dammage minum" : 40,
        #     "dammage maximum" : 60,
        #     "health minumim" : 120,
        #     "health maxumim" : 200
        # },