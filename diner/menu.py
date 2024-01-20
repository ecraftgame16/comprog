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
            "price": 560
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
    entrees = {
    "寿司と刺身": {
        "説明": "新鮮な魚、貝、その他の海鮮類を生または軽く酢で味付けしたご飯と一緒に提供。選択肢にはマグロ、サーモン、ハマチ、ウナギ、エビなどが含まれます。",
        "価格": 1950
    },
    "天ぷら": {
        "説明": "軽く衣を付けて揚げた海鮮と野菜、つけダレと一緒に提供。人気のアイテムにはエビ、サツマイモ、ナス、インゲンがあります。",
        "価格": 1950
    },
    "照り焼き": {
        "説明": "グリルまたは焼きで仕上げた肉（鶏肉、牛肉、または魚）を醤油、みりん、砂糖で作った甘辛いソースでグレーズ。",
        "価格": 1450
    },
    "ラーメン": {
        "説明": "濃厚なブロス、小麦麺、豚肉のスライス、ネギ、海苔（のり）、ゆで卵などの様々なトッピングが特徴の麺スープ料理。",
        "価格": 850
    },
    "うどん・そば": {
        "説明": "太いうどん麺または細いそば麺を、熱いブロスで提供、または冷たいつけダレで。トッピングには天ぷら、豆腐、ネギ、海苔などがあります。",
        "価格": 1600
    },
    "とんかつ": {
        "説明": "パン粉を付けて揚げた豚カツレツで、通常はキャベツサラダと甘酸っぱいソースと一緒に提供されます。",
        "価格": 1522
    },
    "焼き鳥": {
        "説明": "串に刺して焼いた鶏肉のピースで、もも肉、胸肉、翼、つくね（鶏肉のミートボール）など、鶏肉のさまざまな部位を含みます。",
        "価格": 522
    },
    "カツ丼": {
        "説明": "ご飯の上に、揚げた豚カツレツ、卵、野菜、甘辛いソースをのせたどんぶり料理。",
        "価格": 950
    },
    "茶碗蒸し": {
        "説明": "鶏肉、エビ、椎茸などの具材を含んだ、通常は小さなカップやボウルで蒸して提供される、風味豊かな卵の蒸し物。",
        "価格": 550
    },
    "うなぎ丼（うな丼）": {
        "説明": "甘い醤油ベースのソースでグレーズしたうなぎの蒲焼きをご飯の上にのせた丼料理。しばしば漬物を添えて、時には山椒（日本のこしょう）を振りかけて提供されます。",
        "価格": 2087
    }
    }
    lentrees = list(entrees)

    sides = {
        "枝豆": {
            "説明": "軽く塩を振った若い緑の大豆をさや付きで提供。蒸したり茹でたりして、シンプルで風味豊かなスターターです。",
            "価格": 350
        },
        "味噌汁": {
            "説明": "味噌ペースト（発酵した大豆ペースト）、出汁（日本のスープストック）、豆腐、海藻、ネギなどの様々な材料で作られる伝統的なスープ。",
            "価格": 300
        },
        "漬物（日本のピクルス）": {
            "説明": "キュウリ、大根、ナス、生姜など、さまざまな野菜のアソートメント。サクサクした食感と爽やかな味わいが特徴です。",
            "価格": 350
        },
        "胡麻和え": {
            "説明": "ほうれん草やいんげんなどの野菜を、甘くて風味豊かな胡麻ドレッシングで和えたもの。",
            "価格": 520
        },
        "酢の物": {
            "説明": "薄くスライスしたキュウリ、海藻、時にはカニやエビを使い、酢のドレッシングで和えたさっぱりとしたサラダ。",
            "価格": 432
        },
        "たこ焼き": {
            "説明": "小麦粉ベースの生地で作り、ミンチ状またはさいの目に切ったタコ、天かす、紅ショウガ、ネギを入れて焼いたボール状のスナック。",
            "価格": 1450
        },
        "お好み焼き": {
            "説明": "キャベツ、豚肉、エビなどのさまざまな材料を含む、日本のお好みで作る風味豊かなパンケーキ。特製ソース、マヨネーズ、乾燥海藻、鰹節をトッピングしています。",
            "価格": 600
        },
        "揚げ出し豆腐": {
            "説明": "軽く衣を付けて揚げた豆腐を、出汁、醤油、みりんで作った熱いブロスに入れて提供。通常は大根おろしとネギでトッピングされます。",
            "価格": 739
        },
        "唐揚げ": {
            "説明": "一口大に切った鶏肉を醤油、にんにく、生姜に漬け込み、薄力粉やでんぷんで軽くコーティングして揚げた、日本式のフライドチキン。",
            "価格": 700
        },
        "茄子の田楽（味噌グレーズ）": {
            "説明": "焼いたりグリルしたりしたナスのスライスに、甘辛い味噌ベースのグレーズをかけたもの。しばしばゴマやネギで飾られます。",
            "価格": 510
        }
    }
    lsides = list(sides)

    desserts = {
        "餅（もち）": {
            "説明": "もち米（短粒種のもち米）で作られた甘いお餅で、通常は甘い小豆ペーストで詰められ、抹茶（緑茶）、イチゴ、きな粉（焙煎大豆粉）などの様々なフレーバーがあります。",
            "価格": 350
        },
        "抹茶アイスクリーム": {
            "説明": "抹茶（緑茶）で風味付けされたクリーミーで濃厚なアイスクリーム。その鮮やかな緑色と独特な味わいが特徴です。",
            "価格": 490
        },
        "どら焼き": {
            "説明": "カステラで作られた小さなパンケーキ状のパティ2枚で、甘い小豆ペーストをサンドした日本の菓子。",
            "価格": 300
        },
        "たい焼き": {
            "説明": "魚の形をしたケーキで、通常は小豆ペーストやカスタードで詰められ、ワッフルまたはパンケーキのような生地で作られます。",
            "価格": 150
        },
        "大福": {
            "説明": "甘い詰め物、最も一般的にはあんこ（甘い小豆ペースト）が入った柔らかい餅（もち）。バリエーションには果物、例えばイチゴ（いちご大福）やアイスクリームが含まれることがあります。",
            "価格": 300
        },
        "あんみつ": {
            "説明": "寒天ゼリーの小さな立方体、果物、餅、小豆ペーストを使った伝統的な日本のデザートで、しばしば黒糖シロップとアイスクリームを添えて提供されます。",
            "価格": 850
        },
        "かき氷": {
            "説明": "シロップで味付けされたかき氷のデザートで、しばしば練乳、果物、小豆ペーストなどの他の材料が加えられます。",
            "価格": 950
        },
        "羊羹（ようかん）": {
            "説明": "小豆ペースト、寒天、砂糖を使って作られる濃厚なゼリー状のデザート。しばしばブロック状になっており、スライスして提供されます。",
            "価格": 450
        },
        "カステラ": {
            "説明": "砂糖、小麦粉、卵、水飴で作られる人気の日本のスポンジケーキ。そのしっとりとしたふわふわの食感が特徴です。",
            "価格": 750
        },
        "桜餅": {
            "説明": "塩漬けの桜の葉で包まれた季節限定の餅デザートで、通常は甘い小豆ペーストで詰められ、桜の花見シーズンに関連しています。",
            "価格": 300
        }
    }
    ldesserts = list(desserts)

    drinks = {
    "緑茶（抹茶または煎茶）": {
        "説明": "伝統的な日本の緑茶で、抹茶（細かく挽いた粉末状の緑茶）または煎茶（緩く葉の形をした緑茶）として提供されます。どちらも健康効果と爽やかな味わいで知られています。",
        "価格": 350
    },
    "日本酒": {
        "説明": "米を磨いてぬかを取り除いた後に発酵させて作られる日本の米ワイン。温かく、または冷たく提供され、さまざまなグレードやスタイルがあります。",
        "価格": 950
    },
    "ラムネソーダ": {
        "説明": "メロン、ライチ、ワサビなどの珍しいフレーバーが特徴の、ユニークで爽快な日本の炭酸ソフトドリンク。",
        "価格": 250
    },
    "梅酒（プラムワイン）": {
        "説明": "日本の梅、砂糖、アルコールから作られる甘くてフルーティーなワイン。ロックで、ソーダで割って、またはカクテルに使って提供されることが多いです。",
        "価格": 450
    },
    "アサヒまたはサッポロビール": {
        "説明": "軽くてさっぱりした味わいが特徴の人気の日本のビール。多様な日本料理とよく合います。",
        "価格": 550
    }
    }
    ldrinks = list(drinks)