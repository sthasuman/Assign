import csv

class VDC(object):
    def __init__(self, district, name, number ,pop_male,pop_female):
        self.district = district
        self.name = name
        self.number = number
        self.pop_male = pop_male
        self.pop_female = pop_female

    def __str__(self):
        return str("District: %s, Name: %s, Total_Households: %s, Male Population: %s, Female Population: %s, Total_population: %s " % (self.district , self.name , self.number , self.pop_male , self.pop_female , int(self.pop_male)+int(self.pop_female))) 

    
with open ('population.csv', "r") as file:
    reader = csv.reader(file)
    my_list = list(reader)
    

   
#Print the list
for i in range (1, len(my_list),3):
        new = VDC(my_list[i][0], my_list[i][1], my_list[i][3], my_list[i+1][3],my_list[i+2][3])
        if not my_list [i][3].isdigit():
            my_list[i+1] #skip the list if string in 4th column is not digit
        else:
            print (new) #print the list   

# User Input
def checkvdc(name):

    for i in range (1, len(my_list),3):
        if not my_list [i][3].isdigit():
            print ("Not Found")
            break
        else:
            new = VDC(my_list[i][0], my_list[i][1], my_list[i][3], my_list[i+1][3],my_list[i+2][3])
            if name.lower() == my_list[i][1].lower():
                return (new)
                
vdcname = input ("\nEnter the VDC name:")
print (checkvdc(vdcname))



        
