import pywhatkit,pyautogui,time
import pywhatkit as kit
# # phoneNumber = input("Enter the phone number with country code(e.g. +9779800000000): ").strip()
# # if not phoneNumber.startswith("+"):
# #     print("Phone number must include the country code starting with '+'.")
# #     exit()

# # message = input("Enter the message you want to send: ").strip()
# # hour = int(input("Enter the hour(24-hour format) to send the message: "))
# # minute = int(input("Enter the minute to send a message: "))

# # pywhatkit.sendwhatmsg(phoneNumber, message, hour, minute)

# # print("Message scheduled successfully!")

phoneNo = "+9779807365120"
message = "Pls this is toooo fking muchhhhhhhhhh"
kit.sendwhatmsg(phoneNo, message, 2, 14)
time.sleep(3)
pyautogui.press("enter")

print("Message sent instantly!")


