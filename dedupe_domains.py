import tldextract
 
deduped_urls = set({})
unique_domains = set({})
 
text_file = open(r"C:\GScraper\2015-08-03\Scrape\1million.txt", "r")
""" Logic 

"""
for url in text_file:
# extract the different parts of the urk
    domain = tldextract.extract(url.strip())
# combines the domain + the tld suffix
    domain_only = domain.domain+"."+domain.suffix
# checks if the domain is already stored in the variable
    if domain_only in unique_domains:
# if it is 'continue' skips the next part of logic and loads another url
        continue
    else:
# adds the domain to the variable
        unique_domains.add(domain_only)
# adds the url to the deduped urls variable
        deduped_urls.add(url.strip())
# Same as previous scripts   
text_file.close()
 
deduped_file = open(r"C:\GScraper\2015-08-03\Scrape\1million_deduped.txt", "w")
 
for url in deduped_urls:
    deduped_file.write(url.strip()+"\n")
     
deduped_file.close()