#defines the variable and the set
#sets can not contain duplicate entries
deduped_urls = set({})
#opens the scrape file as a read only file as "text_file"
text_file = open(r"C:\GScraper\2015-08-03\Scrape\1million.txt", "r")

#loop each url in the textfile
for url in text_file:
#adds the scrape file from var deduped_urls to text_file
#this filters the urls and url.strip cleans them up
    deduped_urls.add(url.strip())
    

#closes the text file to prevent memory leaks    
text_file.close()
#opens the file to be written
deduped_file = open(r"C:\GScraper\2015-08-03\Scrape\1million_deduped.txt", "w")
#writes the filtered urls to file and stipes and adds a new line after each
for url in deduped_urls:
    deduped_file.write(url.strip()+"\n")
#closes the file   
deduped_file.close()