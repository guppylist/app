var guppylistControllers = angular.module('guppylistControllers', []);


function SearchProductController($scope, $http, $timeout, $location) {
    $scope.searchProduct = function() {
        $http.get('search/data?q=' + $scope.q).
        success(function(data, status, headers, config) {
            var searchScope = angular.element($('#product-search-results')).scope();
            $searchScope.products = data.products;
        }).
        error(function(data, status, headers, config) {

        });
    }
}

function ListAddProductFormController($scope, $http, $cookies) {
    $scope.init = function() {
        $scope.loaderShow = false;
        $scope.listAddForm = eval(scripts.list.addProductToListForm);

        // Existing list select box.
        $scope.lists = eval(scripts.list.lists);

        // Set default form state.
        var tab = 'existing';
        if (_.isEmpty($scope.lists)) {
            tab = 'new';
        }

        // Initialize form.
        $scope.form = {
            'tab': tab,
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
        if (!_.isEmpty($scope.form.list_id)) {
            $scope.form.list_id = $scope.form.list_id.id;
        }

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