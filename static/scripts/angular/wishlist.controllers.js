// Timeout instance on when the user is typing.
var keypressTimeout;
var keypressDelay = 500;

/**
 * Product search page.
 */
wishlistApp.controller('ProductSearchController', function($scope, $http, sharedProperties) {
  /**
   * Handler when the search query is changed.
   */
  $scope.onSearchQueryChange = function() {
    if ($scope.q.length >= 3) {
      clearTimeout(keypressTimeout);

      console.log($scope.q);
      keypressTimeout = setTimeout(function() {
        $scope.searchProducts();
      }, keypressDelay);
    }
  };

  /**
   * Get search results from the Wishlist API.
   */
  $scope.searchProducts = function() {
    $http.get('/api/search/products/?q=' + $scope.q).then(function(data) {
      $scope.products = data.data;
      console.log($scope.products)
    }, function() {

    });
  };

  /**
   * Click handler when a product is clicked.
   */
  $scope.onProductClick = function(product) {
    // Set the selected product to be accessed globally.
    sharedProperties.setProperty('product', product);

    $scope.$root.$broadcast('productSelected');
  };

  // DEBUG DEBUG
  $scope.q = 'hamilton';
  $scope.searchProducts();
});


/**
 * Product details modal.
 */
wishlistApp.controller('ProductDetailsController', function($scope, $http, sharedProperties) {
  $scope.$on('productSelected', function(event) {
    $scope.product = sharedProperties.getProperty('product');

    $scope.getProductDetails($scope.product, function(details) {
      $scope.productDetails = details;
    });
  });

  $scope.getProductDetails = function(product, callback) {
    $http.get('/api/products/' + product.asin + '/similar').then(function(data) {
      $scope.similarProducts = data.data;
    }, function() {

    });
  }
});
