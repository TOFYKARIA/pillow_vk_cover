import asyncio

from cover import CoverImage
from vkbottle.api import API


async def main():
    api = API(token="vk1.a.u2PvQHLcl5Nn8a2udgwNu2Zn9_lYV1Vz6mGf2W5meo1brByL55fLhjLngmuD-4pNMwNfsYpFyakP20Se6qjyf8ODsqXCXlggDThMlEwr-MPuZgmBIdCBL3cx5e08tD0IQBuAfzRwIM2gzAmCD-WRcMYaTSeNdHbuuFODZLxksMh3gO0A6iTUMFB2uADp8k-iOWno-dFIVqjKGQEt7b7tow")
    user_info = await api.account.get_profile_info()

    cover = CoverImage(api=api, user_id=user_info.id)
    cover.draw()
    await cover.upload()


if __name__ == '__main__':
    asyncio.run(main())
