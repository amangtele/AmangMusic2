#
# Copyright (C) 2021-2022 by amangtele@Github, < https://github.com/amangtele >.
#
# This file is part of < https://github.com/amangtele/AmangMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/amangtele/AmangMusic/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from AmangMusic import app
from AmangMusic.core.call import AmangMusic
from AmangMusic.utils.database import is_muted, mute_off
from AmangMusic.utils.decorators import AdminRightsCheck

# Commands
UNMUTE_COMMAND = get_command("UNMUTE_COMMAND")


@app.on_message(
    filters.command(UNMUTE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def unmute_admin(Client, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    if not await is_muted(chat_id):
        return await message.reply_text(_["admin_7"])
    await mute_off(chat_id)
    await AmangMusic.unmute_stream(chat_id)
    await message.reply_text(
        _["admin_8"].format(message.from_user.mention)
    )
