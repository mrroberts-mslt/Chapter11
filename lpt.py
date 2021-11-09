import csv
file = open("lpt.csv","r")
records = list(csv.reader(file))
file.close()
print("Property ID\t","Value\t","Address\t")
print("--------------------------------------------------------------------------")

for record in records[1:]:
    print (record[0],"\t\t", "€", record[1],"\t\t", record[2],"\t\t")
    
    
    


