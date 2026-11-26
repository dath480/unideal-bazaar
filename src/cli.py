from core.core import fetch, get_price


def run() -> None:
    auto_fetch: bool = False

    try:
        item_dict = fetch()
    except:
        return

    while True:
        print("Options:     AutoFetch     Update     Item Id     Exit")
        input_string: str = input()

        match input_string.lower():
            case "exit":
                print("Exited")
                break
            case "autofetch":
                auto_fetch = not auto_fetch
                print("AutoFetch: " + str(auto_fetch))
            case "update":
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
                get_price(item_dict, input_string.upper())
    return