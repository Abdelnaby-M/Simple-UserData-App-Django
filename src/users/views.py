from distutils.command.build_scripts import first_line_re
from rest_framework.views import APIView
from rest_framework.response import Response
import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed
from .serializers import userSerializer
from .models import user
# Create your views here.
    
class userView(APIView):
    
    def get(self, request):
        
        token = request.data["auth-token"]

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        User = user.objects.filter(id=payload['id']).first()
        serializer = userSerializer(User)
        return Response(serializer.data)
    
    
    def post(self, request, *args, **kwargs):
        
        serializer = userSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    
class authView(APIView):
    
    def post(self, request):
        phone_number = request.data['phone_number']
        password = request.data['password']

        User = user.objects.filter(phone_number=phone_number).first()

        if User is None:
            raise AuthenticationFailed('User not found!')

        if User.password != password:
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': User.id,
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response
    
    
class statusView(APIView):
    
    def post(self, request):
        
        phone_number = request.data['phone_number']
        token = request.data["auth-token"]
        status = request.data["status"]
        
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            # print(payload)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        User = user.objects.get(id=payload['id'])
        # User = User.first()
        User.status = status
        User.save()
        print(User)
        serializer = userSerializer(User)
        return Response(serializer.data)