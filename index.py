from scrapper import scrape
import pandas as pd
products=scrape(["smartPhone"],5)
df=pd.DataFrame(products,columns=["Title","Category","brand","Price","Ratings","Availability"])
df.to_csv(na_rep="null",index=False,path_or_buf="products.csv",sep=",")