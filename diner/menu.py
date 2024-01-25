class english_menu:
    entree = {
        "Sushi and Sashimi": {
            "description": "Assorted pieces of fresh fish, shellfish, and other seafood, served raw or lightly vinegared rice. Options often include tuna, salmon, yellowtail, eel, and shrimp.",
            "price": 2000
        },
        "Tempura": {
            "description": "Lightly battered and deep-fried seafood and vegetables, served with a dipping sauce. Popular tempura items include shrimp, sweet potato, eggplant, and green beans.",
            "price": 2000
        },
        "Teriyaki": {
            "description": "Grilled or broiled meat (chicken, beef, or fish) glazed with a sweet and savory sauce made from soy sauce, mirin, and sugar.",
            "price": 1500
        },
        "Ramen": {
            "description": "A noodle soup dish featuring a rich broth, wheat noodles, and various toppings such as slices of pork, green onions, nori (seaweed), and boiled eggs",
            "price": 900
        },
        "Udon and Soba": {
            "description": "Thick udon or thin soba noodles served in a hot broth or chilled with a dipping sauce. Toppings can include tempura, tofu, green onions, and nori.",
            "price": 1650
        },
        "Tonkatsu": {
            "description": "Breaded and deep-fried pork cutlet, typically served with cabbage salad and a sweet and tangy sauce.",
            "price": 1572
        },
        "Yakitori": {
            "description": "Skewered and grilled chicken pieces, often including different parts of the chicken such as thigh, breast, wings, and meatballs.",
            "price": 572
        },
        "Katsu-Don": {
            "description": "A bowl of rice topped with a deep-fried pork cutlet, egg, vegetables, and a sweet and savory sauce.",
            "price": 1000
        },
        "Chawanmushi": {
            "description": "A savory egg custard dish, typically steamed and served in a small cup or bowl, containing ingredients like chicken, shrimp, and shiitake mushrooms.",
            "price": 600
        },
        "Unagi Donburi (Unadon)": {
            "description": "A rice bowl dish featuring grilled eel fillets glazed with a sweet soy-based sauce, often served with pickles and sometimes with a sprinkling of sansho (Japanese pepper).",
            "price": 2137
        }
    }
    lentree = list(entree)

    sides = {
        "Edamame": {
            "description": "Young, lightly salted green soybeans served in the pod, often steamed or boiled. They're a simple yet flavorful starter.",
            "price": 400
        },
        "Miso Soup": {
            "description": "A traditional soup made with miso paste (fermented soybean paste), dashi (Japanese soup stock), and various ingredients like tofu, seaweed, and green onions.",
            "price": 350
        },
        "Tsukemono (Japanese Pickles)": {
            "description": "Assorted pickled vegetables such as cucumber, radish, eggplant, and ginger, known for their crisp texture and refreshing taste",
            "price": 400
        },
        "Goma-ae": {
            "description": "Vegetables, typically spinach or green beans, tossed in a sweet and savory sesame dressing.",
            "price": 570
        },
        "Sunomono": {
            "description": "A light, tangy salad made with thinly sliced cucumbers, seaweed, and sometimes crab or shrimp, all marinated in a vinegar dressing.",
            "price": 482
        },
        "Takoyaki": {
            "description": "Ball-shaped snacks made of a wheat flour-based batter and cooked with minced or diced octopus, tempura scraps, pickled ginger, and green onion.",
            "price": 1500
        },
        "Okonomiyaki": {
            "description": "A savory Japanese pancake containing a variety of ingredients such as cabbage, pork, shrimp, and topped with a special sauce, mayonnaise, dried seaweed, and bonito flakes.",
            "price": 650
        },
        "Agedashi Tofu": {
            "description": "Lightly battered and fried tofu served in a hot broth made of dashi, soy sauce, and mirin, and typically garnished with grated daikon radish and green onions.",
            "price": 789
        },
        "Karaage": {
            "description": "Japanese-style fried chicken, where bite-sized pieces of chicken are marinated in soy sauce, garlic, and ginger, then lightly coated in flour or starch and deep-fried..",
            "price": 750
        },
        "Nasu Dengaku (Miso Glazed Eggplant)": {
            "description": "Eggplant slices broiled or grilled and topped with a sweet and savory miso glaze, often garnished with sesame seeds or green onions.",
            "price": 560,
        "rice" : {
            "discription" : "A white graine tha typicaly acompays is a side to asain foods",
            "price" : 400
        }
        },
    }
    lsides = list(sides)

    desserts = {
        "Mochi": {
            "description": "A sweet rice cake made of mochigome (a short-grain japonica glutinous rice), often filled with sweet red bean paste and can come in various flavors like matcha (green tea), strawberry, or kinako (roasted soybean flour).",
            "price": 400
        },
        "Matcha Ice Cream": {
            "description": " A creamy and rich ice cream flavored with matcha green tea, known for its vibrant green color and unique taste.",
            "price": 540
        },
        "Dorayaki": {
            "description": "A type of Japanese confection consisting of two small pancake-like patties made from castella wrapped around a filling of sweet red bean paste.",
            "price": 350
        },
        "Taiyaki": {
            "description": "A fish-shaped cake, usually filled with red bean paste or custard, and made from a waffle or pancake-like batter.",
            "price": 200
        },
        "Daifuku": {
            "description": "A soft mochi (glutinous rice cake) stuffed with sweet filling, most commonly anko (sweet red bean paste). Varieties may include fruit, like strawberry (ichigo daifuku), or ice cream.",
            "price": 350
        },
        "Anmitsu": {
            "description": "A traditional Japanese dessert made with small cubes of agar jelly, fruits, mochi, red bean paste, and often served with black sugar syrup and a scoop of ice cream.",
            "price": 900
        },
        "Kakigori": {
            "description": "A shaved ice dessert flavored with syrup and often other ingredients such as sweetened condensed milk, fruit, or red bean paste.",
            "price": 1000
        },
        "Yokan": {
            "description": "A thick, jellied dessert made of red bean paste, agar, and sugar. It often comes in a block form and can be sliced into pieces.",
            "price": 500
        },
        "Castella": {
            "description": "A popular Japanese sponge cake made of sugar, flour, eggs, and starch syrup, known for its moist and fluffy texture.",
            "price": 800
        },
        "Sakura Mochi": {
            "description": "A seasonal mochi dessert wrapped in a pickled cherry leaf, typically filled with sweet red bean paste and associated with the cherry blossom season.",
            "price": 350
        },
    }
    ldesserts = list(desserts)
    drinks = {
        "Green Tea (Matcha or Sencha)": {
            "description": "raditional Japanese green tea, which can be served either as matcha (a finely ground, powdered green tea) or sencha (a type of loose leaf green tea). Both are known for their health benefits and refreshing taste.",
            "price": 400
        },
        "Sake": {
            "description": "A Japanese rice wine made by fermenting rice that has been polished to remove the bran. It can be served warm or cold and comes in various grades and styles.",
            "price": 1000
        },
        "Ramen Soda": {
            "description": "A unique and refreshing Japanese carbonated soft drink, often with unusual flavors like melon, lychee, or even wasabi.",
            "price": 300
        },
        "Umeshu (Plum Wine)": {
            "description": "A sweet and fruity wine made from Japanese ume plums, sugar, and alcohol. It's often served on the rocks, mixed with soda, or used in cocktails.",
            "price": 500
        },
        "Asahi or Sapporo Beer": {
            "description": "Popular Japanese beers that are crisp and light, pairing well with a wide range of Japanese dishes.",
            "price":600
        },
    }
    ldrinks = list(drinks)
class japanese_menu:
    entree = {
    "寿司と刺身": {
        "description": "新鮮な魚、貝、その他の海鮮類を生または軽く酢で味付けしたご飯と一緒に提供。選択肢にはマグロ、サーモン、ハマチ、ウナギ、エビなどが含まれます。",
        "price": 1950
    },
    "天ぷら": {
        "description": "軽く衣を付けて揚げた海鮮と野菜、つけダレと一緒に提供。人気のアイテムにはエビ、サツマイモ、ナス、インゲンがあります。",
        "price": 1950
    },
    "照り焼き": {
        "description": "グリルまたは焼きで仕上げた肉（鶏肉、牛肉、または魚）を醤油、みりん、砂糖で作った甘辛いソースでグレーズ。",
        "price": 1450
    },
    "ラーメン": {
        "description": "濃厚なブロス、小麦麺、豚肉のスライス、ネギ、海苔（のり）、ゆで卵などの様々なトッピングが特徴の麺スープ料理。",
        "price": 850
    },
    "うどん・そば": {
        "description": "太いうどん麺または細いそば麺を、熱いブロスで提供、または冷たいつけダレで。トッピングには天ぷら、豆腐、ネギ、海苔などがあります。",
        "price": 1600
    },
    "とんかつ": {
        "description": "パン粉を付けて揚げた豚カツレツで、通常はキャベツサラダと甘酸っぱいソースと一緒に提供されます。",
        "price": 1522
    },
    "焼き鳥": {
        "description": "串に刺して焼いた鶏肉のピースで、もも肉、胸肉、翼、つくね（鶏肉のミートボール）など、鶏肉のさまざまな部位を含みます。",
        "price": 522
    },
    "カツ丼": {
        "description": "ご飯の上に、揚げた豚カツレツ、卵、野菜、甘辛いソースをのせたどんぶり料理。",
        "price": 950
    },
    "茶碗蒸し": {
        "description": "鶏肉、エビ、椎茸などの具材を含んだ、通常は小さなカップやボウルで蒸して提供される、風味豊かな卵の蒸し物。",
        "price": 550
    },
    "うなぎ丼（うな丼）": {
        "description": "甘い醤油ベースのソースでグレーズしたうなぎの蒲焼きをご飯の上にのせた丼料理。しばしば漬物を添えて、時には山椒（日本のこしょう）を振りかけて提供されます。",
        "price": 2087
    }
    }
    lentrees = list(entree)

    sides = {
        "枝豆": {
            "description": "軽く塩を振った若い緑の大豆をさや付きで提供。蒸したり茹でたりして、シンプルで風味豊かなスターターです。",
            "price": 350
        },
        "味噌汁": {
            "description": "味噌ペースト（発酵した大豆ペースト）、出汁（日本のスープストック）、豆腐、海藻、ネギなどの様々な材料で作られる伝統的なスープ。",
            "price": 300
        },
        "漬物（日本のピクルス）": {
            "description": "キュウリ、大根、ナス、生姜など、さまざまな野菜のアソートメント。サクサクした食感と爽やかな味わいが特徴です。",
            "price": 350
        },
        "胡麻和え": {
            "description": "ほうれん草やいんげんなどの野菜を、甘くて風味豊かな胡麻ドレッシングで和えたもの。",
            "price": 520
        },
        "酢の物": {
            "description": "薄くスライスしたキュウリ、海藻、時にはカニやエビを使い、酢のドレッシングで和えたさっぱりとしたサラダ。",
            "price": 432
        },
        "たこ焼き": {
            "description": "小麦粉ベースの生地で作り、ミンチ状またはさいの目に切ったタコ、天かす、紅ショウガ、ネギを入れて焼いたボール状のスナック。",
            "price": 1450
        },
        "お好み焼き": {
            "description": "キャベツ、豚肉、エビなどのさまざまな材料を含む、日本のお好みで作る風味豊かなパンケーキ。特製ソース、マヨネーズ、乾燥海藻、鰹節をトッピングしています。",
            "price": 600
        },
        "揚げ出し豆腐": {
            "description": "軽く衣を付けて揚げた豆腐を、出汁、醤油、みりんで作った熱いブロスに入れて提供。通常は大根おろしとネギでトッピングされます。",
            "price": 739
        },
        "唐揚げ": {
            "description": "一口大に切った鶏肉を醤油、にんにく、生姜に漬け込み、薄力粉やでんぷんで軽くコーティングして揚げた、日本式のフライドチキン。",
            "price": 700
        },
        "茄子の田楽（味噌グレーズ）": {
            "description": "焼いたりグリルしたりしたナスのスライスに、甘辛い味噌ベースのグレーズをかけたもの。しばしばゴマやネギで飾られます。",
            "price": 510
        },
        "ライス" : {
            "description" : "通常アジア料理の付け合わせとして提供される白い穀物",
            "price" : 400
}

    }
    lsides = list(sides)

    desserts = {
        "餅（もち）": {
            "description": "もち米（短粒種のもち米）で作られた甘いお餅で、通常は甘い小豆ペーストで詰められ、抹茶（緑茶）、イチゴ、きな粉（焙煎大豆粉）などの様々なフレーバーがあります。",
            "price": 350
        },
        "抹茶アイスクリーム": {
            "description": "抹茶（緑茶）で風味付けされたクリーミーで濃厚なアイスクリーム。その鮮やかな緑色と独特な味わいが特徴です。",
            "price": 490
        },
        "どら焼き": {
            "description": "カステラで作られた小さなパンケーキ状のパティ2枚で、甘い小豆ペーストをサンドした日本の菓子。",
            "price": 300
        },
        "たい焼き": {
            "description": "魚の形をしたケーキで、通常は小豆ペーストやカスタードで詰められ、ワッフルまたはパンケーキのような生地で作られます。",
            "price": 150
        },
        "大福": {
            "description": "甘い詰め物、最も一般的にはあんこ（甘い小豆ペースト）が入った柔らかい餅（もち）。バリエーションには果物、例えばイチゴ（いちご大福）やアイスクリームが含まれることがあります。",
            "price": 300
        },
        "あんみつ": {
            "description": "寒天ゼリーの小さな立方体、果物、餅、小豆ペーストを使った伝統的な日本のデザートで、しばしば黒糖シロップとアイスクリームを添えて提供されます。",
            "price": 850
        },
        "かき氷": {
            "description": "シロップで味付けされたかき氷のデザートで、しばしば練乳、果物、小豆ペーストなどの他の材料が加えられます。",
            "price": 950
        },
        "羊羹（ようかん）": {
            "description": "小豆ペースト、寒天、砂糖を使って作られる濃厚なゼリー状のデザート。しばしばブロック状になっており、スライスして提供されます。",
            "price": 450
        },
        "カステラ": {
            "description": "砂糖、小麦粉、卵、水飴で作られる人気の日本のスポンジケーキ。そのしっとりとしたふわふわの食感が特徴です。",
            "price": 750
        },
        "桜餅": {
            "description": "塩漬けの桜の葉で包まれた季節限定の餅デザートで、通常は甘い小豆ペーストで詰められ、桜の花見シーズンに関連しています。",
            "price": 300
        }
    }
    ldesserts = list(desserts)

    drinks = {
    "緑茶（抹茶または煎茶）": {
        "description": "伝統的な日本の緑茶で、抹茶（細かく挽いた粉末状の緑茶）または煎茶（緩く葉の形をした緑茶）として提供されます。どちらも健康効果と爽やかな味わいで知られています。",
        "price": 350
    },
    "日本酒": {
        "description": "米を磨いてぬかを取り除いた後に発酵させて作られる日本の米ワイン。温かく、または冷たく提供され、さまざまなグレードやスタイルがあります。",
        "price": 950
    },
    "ラムネソーダ": {
        "description": "メロン、ライチ、ワサビなどの珍しいフレーバーが特徴の、ユニークで爽快な日本の炭酸ソフトドリンク。",
        "price": 250
    },
    "梅酒（プラムワイン）": {
        "description": "日本の梅、砂糖、アルコールから作られる甘くてフルーティーなワイン。ロックで、ソーダで割って、またはカクテルに使って提供されることが多いです。",
        "price": 450
    },
    "アサヒまたはサッポロビール": {
        "description": "軽くてさっぱりした味わいが特徴の人気の日本のビール。多様な日本料理とよく合います。",
        "price": 550
    }
    }
    ldrinks = list(drinks)