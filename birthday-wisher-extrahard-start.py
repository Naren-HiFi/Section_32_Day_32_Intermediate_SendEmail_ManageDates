##################### Extra Hard Starting Project ######################
import random
import pandas
import datetime as dt
import smtplib

MY_EMAIL = "infonaren55@gmail.com"
EMAIL_PASSWORD = "uyeimfunxtpufhna"
TO_MAIL_ADDRESS = "narenbagavathye5@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

now = dt.datetime.now()
today_date = now.day
today_month = now.month
today_day_of_week = now.weekday()
today_tuple = (today_month,today_date)
# 2. Check if today matches a birthday in the birthdays.csv
birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]): data_row for (index,data_row) in birthday_data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_mail:
        content = letter_mail.read()
        replaced_name_in_letter = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP(SMTP_SERVER,SMTP_PORT) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_MAIL_ADDRESS,
            msg=f"Subject:Happy birthday!\n\n{replaced_name_in_letter}"
        )


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.



"""



MY_EMAIL = "infonaren55@gmail.com"
EMAIL_PASSWORD = "uyeimfunxtpufhna"
TO_MAIL_ADDRESS = "narenbagavathye5@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

with smtplib.SMTP(SMTP_SERVER, port=SMTP_PORT) as connection:
    
    # TLS stands for Transport Layer Security.
    # It's a way of securing our connection to our email server.
    
    connection.starttls()
    connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=TO_MAIL_ADDRESS,
        msg="Subject:PYTHON AUTOMATION BOT\n\n This is the reminder for you to learn python regularly."
    )


import datetime as dt

current_date_time = dt.datetime.now()
current_year = current_date_time.year
current_month = current_date_time.month
current_week_day = current_date_time.weekday()

date_of_birth = dt.datetime(year=1995, month=6, day=21,hour=5)
print(date_of_birth)


import smtplib
import datetime as dt
import random

MY_EMAIL = "infonaren55@gmail.com"
EMAIL_PASSWORD = "uyeimfunxtpufhna"
TO_MAIL_ADDRESS = "narenbagavathye5@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 2:
    with open("quotes.txt") as quotes_txt_file:
        quotes_list = quotes_txt_file.readlines()
        quote = random.choice(quotes_list)

    print(quote)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=TO_MAIL_ADDRESS,
                            msg=f"Subject:MONDAY MOTIVATION QUOTE\n\n{quote}"

        )



print(birthday_dict)
b_date = birthday_dict.get("day")
print(b_date)
b_month = birthday_dict.get("month")
b_email = birthday_dict.get("email")
b_person_name = birthday_dict.get("name")



"""
