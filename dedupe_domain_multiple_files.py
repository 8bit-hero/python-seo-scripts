import glob
import tldextract
 
unique_urls = set({})
unique_domains = set({})
 
multiple_files = glob.glob(r"C:\GScraper\2015-08-03\Scrape\*.txt")
 
for file in multiple_files:
    open_file = open(file, "r")
    for url in open_file:
        domain = tldextract.extract(url.strip())
        domain_only = domain.domain+"."+domain.suffix
        if domain_only in unique_domains:
            continue
        else:
            unique_domains.add(domain_only)
            unique_urls.add(url.strip())
    open_file.close()
     
deduped_file = open(r"C:\GScraper\2015-08-03\Scrape\1million_deduped.txt", "w")
 
for url in unique_urls:
    deduped_file.write(url.strip()+"\n")
     
deduped_file.close()