#! python3

# Iterates over set of traffic lights 
main_6th = {"ns": "green", "ew" : "red"}
market_2nd = {"ns": "red", "ew" : "green"}


def switchlights(street):
    mainSpotlight = street["ns"]
    dependentSpotlight = street["ew"]
    iterateMainLight = ["green", "yellow", "red", "red"]
    iterateDependendentLight = ["red", "red", "green", "yellow"]
    number = 1
    while number < 5:
        assert "red" in street.values(), "No red lights!"
        for i in range(0,4):
            mainSpotlight = iterateMainLight[i]
            dependentSpotlight = iterateDependendentLight[i]
            print(mainSpotlight)
            print(dependentSpotlight)
            print("---")
        number +=1

switchlights(market_2nd)

