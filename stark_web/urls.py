"""
URL configuration for stark_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
import index.views as front
import backend.views as backend
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", front.Index),
    path("index/", front.Index),
    path("features/", front.Features),
    path("products/", front.Products),
    path("products/productInfo/<int:itemId>/", front.ProductsInfo),
    path("news/", front.News),
    path("news/newsinfo/<int:newsId>/", front.NewsInfo),
    path("faq/", front.FAQ),
    path("downloads/", front.Downloads),
    path("contactus/", front.ContactUs),
    path("contactus/addform/", front.AddForm),
    
    path("backend/<str:mainType>/", backend.changeIndex),
    path("backend/index/banner/", backend.Banner),
    path("backend/index/banner/<int:bannerId>/", backend.Banner),
    path("backend/index/banner/<int:bannerId>/<str:actionType>/", backend.Banner),    
    path("backend/index/info/", backend.Info),
    path("backend/index/info/<int:infoId>/", backend.Info),
    path("backend/index/info/<int:infoId>/<str:actionType>/", backend.Info),
    path("backend/index/history/", backend.History),
    path("backend/index/history/<int:historyId>/", backend.History),
    path("backend/index/history/<int:historyId>/<str:actionType>/", backend.History),
    path("backend/features/featureType/", backend.FeatureType),
    path("backend/features/featureType/<int:featureTypeId>/", backend.FeatureType),
    path("backend/features/featureType/<int:featureTypeId>/<str:actionType>/", backend.FeatureType),
    path("backend/features/featureInfo/", backend.FeatureInfo),
    path("backend/features/featureInfo/<int:featureInfoId>/", backend.FeatureInfo),
    path("backend/features/featureInfo/<int:featureInfoId>/<str:actionType>/", backend.FeatureInfo),
    path("backend/product/category/", backend.Category),
    path("backend/product/category/<int:categoryId>/", backend.Category),
    path("backend/product/category/<int:categoryId>/<str:actionType>/", backend.Category),
    path("backend/product/item/", backend.Item),
    path("backend/product/item/<int:itemId>/", backend.Item),
    path("backend/product/item/<int:itemId>/<str:actionType>/", backend.Item),
    path("backend/news/news/", backend.News),
    path("backend/news/news/<int:newsId>/", backend.News),
    path("backend/news/news/<int:newsId>/<str:actionType>/", backend.News),
    path("backend/faq/faq/", backend.Faq),
    path("backend/faq/faq/<int:faqId>/", backend.Faq),
    path("backend/faq/faq/<int:faqId>/<str:actionType>/", backend.Faq),
    path("backend/downloads/downloads/", backend.Downloads),
    path("backend/downloads/downloads/<int:downloadsId>/", backend.Downloads),
    path("backend/downloads/downloads/<int:downloadsId>/<str:actionType>/", backend.Downloads),
    path("backend/contactUs/company/", backend.Company),
    path("backend/contactUs/company/<str:actionType>/", backend.Company),
    path("backend/contactUs/message/", backend.Message),
    path("backend/contactUs/message/<int:messageId>/", backend.Message),
    path("backend/contactUs/form/<int:messageId>/<int:formId>/", backend.GetForm),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    