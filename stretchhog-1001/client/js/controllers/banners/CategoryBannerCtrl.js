app.controller('CategoryBannerCtrl', [
	'$scope', 'SlugService', '$stateParams',
	function ($scope, SlugService, $stateParams) {

		SlugService.getCategoryBySlug($stateParams.categorySlug).then(function (data) {
			$scope.item = data;
		});
	}]);


