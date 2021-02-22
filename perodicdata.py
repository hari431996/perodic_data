'''
Below are the steps used to generate the code.
1). During the inspection of the website i found that each element had its own source website, hence it had to be scraped individaully
    so first all the urls had been generated, they were saved in the url file.

2). Then the urls page has been read and using requests module we open the element web page.

3). Then the source is downloaded and parsed using the beautifulsoup module.


'''
#Import libraries
import requests
from bs4 import BeautifulSoup
import csv 

"""
the below code generates all the url of elements
"""
"""
page = requests.get("http://www.mrl.ucsb.edu/~seshadri/Periodic/periodic.html")
soup = fd(page.content,"html.parser")
d = soup.find_all('a', {'target':'ELEM'})
i = 0
f = open("/Users/shreehariboyalla/Desktop/perodic_urls","w")
s = " "
for row in d:
    s = row.text
    if s[0] == ' ':
        s = s[1]
    f.write("http://www.mrl.ucsb.edu/~seshadri/Periodic/Elements/"+s+".html"+"\n")
f.close()
#Request URL
"""
"""
#below code creates a csv file with headers
k = 0
headers = ["Element",'Charge','Spin','Radius']
f = open("/Users/shreehariboyalla/Desktop/periodic_data.csv","w")
csvwriter = csv.writer(f)
csvwriter.writerow(headers)
k = []
z = []
"""
with open("/Users/shreehariboyalla/Desktop/perodic_urls") as fd: #open the file containing urls
    for line in fd:
        l = line.split()
        page = requests.get(l[0])   #open the webpage using url
        #Fetch webpage
        soup = BeautifulSoup(page.content,"html.parser")    #parse the webpage
        ti = soup.find('h2')
        l = []
        table = soup.findAll('table')
        for data in table[0].findAll('td'):
                l.append(data.text)
        charge = ' '
        for i in range(1,len(l)+1):
            if i%4 ==0:
                print(l[i-1], end= " ")
                print("\n")
            else:
                if (i-1)%4 == 0 and l[i-1] == '':
                    print(ti.text,charge , end = ' ')
                else:
                    if len(l[i-1]) > 0 and (l[i-1][0] == "+" or l[i-1][0] == "-"):
                        charge = l[i-1]
                        print(ti.text,"",l[i-1], end= " ")
                    else:
                        print(l[i-1], end = " ")