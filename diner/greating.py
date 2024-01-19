import random
from enlgish_interactions import english
from japanese_interactions import japanese
#welcome message
greatings = ["good morning","good afternoon", "good evening", "we are closed"]
great = random.choice(greatings)

def great_man(great):
    pass
    if great == "good morning":
        return ("""good morning
                  おはようございます """)
    elif great == "good afternoon":
        return("""good afternoon
                 こ ん に ち は""")
    elif great == "good evening":
        return("""good eavning
                こ ん ば ん は""")
    elif great == "we are closed":
        print ("""we are closed come back another time
                  ただいま閉店しています。またのお越しをお待ちしております。""")
        exit()
    else:
        print("""Error greating not found please try again or call out customer service at (+81 562-788-6942)
                 エラー: 挨拶が見つかりません。もう一度お試しください、またはカスタマーサービス（+81 562-788-6942) にお電話ください。 """)
        exit()

print(great_man(great))

try:
    language = int(input("""would you like japanese or english? (1 for japnese 2 for english)
                       日本語と英語のどちらをご希望ですか? (1は日本語、2は英)"""))
except ValueError:
    print ("""Input Error: please ensure that you are only entering 1 or 2 and nothing else
               入力エラー:1または2のみを入力していることを確認してください。それ以外は入力しないでください。""")

if language == 1:
    japanese()
elif language == 2:
    english()
else:
    print("""Input Error: please ensure that you are only ussing 1 or 2 and no other number
              入力エラー:1または2のみを使用し、他の数字は使用しないでください。""")