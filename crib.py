#own plain text M1, M2 and k has been set up

plaintext1 = "i have a cats"
plaintext2 = "there you are"
k          = "mAgnIficIenT@"


BITS = ('0', '1')
ASCII_BITS = 7

def display_bits(b):
    """converts list of {0, 1}* to string"""
    return ''.join([BITS[e] for e in b])

def seq_to_bits(seq):
    return [0 if b == '0' else 1 for b in seq]

def pad_bits(bits, pad):
    """pads seq with leading 0s up to length pad"""
    assert len(bits) <= pad
    return [0] * (pad - len(bits)) + bits
        
def convert_to_bits(n):
    """converts an integer `n` to bit array"""
    result = []
    if n == 0:
        return [0]
    while n > 0:
        result = [(n % 2)] + result
        n = int(n / 2)
    return result

def string_to_bits(s):
    def chr_to_bit(c):
        return pad_bits(convert_to_bits(ord(c)), ASCII_BITS)
    return [b for group in 
            map(chr_to_bit, s)
            for b in group]

def bits_to_char(b):
    assert len(b) == ASCII_BITS
    value = 0
    for e in b:
        value = (value * 2) + e
    return chr(value)

def list_to_string(p):
    return ''.join(p)

def bits_to_string(b):
    return ''.join([bits_to_char(b[i:i + ASCII_BITS]) 
                    for i in range(0, len(b), ASCII_BITS)])
    
def otp(m, k):
    assert len(m) == len(k)
    return[( mm+ kk) % 2 for mm, kk in zip(m, k)]
    


def XOR(C1, C2):
    C3 = ''
    for i in range(len(C1)):
        if C1[i] == C2[i]:
            C3 += '0'
        else:
            C3 += '1'
    return C3

def crib_drag(word, C3):

    w_b = string_to_bits(word)
    w_s = ''
    for i in w_b:
        w_s += str(i)
    for i in range(len(C3)-len(w_s)+1):
        p_b = XOR(C3[i:i+len(w_s)],w_s)
        p_b = [int(x) for x in p_b]
        p_t = bits_to_string(p_b)
        part = p_t.replace(' ','')
        print (p_t)
        


C1 = otp(string_to_bits(plaintext1), string_to_bits(k) )
C2 = otp(string_to_bits(plaintext2), string_to_bits(k) )
C3 = XOR(C1, C2)


print ("Key is    : " + display_bits(string_to_bits(k)))

print ("M1 is     : " + display_bits(string_to_bits(plaintext1)))
print ("C1 is     : " + display_bits((C1)))

print ("\n")

print ("M2 is     : " + display_bits(string_to_bits(plaintext2)))
print ("C2 is     : " + display_bits((C2)))

print ("\n")

print ("C1 is     : " + display_bits((C1)))
print ("C2 is     : " + display_bits((C2)))
print ("C3 is     : " + (C3))




print ("\n")


while (True):

        j = len(C3)/7

        print ("Length of text : ", j )
        print ("Crib words = ") 

        y = input()

        print ("\n")

        x = crib_drag(y, C3)

        print ("\n")