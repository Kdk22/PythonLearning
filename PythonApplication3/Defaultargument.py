def ask(prompt, retries=4, reminder='Please try again !'):
    while True:
        ok= input(prompt)
        if ok in ('y','ye','yes'):
            return False
        if ok in ('N','No','Na','Nope'):
            return False
        retries= retries-1
        if retries<0:
            raise ValueError('invalid user response')
        print(reminder)
ask('Nooo')



