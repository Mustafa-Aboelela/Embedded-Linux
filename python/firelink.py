print("1:youtube")
print("2:google")
print("3:github")
print("4:facebook")
c = int(input("enter  num of address you want"))
def firefox():
    if c == 1:
        return 'https://www.youtube.com/' 
    
    if c == 2:
        return 'http://google.co.kr'
    if c == 3:
        return 'https://github.com/'
    if c == 4:
        return 'https://www.facebook.com/?locale=ar_AR'