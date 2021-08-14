
phone_book = {'이순신': '010-9876-5432'}
phone_book["홍길동"] = "010-1234-5678"
phone_book["강감찬"] = "010-1234-4321"

print(phone_book)
print(phone_book["이순신"])

print(phone_book.keys())
print(phone_book.values())

# []해서 = 값 하면 add와 같은 역할?

for key in sorted(phone_book.keys()):
    print(key, phone_book[key])
