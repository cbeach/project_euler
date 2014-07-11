{- |
Module      :  Project Euler problem 1
Description :  Find the sum of all multiples of 3 and 5 that are less than 1000 
Copyright   :  (c) Casey Beach
License     :  MIT

Maintainer  :  Casey Beach
Stability   :  stable
Portability :  non-portable (This is a project Euler problem, do you really need a reason :P)

Problem 1:  If we list all the natural numbers below 10 that are multiples of 3 or 5,
            we get 3, 5, 6 and 9. The sum of these multiples is 23.  Find the sum of
            all the multiples of 3 or 5 below 1000.
-}

import Data.List

getMultiples :: Int -> Int -> [Int]
getMultiples multiple upper_bound = let r = [multiple,multiple*2..upper_bound] in [x | x<-r, x < upper_bound]


sumOfMultsLT1000 :: Int -> Int -> Int
sumOfMultsLT1000 a b = sum (map head (group (sort (getMultiples a 1000 ++ getMultiples b 1000))))

main :: IO()
main = let sum_of_multiples = sumOfMultsLT1000 3 5 in print sum_of_multiples
