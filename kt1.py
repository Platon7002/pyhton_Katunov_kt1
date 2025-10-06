import random

def babushka_chat():

    print("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!")

    count_poka = 0 

    while True:

        user_input = input("> ")

        if "ПОКА!" in user_input:

            count_poka += user_input.count("ПОКА!")

            if count_poka >= 3:

                print("ДО СВИДАНИЯ, МИЛЫЙ!")

                break

            else:

                random_year = random.randint(1930, 1950)

                responses = [

                    f"НЕТ, НИ РАЗУ С {random_year} ГОДА!",

                    f"КАК СКАЖУ, С {random_year} ГОДА НИ РАЗУ!",

                    f"ОЙ, НЕТ! С {random_year} ГОДА Я НЕ СЛЫШАЛА!"

                ]

                print(random.choice(responses))

        elif user_input.isupper():

            random_year = random.randint(1930, 1950)

            responses = [

                f"НЕТ, НИ РАЗУ С {random_year} ГОДА!",

                f"КАК СКАЖУ, С {random_year} ГОДА НИ РАЗУ!",

                f"ОЙ, НЕТ! С {random_year} ГОДА Я НЕ СЛЫШАЛА!"

            ]

            print(random.choice(responses))

        else:

            responses = [

                "АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!",

                "Я НЕ СЛЫШУ ТЕБЯ, ГОВОРИ ГРОМЧЕ!",

                "ЧЕГО? ГОВОРИ ЯСНЕЕ, МИЛОК!"

            ]

            print(random.choice(responses))

babushka_chat()
