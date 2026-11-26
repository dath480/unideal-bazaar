from core.core import fetch, get_price


def run() -> None:
    auto_fetch: bool = False

    try:
        item_dict = fetch()
    except:
        return

    while True:
        print("Options:     AutoFetch     Update     Item Id     Exit\n")
        input_string: str = input().upper()
        match input_string:
            case "EXIT":
                print("Exited")
                break
            case "AUTOFETCH":
                auto_fetch = not auto_fetch
                print("AutoFetch: " + str(auto_fetch))
            case "UPDATE":
                try:
                    fetch()
                except:
                    return
                print("Updated")
            case _:
                if auto_fetch:
                    try:
                        fetch()
                    except:
                        return
                get_price(item_dict, input_string)
    return