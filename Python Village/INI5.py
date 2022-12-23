'''Python village
5. Working with files'''

'''Given: A file containing at most 1000 lines.
Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.'''


file_name=input("enter relative path:")
text_file=open(file_name,'r')
output_file=open("Python Village/output.txt",'w')
text_file.readline()
for line in text_file:
    output_file.write(line)
    text_file.readline()

print("your output text file is found under Python village by the name of output.txt")