import random

def jogo_da_forca():
    palavras = ["python", "desenvolvimento", "computador", "programacao", "inteligencia"]
    palavra_secreta = random.choice(palavras)
    letras_acertadas = ["_" for _ in palavra_secreta]
    tentativas = 6
    letras_erradas = []

    print("🎉 Bem-vindo ao Jogo da Forca! 🎉")
    print("🔠 Tente adivinhar a palavra secreta letra por letra.")
    print("🛑 Você tem 6 tentativas. Boa sorte!\n")

    while tentativas > 0 and "_" in letras_acertadas:
        print("📜 Palavra: " + " ".join(letras_acertadas))
        print(f"❌ Letras erradas: {', '.join(letras_erradas) if letras_erradas else 'Nenhuma'}")
        print(f"❤️ Tentativas restantes: {tentativas}\n")

        letra = input("👉 Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("⚠️ Por favor, digite apenas uma letra válida.")
            continue

        if letra in letras_acertadas or letra in letras_erradas:
            print("⛔ Você já tentou essa letra! Tente outra.\n")
            continue

        if letra in palavra_secreta:
            print("🎯 Boa! A letra está na palavra. 😄\n")
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    letras_acertadas[i] = letra
        else:
            print("😢 Ops! Essa letra não está na palavra.\n")
            letras_erradas.append(letra)
            tentativas -= 1

    if "_" not in letras_acertadas:
        print("\n🎉 Parabéns! Você adivinhou a palavra: " + "".join(palavra_secreta) + " 🎊")
    else:
        print("\n💀 Você perdeu! A palavra era: " + palavra_secreta)
        print("🪦 Melhor sorte na próxima vez!")

jogo_da_forca()
