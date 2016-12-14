// Timeout instance on when the user is typing.
var keypressTimeout;
var keypressDelay = 500;

/**
 * Product search page.
 */
wishlistApp.controller('ProductSearchController', function($scope, $http, sharedProperties, loader, modalRouter) {
  /**
   * Handler when the search query is changed.
   */
  $scope.onSearchQueryChange = function() {
    if ($scope.q.length >= 3) {
      loader.on('#product-search-results');

      clearTimeout(keypressTimeout);

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
    sharedProperties.setProperty('product', product, function() {
      $scope.$root.$broadcast('productSelected');
    });
  };

  // DEBUG DEBUG
  $scope.q = 'hamilton';
  $scope.onSearchQueryChange();
});

/**
 * Product details modal.
 */
wishlistApp.controller('ProductInfoController', function($scope, $http, sharedProperties, loader, modalRouter) {
  /**
   * Broadcast receiver when a product is selected.
   */
  $scope.$on('productSelected', function(event) {
    $scope.product = sharedProperties.getProperty('product');

    $scope.getProductDetails($scope.product, function(details) {
      modalRouter.showSection('product-section-info');

      $scope.productDetails = details;
    });
  });

  /**
   * Calls the API to get similar products.
   */
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
    sharedProperties.setProperty('product', product, function() {
      $scope.$root.$broadcast('productSelected');

      // Scroll to the top of the modal.
      $('body').animate({scrollTop: 0}, 'slow');
    });
  };

  /**
   * Click handler for the the add-to-list action.
   */
  $scope.onProductAddToListClick = function() {
    $scope.$root.$broadcast('addToList');
  }
});

/**
 * Product add to list modal.
 */
wishlistApp.controller('ProductAddToListController', function($scope, $http, sharedProperties, loader, modalRouter) {
  /**
   * Broadcast receiver for when the add-to-list action is triggered.
   */
  $scope.$on('addToList', function(event) {
    $scope.product = sharedProperties.getProperty('product');
    modalRouter.showSection('product-section-add-to-list');

    $scope.getUserWishlists(function(response) {
      $scope.lists = response.data.results;
    });
  });

  /**
   * Click handler for the the create-list action.
   */
  $scope.onCreateListClick = function() {
    $scope.$root.$broadcast('createList');
  }

  /**
   * Click handler for when a product is added to a list.
   */
  $scope.onProductAddToListClick = function(product, list) {
    console.log(product);
    console.log('list:', list);
  };

  /**
   * Get's the user's wishlists via the API.
   */
  $scope.getUserWishlists = function(callback) {
    $http.get('/api/lists/?userId=1').then(function(response) {
      callback(response);
    }, function() {

    });;
  };
});

/**
 * Product add to list modal.
 */
wishlistApp.controller('ProductCreateListController', function($scope, $http, sharedProperties, loader, modalRouter) {
  $scope.$on('createList', function(event) {
    $scope.product = sharedProperties.getProperty('product');
    modalRouter.showSection('product-section-create-list');
  });

  /**
   * Click handler for when creat-list form is cancelled.
   */
  $scope.onCancelCreateList = function() {
    $scope.listName = '';
    $scope.$root.$broadcast('addToList');
  };

  /**
   * Click handler for when a new list is created.
   */
  $scope.onCreateListClick = function(product) {
    console.log(product);
    console.log('list name:', $scope.listName);
  };
});