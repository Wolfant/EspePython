with open('t.txt', 'r') as story:
     story_words = []
     for line in story:
         line_words = line.split()
         for word in line_words:
             story_words.append(word)

