--Ejercicio 1

fib :: Integer -> Integer
fib 0 = 0
fib 1 = 1
fib n | n>=2 = (fib (n-1)) + (fib (n-2))
      | otherwise = undefined

--Ejercicio 2

parteEntera :: Float -> Integer
parteEntera q | q>=0 && q<1 = 0
              | q<0 && q>(-1) = 0
              | q<(-1) = parteEntera(q+1) - 1
              | otherwise= parteEntera(q-1) +1

--Ejercicio 3

esDivisible :: Integer -> Integer -> Bool
esDivisible a b | a == 0 = True
                | a < b = False
                | a == b = True
                | otherwise = esDivisible (a-b) b

--Ejercicio 4 

sumaImpares :: Integer -> Integer
sumaImpares n | mod n 2 == 0 = sumaImpares(n-1)
              | mod n 2 /= 0 = n + sumaImpares(n-2)
--Ejercicio 7
tDI :: Integer -> Bool
tDI n | n>0 && n<10 = True
      | otherwise = ultimoDigito (n)== ultimoDigito(sacarUltimo n) && tDI (sacarUltimo n)

ultimoDigito :: Integer -> Integer
ultimoDigito n = mod n 10

sacarUltimo :: Integer -> Integer
sacarUltimo n = div n 10

inesimoDigito :: Integer -> Integer -> Integer
inesimoDigito n i | i> cD n = undefined
                  | i == cD n = mod n 10
                  | otherwise = inesimoDigito (sacarUltimo n) i

cD :: Integer -> Integer
cD n | n<10 = 1
     | otherwise = 1 + cD (div n 10)
                         