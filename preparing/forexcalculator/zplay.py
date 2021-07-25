# from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# r = requests.get("https://www.forexfactory.com/calendar.php?week=jul18.2021")
# r = requests.get("https://www.investing.com/economic-calendar/")
def getEconomicCalendar(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    print(response.status)
    # soup = BeautifulSoup(response.data)
    # print(soup)


# url = "https://www.fxstreet.com/economic-calendar"
url = "https://www.forexfactory.com/calendar.php?week=jul18.2021"
getEconomicCalendar(url)
