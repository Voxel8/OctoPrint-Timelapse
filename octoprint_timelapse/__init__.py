# coding=utf-8
from __future__ import absolute_import

from flask import send_from_directory

import octoprint.plugin
from octoprint.server.util.flask import restricted_access
from octoprint.server import admin_permission

class TimelapsePlugin(octoprint.plugin.SettingsPlugin,
                      octoprint.plugin.AssetPlugin,
                      octoprint.plugin.TemplatePlugin,
                      #octoprint.plugin.SimpleApiPlugin,
                      octoprint.plugin.BlueprintPlugin):

    ##~~ SettingsPlugin mixin

    def get_settings_defaults(self):
        return dict(
            # put your plugin's default settings here
        )

    ##~~ AssetPlugin mixin

    def get_assets(self):
        # Define your plugin's asset files to automatically include in the
        # core UI here.
        return dict(
            js=["js/timelapse.js"],
            css=["css/timelapse.css"],
            less=["less/timelapse.less"]
        )

    ##~~ Softwareupdate hook

    def get_update_information(self):
        # Define the configuration for your plugin to use with the Software Update
        # Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
        # for details.
        return dict(
            timelapse=dict(
                displayName="Timelapse Plugin",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="jminardi",
                repo="OctoPrint-Timelapse",
                current=self._plugin_version,

                # update method: pip
                pip="https://github.com/jminardi/OctoPrint-Timelapse/archive/{target_version}.zip"
            )
        )

    ##~~ SimpleApiPlugin

    #def on_api_get(self, request):
    #    #if self.active_script_id is not None:
    #    #    title = self.script_titles[self.active_script_id]
    #    #else:
    #    #    title = None
    #    #return flask.jsonify(running=self._is_running(),
    #    #                     current_script_title=title,
    #    #                     script_titles=self.script_titles)
    #    print 'GET CALLED'
    #    return send_from_directory('/Users/jack/Desktop',
    #                               'dl.zip', as_attachment=True)

    ##~~ BlueprintPlugin

    @octoprint.plugin.BlueprintPlugin.route("/download", methods=["GET"])
    #@restricted_access
    #@admin_permission.require(403)
    def upload_file(self):
        #if "base64String" not in flask.request.values:
        #    return flask.make_response("Expected a base64String value", 400)

        #try:
        #    decode = base64.b64decode(flask.request.values['base64String'])
        #    self._check_directories()

        #    # Delete any firmware files that may exist when using
        #    # custom firmware
        #    self._delete_firmware_files()
        #    with open(os.path.join(self.firmware_directory,
        #                           "firmware.hex"), "wb") as firmware:
        #        firmware.write(decode)
        #        firmware.close()
        #except (TypeError, IOError) as e:
        #    error_text = "There was an issue saving the firmware file."
        #    self._logger.warn("Error saving firmware file: %s" % str(e))
        #    self._update_status(
        #        False, "error", error_text)
        #    return flask.make_response(error_text, 400)

        #self._start_update()
        #return flask.make_response("OK", 200)
        return send_from_directory('/Users/jack/Desktop',
                                   'dl.zip', as_attachment=True)




__plugin_name__ = "Timelapse Plugin"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = TimelapsePlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        #"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
