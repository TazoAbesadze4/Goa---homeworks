#       ფინქციონალური პროგრამირება


#     დავიმახსოვღოთ:
#  def - შექმნა, განსაზღვრა

# def say_hi(user_name):
#     print(user_name + " gamarjoba")

# say_hi("tazo")



# def hi(name):
#     return name + " gamarjoba"

# print(hi("tazo"))


#შექმენით ფუნქცია, რომელიც მომხმარებელს შეეკითხება რიცხვს. 
# ხოლო დაუპრინტავს ამ რიცხვზე 3ჯერ დიდ რიცხვს. 

#გამოიძახეთ ეს ფუნქცია 5ჯერ, სხვადასხვა რიცხვებისთვის 
# და დატესტეთ     --->


#        "number" არის პარამეტრი (როცა ფუნქციას ვქმნით)
# def num(number):
#     number = int(input("enter a namber: "))
#     print(number * 3)

#    "4, 11, ..., 5" არის არგუმრნტი (როცა ფუნქციას გამოიძახებთ)
# num(3)
# num(5)
# num(11)
# num(23)
# num(9)
       #"num" არის პარამეტრი (როცა ფუნქციას ვქმნით)
# def num(num): 
#     print(num * 3)

    # "4, 11, ..., 5" არის არგუმრნტი (როცა ფუნქციას გამოიძახებთ)
# num(4)
# num(11)
# num(6)
# num(7)
# num(5)


#        d r a w    a    a p a r t a m e n t

# from turtle import*

# #   start draw apartament -->

# speed(13)
# width(5)

# def draw_squear():
#     for i in range(4):
#         forward(100)
#         left(90)

# def move_cursor(x, y):
#     penup()
#     goto(x, y)
#     pendown()

# draw_squear()
# move_cursor(0, 150)

# draw_squear()
# move_cursor(-150, 150)

# draw_squear()
# move_cursor(-150, 0)

# draw_squear()
# move_cursor(-150, -150)

# draw_squear()
# move_cursor(0, -150)

# draw_squear()
# move_cursor(100, -150)

# color("blue")
# penup()
# goto(150, -150)
# pendown()
# left(90)
# forward(450)
# left(90)
# forward(350)
# left(90)
# forward(500)
# left(90)
# forward(350)
# left(90)
# forward(50)

# penup()
# goto(150, 300)
# pendown()
# left(70)
# forward(180)
# left(38)
# forward(188)


# exitonclick()

#  e n d    d r a w    a    a p a r t a m e n t

#     test -->

# def sey_hi(user_name):
#     print("gamarjoba " + user_name)

# sey_hi(input("enter name:  "))
# sey_hi(input("enter name:  "))
# sey_hi(input("enter name:  "))
# sey_hi(input("enter name:  "))