Accident Analysis & Association (AAA) toolkit (publish on github).
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
