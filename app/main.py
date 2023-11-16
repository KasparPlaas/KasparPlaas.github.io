# Kaspar Plaas
# 16.11.2023

from fastapi import FastAPI

app = FastAPI()

@app.get("/mang")
def mang(sona):
    arvatud_tahed = []
    elud = 5
    
    while elud > 0:
        kaotatud = 0
        
        for taht in sona:
            if taht in arvatud_tahed:
                print(taht, end=" ")
            else:
                print("_", end=" ")
                kaotatud += 1
                
        if kaotatud == 0:
            print("\nÕnnitleme, võitsid!")
            break
        
        arvamus = input("\nArva täht: ").lower()
        
        arvatud_tahed.append(arvamus)
        
        if arvamus not in sona:
            elud -= 1
            print("Vale arvamine. Elusid jäänud:", elud)
            if elud == 0:
                print("Kahjuks, kaotasid. Õige sõna oli:", sona)

# Sõna, mida mängitakse
sona = "It is very fun"

# Mängu käivitamine
mang(sona.lower())
