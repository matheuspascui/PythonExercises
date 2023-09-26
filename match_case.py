''' Here, i'll explore the match/case conditions in Python.
'''

'''
Code using If-Elif-Else:

http_status = int(input("Type here the some http status to see its message: "))

if http_status == 200:
    print('Succes!)
elif http_status == 400:
    print('Bad request')
elif http_status == 404:
    print('Not found')
elif http_status == 500 or http_status == 501:
    print('Server error')
else:
    print("unknown")
'''

# Below, the same code, using match/case

http_status = int(input("Type here one http number status to see its message:\t"))

match http_status:
    case 200:
        print("Success!")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500 | 501:
        print("Server Error")
    case _: # we use _: to define the "else" condition using match/case
        print("Unexpexted")
    
