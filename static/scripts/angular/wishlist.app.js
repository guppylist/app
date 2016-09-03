var wishlistApp = angular.module('wishlist-app', []);

wishlistApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');
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