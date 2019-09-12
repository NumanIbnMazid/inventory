var myApp = angular.module("myApp", []);

myApp.controller("appCtrl", function ($scope, $http) {

    $scope.orderType = 'sell';
    $scope.orderDate = new Date();


    // //get All Products info
    // $scope.getMaxOrderNo = function () {
    //     $http({
    //         method: 'GET',
    //         url: 'orders/maxOrderNo'
    //     }).then(function (response) {
    //         $scope.orderNo = response.data;
    //     });
    // };
    // //call getAllProduct method
    // $scope.getMaxOrderNo();


    //get All Products info
    $scope.products = [{id:100, title:'example', quantity:2, price:30}];
    // var productList_url = 'http://127.0.0.1:8000/api/product/list/';
    // $scope.getAllProduct = function () {
    //     $http({
    //         method: 'GET',
    //         url: productList_url
    //     }).then(function (response) {
    //         $scope.products = response.data;
    //         // alert(response.data);
    //     });
    // };
    // //call getAllProduct method
    // $scope.getAllProduct();


    $scope.clickedProduct = {};



    // //get All Customer info
    // $scope.customers = [];
    // $scope.getAllCustomer = function () {
    //     $http({
    //         method: 'GET',
    //         url: 'customers/allCustomer'
    //     }).then(function (response) {
    //         $scope.customers = response.data;
    //     });
    // };
    // //call getAllProduct method
    // $scope.getAllCustomer();


    // $scope.clickedCustomer = {};


    //add to cart
    $scope.qty = 0;
    $scope.total = 0;

    $scope.cartProduct = [];
    $scope.finalTotal = 0;
    $scope.addToCart = function () {

        $scope.cp = {};
        $scope.cp = $scope.clickedProduct;
        $scope.cp.cartqty = 1;
        $scope.cp.subTotal = $scope.cp.cartqty * $scope.cp.price;

        //$scope.cartProduct.push($scope.cp);

        if ($scope.cartProduct.length === 0) {
            $scope.cartProduct.push($scope.cp);
            $scope.finalTotal += $scope.cp.subTotal;
        } else {
            var i = 0;
            for (i = 0; i < $scope.cartProduct.length; i++) {

                if ($scope.cartProduct[i].pid === $scope.cp.pid) {
                    alert('Product Already exist');
                    break;
                }
            }
            if (i === $scope.cartProduct.length) {
                $scope.cartProduct.push($scope.cp);
                $scope.finalTotal += $scope.cp.subTotal;
            }
        }

    };

    $scope.removeCart = function (cp) {
        var i = 0;
        for (i = 0; i < $scope.cartProduct.length; i++) {

            if ($scope.cartProduct[i].pid === $scope.cp.pid) {

                $scope.cartProduct.splice(i, 1);
            }
        }
        $scope.finalTotal = $scope.finalTotal - cp.subTotal;



    }

    $scope.qtyINC = function (cp) {
        cp.cartqty++;
        subTotal1 = cp.price * cp.cartqty;
        $scope.finalTotal = $scope.finalTotal - cp.subTotal + subTotal1;
        cp.subTotal = subTotal1;
    }

  $scope.qtyDec = function (cp) {
        cp.cartqty--;
        subTotal1 = cp.price * cp.cartqty;
        $scope.finalTotal = $scope.finalTotal - cp.subTotal + subTotal1;
        cp.subTotal = subTotal1;
    }


    //checkout
    $scope.checkOut = function () {
        $scope.orderInfo = {
            'orderId': '',
            'cid': '',
            'total': '',
            'orderType': '',
            'orderDate': '',
            orderDetailses:[]
        };
        $scope.orderDetailInfo = {
            'orderDetailId': '',
            'orderId': '',
            'pid': '',
            'qty': '',
            'price': '',
            'subTotal': ''
        };
        $scope.orderProduct = {
            'pid': '',
            'qty': '',
        };

        $scope.orderInfo.orderId = $scope.orderNo;
        $scope.orderInfo.cid = $scope.clickedCustomer.cid;
        $scope.orderInfo.total = $scope.finalTotal;
        $scope.orderInfo.orderType = $scope.orderType;
        $scope.orderInfo.orderDate = $scope.orderDate;

//        alert(
//                'orderId: ' +  $scope.orderInfo.orderId
//                + '\ncid: ' + $scope.orderInfo.cid
//                + '\ntotal: ' + $scope.orderInfo.total
//                + '\norderType: ' + $scope.orderInfo.orderType
//                + '\ndate: ' + $scope.orderInfo.orderDate
//                );

   

        for (var i = 0; i < $scope.cartProduct.length; i++) {
            $scope.orderDetailInfo.orderId = $scope.orderNo;
            $scope.orderDetailInfo.pid = $scope.cartProduct[i].pid;
            $scope.orderDetailInfo.qty = $scope.cartProduct[i].cartqty;
            $scope.orderDetailInfo.price = $scope.cartProduct[i].price;
            $scope.orderDetailInfo.subTotal = $scope.cartProduct[i].subTotal;
            $scope.orderProduct.pid = $scope.orderDetailInfo.pid;
            $scope.orderProduct.qty = $scope.orderDetailInfo.qty;
            $scope.orderInfo.orderDetailses.push($scope.orderDetailInfo);
      
          /*  alert($scope.orderInfo.orderDetailses)
            $http({
                method: 'POST',
                url: 'orderDetails/saveOrderDetails',
                data: angular.toJson($scope.orderDetailInfo),
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(function (response) {
                $scope.os = 1;
            }, function (reason) {
                $scope.oe = 0;
            });

*/
            //update product according to order type 
/*
            $scope.orderUrl = $scope.orderType === 'sell' ? 'products/saleProduct' : 'products/purchaseProduct';




            $http({
                method: 'POST',
                url: $scope.orderUrl,
                data: angular.toJson($scope.orderProduct),
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(function (response) {
                $scope.os = 1;
            }, function (reason) {
                $scope.oe = 0;
            });
*/


        }
     $http({
            method: 'POST',
            url: 'orders/saveOrder',
            data: angular.toJson($scope.orderInfo),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function (response) {
            $scope.os = 1;
        }, function (reason) {
            $scope.oe = 0;
        });


    };









});













//
////var myApp = angular.module("myApp", []);
//
//myApp.controller("appCtrl", function ($scope, $http) {
//
//    $scope.oid = "";
//    $scope.orderType = "sell";
//    $scope.orderDate = new Date();
//    $scope.finalTotal = 0;
//
//    //get All Product
//    $scope.products = [];
//    $scope.getAllProduct = function () {
//        $http({
//            method: 'GET',
//            url: 'products/allProduct'
//        }).then(function (response) {
//            $scope.products = response.data;
//        });
//    };
//    //call method to get all products
//    $scope.getAllProduct();
//
//    //getSelected Product
//    $scope.clickedProduct = {};
//
//    //get All Customer
//    $scope.getAllCustomer = function () {
//        $http({
//            method: 'GET',
//            url: 'customers/allCustomer'
//        }).then(function (response) {
//            $scope.customers = response.data;
//        });
//    };
//    //call method to get all Customer
//    $scope.getAllCustomer();
//
//    //getSelected Customer
//    $scope.clickedCustomer = {};
//
//
//    //order logic control
//    $scope.qty = 0;
//    $scope.total = 0;
//
//
//    //add to cart
//    $scope.cartProduct = [];
//    $scope.addToCart = function () {
//        $scope.clickedProduct.qty = $scope.qty;
//        $scope.status = true;
//
//        if ($scope.cartProduct.length === 0) {
//            $scope.cartProduct.push($scope.clickedProduct);
//            $scope.status = false;
//            //alert("first insert");
//        } else if ($scope.cartProduct.length > 0) {
//            for (var i = 0; i < $scope.cartProduct.length; i++) {
//                if ($scope.cartProduct[i].pid === $scope.clickedProduct.pid) {
//                    alert("Item already available in Cart");
//                    $scope.status = false;
//                    break;
//                }
//            }
//        }
//
//        if ($scope.status === true) {
//            $scope.cartProduct.push($scope.clickedProduct);
//        }
//
//        $scope.finalTotal = 0;
//        for (var i = 0; i < $scope.cartProduct.length; i++) {
//            $scope.finalTotal = $scope.finalTotal + ($scope.cartProduct[i].price * $scope.cartProduct[i].qty);
//        }
//
//        $scope.qty = 0;
//        $scope.clickedProduct = {};
//    };
//
//    //remove from cart
//    $scope.rCkickedProduct = {};
//    $scope.removeProduct = function (product) {
//        $scope.rClickedProduct = product;
//        $scope.value = -1;
//        alert($scope.cartProduct.indexOf($scope.rClickedProduct));
//        $scope.value = $scope.cartProduct.indexOf($scope.rClickedProduct);
//        if ($scope.value >= 0) {
//            $scope.cartProduct.splice($scope.value, 1);
//        }
//    };
//
//
//    //CheckOut
//    $scope.checkOut = function () {
//        $scope.orderDetails = {'odid': '', 'oid': '', 'pid': '', 'price': '', 'qty': ''};
//        $scope.order = {'oid': '', 'cid': '', 'total': '', 'orderType': '', 'orderDate': ''};
//
//
//        //make order perform
//        $scope.order.cid = $scope.clickedCustomer.cid;
//        $scope.order.total = $scope.finalTotal;
//        $scope.order.orderType = $scope.orderType;
//        $scope.order.orderDate = $scope.orderDate;
//
//        $http({
//            method: 'POST',
//            url: 'orders/order',
//            data: angular.toJson($scope.order),
//            headers: {
//                'Content-Type': 'application/json'
//            }
//        }).then(function (response) {
//            $scope.os = 1;
//        }, function (reason) {
//            $scope.oe = 0;
//        });
//
//
//        //make order details perform
//        for (var i = 0; i < $scope.cartProduct.length; i++) {
//            $scope.orderDetails.oid = $scope.oid;
//            $scope.orderDetails.pid = $scope.cartProduct[i].pid;
//            $scope.orderDetails.price = $scope.cartProduct[i].price;
//            $scope.orderDetails.qty = $scope.cartProduct[i].qty;
//            //alert("loop: " + (i + 1));
//            $http({
//                method: 'POST',
//                url: 'orderdetails/orderdetail',
//                data: angular.toJson($scope.orderDetails),
//                headers: {
//                    'Content-Type': 'application/json'
//                }
//            }).then(function (response) {
//                $scope.ods = 1;
//            }, function (reason) {
//                $scope.ode = 0;
//            });
//
//
//            //make product update perform
//            $scope.updatedProduct = {'pid': '', 'pname': '', 'price': '', 'qty': ''};
//
//            //alert($scope.productsAgain.length);
//            for (var j = 0; j < $scope.productsAgain.length; j++) {
//                //alert("enter to loop");
//                if ($scope.productsAgain[j].pid === $scope.orderDetails.pid) {
//                    //alert("product stock: " + $scope.productsAgain[i].qty);
//                    //alert("cart qty: " + $scope.orderDetails.qty);
//                    if ($scope.orderType === 'sell') {
//                        $scope.changedQty = $scope.productsAgain[j].qty - $scope.orderDetails.qty;
//                    } else {
//                        $scope.changedQty = parseInt($scope.productsAgain[j].qty) + parseInt($scope.orderDetails.qty);
//                    }
//                    //alert("changable qty: " + $scope.changedQty);
//                    $scope.updatedProduct.pid = $scope.productsAgain[j].pid;
//                    $scope.updatedProduct.pname = $scope.productsAgain[j].pname;
//                    $scope.updatedProduct.price = $scope.productsAgain[j].price;
//                    $scope.updatedProduct.qty = $scope.changedQty;
//                }
//            }
//
//            $http({
//                method: 'PUT',
//                url: 'products/product',
//                data: angular.toJson($scope.updatedProduct),
//                headers: {
//                    'Content-Type': 'application/json'
//                }
//            }).then(function (response) {
//                $scope.ps = 1;
//            }, function (reason) {
//                $scope.pe = 0;
//            });
//
//        }
//
//
//
//
//
//    };
//
//    //safty
//    $scope.productsAgain = [];
//    $scope.productAgainRequest = function () {
//        $http({
//            method: 'GET',
//            url: 'products/allProduct'
//        }).then(function (response) {
//            $scope.productsAgain = response.data;
//        });
//    };
//    $scope.productAgainRequest();
//
//
//
//});
//
//
//
//myApp.controller("orderDetailsChartCtrl", function ($scope, $http) {
//
//    //get All Customer
//    $scope.getAllCustomer = function () {
//        $http({
//            method: 'GET',
//            url: 'customers/allCustomer'
//        }).then(function (response) {
//            $scope.customers = response.data;
//        });
//    };
//    //call method to get all Customer
//    $scope.getAllCustomer();
//
//
//    //get all orders info
//    $scope.orders = [];
//    $scope.getAllOrders = function () {
//        $http({
//            method: 'GET',
//            url: 'orders/order'
//        }).then(function (response) {
//            $scope.orders = response.data;
//        });
//    };
//    //call method to get all orders info
//    $scope.getAllOrders();
//
//
//   
//
//
//    //get order details info by order id
//    $scope.clickedItem = {};
//    $scope.findOd = function (order) {
//        $scope.clickedItem = order;
//
//        $http({
//            method: 'GET',
//            url: 'orderdetails/getOdDetailsByOID/' + $scope.clickedItem.oid
//        }).then(function (response) {
//            $scope.orderDetails = response.data;
//        });
//
//    };
//
//
//
//});


