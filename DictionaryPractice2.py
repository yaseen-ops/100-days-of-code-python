travel_log = [
    {
        "country": "England",
        "cities": ["London", "Birmingham", "Manchester"],
        "visits": 12,
        "favourite": "London"
    },
    {
        "country": "USA",
        "cities": ["California", "Texas", "SanFrancisco", "NewYork"],
        "visits": 10,
        "favourite": "Texas"
    },
]

print(travel_log)


# By below append code we can easily add a dictionary in a list.
# travel_log.append({"country": "Germany", "visits": 3, "cities": ["Berlin", "frankfurt", "hamburg"]})
# print(travel_log[2])
#                  OR               #


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    #  OR #
    # new_country = {"country": country_visited, "visits": times_visited, "cities": cities_visited}
    travel_log.append(new_country)


add_new_country("Germany", 5, ["Berlin", "frankfurt", "hamburg"])
print(travel_log)
