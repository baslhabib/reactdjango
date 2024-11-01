from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .genetic_algorithm import run_genetic_algorithm  # Import your simple algorithm function

@api_view(['GET'])  # Change to GET since we're not expecting any input for this simple example
def run_algorithm(request):
    if request.method == 'GET':
        try:
            result = run_genetic_algorithm()  # Call the simple genetic algorithm
            return Response({"result": result}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
