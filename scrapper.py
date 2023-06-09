import requests as r
import bs4
from pymaybe import maybe

from scrapperHeaderSetup import createHeader
from retrieveProductData import getProductData
from retrieveProductLinks import getLinks
rootUrl="https://www.amazon.in/"
searchParameterPrefix="s?k="
pageParameterPrefix="&page="


def scrape(searchProducts,maxProductsPerSearchTerm):
    searchProductsLength=len(searchProducts)
    retrievedProductLinks=set()
    i=0
    while(i<searchProductsLength):
        searchProduct=searchProducts[i]
        searchUrl=rootUrl+searchParameterPrefix+searchProduct
        searchHeader=createHeader()
        response=r.get(searchUrl,headers=searchHeader)
        # print(response.content)
        print(searchUrl)
        if(response.status_code==200):
            i+=1
            resHtml=response.content
            soupHtml=bs4.BeautifulSoup(resHtml,'html.parser')
            
            # * finding maxPages for the search Product
            maxSearchProductPages=maybe(soupHtml.find('span',{'class':"s-pagination-item s-pagination-disabled"})).text.strip().or_else(None)
            try:
                maxSearchProductPages=int(maxSearchProductPages)
            except:
                maxSearchProductPages=1
            print(searchProduct+" maxPagesAvailable:"+str(maxSearchProductPages))
            retrievedProductLinks=retrievedProductLinks.union(getLinks(maxSearchProductPages,searchUrl,maxProductsPerSearchTerm))
            # * getting product links by looping available pages
        else:
            print("response error for the product: "+searchProduct)

    retrievedProductLinksList=list(retrievedProductLinks)
    print(retrievedProductLinks)
    productData=[]
    tsize=len(retrievedProductLinksList)
    for plink in retrievedProductLinksList:
        print("product retrievals remaining: "+str(tsize-len(productData)))
        productData.append(getProductData("https://www.amazon.in"+plink))
    
    return productData
    # finding the total number of pages for the searchProduct



