# -*- coding: utf-8 -*-
"""Test plugin for Picard Plugin API translations management.
"""
# Copyright (C) 2025 Bob Swift (rdswift)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.

# pylint: disable=line-too-long
# pylint: disable=import-error
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals


from picard.plugin3.api import (
    BaseAction,
    PluginApi,
)


class TestTranslations(BaseAction):
    NAME = 'Test API Translations'

    def __init__(self, api: PluginApi = None):
        super().__init__(api=api)
        self.api = api

    def callback(self, objs):
        self.api.logger.debug("Testing Test API Settings Plugin translation management.")

        # Test simple text translation
        test_text = self.api.tr('message.test_text', "This is a test string for translation.")
        self.api.logger.info(test_text)

        # Test plural translations
        plurals = ['message.test_plurals', "There is {n} item.", "There are {n} items."]
        test_plurals_minus = self.api.trn(*plurals, n=-1)
        test_plurals_zero = self.api.trn(*plurals, n=0)
        test_plurals_one = self.api.trn(*plurals, n=1)
        test_plurals_two = self.api.trn(*plurals, n=2)
        test_plurals_large = self.api.trn(*plurals, n=100000)

        self.api.logger.info(test_plurals_minus)
        self.api.logger.info(test_plurals_zero)
        self.api.logger.info(test_plurals_one)
        self.api.logger.info(test_plurals_two)
        self.api.logger.info(test_plurals_large)

        # Test different strings with same ID
        another_test_text = self.api.tr('message.test_text', "A different test string for translation.")
        self.api.logger.info(another_test_text)


def enable(api: PluginApi):
    """Called when plugin is enabled."""
    api.register_file_action(TestTranslations)
    api.register_track_action(TestTranslations)
    api.register_album_action(TestTranslations)
