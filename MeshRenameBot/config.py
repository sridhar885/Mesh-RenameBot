from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, ""]
        API_HASH = [str, "89ebdbc6e7bf9195bde696b0e9b3c387"]
        API_ID = [int, 8941261]
        BOT_TOKEN = [str, "1998570339:AAGnc97dhnar2w6tITYpLegXdku4qhoys38"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 50]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, False]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[2025727672]]
        OWNER_ID = [int, 2025727672]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,""]
        FORCEJOIN_ID = [int,-100123465978]

        TRACE_CHANNEL = [int, 0]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
