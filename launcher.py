from lib.bot import bot
from lib.website import app

VERSION = "0.0.1"

bot.run()
app.run(debug=True)