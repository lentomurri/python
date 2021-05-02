def liters_100km_to_miles_gallon(liters):
    return (100 / 1.609344) / ((liters / 3.785411784))


def miles_gallon_to_liters_100km(miles):
    #convert miles gallon to a liter #
    return 100 / (miles * 1.609344) * 3.785411784
