import secrets

# List of characters for password
characters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9', '!','@','#','$','£','%','^','&','*','(',')','_','+','=','{','}','[',']','|',':',';','"','<','>','?','~','`','.','/']

def PassGen():
    
    # Create password list
    Password=[]
    
    # Generate password
    for n in range(10):
        Password.append(secrets.choice(characters))
    
    # Create text file for password
    textfile=open('/opt/PassGen/src/Password.txt', 'w', encoding='utf-8')
    textfile.write('Password =  \n')
    textfile.write('\n')
    
    # Enter password into text file and save file
    for element in Password:
        textfile.write(element)
    textfile.write('\n')
    textfile.write('\n')
    textfile.write('IMPORTANT - This will be erased in 30 minutes.')
    textfile.close()

# Run password generator
PassGen()
