import requests
from bs4 import BeautifulSoup

url = "https://www.crimemapping.com/Print?dteFrom=4-10-2023&dteTo=4-16-2023&attr=[%221%22,%222%22,%223%22,%224%22,%225%22,%226%22,%227%22,%228%22,%229%22,%2210%22,%2211%22,%2212%22,%2213%22,%2214%22,%2215%22]&ext={%22type%22:%22extent%22,%22xmin%22:-13173275.399040008,%22ymin%22:4025434.7964986674,%22xmax%22:-13146751.750225088,%22ymax%22:4038199.7802222744,%22spatialReference%22:{%22wkid%22:102100},%22cache%22:{%22_parts%22:[{%22extent%22:{%22type%22:%22extent%22,%22xmin%22:-13173275.399040008,%22ymin%22:4025434.7964986674,%22xmax%22:-13146751.750225088,%22ymax%22:4038199.7802222744,%22spatialReference%22:{%22wkid%22:102100}},%22frameIds%22:[0]}]}}&tmpfilt={%22PreviousID%22:3,%22PreviousNumDays%22:7,%22PreviousName%22:%22Previous%20Week%22,%22FilterType%22:%22Previous%22,%22ExplicitStartDate%22:%2220230410%22,%22ExplicitEndDate%22:%2220230416%22}&agfilt=[]&bmpid=1&disacpt=false"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

data_list = []


for tr in soup.find_all("tr", {"class": "k-alt"}):
    incident = {}
    incident["description"] = tr.find("td", role="gridcell").get_text().strip()
    incident["incident_number"] = (
        tr.find_all("td", role="gridcell")[1].get_text().strip()
    )
    incident["location"] = tr.find_all("td", role="gridcell")[2].get_text().strip()
    incident["agency"] = tr.find_all("td", role="gridcell")[3].get_text().strip()
    incident["date"] = tr.find_all("td", role="gridcell")[4].get_text().strip()
    data_list.append(incident)

for incident in data_list:
    print("Description:", incident["description"])
    print("Incident Number:", incident["incident_number"])
    print("Location:", incident["location"])
    print("Agency:", incident["agency"])
    print("Date:", incident["date"])
    print("---")
