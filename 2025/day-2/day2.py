with open("list.txt", 'r') as file:
    id_ranges = file.readlines()[0].split(',')

sum = 0
for id_range in id_ranges:
    upper_bound = int(id_range.split('-')[1])
    counter = int(id_range.split('-')[0])
    while counter <= upper_bound:
       invalid = False
       test_str = str(counter)
       num_chunks = 2
       while num_chunks <= len(test_str):
           if(len(test_str) % num_chunks == 0):
               invalid = True
               index = int(len(test_str) / num_chunks)
               pattern = test_str[0:index]
               if (test_str.count(pattern) != num_chunks):
                   invalid = False

               if ( invalid):
                   print(counter)
                   sum += counter
                   break   
           num_chunks += 1                    
       counter += 1

print(sum)