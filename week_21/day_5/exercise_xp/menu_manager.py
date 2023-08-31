
import psycopg2.extras

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '2424863Qqq'
DATABASE = 'exercise_restaurant_menu'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


class MenuManager:

    def get_by_name(self, item_name):
        try:
            query = F'SELECT * FROM public."Menu_Items" WHERE (item_name = \'{item_name}\');'
            cursor.execute(query)
            results = cursor.fetchall()
            # connection.close()
            return results
        except:
            return None

    def all_items(self):
        query = F'SELECT * FROM public."Menu_Items"'
        cursor.execute(query)
        results = cursor.fetchall()
        # connection.close()
        return results


# bob = MenuManager()
# for item in bob.all_items():
#     print(item)
