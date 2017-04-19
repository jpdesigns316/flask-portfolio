var app = angular.module("computer", ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.
        when('/main', {
            templateUrl: 'main.html',
            controller: 'MainCtrl'
        }).
        when('/about', {
            templateUrl: 'about.html',
            controller: 'MainCtrl'
        }).
        when('/resume', {
            templateUrl: 'resume.html',
            controller: 'ResumeCtrl'
        }).
        when('/projects', {
            templateUrl: 'projects.html',
            controller: 'ProjectsCtrl'
        }).
        when('/contact', {
            templateUrl: 'contact.html',
            controller: 'ContactCtrl'
        }).
        otherwise({
            redirectTo: '/main'
        });
    }])

    .controller('MainCtrl', ['$scope', '$http', function($scope, $http) {
        $scope.person = "Jonathan D. Peterson";
        $http.get("json/front.json")
            .then(function(response) {
                $scope.links = response.data;
            })
    }])

    .controller('ResumeCtrl', ['$scope', '$http', function($scope, $http) {

        $http.get("json/bio.json")
            .then(function(response) {
                $scope.bio = response.data;
            });
        $http.get("json/education.json")
            .then(function(response) {
                $scope.schools = response.data;
            });
        $http.get("json/skills.json")
            .then(function(response) {
                $scope.skills = response.data;
            });


    }])

    .controller('ProjectsCtrl', ['$scope', '$http', function($scope, $http) {
        $http.get("json/projects.json")
            .then(function(response) {
                $scope.projects = response.data;
            })
    }])


    .controller('ContactCtrl', function($scope, $http) {
        $scope.result = 'hidden'
        $scope.resultMessage;
        $scope.formData; //formData is an object holding the name, email, subject, and message
        $scope.submitButtonDisabled = false;
        $scope.submitted = false; //used so that form errors are shown only after the form has been submitted
        $scope.submit = function(contactform) {
            $scope.submitted = true;
            $scope.submitButtonDisabled = true;
            if (contactform.$valid) {
                $http({
                    method: 'POST',
                    url: 'contact-form.php',
                    data: $.param($scope.formData), //param method from jQuery
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    } //set the headers so angular passing info as form data (not request payload)
                }).success(function(data) {
                    console.log(data);
                    if (data.success) { //success comes from the return json object
                        $scope.submitButtonDisabled = true;
                        $scope.resultMessage = data.message;
                        $scope.result = 'bg-success';
                    } else {
                        $scope.submitButtonDisabled = false;
                        $scope.resultMessage = data.message;
                        $scope.result = 'bg-danger';
                    }
                });
            } else {
                $scope.submitButtonDisabled = false;
                $scope.resultMessage = 'Failed <img src="http://www.chaosm.net/blog/wp-includes/images/smilies/icon_sad.gif" alt=":(" class="wp-smiley">  Please fill out all the fields.';
                $scope.result = 'bg-danger';
            }
        }
    });
