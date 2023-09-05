import requests
import bz2
import osmium
import os
from tqdm import tqdm
import argparse

# Run using:
# pip install requests osmium tqdm
# python code_A_download.py --url https://download.geofabrik.de/north-america/us/california/norcal-latest.osm.bz2 --lat_min 37.6 --lat_max 37.9 --lon_min -123.1 --lon_max -122.3
# 

def download_and_extract(url, lat_min, lat_max, lon_min, lon_max):
    # Download the bz2 file
    response = requests.get(url, stream=True)
    
    # Get the total file size
    file_size = int(response.headers.get("content-length", 0))

    # Initialize the progress bar
    progress_bar = tqdm(total=file_size, unit="iB", unit_scale=True)

    # Save the downloaded file
    bz2_filename = url.split('/')[-1]
    with open(bz2_filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            progress_bar.update(len(chunk))
            f.write(chunk)

    progress_bar.close()

    # Unpack the bz2 file to get the osm file
    osm_filename = bz2_filename.replace('.bz2', '')
    with open(osm_filename, "wb") as new_file, bz2.BZ2File(bz2_filename, "rb") as file:
        for data in iter(lambda : file.read(100 * 1024), b''):
            new_file.write(data)

    # Custom osmium handler to extract area based on coordinates
    class ExtractArea(osmium.SimpleHandler):
        def __init__(self, writer):
            super(ExtractArea, self).__init__()
            self.writer = writer

        def node(self, n):
            if lat_min < n.location.lat < lat_max and lon_min < n.location.lon < lon_max:
                self.writer.add_node(n)
            
        def way(self, w):
            self.writer.add_way(w)

        def relation(self, r):
            self.writer.add_relation(r)

    # Create an osmium writer for the new osm file
    output_filename = f"extracted_area_{lat_min}_{lat_max}_{lon_min}_{lon_max}.osm"
    with osmium.io.Writer(output_filename, header=osmium.osm.mutable.Header()) as writer:
        handler = ExtractArea(writer)
        handler.apply_file(osm_filename)

    print(f"Extraction complete. The extracted area is saved in '{output_filename}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download and extract a specific area from an OSM file.")
    parser.add_argument('--url', type=str, default="https://download.geofabrik.de/north-america/us/california/norcal-latest.osm.bz2", help='URL to download the osm.bz2 file')
    parser.add_argument('--lat_min', type=float, default=37.6, help='Minimum latitude for the bounding box')
    parser.add_argument('--lat_max', type=float, default=37.9, help='Maximum latitude for the bounding box')
    parser.add_argument('--lon_min', type=float, default=-123.1, help='Minimum longitude for the bounding box')
    parser.add_argument('--lon_max', type=float, default=-122.3, help='Maximum longitude for the bounding box')

    args = parser.parse_args()
    download_and_extract(args.url, args.lat_min, args.lat_max, args.lon_min, args.lon_max)


