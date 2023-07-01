from Repository.Read_data import store
def get_total_price():
    items = {'rice': 20, 'sugar': 30, 'salt': 20, 'oil': 80, 'paneer': 110, 'maggi': 50, 'boost': 90, 'colgate': 85}
    total_price = 0
    qty = 0
    plist = []
    for sto in store:
        qty = sto['quantity']
        x = sto['product_name']
        if x in items.keys():
              price = qty * items[x]
              total_price += price
        else:
            print("Sorry you enter item  is not available ")
    return total_price
