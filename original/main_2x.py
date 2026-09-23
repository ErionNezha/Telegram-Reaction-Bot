from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType
from aiogram.utils import executor
from random import choice


bot = Bot(token='<KEY>', parse_mode='HTML')
dp = Dispatcher(bot)


@dp.channel_post_handler(content_types=ContentType.ANY)
async def echo(message: types.Message):
    reactions = ["👍", "👎", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🐳", "❤‍🔥", "🌚", "🌭", "💯", "🤣", "⚡", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍", "🤗", "🫡", "🎅", "🎄", "☃", "💅", "🤪", "🗿", "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", "😎", "👾", "🤷‍♂", "🤷", "🤷‍♀", "😡"]
    reaction = f'("type": "emoji", "emoji": "{choice(reactions)}")'.replace('(', '{').replace(')', '}')
    await bot.request(
        method="setMessageReaction",
        data={
            "chat_id": message.chat.id,
            "message_id": message.message_id,
            "reaction": f'[{reaction}]'
        }
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
