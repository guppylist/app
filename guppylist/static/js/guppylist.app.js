/* AngularJS */
var guppylistApp = angular.module('guppylist', ['ngCookies', 'guppylistControllers'], function($compileProvider) {
  $compileProvider.directive('compile', function($compile) {
    return function(scope, element, attrs) {
      scope.$watch(
      function(scope) {
        return scope.$eval(attrs.compile);
      },
      function(value) {
        element.html(value);
        $compile(element.contents())(scope);
      }
      );
    };
  });
});

guppylistApp.run(function run($http, $cookies){
  // For CSRF token compatibility with Django
  $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
});

guppylistApp.config(function ($httpProvider) {
  $httpProvider.defaults.transformRequest = function(data) {
    if (data === undefined) {
      return data;
    }
    return $.param(data);
  }

  $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
}).
config(['$locationProvider', function($locationProvider){
  $locationProvider.html5Mode(true).hashPrefix('!');
}]).
config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
});