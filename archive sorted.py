import csv 
savedata=[]
with open("archive_dataset.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        savedata.append(row)

header=savedata[0]
planetdata=savedata[1:]

for k in planetdata:
    k[2]=k[2].lower()

planetdata.sort(key=lambda planetdata:planetdata[2])

with open("Archivedatasetsorted.csv","a+")as f:
     csvwriter=csv.writer(f)
     csvwriter.writerow(header)
     csvwriter.writerows(planetdata)

with open("Archivedatasetsorted.csv")as input, open("Archiveset.csv","w", newline="")as output:
     writer=csv.writer(output)
     for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)