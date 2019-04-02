from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    print('this is response: ', response)
    for line in response:
        print('line inside for loop before decode: ',line)
        line = line.decode('utf-8')
        print('___________UTF-8 line after decode: ', line)
        if 'EST' in line or 'EDT' in line:
            print(line)


'''
    THis is for sending email
'''

import smtplib
content = 'THis is just a testing message inside the content.'
mail = smtplib.SMTP('smtp.gmail.com', 587) #This is to connect to gmail server through port 587
mail.ehlo() #extended SMTP server
mail.starttls() #start TLS MODE ie. Transport Layer Security to encrypt  the email and password
mail.login('tamang5sweeta@gmail.com', '5camprock5')
mail.sendmail('tamang5sweeta@gmail.com','khadkautshav7@gmail.com', 'subject: Hello World\n\n This is my message to the world.')
mail.sendmail('tamang5sweeta@gmail.com','khadkautshav7@gmail.com',content)
mail.quit()

# ref: https://www.youtube.com/watch?v=FQN_4sylvF4