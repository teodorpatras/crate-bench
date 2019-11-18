from bench.importers import BaseImporter


class TripsImporter(BaseImporter):
    @property
    def table_name(self):
        return 'trips'

    @property
    def schema(self):
        return """
            trip_id INT PRIMARY KEY,
            route_id STRING NOT NULL,
            service_id INT NOT NULL,
            trip_headsign STRING,
            trip_short_name STRING,
            direction_id INT,
            block_id STRING,
            shape_id INT,
            wheelchair_accessible INT,
            bikes_allowed INT
        """
