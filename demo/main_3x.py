import asyncio
import logging
import sys
from random import choice

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message, ReactionTypeEmoji

# Bot token can be obtained via https://github.com/ErionNezha
TOKEN = '<KEY>'

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.channel_post(F.content_type.in_({'photo', 'video', 'audio', 'voice', 'document', 'video_note', 'text'}))
async def on_message(message: Message):
    reactions = ["👍", "👎", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡",
                 "🥱", "🥴", "😍", "🐳", "❤‍🔥", "🌚", "🌭", "💯", "🤣", "⚡", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕", "😈",
                 "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍", "🤗", "🫡", "🎅", "🎄", "☃", "💅", "🤪", "🗿",
                 "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", "😎", "👾", "🤷‍♂", "🤷", "🤷‍♀", "😡"]

    await message.bot.set_message_reaction(chat_id=message.chat.id,
                                           message_id=message.message_id,
                                           reaction=[ReactionTypeEmoji(type='emoji', emoji=choice(reactions))])


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
