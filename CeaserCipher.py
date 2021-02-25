import io
import re
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def student_Data(f,student_ID,student_name,student_age):
    f.write(student_ID)
    f.write('\n')
    f.write(student_name)
    f.write('\n')
    f.write(str(student_age))
    f.close()

def reading_Student_data(filename):
    f2= open(filename, "r")
    reading=f2.read()
    print("Data From File",reading)

def Genrating_Key(SID,age,string_ID,student_name): 
   
    sum = int(0) 
    while (SID != 0): 
          sum = sum + int(SID % 10) 
          SID = int(SID/10)      
    sum_of_SID=sum
    second_sum = sum_of_SID % age
    if second_sum==0:
        shiftdigit=string_ID[len(string_ID)-1:]
        remaindigit=string_ID[:len(string_ID)-1]
        shift_result=shiftdigit+remaindigit
        print(shift_result)
    else:
        if second_sum > 9:
            second_sum=second_sum-10

        shiftdigit=string_ID[:second_sum]
        remaindigit=string_ID[second_sum:]
        shift_result=remaindigit+shiftdigit
    
    final_encryption_key=str(shift_result)+str(age)+str(len(student_name))
    key_file=open("mykey.txt",'w')
    key_file.write(final_encryption_key)
    key_file.close()

def AVG_Key():

    mykeyfile=io.open("mykey.txt","r")
    key_text=mykeyfile.read()
    lengthofkey=len(key_text)
    key_text=int(key_text)
    key_sum = int(0) 
    while (key_text != 0): 
          key_sum = key_sum + int(key_text % 10) 
          key_text = int(key_text/10)      
    sum_of_Key=key_sum


    average_of_key = sum_of_Key/lengthofkey
    AVG_Key.shifting_value = round(average_of_key)

    print("Shift Cipher Key Value ::   ",AVG_Key.shifting_value)

def encryption(string,c_type):

    shift = AVG_Key.shifting_value
    cipher = ''
    for student_name in string: 
        if c_type == "left":

            if student_name == ' ':
                cipher = cipher + student_name
            elif  student_name.isupper():
                cipher = cipher + chr((ord(student_name) - shift - 65) % 26 + 65)
            
            else:
                cipher = cipher + chr((ord(student_name) - shift - 97) % 26 + 97)

            cipher_file = open("Orignal.txt","w")
            cipher_file.write(cipher)

           




            

        elif c_type== 'right':

            if student_name == ' ':
                cipher = cipher + student_name
            elif  student_name.isupper():
                cipher = cipher + chr((ord(student_name) + shift - 65) % 26 + 65)
            
            else:
                cipher = cipher + chr((ord(student_name) + shift - 97) % 26 + 97)

            cipher_file = open("cipher.txt","w")
            cipher_file.write(cipher)

    if c_type== 'right':
        print("Now Cipher Text  is ::  ",str(cipher))
    elif c_type=='left':
        print("Now After Decryption Text  is ::  ",str(cipher))
    
def final_cipher():
    c_f=open("cipher.txt",'r')
    cipher=c_f.read()
    k_f=open("mykey.txt","r")
    key=k_f.read()
    # c = "".join(map(lambda x,y: x+y, cipher, key))
    leng_cipher=len(cipher)
    leng_key=len(key)
    if leng_cipher > leng_key :
        c = "".join(map(lambda x,y: x+y, cipher, key))
        a=cipher[leng_key:]    
        final_cipher=c+a
        n_c_f=open("cipher.txt","w")
        n_c_f.write(final_cipher)

        # print(final_cipher)
    elif leng_key>leng_cipher:
        c = "".join(map(lambda x,y: x+y, cipher, key))
        a=key[leng_cipher:]    
        final_cipher=c+a
        n_c_f=open("cipher.txt","w")
        n_c_f.write(final_cipher)

    elif leng_key==leng_cipher:
        final_cipher = "".join(map(lambda x,y: x+y, cipher, key))
        n_c_f=open("cipher.txt","w")
        n_c_f.write(final_cipher)
    else:
        pass
    print("Now Final Cipher Text  is ::  ",str(final_cipher))
    
def finalDecryption():
    c_f=open("cipher.txt",'r')
    cipher=c_f.read()
    k_f=open("mykey.txt","r")
    key=k_f.read()

    for i in key:
        cipher = re.sub(i,"",cipher)
    print("Key removed:", cipher)

    f_d_c=open("Orignal.txt","w")
    f_d_c.write(cipher)

if __name__ == "__main__":
   

    print(Fore.GREEN+"\n  ================================================================================================================")
    print(Fore.GREEN+"\n  ================================================================================================================")
    print(Fore.GREEN+"  ==========================CUSTOMIZED CEASAR ENCRYPTION/DECRYPTION METHOD========================================")
    print(Fore.GREEN+"  ================================================================================================================")
    print(Fore.GREEN+"  ================================================================================================================")
    print(Fore.GREEN+"  =========================================MAIN MENU==============================================================")
    print(Fore.GREEN+"  ================================================================================================================\n")
    print(Fore.YELLOW+'\n  NOTE :: You Have To Enter The Text In Orignal.txt File For Encryption ')
    user_input = input("\n========================= Select an option[E]=Encryption  [D]=Decryption [e] = Exit=============================\n")
    if user_input == 'E':
    
        student_ID = input(Fore.MAGENTA+"Enter Your ID :: ")
        SID=int(student_ID)

        string_ID=str(student_ID)
    
        filename = "%s.txt" % student_ID
    
        f=open(filename,"w")
    
        student_name = input("Enter Your Full Name :: ")


    
        student_age = input("Enter Your Age :: ")
        
        student_age=int(student_age)
    
        student_Data(f,student_ID,student_name,student_age,)

        reading_Student_data(filename)
        
        Genrating_Key(SID,student_age,string_ID,student_name)

        AVG_Key()

        shift = AVG_Key.shifting_value

        

        plain_file= open('plaintext.txt','r')
        text=plain_file.read()

        c_type='right'
        encryption(text,c_type)
        final_cipher()
        

    elif user_input== 'D':
        finalDecryption()
            

        read_f=open("Orignal.txt","r")
        encrypted_text = read_f.read()

        AVG_Key()
        shift = AVG_Key.shifting_value-1

        c_type='left'
        encryption(encrypted_text,c_type)
        



    elif user_input=='e':
        print(" =========================Exit=============================")
        exit()

    else:
        print("You Have Enter Wrong Input Try Again")

