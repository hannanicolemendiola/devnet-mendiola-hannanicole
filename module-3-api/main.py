import requests
import random

url_list = [
    'https://pokeapi.co/api/v2/pokemon/71',
    'https://pokeapi.co/api/v2/pokemon/6',
    'https://pokeapi.co/api/v2/pokemon/250',
    'https://pokeapi.co/api/v2/pokemon/249',
    'https://pokeapi.co/api/v2/pokemon/214'
]

pokemon = random.choice(url_list)
response = requests.get(pokemon)
pokemon_data = response.json()

all_response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
all_data = all_response.json()
all_pokemon = all_data["results"]

print("=== Guess the Pokémon! ===")
print(f"Height: {pokemon_data['height']}")
print(f"Weight: {pokemon_data['weight']}")
lives = 3

while lives > 0:
    guess = input("Your guess: ").lower()
    if guess == pokemon_data['name']:
        print("Correct!")
        break
    else:
        lives -= 1
        if any(names['name'] == guess for names in all_pokemon):
            print(f"Wrong Pokémon! Please try again.\nLives left: {lives}")
        else:
            print(f"Invalid Pokémon name! Please try again.\nLives left: {lives}")
        if lives == 0:
            print(f"Game over! The correct Pokémon is {pokemon_data['name'].capitalize()}.")