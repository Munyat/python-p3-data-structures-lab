spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return[spicy["name"] for spicy in spicy_foods]

    pass

def get_spiciest_foods(spicy_foods):
    return[spicy for spicy in spicy_foods if spicy["heat_level"] > 5]
    pass

def print_spicy_foods(spicy_foods):
    for spicy in spicy_foods:
        print(f'{spicy["name"]} ({spicy["cuisine"]}) | Heat Level: {"🌶" *spicy["heat_level"]}')
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy in spicy_foods:
        if spicy["cuisine"] == cuisine:
            return spicy
    pass

def print_spiciest_foods(spicy_foods):
    for spicy in spicy_foods:
        if spicy["heat_level"] > 5:
            print(f'{spicy["name"]} ({spicy["cuisine"]}) | Heat Level: {"🌶" *spicy["heat_level"]}')
    pass

def get_average_heat_level(spicy_foods):
    total = 0 
    for spicy in spicy_foods:
        total += spicy["heat_level"]
    return total // len(spicy_foods)
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
