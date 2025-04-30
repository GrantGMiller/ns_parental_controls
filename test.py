import os
import json

from gm_nintendo_parental import ParentalControl


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
    callback_kwargs={'random': 'kwargs'}
)

if not pc.access_token:
    if not pc.session_token:
        print(pc.get_auth_url())
        pc.process_auth_link(input('copy paste the link here:\n'))
    else:
        pc.get_new_access_token()

pc.lock_device('Grant', False)
