import random 

Caratteri = "qwertyuiopasdfghjklzxcvbnm,.;:-_òàùè+ç°§é*@#[]1234567890'ì!£$%&/()=?^€<>*-+."
passlength = int(input("inserisci la lunghezza della tua pswd (consigliato ~20):"))
Password = ("")
for i in range(passlength):
    Password += random.choice(Caratteri)
print("La tua password generata sicura è: ", end = " ")
print (Password)
