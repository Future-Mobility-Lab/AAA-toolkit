Accident Analysis & Association (AAA) toolkit.

**(update is pending, more organized structure with descriptions is being added, association between code parts and ipynb files is being processed)**

The Accident Analysis & Association (AAA) toolkit is a comprehensive program designed for data-driven accident analysis and mapping. The toolkit leverages a range of geospatial and traffic data sources to create a multi-dimensional view of traffic incidents in a particular region.

The traffic speed readings are available by the link (CSV - traffic speed readings on the day of disruption, PMW - traffic speed readings during the first week before the day of disruption, PMW2 - traffic speed readings the during a week, two weeks before the day of disruption)
https://drive.google.com/file/d/1tKqefd8TgX_fVh-COoQk0ZN-YSSJ3gH6/view?usp=sharing

Code parts:
1.	Download OSM data for specific coordinates / or extract from Geofabrik.
2.	Download CTADS and extract the incidents in the area.
3.	Filter CTADS and OSM by area: CTADS-area, OSM-area
4.	Convert OSM to points
5.	Get VDS points from PEMS.
6.	Apply road alignment: VDS2ROAD, CTADS2ROAD.
7.	Apply algorithm: CTADS2VDS. Associate VDS points to accident points.
8.	CTADS2TS: Download traffic speed on the day of incident and two weeks before.
9.	Produce the final pickle file for traffic speeds/traffic flows.


The code implements multiple steps and code parts:

    Download OSM data for specific region from Geofabrik.: This code is responsible for obtaining OpenStreetMap (OSM) data from Geofabrik, a provider of free and up-to-date geodata derived from OSM.

    Download CTADS and extract the incidents in the area.: The next part of the code fetches data from the Countrywise Traffic Accident Data Set (CTADS). This data includes details about traffic incidents that have occurred in the specified region.

    Filter CTADS and OSM by area: CTADS-area, OSM-area.: This step filters both the OSM and CTADS data by area, ensuring that only relevant geographic and incident data are retained for analysis.

    Convert OSM to points.: The code then extracts and converts the OSM road data into point data. This conversion is necessary for subsequent application of the proposed association algorithm.

    Get VDS points from PEMS.: The toolkit then retrieves Vehicle Detector Station (VDS) points from the PeMS (Performance Measurement System), which collects real-time traffic data from highways.

    Apply road alignment: VDS2ROAD, CTADS2ROAD.: The next step is the alignment of road data. This involves mapping the VDS and CTADS data to the corresponding road point data. This allows us to associate traffic detectors and accidents with specific roads.

    Apply algorithm: CTADS2VDS. Associate VDS points to accident points.: The CTADS2VDS algorithm is then applied, which associates VDS points (traffic data points) with accident points from the CTADS. This association makes it possible to link traffic conditions with accident locations.

    CTADS2TS: Download traffic speed on the day of incident and two weeks before.: The code subsequently fetches traffic speed data for the day of each incident and the two weeks prior (the time interval can be modified) to each incident. This information provides valuable context, as it allows for the examination of any changes in traffic conditions leading up to an incident.

    Produce the final pickle file for traffic speeds/traffic flows associated with specific accidents: The final part of the code generates a Python pickle file, which is a binary file format used for serializing and de-serializing a Python object structure. This file contains the finalized data regarding traffic speeds and flows.
