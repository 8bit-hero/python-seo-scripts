import glob
first_scrape_set = set({})
first_scrape_file = open(r"C:\GScraper\2015-08-03\Scrape\first_scrape_demo.txt", "r")
second_scrape_files = glob.glob(r"C:\GScraper\2015-08-03\Scrape\demo*.txt")
new_urls_file = open(r"C:\GScraper\2015-08-03\Scrape\only_new_urls.txt", "w")
for url in first_scrape_file:
    first_scrape_set.add(url.strip())
for file in second_scrape_files:
    open_file = open(file, "r")
    for url in open_file:
        if url.strip() in first_scrape_set:
            continue
        else:
            new_urls_file.write(url.strip()+"\n")
first_scrape_file.close()
# second_scrape_file.close()
new_urls_file.close()