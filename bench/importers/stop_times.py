from bench.importers import BaseImporter


class StopTimesImporter(BaseImporter):
    @property
    def table_name(self):
        return 'stop_times'

    @property
    def schema(self):
        return """
            trip_id INT NOT NULL,
            arrival_time STRING,
            departure_time STRING,
            stop_id STRING NOT NULL,
            stop_sequence INT NOT NULL,
            pickup_type INT,
            drop_off_type INT,
            stop_headsign STRING
        """
