import requests
from bs4 import BeautifulSoup
baseurl="https://www.holidify.com/country/india/places-to-visit.html"
page="?pageNum="
file=open("travel.txt","w")
for x in range(0,3,1):
    number=str(x)
    url=baseurl+page+number
    zomr=requests.get(url)
    print(zomr.status_code)
    zomsoup=BeautifulSoup(zomr.text,'html.parser')
    a=zomsoup.find_all('h2',class_="card-heading")
    des=zomsoup.find_all('p',{"class":"card-text"})

    #b=zomsoup.findAll('p',{"class":"card-text"})
    for (i,j) in zip(a,des):
        file.write(i.text+"-"+j.text)
        file.write("\n")

        print(i.text+"-"+j.text)
        print("\n")
    
file.close() 
      
        
