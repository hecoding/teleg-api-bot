#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#                                                                              #
#   telegbot.py                                                                #
#                                                                              #
#   Main teleg-api-bot class, it represents a bot.                             #
#                                                                              #
#                                                                              #
#                                                                              #
#   Copyright (C) 2015 LibreLabUCM All Rights Reserved.                        #
#                                                                              #
#   This file is part of teleg-api-bot.                                        #
#                                                                              #
#   This program is free software: you can redistribute it and/or modify       #
#   it under the terms of the GNU General Public License as published by       #
#   the Free Software Foundation, either version 3 of the License, or          #
#   (at your option) any later version.                                        #
#                                                                              #
#   This program is distributed in the hope that it will be useful,            #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of             #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              #
#   GNU General Public License for more details.                               #
#                                                                              #
#   You should have received a copy of the GNU General Public License          #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.      #
#                                                                              #
################################################################################

# The name of your plugin, inherited from this class, and the filename in which is contained must coincide
#   but you can lowercase the first letter of the file.


class Plugin:
    def __init__(self, telegBot):
        self.telegBot = telegBot
