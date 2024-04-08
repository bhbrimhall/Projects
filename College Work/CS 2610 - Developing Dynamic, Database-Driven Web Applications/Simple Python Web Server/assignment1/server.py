import socket
from encoder import decode_request, encode_response
from middleware import logging_middleware, static_files_middleware, required_headers_middleware, compose
from router import router

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 8000))
    s.listen()
    print("Listening on port 8000...")

    while True:
        connection, addr = s.accept()
        with connection:
            data = connection.recv(8192)
            if not data:
                connection.close()
                continue

            req = decode_request(str(data, "UTF-8"))
            
            middleware_chain = compose(router,[static_files_middleware, required_headers_middleware, logging_middleware])
            
            res = middleware_chain(req)
            
            res = encode_response(res)
    
            connection.send(bytes(res, "UTF-8"))
            