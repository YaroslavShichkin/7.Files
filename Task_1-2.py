cook_book = {}

with open('Files/recipes.txt', 'r', encoding='utf8') as file:
    for line in file:
        food = []
        ingredient_count = file.readline()
        for _ in range(int(ingredient_count)):
            ingredient_name, quantity, measure = file.readline().split(' | ')
            food.append({'ingredient_name' : ingredient_name, 'quantity' : quantity, 'measure' : measure.strip()})
        file.readline()
        cook_book.setdefault(line.strip(), food)

print(cook_book)