import aiogram
from misc import dispatcher
from handlers import *

if __name__ == '__main__':
    aiogram.utils.executor.start_polling(dispatcher, skip_updates=True)
