# Over The Hill

**Type:** Crypto

**Points:** 60

**Description:**

>Over the hills and far away,many times I've gazed, many times been bitten. Many dreams come true and some have silver linings, I live for my dream of a decrypted [flag.file](over-crpyted)

## Write-up

This is Hill cipher.
To decrpyt the ciphertext, first we use an [online calculator](https://planetcalc.com/3324/) to calculate the inverse of the key matrix with modulo 64.
```
matrix = [[54, 53, 28, 20, 54, 15, 12, 7],
          [32, 14, 24, 5, 63, 12, 50, 52],
          [63, 59, 40, 18, 55, 33, 17, 3],
          [63, 34, 5, 4, 56, 10, 53, 16],
          [35, 43, 45, 53, 12, 42, 35, 37],
          [20, 59, 42, 10, 46, 56, 12, 61],
          [26, 39, 27, 59, 44, 54, 23, 56],
          [32, 31, 56, 47, 31, 2, 29, 41]]
          
inverted_matrix = [[31,44,13,33,47,24,12,21],
                   [37,22,19,37,40,1,59,55],
                   [45,59,63,4,27,63,20,50],
                   [44,10,0,9,11,1,14,16],
                   [54,47,14,7,31,25,48,48],
                   [39,2,56,48,38,27,48,34],
                   [38,1,12,40,40,13,34,5],
                   [27,22,5,21,22,20,7,59]]
```

Then we put the inverted_matrix into our own [decrpyting program](hill.py)

```
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
```

## Flag
IceCTF{linear_algebra_plus_led_zeppelin_are_a_beautiful_m1xture}
