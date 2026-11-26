import requests
import datetime
from requests import Response
from datetime import datetime

URL = "https://api.hypixel.net/v2/skyblock/bazaar"


def fetch() -> dict:
    raw_dictionary: dict = {}

    try:
        contents: Response = requests.get(URL)
        raw_dictionary = contents.json()["products"]
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to Hypixel API")
        raise
    except requests.Timeout:
        print("Error: Timeout")
        raise
    except requests.HTTPError:
        print("Error: HTTP Error")
        raise

    id_price_dict: dict = {}

    for item in raw_dictionary.keys():
        id_price_dict[item] = raw_dictionary[item]["quick_status"]["buyPrice"]

    return id_price_dict


def find_matches(key_list: list, target: str) -> list:
    match_list: list = key_list.copy()
    tmp_list: list = []

    try:
        key_list.index(target)
    except ValueError:
        for i in range(len(target)):
            for key in match_list:
                if len(key) < len(target):
                    continue

                if key[i] == target[i]:
                    tmp_list.append(key)
            match_list = tmp_list
            tmp_list = []
        return match_list

    tmp_list.append(target)
    return tmp_list

"""
def q_typo_detect(c: str, t: str) -> bool:
    q_typo_dict: dict[str , str] = {
        "A": "AQWSZ",
        "B": "BVGHN ",
        "C": "CXDFV ",
        "D": "DSERFCX",
        "E": "E234RDSW",
        "F": "FDRTGVC",
        "G": "GFTYHBV",
        "H": "HGYUJNB",
        "I": "IU789OKJ",
        "J": "JHUIKMN",
        "K": "KJIOL,M",
        "L": "LKOP;.,",
        "M": "MNJK, ",
        "N": "NBHJM ",
        "O": "OI890PLK",
        "P": "PO90-[;L",
        "Q": "Q`12WA",
        "R": "RE345TFD",
        "S": "SWEDXZA",
        "T": "TR456YGF",
        "U": "UY678IJH",
        "V": "VCFGB ",
        "W": "WQ123ESA",
        "X": "XZSDC ",
        "Y": "YT567UHG",
        "Z": "ZASX",
        "_": "-0P[]="
    }

    try:
        if q_typo_dict[c].find(t) != -1:
            return True
        else:
            return False
    except KeyError:
        return False
"""

def weighted_cmp(key_list: list, target: str) -> str:
    top_contestant: str = "None"
    top_compatibility: float = 0.0

    for key in key_list:
        match_count: int = 0

        for i in range(min(len(key), len(target))):
            if key[i] == target[i]:
                match_count += 1

        compatibility = match_count/max(len(key), len(target))
        if (compatibility > top_compatibility) and (compatibility > 0.4):
            top_contestant = key
            top_compatibility = compatibility

    return top_contestant


def get_price(dictionary: dict, target: str) -> None:
    key_list: list = list(dictionary.keys())
    match_list: list = find_matches(key_list, target)

    match len(match_list):
        case 1:
            print(match_list[0])
            print(dictionary[match_list[0]])
        case 0:
            print("Item not found")

            if (tmp := weighted_cmp(key_list, target)) != "None":
                print("Did you mean " + tmp + "?")
        case _:
            print(*match_list, sep="   ")
    return None

class BuyPrices:

    id_price_dict: dict = {}
    last_fetch_time: datetime = None

    def Update(self) -> None:
        try:
            self.id_price_dict = fetch()
        except:
            raise


    def FetchPrices(self) -> dict:
        now: datetime = datetime.now()
        
        if (now - self.last_fetch_time).seconds >= 60:
            print("fetched")
            self.Update()
            self.last_fetch_time = now
        else:
            print("cached")
        return self.id_price_dict
    

    def __init__(self) -> None:
        self.Update()
        self.last_fetch_time = datetime.now()
