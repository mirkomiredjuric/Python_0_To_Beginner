programming_dictionary = {"Bug" : "An error in programming", "Function" : "A piece of code"} #key : value
print(programming_dictionary)
print(programming_dictionary.keys())
print(programming_dictionary.values())
print(programming_dictionary.items())
print(programming_dictionary["Bug"])

empty_dictionary = {} #create empty dictionary

#programming_dictionary = {} #wipe dicitionary

programming_dictionary["Bug"] = "Mire test" #replace value for key "Bug"
print(programming_dictionary)

#Nested dictionary in a dictionary
travel_log = {
    "France" : { "cities_visited" : ["Paris", "Lille", "Dijon"], "total_visit": 12},
    "Germany" : { "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visit": 18},
}

#Nested dictionary in a dictionary
travel_log = [
    {"country" : "France",  "cities_visited" : ["Paris", "Lille", "Dijon"], "total_visit": 12},
     {"country" : "Germany", "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visit": 18},
]
