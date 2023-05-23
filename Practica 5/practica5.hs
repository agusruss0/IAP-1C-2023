--Ejercicio 1

longitud :: [t] -> Integer
longitud [] = 0
longitud l = 1 + longitud(tail l)

ultimo :: [t] -> t
ultimo (x:xs) | longitud (x:xs) == 1 = x 
              | otherwise = ultimo (tail (x:xs))

--principio :: [t] -> [t]
--principio

reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = (reverso xs) ++ [x]

--Ejercicio 2

pertenece :: (Eq t) => t -> [t]-> Bool
pertenece t [] = False
pertenece t (x:xs) | t == x = True
                   | otherwise = pertenece t xs

todosIguales :: (Eq t) => [t] -> Bool
todosIguales (x:xs) | longitud (x:xs)==1 = True
                    | pertenece x xs = todosIguales xs
                    | otherwise = False

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos (x:xs) | longitud (x:xs) == 1 = True
                      | not(pertenece x xs) = todosDistintos xs
                      | otherwise = False

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos (x:xs) | longitud (x:xs)==1 = False
                    | x /= head xs = hayRepetidos (x:tail xs) 
                    | x == head xs = True
                    |otherwise = hayRepetidos xs

--Dafer's Way

seRepiteLoco :: (Eq t) => [t] -> Bool
seRepiteLoco l = not(todosDistintos l)

quitar :: (Eq t) => t -> [t] -> [t]
quitar n [] = []
quitar n (x:xs) | n == x = xs
                | otherwise = x : quitar n xs

quitarTodos :: (Eq t) => t -> [t] -> [t] 
quitarTodos n [] = []
quitarTodos n (x:xs) | n == x = quitarTodos n xs
                     | otherwise = x : quitarTodos n (quitar n xs)

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos []=[]
eliminarRepetidos (x:xs) | pertenece x xs = x : eliminarRepetidos (quitarTodos x xs)
                         | otherwise = x : eliminarRepetidos xs

mismoElementos :: (Eq t) => [t] -> [t] -> Bool
mismoElementos [] [] = True
mismoElementos [] l = False
mismoElementos l [] =False
mismoElementos (x:xs) l | pertenece x l = mismoElementos (eliminarRepetidos xs) (eliminarRepetidos (quitarTodos x l))

--Alternativo
mismoConjunto :: (Eq t) => [t] -> [t] -> Bool
mismoConjunto c1 c2 = incluido c1 c2 && incluido c2 c1

incluido :: (Eq t) => [t] -> [t] -> Bool
incluido [] _ = True
incluido (x:xs) c2 = pertenece x c2 && incluido xs c2

capicua ::(Eq t) => [t] -> Bool
capicua [] = True
capicua (x:xs) | x == head(reverso (x:xs)) = capicua (quitar x (reverso xs))
               | otherwise = False

--Ejercicio 3

sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs

maximo :: [Integer] -> Integer
maximo (x:xs) | longitud (x:xs) == 1 = x
              | x <= head xs = maximo xs
              | otherwise =maximo (x: tail xs)

sumarN :: Integer -> [Integer] -> [Integer]
sumarN n []=[]
sumarN n (x:xs) = n+x : sumarN n xs

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs) | longitud (x:xs)==1 = [x+x]
                      | otherwise =x+x : sumarN x xs

sumarElUltimo :: [Integer]-> [Integer]
sumarElUltimo (x:xs) | longitud (x:xs)== 1 = [x+x]
                     | otherwise = x + head(reverso (x:xs)) : sumarN (head(reverso xs)) xs

pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | mod x 2 == 0 = x : pares xs
             | otherwise = pares xs

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN 0 l = undefined
multiplosDeN n [] = []
multiplosDeN n (x:xs) | mod x n == 0 = x : multiplosDeN n xs
                      | otherwise = multiplosDeN n xs

ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar (x:xs) = ordenar (quitar (maximo (x:xs)) (x:xs)) ++ maximo (x:xs) : []

--Ejercicio 4
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:xs) | x == (head xs) && x == ' ' =  sacarBlancosRepetidos (quitar x xs)
                             | otherwise = x : sacarBlancosRepetidos xs