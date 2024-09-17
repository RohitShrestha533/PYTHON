def announce(f): #takes hello function
    def wrapper():
        print("about to run function")
        f(); # call that hello function
        print("done with function")
    return wrapper
    
@announce  #decorator
def hello():
    print("hello world !")

hello()            


