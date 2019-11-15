from bench.importers import BaseImporter


class CalendarImporter(BaseImporter):
    @property
    def table_name(self):
        return 'calendar'

    @property
    def schema(self):
        return {
            'service_id': 'INT',
            'monday': 'INT',
            'tuesday': 'INT',
            'wednesday': 'INT',
            'thursday': 'INT',
            'friday': 'INT',
            'saturday': 'INT',
            'sunday': 'INT',
            'start_date': 'STRING',
            'end_date': 'STRING'
        }
