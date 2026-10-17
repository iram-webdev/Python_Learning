letter="hey my name is {1} and i am from {0}"
country="india"
name="iram"

print(letter.format(country, name))

print(f"hey my name is {{name}} and i am from {country}")


text="for only {price:.2f}dollars!"
print(text.format(price =49.099999))

print(type(f"{2*30}"))
