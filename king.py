s = input('Input "start" to continue: ')
if s.lower() == 'start':
    print('Are You Gay..')
    print('Well if U think U are Come Up Here And Check')
    print('Welcome To Gay Checker')
    print('type kinggy to continue')

    vv = input()
    if vv.lower() == 'kinggy':
        print('Tell me your name:')
        name = input()

        if name.lower() == 'gaybriel':
            print('No need for test You Are Gay')
        else:
            print(f'So {name}, you must be 100% straight... or maybe not 😏')
            print('Now I will ask you some questions')
            print('Answer with yes or no')

            questions = [
                "Do you like to wear pink?",
                "Do you enjoy watching romantic movies?",
                "Do you prefer shopping over sports?",
                "Do you like to dance?",
                "Do you enjoy cooking?",
                "Do you like to gossip?",
                "Do you enjoy fashion and style?",
                "Do you like to talk about feelings?",
                "Do you enjoy spending time with friends?",
                "Do you like to go to parties?",
            ]

            score = 0

            for question in questions:
                answer = input(question + " (yes/no): ").strip().lower()
                if answer == 'yes':
                    print("Interesting!")
                    score += 1
                elif answer == 'no':
                    print("Okay, noted.")
                else:
                    print("Please answer with 'yes' or 'no'.")

            # Decide result
            if score >= 7:
                print(r"""
   _____      _   _   _   _   _   _ 
  / ____|    | | | | | | | | | | | |
 | |  __  ___| |_| |_| |_| |_| |_| |
 | | |_ |/ _ \ __| __| __| __| __| |
 | |__| |  __/ |_| |_| |_| |_| |_|_|
  \_____|\___|\__|\__|\__|\__|\___/
Why Are You GAY 🌈
""")
            elif score >= 4:
                print("\n--- RESULT ---")
                print("Hmm... I just hope we don't lose you to the dark side.")
            else:
                print("\n--- RESULT ---")
                print("Stand Strong Soldier 🏹")
                print('Powered by King')
