/**
 * Get and set properties/objects that are shared between controllers.
 */
wishlistApp.service('sharedProperties', function () {
  var properties = {};

  return {
    getProperty: function(name) {
      return properties[name];
    },
    setProperty: function(name, value) {
      properties[name] = value;
    }
  };
});