# Γράψτε μια συνάρτηση σε Python η οποία υπολογίζει το ποσό πληρωμής
# όταν της περνάει ο χρήστης τις εγγραφές ενός λεξικού σε λίστα
# για το τι αγόρασε και το ποσοστό φόρου.
# Άσκηση 3,8,9,12
# list of numbers 
import csv

 # Function to print sum 
def returnSum(myDict, foros): 
    sum = 0
    for i in myDict: 
        #print (myDict[i])
        sum = sum + float(myDict[i])
    return sum *((100+foros)/100)

# Driver Function 
duck = {'a': 100, 'b':200, 'c':300,'eliza':0.15} 


reader = csv.reader(open('mock_data_dict.csv', 'r'))
mydict = {}
for row in reader:
   k, v = row
   mydict[k] = v

#for i in mydict:
#   print (i, mydict[i])


print("Sum :", returnSum(duck,24)) 
