def chopper(slist, utext):
    chopped = []
    for word in slist:
        if utext != word[0:1]:
            del word
        else:
            word = word[1:]
            chopped.append(word)
    return chopped

chopper([good,hello],a)



