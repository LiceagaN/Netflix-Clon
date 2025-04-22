from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.utils.firebase import verify_token
from core.models import User

class AuthenticatedAPIView(APIView):
    def dispatch(self, request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return Response({'error': 'Authorization header missing or invalid'}, status=status.HTTP_401_UNAUTHORIZED)

        id_token = auth_header.split(' ')[1]
        decoded = verify_token(id_token)
        if not decoded:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
        
        uid = decoded['uid']
        email = decoded.get('email', '')
        user, _ = User.objects.get_or_create(firebase_uid=uid, defaults={'email': email})
        request.user = user
        
        return super().dispatch(request, *args, **kwargs)