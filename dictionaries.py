states={
'Oregan': 'OR',
"Florida": "FL",
"Ohio": "OH"
}

cities={
"OH": "Cincinnati",
"FL": "Miami"
}

cities["OR"] = "Portland"

print(cities)

print("cities in florida",cities[states["Florida"]])

for states,abrev in  states.items():
    print(states,abrev,cities[abrev])

for abrev,city in cities.items():
    print(abrev,city)

for states,abrev in states.items():
    print(states,abrev,cities[abrev])
