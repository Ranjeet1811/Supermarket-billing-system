store = []


def read_store_data():
    user_name = input("Enter your name : ")
    print("Welcome to Karan Karyana Store Mr.", user_name)

    list1 = '''
    rice     Rs 20/kg
    sugar    Rs 30/kg
    salt     Rs 20?kg
    oil      Rs 80/kg
    paneer   Rs 110/kg
    maggi    Rs 50/kg
    boost    Rs 90/kg
    colgate  Rs 85/eacg 
    '''
    option = int(input("For list of items press 1 "))
    if option == 1:
        print(list1)
    while True:
        st = {}
        p_name = input("Enter the product name (or 'q' to quit) :  ")
        if p_name == 'q':
            break
        st['product_name'] = p_name
        quantity = int(input("Enter the quantity  : "))
        st['quantity'] = quantity
        store.append(st)
    return store
