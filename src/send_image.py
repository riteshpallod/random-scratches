import os
from telegram import Bot

def get_env_var(ENV):
    return os.environ[ENV]

channel_id = "-1001550665714"

bot = Bot(token=get_env_var("TELEGRAM_ACCESS_TOKEN"))
bot.send_photo(chat_id = "-1001550665714", photo = "https://www.thefamouspeople.com/profiles/images/monica-bellucci-7.jpg")
bot.send_photo(chat_id = channel_id, photo = "https://instagram.fpnq7-2.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s640x640/222889988_1522232958120173_1918465021306860604_n.jpg?_nc_ht=instagram.fpnq7-2.fna.fbcdn.net&_nc_cat=105&_nc_ohc=4SLZXFUjhDsAX9aQUYh&tn=1R5DYn8Vk6cNYrqk&edm=AP_V10EBAAAA&ccb=7-4&oh=7961bdfa6e90af14a1fc09425e8b8192&oe=610E1C8D&_nc_sid=4f375e",
    caption = "man in background trying to act cool")
bot.send_photo(chat_id = channel_id, photo = "https://x.glance-cdn.net/public/dynamic/1440x2560/c7b78cc0d639b62bf421372d6c6da21da613ac9e.jpg",
            caption = "Hi Neha, this is a bot, trust me I am really a bot. Anyway sending a glance asset from Python")
