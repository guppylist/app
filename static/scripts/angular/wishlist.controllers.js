// Timeout instance on when the user is typing.
var keypressTimeout;
var keypressDelay = 500;

/**
 * Product search page.
 */
wishlistApp.controller('ProductSearchController', function($scope, $http, sharedProperties, loader) {
  /**
   * Handler when the search query is changed.
   */
  $scope.onSearchQueryChange = function() {
    if ($scope.q.length >= 3) {
      loader.on('#product-search-results');

      clearTimeout(keypressTimeout);

      console.log($scope.q);
      keypressTimeout = setTimeout(function() {
        $scope.searchProducts($scope.q, function(response) {
          $scope.products = response.data;
          loader.off('#product-search-results');
        });
      }, keypressDelay);
    }
  };

  /**
   * Get search results from the Wishlist API.
   */
  $scope.searchProducts = function(q, callback) {
    $http.get('/api/search/products/?q=' + q).then(function(response) {
      callback(response);
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
  $scope.onSearchQueryChange();
});


/**
 * Product details modal.
 */
wishlistApp.controller('ProductDetailsController', function($scope, $http, sharedProperties, loader) {
  $scope.$on('productSelected', function(event) {
    $scope.product = sharedProperties.getProperty('product');

    $scope.getProductDetails($scope.product, function(details) {
      $scope.productDetails = details;
    });
  });

  $scope.getProductDetails = function(product, callback) {
    loader.on('.similar-products');
    $http.get('/api/products/' + product.asin + '/similar').then(function(data) {
      $scope.similarProducts = data.data;
      loader.off('.similar-products');
    }, function() {

    });
  }

  /**
   * Click handler when a product is clicked.
   */
  $scope.onProductClick = function(product) {
    // Set the selected product to be accessed globally.
    sharedProperties.setProperty('product', product);

    $scope.$root.$broadcast('productSelected');

    // Scroll to the top of the modal.
    $('body').animate({scrollTop: 0}, 'slow');
  };
});
