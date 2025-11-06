with open('cat.jpg','rb') as rf:
    with open('cat_copy.jpg','wb') as wf:
        for line in rf:
            wf.write(line)