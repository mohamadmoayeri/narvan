from django import forms

class fibonacci_form(forms.Form):

    x=forms.IntegerField(label_suffix="=",label='n')

    def clean_x(self):
        x=self.cleaned_data['x']
        if  x<=0:
            raise forms.ValidationError('please enter a positive integer number')
        return x



class ackermann_form(forms.Form):

    n=forms.IntegerField(label='n',label_suffix="=")
    m=forms.IntegerField(label='m',label_suffix="=")

   

    def clean(self):
        n=self.cleaned_data['n']

        m=self.cleaned_data['m']
        
        if m<0 or n<0 or n>=6:
            raise forms.ValidationError("numbers must be positive integer and n must be less than 6")

        elif n==3 and m>13:
            raise forms.ValidationError('m must be less than 14')
        elif n==4 and m>1:
            raise forms.ValidationError('m must be less than 2')
        elif n==5 and m>0:
            raise forms.ValidationError('m must be less than 1')

      

        



        


        return self.cleaned_data






class factorial_form(forms.Form):
    z=forms.IntegerField(label="n",label_suffix="=")

    def clean_z(self):
        z=self.cleaned_data.get('z')
        if  z<0:
            raise forms.ValidationError('please enter a positive integer number')

        return z