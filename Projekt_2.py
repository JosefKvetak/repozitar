import random
import time

def generate_secret():
    digits = list('0123456789')
    while True:
        secret = random.sample(digits, 4)
        if secret[0] != '0':
            return ''.join(secret)

def is_valid_guess(guess):
    if len(guess) != 4:
        return False, "Tip musí mít přesně 4 číslice."
    if not guess.isdigit():
        return False, "Tip musí obsahovat pouze číslice."
    if guess[0] == '0':
        return False, "Tip nesmí začínat nulou."
    if len(set(guess)) != 4:
        return False, "Číslice se nesmějí v tipu opakovat."
    return True, ""

def count_bulls_and_cows(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum((min(secret.count(d), guess.count(d)) for d in set(guess))) - bulls
    return bulls, cows

def pluralize(word, count):
    if count == 1:
        return word
    else:
        return word + 's'

def main():
    print("Vítejte ve hře Bulls and Cows!")
    print("Mám na mysli tajné čtyřmístné číslo s unikátními číslicemi, které nesmí začínat nulou.")
    print("Vaším úkolem je uhodnout číslo.")
    secret = generate_secret()

    start_time = time.time()

    while True:
        guess = input("Zadejte svůj tip: ").strip()
        valid, message = is_valid_guess(guess)
        if not valid:
            print("Neplatný tip:", message)
            continue

        bulls, cows = count_bulls_and_cows(secret, guess)
        print(f"{bulls} {pluralize('bull', bulls)} a {cows} {pluralize('cow', cows)}")

        if bulls == 4:
            end_time = time.time()
            elapsed = end_time - start_time
            mins, secs = divmod(elapsed, 60)
            print(f"Gratuluji! Uhodli jste tajné číslo za {int(mins)} minut a {int(secs)} sekund.")
            break

if __name__ == "__main__":
    main()