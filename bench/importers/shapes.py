from bench.importers import BaseImporter


class ShapesImporter(BaseImporter):
    @property
    def table_name(self):
        return 'shapes'

    @property
    def schema(self):
        return {
            'shape_id': 'INT primary key',
            'shape_pt_lat': 'STRING',
            'shape_pt_lon': 'STRING',
            'shape_pt_sequence': 'INT'
        }
