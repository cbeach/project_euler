
fibs :: [Integer]
fibs = 0 : 1 : [a + b | (a, b) <- zip fibs (tail fibs)]

firstNFibs :: Integer -> [Integer]
firstNFibs n = [f | (i, f) <- zip [0..n] fibs] 

fibsLessThan :: Integer -> [Integer]
fibsLessThan l = [f | f <- takeWhile (< l) fibs]

main::IO()
main = print (sum [f | f <- fibsLessThan 4000000, f `mod` 2 == 0])
