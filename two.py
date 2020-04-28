'''
This is a simple program to learn
if __name__ = "__main__"
'''
from one.py import func1
#this is two.py
def func2():
    #fucntion for printing inside two.py
    print("This is a function inside two.py")


print("Hello, I am from two.py")

if __name__ == '__main__':
        '''
        This code will run if this script is called directly
        '''
        #accessing this function from two.py
        func1()
        func2()
        
