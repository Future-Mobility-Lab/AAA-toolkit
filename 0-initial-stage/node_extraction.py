import re
import csv
import argparse

def process_batch(batch, min_lat, max_lat, min_lon, max_lon):
    node_data = []
    pattern = r'<node id="(\d+)"[^>]*lat="(-?\d+\.\d+)" lon="(-?\d+\.\d+)"\s*(?:/>|>.*?</node>)'
    matches = re.findall(pattern, batch, re.DOTALL)
    for match in matches:
        node_id, lat, lon = match
        lat, lon = float(lat), float(lon)
        if min_lat <= lat <= max_lat and min_lon <= lon <= max_lon:
            node_data.append([node_id, lat, lon])
    return node_data

def write_to_csv(data, filename):
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(data)

def main(args):
    batch_size = args.batch_size
    min_lat, max_lat = args.min_lat, args.max_lat
    min_lon, max_lon = args.min_lon, args.max_lon
    csv_file = args.output_csv

    # Initialize the CSV file with headers
    with open(csv_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Node ID", "Latitude", "Longitude"])

    batch = ""
    line_count = 0

    with open(args.input_osm, "r", encoding="utf-8") as osmfile:
        for line in osmfile:
            batch += line
            line_count += 1
            if line_count >= batch_size:
                node_data = process_batch(batch, min_lat, max_lat, min_lon, max_lon)
                write_to_csv(node_data, csv_file)
                batch = ""
                line_count = 0

        # Process the last batch if it's not empty
        if batch:
            node_data = process_batch(batch, min_lat, max_lat, min_lon, max_lon)
            write_to_csv(node_data, csv_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process OSM files and extract node data.')
    parser.add_argument('--input_osm', type=str, default="map.osm", help='Path to the input OSM file.')
    parser.add_argument('--output_csv', type=str, default="nodes.csv", help='Path to the output CSV file.')
    parser.add_argument('--batch_size', type=int, default=10000, help='Number of lines to process in each batch.')
    parser.add_argument('--min_lat', type=float, default=float('-inf'), help='Minimum latitude for filtering.')
    parser.add_argument('--max_lat', type=float, default=float('inf'), help='Maximum latitude for filtering.')
    parser.add_argument('--min_lon', type=float, default=float('-inf'), help='Minimum longitude for filtering.')
    parser.add_argument('--max_lon', type=float, default=float('inf'), help='Maximum longitude for filtering.')
    
    args = parser.parse_args()
    main(args)

# run: python your_script.py input.osm output.csv --batch_size 10000 --min_lat 10 --max_lat 50 --min_lon -10 --max_lon 30
