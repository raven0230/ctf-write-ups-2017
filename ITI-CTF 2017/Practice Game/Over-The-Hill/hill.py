alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789_{}"

inverted_matrix = [[31,44,13,33,47,24,12,21],
                   [37,22,19,37,40,1,59,55],
                   [45,59,63,4,27,63,20,50],
                   [44,10,0,9,11,1,14,16],
                   [54,47,14,7,31,25,48,48],
                   [39,2,56,48,38,27,48,34],
                   [38,1,12,40,40,13,34,5],
                   [27,22,5,21,22,20,7,59]]

ciphertext = "7Nv7}dI9hD9qGmP}CR_5wJDdkj4CKxd45rko1cj51DpHPnNDb__EXDotSRCP8ZCQ"

def mul(m1, m2):
    global alphabet
    size = len(alphabet)
    result = []
    for mat in m1:
        s = 0
        for i in range(0,len(mat)):
            s += mat[i]*m2[i]
        result.append(s%size)
    return result

def strToCode(s):
    global alphabet
    code = []
    for i in s:
        code.append(alphabet.find(i))
    return code

def codeToStr(c):
    global alphabet
    size = len(alphabet)
    s = ''
    for i in c:
        s += alphabet[round(i)%size]
    return s

def splitStr(s,size):
    return [ s[i:i+size] for i in range(0, len(s), size)]

def main():
    plaintext = ''
    for sub in splitStr(ciphertext,8):
        plaintext += codeToStr(mul(inverted_matrix,strToCode(sub)))
    print(plaintext)

main()
