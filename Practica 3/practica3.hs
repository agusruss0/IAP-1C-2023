--Ejercicio 1
f :: Integer -> Integer
f n | n==1 = 8
    | n==4 = 131
    | n==16 = 16
    | otherwise= undefined

g :: Integer -> Integer
g n | n==8 = 16
    | n==131 = 4
    | n==16 = 1
    | otherwise=undefined

h :: Integer -> Integer
h n = f (g n)

k :: Integer -> Integer
k n = g (f n)

--Ejercicio 2
absoluto :: (Num a, Ord a) => a -> a 
absoluto n | n<0 = -n
           | n==0 = 0
           | otherwise=n

maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto n m | absoluto n > absoluto m = n
                   | absoluto n < absoluto m = m
                   | otherwise = n

maximo :: Integer -> Integer -> Integer
maximo a b | a>b=a
           | otherwise= b

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 a b c = maximo (maximo a b) c

algunoEs0 :: Float -> Float -> Bool
algunoEs0 q r = q==0 || r==0 

-- Dafer Style
algunoes0 :: Float -> Float -> Bool
algunoes0 0 _ = True
algunoes0 _ 0 = True
algunoes0 _ _ = False

ambosSon0 :: Float -> Float -> Bool
ambosSon0 q r = q==0 && r==0

mismoIntervalo :: Integer -> Integer -> Bool
mismoIntervalo n m | (n<=3) && (m<=3) = True
                   | (n>3) && (m>3) && (n<=7) && (m<=7) = True
                   | (n>7) && (m>7)= True
                   | otherwise= False

sonIguales :: Integer -> Integer -> Bool
sonIguales n m = n==m 

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos a b c | not(sonIguales a b) && not(sonIguales a c)&& not(sonIguales b c) = a+b+c
                    | sonIguales a b && not(sonIguales b c)= a+c
                    | not(sonIguales a b) && sonIguales a c = b+c
                    | not(sonIguales a b) && sonIguales b c = a+c
                    | otherwise = a
{-variante daferiana
a/=b && a/=c && b/=c = a+b+c ya abarca la condicion de q son todos distintos
a/=b = a+b
a/=c = a+c
b/=c = b+c
other = a
-}
esMultiplo :: Integer -> Integer -> Bool
esMultiplo n m = mod n m == 0

digitoUnidades :: Integer -> Integer
digitoUnidades n = mod n 10

digitoDecenas :: Integer -> Integer
digitoDecenas m = digitoUnidades(div m 10)

--Ejercicio 3
estanRelacionados :: Integer -> Integer ->Bool
estanRelacionados a b | a==0 || b==0 = False
                      | esMultiplo (a*a) (a*b) = True
                      |otherwise= False

--Ejercicio 4
prodInt :: (Float,Float) -> (Float, Float) -> Float
prodInt (u1,u2) (v1,v2) = u1*v1+u2*v2

todoMenor :: (Float,Float) -> (Float, Float) -> Bool
todoMenor (u1,u2) (v1,v2) = u1<v1 && u2<v2

--Extra
norma :: (Float,Float) -> Float
norma (x,y) = sqrt(x^2+y^2)

distanciaPuntos :: (Float,Float) -> (Float, Float) -> Float
distanciaPuntos (u1,u2) (v1,v2) = norma (v1-u1,v2-u2)

sumarTerna :: (Integer,Integer,Integer)->Integer
sumarTerna(a,b,c)= a+b+c

sumarSoloMultiplos :: (Integer,Integer,Integer) -> Integer -> Integer
sumarSoloMultiplos (a,b,c) n | esMultiplo a n && esMultiplo b n && esMultiplo c n = a+b+c
                             | esMultiplo a n && esMultiplo b n = a+b 
                             | esMultiplo a n && esMultiplo c n = a+c 
                             | esMultiplo b n && esMultiplo c n = b+c
                             | esMultiplo a n = a
                             | esMultiplo b n = b
                             | esMultiplo c n = c
                             | otherwise = 0

posPrimerPar :: (Integer,Integer,Integer) -> Integer
posPrimerPar (a,b,c) | esMultiplo a 2 = 1
                     | esMultiplo b 2 = 2
                     | esMultiplo c 2 = 3
                     | otherwise = 4

crearPar :: tx -> ty -> (tx,ty)
crearPar x y = (x,y)

invertir :: (tx,ty) -> (ty,tx)
invertir (x,y) = (y,x)

--Ejercicio 5
todosMenores :: (Integer,Integer,Integer) -> Bool
todosMenores (a,b,c) = (f1 a > f2 a) && (f1 b > f2 b) && (f1 c > f2 c)

f1 :: Integer -> Integer
f1 x | x <= 7 = x^2
     | otherwise = 2*x-1

f2 :: Integer -> Integer
f2 y | esMultiplo y 2 = div y 2
     | otherwise = 3*y+1

--Ejercicio 6
bisiesto :: Integer -> Bool
bisiesto año | not(esMultiplo año 4) || (esMultiplo año 100 && not(esMultiplo año 400))=False
             | otherwise= True

--Ejercicio 7
distanciaManhattan :: (Float,Float,Float)->(Float,Float,Float)-> Float
distanciaManhattan (p1,p2,p3) (q1,q2,q3) = absoluto (p1-q1)+absoluto(p2-q2)+absoluto(p3-q3)

--Ejercicio 8
comparar :: Integer -> Integer -> Integer
comparar a b | sumaUltDos a < sumaUltDos b = 1
             | sumaUltDos a > sumaUltDos b = -1
             | otherwise = 0

sumaUltDos :: Integer -> Integer
sumaUltDos x = digitoDecenas x + digitoUnidades x