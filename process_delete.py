#!"C:\Users\DC404A\PycharmProjects\sparta_algorithm\venv\Scripts\python.exe"

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove('data/'+pageId)

#Redirection
print("Location: index.py")
print()