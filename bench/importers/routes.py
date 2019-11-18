from bench.importers import BaseImporter


class RoutesImporter(BaseImporter):
    @property
    def table_name(self):
        return 'routes'

    @property
    def schema(self):
        return """
            route_id STRING PRIMARY KEY,
            agency_id INT,
            route_short_name STRING,
            route_long_name STRING,
            route_type INT NOT NULL,
            route_color STRING,
            route_text_color STRING,
            route_desc STRING
        """
