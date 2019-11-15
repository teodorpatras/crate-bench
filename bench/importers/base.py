import time
import csv

BATCH_SIZE = 10000


class BaseImporter:
    def __init__(self, cursor):
        self.cursor = cursor
        super().__init__()

    def import_file(self, file_path):
        start_time = time.time()
        print("\n ◎ Importing {} into '{}'...".format(
            file_path, self.table_name))
        self._create_table()
        count = self._import_from_file(file_path)
        diff = time.time() - start_time
        print(" ◎ {} '{}' imported in {} seconds!".format(
            count, self.table_name, round(diff, 2)))
        return diff

    def _create_table(self):
        schema_str = ', '.join(
            map(lambda item: ' '.join(item), self.schema.items()))

        return self.cursor.execute('CREATE TABLE IF NOT EXISTS {} ({})'.format(self.table_name, schema_str))

    def _import_from_file(self, file_path):
        count = 0
        with open(file_path) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            # skip header
            next(reader)
            rows = []
            for row in reader:
                count += 1
                rows.append(row)
                # if we reached batch size, do a batch insert
                if len(rows) == BATCH_SIZE:
                    self.cursor.executemany(self.insert_query, rows)
                    rows = []
            # if there are still some rows left, insert them
            if len(rows) > 0:
                self.cursor.executemany(self.insert_query, rows)
            return count

    @property
    def insert_query(self):
        return """INSERT INTO {} ({}) VALUES ({})""".format(
            self.table_name,
            ', '.join(self.schema.keys()),
            ', '.join('?' * len(self.schema))
        )

    @property
    def has_primary(self):
        filtered = filter(lambda v: 'primary key' in v, self.schema.values())
        return len(list(filtered)) > 0

    @property
    def table_name(self):
        raise RuntimeError('Must be overridden by subclasses!')

    @property
    def schema(self):
        raise RuntimeError('Must be overridden by subclasses!')
