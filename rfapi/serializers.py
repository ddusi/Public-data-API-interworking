from listings.models import AddressInfo, PropertyList,PhotoForListing
from rest_framework import serializers


class AddressInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressInfo
        fields = '__all__' #['url', 'username', 'email', 'groups']



class PropertyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyList
        fields = '__all__' #['url', 'username', 'email', 'groups']



class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoForListing
        fields = '__all__' # ['photo', 'is_main', 'listing'] 


