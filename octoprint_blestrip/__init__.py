# coding=utf-8
from __future__ import absolute_import
from .bleStrip import bleStrip

import octoprint.plugin
import octoprint.events
import logging
#import time
import threading

class bleStripPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.EventHandlerPlugin,
                       octoprint.plugin.ProgressPlugin):

    def __init__(self):
        self._lock = threading.Lock()
        self._bleStrip = bleStrip()

    def on_after_startup(self):
        #self._bleStrip = bleStrip()
        self._logger.info("bleStrip plugin (more: %s)" % self._settings.get(["MAC"]))

    def get_settings_defaults(self):
        return dict(MAC="BE:FF:80:00:B6:AB",
                    SUR="FF",
                    SUG="FF",
                    SUB="FF",
                    CONR="00",
                    CONG="FF",
                    CONB="00",
                    COR="FF",
                    COG="FF",
                    COB="FF",
                    PDR="00",
                    PDG="FF",
                    PDB="00",
                    SDR="FF",
                    SDG="FF",
                    SDB="FF")

    def get_template_vars(self):
        return dict(MAC=self._settings.get(["MAC"]))

    def get_template_configs(self):
        return [ dict(type="navbar", custom_bindings=False),
                 dict(type="settings", custom_bindings=False)
        ]

    def on_event(self, event, payload):
	self._logger.info("bleStrip plugin - Event: ", event)
        with self._lock:
            if event == octoprint.events.Events.STARTUP:
                self._bleStrip.ledcolor(self._settings.get(["SUR"]),self._settings.get(["SUG"]),self._settings.get(["SUB"]))
            elif event == octoprint.events.Events.CONNECTED:
		self._bleStrip.ledcolor(self._settings.get(["CONR"]),self._settings.get(["CONG"]),self._settings.get(["CONB"]))
            elif event == octoprint.events.Events.CLIENT_OPENED:
                self._bleStrip.ledcolor(self._settings.get(["COR"]),self._settings.get(["COG"]),self._settings.get(["COB"]))
            elif event == octoprint.events.Events.PRINT_DONE:
                self._bleStrip.ledcolor(self._settings.get(["PDR"]),self._settings.get(["PDG"]),self._settings.get(["PDB"]))
            elif event == octoprint.events.Events.SHUTDOWN:
                self._bleStrip.ledcolr(self._settings.get(["SDR"]),self._settings.get(["SDG"]),self._settings.get(["SDB"]))

__plugin_name__ = "ble Strip"
__plugin_implementation__ = bleStripPlugin()
