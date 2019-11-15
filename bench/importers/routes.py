from bench.importers import BaseImporter


class RoutesImporter(BaseImporter):
    @property
    def table_name(self):
        return 'routes'

    @property
    def schema(self):
        return {
            'route_id': 'STRING primary key',
            'agency_id': 'INT',
            'route_short_name': 'STRING',
            'route_long_name': 'STRING',
            'route_type': 'INT',
            'route_color': 'STRING',
            'route_text_color': 'STRING',
            'route_desc': 'STRING'
        }
