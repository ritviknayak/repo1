c = 62324783949134119159408816513334912534343517300880137691662780895409992760262021
n = 1280678415822214057864524798453297819181910621573945477544758171055968245116423923
e = 65537

p = 1899107986527483535344517113948531328331
q = 674357869540600933870145899564746495319033

t = (p-1)*(q-1)

# Compute the modular multiplicative inverse of e modulo t
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

d = modinv(e, t)

p = pow(c, d, n)
message_str = str(p)  # Convert the result to a string
message_ascii = bytearray.fromhex(hex(p)[2:]).decode('ascii')

print(message_ascii)
