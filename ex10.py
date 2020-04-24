
def decorate(func):
    def func_wrapper(arg):
        return "This function was wrapped, now it will execute: {}".format(func(arg))
    return func_wrapper

@decorate
def write_this(text):
    return "The function is printing this text: " + text


print(write_this("Actual text"))
    