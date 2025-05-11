import json
import os

import config
from ns_parental_controls import ParentalControl


def save(**k):
    with open('test.json', 'wt') as file:
        file.write(json.dumps(k, indent=2))


def load(**k):
    if not os.path.isfile('test.json'):
        return k

    try:
        with open('test.json', 'rt') as file:
            return json.load(file)
    except Exception as e:
        print(e)
        return k


pc = ParentalControl(
    save_state_callback=save,
    load_state_callback=load,
    callback_kwargs={'random': 'kwargs'},
    debug=True
)

if not pc.access_token:
    if not pc.session_token:
        print(pc.get_auth_url())
        pc.process_auth_link(input('copy paste the link here:\n'))
    else:
        pc.get_new_access_token()

# pc.lock_device('My NS', False)
# pc.set_playtime_minutes_for_today(config.DEVICE_LABEL, 30)
# pc.add_playtime_minutes_for_today(config.DEVICE_LABEL, 30)
# dev = pc.get_device('Grant')
pc.get_today_playtime_minutes('Grant')