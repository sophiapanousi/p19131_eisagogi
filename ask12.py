#Γράψτε ένα πρόγραμμα σε Python το οποίο παίρνει μια ημερομηνία σε μορφή ΗΗ/ΜΜ/ΕΕΕΕ και
#εμφανίζει πόσες μέρες/ώρες/δευτερόλεπτα απέχει αυτή από την τρέχουσα ημερομηνία του
# υπολογιστή, καθώς και πόσες ημέρες έχει ο μήνας εκείνης της ημερομηνίας. Η ώρα για την
# ημερομηνία που παίρνετε σαν είσοδο από τον χρήστη είναι η ίδια με αυτήν του συστήματος,
# άρα δεν χρειάζεται ο χρήστης να δηλώσει την ώρα.


from datetime import datetime
def GetUserDate():
    isValid=False
    while not isValid:
        userIn = input("Δώστε μια ημερομηνία στη μορφή ηη/μμ/εεεε: ")
        try:             
            d = datetime.strptime(userIn, "%d/%m/%Y")
            isValid=True            
        except:
            print ("Που είσαι τέρμα ηλ; \n")
    return d

def convert_timedelta(duration):
    days, seconds = duration.days, duration.seconds
    #print (days)
    #print(seconds)
    minutes = (seconds) // 3600
    hours = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return days, hours, minutes, seconds




user_date=GetUserDate()
cur_date = datetime.now()
print(user_date)
print(cur_date)
#print(abs((user_date - cur_date).days))
td=abs(user_date - cur_date)
print(td)
#td = datetime.timedelta(2, 7743, 12345)
days, hours, minutes, seconds = convert_timedelta(td)
#days, hours, minutes, seconds = seconds_to_dhms(td.seconds)
print ('Έχουν μεσολαβήσει {} ημέρες, {} ώρες, {} λεπτά, {} δευτερόλεπτα'.format(days, minutes, hours,seconds))
print("από την τελευταία φορά που έκανα σεξ.")

