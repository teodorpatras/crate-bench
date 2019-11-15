from bench.importers import BaseImporter


class StopsImporter(BaseImporter):
    @property
    def table_name(self):
        return 'stops'

    @property
    def schema(self):
        return """
            stop_id STRING primary key,
            stop_code STRING,
            stop_name STRING,
            stop_desc STRING,
            stop_lat STRING,
            stop_lon STRING,
            location_type INT,
            parent_station STRING,
            wheelchair_boarding STRING,
            platform_code STRING,
            zone_id STRING
        """
