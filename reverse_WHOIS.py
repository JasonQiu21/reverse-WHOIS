import mechanize
from bs4 import BeautifulSoup

#open viewdns.info/reversewhois/ and fill out the form with our registrant
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [("User-agent", "Mozilla/5.0")]
br.open("https://viewdns.info/reversewhois/")
br.select_form(name="reversewhois")
registrant = input("Registrant Name or Email Address:    ")
br["q"] = registrant
response = br.submit()

#find the table we need (with all the URLs of the registrant)
bs = BeautifulSoup(response.read(), features="lxml")
table = bs.findAll(lambda tag: tag.name=='table')[2]

#print everything out
rows = table.findAll(lambda tag: tag.name=='tr')
print(f"All URLs registered by {registrant}:")
for i in rows[4:-1]:
    url = i.find('td')
    print(url.get_text())