#!/usr/bin/env python3

"""This module demonstrates an ETL (Extract, Transform, Load) flow:

- Extract: Download daily NYC weather for the year 2018
- Transform: Convert the temperature to fahrenheit
- Load: Store in a local sqlite3 database
"""
from collections import namedtuple
from contextlib import closing
from datetime import datetime
from typing import List
import pickle
import sqlite3

from pandas.core.frame import DataFrame
from meteostat import Point, Daily
from prefect import task, Flow
from prefect.tasks.database.sqlite import SQLiteScript

# Latitude and Longitude of New York City
LAT_NYC = 40.7128
LON_NYC = -74.0060

WeatherData = namedtuple(
    'WeatherData',
    [
        'date',
        'average_temp',
        'precipitation',
    ],
)


# Prefect Task to create the sqlite database table
create_table = SQLiteScript(
    db='weather.db',
    script='CREATE TABLE IF NOT EXISTS weather '
    '(timestamp DATE, average_temp NUMERIC, precipitation NUMERIC)',
)


@task
def get_weather(latitude: float, longitude: float, year: int) -> DataFrame:
    """Use the meteostat library to query for historical weather"""
    # Set time period
    start = datetime(year, 1, 1)
    end = datetime(year, 12, 31)

    # Create Point for NYC
    location = Point(latitude, longitude)

    # Get daily data for the year
    data = Daily(location, start, end)
    return data.fetch()


@task
def get_weather_from_saved_file() -> DataFrame:
    """Obtain the weather from a pre-saved file"""
    with open('weather_pickle.bin', 'rb') as data_fp:
        data = pickle.load(data_fp)

    return data


@task
def parse_weather(data: DataFrame) -> List[WeatherData]:
    """Parse the results, converting to fahrenheit"""
    parsed_results = []

    for index, row in data.iterrows():
        date = sqlite3.Date(index.year, index.month, index.day)
        item = WeatherData(
            date=date,
            average_temp=celsius_to_fahr(row.get('tavg', 0)),
            precipitation=row.get('prcp', 0),
        )
        parsed_results.append(item)
    return parsed_results


def celsius_to_fahr(degrees_celsius: float) -> float:
    """Convert degrees celsius to degrees fahrenheit"""
    return (degrees_celsius * 9.0 / 5.0) + 32.0


@task
def store_weather(data: List[WeatherData]):
    """Insert the weather data into a sqlite3 database"""
    insert_cmd = 'INSERT INTO weather VALUES (?, ?, ?)'
    with closing(sqlite3.connect('weather.db')) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.executemany(insert_cmd, data)
            conn.commit()


def main():
    """Create and run the flow for NYC 2018"""
    # Create the flow
    with Flow('pickle flow') as flow:
        db_table = create_table()
        weather_data = get_weather(LAT_NYC, LON_NYC, 2018)
        parsed_data = parse_weather(weather_data)
        populated_table = store_weather(parsed_data)
        populated_table.set_upstream(db_table)

    # Run the flow
    flow.run()


if __name__ == '__main__':
    main()
