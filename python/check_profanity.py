import urllib

def read_text():
    quotes = open("C:\Users\Candice\Documents\WebDev\udacity\python\movie_quotes.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("No curse words found.")
    connection.close()
    
read_text()
