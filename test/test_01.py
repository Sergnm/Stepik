words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

result = {words[i]: [ ord(words[i][j]) for j in range(len(list(words[i]))) ]  for i in range(len(words))}
print(result)