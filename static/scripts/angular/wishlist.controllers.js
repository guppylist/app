wishlistApp.controller('ProductSearchController', function($scope, $http) {
  $scope.onSearchQueryChange = function() {
    console.log($scope.q);
    $scope.searchProducts();
  };

  $scope.searchProducts = function() {
    $http.get('/api/search/products/?q=' + $scope.q).then(function(data) {
      console.log(data.data);
      $scope.products = data.data;
    }, function() {

    });
  };
});
