from bench.importers import BaseImporter


class AgenciesImporter(BaseImporter):
    @property
    def table_name(self):
        return 'agencies'

    @property
    def schema(self):
        return """
             agency_id INT primary key,
             agency_name STRING,
             agency_url STRING,
             agency_timezone STRING,
             agency_lang STRING,
             agency_phone STRING 
        """
