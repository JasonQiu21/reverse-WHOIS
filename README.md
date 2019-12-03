# Reverse WHOIS lookup

## What's this?
This is a task for Google Code-in 2019-2020 for the Fedora Project. The tool uses [Mechanize](https://github.com/python-mechanize/mechanize) and [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to scrape [viewdns's](https://viewdns.info/reversewhois/) reverse WHOIS web tool to find what URLs are registered under a person or corporation.

## What's WHOIS?
From the [Wikipedia Article](https://en.wikipedia.org/wiki/WHOIS):
> WHOIS (pronounced as the phrase "who is") is a query and response protocol that is widely used for querying databases that store the registered users or assignees of an Internet resource, such as a domain name, an IP address block or an autonomous system, but is also used for a wider range of other information. The protocol stores and delivers database content in a human-readable format.

Basically, it stores who owns what IPs addresses and what domains (if any) they point to. You request information about the people/corporations (registrants) who registered that specific domain.

## What's reverse WHOIS?
The reverse of WHOIS. Instead of requesting a domain or IP address, you request a registrant, and you find what domains are registered under that registrant.