from bench.importers import BaseImporter


class FrequenciesImporter(BaseImporter):
    @property
    def table_name(self):
        return 'frequencies'

    @property
    def schema(self):
        return {
            'trip_id': 'INT',
            'start_time': 'STRING',
            'end_time': 'STRING',
            'headway_secs': 'INT',
            'exact_times': 'STRING'
        }
