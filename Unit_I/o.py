details = {
    "name": "John",
    "age": 25,
    "city": "Delhi",
    "score": 85.5,
    "active": True,
    "count": 100,
    "grade": "A",
    "marks": 95
}
print(details.setdefault("name", "Doe"))
print(details)
# print(details.get("age","Key does not exist"))