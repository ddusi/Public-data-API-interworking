import json
import urllib.parse
from urllib import request

# from listings.models import AddressInfo, PropertyList,PhotoForListing
from django.http import JsonResponse


# permissions_classes = (IsAuthenticated)
# http_method_names = [ 'PUT' ,'post', 'get']

def get_floor_info_view(request):


    sigunguCd = request.POST.get("sigunguCd")
    bjdongCd = request.POST.get("bjdongCd")
    bun = request.POST.get("bun")
    ji =request.POST.get("ji")
    
    #lnbrslno = request.POST.get('lnbrslno')
    
    #jibun_addr = request.POST.get('jibun_addr')

    context = { 'result': ''}

    
    

    context['result'] = 'success'


    
    print('get coord 실행')
    my_token = 'aaa'
    my_token = 'vsDuYh7rKmSHlHabD5uIMLru%2FIbLvNX38VCAiEJsb7TXLlrxRZr4Ru1X%2B8zleeAcQ15nwv6KG1IMS57yLx0fHg%3D%3D'

    # print(my_token)

    url = 'http://apis.data.go.kr/1611000/BldRgstService/getBrFlrOulnInfo'

   
    queryParams = '?' + urllib.parse.urlencode(
        #  {
                       
                        # "sigunguCd": '11680',
                        # "bjdongCd" : '10300' ,
                        # "bun": '0012',
                        # "ji": '0000',
        #             "serviceKey" :  my_token
        #             }
        
        
         {
         urllib.parse.quote_plus('ServiceKey', safe='/') :  my_token,
         #'serviceKey' :  my_token,  
         urllib.parse.quote_plus('numOfRows', safe='/') : 100,
         urllib.parse.quote_plus('sigunguCd', safe='/') :  sigunguCd, 
         urllib.parse.quote_plus('bjdongCd', safe='/') : bjdongCd, 
         urllib.parse.quote_plus('bun', safe='/') : bun, #x, 
         urllib.parse.quote_plus('ji', safe='/') : ji , # y, 

         
    }
          )
    print(queryParams)
    request = urllib.request.Request(url + queryParams+"&_type=json&serviceKey="+my_token)
    request.get_method = lambda: 'GET'
    response_data = urllib.request.urlopen(request).read()
    #print(response_data)

    json_data = json.dumps(response_data.decode('utf-8'))
    jdata = json.loads(json_data).replace("\'", "\"")


    print(jdata)
    final_data= json.loads(jdata)
    #print(final_data['response']['body']['items'])
    if final_data['response']['body']['items']!="" :
        context['list'] = final_data['response']['body']['items']
    a = final_data['response']['body']['items']['item']

    b = sorted(a, key=  lambda x: x['flrNo'] )#itemgetter('flrNo'))    x['rnum'])


    print(b)
    if final_data['response']['body']['items']!="" :# final_data["errCd"] == 0 :
        context['result'] = 'success'
        context['list'] = final_data['response']['body']['items']['item']


    else :
        print("에          러")
        context['result'] = 'fail'


    return JsonResponse(context)

