This program is an example of implementation of singleton design pattern

This design pattern assures that there is only one instance of a class

This is simple and primitive login manager, it contains session class which is a singleton. If you pass right passes, session class will be instantiated, but if you try to log in again on the same passes, second instance of the session class will not be instantiated because it's a singleton. Logout button removes session instance and the singleton can be instantiated again. Clear button clears all entries and quit button closes the program.

Login: foo
Password: bar