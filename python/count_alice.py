file = open("Alice.txt","r")
word = ""
maxcount = 0 
words = []
 
for line in file:
    line = " ".join(line.split()) #remove all whitespace in line
    line_word = line.lower().replace(',','').replace('.','').split(" "); #divide the line to words 
    for w in line_word: 
        words.append(w); 

for i in range(0, len(words)): 
    count = 1; 
    for j in range(i+1, len(words)): 
        if(words[i] == words[j] ): 
            count = count + 1; 
 
    if(count > maxcount): 
        maxcount = count; 
        word = words[i]; 
 
print(word , maxcount)
file.close(); 