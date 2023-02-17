# 3-4 Guest-list

guest_list = ["Ailen", "Yusel", "Herniel"]

for guest in guest_list:
    print(guest + ", you are invited to dinner at my house on Saturday.")

# 3-5 Changing Guest List

print(guest_list[2] + " can't make it to dinner")

guest_list[2] = "Casper"

for guest in guest_list:
    print(guest + ", you are invited to dinner at my house on Saturday.")

# 3-6 More Guest

print("Hey mates, I found a bigger table!!")

guest_list.insert(0, "Carlos")
guest_list.insert(0, "Juan")
guest_list.append("Superman")

for guest in guest_list:
    print(guest + ", you are invited to dinner at my house on Saturday.")

# 3-7 Shrinking Guest List

print("I can only invite 2 people to dinner")

print(guest_list.pop(0) + ", I'm sorry, but I can't buy you dinner.")
print(guest_list.pop(0) + ", I'm sorry, but I can't buy you dinner.")
print(guest_list.pop(0) + ", I'm sorry, but I can't buy you dinner.")
print(guest_list.pop(0) + ", I'm sorry, but I can't buy you dinner.")

for guest in guest_list:
    print(guest + ", you're still invited to dinner.")

# 3-8 Seeing the world
place_list = ["Hawaii", "Cancun", "Sahara Desert", "Himalaya", "Alaska"]

print(place_list)
print(sorted(place_list))
print(place_list)
place_list.reverse()
print(place_list)
place_list.reverse()
print(place_list)
place_list.sort()
print(place_list)
place_list.sort(reverse=True)
print(place_list)

# 3-9 Dinner Guests

print("I have invited %s people to my dinner" % len(guest_list))

# 3 -10 Every function

things_list = ["bike", "lake", "Canada", "pig", "bike", "dog", "carpenter", "lake", "dog", "pig", "carpenter", "dog"]

print(things_list)
# iterate list
for thing in things_list:
    # remove duplicates
    while things_list.count(thing) > 1:
        things_list.remove(thing)
    # if the index is even I apply reverse otherwise I apply sort
    if thing.index(thing) % 2 == 0:
        things_list.reverse()
    else:
        things_list.sort()

things_dict = {}
# Group words by size in a dictionary
while len(things_list) > 0:
    tmp = things_list.pop()
    if len(tmp) in things_dict:
        things_dict[len(tmp)].append(tmp)
    else:
        things_dict[len(tmp)] = [tmp]

print(things_dict)
# Group words by size in a dictionary
my_keys = sorted(list(things_dict))
for key in my_keys:
    things_list.extend(things_dict[key])

print(things_list)
c = 0
# I order the words by size and at the beginning of each group of words I insert the size
for thing in things_list:
    if len(thing) > c:
        c = len(thing)
        things_list.insert(things_list.index(thing), c)

print(things_list)
things_list.clear()
print(things_list)


# Dictionary practice

course_list = {"2023W_ITP_1233_1": "Linchen Wang", "2023W_AML_1204_1": "Aamir", "CBD_2303_1": "Linchen Wang",
               "2023W_CBD_1001_1": "Linchen Wang", "2023W_CBD_2223_1": "Karan", "2023W_CBD 1143_1": "Mike",
               "2023W_ITP 1134_1": "Albert Danison"}
print(course_list)
course_list["2023W_CBD 1143_1"] = "John Wick"
print(course_list)




