import asyncio
from utils import notifications



async def send_farm_claim_notification(user_id: int):
    await asyncio.sleep(27000)
    await notifications.send_notification(user_id, 'You can claim your reward after 30 minutes')
