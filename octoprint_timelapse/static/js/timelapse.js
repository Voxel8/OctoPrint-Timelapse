/*
 * View model for OctoPrint-Timelapse
 *
 * Author: Jack Minardi
 * License: AGPLv3
 */
$(function() {
    function TimelapseViewModel(parameters) {
        var self = this;

        // assign the injected parameters, e.g.:
        // self.loginStateViewModel = parameters[0];
        // self.settingsViewModel = parameters[1];

		self.downloadZip = function(){
			console.log("WOOOOO");
			window.location = 'plugin/timelapse/download';
		};
    }

    // view model class, parameters for constructor, container to bind to
    OCTOPRINT_VIEWMODELS.push([
        TimelapseViewModel,

        // e.g. loginStateViewModel, settingsViewModel, ...
        [ /* "loginStateViewModel", "settingsViewModel" */ ],

        // e.g. #settings_plugin_timelapse, #tab_plugin_timelapse, ...
        ['#settings_plugin_timelapse']
    ]);
});
