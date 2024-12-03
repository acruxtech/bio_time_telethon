import time
from datetime import datetime, timedelta
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from config import API_ID, API_HASH
from utils import time_has_changed


client = TelegramClient('session', api_id=API_ID, api_hash=API_HASH).start()


def main() -> None:
    prev_update_time = datetime.now() - timedelta(minutes=1)

    while True:
        if time_has_changed(prev_update_time):
            client.loop.run_until_complete(
                client(
                    UpdateProfileRequest(
                        about=f'UTC+3: {datetime.now().strftime("%H:%M")}'
                    )
                )
            )
        prev_update_time = datetime.now()
        time.sleep(1)


if __name__ == '__main__':
    main()
