# atgriezīsim vārdu vārdnīcu no ievadīta teksta

def word_count(text: str, strip_chars: str = ".,!?;:") -> dict:
    """Atgriež vārdnīcu ar vārdu skaitu tekstā
    Arg:
    text: str
    Return:
    dict
    """
    words = text.split() # sadala vārdus sarakstā
    word_dict = {} # jauna vārdnīca
    for word in words:
        word = word.lower() # pārvēršam par maziem burtiem, lai nebūtu divi vienādi vārdi ar dažādiem burtiem
        # nākošās divas rindas noņem punktus, komatus, jautājuma zīmes, izsaukuma zīmes, semikolu un divpunkti no vārdiem
        for char in strip_chars:
            word = word.replace(char, "")
        if word in word_dict: # ja vārds jau ir vārdnīcā, tad palielinām skaitītāju par 1
            word_dict[word] += 1
        else: # ja vārds nav vārdnīcā, tad pievienojam to ar skaitītāju 1
            word_dict[word] = 1
    return word_dict

print(word_count("Rīgas Tehniskā universitāte ir lieliska universitāte! Tā tiešam ir lieliska!"))

# alternatīva būtu izmantot manu mīļo Counter
from collections import Counter
def word_count_with_counter(text: str, strip_chars: str = ".,!?;:") -> dict:
    """Atgriež vārdnīcu ar vārdu skaitu tekstā, izmantojot Counter
    Arg:
    text: str
    Return:
    dict
    """
    words = text.split() # sadala vārdus sarakstā
    # noņem punktus, komatus, jautājuma zīmes, izsaukuma zīmes, semikolu un divpunkti no vārdiem
    words = [word.lower().strip(strip_chars) for word in words]
    # piezimē strip nenoņem no vidus, bet tikai no sākuma un beigām, tāpēc ja vārds ir "lieliska!" tad tas kļūst par "lieliska", bet ja vārds ir "lielis!ka" tad tas paliek "lielis!ka"
    return dict(Counter(words)) # atgriež vārdnīcu ar vārdu skaitu

print(word_count_with_counter("Rīgas Tehniskā universitāte ir lieliska universitāte! Tā tiešam ir lieliska!"))
