import importlib
import re
from typing import Optional, List
from sys import argv

from telegram import Bot, Update, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton


QWERTUR = "https://telegra.ph/file/ff1e6ce577cbc289fc321.jpg"

__mod_name__ = "PICTURE"


__help__ = """
   update.effective_message.reply_photo(
            QWERTUR, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
        )
  - /afk <reason>: Mark yourself as AFK.
  - brb <reason>: Same as the afk command, but not a command.\n
  When marked as AFK, any mentions will be replied to with a message stating that you're not available!
"""
