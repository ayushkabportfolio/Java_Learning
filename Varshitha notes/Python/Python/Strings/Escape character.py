##escape character
'''To insert characters that are illegal in a string, use an escape character.

An escape character is a ""backslash \ followed by the character you want to insert.""
                    if i want to use double quote "word" -- so thru escape char -->\"word\"

An example of an illegal character is a double quote inside a string that is surrounded by double quotes'''

'''
txt = "We are the so-called "Vikings" from the north."   #worng format
        inside double quote ,single quote should be used

but wht if we want to use double quote inside the double quote or similiar for single quote
    
    Therefore thru escape character \ backslash we can use it   
'''

'''   /" /' /t /n /b /r // '''

\"  Double quote

txt ="We are the so-called \"Vikings\" from the north."
print(txt)              #We are the so-called "Vikings" from the north.

\'	Single Quote

txt ='We are the so-called \'Vikings\' from the north.'
print(txt)              #We are the so-called 'Vikings' from the north.

\\	Backslash

txt = "helo world \\"
print(txt)              #helo world \
#--realtime example
path = "C:\\Program Files\\MyApp\\"
print(path)             #C:\Proram Files\MyApp\

\n	New Line

txt = "you are the one i wanted \nbut i dont want you"
print(txt)              #you are the one i wanted
                        #but i dont want you

\t	Tab

txt = "you are the one i wanted\tbut i dont want you"
print(txt)              #you are the one i wanted	but i dont want you

txt = "you\tare\tthe\tone\ti\twanted\tbut\ti\tdont\twant\tyou"
print(txt)              #you	are	the	one	i	wanted	but	i	dont	want	you

\r	Carriage Return

'''A carriage return is a control character used in text processing to move 
the cursor to the beginning of the current line without advancing to the next line. 
In Python, you can use the carriage return character \r to achieve this effect.'''

##in simple word it will print from where the \r is used
txt = "hello where r u \rworld,cool "
print(txt)                  #world,cool

\b	Backspace  - removes the back spaces

txt = "how \bare \byou"
print(txt)

txt = 'you\t\bare\t\bthe\t\bone\t\bi\t\bwanted\t\bbut\t\bi\t\bdont\t\bwant\t\byou'
print(txt)          #youaretheoneiwantedbutidontwantyou

\f	Form Feed
'''In some text editors or older systems, you might see a visible indication of a form feed,
 but often it will just be displayed as a blank space or a special symbol.'''

print("First Page\fSecond Page")   #First PageSecond Page

\ooo	Octal value
'''A backslash followed by three integers will result in a octal value
by useing ASCII values making word'''

a = '\110\145\154\154\157'
print(a)                    #Hello

\xhh	Hex value

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)          #Hello
