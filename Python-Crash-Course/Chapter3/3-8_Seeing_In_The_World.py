places_to_visit = ['Monaco','Spa','Monza','Baku']
print (f'I will like to visit this places {places_to_visit}')

places_to_visit.sort()
print(f'It will be nice to visit them in this order {places_to_visit}')

places_to_visit.sort(reverse = True)
print(f'Or if I think better I will prefer this order {places_to_visit}')

print(f'I think this order is better {sorted(places_to_visit)}')

print(f'Or maybe I will take the reverse way {sorted(places_to_visit)}')

for i in places_to_visit:
    print(i)