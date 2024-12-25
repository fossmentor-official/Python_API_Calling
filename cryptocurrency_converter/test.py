from cryptozor import Cryptozor

Cryptozor = Cryptozor("pkr", "eth")  # From INR to ETH

value = Cryptozor.convert(2500)  # Amount
print(value)
