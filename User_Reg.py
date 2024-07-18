import re

class UserRegistration:
    def __init__(self):
        self.first_name = None

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
    
    def menu(self):
        print("1. Enter valid first name :")
        user_choice=int(input('enter your choice :'))
        return user_choice



    def selection(self,choice):
        match choice:
            case 1:
                self.users_first_name()
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