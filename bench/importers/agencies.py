from bench.importers import BaseImporter


class AgenciesImporter(BaseImporter):
    @property
    def table_name(self):
        return 'agencies'

    @property
    def schema(self):
        return """
             agency_id INT PRIMARY KEY,
             agency_name STRING NOT NULL,
             agency_url STRING NOT NULL,
             agency_timezone STRING NOT NULL,
             agency_lang STRING,
             agency_phone STRING 
        """
