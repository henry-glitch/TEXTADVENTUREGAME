#title
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



#death message
def death():
    print("                                 _____  _____                           ")
    print("                                <     `/     |                          ")
    print("                                 >          (                           ")
    print("                                |   _     _  |                          ")
    print("                                |  |_) | |_) |                          ")
    print("                                |  | \ | |   |                          ")
    print("                                |            |                          ")
    print("                 ______.______%_|            |__________  _____         ")
    print("               _/                                       \|     |        ")
    print("              |               D U M B   A S S                  <        ")
    print("              |_____.-._________              ____/|___________|        ")
    print("                                | * 10/9/30  |                          ")
    print("                                |            |                          ")
    print("                                |            |                          ")
    print("                                |            |                          ")
    print("                                |   _        <                          ")
    print("                                |__/         |                          ")
    print("                                 / `--.      |                          ")
    print("                               %|            |%                         ")
    print("                           |/.%%|          -< @%%%                      ")
    print("                           `\%`@|     v      |@@%@%%                    ")
    print("                         .%%%@@@|%    |    % @@@%%@%%%%                 ")
    print("                    _.%%%%%%@@@@@@%%_/%\_%@@%%@@@@@@@%%%%%%             ")


#room2


def man():
    print("you run towards the  warehouse and slam the door behind yourself The man jolts around and aims a crossbow at our head")
    print("            .-.        ")
    print("           /  \\       ")                      
    print("      .---/-+--||      ")                      
    print("     |  K=====++->     ")                       
    print("      '---\-+--||      ")                         
    print("           \  //       ")                         
    print("            `-'        ")
    print("Do you Either")
    print("a) talk to him")
    print("b) Go and try and kill the man")
    b = input("Enter a or b: ")
    if b == "a":
        print("you call out to him explaining you cause no harm")
        death()
    elif b == "b":
        print("The last thing you ever fell is cold metal slide through your head")
        print(\n)
        death()
    else:
        print("That was not an option.  Game Over")



#introduction
print("The year was 2036 a new Pathogen was released by a terrorist organiztion wanting to create a new world  ")
print("order it was spread from across the world before anyone noticed.The virus had a rabies gene that lead humans")
print("2 months later the world is in collapse businuses, governments and civilisation fell into collapse the people")
print("Who are still alive search in the shadows for what is left trying to rebuild there reality.")
print("\n")
print("\n")
#room 1
print("You Sprint down the street running from the zombies,you hear voices coming from inside a abondened warehouse.")
print("Do you Either")
print("a) keep on running.")
print("b) Go  and investigate")
x = input("Enter a or b: ")
if x == "a":
    print("The zombies hunt you down and trap you against the wall You died")
    death()
elif x == "b":
    print("You go in to investigate.")
    print("A man dressed in tattered old clothing turns around aims his crossbow at your head")
    man()
else:
    print("That was not an option.  Game Over")


