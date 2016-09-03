var keypressTimeout;

wishlistApp.controller('ProductSearchController', function($scope, $http) {
  $scope.onSearchQueryChange = function() {
    if ($scope.q.length >= 3) {
      clearTimeout(keypressTimeout);

      console.log($scope.q);
      keypressTimeout = setTimeout(function() {
        $scope.searchProducts();
      }, 450);
    }
  };

  $scope.searchProducts = function() {
    $http.get('/api/search/products/?q=' + $scope.q).then(function(data) {
      $scope.products = data.data;
      console.log($scope.products)
    }, function() {

    });
  };

  // DEBUG DEBUG
  $scope.q = 'sfgiants';
  $scope.searchProducts();
});
