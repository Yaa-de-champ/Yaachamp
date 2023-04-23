# Ask for user input
name = input("Enter your name: ")
description = input("Describe yourself: ")

# Create HTML file with user input
with open("index.html", "w") as f:
    f.write("<html>\n")
    f.write("<head>\n")
    f.write("</head>\n")
    f.write("<body>\n")
    f.write("<center>\n")
    f.write("<h1>" + name + "</h1>\n")
    f.write("</center>\n")
    f.write("<hr />\n")
    f.write(description + "\n")
    f.write("<hr />\n")
    f.write("</body>\n")
    f.write("</html>")
