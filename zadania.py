# zadanie 1
def is_palindrome(text:str)->bool:
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text==cleaned_text[::-1]

#zadanie 2
def fibonacci(n:int)->int:
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#zadanie 3
def count_vowels(text:str)->int:
    vowels="aeiouy"
    text=text.lower()
    count=0
    for char in text:
        if char in vowels:
            count+=1
    return count

#zadanie 4
def calculate_discount(price:float,discount:float)->float:
    if not 0<=discount<=1:
        raise ValueError("Zniżka musi być w zakresie od 0 do 1")
    discounted_price=price*(1-discount)
    return discounted_price

#zadanie 5
def flatten_list(nested_list: list) -> list:
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

#zadanie 6
import string
def word_frequencies(text: str)->dict:
    text=text.lower()
    text=text.translate(str.maketrans("","",string.punctuation))
    words=text.split()
    freq={}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

#zadanie 7
def is_prime(n:int)->bool:
    if n<2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
