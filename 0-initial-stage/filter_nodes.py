import csv
import argparse

def filter_csv(input_csv, output_csv, lat_min, lat_max, lon_min, lon_max):
    with open(input_csv, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
        csvreader = csv.reader(infile)
        csvwriter = csv.writer(outfile)
        
        header = next(csvreader)
        csvwriter.writerow(header)
        
        for row in csvreader:
            node_id, lat, lon = row
            lat, lon = float(lat), float(lon)
            
            if lat_min <= lat <= lat_max and lon_min <= lon <= lon_max:
                csvwriter.writerow(row)

def main(args):
    filter_csv(
        args.input_csv,
        args.output_csv,
        args.lat_min,
        args.lat_max,
        args.lon_min,
        args.lon_max
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter a CSV file of geographic nodes by bounding box.")
    
    parser.add_argument('--input_csv', default='nodes.csv', type=str, help="Path to the input CSV file.")
    parser.add_argument('--output_csv', default='filtered_nodes.csv', type=str, help="Path to the output CSV file.")
    
    parser.add_argument('--lat_min', type=float, default=37.6, help="Minimum latitude.")
    parser.add_argument('--lat_max', type=float, default=37.9, help="Maximum latitude.")
    parser.add_argument('--lon_min', type=float, default=-123.1, help="Minimum longitude.")
    parser.add_argument('--lon_max', type=float, default=-122.3, help="Maximum longitude.")
    
    args = parser.parse_args()
    main(args)
