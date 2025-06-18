def main():
    empty_grocery_list = []
    empty_grocery_dict = {}
    updated_grocery_list = get_grocery(empty_grocery_list)
    grocery_food_w_num_dict = get_food_num(updated_grocery_list, empty_grocery_dict)
    grocery_display(grocery_food_w_num_dict)


def get_grocery(grocery_list):
        # will get the list of grocery
    while True:
        grocery_input = input().upper().strip()
        if grocery_input == "DONE":
            break
        elif grocery_input == "" or grocery_input == " " :
            continue
        else:
            grocery_list.append(grocery_input)
    return grocery_list


def get_food_num(updated_grocery_list, grocery_dict ):
        # will get the number of item per food in the grocery list and make dict
    for food in updated_grocery_list:      #will select the foods in the grocery_list
        if food in updated_grocery_list:
            food_num = updated_grocery_list.count(food)
            grocery_dict[food] = food_num
    return grocery_dict

def grocery_display(grocery_food_w_num_dict):
        #will display the food_num and food
    for display in grocery_food_w_num_dict:
        print(grocery_food_w_num_dict.get(display), display)


main()