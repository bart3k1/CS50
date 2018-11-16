flights = [('Poznań', 'Timbuktu', 1415), ('Warszawa', 'Timbuktu', 1425), ('Warszawa', 'Nowy Jork', 1825)]

for flight in flights:
    print("{} to {}, {} minutes.".format(flight[0], flight[1], flight[2]))