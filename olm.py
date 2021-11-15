import os
import sqlite3

packages = os.getenv('REDHAT_OPERATORS')

query = (
    f'SELECT image FROM related_image WHERE operatorbundle_name IN '
    f'(SELECT head_operatorbundle_name FROM channel WHERE '
    f'package_name IN ({packages}) AND name = '
    f'(SELECT default_channel FROM package WHERE name IN ({packages})))')

con = sqlite3.connect('/tmp/index.db')
cur = con.cursor()
result_set = cur.execute(query)
results = result_set.fetchall()
con.close()
images = [item[0] for item in results]
print('\n'.join(images))

