from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FormSubmission
from .serializers import FormSubmissionSerializer

@api_view(['GET', 'POST'])
def form_submission_api(request):
	if request.method == 'GET':
		submissions = FormSubmission.objects.all().order_by('-id')
		serializer = FormSubmissionSerializer(submissions, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = FormSubmissionSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
