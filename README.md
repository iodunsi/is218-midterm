# IS 218 Midterm

Design Patterns:


- [Command Design Pattern](https://github.com/iodunsi/is218-midterm/blob/master/app/commands/__init__.py) - This design pattern is implemented within the app/commands/__init__.py file through the use of CommandHandler, AddCommand, SubtractCommand, DivideCommand and MenuCommand classes, respectively. This design pattern is used to escapsulate a request as an object, permitting parameterization, as included in the instructions on the previous homework assignments. 

The remaining examples of implementations of this design pattern are found within these files: 
[app/plugins/add/__init__.py](https://github.com/iodunsi/is218-midterm/blob/master/app/plugins/add/__init__.py),  [app/plugins/subtract/__init__.py](https://github.com/iodunsi/is218-midterm/blob/master/app/plugins/subtract/__init__.py)  
[app/plugins/multiply/__init__.py](https://github.com/iodunsi/is218-midterm/blob/master/app/plugins/multiply/__init__.py)
 [app/plugins/divide/__init__.py](https://github.com/iodunsi/is218-midterm/blob/master/app/plugins/divide/__init__.py)   
 [app/plugins/menu/__init__.py](https://github.com/iodunsi/is218-midterm/blob/master/app/plugins/menu/__init__.py)


- [Facade Design Pattern](https://github.com/iodunsi/is218-midterm/blob/master/app/__init__.py) - This design pattern is implented within the app/__init__.py file with the purpose of effective command registration and execution.


[Environment Variables](https://github.com/iodunsi/is218-midterm/blob/master/app/__init__.py):

 Environment variables are used to avoid hardcoding static values within the code. They are typically used for development and testing purposes. Within this project, environment variables are loaded via the dotenv module, and defaults are set if not explicitly configured. This is referenced in the "App" class which can be found in app/__init__.py. (linked above)

LBYL (Look Before You Leap) - This approach is meant to carefully check conditions before throwing an exception. This is implemented within the [app/__init__.py file](https://github.com/iodunsi/is218-midterm/blob/master/app/__init__.py) where the user is prompted to press Enter without typing anything to exit the program.


EAFP (Easier to Ask for Forgiveness than Permission) - This approach is meant to actually execute the command along with exceptions. This is implemented within the [app/__init__.py file](https://github.com/iodunsi/is218-midterm/blob/master/app/__init__.py) within the start method.
 


 Logging

 Logging is used to easily document errors for debug purposes. Configuration for logging is located within the [app/__init__.py file](https://github.com/iodunsi/is218-midterm/blob/master/app/__init__.py) through using Python's dictionary, which utilizes "key:value" pairs.