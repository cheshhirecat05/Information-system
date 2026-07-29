import random
import os
from captcha.image import ImageCaptcha

# CAPTCHA
image = ImageCaptcha(width=280, height=90)

captcha_text = ''.join(random.choices(
    '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=6))

print("Generated Captcha Text:", captcha_text)

image.write(captcha_text, 'captcha.png')
os.startfile('captcha.png')

user_input = input('Enter CAPTCHA: ')

if user_input.upper() == captcha_text.upper():
    print("Captcha verification successful!\n")

    # 2FA
    two_factor_code = ''.join(random.choices('0123456789', k=6))
    print("2FA Code (simulated):", two_factor_code)

    user_2fa_input = input("Enter 2FA code: ")

    if user_2fa_input == two_factor_code:
        print("Two-Factor Authentication successful! Login complete.")
    else:
        print("2FA failed.")
else:
    print("Captcha failed.")