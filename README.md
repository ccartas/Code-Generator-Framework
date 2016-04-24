# Python Code-Generator-Framework

Code generator framework written using Python templatization.

Supported Languages:
- Java
- JavaScript (AngularJS)

How to Run?
- Install Python 3.4.3;
- Open the config.json file located in the config folder: -> language attribute supported values: "java" or "javascript"
                                                          -> package attribute: "your.package.name" (selected language: java)
                                                          -> type attribute: "class" or "interface (selected language: java)
                                                          -> name attribute: Names of the classes or interfaces separated by ","
                                                          -> attributes: "attribute name" : "attribute type"
                                                          -> methods: "method name" : "method type" (if interface type is selected)
                                                          -> appName: "name of javascript app" (selected language: javascript)
                                                          -> modules: Modules names separated by "," (selected language: javascript)
- Run app.py 

How it works?

Java: If for the type is selected "class" the program will create the specified classes that contains:
      - Default constructors;
      - Private attributes;
      - Getters and Setters;
      
      If for the type is selected "interface" the program will create the specified interfaces that contains:
      - public methods declared in the config file;
      
JavaScript: Create an application with containing modules and for each module 
            it creates specific services and controllers with their dependencies.
            
            For example: appName: "shopApp"
                         modules: "user,products, payment"
            The directory tree will look like this: 
            
            shopApp
             user
              controller
               userController.js
              service
               userService.js
              app-user.js
             products
              controller
               productsController.js
              service
               productsService.js
              app-products.js
             payment
              controller
               paymentController.js
              service
               paymentService.js
              app-payment.js
             app.js
