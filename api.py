import requests
import json

# Returns a pokemon object with information such as name and types
def get_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")

    pokemon = json.loads(response.text)

    return pokemon

# Returns a pokemon species with information such as name and evolution chain
def get_pokemon_species(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{name}")

    pokemon_species = json.loads(response.text)

    return pokemon_species

# Returns the evolution chain of a pokemon species
def get_evolution_chain(pokemon_species):
    response = requests.get(pokemon_species["evolution_chain"]["url"])

    evolution_chain = json.loads(response.text)

    return evolution_chain

# Returns a full list of names in the evolution chain of a pokemon
# Input is the chain for a specific pokemon
def get_pokemon_names_in_chain(chain):
    pokemon_in_evolution_chain = []
    # Add first pokemon
    pokemon_in_evolution_chain.append(chain["species"]["name"])

    # A pokemon can evolve into multiple pokemons
    for pokemon in chain["evolves_to"]:
        pokemon_in_evolution_chain = pokemon_in_evolution_chain + get_pokemon_names_in_chain(pokemon)

    return pokemon_in_evolution_chain

