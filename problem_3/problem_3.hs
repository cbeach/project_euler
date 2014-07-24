--Problem 3: The prime factors of 13195 are 5, 7, 13 and 29.
--           What is the largest prime factor of the number 600851475143?

import qualified Data.Numbers.Primes as Primes

prime_factors :: Integer -> [Integer]
prime_factors large_prime = let lp_sqrt = floor . sqrt . fromIntegral $ 600851475143 in [p | p <- takeWhile (< lp_sqrt) Primes.primes, large_prime `mod` p == 0]



main :: IO()
main = print (maximum . prime_factors $ 600851475143)
