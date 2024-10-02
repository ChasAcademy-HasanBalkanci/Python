mitt_set = {1, 2, 2, 3 ,4 }
mitt_andra_set = {3, 4, 5, 6}
# x = mitt_set[2] # fungerar inte
mitt_set.add(5)
mitt_set.remove(2)
mitt_set.discard(10) # tar bort elementet om det finns
union = mitt_set.union(mitt_andra_set)
snitt = mitt_set.intersection(mitt_andra_set)
skillnad = mitt_set.difference(mitt_andra_set)

print(union)

print(snitt)

print(skillnad)