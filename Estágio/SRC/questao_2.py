def verificar_letra_a(texto):
    contagem = texto.lower().count('a')
    
    if contagem > 0:
        print(f"A letra 'a' (maiúscula ou minúscula) aparece {contagem} vez(es) no texto.")
    else:
        print("A letra 'a' não está presente no texto.")

texto = input("Digite um texto: ")
verificar_letra_a(texto)