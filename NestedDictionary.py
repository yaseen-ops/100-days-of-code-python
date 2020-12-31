# travel_log = {
#     "cities_visited": {
#         "England": ["London", "Birmingham", "Manchester"],
#         "USA": ["California", "Texas", "SanFrancisco", "NewYork"],
#         "Germany": ["Berlin", "Frankfurt", "Hamburg"]
#     }
# }

# print(travel_log["cities_visited"]["England"][1])

travel_log = {
    "England": {
        "cities_visited": ["London", "Birmingham", "Manchester"],
        "total_visits": 12,
        "Favourite_place": "London"
    },
    "USA": {
        "cities_visited": ["California", "Texas", "SanFrancisco", "NewYork"],
        "total_visits": 10,
        "Favourite_place": "Texas"
    },
    "Germany": {"cities_visited": ["Berlin", "Frankfurt", "Hamburg"], "total_visits": 8, "Favourite_place": "Berlin"}
}

print(travel_log["England"]["Favourite_place"])
print(travel_log["Germany"]["Favourite_place"])
