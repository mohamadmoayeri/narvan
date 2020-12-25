from rest_framework import serializers


class Serial(serializers.Serializer):
    n = serializers.IntegerField(required=True)
    m = serializers.IntegerField(required=False)
    func = serializers.CharField(max_length=10, required=True)

    def validate(self,data):
        if data['func']=='ackermann' and (data['n']<0 or data['m']<0 or data['n']>5):
            raise serializers.ValidationError({'error':"numbers must be positive integer and n must be less than 6"})

        elif data['func']=='ackermann' and (data['n']==4 and data['m']>1):
            raise serializers.ValidationError({'error':'m must be less than 2'})

        elif data['func']=='ackermann' and (data['n']==3 and data['m']>13):
            raise serializers.ValidationError({'error':"m must be less than 14"})

        elif data['func']=='ackermann' and (data['n']==5 and data['m']>0):
            raise serializers.ValidationError({'error':"m must be less than 1"})

        elif data['func']=='fibonacci' and data['n']<0:
            raise serializers.ValidationError({'error':"n must be positive integer number"})

        elif data['func']=='factorial' and data['n']<0:
            raise serializers.ValidationError({'error':"n must be positive integer number"})



        return data

