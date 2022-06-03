import random
import os

import re

class User:
    current_login_user = None
    def __init__(self, uid=-1 , username="", password="" , register_time="yyyy-MM-dd_HH:mm:ss.SSS" , role = ""):
        self.uid = uid
        self.username = username
        self.password = password
        self.register_time = register_time
        self.role = role


    def __str__(self):
        return f"{self.uid};;;{self.username};;;{self.password};;;{self.rigester_time};;;{self.role}"


    def validate_username(self, username):
        regex = re.compile(r"^[A-Za-z_]+$")
        if(regex.match(username)):

            return True

        return False

    def validate_password(self, password):
        size = re.compile(r"^.{8,}$")
        if (size.match(password)):
            return True
        else:
            return False


    def validate_email(self, email):
        regex = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com$")
        size = re.compile(r"^.{9,}$")
        if (regex.match(email) and size.match(email)):
            return True
        else:
            return False


    def clear_user_data(self):
        path = os.path.dirname(__file__)
        path = path.replace("model" , "")
        user_data = open(path + "data\\user.txt", "w")
        user_data.close()



    def authenticate_user(self, username, password):
        path = os.path.dirname(__file__)
        path = path.replace("model", "")
        user_data = open(path + "\\data\\user.txt")

        for line in user_data:
            temp_list = line.split(";;;")
            print(self.encrypt_password(password), temp_list[2])
            if (username == temp_list[1] and self.encrypt_password(password) == temp_list[2]):
                user_data.close()
                return True
        user_data.close()
        return False



    def check_username_exist(self, username):
        path = os.path.dirname(__file__)
        path = path.replace("model", "")
        username_data = open(path + "\\data\\user.txt")
        for line in username_data:
            temp_username = (line.split(";;;"))[1]

            if (temp_username == username):
                username_data.close()
                return True
        username_data.close()
        return False


    def generate_unique_user_id(self):
        path = os.path.dirname(__file__)
        path = path.replace("model", "")
        user_data = open(path + "data\\user.txt", encoding="utf8", mode="r")
        user_ids = []
        for line in user_data:
            temp_ids = line.split(";;;")[0]
            user_ids.append(temp_ids)

        user_id_exist = True
        while user_id_exist:
            user_id = random.randint(100000, 999999)

            if (str(user_id) in user_ids) == False:
                user_id_exist = False

        return user_id


    def encrypt_password(self, password):
        all_punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        # creat the encrypted_result with defualt first three character
        encrypted_resualt = "^^^"
        # creat three character with all_punctuation
        # get the character of all_punctuation at input string length module all_punctuation length as the first_character
        fisrt_character = all_punctuation[len(password) % len(all_punctuation)]
        # get the character of all_punctuation at input string length module 5 as the second_character
        second_charcter = all_punctuation[len(password) % 5]
        # get the character of all_punctuation at input string length module 10 as the third_character
        third_charcter = all_punctuation[len(password) % 10]

        # generate encrypted string according to instruction
        for x in range(len(password)):

            if x % 3 == 0:
                encrypted_resualt += fisrt_character + password[x] + fisrt_character
            if x % 3 == 1:
                encrypted_resualt += second_charcter * 2 + password[x] + second_charcter * 2
            if x % 3 == 2:
                encrypted_resualt += third_charcter * 3 + password[x] + third_charcter * 3
        # add three defualt character to the end of encrypted result
        encrypted_resualt += "$$$"
        return encrypted_resualt


    def register_user(self, username, password, email, register_time, role):
        if (self.check_username_exist(username)):
            return False
        user_id = self.generate_unique_user_id()
        register_time = self.date_conversion(register_time)
        if (self.validate_username(username) and self.validate_password(password) and self.validate_email(email)):
            path = os.path.dirname(__file__)
            path = path.replace("model", "")
            user_data = open (path + "\\data\\user.txt" , 'a')
            if (role =="student" ):
                user_data.write(f"\n{user_id};;;{username};;;{self.encrypt_password(password)};;;{register_time};;;{role};;;{email}")
                user_data.close()
            elif(role == "instructor"):
                user_data.write(f"\n{user_id};;;{username};;;{self.encrypt_password(password)};;;{register_time};;;{role};;;{email};;;;;;;;;")
                user_data.close()


    def date_conversion(self, register_time):
        # Add +11 hours for Melbourn time
        seconds = register_time + (11 * 3600)
        # Save the time in Human
        # Number of days in month
        # in normal year
        daysOfMonth = [31, 28, 31, 30, 31, 30,
                       31, 31, 30, 31, 30, 31]

        (currYear, daysTillNow, extraTime,
         extraDays, index, date, month, hours,
         minutes, secondss, flag) = (0, 0, 0, 0, 0,
                                     0, 0, 0, 0, 0, 0)

        # Calculate total days unix time T
        daysTillNow = seconds // (24 * 60 * 60)
        extraTime = seconds % (24 * 60 * 60)
        currYear = 1970

        # Calculating current year
        while (daysTillNow >= 365):
            if (currYear % 400 == 0 or
                    (currYear % 4 == 0 and
                     currYear % 100 != 0)):
                daysTillNow -= 366

            else:
                daysTillNow -= 365

            currYear += 1

        # Updating extradays because it
        # will give days till previous day
        # and we have include current day
        extraDays = daysTillNow + 1

        if (currYear % 400 == 0 or
                (currYear % 4 == 0 and
                 currYear % 100 != 0)):
            flag = 1

        # Calculating MONTH and DATE
        month = 0
        index = 0

        if (flag == 1):
            while (True):

                if (index == 1):
                    if (extraDays - 29 < 0):
                        break

                    month += 1
                    extraDays -= 29

                else:
                    if (extraDays - daysOfMonth[index] < 0):
                        break

                    month += 1
                    extraDays -= daysOfMonth[index]

                index += 1

        else:
            while (True):
                if (extraDays - daysOfMonth[index] < 0):
                    break

                month += 1
                extraDays -= daysOfMonth[index]
                index += 1

        # Current Month
        if (extraDays > 0):
            month += 1
            date = extraDays

        else:
            if (month == 2 and flag == 1):
                date = 29
            else:
                date = daysOfMonth[month - 1]

        # Calculating HH:MM:YYYY
        hours = int(extraTime // 3600)

        minutes = int(extraTime % 3600) // 60
        secondss = (extraTime % 3600) % 60

        result = f"{str(currYear)}-{str(str(month))}-{str(int(date))}_{str(hours)}:{str(minutes)}:{str(secondss)[0:6]}"

        # Return the time
        return result
































