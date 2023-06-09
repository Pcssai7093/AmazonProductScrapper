import requests as r
import bs4
# ignore if there is any error in the below line 
from pymaybe import maybe
from scrapperHeaderSetup import createHeader

def getProductData(url):
    data_fetched=False
    
    while(not data_fetched):
        searchHeader=createHeader()
        response=r.get(url,headers=searchHeader)
        if(response.status_code!=200):
            continue
        else:
            resHtml=response.content
            soup=bs4.BeautifulSoup(resHtml,'html.parser')
            if(soup.title.text=="Amazon.in"):
                continue
            title=maybe(soup.find('span',attrs={"id":"productTitle"})).text.strip().or_else(None)
            category=maybe(soup.find('div',attrs={"id":"nav-subnav"})).attrs['data-category'].or_else(None)
            brand=maybe(soup.find('div',attrs={"id":"productOverview_feature_div"})).find('span',attrs={"class":"a-size-base po-break-word"}).text.strip().or_else(None)
            if(brand!=None and len(brand)==0):
                brand=None
            price=maybe(soup.find('div',attrs={"id":"corePriceDisplay_desktop_feature_div"})).find('span',attrs={"class":"a-price-whole"}).text.replace(",","").strip().or_else(None)
            try:
                price=float(price) 
            except:
                price=None
            # price=float(price) if price!=None else None
            rating=(maybe(soup.find('span',attrs={"id":"acrPopover"})).find('span',attrs={"class":"a-size-base a-color-base"}).text.strip()).or_else(None)
            try:
                rating=float(rating) 
            except:
                rating=None
           
            availability_status=maybe(soup.find("div",attrs={"id":"availability"})).find("span").text.strip().or_else(None)
            if(availability_status!=None and len(availability_status)==0):
                availability_status=None
            data_fetched=True
            return [title,category,brand,price,rating,availability_status]
    return []

