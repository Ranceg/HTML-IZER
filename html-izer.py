#HTML-IZER * Phenomenal_alien * 12/29/2019

#bugz ~
#===*===*===*===*===*===*===*===*===*===*===*===*===*===#
#must sequntially append txt to file                    #
#appears to be printing The keywords in the document,   #
#but not even printing the content                      #
#multiline frameIn/out variables                        #
#===*===*===*===*===*===*===*===*===*===*===*===*===*===#
'''
def __init__(self, name):
    self.name = name    # instance variable unique to each instance
'''
def tags(keyword):
    #possible tags list
    h = "<h{0}0>{1}</h{0}>".format(ran, text) #header
    b = "<b>%s</b>" %text #bold
    return str(keyword)
    

def framing():

    title = input("Title?: ")
    
    #HTML Document first input
    frameIn = [
    "!DOCTYPE html> \n",
    "<html> \n",
    "<head> \n\t",
    "   <title>%s<title> \n" %title,
    "</head> \n",
    "<body> \n\t"
    ]
    
    #HTML Document final input
    frameOut = """</body> \n"
    "<html> \n"""


    #call tags function with keyword parameter
    kw = tags(keyword)
    #full rendered HTML Doc
    frame = str(frameIn), str(kw), str(frameOut)
    return str(frame)

def main():
    global keyword, ran, text
    ran = 1
    strRan = str(ran)
    #tag identifier
    keyword = input(str("keyword?: "))
    #If user calls for the header tag setup
    if keyword == "h":
        ran += 1 
    while True:
        text = input("Text?: ")
        writeFile()
        return "Ran %s times" %strRan

def writeFile():
    content = str(framing())
    for i in range(8):
        print(frameIn)
        i += 1
    rwa = "w+"
    filename = input("filename? = ")
    location = "C:/Users/Gnarly/Documents/Python Scripts/html-Ized"
    fileSrc = "{0}/{1}.html".format(location,filename)
    htmlFile= open(fileSrc, rwa)
    for line in content:
        print(line, end='')
        htmlFile.write(line)
    htmlFile.close()
    print("HTML File Succesully Designed!")
    print("Stored in %s" %location+filename)      


main()
