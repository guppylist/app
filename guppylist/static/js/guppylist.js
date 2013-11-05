function MeadowsListNewsController($scope) {
  $scope.readMoreStyle = {display: 'block'};

  $scope.showListNewsDetails = function() {
    $scope.listNewsDetailsStyle = {display: 'block'};
    $scope.readMoreStyle = {display: 'none'};
  }
}