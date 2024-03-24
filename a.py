# # # # a = int(input())
# # # # b = int(input())
# # # # c = int(input())
# # # # if a > 0 and b > 0 and c > 0 :
# # # #    if a + b > c and a + b > c and b + c > a :
# # # #       print("tam giac ne ae")
# # # #       if a^2 + b^2 == c^2 or a^2 + c^2 == b^2 or c^2 + b^2 == a^2 :
# # # #          print("tam giac vuong ne ae")
# # # #       elif a == b or b == c or a == c :
# # # #          print("tam giac can")
# # # # else:
# # # #    print("khong co so")
# # # def check():
# # #     user = input()
# # #     if user == "admin":
# # #         password = input()
# # #         if password == "123456@Abc":
# # #             print("welcome")
# # #         else:
# # #             print("wrong password")
# # #     else:
# # #         print("wrong username")

# # # def check1():
# # #     user = input()
# # #     password = input()
# # #     if user == "admin" and password == "123456@Abc":
# # #          print("welcome")
# # #     else:
# # #          print("wrong username or password")
# # # check1()

# # def nhapdiemso(a,b,c):
# #     x = (a + b + c)/3
# #     if x >= 8:
# #         print("Xuat sac")
# #     elif x >= 7 and x < 8 :
# #         print("Gioi")
# #     elif x >= 5 and x < 7 :
# #         print("Dat")
# #     elif x<= 5:
# #         print("Hs duoi tb")
# # while True:        
# #   a = float(input("Diem van:"))
# #   b = float(input("Diem toan:"))
# #   c = float(input("Diem TA:"))
# #   if a < 0 or a > 10 or b < 0 or b > 10 or c < 0 or c > 10:
# #       print("Nhap lai diem")
# #       continue
# #   else:
# #       nhapdiemso(a,b,c)
# #       break

# def bmi(weight, height):
#     bmi = weight / (height*height)
#     if bmi >= 40:
#         return("beo phi cap do III")
#     elif bmi < 40:
#         return("beo phi cap do II")
#     elif bmi < 35:
#         return("beo phi cap do I")
#     elif bmi < 30:
#         return("Thua can")
#     elif bmi < 25:
#         return("Binh thuong")
#     elif bmi < 18.5:
#         return("gay cap do I")
#     elif bmi < 17:
#         return("gay cap do II")
#     elif bmi < 16:
#         return("gay cap do III")

# weight = float(input())
# height = float(input())
# print(bmi(weight, height))
a = int(input())
print("dat") if a > 5 else print("khong dat")