import math
import traceback

from discord import Message
from discord.ext.commands import Bot, Context, CommandNotFound, CheckFailure, MissingRequiredArgument, \
    DisabledCommand, CommandOnCooldown, BadUnionArgument

from modules.custom.custom_cog import CustomCog
from utils.literal import get_cog, literals
from utils.log import Log


class LogCog(CustomCog, name=get_cog('LogCog')['name']):
    """
    발생한 오류를 기록하는 기능을 포함합니다.
    """

    def __init__(self, client: Bot):
        super().__init__(client)
        self.client: Bot = client

    @CustomCog.listener()
    async def on_ready(self):
        Log.auto(f'{self.client.user} on ready!')

    @CustomCog.listener()
    async def on_message(self, msg: Message):
        if msg.content:
            Log.auto(f'\n\t{msg.guild}/{msg.channel}/{msg.author}/{msg.id}\n\t{msg.content}',
                     message=msg)

    @CustomCog.listener()
    async def on_message_edit(self, msg_before: Message, msg_after: Message):
        if msg_before.content or msg_after.content:
            Log.auto(f'\n\t{msg_before.guild}/{msg_before.channel}/{msg_before.author}/{msg_before.id}\n\t'
                     f'before : {msg_before.content}\n\t'
                     f'after : {msg_after.content}',
                     message=msg_after)
        ctx = await self.client.get_context(msg_after)
        await self.client.invoke(ctx)

    @CustomCog.listener()
    async def on_message_delete(self, msg: Message):
        if msg.content:
            Log.auto(f'\n\t{msg.guild}/{msg.channel}/{msg.author}/{msg.id}\n\t'
                     f'content : {msg.content}',
                     message=msg)

    @CustomCog.listener()
    async def on_command_error(self, ctx: Context, error: Exception):
        if isinstance(error, CommandOnCooldown):
            Log.error(f'command now on cooldown, {error.retry_after}s left.')
            await ctx.send(literals('LogCog.on_command_error')['cooldown'] % math.ceil(error.retry_after))
            return
        elif ctx.command is not None:
            ctx.command.reset_cooldown(ctx)
        if isinstance(error, CommandNotFound):
            Log.error(f'not command : {error}')
            return
        if isinstance(error, CheckFailure):
            Log.error(f'check failed : {error}')
            return
        # if isinstance(error, BadArgument):
        #     Log.error(f'bad argument : {error}')
        #     return
        if isinstance(error, BadUnionArgument):
            Log.error(f'bad union argument: {error}')
            return
        if isinstance(error, MissingRequiredArgument):
            Log.error(f'missing required argument : {error}')
            return
        if isinstance(error, DisabledCommand):
            Log.error(f'disabled command : {error}')
            return
        Log.error(str(error) + '\n'
                  + ("".join(traceback.format_exception(etype=type(error), value=error, tb=error.__traceback__))))
        raise error


def setup(client: Bot):
    client.add_cog(LogCog(client))
