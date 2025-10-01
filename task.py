#Лаб 5 пайтон
with open ("myfile.txt","w") as f:
  f.write("Тестовый\n")
  f.write("Вторая строка\n")
with open ("myfile.txt", "r") as f:
  content=f.read()
print("Содержимое файла:")
print(content)
