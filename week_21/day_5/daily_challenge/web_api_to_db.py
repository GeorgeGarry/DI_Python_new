import requests
import psycopg2
from psycopg2 import extras
import random


def fetch_random_countries(count=10):
    url = f'https://restcountries.com/v3.1/all?fields=name,capital,flags,subregion,population'
    response = requests.get(url)

    if response.status_code == 200:
        countries = response.json()
        return random.sample(countries, count)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []


def insert_countries_into_db(countries):
    HOSTNAME = 'localhost'
    USERNAME = 'postgres'
    PASSWORD = '2424863Qqq'
    DATABASE = 'web_to_api_countries'

    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    try:
        for country in countries:
            name = country["name"]["official"]
            capital = country["capital"][0]
            flag = country["flags"]["png"]
            subregion = country["subregion"]
            population = country["population"]

            query = f"INSERT INTO countries (name, capital, flag, subregion, population) VALUES (%s, %s, %s, %s, %s);"
            cursor.execute(query, (name, capital, flag, subregion, population))

        connection.commit()
        connection.close()
    except:
        print("something went wrong...")


random_10_countries = fetch_random_countries()

insert_countries_into_db(random_10_countries)
