guest_list = ['Bill Gates', 'Albert Einstein', 'Usain Bolt']

print(guest_list[0] + ", you have been invited to Dylan's Dinner!")
print(guest_list[1] + ", you have been invited to Dylan's Dinner!")
print(guest_list[2] + ", you have been invited to Dylan's Dinner!")

print("Sadly, " + guest_list.pop() + " can't make it to dinner.")
guest_list.append('XXXTentacion')

print(guest_list[0] + ", you have been invited to Dylan's Dinner!")
print(guest_list[1] + ", you have been invited to Dylan's Dinner!")
print(guest_list[2] + ", you have been invited to Dylan's Dinner!")

print("\nWow, I just found a bigger dinner table in my mansion!.")
guest_list.insert(0, "David McClish")
guest_list.insert(2, "Wendy McClish")
guest_list.append("Piper")

print(guest_list[0] + ", you have been invited to Dylan's Dinner!")
print(guest_list[1] + ", you have been invited to Dylan's Dinner!")
print(guest_list[2] + ", you have been invited to Dylan's Dinner!")
print(guest_list[3] + ", you have been invited to Dylan's Dinner!")
print(guest_list[4] + ", you have been invited to Dylan's Dinner!")
print(guest_list[5] + ", you have been invited to Dylan's Dinner!")


print("\nOops, turns out I can only invite two people for dinner.")
print("Sadly, " + guest_list.pop() + ", your are uninvited to my dinner.")
print("Sadly, " + guest_list.pop(4) + ", your are uninvited to my dinner.")
print("Sadly, " + guest_list.pop(1) + ", your are uninvited to my dinner.")
print("Sadly, " + guest_list.pop(2) + ", your are uninvited to my dinner.")

print("\nHuzzah, " + guest_list[0] + ", you are still INVITED to dinner!")
print("Huzzah, " + guest_list[1] + ", you are still INVITED to dinner!")

del guest_list[1]
del guest_list[0]
print (guest_list)
