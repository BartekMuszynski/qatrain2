#### qa-train
This framework is made for training purposes. It will include UI and API tests performed on github.

## Framework structure
src and tests directories are in seperated directories to distnguish between source code and tests.


## Applications
This module stores directories with tested application.
Adding new apllication for tests :
In src create a directory named after tested aplication eg tested_app
Inside tested_app add directories describing type of tests eg tested_app_api

## Config Module 
This module conatins  configuration settings.
Each and every parameter that will be used and  in tests should be invlolved in file config.py

## Helpers module
This module contains all functions and classes used in tests but not stored in other files.
To add any helpers, involve them in helpers.py

## Tests module
This module contains all tests created for applications under test.

Adding new tests for application :
In test directory create a directory named after tested aplication eg tested_app
Inside tested_app add directories describing type of tests eg tested_app_api

