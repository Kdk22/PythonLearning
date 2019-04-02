def CheeseShop(kind, *arguments, **keyargs):
    print('Do you have any ' , kind, '?')
    print('Sorry we donn n\'t have any', kind,  )
    for arg in arguments:
        print(arg)
    print('-'*40)
    for kwd in keyargs:
        print(kwd ,':', keyargs[kwd])

CheeseShop('yak', 'itn\'s very funny. ','It n\'s very very funny', ShopKeeper= 'Chikeellyy', CLient ='Chakalllaa'  )

def concat(*args, L=[]): #only use keyword arguments after *args parameter
    L.append(args)
    return L

concat(2,3,4,5,6)
