#! python3
import re, pyperclip

#create a regex for phone numbers
phoneRegex=re.compile(r'''
# 415-555-6079 555-7890 (415) 555-8907, 555-8907 ext 1234, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?     #area code opt
(\s|-)                       #first seperator
\d\d\d                       #first 3 digits
-                            #separator
\d\d\d\d                     #last 4
((ext(\.)?\s|x)              #ext word part
((\d){2,5}))?   )             #extension num part
''', re.VERBOSE)

#create a regex for email addresses
emailRegex=re.compile('''
#some.+_thing@something.com
[a-zA-Z0-9_.+]+ #name part
@ #@
[a-zA-Z0-9_.+]+ #domain name part
''', re.VERBOSE)

# get the text off the clipboard
text=pyperclip.paste()

# - extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)
print(extractedEmail)

# - copy the extracted email/phone to the clip board
results= '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
