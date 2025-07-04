from mapconfig import GeoMap

m = GeoMap()

m.add_marker("New Delhi", popup="Capital City")
m.add_marker("Mumbai")
m.add_circle("Hyderabad", radius=10000, color="green", popup="Cyber City")
# m.add_path("New Delhi", "Mumbai", color="blue", weight=3, popup="Path from Delhi to Mumbai")
# m.add_path("chennai", "Mumbai", color="blue", weight=3, popup="Path from Delhi to Mumbai")


icon_url = "https://cdn-icons-png.flaticon.com/512/684/684908.png"
m.add_custom_icon_marker("Chennai", icon_url=icon_url, popup="Marina Beach City")
# distance = m.get_distance("New Delhi", "Mumbai")
m.add_shortest_path("Kharar", "Jammu", color="blue", weight=3, popup="Path from Kharar to Jammu")
# print(f"The driving distance between New Delhi and Mumbai is {distance:.1f} km")

m.show()
