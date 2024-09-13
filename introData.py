sentence = input("Input a sentence... ")
wordCount = 0

def outputSentence():
    print(f"You wrote, '{sentence}'.")
    print("...")
    print("...")
    print("...")
    wordCount = len(sentence.split())
    if wordCount == 1:
        print(f"There is 1 word in your sentence.")
    else:
        print(f"There are {wordCount} words in your sentence.")
outputSentence()