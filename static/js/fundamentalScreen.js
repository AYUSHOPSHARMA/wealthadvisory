var app = angular.module("myApp", []);
app.controller("w3TestDirective",['$scope', '$http', function($scope, $http) {
   $scope.ScreenerSelectOnChangePE = function(val){
            $scope.PE = val;
   }
}]);