/**
 * Get and set properties/objects that are shared between controllers.
 */
wishlistApp.service('sharedProperties', function () {
  var properties = {};

  var service = {
    getProperty: function(name) {
      return properties[name];
    },
    setProperty: function(name, value, callback) {
      properties[name] = value;
      callback();
    }
  }

  return service;
});

/**
 * Show/hides loader overlay.
 */
wishlistApp.service('loader', function() {
  var service = {
    on: function(element, text) {
      if (text) {
        $(element + ' .loader span').html(text);
      }
      $(element + ' .loader').show();
    },
    off: function(element) {
      $(element + ' .loader').hide();
    }
  };

  return service;
});

/**
 * Centralized modal event handler across multiple controllers.
 */
wishlistApp.service('modalRouter', function() {
  var service = {
    /**
     * Shows a specified section and hides all the others.
     */
    showSection: function(id) {
      $('.product-modal-section').hide();
      $('#' + id).show();
    }
  };

  return service;
});

/**
 * Outputs the rating indicator markup.
 *
 * @param rating - integer rating to be converted.
 * @param type - graphite or teacher rating.
 */
//wishlistApp.filter('rating_indicator', function() {
//  return function(rating, type, scope) {
//    type = type ? type : 'graphite';
//
//    var output = '<span class="quiet">not rated</span>';
//    if (rating) {
//      output = '<span class="rating-star small ' + type + ' rating-' + Math.round(rating) + '"></span>';
//    }
//
//    return output;
//  }
//});