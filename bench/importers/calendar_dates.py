from bench.importers import BaseImporter


class CalendarDatesImporter(BaseImporter):
    @property
    def table_name(self):
        return 'calendar_dates'

    @property
    def schema(self):
        return """
            service_id INT NOT NULL,
            date STRING NOT NULL,
            exception_type INT NOT NULL
        """
