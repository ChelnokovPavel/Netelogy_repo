from pprint import pprint


with open('recipes.txt') as recipes:
    cook_book = {}
    for recipe in recipes:
        recipe_name = recipe.strip()
        counter = int(recipes.readline().strip())
        temp_data = []
        for i in range(counter):
            ingredients = [x.strip() for x in recipes.readline().split('|')]
            ingredients_dict = {'ingredient_name': ingredients[0],
                                'quantity': ingredients[1],
                                'measure': ingredients[2]}
            temp_data.append(ingredients_dict)
        cook_book[recipe_name] = temp_data
        recipes.readline()


dishes = ['Запеченный картофель', 'Омлет']


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    ingredients = [cook_book[x] for x in dishes]
    for ingredient in ingredients:
        for ingr in ingredient:
            temp_dict = ingr.copy()
            key = temp_dict['ingredient_name']
            temp_dict.pop('ingredient_name')
            if key in shop_list:
                temp_dict['quantity'] = int(shop_list[key]['quantity']) + (int(temp_dict['quantity']) * person_count)
            else:
                temp_dict['quantity'] = int(temp_dict['quantity']) * person_count
            shop_list[key] = temp_dict
    return shop_list


pprint(get_shop_list_by_dishes(dishes, 3))


with open('file_1.txt') as f1, open('file_2.txt') as f2, open('file_3.txt', 'w') as f3:
    f1_read = f1.read()
    f2_read = f2.read()
    f1_list = f1_read.split('\n')
    f2_list = f2_read.split('\n')
    if len(f1_list) < len(f2_list):
        f3.writelines(f'{f1.name}\n')
        f3.writelines(f'{len(f1_list)}\n')
        f3.writelines(f'{f1_read}\n')
        f3.writelines(f'{f2.name}\n')
        f3.writelines(f'{len(f2_list)}\n')
        f3.writelines(f'{f2_read}\n')
    else:
        f3.writelines(f'{f2.name}\n')
        f3.writelines(f'{len(f2_list)}\n')
        f3.writelines(f'{f2_read}\n')
        f3.writelines(f'{f1.name}\n')
        f3.writelines(f'{len(f1_list)}\n')
        f3.writelines(f'{f1_read}\n')
