cook_book_1 = {}
cook_book_2 = {}

def cook_book_creation(location, cook_book):
    with open(location, 'r', encoding='utf8') as file:
        for line in file:
            food = []
            ingredient_count = file.readline()
            for _ in range(int(ingredient_count)):
                ingredient_name, quantity, measure = file.readline().split(' | ')
                food.append({'ingredient_name' : ingredient_name, 'quantity' : quantity, 'measure' : measure.strip()})
            file.readline()
            cook_book.setdefault(line.strip(), food)

cook_book_creation('Files/recipes.txt', cook_book_1)
cook_book_creation('Files/recipes_2.txt', cook_book_2)

# print(cook_book)

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    x = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in x.keys():
                pass
                x[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity'])*person_count
            else:
                x.setdefault(ingredient['ingredient_name'], {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity'])*person_count})
    return(x)

print(get_shop_list_by_dishes(cook_book_1, ['Запеченный картофель', 'Омлет'], 2))
print(get_shop_list_by_dishes(cook_book_2, ['Хлеб', 'Блины', 'Кекс'], 5))