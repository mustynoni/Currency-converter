import requests
import os
import datetime
import json


def get_exchange_rates(url, rate_file):
    today = datetime.datetime.today()

    # rate file does not exist
    if not os.path.exists(rate_file):
        download_exchange_rate_to_file(url, rate_file)
    else:
        last_modified_ts = os.path.getmtime(rate_file)
        last_modified = datetime.datetime.fromtimestamp(last_modified_ts)

        # when today date and the file last modified date are not the same
        if today.day != last_modified.day:
            download_exchange_rate_to_file(url, rate_file)

    # read the json file
    file_handler = open(rate_file, 'r')
    result = json.load(file_handler)
    file_handler.close()
    return result


def download_exchange_rate_to_file(url, rate_file):
    response = requests.get(url)

    if response.status_code == requests.codes.ok:
        result = response.json()
        if result['success']:
            file_handler = open(rate_file, 'w')
            json.dump(result, file_handler)
            file_handler.close()
        else:
            pass
            # throw exception
