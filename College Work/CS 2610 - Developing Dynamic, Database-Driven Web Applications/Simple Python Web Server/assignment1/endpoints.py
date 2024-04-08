from response import Response

def about(req):
    with open("templates/about.html") as html_file:
        html_file = html_file.read()
        return Response(version = "HTTP/1.1",
                        code = "200",
                        reason = "ok",
                        headers = {
                            "Content-Type": "text/html",
                            "Content-Length": str(len(html_file))
                        },
                        text = html_file
                        )
        

def experience(req):
    with open("templates/experience.html") as html_file:
        html_file = html_file.read()
        return Response(version = "HTTP/1.1",
                        code = "200",
                        reason = "ok",
                        headers = {
                            "Content-Type": "text/html",
                            "Content-Length": str(len(html_file))
                        },
                        text = html_file
                        )
        

def index(req):
    with open("templates/index.html") as html_file:
        html_file = html_file.read()
        return Response(version = "HTTP/1.1",
                        code = "200",
                        reason = "ok",
                        headers = {
                            "Content-Type": "text/html",
                            "Content-Length": str(len(html_file))
                        },
                        text = html_file
                        )
        

def projects(req):
    with open("templates/projects.html") as html_file:
        html_file = html_file.read()
        return Response(version = "HTTP/1.1",
                        code = "200",
                        reason = "ok",
                        headers = {
                            "Content-Type": "text/html",
                            "Content-Length": str(len(html_file))
                        },
                        text = html_file
                        )

def info(req):
    return Response(version = "HTTP/1.1",
            code = "301",
            reason = "Moved Permanently",
            headers = {
                "Location": "/about",
            },
            text = ""
            )