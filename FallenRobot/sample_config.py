import json
import os


def get_user_list(config, key):
    with open("{}/FallenRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]



class Config(object):
    LOGGER = True

    API_ID = 10872193
    API_HASH = "7a2c777e52479d13fb1adb29944130cf"
    TOKEN = "6158580139:AAFY-AwcxtmupB8srXBEbHQenKCS9lK3wnI"
    OWNER_ID = 5205602399
    OWNER_USERNAME = "MolesteRishu"
    SUPPORT_CHAT = "Kaizuryu_Bot_Support"
    JOIN_LOGGER = -1001607942799
    EVENT_LOGS = -1001607942799

    SQLALCHEMY_DATABASE_URI = "postgresql://wlywacfh:UGnK09rXIwWrgh5l9O0Okk-dieKiXpjP@raja.db.elephantsql.com/wlywacfh"
    DATABASE_URL = "postgresql://wlywacfh:UGnK09rXIwWrgh5l9O0Okk-dieKiXpjP@raja.db.elephantsql.com/wlywacfh"
    MONGO_DB_URI = "mongodb+srv://xelcius:raizel~97@cluster0.gj9j8.mongodb.net/cluster0?retryWrites=true&w=majority"
    LOAD = []
    NO_LOAD = ["rss"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    
    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    DONATION_LINK = ""
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = "CAACAgUAAxkBAAEDafNhq5Z0DegqVzauwSighMw5cPWp8QACVgQAAuUG0FRXfCEuBziNzCIE"
    ALLOW_EXCL = True 
    CASH_API_KEY = "GPK42QMONC7TGVVL"
    TIME_API_KEY = "GPOIC5IBWGWC"
    BL_CHATS = []
    SPAMMERS = None
    ALLOW_CHATS = True
    START_IMG = ""
    HEROKU_API_KEY = None
    HEROKU_APP_NAME = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    ARQ_API_KEY = "LJMETG-DPHBCX-DGHJCD-TMFIGB-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    ALLOW_EXCL = None
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
