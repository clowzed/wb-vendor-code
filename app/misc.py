import aiogram
import config
from aiogram.contrib.middlewares.logging import LoggingMiddleware

bot = aiogram.Bot(config.BOT_TOKEN)
dispatcher = aiogram.Dispatcher(bot)

dispatcher.middleware.setup(LoggingMiddleware())
