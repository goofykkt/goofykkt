major_rivers = {
    'danube':'geramany',
    'mas':'netherlands',
    'amazon':'america'
}

for river,country in major_rivers.items():
    print(f'The {river.title()} runs through {country.title()} ')

for river in major_rivers.keys():
    print(f'The river is {river.title()}')

for country in major_rivers.values():
    print(f'The country is {country.title()}')