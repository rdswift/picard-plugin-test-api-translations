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
    t_,
)


class TestTranslations(BaseAction):
    NAME = "Test API translations"
    PLURALS = {
        'unformatted': t_('message.test_plurals1', "There is {n} item.", "There are {n} items."),
        'formatted': t_('message.test_plurals2', "There is {n:,} item.", "There are {n:,} items."),
    }

    def __init__(self, api: PluginApi = None):
        super().__init__(api=api)
        self.api = api
        self.setText(api.tr("action.name", self.NAME))

    def callback(self, objs):
        self.api.logger.debug("# Testing Test API Settings Plugin translation management.")

        # Test simple text translation
        self.api.logger.debug("# Test simple text translation.")
        test_text = self.api.tr('message.test_text', "This is a test string for translation.")
        self.api.logger.info(test_text)

        # Test different strings with same ID
        self.api.logger.debug("# Test simple text translation for different string for an existing id.")
        test_text = self.api.tr('message.test_text', "A different test string for translation.")
        self.api.logger.info(test_text)

        # Test plural translations with no number formatting
        self.api.logger.debug("# Test plurals with integer and no number formatting.")
        plurals = self.PLURALS['unformatted']
        for number in [-1, 0, 1, 2, 10000]:
            test_text = self.api.trn(*plurals, n=number)
            self.api.logger.info(test_text)

        self.api.logger.debug("# Test plurals with float and no number formatting.")
        for number in [-1.1, 0.0, 1.0, 1.1, 2.1, 10000.123]:
            test_text = self.api.trn(*plurals, n=number)
            self.api.logger.info(test_text)

        # Test plural translations with number formatting
        self.api.logger.debug("# Test plurals with integer and number formatting.")
        plurals = self.PLURALS['formatted']
        for number in [-1, 0, 1, 2, 10000]:
            test_text = self.api.trn(*plurals, n=number)
            self.api.logger.info(test_text)

        self.api.logger.debug("# Test plurals with float and number formatting.")
        for number in [-1.1, 0.0, 1.0, 1.1, 2.1, 10000.123]:
            test_text = self.api.trn(*plurals, n=number)
            self.api.logger.info(test_text)


def enable(api: PluginApi):
    """Called when plugin is enabled."""
    api.register_file_action(TestTranslations)
    api.register_track_action(TestTranslations)
    api.register_album_action(TestTranslations)
