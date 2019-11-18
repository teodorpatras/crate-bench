from bench.importers import BaseImporter


class FrequenciesImporter(BaseImporter):
    @property
    def table_name(self):
        return 'frequencies'

    @property
    def schema(self):
        return """
            trip_id INT NOT NULL,
            start_time STRING NOT NULL,
            end_time STRING NOT NULL,
            headway_secs INT NOT NULL,
            exact_times INT
        """
