
# Four examples

for i, j in enumerate("hello"):
    print(i, j)

     

a = enumerate(["a","b","c"])
print(list(a))


for i, item in [(0, 'a'), (1, 'b'), (2, 'c')]:
    print(i, item)


for i, j in enumerate('cat'):
    print(i, j)