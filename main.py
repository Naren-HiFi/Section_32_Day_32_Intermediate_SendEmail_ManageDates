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


