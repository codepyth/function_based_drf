from rest_framework import serializers
from .models import *

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'image1', 'image2', 'image3']

class FinancialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financial
        fields = ['id', 'salePrice', 'costPrice']

class AlternativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternative
        fields = ['product_id']
    
    def to_representation(self, instance):
        rep = super(AlternativeSerializer, self).to_representation(instance)
        rep['product_id'] = instance.product_id.name
        # rep['foreignkeyname'] = instance.foreignkeyname.actualfieldname in parent table
        return rep

class RelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Related
        fields = ['product_id']

    def to_representation(self, instance):
        rep = super(RelatedSerializer, self).to_representation(instance)
        rep['product_id'] = instance.product_id.name
        # rep['foreignkeyname'] = instance.foreignkeyname.actualfieldname in parent table
        return rep

class ProductRelationSerializer(serializers.ModelSerializer):
    isRelated = RelatedSerializer(many=True)
    alternative = AlternativeSerializer(many=True)
    class Meta:
        model = ProductRelations
        fields = ['isRelated', 'alternative']


# class ProductSerializer(serializers.ModelSerializer):
#     property = PropertySerializer(many=True)
#     financial = FinancialSerializer(many=True)
#     product_relation = ProductRelationSerializer(many=True)
#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'quantity', 'property', 'financial', 'product_relation']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'quantity']