from datetime import datetime
from response import Response

def logging_middleware(next):
    
    def middleware(req):
        print(f"{req.method} {req.uri}")
        res = next(req)
        print(f"{res.version} {res.code} {res.reason}")
        return res
    
    return middleware

def static_files_middleware(next):
    
    def middleware(req):
        if "." in req.uri:
            try:
                with open("static" + req.uri) as static_file:
                    
                    static_file = static_file.read()
                    
                    if req.uri[req.uri.index("."):] == ".js":
                        return Response(
                            version = "HTTP/1.1",
                            code = 200,
                            reason = "ok",
                            headers = {
                                "Content-Type": "text/javascript",
                                "Content-Length": str(len(static_file))
                            },
                            text = static_file
                        )
                    elif req.uri[req.uri.index("."):] == ".css":
                        return Response(
                            version = "HTTP/1.1",
                            code = 200,
                            reason = "ok",
                            headers = {
                                "Content-Type": "text/css",
                                "Content-Length": str(len(static_file))
                            },
                            text = static_file
                        )
                    else:
                        raise FileNotFoundError
                    
            except FileNotFoundError:
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
        
        res = next(req)
        return res
    
    return middleware

def required_headers_middleware(next):
    def middleware(req):
        res = next(req)
        
        headers = {
        "Server": "my server",
        "Date": str(datetime.today()),
        "Connection": "close",
        "Cache-Control": "no-cache"
        }
        
        headers.update(res.headers)
        res.headers = headers
        return res

    return middleware

def compose(end_result_function, middleware_factory_list):
    
    if len(middleware_factory_list) != 0:
        middleware_chain = middleware_factory_list[0](end_result_function)
        
        if len(middleware_factory_list) != 1:
            for middleware in middleware_factory_list[1:]:
                middleware_chain = middleware(middleware_chain)
                
            return middleware_chain
        else:
            print("Only one middleware in list")
    else:
        print("no middleware in list")