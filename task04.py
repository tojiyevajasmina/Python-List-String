

email = input("Email manzillarni vergul bilan kiriting: ")

l_email = email.split(",")


damens = []

for i in l_email:
    i = i.strip()   
    if "@" in i:      
        damen = i[i.find("@"):]  
        if damen not in damens:  
            damens.append(damen)


print(damens )

