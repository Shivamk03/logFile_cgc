print('''
░██████╗██╗░░██╗██╗██╗░░░██╗░█████╗░███╗░░░███╗
██╔════╝██║░░██║██║██║░░░██║██╔══██╗████╗░████║
╚█████╗░███████║██║╚██╗░██╔╝███████║██╔████╔██║
░╚═══██╗██╔══██║██║░╚████╔╝░██╔══██║██║╚██╔╝██║
██████╔╝██║░░██║██║░░╚██╔╝░░██║░░██║██║░╚═╝░██║
╚═════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝''')
f=open("log.txt","r")
o=open("Output.txt","a")
print("IP\t\tDATE/TIME\t\t\tREQUEST TYPE\tPROTOCOL/VERSION\tSTATUS CODE\tPACKET SIZE\n")
o.write("IP\t\t\t\t\tDATE/TIME\t\t\t\t\tREQUEST TYPE\tPROTOCOL/VERSION\tSTATUS CODE\tPACKET SIZE\n\n")
print()
lines=f.readlines()
for line in lines:
    line=line.replace('"',"")
    line=line.split(" ")
    for i in range(len(line[0]),16):
        o.write(" ")
    o.write(f"{line[0]}\t{line[3]+line[4]}\t\t{line[5]}\t\t\t{line[7]}\t\t\t{line[8]}\t\t\t{line[9]}\n")
    print(f"{line[0]}\t{line[3]+line[4]}\t{line[5]}\t\t\t{line[7]}\t\t{line[8]}\t\t\t{line[9]}")
    
    