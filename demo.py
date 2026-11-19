# def decorator(fun):
#     def wrapper():
#         print("1")
#         fun()
#         print("3")
#     return wrapper

# def num():
#     print("2")
    
# n = decorator(num)
# n()








# def decorator(fun):
#     def wrapper():
#         print("1")
#         fun()
#         print("3")
#     return wrapper
        
# @decorator
# def num():
#     print(2)

# num()
    
    
    
def fun():
    for i in range(1,5):
        yield i * i
   
# sq = fun()    
# for i in range(1,5):
#     print(next(sq))