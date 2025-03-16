import logging


class Processor:
    def __call__(self, g):
        """
        Converts raw OSMnx graph data into structured nodes and edges for MongoDB storage.
        """
        nodes, edges = [], []

        logging.info("Processing nodes...")
        for node_id, data in g.nodes(data=True):
            node = {
                "_id": node_id,
                "location": {
                    "type": "Point",
                    "coordinates": [data["x"], data["y"]]
                },
                "street_count": data.get("street_count", 0)
            }
            nodes.append(node)
        logging.info("Processed %d nodes.", len(nodes))

        logging.info("Processing edges...")
        for u, v, data in g.edges(data=True):
            maxspeed = data.get("maxspeed", "30")
            edges.append({
                "_id": f"{u}-{v}",
                "from": u,
                "to": v,
                "length": data.get("length", 0),
                "highway": data.get("highway", "unknown"),
                "maxspeed": int(maxspeed) if str(maxspeed).isdigit() else 30,
                "oneway": data.get("oneway", False)
            })
        logging.info("Processed %d edges.", len(edges))

        return nodes, edges
