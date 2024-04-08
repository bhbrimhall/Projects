from request import Request

def decode_request(encoded_request):

    encoded_request = encoded_request.split("\n")
    
    first_line = encoded_request.pop(0).replace("\r", "").split(" ")
    req_method = first_line[0]
    req_uri = first_line[1]
    req_version = first_line[2]
    
    req_headers = {}
    while True:
        
        line = encoded_request.pop(0)
        
        if line == "\r":
            break
        
        line = line.replace("\r", "").split(" ", 1)
        req_headers[line[0][:-1]] =  line[1]
        
    req_text = "\n".join(encoded_request)
    
    return Request(method = req_method, 
                   uri = req_uri, 
                   version = req_version, 
                   text = req_text, 
                   headers = req_headers)

def encode_response(response):
    encoded_response = f"{response.version} {response.code} {response.reason}\n"
    for key in response.headers:
        encoded_response = encoded_response + key + ": " + response.headers[key] + "\n"
    encoded_response = encoded_response + "\n" + response.text
    return encoded_response