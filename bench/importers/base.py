import time
import csv


class BaseImporter:
    def __init__(self, cursor):
        self.cursor = cursor
        super().__init__()

    def import_file(self, file_path):
        self._create_table()
        print("\n ◎ Importing {} into '{}'...".format(
            file_path, self.table_name))
        start_time = time.time()
        self._import_from_file(file_path)
        diff = time.time() - start_time
        print(" ◎ {} '{}' imported in {} seconds!".format(
            self.cursor.rowcount, self.table_name, round(diff, 2)))
        # set back refresh interval
        self.cursor.execute("""
            ALTER TABLE {} SET (refresh_interval = 1000)
         """.format(self.table_name))
        return diff

    def _create_table(self):
        # https://crate.io/docs/crate/guide/en/latest/best-practices/data-import.html
        self.cursor.execute("""
            CREATE TABLE {} ({})
            CLUSTERED INTO 2 shards
            WITH (
                number_of_replicas = 0,
                refresh_interval = 0
            )
        """.format(self.table_name, self.schema))

    def _import_from_file(self, file_path):
        self.cursor.execute("""
            COPY {} FROM 'file://{}'
            WITH (
                format = 'csv'
            )
        """.format(self.table_name, file_path))

    @property
    def table_name(self):
        raise RuntimeError('Must be overridden by subclasses!')

    @property
    def schema(self):
        raise RuntimeError('Must be overridden by subclasses!')
