from endpoints import about, experience, index, projects, info
from response import Response

def router(req):
    if req.uri == "/about":
        return about(req)
    elif req.uri == "/experience":
        return experience(req)
    elif req.uri == "/":
        return index(req)
    elif req.uri == "/projects":
        return projects(req)
    elif req.uri == "/info":
        return info(req)
    else:
        return Response(
            version="HTTP/1.1",
            code=404,
            reason="Not found",
            headers={
                "Content-Type": "text/html",
                "Content-Length": "23"
            },
            text="<h1>Page not found</h1>"
        )