from aiogram import Dispatcher
from aiogram.dispatcher.filters import BaseFilter
from aiogram.types import Message

import loggers


class MessageForwardedFilter(BaseFilter):
    is_forwarded: bool

    async def __call__(self, message: Message):
        if self.is_forwarded and (message.forward_from
                                  or message.forward_from_chat
                                  or message.forward_from_message_id):
            loggers.filters.debug("Message is forwarded!")
            return True
        if not self.is_forwarded and not (message.forward_from
                                          or message.forward_from_chat
                                          or message.forward_from_message_id):
            loggers.filters.debug("Message is not forwarded!")
            return True


def setup(dispatcher: Dispatcher, *args, **kwargs):
    dispatcher.message.bind_filter(MessageForwardedFilter)
