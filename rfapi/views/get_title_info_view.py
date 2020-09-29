import requests
import xmltodict
from furl import furl
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class GetTitleInfoView(APIView):
	def post(self, request):
		ServiceKey = 'vsDuYh7rKmSHlHabD5uIMLru%2FIbLvNX38VCAiEJsb7TXLlrxRZr4Ru1X%2B8zleeAcQ15nwv6KG1IMS57yLx0fHg%3D%3D'

		f = furl('http://apis.data.go.kr/1611000/BldRgstService/getBrTitleInfo')
		for key, val in request.data.items():
			f.args[key] = val

		response_json = requests.get(f.url + '&ServiceKey=' + ServiceKey)
		getBrTitleInfo_api_request = xmltodict.parse(response_json.text)

		return Response(getBrTitleInfo_api_request, status=status.HTTP_200_OK)
