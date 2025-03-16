# python
# osm/__init__.py
from typing import List, Dict

from .fetch import Fetcher
from .process import Processor

class OSM:
    def __init__(self):
        self._fetcher = Fetcher()
        self._processor = Processor()

    def fetch(self, missing_areas: List[Dict]):
        return self._fetcher(missing_areas)

    def process(self, g):
        return self._processor(g)

osm = OSM()