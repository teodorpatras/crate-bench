from bench.importers import BaseImporter


class TripsImporter(BaseImporter):
    @property
    def table_name(self):
        return 'trips'

    @property
    def schema(self):
        return {
            'route_id': 'STRING',
            'service_id': 'INT',
            'trip_id': 'INT primary key',
            'trip_headsign': 'STRING',
            'trip_short_name': 'STRING',
            'direction_id': 'INT',
            'block_id': 'STRING',
            'shape_id': 'INT',
            'wheelchair_accessible': 'STRING',
            "bikes_allowed": 'STRING'
        }
