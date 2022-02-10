file_handle = open("test.txt")
lines = file_handle.readlines()
print(lines)
file_handle.close()

file_handle = open("test.txt")
file_data= file_handle.read()
file_lines = file_data.split("#")
print(file_lines)
file_handle.close()

file_handle = open("test.txt")
numbers = []
while True:
    line = file_handle.readline()
    if line == "":break
    numbers.append(line.strip())
print(numbers)
file_handle.close()


