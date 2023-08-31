import psycopg2
import psycopg2.extras

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '2424863Qqq'
DATABASE = 'exercise_restaurant_menu'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


class MenuItem:

    def __init__(self, item_name, item_price=0):
        self.item_name = item_name
        self.item_price = item_price

    def save(self):
        query = F'INSERT INTO public."Menu_Items" (item_name, item_price) VALUES (\'{self.item_name}\', {self.item_price});'

        cursor.execute(query)
        connection.commit()
        # connection.close()

    def delete(self):
        query = F'DELETE FROM public."Menu_Items" WHERE (item_name = \'{self.item_name}\');'
        cursor.execute(query)
        connection.commit()
        # connection.close()

    def update(self, new_name, new_price):
        query = F'UPDATE public."Menu_Items" SET item_name=\'{new_name}\', item_price=\'{new_price}\' WHERE (item_name = \'{self.item_name}\');'
        cursor.execute(query)
        connection.commit()
        # connection.close()

    def view_one_item(self):
        query = F'SELECT * FROM public."Menu_Items" WHERE (item_name = \'{self.item_name}\');'
        cursor.execute(query)
        results = cursor.fetchall()
        # connection.close()
        return results

# item_1 = MenuItem('Burger2', 35)
# print(item_1.item_name)
# item_1.save()
# item_1.update('New_burger', 40)
# item_1.delete()
