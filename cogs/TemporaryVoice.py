import disnake
from disnake.ext import commands
import asyncio
from disnake.utils import get

import config

class TemporaryVoiceView(disnake.ui.View):

    def __init__(self, bot):
        self.bot = bot
        self.guild = self.bot.get_guild(config.GUILD_ID)
        super().__init__(timeout = None)

    def check_message(self, message, interaction):
        return message.channel == interaction.channel and message.author.id == interaction.user.id

    async def str_enter(self, interaction: disnake.CommandInteraction, argument: str):

        if argument == "name":
            await interaction.send("Введите новое название:", ephemeral = True)

        elif argument == "limit":
            await interaction.send("Введите лимит пользователей:", ephemeral = True)

        elif argument == "user":
            await interaction.send("Введите ID пользователя:", ephemeral = True)

        try:
            return await self.bot.wait_for('message', check = lambda message: self.check_message(message, interaction), timeout = 30.0)
        except asyncio.TimeoutError:
            return None

    @disnake.ui.button(label = "", style = disnake.ButtonStyle.gray, emoji = "<:pencil:1144951148789379092>", row = 1)
    async def room_name_change(self, button: disnake.ui.Button, interaction: disnake.CommandInteraction):
        permissions = interaction.user.voice.channel.permissions_for(interaction.user)
        
        if interaction.user.voice.channel.category.id == config.PRIVATE_CATEGORY_ID and permissions.moderate_members:
            NewName = await self.str_enter(interaction, "name")

            if NewName:
                await interaction.user.voice.channel.edit(name = f"{NewName.content}")
                await interaction.send("Вы успешно изменили название комнаты!", ephemeral = True)
                await NewName.delete()

        else:
            await interaction.send("У Вас недостаточно прав!", ephemeral = True)


    @disnake.ui.button(label = "", style = disnake.ButtonStyle.gray, emoji = "<:lock:1147879811742699523>", row = 1)
    async def private_change(self, button: disnake.ui.Button, interaction: disnake.CommandInteraction):
        permissions = interaction.user.voice.channel.permissions_for(interaction.user)

        if interaction.user.voice.channel.category.id == config.PRIVATE_CATEGORY_ID and permissions.moderate_members:
            DefaulRolePermissions = interaction.user.voice.channel.permissions_for(self.guild.default_role)

            if DefaulRolePermissions.connect:
                await interaction.user.voice.channel.set_permissions(self.guild.default_role, connect = False)
                await interaction.send("Вы успешно закрыли комнату!", ephemeral = True)

            else:
                await interaction.user.voice.channel.set_permissions(self.guild.default_role, connect = True)
                await interaction.send("Вы успешно открыли комнату!", ephemeral = True)

        else:
            await interaction.send("У Вас недостаточно прав!", ephemeral = True)


    @disnake.ui.button(label = "", style = disnake.ButtonStyle.gray, emoji = "<:eye:1147883731391103078>", row = 1)
    async def view_change(self, button: disnake.ui.Button, interaction: disnake.CommandInteraction):
        permissions = interaction.user.voice.channel.permissions_for(interaction.user)

        if interaction.user.voice.channel.category.id == config.PRIVATE_CATEGORY_ID and permissions.moderate_members:
            DefaulRolePermissions = interaction.user.voice.channel.permissions_for(self.guild.default_role)

            if DefaulRolePermissions.view_channel:
                await interaction.user.voice.channel.set_permissions(self.guild.default_role, view_channel = False)
                await interaction.send("Вы успешно скрыли комнату!", ephemeral = True)

            else:
                await interaction.user.voice.channel.set_permissions(self.guild.default_role, view_channel = True)
                await interaction.send("Вы успешно раскрыли комнату!", ephemeral = True)

        else:
            await interaction.send("У Вас недостаточно прав!", ephemeral = True)


    @disnake.ui.button(label = "", style = disnake.ButtonStyle.gray, emoji = "<:limit:1147898429851308172>", row = 1)
    async def limit_change(self, button: disnake.ui.Button, interaction: disnake.CommandInteraction):
        permissions = interaction.user.voice.channel.permissions_for(interaction.user)
        
        if interaction.user.voice.channel.category.id == config.PRIVATE_CATEGORY_ID and permissions.moderate_members:
            limit = await self.str_enter(interaction, "limit")

            if limit and int(limit.content) < 100 and int(limit.content) > 0:
                await interaction.user.voice.channel.edit(user_limit = int(limit.content))
                await interaction.send("Вы успешно изменили лимит пользователей в комнате!", ephemeral = True)

            else:
                await interaction.send("Лимит не может быть больше 99 и меньше 1!", ephemeral = True)

            await limit.delete()

        else:
            await interaction.send("У Вас недостаточно прав!", ephemeral = True)

    
    @disnake.ui.button(label = "", style = disnake.ButtonStyle.gray, emoji = "<:human:1147901811865440257>", row = 2)
    async def user_connect_change(self, button: disnake.ui.Button, interaction: disnake.CommandInteraction):
        permissions = interaction.user.voice.channel.permissions_for(interaction.user)

        if interaction.user.voice.channel.category.id == config.PRIVATE_CATEGORY_ID and permissions.moderate_members:
            _user = await self.str_enter(interaction, "user")

            if _user:
                user = self.guild.get_member(int(_user.content))
                UserPermissions = interaction.user.voice.channel.permissions_for(user)

                if UserPermissions.connect:
                    await interaction.user.voice.channel.set_permissions(user, connect = False)
                    await interaction.send("Вы успешно запретили этому пользователю доступ к комнате!", ephemeral = True)

                else:
                    await interaction.user.voice.channel.set_permissions(user, connect = True, view_channel = True)
                    await interaction.send("Вы успешно разрешили этому пользователю доступ к комнате!", ephemeral = True)

                await _user.delete()

        else:
            await interaction.send("У Вас недостаточно прав!", ephemeral = True)


    @disnake.ui.button(label = "", style = disnake.ButtonStyle.gray, emoji = "<:mic:1147912291094904883>", row = 2)
    async def user_mic_change(self, button: disnake.ui.Button, interaction: disnake.CommandInteraction):
        permissions = interaction.user.voice.channel.permissions_for(interaction.user)

        if interaction.user.voice.channel.category.id == config.PRIVATE_CATEGORY_ID and permissions.moderate_members:
            _user = await self.str_enter(interaction, "user")

            if _user:
                user = self.guild.get_member(int(_user.content))
                UserPermissions = interaction.user.voice.channel.permissions_for(user)

                if UserPermissions.speak:
                    await interaction.user.voice.channel.set_permissions(user, speak = False)
                    await interaction.send("Вы успешно запретили этому пользователю говорить в комнате!", ephemeral = True)

                else:
                    await interaction.user.voice.channel.set_permissions(user, speak = True)
                    await interaction.send("Вы успешно разрешили этому пользователю говорить в комнате!", ephemeral = True)

                await _user.delete()

        else:
            await interaction.send("У Вас недостаточно прав!", ephemeral = True)


    @disnake.ui.button(label = "", style = disnake.ButtonStyle.gray, emoji = "<:krest:1147925346960810025>", row = 2)
    async def kick_user(self, button: disnake.ui.Button, interaction: disnake.CommandInteraction):
        permissions = interaction.user.voice.channel.permissions_for(interaction.user)

        if interaction.user.voice.channel.category.id == config.PRIVATE_CATEGORY_ID and permissions.moderate_members:
            _user = await self.str_enter(interaction, "user")

            if _user:
                user = self.guild.get_member(int(_user.content))

                if user.voice.channel.id == interaction.user.voice.channel.id:
                    await user.move_to(None)
                    await interaction.send("Вы успешно исключили пользователя из комнаты!", ephemeral = True)

                else:
                    await interaction.send("Этого пользователя нет в этой комнате!", ephemeral = True)

                await _user.delete()

        else:
            await interaction.send("У Вас недостаточно прав!", ephemeral = True)


    @disnake.ui.button(label = "", style = disnake.ButtonStyle.gray, emoji = "<:crown:1147927922280235150>", row = 2)
    async def owner_change(self, button: disnake.ui.Button, interaction: disnake.CommandInteraction):
        permissions = interaction.user.voice.channel.permissions_for(interaction.user)

        if interaction.user.voice.channel.category.id == config.PRIVATE_CATEGORY_ID and permissions.moderate_members:
            _user = await self.str_enter(interaction, "user")

            if _user:
                user = self.guild.get_member(int(_user.content))

                await interaction.user.voice.channel.set_permissions(interaction.user, moderate_members = False)
                await interaction.user.voice.channel.set_permissions(user, moderate_members = True)
                await interaction.send("Вы успешно передали владение комнатой!", ephemeral = True)

                await _user.delete()

        else:
            await interaction.send("У Вас недостаточно прав!", ephemeral = True)



class TemporaryVoice(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.guild = self.bot.get_guild(config.GUILD_ID)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: disnake.Member, before: disnake.VoiceState, after: disnake.VoiceState):
        PossibleChannelName = f"Комната {member.name}"
        if after.channel:
            if after.channel.id == config.MAIN_PRIVATE_CHANNEL_ID:
                overwrites = {
                    self.guild.default_role: disnake.PermissionOverwrite(connect = True, view_channel = True, kick_members = False, mute_members = False, mention_everyone = False),
                    self.guild.me: disnake.PermissionOverwrite(connect = True, view_channel = True),
                    member: disnake.PermissionOverwrite(connect = True, view_channel = True, moderate_members = True)
                }
                TempChannel = await after.channel.clone(name = PossibleChannelName, overwrites = overwrites)
                await member.move_to(TempChannel)

        if before.channel:
            if before.channel.category.id == config.PRIVATE_CATEGORY_ID and before.channel.id != config.MAIN_PRIVATE_CHANNEL_ID:
                if len(before.channel.members) == 0:
                    await before.channel.delete()

    @commands.command()
    @commands.has_any_role(*config.HIGHER_STAFF_ROLES)
    async def temporary_voice_embed(self, ctx):
        embed = disnake.Embed(
            title = "УПРАВЛЕНИЕ ПРИВАТНОЙ КОМНАТОЙ",
            color = 0x292b2e,
            description = f"<a:arrow:1140371321683984424> <:pencil:1144951148789379092> - **изменить название комнаты**\n" +
                          f"<a:arrow:1140371321683984424> <:lock:1147879811742699523> - **открыть/закрыть комнату**\n" +
                          f"<a:arrow:1140371321683984424> <:eye:1147883731391103078> - **сделать комнату видимой/невидимой**\n" +
                          f"<a:arrow:1140371321683984424> <:limit:1147898429851308172> - **изменить лимит пользователей в комнате**\n" +
                          f"<a:arrow:1140371321683984424> <:human:1147901811865440257> - **выдать/забрать доступ в комнату у пользователя**\n" +
                          f"<a:arrow:1140371321683984424> <:mic:1147912291094904883> - **запретить/разрешить говорить пользователю в комнате\n**" +
                          f"<a:arrow:1140371321683984424> <:krest:1147925346960810025> - **выгнать пользователя из комнаты**\n" +
                          f"<a:arrow:1140371321683984424> <:crown:1147927922280235150> - **передать владение комнатой**"
        )
        view = TemporaryVoiceView(self.bot)
        await ctx.send(embed = embed, view = view)


def setup(bot):
    bot.add_cog(TemporaryVoice(bot))