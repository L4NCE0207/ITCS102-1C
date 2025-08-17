amount = eval(input("Enter amount to deposit: "))
print("Here is a breakdown of your deposit:")

ans1 = amount // 1000
amount = amount - ans1 * 1000

ans2 = amount // 500
amount = amount - ans2 * 500

ans3 = amount // 200
amount= amount - ans3 * 200

ans4 = amount // 100
amount = amount - ans4 * 100

ans5 = amount // 50
amount = amount - ans5 * 50
  
ans6 = amount // 20
amount = amount - ans6 * 20
 
ans7 = amount // 10
amount = amount - ans7 * 10

ans8 = amount // 5
amount = amount - ans8 * 5

ans9 = amount // 1
amount = amount - ans9 * 1

print(ans1, "-", 1000)
print(ans2, "-", 500)
print(ans3, "-", 200)
print(ans4, "-", 100)
print(ans5, "-", 50)
print(ans6, "-", 20)
print(ans7, "-", 10)
print(ans8, "-", 5)
print(ans9, "-", 1)