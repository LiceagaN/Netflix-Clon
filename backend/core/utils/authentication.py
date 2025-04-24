from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from core.models import User
from core.utils.firebase import verify_token  # ajusta esta importación según tu estructura

class FirebaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            raise exceptions.AuthenticationFailed('Authorization header missing or invalid')

        id_token = auth_header.split(' ')[1]
        decoded = verify_token(id_token)
        if not decoded:
            raise exceptions.AuthenticationFailed('Invalid token')

        uid = decoded['uid']
        email = decoded.get('email', '')
        user, _ = User.objects.get_or_create(firebase_uid=uid, defaults={'email': email})
        return (user, None)
