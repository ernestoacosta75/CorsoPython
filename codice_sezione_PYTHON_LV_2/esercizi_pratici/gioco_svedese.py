def gioco_svedese(parola_o_fase):
    vocali = 'aeiouAEIOU'
    token = "o"
    nuova_parola_o_frase = ""
    for carattere in parola_o_fase:
        if carattere not in vocali:
            nuova_parola_o_frase += carattere + token + carattere
        else:
            nuova_parola_o_frase += carattere
    print("Parola o frase originale: {}".format(parola_o_fase))
    print("Parola o frase originale convertita: {}".format(nuova_parola_o_frase))

gioco_svedese(input("Inserire la parola o frase da convertire --> "))    
