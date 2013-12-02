$(function () {
    $.ajaxSettings.traditional = true;
    $("[data-toggle='popover']").popover();

    $('#search-field').typeahead({
        minLength: 2,
        items: 30,
        source: function(q, process) {
            var data = new Array;

            return $.ajax({
                url: 'http://completion.amazon.com/search/complete',
                type: 'GET',
                cache: false,
                dataType: 'jsonp',
                success: function (response) {
                    for (var i in response[1]) {
                        data.push(response[1][i]);
                    }
                    return process(data);
                },
                data: {
                    q: q,
                    'search-alias': 'videogames',
                    mkt: '1',
                    callback: '?'
                }
            });
        },
        updater: function(item) {
            this.$element[0].value = item;
            this.$element[0].form.submit();
            return item;
        }
    });
});

/* AngularJS */
angular.module('guppylist', ['ngCookies'], function($compileProvider) {
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
    })
})
.run( function run( $http, $cookies ){
    // For CSRF token compatibility with Django
    $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
})
.config(function ($httpProvider) {
    $httpProvider.defaults.transformRequest = function(data) {
        if (data === undefined) {
            return data;
        }
        return $.param(data);
    }

    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
});

function ListAddProductFormController($scope, $http, $cookies) {
    $scope.init = function() {
        $scope.loaderShow = false;
        $scope.listAddForm = eval(scripts.list.addProductToListForm);

        // Existing list select box.
        $scope.lists = eval(scripts.list.lists);

        // Initialize form.
        $scope.form = {
            'tab': 'existing',
            'product_id': scripts.list.productId,
            'list_id': $scope.lists[0],
        };
    }

    $scope.tabClick = function(type) {
        $scope.form.tab = type;
    }

    $scope.formSubmit = function() {
        $scope.loaderShow = true;

        // Prepare list_id.
        $scope.form.list_id = $scope.form.list_id.id;
        console.log($scope.form);

        var url = '/lists/add/new/submit/';
        if ($scope.form.tab == 'existing') {
            url = '/lists/add/existing/submit/';
        }

        $http.post(url, $scope.form).
            success(function(response, status) {
                console.log(response);
                if (response.success) {
                    $('#addToList').modal('hide');
                } else {
                    $scope.listAddForm = response.form;
                }
                $scope.loaderShow = false;
            }).
            error(function(data, status) {
                console.log('error');
            });
    }

    $scope.init();
}