

# 
# print "uploaded:", response

import dropbox, os
from os import walk
client = dropbox.client.DropboxClient('6SUyZChjYXAAAAAAAAAADAgT0adFe9EVeUiWWh-9vVev3kfbYQT6sYZ8Z1E-6vbC')

files = []
for (dirpath, dirnames, filenames) in walk('/home/administrator/Documents/uploads/2016/01/'):
    files.extend(filenames)
    break

for item in files :
	f = open('/home/administrator/Documents/uploads/2016/01/' + item, 'rb')
	response = client.put_file('/Public/wp-content/uploads/2016/01/'+item, f)
	os.remove('/home/administrator/Documents/uploads/2016/01/' + item)
