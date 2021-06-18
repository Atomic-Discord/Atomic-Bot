import os
from discord.ext.commands import Bot as BotBase
from discord import Intents
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler

OWNER_IDS = [828802130533810226]

load_dotenv()

class AtomicBot(BotBase):
	def __init__(self):
		self.ready = False
		self.scheduler = AsyncIOScheduler()

		super().__init__(
				command_prefix=".",
				case_sensitive=True,
				intents=Intents.all(),
			)

	def run(self):
		super().run(os.environ.get("TOKEN"), reconnect=True)


	async def on_connect(self):
		print("Bot connected")

	async def on_disconnect(self):
		print("Bot disconnected")

	async def on_ready(self):
		if not self.ready:
			self.scheduler.start()
			print("Bot is ready")

bot = AtomicBot()