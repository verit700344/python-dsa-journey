numbers = [1, 2, 4, 5]

expected = 15

actual = 0

for number in numbers:
    actual = actual + number

missing = expected - actual
print(missing)