from operator import itemgetter
def get_num_words(content):
     t=content.split()
     print("Found {} total words ".format(len(t)))

     return t

def test(lowered_content):
    freq={}
    str1=lowered_content.lower()
    for c in set(str1):
        freq[c]=str1.count(c)
    return freq

def presentation(sort):
    attempted_solution=dict(sorted(sort.items(), key=itemgetter(1),reverse=True))


    for k,v in attempted_solution.items():
        if k.isalpha():
            print("{}: {}".format(k, v))



