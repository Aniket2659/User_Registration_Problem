import re

class UserRegistration:
    def __init__(self):
        self.first_name = None
        self.last_name=None
        self.email=None

    def users_first_name(self):
        try:
            self.first_name = input("Enter your first name: ")
            validation= re.match(r"^[A-Z][a-zA-Z]{2,}$",self.first_name)
            if not validation:
                raise ValueError("Invalid first_name")
            else:
                print('registration is successfull')
            
        except ValueError as e:
            print(e)
            print('First name must start with a capital letter and have at least 3 characters')


    def users_last_name(self):
        try:
            self.last_name = input("Enter your last name: ")
            validation= re.match(r"^[A-Z][a-zA-Z]{2,}$",self.last_name)
            if not validation:
                raise ValueError("Invalid last name")
            else:
                print('registration is successfull')
                
        except ValueError as e:
            print(e)
            print('last name must start with a capital letter and have at least 3 characters')
    
    def Email(self):
        try:
            self.email = input("Enter your email : ")
            validation= re.match(r"^(abc)+\.([a-zA-Z0-9]+)@(bl)\.(co)\.([a-zA-Z0-9]+)$",self.email)
            if not validation:
                raise ValueError("Invalid email")
            else:
                print('registration is successfull')
                
        except ValueError as e:
            print(e)
            print(" email has 3 mandatory parts (abc, bl& co) and 2 optional (xyz & in) with precise @ and . positions")

    
    
    def menu(self):
        print("1. Enter valid first name ")
        print("2. Enter valid last name ")
        print("3. Enter valid email ")
        user_choice=int(input('enter your choice :'))
        return user_choice



    def selection(self,choice):
        match choice:
            case 1:
                self.users_first_name()
            case 2:
                self.users_last_name()
            case 3:
                self.Email()
            
            case _:
                print("Invalid choice")
                


if __name__ == "__main__":
    user_registration_obj = UserRegistration()
    
    while True:
        choice=user_registration_obj.menu()
        user_registration_obj.selection(choice)

        exit=input('do you want to exit :')
        if exit == 'yes':
            break