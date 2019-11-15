from bench.importers import BaseImporter


class TransfersImporter(BaseImporter):
    @property
    def table_name(self):
        return 'transfers'

    @property
    def schema(self):
        return {
            'from_stop_id': 'STRING',
            'to_stop_id': 'STRING',
            'transfer_type': 'INT',
            'min_transfer_time': 'STRING',
            'from_route_id': 'STRING',
            'to_route_id': 'STRING',
            'from_trip_id': 'STRING',
            'to_trip_id': 'STRING'
        }
