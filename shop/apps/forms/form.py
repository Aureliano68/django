from django import forms
import datetime
from django.core import validators
from django.core.exceptions import ValidationError

class input1(forms.Form):
    name=forms.CharField(max_length=30,label="نام",required=True)
    family=forms.CharField(max_length=50,label=" نام خانوادگی",required=True)
    age=forms.IntegerField(label='سن', required=False)
    is_active=forms.BooleanField(initial=True,label='وضعیت')
    

class input2(forms.Form):
    name=forms.CharField(max_length=30,label="نام",required=True)
    family=forms.CharField(max_length=50,label=" نام خانوادگی",required=True)
    age=forms.IntegerField(label='سن', required=False)
    is_active=forms.BooleanField(initial=True,label='وضعیت')
    avg=forms.DecimalField(max_digits=4,decimal_places=2,max_value=20,min_value=0,label='معدل')
    email=forms.EmailField(label='ایمیل')
    regester=forms.DateField(label='تاریخ')
    image=forms.ImageField(label='بارگذاری تصویر')
    fav_color=[
        ('1','آبی'),
        ('1','قرمز'),
        ('1','سبز'),
        ('1','مشکی'),

    ]
    color=forms.ChoiceField(choices=fav_color,label='رنگ انتخابی')
    

    
class input3(forms.Form):
    name=forms.CharField(max_length=30,label="نام",required=True)
    family=forms.CharField(max_length=50,label=" نام خانوادگی",required=True)
    age=forms.IntegerField(label='سن', required=False)
    is_active=forms.BooleanField(initial=True,label='وضعیت')
    password=forms.CharField(max_length=20,required=True,label='رمز عبور',widget=forms.PasswordInput())
    list_years=['1992','1993','1994','1995','1996']
    regester_date=forms.DateField(label='تاریخ',initial=datetime.datetime.now,widget=forms.SelectDateWidget(years=list_years))
    regester_date2=forms.DateField(label='تاریخ',initial=datetime.datetime.now,widget=forms.NumberInput(attrs={'type':'date'}))
    fav_color=[
        ('1','آبی'),
        ('1','قرمز'),
        ('1','سبز'),
        ('1','مشکی'),

    ]
    color=forms.MultipleChoiceField(label='رنگ انتخابی',widget=forms.CheckboxSelectMultiple,choices=fav_color)
    color2=forms.ChoiceField(label='رنگ انتخابی',widget=forms.RadioSelect,choices=fav_color)
    
    
    
    
def chekvalidname(value):
    value=str(value)
    if len(value)<3 or len(value)>8:
        raise forms.ValidationError('کاراکترها بیش از حد مجاز هستند')
  
def chekvalidage(value):
    value=int(value)
    if value<20 or value>40:
        raise forms.ValidationError('سن درست نیست')
    
class input4(forms.Form):
    name=forms.CharField(max_length=30,
                         label="نام",
                         required=True,
                         validators=[chekvalidname])
    
    family=forms.CharField(max_length=50,label=" نام خانوادگی",required=True)
    
    age=forms.IntegerField(label='سن', required=False,validators=[chekvalidage])
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        return name
        
    def clean_family(self):
        family = self.cleaned_data["family"]
        if family[0]!='t':
            raise ValidationError('فامیلی باس با تت شروع شه')
        return family
    
    
    def clean_age(self):
        age = self.cleaned_data["age"]
        return age
        