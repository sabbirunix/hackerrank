def mixed_func(*args, **kwargs):
    print(type(args))
    print('args are: ' +str(args))
    print(type(kwargs))
    print('kwargs are: ' +str(kwargs))


# mixed_func(input())
print('********** take1 ************')
mixed_func('Python', 'The', 'Best', language='Python', users='A lot')
print('********** take2 ************')
mixed_func('My', 'final score', bd=10, en=10, math=10)
