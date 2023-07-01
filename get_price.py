from Repository.Read_data import read_store_data
from Services.calculateprice import get_total_price
def get_all():

    store_data = read_store_data()
    print()
    print(" -------your product list with quantity ------ ")
    for j in store_data:
        print(j)
    print()
    print("Your total Amount  is :", get_total_price())
    print("Thanks for shopping ")
