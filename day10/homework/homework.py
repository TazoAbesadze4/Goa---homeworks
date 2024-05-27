#გააკეთეთ პროგრამა. (მოხმარებელს შემოატანინეთ პაროლი იქამდე სანამ 
# არ დაემტხვევა რეგისტრირებულ პაროლს, while ციკლის და if else
# ის გამოყენებით

password = "tazo1"

while True:
    input_password = input("enter password:  ")

    if input_password == password:
        print("sworia")
        break
    else:
        print("arasworia")