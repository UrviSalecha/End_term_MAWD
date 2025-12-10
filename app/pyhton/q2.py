#File handling create count_words (filename)
# opens a text file 
# counts number of times word appear
filename="C:\Users\LNMIIT\data.txt"
def count_words(filename,word):
    try:
        with open(filename,'r') as f:
            content=f.read()
            words=content.split()
            count=words.count(word)
            return count
    except FileNotFoundError:
        return "File not found"
    word="the"
    print(f"The word '{word}' appears {count_words(filename,word)} times in the file.")
count_words(filename,word)
