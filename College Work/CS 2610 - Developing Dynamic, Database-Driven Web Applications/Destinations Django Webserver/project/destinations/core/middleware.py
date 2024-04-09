from .models import Session
from django.shortcuts import redirect
import hashlib
from django.http import HttpRequest

def session_middleware(next):
    def middleware(req:HttpRequest):
        
        #get the token
        token = req.COOKIES.get('token')
        
        #if the token exists
        if token != None:
            token_hash = hashlib.sha256(bytes(token, "UTF-8")).hexdigest()
            
            #see if the token is linked to a session and attach the corresponding user to the request
            try:
                session = Session.objects.get(token = token_hash)
                req.user = session.user
            except:
                session = False
                req.user = None
        else:
            session = False
            req.user = None
        
        public_uris = ['/', '/users/new/', '/sessions/new/', '/users/', '/sessions/']
        
        #if there is no session and the user is requesting a private uri
        if not session and req.path not in public_uris:
            return redirect('/sessions/new/')
        
        res = next(req)
        return res
     
    return middleware