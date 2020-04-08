input = open('ex8b.txt', 'r') 
lines = input.readlines() 
  
file1 = open('points_class_0.txt', 'w') 
file2 = open('points_class_1.txt', 'w') 



for line in lines: 
    split = line.split()
    file = file1 if split[0] == '1' else file2
    x = split[1][2:]
    y = split[2][2:]
    file.write(x + ' ' + y + '\n')


file1.close() 
file2.close() 