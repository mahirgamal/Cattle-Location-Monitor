# Cattle Location Monitor

This project visualizes the locations of cattle on the a farm using Folium and Google Maps API. The map includes markers for the farm boundary, water locations, and individual cattle identified by RFID.

## Features

- **Farm Boundary**: Displays the boundary of the farm as a polygon.
- **Water Locations**: Marks water bodies on the farm.
- **Cattle Locations**: Shows the locations of cattle with RFID identifiers.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/mahirgamal/Cattle-Location-Monitor.git
    cd Cattle-Location-Monitor
    ```

2. Install the required Python packages:
    ```sh
    pip install folium
    ```

3. Add your Google Maps API key:
    Replace `'YOUR_GOOGLE_MAPS_API_KEY'` in the script with your actual API key.
    Obtain a Google Maps API Key: Follow the instructions on  https://developers.google.com/maps/get-started to create an API key.

## Usage

1. Ensure you have the `animal_location_data.json` file with the cattle location data.

2. Run the script:
    ```sh
    python script.py
    ```

3. Open the generated `Farm.html` file in a web browser to view the map.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments
We acknowledge that this work originates from the Trakka project and builds on the existing TerraCipher Trakka implementation. We appreciate the support and resources provided by the Trakka project team. Also, we thank Dave Swain and Will Swain from TerraCipher for their guidance and assistance throughout this project.


## License
This project is licensed under Apache License 2.0 - see the [LICENSE][lic] file for details.

## Contact
If you have any questions, suggestions or need assistance, please don't hesitate to contact us at mhabib@csu.edu.au, akabir@csu.edu.au.

[//]: #
  [lic]: <https://github.com/mahirgamal/Cattle-Location-Monitor/blob/main/LICENSE>

