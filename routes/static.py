from bottle import get, static_file

@get("/static/<filepath:re:.*\.png>")
def image(filepath):
    return static_file(filepath, root="static/")
