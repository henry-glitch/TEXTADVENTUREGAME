print("        ,----,                                                                                                                                          ")
print("      ,/   .`|                                                                                                                                          ")
print("    ,`   .'  :  ,---,                         ,---,                                                   ,--,                                              ")
print("  ;    ;     /,--.' |                        '  .' \      ,-.----.                                  ,--.'|             ,-.----.                         ")
print(".'___,/    ,' |  |  :                       /  ;    '.    \    /  \    ,---.                        |  | :             \    /  \                        ")
print("|    :     |  :  :  :                      :  :       \   |   :    |  '   ,'\                       :  : '             |   :    |  .--.--.              ")
print(";    |.';  ;  :  |  |,--.   ,---.          :  |   /\   \  |   | .\ : /   /   |   ,---.     ,--.--.  |  ' |        .--, |   | .\ : /  /    '     ,---.   ")
print("`----'  |  |  |  :  '   |  /     \         |  :  ' ;.   : .   : |: |.   ; ,. :  /     \   /       \ '  | |      /_ ./| .   : |: ||  :  /`./    /     \  ")
print("    '   :  ;  |  |   /' : /    /  |        |  |  ;/  \   \|   |  \ :'   | |: : /    / '  .--.  .-. ||  | :   , ' , ' : |   |  \ :|  :  ;_     /    /  | ")
print("    |   |  '  '  :  | | |.    ' / |        '  :  | \  \ ,'|   : .  |'   | .; :.    ' /    \__\/: . .'  : |__/___/ \: | |   : .  | \  \    `. .    ' / | ")
print("    '   :  |  |  |  ' | :'   ;   /|        |  |  '  '--'  :     |`-'|   :    |'   ; :__   ,\" .--.; ||  | '.'|.  \  ' | :     |`-'  `----.   \'   ;   /|")
print("    ;   |.'   |  :  :_:,''   |  / |        |  :  :        :   : :    \   \  / '   | '.'| /  /  ,.  |;  :    ; \  ;   : :   : :    /  /`--'  /'   |  / | ")
print("    '---'     |  | ,'    |   :    |        |  | ,'        |   | :     `----'  |   :    :;  :   .'   \  ,   /   \  \  ; |   | :   '--'.     / |   :    | ")
print("              `--''       \   \  /         `--''          `---'.|              \   \  / |  ,     .-./---`-'     :  \  \`---'.|     `--'---'   \   \  / ")
print("                           `----'                           `---`               `----'   `--`---'                \  ' ;  `---`                 `----'   ")
print("                                                                                                                  `--`                                  ")
print("\n")
print("The year was 2036 a new Pathogen was released by a terrorist organiztion wanting to create a new world  ")
print("order it was spread from across the world before anyone noticed.The virus had a rabies gene that lead humans")
print("2 months later the world is in collapse businuses, governments and civilisation fell into collapse the people")
print("Who are still alive search in the shadows for what is left trying to rebuild there reality.")
print("\n")
print("\n")
print("You Stumble down the street looking for food,you hear voices coming from inside a abondened warehouse.")
print("Do you Either")
print("a) Go and investigate.")
print("b) scavage in the nearby shop")
print("c) Read the instructions")
x = input("Enter a or b: ")
if x == "a":
    print("Someone hears your screams...")
    # Contine adventure Here
elif x == "b":
    print("You go in to investigate.")
    print("A man dressed in tattered old clothing turns around aims his crossbow at your head")
    death()
elif x == "c":
    print("Make sure to type the correct awnser text is all lowercase.")
else:
    print("That was not an option.  Game Over")

def death():
    print("you died")
