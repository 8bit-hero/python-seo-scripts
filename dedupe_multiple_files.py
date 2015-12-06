import glob
# sets the variable and the set
unique_urls = set({})
# defines the variable and via glob, loads all txt files in directory 
multiple_files = glob.glob(r"C:\GScraper\2015-08-06\Scrape\*.txt")
# loop to read each url in each file and strip	
for file in multiple_files:
    open_file = open(file, "r")
    for url in open_file:
        unique_urls.add(url.strip())
    open_file.close()
# opens file to write urls to
deduped_file = open(r"C:\GScraper\2015-08-03\Scrape\random_files_deduped.txt", "w")
# loop to write urls to file
for url in unique_urls:
    deduped_file.write(url.strip()+"\n")
# closes file    
deduped_file.close()