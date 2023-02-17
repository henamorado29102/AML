things_list = ["bike", "Canada", "pig", "bike", "dog", "carpenter", "dog", "pig"]
things_dict = {}

qwe = {"a": [1, 2], "e": [3, 4]}
qwe["a"].append(4)
qwe[2] = ["q", "r"]
print(qwe[2])

while len(things_list) > 0:
    tmp = things_list.pop()
    print(len(tmp))
    if len(tmp) in things_dict:
        things_dict[len(tmp)].append(tmp)
    else:
        things_dict[len(tmp)] = [tmp]
#    if things_dict[len(tmp)]:
#        things_dict[len(tmp)] = []
#    else:
#        things_dict[len(tmp)].append(tmp)

my_keys = sorted(list(things_dict))
for key in my_keys:
    things_list.extend(things_dict[key])
c = 0
for thing in things_list:
    if len(thing) > c:
        c = len(thing)
        things_list.insert(things_list.index(thing), c)


print(my_keys)
print(things_dict)
print(things_list)
