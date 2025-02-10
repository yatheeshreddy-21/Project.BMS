res = lambda num: num*10
print(res(76))

print((lambda num: num*10)(76))
print((lambda num: print(num))(6))

res = lambda *args: sum(args)
print(res(10,20))
print(res(10,20,30,40,50,60))

res = lambda *args, **kwargs: [args, kwargs]
print(res(10,20))
print(res(10,20,30,x=40,y=50))
print(res())
