"""
usage:
python fibrerollout.py --exchange COT
 OR
python fibrerollout.py --exchange COT --exchange KBE
"""
import argparse

import requests
from gooey import Gooey

NETWORKMAPS_JS = "http://www.openeir.ie/js/app/eircom.networkmaps.js"


def get_exchange_data(exchange_codes):
    networkmaps_js = requests.get(NETWORKMAPS_JS)
    nga_exchange_lists = [line for line in networkmaps_js.text.split('\n') if
                          "com/nga-exchange" in line]
    if nga_exchange_lists:
        # We only use one so get the first
        nga_exchange_list = nga_exchange_lists[0]
        nga_exchange_list_url = nga_exchange_list.strip()[7:-2]
        nga_exchange_csv = requests.get(nga_exchange_list_url)
        for exchange_code in exchange_codes:
            nga_exchanges = [line for line in nga_exchange_csv.text.split('\n')
                             if ',%s' % exchange_code.strip() in line]
            if nga_exchanges:
                for nga_exchange in nga_exchanges:
                    exchange_data = nga_exchange.strip().split(',')
                    print('%s - %s' % (exchange_data[2], exchange_data[-1]))
            else:
                print('No fibre rollout data found for that exchange')
        print('Source: %s' % nga_exchange_list_url)


@Gooey
def main():
    parser = argparse.ArgumentParser(
        description='Simple script to pull fibre rollout exchange data')
    parser.add_argument('--exchange', action="store", dest="exchange_codes",
                        required=True,
                        help="Separate multiple exchange codes with comma")
    args = parser.parse_args()

    if not args.exchange_codes:
        print("You must specify at least one exchange code.")

    get_exchange_data(args.exchange_codes.split(","))


if __name__ == '__main__':
    main()
