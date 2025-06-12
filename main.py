# Kodni bu yerga yozing

from random import randint

menu = '''
===== Loop Lab: Interaktiv Topshiriqlar =====
1. 🎯 Maxfiy sonni toping (Random son o'yini)
2. 🔄 So'zni teskari yozish
3. 🔢 Sonlar orasidagi eng kichigini topish
4. 🧮 FizzBuzz o'yini (1 dan N gacha)
0. ❌ Dasturdan chiqish
============================================= 
'''
while True:
    print(menu)
    
    choise = int(input("Tanlang: "))

    if choise == 1:
            number = randint(1000,9999)
            count = 0

            while count < 7 :
                count += 1
                num = int(input("Sonni kiriting: "))
            if num > number :
                print( "Juda katta son!")
            if num < number :
                print("Juda kichik son!")
            if num == number :
                print("Tabriklaymiz, topdingiz!")
                break
            else :
                print("Topolmadingiz!",number)
    elif choise == 2:
        
        text = input("Matnni kiriting: ")
        x = ""
        for i in text :
            x = i + x


        print("Teskarisi:",x)
    elif choise == 3:
       
        min_son = int(input("Sonni kiriting: "))

        for i in range(min_son) :
            min_son = None 
            
            for i in range(5):
                son = float(input(f"{i+1}-sonni kiriting: "))
                        
                if min_son is None or son < min_son:
                    min_son = son

                print("Eng kichik son:", min_son)
            else:
                print("Urunishlar tugadi!",min_son)
    elif choise == 4:
        
        number = int(input("Sonni kiriting: "))

        for i in range(1,number+1):
            
            if i % 3 == 0 and i % 5 == 0 :
                print("FizzBuzz",i)
            
            elif i % 3 == 0 :
                print("Fizz",i)
                
            elif i % 5 == 0 :
                print("Buzz",i)
            
            else:
                print(i)
    elif choise == 0:
        print("Dastur to'xtadi!?")
    else:
        print("Siz noto'g'ri menyudasiz!")
