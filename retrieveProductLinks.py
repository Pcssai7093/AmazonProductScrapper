import requests as r
import bs4
# ignore if there is any error in the below line 
from pymaybe import maybe
from scrapperHeaderSetup import createHeader
pageParameterPrefix="&page="

def getLinks(maxPages,prefixUrl,maxProductsPerSearchTerm):
    productLinks=set()
    i=0

    while(i<maxPages):
        url=prefixUrl+pageParameterPrefix+str(i+1)
        searchHeader=createHeader()  
        response=r.get(url,headers=searchHeader)
        if(response.status_code==200):
            i+=1
            resHtml=response.content
            soupHtml=bs4.BeautifulSoup(resHtml,'html.parser')
            productLinkTags=soupHtml.find_all('a',{"class":"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
            for a in productLinkTags:
                productLinks.add(a.get("href"))
                if(len(productLinks)>=maxProductsPerSearchTerm):
                    return productLinks
        else:
            pass
    print("total product links retrieved: "+str(len(productLinks)))
    return productLinks
            