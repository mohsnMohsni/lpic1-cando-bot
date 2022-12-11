# Standard imports
from typing import Callable

# Third-party imports.
from pyrogram.types import Message

from .constants import messages


def command_length_validator(valid_parameter_length: int) -> Callable:
    print('from level 1')
    def command_length_validator_decorator(func: Callable) -> Callable:
        print('from level 2')
        async def wrapper(message: Message, *args, **kwargs) -> None:
            print('from level 3')
            if len(message.command) != valid_parameter_length:
                await message.reply(messages.PARAMETERS_NOT_VALID)
                return
            await func()
        return wrapper

    return command_length_validator_decorator


def command_validator(command_index: int, validator: Callable, err_message: str) -> Callable:
    def command_validator_decorator(func: Callable) -> Callable:
        async def wrapper(message: Message, *args, **kwargs) -> None:
            if not validator(message.command[command_index]):
                await message.reply(err_message)
                return
            await func()

        return wrapper

    return command_validator_decorator
