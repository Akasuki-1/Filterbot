import importlib
import re
from typing import Optional, List
from sys import argv

from telegram import Message, Chat, Update, Bot, User
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.error import Unauthorized, BadRequest, TimedOut, NetworkError, ChatMigrated, TelegramError
from telegram.ext import CommandHandler, Filters, MessageHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async, DispatcherHandlerStop
from telegram.utils.helpers import escape_markdown

from tg_bot import dispatcher, updater, TOKEN, WEBHOOK, OWNER_ID, DONATION_LINK, CERT_PATH, PORT, URL, LOGGER, \
    ALLOW_EXCL, START_PHOTTO, OWNER_NAME, OWNER_USERNAME 
# needed to dynamically load modules
# NOTE: Module order is not guaranteed, specify that in the config file!
from tg_bot.modules import ALL_MODULES
from tg_bot.modules.helper_funcs.chat_status import is_user_admin
from tg_bot.modules.helper_funcs.misc import paginate_modules


from telegram import Bot, Update, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton


QWERTUR = "https://telegra.ph/file/ff1e6ce577cbc289fc321.jpg"

__mod_name__ = "PICTURE"


__help__ = """
  
reply_photo(QWERTUR, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
  - /afk <reason>: Mark yourself as AFK.
  - brb <reason>: Same as the afk command, but not a command.\n
  When marked as AFK, any mentions will be replied to with a message stating that you're not available!
"""
