var wishlistApp = angular.module('wishlist-app', []);

wishlistApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[{');
  $interpolateProvider.endSymbol('}]');
});