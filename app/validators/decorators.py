# Standard imports
from typing import Callable

# Third-party imports.
from pyrogram.types import Message
from pyrogram.client import Client

# Local imports with absolute path.
from ..constants import messages


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


def retrieve_instance_and_instance_validator(model_class: object, key: str, value_index: int) -> Callable:
    def retrieve_instance_and_instance_validator_decorator(func: Callable) -> Callable:
        async def wrapper(client: Client, message: Message, *args, **kwargs) -> None:
            model_instance: model_class = model_class.filter_first(**{key: message.command[value_index]})
            if not model_instance:
                await message.reply(messages.NO_OBJECT_FOUND)
                return
            await func(client, message, model_instance=model_instance, *args, **kwargs)

        return wrapper

    return retrieve_instance_and_instance_validator_decorator
