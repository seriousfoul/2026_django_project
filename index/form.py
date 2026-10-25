from django import forms

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


class OrderForm(forms.Form):    
    companyname = forms.CharField(max_length=30, required=False, error_messages=error_message)
    contactname = forms.CharField(max_length=10, error_messages=error_message)
    email = forms.CharField(max_length=100, error_messages=error_message)
    address = forms.CharField(max_length=100, error_messages=error_message)
    phone = forms.CharField(max_length=20, error_messages=error_message)
    title = forms.CharField(max_length=30, error_messages=error_message)
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}), required=False, error_messages=error_message)