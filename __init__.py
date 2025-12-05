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
        self.api.logger.debug("Test simple text translation.")
        test_text = self.api.tr('message.test_text', "This is a test string for translation.")
        self.api.logger.info(test_text)

        # Test different strings with same ID
        self.api.logger.debug("Test simple text translation for different string for an existing id.")
        another_test_text = self.api.tr('message.test_text', "A different test string for translation.")
        self.api.logger.info(another_test_text)

        # Test plural translations with no number formatting
        self.api.logger.debug("Test plurals with no number formatting.")
        plurals1 = ['message.test_plurals1', "There is {n} item.", "There are {n} items."]

        test_plurals_minus = self.api.trn(*plurals1, n=-1)
        self.api.logger.info(test_plurals_minus)

        test_plurals_zero = self.api.trn(*plurals1, n=0)
        self.api.logger.info(test_plurals_zero)

        test_plurals_one = self.api.trn(*plurals1, n=1)
        self.api.logger.info(test_plurals_one)

        test_plurals_two = self.api.trn(*plurals1, n=2)
        self.api.logger.info(test_plurals_two)

        test_plurals_large = self.api.trn(*plurals1, n=100000)
        self.api.logger.info(test_plurals_large)

        self.api.logger.debug("Test plurals with float and no number formatting.")
        test_plurals_float = self.api.trn(*plurals1, n=10000.123)
        self.api.logger.info(test_plurals_float)

        # Test plural translations with number formatting
        self.api.logger.debug("Test plurals with number formatting.")
        plurals2 = ['message.test_plurals2', "There is {n:,} item.", "There are {n:,} items."]

        test_plurals_minus = self.api.trn(*plurals2, n=-1)
        self.api.logger.info(test_plurals_minus)

        test_plurals_zero = self.api.trn(*plurals2, n=0)
        self.api.logger.info(test_plurals_zero)

        test_plurals_one = self.api.trn(*plurals2, n=1)
        self.api.logger.info(test_plurals_one)

        test_plurals_two = self.api.trn(*plurals2, n=2)
        self.api.logger.info(test_plurals_two)

        test_plurals_large = self.api.trn(*plurals2, n=100000)
        self.api.logger.info(test_plurals_large)

        self.api.logger.debug("Test plurals with float and number formatting.")
        test_plurals_float = self.api.trn(*plurals2, n=10000.123)
        self.api.logger.info(test_plurals_float)


def enable(api: PluginApi):
    """Called when plugin is enabled."""
    api.register_file_action(TestTranslations)
    api.register_track_action(TestTranslations)
    api.register_album_action(TestTranslations)
