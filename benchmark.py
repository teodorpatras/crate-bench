import os
from crate import client
from bench import importers, downloader

FIXTURES_URL = "https://www.vbb.de/media/download/2029"
IMPORT_MAPPING = {
    'agency.txt': importers.AgenciesImporter,
    'calendar_dates.txt': importers.CalendarDatesImporter,
    'calendar.txt': importers.CalendarImporter,
    'frequencies.txt': importers.FrequenciesImporter,
    'routes.txt': importers.RoutesImporter,
    'shapes.txt': importers.ShapesImporter,
    'stop_times.txt': importers.StopTimesImporter,
    'stops.txt': importers.StopsImporter,
    'transfers.txt': importers.TransfersImporter,
    'trips.txt': importers.TripsImporter
}


def fetch_fixtures():
    print("\n↓ Preparing benchmark! Downloading fixtures...")
    directory = os.path.join(os.getcwd(), 'fixtures')
    downloader.fetch_data(FIXTURES_URL, directory)
    print("✓ Done! Fixtures can be found under '{}'!\n".format(directory))
    return directory


def import_data(directory):
    connection = client.connect('localhost:4200')
    sec = 0
    for filename in os.listdir(directory):
        if filename in IMPORT_MAPPING:
            importer = IMPORT_MAPPING[filename](connection.cursor())
            sec += importer.import_file(os.path.join(directory, filename))
    return round(sec, 2)


if __name__ == '__main__':
    directory = fetch_fixtures()
    print("================ CRATEDB BULK INSERT BENCHMARK ======================\n")
    sec = import_data(directory)
    print("\n\n================ AWWW YES! DONE IN {} SECONDS! (⌐■_■) ===============\n".format(sec))
