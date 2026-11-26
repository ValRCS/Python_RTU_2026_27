def format_name(name: str) -> str:
    """Atgriež tekstu noņemot tukšos simbols priekšā un aizmugurē
    Arg:
    name: str
    Return:
    str
    """
    result = name.strip().title()
    return result # varēju nemaz neglabāt un uzreiz return name.strip().title()

print(format_name("RĪGAS tehniskā UniVERSitāte"))

assert format_name("  ANNA  ") == "Anna"
assert format_name("jĀnis bĒrziņš") == "Jānis Bērziņš"
assert format_name("") == ""

print("Testi veiksmīgi!")

# taisam citu funkciju kurā pirmie divi vārdi būs ar lielo pārejie ar mazo.
def pirmie_capital_otrie_lower(name: str) -> str:
    """Atgriež tekstu, kur pirmie divi vārdi ar lielo burtu, pārējie ar mazo
    Arg:
    name: str
    Return:
    str
    """
    words = name.split() # sadala vārdus sarakstā
    # tātad mums ir dekonstruēts vārds sarakstā, tagad varam mainīt katru vārdu atsevišķi
    # for i in range(len(words)): # skaitās nePythonic, bet šeit derēs, jo mums vajag indeksu
    #     if i < 2: # tātad ar indeksu 0 un 1, jo pirmais vārds ir ar indeksu 0, otrais ar indeksu 1
    #         words[i] = words[i].capitalize() # pirmais burts lielais, pārējie mazie
    #     else:
    #         words[i] = words[i].lower() # visi mazie burti
    # pythonic veids ir izmantot enumerate, kas dod gan indeksu, gan vērtību
    for i, word in enumerate(words): # protams i un word ir jūsu izvēle, bet parasti lieto šos nosaukumus
        print(f"Indekss: {i}, Vārds: {word}")
        if i < 2: # atkal 0 un 1 ir pirmie divi vārdi
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()
    # kad apstrāde beigusies, tad saliekam vārdus atpakaļ vienā stringā
    result = " ".join(words) # saliek atpakaļ vienā stringā
    return result

print("" + pirmie_capital_otrie_lower("RĪGAS tehniskā UniVERSitāte uZVAR") + "!")