import os
import sys
import string

os.system('cls')


inputFile = str(input("Input the extension of the file you want to generate (All lowercase):  "))

print(inputFile)

#defining working extensions
extPy = ".py"
extCpp = ".cpp"
extCs = ".cs"
extHtml = ".html"

if inputFile == extPy:
    fileType = 1
elif inputFile == extCpp:
    fileType = 2
elif inputFile ==  extCs:
    fileType = 3
elif inputFile  == extHtml:
    fileType = 4


if fileType == 1 : # python
    py = open("base.py", "x")
    py.write("#made by Delta\n")
    py.write("\n")
    py.write("import sys\n")
    py.write("import os\n")
    

    print ("file generated")
    py.close()


elif fileType == 2 : # c++
    cpp = open("base.cpp", "x")
    cpp.write("//made by Delta\n")
    cpp.write("#include <iostream>\n")
    cpp.write("\n")
    cpp.write("int main() {\n")
    cpp.write("\n")
    cpp.write("}\n")

    print ("file generated")
    cpp.close()


elif fileType == 3: # csharp
    cs = open("base.cs", "x")
    cs.write("//made by Delta\n")
    cs.write("\n")
    cs.write("\n")
    cs.write("\n")
    cs.write("static void Main(string[] args) {")
    cs.write("\n")
    cs.write("\n")
    cs.write("}\n")

    
    print("file generated")
    cs.close()

elif fileType == 4:
	styleSheet = bool(input("Do you want a css styleSheet? (boolean):  "))
	html = open("index.html", "x")
	html.write("<!-- made by Delta -->\n")
	html.write("<!DOCTYPE html>\n")
	html.write("<html>\n")
	html.write("	<head>\n")
	html.write("\n")
	
	html.write("		<title>Basic Html File </title>\n")
	html.write('		<link rel ="stylesheet" type ="text/css"\n')
	html.write('		href="style.css">')
	html.write("\n")
	html.write("	</head>\n")
	html.write("\n")
	html.write("	<body>\n")
	html.write("\n")
	html.write("		<h1>Base file made by Delta</h1>\n")
	html.write("	</body>\n")

	print("file generated")
	html.close()
	css = open("style.css", "x")
	css.write("h1{\n")
	css.write("	color:lime;\n")
	css.write("}\n")

	print ("Css styleSheet generated")
	css.close()
