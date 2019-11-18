from bench.importers import BaseImporter


class CalendarImporter(BaseImporter):
    @property
    def table_name(self):
        return 'calendar'

    @property
    def schema(self):
        return """
            service_id INT NOT NULL,
            monday INT NOT NULL,
            tuesday INT NOT NULL,
            wednesday INT NOT NULL,
            thursday INT NOT NULL,
            friday INT NOT NULL,
            saturday INT NOT NULL,
            sunday INT NOT NULL,
            start_date STRING NOT NULL,
            end_date STRING NOT NULL
        """
