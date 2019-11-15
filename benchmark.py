import os
import time
from bench import downloader

DATA_URL = "https://www.vbb.de/media/download/2029"


def main():
    print("\n ↓ Downloading import data...")
    # fetch & unarchive assets
    directory = os.path.join(os.getcwd(), 'data')
    downloader.fetch_data(DATA_URL, directory)
    print(" ✓ Done! Import data can be found under '{}'...\n".format(directory))


if __name__ == '__main__':
    print("\n================ CRATEDB BATCH INSERT BENCHMARK ======================\n")
    start = time.time()
    main()
    diff = round(time.time() - start, 2)
    print("\n\n================ AWWW YES! DONE IN {} SECONDS! (⌐■_■) ===============\n".format(diff))
