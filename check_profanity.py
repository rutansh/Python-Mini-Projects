import urllib
def read_text():
    quotes=open(r"C:\Users\Dell\Documents\movies_quotes.txt")
    contents_of_file=quotes.read()
   # print(contents_of_file)
    check_profanity(contents_of_file)
    quotes.close()
def check_profanity(text_to_check):
    connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output=connection.read()
    
    connection.close()
    if "true" in output:
        print("profanity word found..!")
    else:
        print("no profanity word found in the given file")
read_text()
