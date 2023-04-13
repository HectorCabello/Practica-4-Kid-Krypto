import fileinput

# This function reads the file and returns a list with the lines
lines = []
for line in fileinput.input():
    lines.append(line.rstrip('\n'))

def calculateFactors(input):
    a,b,A,B = int(input[0]),int(input[1]),int(input[2]),int(input[3])
    M = a*b - 1
    e = A*M + a
    d = B*M + b
    n = int((e*d - 1)/M)
    #print(f"M={M}, e={e}, d={d}, n={n}")
    return [M,e,d,n]

def encrypt(input,message):
    #print("Encrypt",input)
    #input: a,b,A,B
    M,e,d,n = calculateFactors(input)
    #print(f"M={M}, e={e}, d={d}, n={n}")
    ciferText = message * e % n
    print(ciferText)

def decrypt(input,ciferText):
    #print("Decrypt",input)
    #input: a,b,A,B
    M,e,d,n = calculateFactors(input)
    #print(f"M={M}, e={e}, d={d}, n={n}")
    plainText = ciferText * d % n
    print(plainText)

# This function read the first element of the list and chose which function to call, ecrypt or decrypt
def encryptOrDecrypt():
    if lines[0] == "E":
        encrypt(lines[1:],int(lines[-1]))
    elif lines[0] == "D":
        decrypt(lines[1:],int(lines[-1]))
    else:
        print("Error, first line must be E or D")

encryptOrDecrypt()