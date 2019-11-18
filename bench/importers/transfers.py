from bench.importers import BaseImporter


class TransfersImporter(BaseImporter):
    @property
    def table_name(self):
        return 'transfers'

    @property
    def schema(self):
        return """
            from_stop_id STRING NOT NULL,
            to_stop_id STRING NOT NULL,
            transfer_type INT,
            min_transfer_time INT,
            from_route_id STRING,
            to_route_id STRING,
            from_trip_id INT,
            to_trip_id INT
        """
