# Copyright (C) 2018 - 2020 MrYacha.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# This file is part of Sophie.

from aiogram.dispatcher.handler import MessageHandler

from sophie.components.localization.strings import get_strings_dec
from .. import router


@router.message(commands=['lang'])
@get_strings_dec
class GetLanguageMenu(MessageHandler):
    async def handle(self):
        strings = self.data['strings']
        text = strings.get('current_lang', emoji=strings.emoji, language=strings.babel.english_name)
        await self.event.reply(text)
