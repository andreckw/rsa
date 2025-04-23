from random import randint, choice
from math import gcd

class RSA():
    
    p = 0
    q = 0
    totiente_n = 0
    n = 0
    e = 2
    d = 2
    testar = False
    texto_criptografado = False
        
    
    def criptografar(self, texto, testar = False):
        self.testar = testar
        primos = self._gerarprimos()
        self.p = choice(primos)
        while not self._isprimo(self.p):
            self.p = choice(primos)
        
        self.q = choice(primos)
        while not self._isprimo(self.q) and self.q == self.p:
            self.q = choice(primos)
        
        if self.testar:
            self.p = 7
            self.q = 11
        self.totiente_n = (self.p - 1) * (self.q - 1)
        self.n = self.p * self.q
        
        while 1 < gcd(self.e, self.totiente_n) and self.e < self.totiente_n:
            self.e += 1
        
        while ((self.d * self.e) % self.totiente_n != 1) and self.d < self.totiente_n:
            self.d += 1
        
        ascii = self._transformar_em_ascii(texto)
        retorno = ""
        
        for a in ascii:
            retorno += str((a ** self.e) % self.n)
        
        self.texto_criptografado = retorno
        
        self._gerar_arquivo_params()
        return retorno
    
    
    def descriptografar(self, texto, d, n):
        
        for i in texto:
            print(bin(int(i)))
                
    
    
    def _transformar_em_ascii(self, texto):
        texto_bytes = ""
        if (type(texto) == bytes):
            texto_bytes = bytearray(texto)
        else:
            texto_bytes = bytearray(texto, encoding="utf-8")
        
        retorno = []
        for a in texto_bytes:
            retorno.append(int(a))
        
        return retorno
            
        
    
    def _gerarprimos(self):
        x = 2
        y = randint(2, 55001)
        retorno = []
        
        for i in range(x-1, y):
            if self._isprimo(i):
                retorno.append(i)
        
        return retorno
    
    
    def _isprimo(self, num):
        retorno = True
        for divisor in range(1, num):
            if num % divisor == 0 and divisor != 1:
                retorno = False
                break
        
        return retorno

    
    def _gerar_arquivo_params(self):
        
        with open("chaves.txt", "w") as c:
            c.write(f"p = {self.p}\n")
            c.write(f"q = {self.q}\n")
            c.write(f"totiente_n = {self.totiente_n}\n")
            c.write(f"n = {self.n}\n")
            c.write(f"e = {self.e}\n")
            c.write(f"d = {self.d}\n")
        
    


if __name__ == "__main__":
    rsa = RSA()
    print(rsa.criptografar("teste", True))
    print(rsa.descriptografar("747337473", 43, 77))