/*
 * View model for OctoPrint-V8Timelapse
 *
 * Author: Jack Minardi
 * License: AGPLv3
 */
$(function() {
  function V8TimelapseViewModel(parameters) {
    var self = this;
    self.loginState = parameters[0];
    self.popup = undefined;

    self.onDataUpdaterPluginMessage = function(plugin, data) {
      if (plugin != "v8timelapse") {
        return;
      }
      if (data.hasOwnProperty("error_deleting")) {
        if (data.error_deleting) {
          self._showPopup({
            title: gettext("Deleting Files Failed"),
            text: gettext("There was an issue removing the images from the filesystem."),
            type: "error",
            hide: true,
            buttons: {
              sticker: false
            }
          });
        } else {
          self._showPopup({
            title: gettext("Files Successfully Deleted"),
            text: gettext("The images were deleted from the filesystem."),
            type: "success",
            hide: true,
            buttons: {
              sticker: false
            }
          });
        }
      }
    };

    self.delete_files = function() {
      $.ajax({
        type: "POST",
        url: "/api/plugin/v8timelapse",
        data: JSON.stringify({
          command: "delete_files"
        }),
        contentType: "application/json; charset=utf-8",
        dataType: "json"
      });
    };

    self.download_zip = function(){
      $.get( "/api/plugin/v8timelapse", function(data) {
        if (data.can_download) {
          window.location = "plugin/v8timelapse/download";
        } else {
          self._showPopup({
            title: gettext("Download failed."),
            text: gettext("No images exist on the file system."),
            type: "error",
            hide: false,
            buttons: {
              sticker: false
            }
          });
        }
      }, "json");
    };

    self._showPopup = function(options, eventListeners) {
      self._closePopup();
      self.popup = new PNotify(options);

      if (eventListeners) {
        var popupObj = self.popup.get();
        _.each(eventListeners, function(value, key) {
          popupObj.on(key, value);
        })
      }
    };

    self._closePopup = function() {
      if (self.popup !== undefined) {
        self.popup.remove();
      }
    };
  }

  ADDITIONAL_VIEWMODELS.push([
    V8TimelapseViewModel,
    ["loginStateViewModel"],
    ["#settings_plugin_v8timelapse"]
  ]);
});
