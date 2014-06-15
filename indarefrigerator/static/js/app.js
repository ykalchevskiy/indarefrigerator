(function() {
    var app = angular.module('refrigerator', []);

    app.controller('RefrigeratorController', function($http) {
        var refrigerator = this;

        refrigerator.product = {};
        refrigerator.products = {};

        $http.get('/api/products').success(function(data) {
            refrigerator.products = data.objects;
        });

        refrigerator.createProduct = function() {
            $http.post('/api/products', refrigerator.product)
                    .success(function(data) {
                        refrigerator.products.push(data);
                        refrigerator.product = {};
                        alert('Created!');
                    })
                    .error(function(response) {
                        alert('Error: ' + response.message);
                    });
        };

        refrigerator.updateProduct = function(product) {
            $http.put('/api/products/' + product.id, product)
                    .success(function(data) {
                        alert('Updated!');
                    })
                    .error(function(response) {
                        alert('Error: ' + response.message);
                    });
        };

        refrigerator.deleteProduct = function(product) {
            $http.delete('/api/products/' + product.id)
                .success(function() {
                    refrigerator.products.splice(refrigerator.products.indexOf(product), 1);
                    alert('Deleted!');
                })
                .error(function(response) {
                    alert('Error: ' + response.message);
                });
        };

        refrigerator.getRemaining = function(product) {
            var now = new Date,
                todayMilliseconds = Date.UTC(now.getFullYear(), now.getMonth(), now.getDate()),
                endDateMilliseconds = Date.parse(product.end_date),
                dayMilliseconds = 1000 * 60 * 60 * 24;
            if (!endDateMilliseconds) {
                return '?';
            }
            return (endDateMilliseconds - todayMilliseconds) / dayMilliseconds;
        };

        // helpers

        refrigerator.getDate = function() {
            return new Date().toJSON().slice(0,10);
        };
    });

    $('.datepicker').datepicker({
        changeMonth: true,
        changeYear: true,
        dateFormat: "yy-mm-dd"
    });
})();
