# Standard imports
from typing import Callable

# Third-party imports.
from pyrogram.types import Message

from .constants import messages


def command_count_validator(valid_parameter_length: int) -> Callable:
    def command_count_validator_decorator(func: Callable) -> Callable:
        async def wrapper(message: Message, *args, **kwargs) -> None:
            if len(message.command) != valid_parameter_length:
                await message.reply(messages.PARAMETERS_NOT_VALID)
                return
            await func()

        return wrapper

    return command_count_validator_decorator


def command_validator(command_index: int, validator: Callable, err_message: str) -> Callable:
    def command_validator_decorator(func: Callable) -> Callable:
        async def wrapper(message: Message, *args, **kwargs) -> None:
            if not validator(message.command[command_index]):
                await message.reply(err_message)
                return
            await func()

        return wrapper

    return command_validator_decorator
