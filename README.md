# teleg-api-bot

Telegram Api for new bot system

## Getting started

This project uses Python 3, so you should probably install that, if you haven't already.

For an introduction to the Telegram Bot API, take a look at our [Getting Started](https://github.com/LibreLabUCM/teleg-api-bot/wiki/Getting-started-with-the-Telegram-Bot-API) wiki page.

## Installation

You can get it from pip:

```
$ pip install teleg-api-bot
```

Or you can go ahead and clone this repo, and install it:

```
$ python setup.py install
```

## Usage

Dependencies: Python 3.4, py-yaml, requests (see [requirements-dev](./requirements-dev.txt))

Example bot:

```python
#!/usr/bin/env python3

from telegapi.telegbot import TelegBot
from telegapi.logger import Logger

logger = Logger()
import time, json

def receive_message(msg):
    logger.msg(msg)
    if msg["text"] == "/help":
        bot.send_message(msg["chat"]["id"], "Text")


bot = TelegBot('TOKEN')
bot.on_receive_message = receive_message
bot.connect()
bot.run()
```

### Plugins
There's also support for plugins. If you want to extend the functionality writting plugins, make a folder for them and pass it to the `load_plugins` method.

The file in which is contented must have the same name as the class (first letter can be lowercased). And note it must inherit from `Plugin`.   
An `exampleplugin.py` file:
```python
from telegapi.plugin import Plugin


class Exampleplugin(Plugin):
    def example(self):
        print('Hi! I\'m an example plugin method')

    def looper(self, times, msg):
        if msg['from']['username'] == self.telegBot.data['username']:
            return

        for i in range(times):
            self.telegBot.send_message(msg["chat"]["id"], "Hi")
```

After this, drop it to your plugin folder and let's do an example bot using plugins:
```python
from telegapi.telegbot import TelegBot
from telegapi.logger import Logger

logger = Logger()
import time, json

def receive_message(msg):
    if msg["date"] < time.time() - 2:
        return  # old
    logger.msg(msg)
    bot.exampleplugin.looper(5, msg)


bot = TelegBot('TOKEN')
bot.load_plugins('PLUGINDIRECTORYPATH')
bot.on_receive_message = receive_message
bot.exampleplugin.example()
bot.connect()
bot.run()
```

It shows:
```
Hi! I'm an example plugin method
...
```

`PLUGINDIRECTORYPATH` can also be relative.