import asyncio
import datetime
import logging
import logging.config
import sys
from pyrogram import *
from pyrogram.errors.exceptions.not_acceptable_406 import *
from config import *
from database import *
from database.users import *
from helpers import *
from pyshorteners import *
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
import os
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K


if __name__ == "__main__" :

class Bot(Client):
    def __init__(self):
        super().__init__(
            "shortener",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="plugins"),
        )

    async def start(self):

        temp.START_TIME = datetime.datetime.now()
        await super().start()

        if UPDATE_CHANNEL:
            try:
                self.invite_link = await self.create_chat_invite_link(UPDATE_CHANNEL)
            except Exception:
                logging.error(
                    f"Make sure to make the bot in your update channel - {UPDATE_CHANNEL}"
                )
                sys.exit(1)

        me = await self.get_me()
        self.owner = await self.get_users(int(OWNER_ID))
        self.username = f"@{me.username}"
        temp.BOT_USERNAME = me.username
        temp.FIRST_NAME = me.first_name
        if not await db.get_bot_stats():
            await db.create_stats()

        banned_users = await filter_users({"banned": True})
        async for user in banned_users:
            temp.BANNED_USERS.append(user["user_id"])

        await set_commands(self)

        await broadcast_admins(self, "** Bot started successfully **")
        logging.info("Bot started")

        if WEB_SERVER:
            await create_server()
            logging.info("Web server started")
            logging.info("Pinging server")

    async def stop(self):
        await broadcast_admins(self, "** Bot Stopped Bye **")
        await super().stop()
        logging.info("Bot Stopped Bye")
