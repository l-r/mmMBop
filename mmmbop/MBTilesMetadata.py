import sqlite3
import json


class MBTilesMetadata:
    def __init__(self, sources):
        self.sources = sources

    @staticmethod
    def _parse_json(data):
        values = {}
        for item in data:
            name, value = item
            if name == "name":
                values['name'] = value
            if name == "json":
                data = json.loads(value)
                values['layer_id'] = [v for f in data['vector_layers'] for k, v in f.items() if k == "id"]  # yolo
                if values['layer_id']:
                    values['layer_id'] = values['layer_id'][0]
        return values

    def get_metadata(self):
        # TODO write py-node-mbtiles one day to avoid this quagmire
        all_metadata = []
        for index, _ in enumerate(self.sources):
            conn = sqlite3.connect(self.sources[index])
            c = conn.cursor()
            c.execute('''select * from metadata''')
            result = c.fetchall()

            values = self._parse_json(result)
            all_metadata.append(values)

        return all_metadata
