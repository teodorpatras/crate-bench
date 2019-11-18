from bench.importers import BaseImporter


class ShapesImporter(BaseImporter):
    @property
    def table_name(self):
        return 'shapes'

    @property
    def schema(self):
        return """
            shape_id INT NOT NULL,
            shape_pt_lat STRING NOT NULL,
            shape_pt_lon STRING NOT NULL,
            shape_pt_sequence INT NOT NULL
        """
