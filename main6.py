# def <FUNCTION_NAME>(INPUTS[Optionals])
# ... body
# return <RESULT>[OPTIONAL]

# f(x) = x^2

def my_function(x, y=5):
    print("x: ", x)
    print("y: ", y)


my_function(1)

my_function(1, 10)


def my_function2(x, y):
    print("x: ", x)
    print("y: ", y)


my_function2(x=1, y=[1, 2, 3])
my_function2(x="Jhon", y={"key 1": 2, "key 3": 2})
