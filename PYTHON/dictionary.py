w = set()

def check(word):
        if word.lower() in w:
             return True
        else:
            return False

def load(dictionary):
        file = open(dictionary, "r")
        for line in file:
            w.add(line.rstrip())
        file.close()
        return True

def size():
    return(len(w))

def unload():
    return True

