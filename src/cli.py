from core.core import get_price, BuyPrices

def run() -> None:
    try:
        price_cacher: BuyPrices = BuyPrices()
    except:
        return

    item_dict: dict = {}

    while True:
        print("Options:     Item Id     Exit\n")
        input_string: str = input().upper()
        match input_string:
            case "EXIT":
                print("Exited")
                break
            case _:
                try:
                    item_dict = price_cacher.FetchPrices()
                    get_price(item_dict, input_string)
                except:
                    return
    return