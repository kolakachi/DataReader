import csv

Result = []
Counter = 0
FileToRead = open('slatecode test.csv','rU')
FileReader = csv.reader(FileToRead)
for Row in FileReader:
    Result.append(Row[Counter])    
    print (Row[Counter])
    Counter+=1
        
del(Counter)
