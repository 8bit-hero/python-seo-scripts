keywords = open(r"Ckeywords.txt", "r")
kw = []
for keyword in keywords:
    kw.append(keyword)
keywords.close()
         
footprints = open(r"foot.txt", "r")
fp = []
for footprint in footprints:
    fp.append(footprint)
footprints.close()
     
keywords_and_footprints = open(r"combined.txt", "w")
 
for keyword in kw:
    for footprint in fp:
        # print keyword.strip()+" "+footprint.strip()
        keywords_and_footprints.write(keyword.strip()+" "+footprint.strip()+"\n")
keywords_and_footprints.close()