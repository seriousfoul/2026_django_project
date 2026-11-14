from django.contrib import admin
from internal.models import Employee, CompanyLevel, Login, LoginToken


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employeeid', 'name', 'account', 'enable', 'addtime', 'lastUpdate', 'companylevelid_id')
    list_filter = ('enable', 'companylevelid_id')
    search_fields = ('employeeid', 'name', 'account', 'companylevelid_id')
    ordering = ('companylevelid_id', 'addtime', 'account', 'enable', 'name')
    
   
class CompanyLevelAdmin(admin.ModelAdmin):
    list_display = ('companylevelid', 'level', 'name', 'grade', 'enable')
    list_filter = ('enable', 'grade', 'level')
    search_fields = ('companylevelid', 'grade', 'level', 'enable', 'name')
    ordering = ('companylevelid', 'enable', 'grade', 'level', 'name')
    
class LoginAdmin(admin.ModelAdmin):
    list_display = ('loginid','employeeid_id', 'loginTime', 'logoutTime')
    search_fields = ('loginid','employeeid_id', 'loginTime', 'logoutTime')
    ordering = ('loginid', 'loginTime', 'logoutTime', 'employeeid_id')
    
class LoginTokenAdmin(admin.ModelAdmin):
    list_display = ('logintokenid','employeeid_id', 'token', 'tokenTime')
    search_fields = ('logintokenid','employeeid_id', 'tokenTime')
    ordering = ('logintokenid', 'tokenTime', 'employeeid_id')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(CompanyLevel, CompanyLevelAdmin)
admin.site.register(Login, LoginAdmin)
admin.site.register(LoginToken, LoginTokenAdmin)
