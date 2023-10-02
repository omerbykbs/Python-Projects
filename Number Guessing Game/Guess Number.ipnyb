while True:
    guess = int(input("I'm thinking a number between 1 and 100. Can you guess it right? "))
    if (guess < 1 or guess > 100):
        print("OUT OF BOUNDS! Please try with a number between 1 and 100:")
        continue
    if (guess == num):
        print(f"BINGO! You found it in your {len(guesses)}. guess!")
        break
    guesses.append(guess)
    if guesses[-2]:
        if abs(guess-num) < abs(guesses[-2]-num):
            print('WARMER!')
        elif abs(guess-num) > abs(guesses[-2]-num):
            print('COLDER!')
        else:
            if abs(num-guesses[-2]) > 10:
                print('AS COLD AS BEFORE')
            else:
                print('AS WARM AS BEFORE')
    else:
        if abs(guess-num) <= 10:
            print("WARM!")
        else:
            print("COLD!")

