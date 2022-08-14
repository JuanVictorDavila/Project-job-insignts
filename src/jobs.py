import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')

        jobs_data = []

        for row in jobs_reader:
            jobs_data.append(row)
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    return jobs_data
