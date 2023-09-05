import osmium
import argparse

class RoadFilter(osmium.SimpleHandler):
    def __init__(self, writer):
        super(RoadFilter, self).__init__()
        self.writer = writer

    def way(self, w):
        try:
            road_type = w.tags['highway']
            if road_type in ['primary', 'secondary', 'tertiary', 'motorway']:
                self.writer.add_way(w)
        except KeyError:
            pass

    def node(self, n):
        self.writer.add_node(n)

    def relation(self, r):
        self.writer.add_relation(r)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract specific road types from an OSM file.")
    parser.add_argument('input_file', type=str, help="Path to the input OSM file")
    parser.add_argument('output_file', type=str, help="Path to the output OSM file")

    args = parser.parse_args()

    with osmium.io.Writer(args.output_file, header=osmium.osm.mutable.Header()) as writer:
        handler = RoadFilter(writer)
        handler.apply_file(args.input_file, locations=True)

    print(f"Extraction complete. The filtered roads are saved in '{args.output_file}'.")
# Run: python extract_roads.py input.osm output.osm
