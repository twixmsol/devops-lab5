#Лаб 5 пайтон
with open ("myfile.txt","w") as f:
  f.write("Тест\n")
  f.write("екінші жол\n")
with open ("myfile.txt", "r") as f:
  content=f.read()
print("Файл құрылымы:")
print(content)
