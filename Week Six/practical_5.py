import re
sample_text = (" As Python s creator, I'd like to say a few words about its "+
              "origins adding a bit of personal philosophy. "+
              "Over six years ago in December I was looking for a "+
              "hobby programming project that would keep me occupied "+
              "during the week around Christmas. My office, "+
              "a government run research lab in Amsterdam would be closed "+
              "but I had a home computer and not much else on my hands "+
              " I decided to write an interpreter for the new scripting "+
              "language  I had been thinking about lately a descendant of ABC "+
              "that would appeal to UnixC hackers I chose Python as a "+
              "working title for   the project being in a slightly irreverent "+
              "mood and a big fan of Monty Python s Flying Circus.  ")

######################### EXERCISE 1 ##########################################

def split_text(text: str, delimiters:str="") -> list:
    result = []
    buffer = ""
    for c in text:
        if c in delimiters:
            if len(buffer) > 0:
                result.append(buffer)
                buffer=""
        else:
            buffer += c
    if(len(buffer) > 0):
        result.append(buffer)
    return result

def get_words_frequencies(text: str):
    # Gets all words and ignores cases and ignores punctuation
    words = re.findall(r'(\b[a-z]+)',text.lower())
    result = {}
    for word in words:
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1
    return result