from django.shortcuts import render,redirect
import internal.models as models
from datetime import datetime
import hashlib
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.forms.models import model_to_dict
import os

pageTypeName = {
    "index":"首頁設定",
    "features":"核心特色",
    "product":"產品相關",
    "news":"最新消息",
    "faq":"常見問題",
    "downloads":"文件下載",
    "contactUs":"聯絡我們",
    "banner":"首頁橫幅",
    "info":"公司照片",
    "history": "歷史前沿",
    "featureType": "特色種類",
    "featureInfo": "特色資訊",
    "category":"產品種類",
    "item":"產品資訊",
    "company":"公司資訊",
    "form":"諮詢表單",
    "message":"訊息通知"
    }

pageMainType = [
    "index", 
    "features", 
    "product", 
    "news", 
    "faq", 
    "downloads", 
    "contactUs" 
    ]

pageSubType = {
    "index" : ["banner", "info", "history"],
    "features": ["featureType", "featureInfo"],
    "product": ["category", "item"],
    "news": ["news"],
    "faq": ["faq"],
    "downloads": ["downloads"],
    "contactUs": ["company", "message"]
    }

typeData = {}
for mainType in pageMainType:   
    typeData[mainType] = pageTypeName.get(mainType)

subTypeData = {}
for typeName, subTypeList in pageSubType.items():
    subType = []
    for subTypeName in subTypeList:
        subType.append({
               "type": subTypeName,
               "typeName": pageTypeName.get(subTypeName)
            })
    subTypeData[typeName] = subType

# Create your views here.
def Banner(request, bannerId :int=0, actionType :str=None):
    if request.method == "POST":
        if actionType == "put" and bannerId > 0:
            record = models.Banner.objects.get(bannerid=bannerId)
            record.name = request.POST['name']
            record.enable = True if request.POST.get('enable') is not None and request.POST.get('enable').lower() == "true" else False
            record.save()
            msg = "update success!"
        else:            
            if request.FILES.get('image') and request.FILES.get('image').size() > 0 :
                imgName = __SaveFile(request.FILES.get('image',''), request.POST['name'], ".webp")
                imgPath = "/media/" + imgName
            else:
                imgPath = ""
            name = request.POST['name']
            enable = True if request.POST.get('enable') is not None and request.POST.get('enable').lower() == "true" else False
            record = models.Banner.objects.create(name=name, imgpath=imgPath, enable=enable)
            record.save()
            msg = "insert success!"
    else:
        if actionType == "delete" and bannerId > 0:
            record = models.Banner.objects.get(bannerid=bannerId)
            record.delete()
            msg = "delete success!"
        
    query = models.Banner.objects.all()
    data = query 

    mainType = pageMainType[0]
    subType = pageSubType[mainType][0]
    menu = typeData
    subMenu = subTypeData.get(mainType)
    currentTypeName = pageTypeName[subType]
    
    return render(request, "backend_banner.htm", locals())

def Info(request, infoId :int=0, actionType :str=None):
    if request.method == "POST":
        if actionType == "put" and infoId > 0:            
            record = models.Info.objects.get(infoid=infoId)
            record.title = request.POST['title']
            record.enable = True if request.POST.get('enable') is not None and request.POST.get('enable').lower() == "true" else False
            record.save()
            msg = "update success!"
        else:                  
            if request.FILES.get('image') and request.FILES.get('image').size() > 0:
                imgName = __SaveFile(request.FILES.get('image',''), request.POST['title'], ".webp")
                imgPath = "/media/" + imgName
            else:
                imgPath = ""
            title = request.POST['title']
            enable = True if request.POST.get('enable') is not None and request.POST.get('enable').lower() == "true" else False
            record = models.Info.objects.create(title=title, imgpath=imgPath, enable=enable)
            record.save()
            msg = "insert success!"
    else:
        if actionType == "delete" and infoId > 0:
            record = models.Info.objects.get(infoid=infoId)
            record.delete()
            msg = "delete success!"
        
    query = models.Info.objects.all()
    data = query 
     
    mainType = pageMainType[0]
    subType = pageSubType[mainType][1]
    menu = typeData
    subMenu = subTypeData.get(mainType)
    currentTypeName = pageTypeName[subType]
    return render(request, "backend_info.htm", locals())

def History(request, historyId :int=0, actionType :str=None):
    if request.method == "POST":
        if actionType == "put" and historyId > 0:            
            record = models.History.objects.get(historyid=historyId)
            record.title = request.POST['title']
            record.content = request.POST['content']
            record.save()
            msg = "update success!"
        else:            
            title = request.POST['title']
            content = request.POST['content']
            record = models.History.objects.create(title=title, content=content)
            record.save()
            msg = "insert success!"
    else:
        if actionType == "delete" and historyId > 0:
            record = models.History.objects.get(historyid=historyId)
            record.delete()
            msg = "delete success!"
        
    query = models.History.objects.all()
    data = query
       
    mainType = pageMainType[0]
    subType = pageSubType[mainType][2]
    menu = typeData
    subMenu = subTypeData.get(mainType)
    currentTypeName = pageTypeName[subType]
    return render(request, "backend_history.htm", locals())

def FeatureType(request, featureTypeId :int=0, actionType :str=None):
    if request.method == "POST":
        if actionType == "put" and featureTypeId > 0:
            record = models.FeatureType.objects.get(featuretypeid=featureTypeId)
            record.name = request.POST['name']
            record.chinese_name = request.POST['chineseName']
            record.enable = True if request.POST.get('enable') is not None and request.POST.get('enable').lower() == "true" else False
            record.save()
            msg = "update success!"
        else:                 
            name = request.POST['name']
            chinese_name = request.POST['chineseName']
            enable = True if request.POST.get('enable') is not None and request.POST.get('enable').lower() == "true" else False
            record = models.FeatureType.objects.create(name=name, chinese_name=chinese_name, enable=enable)
            record.save()
            msg = "insert success!"
    else:
        if actionType == "delete" and featureTypeId > 0:
            record = models.FeatureType.objects.get(featuretypeid=featureTypeId)
            record.delete()
            msg = "delete success!"
        
    query = models.FeatureType.objects.all()
    data = query 
       
    mainType = pageMainType[1]
    subType = pageSubType[mainType][0]
    menu = typeData
    subMenu = subTypeData.get(mainType) 
    currentTypeName = pageTypeName[subType]
    return render(request, "backend_featureType.htm", locals())
   

def FeatureInfo(request, featureInfoId :int=0, actionType :str=None):
    if request.method == "POST":
        if actionType == "put" and featureInfoId > 0:            
            record = models.FeatureInfo.objects.get(featureinfoid=featureInfoId)
            record.topic_id = eval(request.POST['topic'])
            record.title = request.POST['title']
            record.content = request.POST['content']
            record.save()
            msg = "update success!"
        else:
            topic = eval(request.POST['topic'])
            title = request.POST['title']
            content = request.POST['content']
            record = models.FeatureInfo.objects.create(topic_id=topic, title=title, content=content)
            record.save()
            msg = "insert success!"
    else:
        if actionType == "delete" and featureInfoId > 0:
            record = models.FeatureInfo.objects.get(featureinfoid=featureInfoId)
            record.delete()
            msg = "delete success!"  
    
    query = models.FeatureInfo.objects.all()
    query2 = models.FeatureType.objects.filter(enable=True)
    data = query
    topics = query2
       
    mainType = pageMainType[1]
    subType = pageSubType[mainType][1]
    menu = typeData
    subMenu = subTypeData.get(mainType)
    currentTypeName = pageTypeName[subType]
    return render(request, "backend_featureInfo.htm", locals())
    

def Category(request, categoryId :int=0, actionType :str=None):
    if request.method == "POST":
        if actionType == "put" and categoryId > 0:
            record = models.Category.objects.get(categoryid=categoryId)
            record.name = request.POST['name']
            record.enable = True if request.POST.get('enable') is not None and request.POST.get('enable').lower() == "true" else False
            record.save()
            msg = "update success!"
        else:                 
            name = request.POST['name']
            enable = True if request.POST.get('enable') is not None and request.POST.get('enable').lower() == "true" else False
            record = models.Category.objects.create(name=name, enable=enable)
            record.save()
            msg = "insert success!"
    else:
        if actionType == "delete" and categoryId > 0:
            record = models.Category.objects.get(categoryid=categoryId)
            record.delete()
            msg = "delete success!"
        
    query = models.Category.objects.all()
    data = query 
    
    mainType = pageMainType[2]
    subType = pageSubType[mainType][0]
    menu = typeData
    subMenu = subTypeData.get(mainType)
    currentTypeName = pageTypeName[subType]
    return render(request, "backend_category.htm", locals())

def Item(request, itemId :int=0, actionType :str=None):
    if request.method == "POST":
        if actionType == "put" and itemId > 0:            
            record = models.Item.objects.get(itemid=itemId)
            if request.FILES.get('image') and request.FILES.get('image').size() > 0 :                
                if record.imgpath != None:
                    __DeleteFile(record.imgpath)
                imgName = __SaveFile(request.FILES.get('image',''), request.POST['name'], ".webp")                
                record.imgPath = "/media/" + imgName
            else:
                record.imgpath = ""
            record.name = request.POST['name']
            record.dimension = request.POST['dimension']
            record.material = request.POST['material']
            record.info = request.POST['info']
            record.categoryid_id = request.POST['categoryid']
            record.save()
            msg = "update success!"
        else:           
           if request.FILES.get('image') and request.FILES.get('image').size() > 0:
               imgName = __SaveFile(request.FILES.get('image',''), request.POST['name'], ".webp")
               imgPath = "/media/" + imgName
           else:
               imgPath = ""
           name = request.POST['name']
           dimension = request.POST['dimension']
           material = request.POST['material']
           info = request.POST['dimension']
           categoryid = request.POST['categoryid']
           record = models.Item.objects.create(name=name, imgpath=imgPath, dimension=dimension, material=material, info=info, categoryid_id=categoryid)
           record.save()
           msg = "insert success!"
    else:
        if actionType == "delete" and itemId > 0:
            
            record = models.Item.objects.get(itemid=itemId)
            __DeleteFile(record.imgpath)
            record.delete()
            msg = "delete success!"
            
    query = models.Item.objects.all()
    query2 = models.Category.objects.filter(enable=True)   
    data = query
    topics = query2
       
    mainType = pageMainType[2]
    subType = pageSubType[mainType][1]
    menu = typeData
    subMenu = subTypeData.get(mainType)
    currentTypeName = pageTypeName[subType]
    return render(request, "backend_item.htm", locals())

def News(request, newsId :int=0, actionType :str=None):
    if request.method == "POST":
        if actionType == "put" and newsId > 0:            
            record = models.News.objects.get(newsid=newsId)
            record.title = request.POST['title']
            record.content = request.POST['content']
            record.save()
            msg = "update success!"
        else:
            title = request.POST['title']
            content = request.POST['content']
            record = models.News.objects.create(title=title, content=content)
            record.save()
            msg = "insert success!"
    else:
        if actionType == "delete" and newsId > 0:
            record = models.News.objects.get(newsid=newsId)
            record.delete()
            msg = "delete success!"

    
    query = models.News.objects.all()        
    data = query
       
    mainType = pageMainType[3]
    subType = pageSubType[mainType][0]
    menu = typeData
    subMenu = subTypeData.get(mainType)
    currentTypeName = pageTypeName[subType]
    return render(request, "backend_news.htm", locals())

def Faq(request, faqId :int=0, actionType :str=None):
    if request.method == "POST":
        if actionType == "put" and faqId > 0:              
            record = models.Faq.objects.get(faqid=faqId)
            record.question = request.POST['question']
            record.answer = request.POST['answer']
            record.save()
            msg = "update success!"
        else:
            question = request.POST['question']
            answer = request.POST['answer']
            record = models.Faq.objects.create(question=question, answer=answer)
            record.save()
            msg = "insert success!"
    else:
        if actionType == "delete" and faqId > 0:
            record = models.Faq.objects.get(faqid=faqId)
            record.delete()
            msg = "delete success!"

    query = models.Faq.objects.all()
    data = query
      
    mainType = pageMainType[4]
    subType = pageSubType[mainType][0]
    menu = typeData
    subMenu = subTypeData.get(mainType)
    currentTypeName = pageTypeName[subType]
    return render(request, "backend_faq.htm", locals())


def Downloads(request, downloadsId :int=0, actionType :str=None):
    if request.method == "POST":
        if actionType == "put" and downloadsId > 0:            
            record = models.Downloads.objects.get(downloadsid=downloadsId)
            if request.FILES.get('pdf') and request.FILES.get('pdf').size() > 0:                
                if record.filepath != None:
                    __DeleteFile(record.filepath)
                fileName = __SaveFile(request.FILES.get('pdf'), request.POST['name'], ".pdf")        
                record.filepath = "/media/" + fileName
                record.size = __fileSize(request.FILES.get('pdf','').size)             
            record.name = request.POST['name']            
            record.version = request.POST['version']
            record.info = request.POST['info']
            record.save()
            msg = "update success!"
        else: 
            fileName = __SaveFile(request.FILES.get('pdf',''), request.POST['name'], ".pdf")                
            filePath = "/media/" + fileName
            name = request.POST['name']
            size = __fileSize(request.FILES.get('pdf','').size)
            version = request.POST['version']
            info = request.POST['info']
            record = models.Downloads.objects.create(name=name, filepath=filePath, size=size, version=version, info=info)
            record.save()
            msg = "insert success!"
    else:
        if actionType == "delete" and downloadsId > 0:
            record = models.Downloads.objects.get(downloadsid=downloadsId)
            record.delete()
            msg = "delete success!"
            
    query = models.Downloads.objects.all()
    data = query
    
    mainType = pageMainType[5]
    subType = pageSubType[mainType][0]
    menu = typeData
    subMenu = subTypeData.get(mainType)  
    currentTypeName = pageTypeName[subType]    
    return render(request, "backend_downloads.htm", locals())    

def Company(request, actionType :str=None):
    if request.method == "POST":
        record = models.Company.objects.all().first()
        if actionType == "put":
            record.name = request.POST['name']
            record.email = request.POST['email']
            record.address = request.POST['address']
            record.phone = request.POST['phone']
            record.fax = request.POST['fax']
            record.servicetime = request.POST['servicetime']
            record.save()
            msg = "update success!"
        else:
            if not record:
                name = request.POST['name']
                email = request.POST['email']
                address = request.POST['address']
                phone = request.POST['phone']
                fax = request.POST['fax']
                servicetime = request.POST['servicetime']
                record = models.Company.objects.create(name=name, email=email, address=address, phone=phone, fax=fax, servicetime=servicetime)
                record.save()
                msg = "insert success!"
            else:
                msg = "company's data is exist"

    query = models.Company.objects.all().first()
    data = query
       
    mainType = pageMainType[6]
    subType = pageSubType[mainType][0]
    menu = typeData
    subMenu = subTypeData.get(mainType)
    currentTypeName = pageTypeName[subType]
    return render(request, "backend_company.htm", locals())
 

def GetForm(request, messageId :int=0, formId :int=0):
    if formId > 0:
        record = models.Message.objects.get(messageid=messageId)
        record.read = True
        record.save()
        record = models.Form.objects.get(formid = formId)
        record = model_to_dict(record)
        return JsonResponse(record)
    else:
        return JsonResponse(status=404)
    

def Message(request, messageId :int=0):
    if request.method == "POST" and messageId > 0:
        record = models.Message.objects.get(messageid=messageId)
        record.processed = True if request.POST.get('processed') is not None and request.POST.get('processed').lower() == "on" else False
        record.save()
        msg = "update success!" 
    
    data = models.Message.objects.all()
    
    mainType = pageMainType[6]
    subType = pageSubType[mainType][1]
    menu = typeData
    subMenu = subTypeData.get(mainType)
    currentTypeName = pageTypeName[subType]
    return render(request, "backend_message.htm", locals())


def changeIndex(request, mainType):
    if (pageSubType.get(mainType) != None and len(pageSubType.get(mainType)) > 0 and pageSubType.get(mainType)[0] != None):
        subType = pageSubType.get(mainType)[0]
        return redirect(f"/backend/{mainType}/{subType}/")
    else:
        return JsonResponse(status=404)

def __fileSize(fileByte):
    sizeType = ["B", "KB", "MB", "GB"]
    index = 0    
    while (fileByte >= 1024):
        index = index + 1
        fileByte = fileByte / 1024
    size = f"{fileByte:.2f} {sizeType[index]}"
    return size


def __SaveFile(file, name: str, fileFormat:str):
    fileName = datetime.now().strftime("%Y/%m/%d") +"_" + name
    fileName = hashlib.sha256(fileName.encode("utf-8")).hexdigest()[:10] + fileFormat
    fs = FileSystemStorage()
    return fs.save(fileName, file)

def __DeleteFile(filePath: str):
    filePath = filePath[1:]
    print("刪除檔案")
    print('目前目錄：', os.getcwd())
    print('檔案路徑：', os.path.abspath(filePath))
    if (os.path.exists(os.path.abspath(filePath))):    
        print("路徑正確")
        os.remove(os.path.abspath(filePath))
        checkFile = True
        print("刪除成功")
    else:
        checkFile = False
        print("刪除失敗")
    return checkFile