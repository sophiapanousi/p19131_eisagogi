

a= abs(int(input ("Δώστε έναν αριθμό : ")))
#διάβασε έναν ακέραιο από το πληκτρολόγιο και κράτα απόλυτη τιμη

while a > 9 :#or a < -9 :
    a= 3 * a + 1
    k=0
    print ('Ο αριθμός είναι αυτή τη στιγμή :',a)
    while a != 0 :
        k=a % 10 + k
        print ('Tο κκε ειναι εδώ ενωμένο δυνατό :',k)
        a= a // 10 
      #  return k
    a= k
    #return a

