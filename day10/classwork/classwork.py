#(მოხმარებელს შემოატანინეთ პაროლი იქამდე სანამ არ დაემტხვევა 
# რეგისტრირებულ პაროლს, while ციკლის და  if else _ის გამოყენებით) 

authorized = False
password = "tazo122"

while password != True:
    user_input = input("please enter your password: ")
    if user_input == password:
        print("password is corecct")
        authorized = True
