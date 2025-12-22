from zadania import is_palindrome
print(is_palindrome("kajak"))
print(is_palindrome("Kobyła ma mały bok"))
print(is_palindrome("python"))
print(is_palindrome(""))
print(is_palindrome("A"))

from zadania import fibonacci
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(5))
print(fibonacci(10))
#error print(fibonacci(-1))

from zadania import count_vowels
print(count_vowels("Python"))
print(count_vowels("AEIOUY"))
print(count_vowels("bcd"))
print(count_vowels(""))
print(count_vowels("Próba żółwia"))

from zadania import calculate_discount
print(calculate_discount(100, 0.2))
print(calculate_discount(50,0))
print(calculate_discount(200,1))
#error print(calculate_discount(100,-0.1))
#error (calculate_discount(100, 1.5)

from zadania import flatten_list
print(flatten_list([1, 2, 3]))
print(flatten_list([1, [2, 3], [4, [5]]]))
print(flatten_list([]))
print(flatten_list([[[1]]]))
print(flatten_list([1, [2, [3, [4]]]]))

from zadania import word_frequencies
print(word_frequencies("To be or not to be"))
print(word_frequencies("Hello, hello!"))
print(word_frequencies(""))
print(word_frequencies("Python Python python"))
print(word_frequencies("Ala ma kota, a kot ma Ale."))

from zadania import is_prime
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(0))
print(is_prime(1))
print(is_prime(5))
print(is_prime(97))



