from bench.importers import BaseImporter


class StopTimesImporter(BaseImporter):
    @property
    def table_name(self):
        return 'stop_times'

    @property
    def schema(self):
        return {
            'trip_id': 'INT',
            'arrival_time': 'STRING',
            'departure_time': 'STRING',
            'stop_id': 'STRING',
            'stop_sequence': 'INT',
            'pickup_type': 'STRING',
            'drop_off_type': 'STRING',
            'stop_headsign': 'STRING'
        }
