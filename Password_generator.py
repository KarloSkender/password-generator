import random
def choose_length():
    while True:
        length=input("Unesi duljinu sifre :")
        if not length.isdigit():
            print("Niste unijeli broj!!!")
            continue
        else:
            length=int(length)
            if length<7 or length>16:
              print("Duljina treba biti izmedu 7 i 16 znakova,pokusaj ponovno.")
              continue
            else:
                break
    return length

def pool():
    lista = [
        ("Mala slova", "abcdefghijklmnoprstuvzyxw"),
        ("Velika slova", "ABCDEFGHIJKLMONPRSTUVZYXW"),
        ("Brojeve", "0123456789"),
        ("Simbole", "!?+*@#$%&")
    ]

    nazivi = []
    char_pool = ""

    while char_pool == "":
        for naziv, znakovi in lista:
            answer = input(f"Zelite li {naziv} u svojoj sifri (Da,Ne): ")

            if answer == 'Da':
                char_pool += znakovi
                nazivi.append(naziv)

        if char_pool == "":
            print("Niste nista odabrali pokusajte ponovno")

    return char_pool, nazivi

    
    

def password(length,everything,kategorije):
    lista=[("Mala slova","abcdefghijklmnoprstuvzyxw"),("Velika slova","ABCDEFGHIJKLMONPRSTUVZYXW"),
           ("Brojeve","0123456789"),("Simbole","!?+*@#$%&")]
    
    final_pass=""
    for naziv, znakovi in lista:
        if naziv in kategorije:
            final_pass += random.choice(znakovi)
    
    for i in range(length-len(kategorije)):
        rand1=random.choice(everything)
        final_pass+=rand1
    return final_pass

def random_shuffle(final):
    final2=list(final)
    random.shuffle(final2)
    return "".join(final2)




def main():
    
    duljina=choose_length()
    everything,kategorije=pool()
    final=password(duljina,everything,kategorije)
    final2=random_shuffle(final)
    print(final2)
if __name__ == "__main__":
    main()
    
    

    






    
   



