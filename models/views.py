from django.shortcuts import render
from rest_framework import generics
from .models import ListFeatures, Code, UserCodeRedemption
from .serializers import ListFeaturesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import CodeSerializer

class ListFeaturesList(generics.ListCreateAPIView):
    serializer_class = ListFeaturesSerializer

    def get_queryset(self):
        queryset = ListFeatures.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset

class ListFeaturesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ListFeaturesSerializer
    queryset = ListFeatures.objects.all()

class CodeListCreateView(generics.ListCreateAPIView):
    serializer_class = CodeSerializer
    queryset = Code.objects.all()

class CodeRedeemView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CodeSerializer

    def post(self, request, *args, **kwargs):
        code_value = request.data.get('code')
        user = request.user

        if code_value == 'nicetry':
            try:
                code = Code.objects.get(code=code_value)
                if UserCodeRedemption.objects.filter(user=user, code=code).exists():
                    return Response({'error': 'คุณใช้โค้ดนี้ไปแล้ว!'}, status=status.HTTP_409_CONFLICT)
                
                UserCodeRedemption.objects.create(user=user, code=code)
                user.points += 50  # Assuming 'points' is a field in the User model
                user.save()

                return Response({'success': 'ได้รับแต้ม 50 แต้ม'}, status=status.HTTP_200_OK)
            except Code.DoesNotExist:
                return Response({'error': 'โค้ดผิดพลาดหรือไม่มีโค้ดนี้!'}, status=status.HTTP_400_BAD_REQUEST)
        elif code_value == 'ggez':
            try:
                code = Code.objects.get(code=code_value)
                if UserCodeRedemption.objects.filter(user=user, code=code).exists():
                    return Response({'error': 'คุณใช้โค้ดนี้ไปแล้ว!'}, status=status.HTTP_409_CONFLICT)
                
                UserCodeRedemption.objects.create(user=user, code=code)
                user.points += 10  # Assuming 'points' is a field in the User model
                user.save()

                return Response({'success': 'ได้รับแต้ม 10 แต้ม'}, status=status.HTTP_200_OK)
            except Code.DoesNotExist:
                return Response({'error': 'โค้ดผิดพลาดหรือไม่มีโค้ดนี้!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'โค้ดผิดพลาดหรือไม่มีโค้ดนี้!'}, status=status.HTTP_400_BAD_REQUEST)