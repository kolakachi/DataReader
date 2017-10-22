import csv

Counter = 0
FileToRead = open('slatecode test.csv','rU')
FileReader = csv.reader(FileToRead)
for Row in FileReader:
        
    print (Row[Counter])
    Counter+=1
        
del(Counter)
