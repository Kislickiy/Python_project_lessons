# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59


input_data = input("Enter a number between 0 and 8 640 000: ")
number_of_dates = 0
number_of_hours = 0
number_of_minutes = 0

if 0 <= int(input_data) < 8640000:
    number_of_dates = int(input_data) // 60 // 60 // 24
    number_of_hours = int(input_data) // 60 // 60 % 24
    if number_of_hours == 0:
        number_of_hours = "00"
    elif len(str(number_of_hours)) == 1:
        number_of_hours = "0" + str(number_of_hours)
    number_of_minutes = int(input_data) // 60 % 60
    if number_of_minutes == 0:
        number_of_minutes = "00"
    elif len(str(number_of_minutes)) == 1:
        number_of_minutes = "0" + str(number_of_minutes)
    number_of_seconds = int(input_data) % 60
    if number_of_seconds == 0:
        number_of_seconds = "00"
    elif len(str(number_of_seconds)) == 1:
        number_of_seconds = "0" + str(number_of_seconds)
else:
    print("Number must be between 0 and 8 640 000")

if str(number_of_dates)[-1] == "0" or 11 <= int(number_of_dates) < 20:
    name_of_days = "Днів"
elif str(number_of_dates)[-1] == "1":
    name_of_days = "День"
elif str(number_of_dates)[-1] == "2" or str(number_of_dates)[-1] == "3" or str(number_of_dates)[-1] == "4":
    name_of_days = "Дні"
else:
    name_of_days = "Днів"
print(str(number_of_dates) + " " + str(name_of_days) + " " + str(number_of_hours)
      + ":" + str(number_of_minutes) + ":" + str(number_of_seconds))