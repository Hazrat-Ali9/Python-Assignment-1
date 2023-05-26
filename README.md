# List: 

* List is one type of built-in data structure in python that is used to store an ordered collection of items in a single variable.
* Write comma-separated values inside a square bracket ([ ]) to create a list in python.
* List is ordered (There is indexing)
* In a list, items can be accessed and manipulated using their index value.
* Dictionaries are faster when searching for items based on their keys


# Dictionaries : 

* A dictionary is a built-in data structure in python that is used to store an unordered collection of items in the form of a key: value pair.
* To create a dictionary in python write comma-separated data in form of a key: value pair inside the curly bracket ({ }).
* Dictionary is unordered (There is no indexing).
* In a dictionary, items can only be accessed using their keys.
* Lists are faster when accessing items based on their index.

# *args
*args is used to send a non-keyworded variable length argument list to the function. Here’s an example to help you get a clear idea:

args is a short form of arguments. With the use of args python takes any number of arguments in user-defined function and converts user inputs to a tuple named args. In other words, args means zero or more arguments which are stored in a tuple named args.
def myCode(*argv): 
    for arg in argv: 
        print (arg)
        
myCode('Hello', 'Welcome', 'to','the', 'New World') 


Hello
Welcome
to
the
New World


# **kwargs ??
kwargs allows you to pass keyworded variable length of arguments to a function. You should use kwargs if you want to handle named arguments in a function.
**kwargs
The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).
A keyword argument is where you provide a name to the variable as you pass it into the function.
One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it.
That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.
def Greet_You(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))
              
Greet_You(Hello = "Hello",Name="Friend",How="How",Are="Are",You="You?")

Hello = Hello
Name = Friend
How = How
Are = Are
You = You?