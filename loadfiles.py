import subprocess

#count lines in textfile
lines = len(open('get.txt').readlines())

#load the file
with open("get.txt","r") as f:
    list = f.read().split("\n")
#    print(list[0])
#    print(type(list[0]))
#    cmd = list[2]
#    subprocess(cmd)

#the first line is function name
function_name = list[0]

#make function command
cmd_function = ["sudo", "./build/sfc_funciton"]
cmd_function.append(function_name)

#port number change
file_name = "build/clientyolo.py"

with open(file_name,encoding="cp932") as f:
    data_lines = f.read()

port = "PORT = "+ list[1]
print(port)
data_lines = data_lines.replace("PORT = 33117",port)

write_file = "build/clientyolo2.py"
with open(write_file,mode= "w",encoding="cp932") as f:
    f.write(data_lines)

#make docker command
cmd_docker = []

for num in range(2,lines):
    cmd_docker.append(list[num])

print(cmd_docker)
subprocess.call(cmd_docker)

