from shop_adapter import ShopAdapter
import time

def main():

    while(True):
        print(ShopAdapter().search_offers())
        time.sleep(5)

    
    

if __name__ == "__main__":
    main()