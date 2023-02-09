# Coder: Mr. Yako
# Instagram: @YakoSec
# GitHub : @YakoSec
# Telegram: @YakoSec

import random
import colorama
from colorama import Fore, Back, Style
colorama.init()

from faker import Faker
fake = Faker()

print(Fore.YELLOW)
print("Coder: Mr. Yako \nInstagram: @YakoSec \nTelegram: @YakoSec \nGitHub: @YakoSec")

print(Fore.LIGHTBLUE_EX)
print("Name: ",fake.name())
print(Fore.GREEN)
print("EMail: ",fake.email())
print(Fore.MAGENTA)
print("Country: ",fake.country())
print(Fore.RED)
print("Profile: ",fake.profile())
