#!"C:\Users\DC404A\PycharmProjects\sparta_algorithm\venv\Scripts\python.exe"

print("content-type: text/html; charset=utf-8\n")
import cgi, os, view

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'welcome'
    description = 'Hello, web'
print('''
<!DOCTYPE html>
<head>
    <title>{title}_WEB</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1><a href="index.py">HOME</a></h1>
    <div id="grid">
        <ol>
            {listStr}
        </ol>
        <div id="article">
        <a href="create.py">create</a>
        <form action="process_create.py" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
            <p><input type="submit"></p>
        </form>
        </div>
    </div>
</body>
'''.format(title=pageId, desc=description, listStr=view.getList()))