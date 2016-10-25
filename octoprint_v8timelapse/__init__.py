# coding=utf-8
from __future__ import absolute_import
import os
import shutil

import flask

import octoprint.plugin
from octoprint.server.util.flask import restricted_access
from octoprint.server import admin_permission


class V8TimelapsePlugin(octoprint.plugin.SettingsPlugin,
                        octoprint.plugin.AssetPlugin,
                        octoprint.plugin.TemplatePlugin,
                        octoprint.plugin.SimpleApiPlugin,
                        octoprint.plugin.BlueprintPlugin,
                        octoprint.plugin.StartupPlugin):

    def get_settings_defaults(self):
        return dict(
        )

    def get_assets(self):
        return dict(
            js=["js/v8timelapse.js"]
        )

    def get_api_commands(self):
        return dict(
            delete_files=[]
        )

    def on_api_command(self, command, data):
        if command == "delete_files":
            self.delete_files()
        else:
            self._logger.info("Unknown command: " + command)

    def on_api_get(self, request):
        self.zip_contents()
        return flask.jsonify(can_download=self.file_exists())

    def zip_contents(self):
        self.create_directory()

        directory = os.path.expanduser("~/pics/")
        filename = "timelapse"
        shutil.make_archive(
            os.path.join(directory, filename), 'zip', directory)

    def create_directory(self):
        directory = os.path.expanduser("~/pics/")
        if not os.path.exists(directory):
            os.makedirs(directory)

    def on_after_startup(self):
        self.create_directory()

    def file_exists(self):
        return os.path.isfile(os.path.expanduser("~/pics/timelapse.zip"))

    def delete_files(self):
        try:
            shutil.rmtree(os.path.expanduser("~/pics/"))
            self._plugin_manager.send_plugin_message(self._identifier, dict(
                error_deleting=False))
        except:
            self._plugin_manager.send_plugin_message(self._identifier, dict(
                error_deleting=True))

    def get_template_configs(self):
        return [
            dict(type="settings", name="Timelapse",
                 data_bind="visible: loginState.isAdmin()"),
        ]

    def get_update_information(self):
        return dict(
            v8timelapse=dict(
                displayName="Timelapse Plugin",
                displayVersion=self._plugin_version,

                type="github_commit",
                user="Voxel8",
                repo="OctoPrint-V8Timelapse",
                current=self._plugin_version,

                pip=("https://github.com/Voxel8/OctoPrint-V8Timelapse/"
                     "archive/{target_version}.zip")
            )
        )

    @octoprint.plugin.BlueprintPlugin.route("/download", methods=["GET"])
    def download(self):
        return flask.send_from_directory(os.path.expanduser("~/pics/"),
                                         "timelapse.zip",
                                         as_attachment=True)

    def is_blueprint_protected(self):
        return False


__plugin_name__ = "Timelapse Plugin"


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = V8TimelapsePlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {}
