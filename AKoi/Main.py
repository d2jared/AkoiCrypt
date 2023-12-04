import Akoi_Crypt as crypt
import chat_serveur as serveur
import chat_client as client

def logo():
    print("\n\n")
    print("                    .,,.    ..")
    print("                  z$$$$$b c$$$L")
    print("               ,,$$$$$$$F,,'?$$                .,,,")
    print("          ,c' z$$$$$$$$',$$$c`F .          ,c$$$$,.")
    print("         ,$' d$$$$$$P',d$$$$$b'F3$ccc,,cc$$$$$$$$$$$c")
    print("        d$' d$$$$$$P,d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("        4$F 4$$$PF',c$$$?$$$$' $c$$$$$$$$$$$$$$$$$$$'.")
    print("        $PL 4$$zc$'$$PLd$$$$$P 3$$$$$$$$$$$$$$$$$$$$$$F")
    print("        $ L '$$$$P,$$$"" d$$ : ?$$$$$$$$$$$$$$$$$$$$$P")
    print("         J$L d$P',$$$L,-,$$$b;h $$$$$$$$$$$$$$$$$$$P',c")
    print("         ?$$.$ '$$$$$$$$$$$$c;F $$$$$$$$$$$$$$$$?5,c$$$")
    print("         `$$'.'?,'L$$$$$$$$ :/,d$$$$$L'$$$$$$$$$$$$$$$'")
    print("          '$b'$cc,'$$$$$$$$cr,$$$$$$$?b,'?$$$$$$$$$$P'")
    print("            '?$$$$c`$$$bK''=d$$P??',r= ??$c,.'''',,")
    print(" `L c ,         F?$-'$$F `',;!!>',nMMMM ;!!!!><$$c,                                           .o.       oooo                   o8o ")
    print("   '$ $   <>'MMMMMn'''' ,nMMMM  `!!!!!;,'?$$$$$bc                                            .888.      `888                   `'' ") 
    print("      ,$$    ,cb,`<, )MMMMMMMMMMM !;,````     ""C3$$$,                                        .8'888.      888  oooo   .ooooo.  oooo ")
    print("   $$$F ,c$$$$P'<> )L.,cc,,'TMe`!!!!!!   ,c$$$$$$$$P                                       .8' `888.     888 .8P'   d88' `88b `888 ")
    print("  3$$$$ $$P'        `4n,'''''''''''??'''.,,,       .,,xn,,.                               .88ooo8888.    888888.    888   888  888 ")
    print("  4$$$$cP'            `'4MMMMMMMP',==~',;;,.  -=MMMMMMMMMMM=                             .8'     `888.   888 `88b.  888   888  888 ")
    print("   $$P'                    ''_r=''.df:!!!!!!!!!;, ''''~=<                               o88o     o8888o o888o o888o `Y8bod8P' o888o")
    print("   `                      ,xP' xMMMMM                                                                                 by d2jared,")
    print("                     _,eM"",dfJMMMMMMM.`!!!!!!!!!!!!;")
    print("                  ,nMMP',dMMMLMMMMMMMMMe`!!!!!!!!!!!!>")
    print("              ,eMMMMP',MMMMMMMMMMMMMMMMMe`!!!!!!!!!!!!>")
    print("            eMMMMMM',dMMMMMMMMMMMMMMMMMMMr`!!!!!!!!!!!!")
    print("         ,dMMMMMMP',MMMMMMMMMMMMMMMMMMMMMM !!!!!!!!!!!!!")
    print("       ,dMMMMMMMP dMMMMMMMMMMMMMMMMMMMMMMM !!!!!!!!!!!!!")
    print("     ,MMMMMMMMM' dMMMMMMMMMMMMMMMMMMMMMMMM !!!!!!!!!!!>!")
    print("   eMMMMMMMMMMP MMMMMMMMMMMMMMMMMMMMMMMMMP !!!!!!!!!!!;!")
    print(" eMMMMMMMMMMMM dMMMMMMMMMMMMMMMMMMMMMMMMM ;!!!!!!!!!' !'")
    print("'4MMMMMMMMMMM'uMMMMMMMMMMMMMMMMMMMMMMMMM> !!!!!!!!!',!!")
    print(";!> ;,'MMMMM>;MMMMMMMMMMMMMMMMMMMMMMMMMM ,'4MM ,c ;;;;,.")
    print("TMMMMMMMMMMMMMM>;!!!!!!' ,!!', !!!!!!!!!!!!!!!!!!!!!!!'!      .,zc$$$c','")
    print(";!!!!!!!!!!!';!!!!!!!!!!!!!!!!!!!!!!!!:!!! ,!!!!! ;>'!!!!!>'$$$$$P???L ',")
    print("!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!'',!!!!!! ;!!> '$$'      ?P`b")
    print("!!!!!!!!!!! ,`'''!!!!!!!!!!!!!!!!!!!!', !!!!> !!!!! ?         -$E")
    print("!!!!!!!!!!! <<',;;,`` '``!!!>;`'!!!!!!!!!!!!!!!!!!!!!!!  !!!!!>'''`")
    print("   ``'''''!! `'dc,,zcc`;,``'!!!!!!!!!!!!!!!!!!!> !!!!!'")
    print("              ,$$$$$$$b`;, ``''!!!!!!!!!!!!!> ```")
    print("             ,$$$$$$$$$F   ````       ```````")
    print("            ,$$$$$$$$'")
    print("            $$$$$$P'")
    print("          ,$$$$$P'")
    print("         ,$$$$'")
    print("'$c-, , '$$$F")
    print(" '$$c?,%,4$F")
    print("  `?$c'c'4'")
    print("     4c`b")
    print("       '")
    print("\n\n")



def menu():
    print("\n\n")
    print("Welcome to Akoi\n")
    print("Menu : \n")
    print("1. Cypter\n")
    print("2. Decrypter\n")
    print("3. Se Connecter au Serveur\n")
    print("4. Crée un Serveur\n")
    print("5. Quitter\n")



    print("\n\n")

    choice = int(input("Enter your choice : "))

    match choice:
        case 1:
            plainText = input("Entrer un Texte à chiffrer : ")
            cipherText = crypt.Encrypt(plainText)
            print("Texte chiffré : ", cipherText)
        case 2:
            cipherText = input("Entrer un Texte à déchiffrer : ")
            cle = input("Entrer une clé : ")
            plainText = crypt.Decrypt(cipherText, cle)
            print("Texte déchiffré : ", plainText)
        case 3:
            client.main()
        case 4:
            serveur.main()
        case 5:
            exit()
        case _:
            print("Invalid choice")


while True:
    
        logo()
        menu()


