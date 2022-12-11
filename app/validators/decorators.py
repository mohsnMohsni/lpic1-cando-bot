# Standard imports
from typing import Callable

# Third-party imports.
from pyrogram.types import Message
from pyrogram.client import Client

# Local imports with absolute path.
from .constants import messages


def test_health(_message: str = 'test'):
    def test_health_decorator(func: Callable) -> Callable:
        async def wrapper(client: Client, message: Message, *args, **kwargs) -> None:
            await message.reply(_message)
            await func(client, message, *args, **kwargs)

        return wrapper

    return test_health_decorator


def command_length_validator(valid_parameter_length: int) -> Callable:
    def command_length_validator_decorator(func: Callable) -> Callable:
        async def wrapper(client: Client, message: Message, *args, **kwargs) -> None:
            if len(message.command) != valid_parameter_length:
                await message.reply(messages.PARAMETERS_NOT_VALID)
                return
            await func(client, message, *args, **kwargs)

        return wrapper

    return command_length_validator_decorator


def command_validator(command_index: int, validator: Callable, err_message: str) -> Callable:
    def command_validator_decorator(func: Callable) -> Callable:
        async def wrapper(client: Client, message: Message, *args, **kwargs) -> None:
            if not validator(message.command[command_index]):
                await message.reply(err_message)
                return
            await func(client, message, *args, **kwargs)

        return wrapper

    return command_validator_decorator
