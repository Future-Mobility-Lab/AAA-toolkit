import json
import csv
import argparse

def load_node_coordinates(csv_path):
    node_coordinates = {}
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            node_id, lat, lon = row
            node_coordinates[node_id] = [float(lat), float(lon)]
    return node_coordinates

def transform_ways(jsonl_path, node_coordinates, output_path):
    with open(jsonl_path, 'r') as infile, open(output_path, 'w') as outfile:
        for line in infile:
            way = json.loads(line)
            way['nd_refs'] = [node_coordinates.get(node_id, None) for node_id in way['nd_refs'] if node_coordinates.get(node_id, None) is not None]
            if way['nd_refs']:  # Only include ways that have at least one coordinate
                outfile.write(json.dumps(way) + '\n')

def main():
    parser = argparse.ArgumentParser(description="Transform a JSONL file of ways to include coordinates.")
    parser.add_argument('--ways_jsonl',default="ways.jsonl", type=str, help="Path to the input ways JSONL file.")
    parser.add_argument('--nodes_csv',default="nodes.csv", type=str, help="Path to the nodes CSV file.")
    parser.add_argument('--output_jsonl',default="converted_ways.csv", type=str, help="Path to the output transformed ways JSONL file.")

    args = parser.parse_args()

    node_coordinates = load_node_coordinates(args.nodes_csv)
    transform_ways(args.ways_jsonl, node_coordinates, args.output_jsonl)

if __name__ == "__main__":
    main()
