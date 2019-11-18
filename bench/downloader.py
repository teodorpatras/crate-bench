import os
import urllib.request
import zipfile


def fetch_data(data_url, data_directory):
    # empty or create the data directory
    if os.path.exists(data_directory):
        for f in os.listdir(data_directory):
            os.remove(os.path.join(data_directory, f))
    else:
        os.makedirs(data_directory)
    # download zip file
    file_path = os.path.join(data_directory, 'data.zip')
    urllib.request.urlretrieve(data_url, file_path)
    # unarchive it
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(data_directory)
    # remove zip file
    os.remove(file_path)
