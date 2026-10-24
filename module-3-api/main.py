import requests
import random

url_list = [
    'https://pokeapi.co/api/v2/pokemon/71',
    'https://pokeapi.co/api/v2/pokemon/6',
    'https://pokeapi.co/api/v2/pokemon/250',
    'https://pokeapi.co/api/v2/pokemon/249',
    'https://pokeapi.co/api/v2/pokemon/214'
]

correct_pokemon = random.choice(url_list)
response = requests.get(correct_pokemon)
data = response.json()

print(data['name'])

print("=== Guess the Pokémon! ===")
print(f"Height: {data['height']}")
print(f"Weight: {data['weight']}")
lives = 3

while lives > 0:
    guess = input("Your guess: ")
    if guess == data['name']:
        print("Correct!")
        break
    else:
        lives -= 1
        print(f"Wrong! Please try again.\nLives left: {lives}")
        if lives == 0:
            print(f"Game over! The correct Pokémon is {data['name']}.")
