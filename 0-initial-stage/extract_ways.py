import re
import json
import argparse
from tqdm import tqdm

def process_batch(batch_data, output_file):
    ways_dict = {}
    way_pattern = r'<way id="(\d+)"[^>]*>(.*?)<\/way>'
    nd_ref_pattern = r'<nd ref="(\d+)"\s*/>'
    highway_pattern = r'<tag k="highway" v="([^"]+)"\s*/>'

    for way_match in re.findall(way_pattern, batch_data, re.DOTALL):
        way_id, way_content = way_match

        highway_match = re.search(highway_pattern, way_content)
        if not highway_match:
            continue

        ways_dict[way_id] = {'id': str(way_id), 'nd_refs': [], 'highway': highway_match.group(1)}

        for nd_ref_match in re.findall(nd_ref_pattern, way_content):
            ways_dict[way_id]['nd_refs'].append(nd_ref_match)

    with open(output_file, 'a') as f:
        for way_data in ways_dict.values():
            f.write(json.dumps(way_data) + '\n')

def main(args):
    batch_size = args.batch_size
    output_file = args.output_file
    input_file = args.input_file
    batch_data = ''

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in tqdm(f):
            batch_data += line
            if len(batch_data.splitlines()) >= batch_size:
                process_batch(batch_data, output_file)
                batch_data = ''

    if batch_data:
        process_batch(batch_data, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process OSM files and extract "way" elements with "highway" keys.')
    parser.add_argument('--input_file', default="map.osm", type=str, help='Path to the input OSM file.')
    parser.add_argument('--output_file', default="ways.jsonl", type=str, help='Path to the output JSONL file.')
    parser.add_argument('--batch_size', type=int, default=2000, help='Number of lines to process in each batch.')
    
    args = parser.parse_args()
    main(args)

# ~ python your_script.py --input_file map.osm output_file output.jsonl --batch_size 1000
