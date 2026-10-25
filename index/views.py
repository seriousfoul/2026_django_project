from django.shortcuts import render
import internal.models as models
from django.http import JsonResponse
import random
from django.forms.models import model_to_dict
import index.form as ValidForm

# Create your views here.
def Index(request):
    banner = models.Banner.objects.all()
    banner = [model_to_dict(bannerRecord) for bannerRecord in banner] 
    history = models.History.objects.all()
    history = [model_to_dict(historyRecord) for historyRecord in history] 
    info = models.Info.objects.all()
    info = [model_to_dict(infoRecord) for infoRecord in info] 
    news = models.News.objects.all().order_by('-lastUpdate')[:3]
    news = [model_to_dict(newsRecord) for newsRecord in news] 
    
    brandSlogan, company = __templates()    
    return render(request, "front_home.htm", locals())


def Features(request):
    features = models.FeatureInfo.objects.all()
    features = [model_to_dict(featureRecord) for featureRecord in features]
    topics = models.FeatureType.objects.filter(enable=True)
    topics = [model_to_dict(topicRecord) for topicRecord in topics]
    
    brandSlogan, company = __templates()
    return render(request, "front_feature.htm", locals())

def Products(request):
    products = models.Item.objects.all()
    products = [model_to_dict(productRecord) for productRecord in products]
    topics = models.Category.objects.filter(enable=True)
    topics = [model_to_dict(topicRecord) for topicRecord in topics]
    
    brandSlogan, company = __templates()
    return render(request, "front_product.htm", locals())

def ProductsInfo(request, itemId: int=0):
    if itemId > 0:
        product = models.Item.objects.get(itemid=itemId)
        product.dimension = product.dimension.replace("{","").replace("}","")
        product.info = product.info.replace("{","").replace("}","")
        product = model_to_dict(product)
        
        brandSlogan, company = __templates()
        return render(request, "front_productInfo.htm", locals())
    else:
        return JsonResponse(status=404)
    
def News(request):
    news = models.News.objects.all()
    news = [model_to_dict(newsRecord) for newsRecord in news]
    
    brandSlogan, company = __templates()
    return render(request, "front_news.htm", locals())

def NewsInfo(request, newsId: int=0):
    if newsId > 0:
        news = models.News.objects.get(newsid=newsId)
        
        brandSlogan, company = __templates()
        return render(request, "front_newsInfo.htm", locals())
    else:
        return JsonResponse(status=404)

def FAQ(request):
    faq = models.Faq.objects.all()
    faq = [model_to_dict(faqRecord) for faqRecord in faq]

    brandSlogan, company = __templates()
    return render(request, "front_faq.htm", locals())

def Downloads(request):
    downloads = models.Downloads.objects.all()
    downloads = [model_to_dict(downloadsRecord) for downloadsRecord in downloads]

    brandSlogan, company = __templates()
    return render(request, "front_downloads.htm", locals())

def ContactUs(request):
    
    brandSlogan, company = __templates()
    return render(request, "front_contactus.htm", locals())

def AddForm(request):
    form = ValidForm.OrderForm(request.POST)
    if form.is_valid():
        companyname = request.POST['companyname']
        contactname = request.POST['contactname']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        title = request.POST['title']
        content = request.POST['content']
        record = models.Form.objects.create(companyname=companyname, contactname=contactname, email=email, address=address, phone=phone, title=title, content=content)
        record.save()
        record = models.Form.objects.all().order_by('-formid').first()
        formId = record.formid
        read = False
        processed = False
        record = models.Message.objects.create(formid_id=formId, read=read, processed=processed)
        record.save()
        msg = "insert success!" 
    else:
        formError = form.errors
        error = ""
        for e in formError.values:
            error = error + e + " \t"
        msg = error
        form = ValidForm()
       
    return render(request, "front_contactus.htm", locals())

def __templates():
    brandSlogans = models.FeatureInfo.objects.filter(topic_id=3)
    if len(brandSlogans) > 0:
        brandSlogan = brandSlogans[random.randint(0, len(brandSlogans)-1)].content
    else:
        brandSlogan = ""
    company = models.Company.objects.all().first()
    company = model_to_dict(company)
    return brandSlogan, company
