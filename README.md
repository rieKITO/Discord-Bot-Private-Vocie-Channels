# Discord Bot Private Voice Channels
Интернет-бот для платформы Discord, предоставляющий инструментарий для создания и управления личными закрытыми голосовыми каналами сообщества.

## Инструменты
- Python
- [Disnake](https://docs.disnake.dev/en/stable/)

## Функциональность
1. Префикс=команда «**!temporary_voice_embed**»

   Данная команда доступна администрации проекта.
   После ввода команды создается интерактивное меню с набором кнопок.
   Кнопки работаю только в том случе, если пользователь находится в своем личном закрытом голосовом канале.

   Перечень действий, предоставляемых префикс-командой «**!temporary_voice_embed**»:

   - **изменить название комнаты** — действие, позволяющее владельцу голосового канала изменить название комнаты.
   - **открыть/закрыть комнату** — действие, позволяющее владельцу голосового канала изменить статус доступности комнаты для других участников проекта на противоположный от текущего.
   - **сделать комнату видимой/невидимой** — действие, позволяющее владельцу голосового канала изменить статус видимости комнаты для других участников проекта на противоположный от текущего.
   - **изменить лимит пользователей в комнате** — действие, позволяющее владельцу голосового канала изменить максимальное количество участников, способных одновременно пребывать в голосовом канале владельца.
   - **выдать/забрать доступ в комнату у пользователя** — действие, позволяющее владельцу голосового канала изменить статус доступности комнаты у конкретного участника проекта на противоположный от текущего.
   - **запретить/разрешить говорить пользователю в комнате** — действие, позволяющее владельцу голосового канала изменить статус возможности пользования голосовыми средствами конкретного участника проекта на противоположный от текущего.
   - **выгнать пользователя из комнаты** — действие, позволяющее владельцу голосового канала исключить конкретного пользователя проекта из голосового канала владельца.
   - **передать владение комнатой** - действие, позволяющее владельцу голосового канала передать владение своим голосовым каналом другому конкретному пользователю.