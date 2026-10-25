from django import forms
from django.core.validators import FileExtensionValidator
import internal.models as models

valid_image = ['jpg', 'jpeg', 'png', 'webp', 'avif']
valid_file = ['pdf']
error_message={
          'required': '此欄位是必須的',
          'invalid': '此欄位格式錯誤',
          'empty': '此欄位內容不能為空',
          'max_length': '此欄位內容超過最大限制',
          'min_length': '此欄位內容低於最小限制',
          'max_value': '此欄位內容超過最大數值',
          'min_value': '此欄位內容低於最小數值',
          'invalid_choice': '此欄位選擇值異常',
      }


class Banner(forms.Form):
    name = forms.CharField(max_length=30, required=False, error_messages=error_message)
    image = forms.FileField(
        allow_empty_file=False, 
        error_messages= error_message,
        validators=[
            FileExtensionValidator(
                allowed_extensions=valid_image, 
                message='不支援的圖片格式，僅限 jpg, jpeg, png, webp, avif'
            )
        ]
    )
    enable = forms.BooleanField(error_messages=error_message)
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            max_size = 5 * 1024 * 1024 
            if image.size > max_size:
                raise forms.ValidationError('圖片檔案過大，最大限制為 5MB！')
        return image


class Info(forms.Form):
    title = forms.CharField(max_length=30, error_messages=error_message)
    image = forms.FileField(
        allow_empty_file=False, 
        error_messages= error_message,
        validators=[
            FileExtensionValidator(
                allowed_extensions=valid_image, 
                message='不支援的圖片格式，僅限 jpg, jpeg, png, webp, avif'
            )
        ]
    )
    enable = forms.BooleanField(error_messages=error_message)
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            max_size = 5 * 1024 * 1024 
            if image.size > max_size:
                raise forms.ValidationError('圖片檔案過大，最大限制為 5MB！')
        return image


class History(forms.Form):
    title = forms.CharField(max_length=30, error_messages=error_message)
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}), error_messages=error_message)

class FeatureType(forms.Form):    
    name = forms.CharField(max_length=30, error_messages=error_message)
    chinese_name = forms.CharField(max_length=30, error_messages=error_message)
    enable = forms.BooleanField(error_messages=error_message)
        
    
class FeatureInfo(forms.Form):
    topic = forms.ChoiceField(error_messages=error_message)
    title = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}), error_messages=error_message)
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}), error_messages=error_message)

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['topic'].choices = [
            (record.featuretypeid, record.chinese_name) 
            for record in models.FeatureType.objects.all()
        ]
        
class Category(forms.Form):    
    name = forms.CharField(max_length=30, error_messages=error_message)
    enable = forms.BooleanField(error_messages=error_message)

class Item(forms.Form):    
    name = forms.CharField(max_length=30, error_messages=error_message)
    image = forms.FileField(
        error_messages= error_message,
        validators=[
            FileExtensionValidator(
                allowed_extensions=valid_image, 
                message='不支援的圖片格式，僅限 jpg, jpeg, png, webp, avif'
            )
        ]
    )
    dimension = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}), error_messages=error_message)
    material = forms.CharField(max_length=100, error_messages=error_message)
    info = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}), required=False, error_messages=error_message)
    categoryid = forms.ChoiceField(error_messages=error_message)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoryid'].choices = [
            (record.categoryid, record.name) 
            for record in models.Category.objects.all()
        ]
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            max_size = 5 * 1024 * 1024 
            if image.size > max_size:
                raise forms.ValidationError('圖片檔案過大，最大限制為 5MB！')
        return image
        

class News(forms.Form):    
    title = forms.CharField(max_length=30, error_messages=error_message)
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}), error_messages=error_message)
        

class Faq(forms.Form):    
    question = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}), max_length=30, error_messages=error_message)
    answer = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}), error_messages=error_message)
        
        
class Downloads(forms.Form):    
    name = forms.CharField(max_length=30, error_messages=error_message)
    pdf = forms.FileField(
        allow_empty_file=False, 
        error_messages= error_message,
        validators=[
            FileExtensionValidator(
                allowed_extensions=valid_file, 
                message='不支援的圖片格式，僅限 pdf'
            )
        ]
    )
    version = forms.CharField(max_length=30, error_messages=error_message)
    info = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}), required=False, error_messages=error_message)


class Company(forms.Form):
    name = forms.CharField(max_length=30, error_messages=error_message)
    email = forms.CharField(max_length=100, error_messages=error_message)
    address = forms.CharField(max_length=100, error_messages=error_message)
    phone = forms.CharField(max_length=20, error_messages=error_message)
    fax = forms.CharField(max_length=20, required=False, error_messages=error_message)  
    servicetime = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}), required=False, error_messages=error_message)
    

class Message(forms.Form):    
    read = forms.BooleanField(required=False, error_messages=error_message)
    processed = forms.BooleanField(required=False, error_messages=error_message)