count = 0
while True: # while True šeit piemērots jo nezinam cik ierakstu lietotājs ievadīs
    text = input("Teksts (beigt — iziet): ")
    # if text.strip().lower() == "beigt": #Strādās arī Beigt, BEIGT, beigt utt. jo .lower() padara visu mazos burtos
    #     break
    # mēs varētu būt vēl draudzīgāki un ignorēt arī liekās atstarpes
    if "beigt" in text.lower().replace(" ", ""): # šeit mēs noņemam visas atstarpes un tad pārbaudam vai ir beigt
        # strādās ar "ES gribu beigt"
        # strādas ar es griiibu b E  igt tiešām utt
        # atceramies ka pats text netiek modificēts, ja gribam kaut ko mainīt tad jāizveido jauns string
        break
    # šeit varētu šo tekstu pievienot teiksim datu bāzei vai sarakstam, bet šeit tikai skaitīsim
    count += 1
print("Ieraksti:", count)