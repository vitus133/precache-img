import os
import sqlite3
import json

# Example of packages
# '[{"local-storage-operator": {}}, {"performance-addon-operator": {}}, {"ptp-operator": {}}, {"sriov-network-operator": {}}]'
packages = json.loads(os.getenv('REDHAT_OPERATORS'))

namespace = 'pre-cache'

def init_pkg_indexes(packages: list) -> dict:
    ret = {}
    for i in range(len(packages)):
        name = list(packages[i].keys())[0]
        ret[name] = i
    return ret


package_indexes = init_pkg_indexes(packages)
package_names = [list(i.keys())[0] for i in packages]
package_names_str = ','.join(package_names)

# Connect to the database
con = sqlite3.connect('/tmp/index.db')


# Get the default channel for each package, if not explicitly set
cur = con.cursor()
for row in cur.execute('SELECT name, default_channel FROM package'):
    if row[0] in package_names:
        default_channel = row[1]
        pkg_idx = package_indexes[row[0]]
        if packages[pkg_idx][row[0]].get('channel') == None:
            packages[pkg_idx][row[0]]['channel'] = default_channel

# Get bundle names by packages and channels
result_set = cur.execute(
    'SELECT package_name, name, head_operatorbundle_name FROM channel WHERE package_name IN (%s) ' %
    ','.join('?'*len(package_names)), package_names)
bundles = result_set.fetchall()
bundles_lst = []
for item in bundles:
    pkg_idx = package_indexes[item[0]]
    if item[1] == packages[pkg_idx][item[0]].get('channel'):
        packages[pkg_idx][item[0]]['operatorbundle_name'] = item[2]
        bundles_lst.append(item[2])


# Get CSVs by bundle names
result_set = cur.execute(
    'SELECT csv FROM operatorbundle WHERE name IN (%s) ' %
    ','.join('?'*len(bundles_lst)), bundles_lst)
csvs = result_set.fetchall()

images = []
for item in csvs:
    csv = json.loads(item[0].decode('utf8'))
    related_images = csv.get('spec').get('relatedImages')
    for i in related_images:
        images.append(i['image'])
    

print(images)    
