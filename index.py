#!"C:\Users\DC404A\PycharmProjects\sparta_algorithm\venv\Scripts\python.exe"

print("content-type: text/html; charset=utf-8\n")
import cgi, os, view
# sanitizer = html_sanitizer.Sanitizer()

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
    description = description.replace('<', '&lt;')
    description = description.replace('>', '&gt;')
    # description = sanitizer.sanitize(description)
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    pageId = 'welcome'
    description = 'Hello, web'
    update_link = ''
    delete_action = ''
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
        {update_link}
        {delete_action}
        <h2>{title}</h2>
        <p>{desc}</p>
        </div>
    </div>
</body>
'''.format(title=pageId,
    desc=description,
    listStr=view.getList(),
    update_link=update_link,
    delete_action=delete_action))