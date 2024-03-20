import folium
import json

# Your Google Maps API key - replace 'YOUR_GOOGLE_MAPS_API_KEY' with your actual API key
google_maps_api_key = 'xyz'


# Read the data back from the file
with open('animal_location_data.json', 'r') as file:
    animal_locations = json.load(file)

# Coordinates for the CSU Farm boundary as provided
csu_farm_boundary = [
    [-35.0542578, 147.3477852],
    [-35.0539329, 147.3447382],
    [-35.0556279, 147.3444271],
    [-35.0558387, 147.3454893],
    [-35.0563744, 147.3454142],
    [-35.0567082, 147.3471308],
    [-35.0542666, 147.3477852]  # Closing the loop to make it a polygon
]

water_locations = [
    [-35.054528, 147.345998],
    [-35.056283, 147.346098]
]

# Create a map centered at the approximate center of the boundary with Google Satellite tiles
map_csu_farm = folium.Map(location=[-35.055, 147.346], zoom_start=18, 
                          tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}&key=' + google_maps_api_key,
                          attr='Google')

# Add a marker for the center of the CSU Farm
folium.Marker(location=[-35.054315, 147.347599], icon=folium.Icon(color='red'),popup='CSU Farm Wagga Wagga').add_to(map_csu_farm)


# Add blue markers for water bodies without popups
for loc in water_locations:
    folium.Marker(
        location=loc, 
        icon=folium.Icon(color='blue'),
        popup='water'
    ).add_to(map_csu_farm)




# Add the boundary as a polygon to the map
folium.Polygon(
    locations=csu_farm_boundary,
    color='blue',
    weight=3,
    fill=False,
    fill_color='cyan',
    fill_opacity=0.3
).add_to(map_csu_farm)

# Integrate animal locations into the map
for animal in animal_locations:
    coords = animal['message']['GeoLocation']['coordinates']
    folium.Marker(
        location=[coords[1], coords[0]],  # Lat, Long
        icon=folium.Icon(color='green'),
        popup=f"RFID: {animal['message']['item']['animal']['identifier']['id']}"
    ).add_to(map_csu_farm)


# Save the map to an HTML file (optional)
map_csu_farm.save('CSU_Farm_Wagga_Wagga.html')

# The file 'CSU_Farm_Wagga_Wagga.html' can be opened in any web browser.
