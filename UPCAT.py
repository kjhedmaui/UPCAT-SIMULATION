import time
import datetime

LanguageKey = {
"L1":"B",
"L2":"B",
"L3":"A",
"L4":"D",
"L5":"C",
"L6":"B",
"L7":"A",
"L8":"B",
"L9":"D",
"L10":"A",
"L11":"C",
"L12":"D",
"L13":"A",
"L14":"C",
"L15":"A",
"L16":"C",
"L17":"B",
"L18":"A",
"L19":"C",
"L20":"C",
"L21":"C",
"L22":"B",
"L23":"A",
"L24":"D",
"L25":"C",
"L26":"A",
"L27":"C",
"L28":"D",
"L29":"A",
"L30":"B",
"L31":"B",
"L32":"B",
"L33":"D",
"L34":"A",
"L35":"C",
"L36":"C",
"L37":"A",
"L38":"A",
"L39":"D",
"L40":"C",
"L41":"D",
"L42":"B",
"L43":"A",
"L44":"D",
"L45":"C",
"L46":"D",
"L47":"B",
"L48":"A",
"L49":"C",
"L50":"C",
"L51":"D",
"L52":"A",
"L53":"B",
"L54":"A",
"L55":"D",
"L56":"A",
"L57":"D",
"L58":"A",
"L59":"D",
"L60":"A",
"L61":"D",
"L62":"D",
"L63":"C",
"L64":"A",
"L65":"B",
"L66":"A",
"L67":"A",
"L68":"C",
"L69":"C",
"L70":"C",
"L71":"D",
"L72":"B",
"L73":"D",
"L74":"D",
"L75":"B",
"L76":"D",
"L77":"D",
"L78":"B",
"L79":"C",
"L80":"A",
"L81":"D",
"L82":"A",
"L83":"A",
"L84":"B",
"L85":"B",
"L86":"C",
"L87":"D",
"L88":"A",
"L89":"B",
"L90":"B",
"L91":"D",
"L92":"B",
"L93":"A",
"L94":"D",
"L95":"D",
"L96":"A",
"L97":"B",
"L98":"C",
"L99":"B",
"L100":"A",
"L101":"D",
"L102":"B",
"L103":"A",
"L104":"A",
"L105":"A",
"L106":"D",
"L107":"A",
"L108":"B",
"L109":"A",
"L110":"D",
"L111":"B",
"L112":"A",
"L113":"A",
"L114":"D",
"L115":"A",
"L116":"B",
"L117":"A",
"L118":"C",
"L119":"A",
"L120":"C",
"L121":"D",
"L122":"C",
"L123":"A",
"L124":"D",
"L125":"B",
"L126":"A",
"L127":"A",
"L128":"D",
"L129":"B",
"L130":"C",
"L131":"B",
"L132":"B",
"L133":"C",
"L134":"D",
"L135":"A",
"L136":"D",
"L137":"B",
"L138":"C",
"L139":"A",
"L140":"C",
"L141":"C",
"L142":"B",
"L143":"A",
"L144":"C",
"L145":"D",
"L146":"D",
"L147":"C",
"L148":"D",
"L149":"B",
"L150":"A",
}

ScienceKey = {
"S1":"D",
"S2":"A",
"S3":"A",
"S4":"A",
"S5":"D",
"S6":"B",
"S7":"A",
"S8":"A",
"S9":"D",
"S10":"D",
"S11":"B",
"S12":"D",
"S13":"D",
"S14":"A",
"S15":"B",
"S16":"C",
"S17":"C",
"S18":"A",
"S19":"D",
"S20":"A",
"S21":"C",
"S22":"A",
"S23":"B",
"S24":"B",
"S25":"A",
"S26":"D",
"S27":"C",
"S28":"C",
"S29":"D",
"S30":"A",
"S31":"B",
"S32":"B",
"S33":"A",
"S34":"C",
"S35":"D",
"S36":"A",
"S37":"D",
"S38":"B",
"S39":"D",
"S40":"B",
"S41":"C",
"S42":"B",
"S43":"D",
"S44":"B",
"S45":"A",
"S46":"A",
"S47":"A",
"S48":"C",
"S49":"D",
"S50":"C",
"S51":"B",
"S52":"C",
"S53":"D",
"S54":"D",
"S55":"C",
"S56":"A",
"S57":"B",
"S58":"C",
"S59":"C",
"S60":"A",
"S61":"D",
"S62":"A",
"S63":"D",
"S64":"B",
"S65":"D",
"S66":"B",
"S67":"A",
"S68":"B",
"S69":"B",
"S70":"C",
"S71":"A",
"S72":"A",
"S73":"A",
"S74":"B",
"S75":"D",
"S76":"B",
"S77":"D",
"S78":"D",
"S79":"D",
"S80":"A",
"S81":"A",
"S82":"D",
"S83":"C",
"S84":"A",
"S85":"C",
"S86":"A",
"S87":"C",
"S88":"D",
"S89":"D",
"S90":"B",
"S91":"A",
"S92":"A",
"S93":"A",
"S94":"D",
"S95":"A",
"S96":"B",
"S97":"A",
"S98":"C",
"S99":"A",
"S100":"A",
}

MathKey = {
"M1":"A",
"M2":"D",
"M3":"D",
"M4":"A",
"M5":"C",
"M6":"B",
"M7":"C",
"M8":"B",
"M9":"B",
"M10":"A",
"M11":"B",
"M12":"B",
"M13":"D",
"M14":"A",
"M15":"D",
"M16":"C",
"M17":"D",
"M18":"B",
"M19":"C",
"M20":"D",
"M21":"D",
"M22":"A",
"M23":"B",
"M24":"B",
"M25":"D",
"M26":"C",
"M27":"D",
"M28":"D",
"M29":"A",
"M30":"C",
"M31":"D",
"M32":"D",
"M33":"A",
"M34":"D",
"M35":"A",
"M36":"C",
"M37":"B",
"M38":"B",
"M39":"D",
"M40":"A",
"M41":"D",
"M42":"D",
"M43":"C",
"M44":"D",
"M45":"C",
"M46":"A",
"M47":"D",
"M48":"D",
"M49":"D",
"M50":"D",
"M51":"B",
"M52":"B",
"M53":"B",
"M54":"B",
"M55":"C",
"M56":"A",
"M57":"A",
"M58":"C",
"M59":"D",
"M60":"D",
"M61":"C",
"M62":"A",
"M63":"D",
"M64":"D",
"M65":"B",
"M66":"D",
"M67":"C",
"M68":"D",
"M69":"B",
"M70":"A",
"M71":"C",
"M72":"D",
"M73":"B",
"M74":"C",
"M75":"B",
"M76":"D",
"M77":"A",
"M78":"C",
"M79":"C",
"M80":"C",
"M81":"D",
"M82":"B",
"M83":"A",
"M84":"C",
"M85":"C",
"M86":"A",
"M87":"A",
"M88":"B",
"M89":"C",
"M90":"D",
"M91":"A",
"M92":"C",
"M93":"B",
"M94":"B",
"M95":"C",
"M96":"B",
"M97":"C",
"M98":"C",
"M99":"B",
"M100":"B"
}

ReadingKey = {
"R1":"A",
"R2":"C",
"R3":"B",
"R4":"C",
"R5":"D",
"R6":"B",
"R7":"D",
"R8":"A",
"R9":"C",
"R10":"B",
"R11":"D",
"R12":"C",
"R13":"C",
"R14":"D",
"R15":"C",
"R16":"B",
"R17":"D",
"R18":"B",
"R19":"D",
"R20":"B",
"R21":"C",
"R22":"A",
"R23":"D",
"R24":"B",
"R25":"D",
"R26":"C",
"R27":"A",
"R28":"D",
"R29":"B",
"R30":"C",
"R31":"A",
"R32":"D",
"R33":"A",
"R34":"B",
"R35":"D",
"R36":"D",
"R37":"B",
"R38":"B",
"R39":"A",
"R40":"A",
"R41":"C",
"R42":"B",
"R43":"A",
"R44":"C",
"R45":"D",
"R46":"A",
"R47":"C",
"R48":"B",
"R49":"A",
"R50":"D",
"R51":"D",
"R52":"D",
"R53":"B",
"R54":"B",
"R55":"C",
"R56":"D",
"R57":"B",
"R58":"A",
"R59":"D",
"R60":"B",
"R61":"D",
"R62":"A",
"R63":"C",
"R64":"B",
"R65":"C",
"R66":"D",
"R67":"B",
"R68":"C",
"R69":"C",
"R70":"D",
"R71":"A",
"R72":"C",
"R73":"A",
"R74":"B",
"R75":"D",
"R76":"C",
"R77":"B",
"R78":"D",
"R79":"A",
"R80":"C",
"R81":"D",
"R82":"A",
"R83":"B",
"R84":"B",
"R85":"C",
"R86":"B",
"R87":"B",
"R88":"B",
"R89":"C",
"R90":"C",
"R91":"B",
"R92":"C",
"R93":"C",
"R94":"D",
"R95":"A",
"R96":"B",
"R97":"C",
"R98":"C",
"R99":"A",
"R100":"A",
"R101":"D",
"R102":"C",
"R103":"B",
"R104":"D",
"R105":"A",
"R106":"D",
"R107":"D",
"R108":"A",
"R109":"B",
"R110":"B",
"R111":"B",
"R112":"D",
"R113":"A",
"R114":"A",
"R115":"C",
"R116":"B",
"R117":"A",
"R118":"B",
"R119":"A",
"R120":"B",
"R121":"C",
"R122":"D",
"R123":"C",
"R124":"A",
"R125":"B",
"R126":"C",
"R127":"A",
"R128":"D",
"R129":"D",
"R130":"C",
"R131":"B",
"R132":"A",
"R133":"D",
"R134":"C",
"R135":"B",
"R136":"A",
"R137":"D",
"R138":"C",
"R139":"B",
"R140":"A",
"R141":"C",
"R142":"D",
"R143":"B",
"R144":"C",
"R145":"D",
"R146":"A",
"R147":"C",
"R148":"C",
"R149":"C",
}

print("UPCAT SIMULATION (Based on Filipiknow's Ultimate UPCAT PREP 2018)\n")
input("hit enter to Proceed.")
print("\nDisclaimer: this program only serves as an as a sort of an 'answer sheet' and will not display the questions.\n"
      "To start off, please download the free pdf here: https://filipiknow.net/wp-content/uploads/2018/11/Ultimate-UPCAT-Prep-ebook-2.pdf\n"
      "The review guide will contain the questions to be answered as well as the respective answer keys.\n"
      "Once you have the review material. You can immediately proceed answering.\n"
      "Note that once the test is started, you should finish it in one sitting or else you will have to START ALL OVER AGAIN\n")
input("hit enter to Proceed.")
print("\nDeveloper's note: This program is not perfect because I am not that good at programming yet.\n"
      "If there are problems and suggestions. You can contact me at @Kajiyummy on Twitter or\n"
      "Kjhedmaui@gmail.com. Hope this program can help you in your review for UPCAT. -Kaji\n")
input("hit enter to Proceed.")
print("\nNotes: *Erasures are not allowed in the program\n"
      "*You should take your time on each test. Developer recommends one or two tests a day.\n"
      "*Each of the tests are lengthy, you can take breaks in between sessions, but DO NOT CLOSE the program\n"
      "*Progress is not saved\n"
      "*a Log file will be made in the same folder where the rar file is or where the python file is. filename: [yourname]-log.txt\n")
input("hit enter to Proceed.")
run = True
Username = input("\nWhat is your name?")
log = open(Username + "-log.txt","a")
Valid = ["A","B","C","D"]
print("\nHello " + Username + ", welcome to the UPCAT simulation.")
while run == True:
    sub = input("What subject do you want to take?(Language/Science/Math/Reading) enter 'Exit' to finish the session:").upper()
    if sub == "LANGUAGE" or sub == "SCIENCE" or sub == "MATH" or sub == "READING":
        while sub == "LANGUAGE" or sub == "SCIENCE" or sub == "MATH" or sub == "READING":
            if sub == "LANGUAGE":
                n = 0
                lang = True
                print("\n\n\n\n\n\nLANGUAGE PROFICIENCY TEST:")
                print("START")
                ans = ""
                LangAnswers = []
                while lang == True:
                    n = n + 1
                    ans = input(str(n) + ". ").upper()
                    if ans not in Valid:
                        n = n - 1
                        print("Invalid answer. Going back...\n")
                    else:
                        LangAnswers.append(ans)
                        if n == 150:
                            lang = False
                c = 0
                t = 0
                p = 0
                check = ""
                print("\nRESULTS: ")
                log.write(Username + "'s Language Proficiency Exam Summary (" + str(datetime.datetime.now()) + "):\n")
                for Lanswer in LangAnswers:
                    t = t + 1
                    if Lanswer == LanguageKey["L" + str(t)]:
                        check = "Correct"
                        c = c + 1
                    else:
                        check = "Incorrect"
                    print(str(t) + ". " + Lanswer + " - " + check)
                    log.write(str(t) + ". " + Lanswer + " - " + check + "\n")
                p = (c / t) * 100
                p = round(p, 2)
                print("\nLanguage Proficiency Score: " + str(c) + "/" + str(t))
                print("Rating: " + str(p) + "%\n\n")
                log.write("\nLanguage Proficiency Score: " + str(c) + "/" + str(t))
                log.write("\nRating: " + str(p) + "%\n\n\n\n")
                retry = True
                while retry == True:
                    sub = input(Username + ", do you want to try again or proceed with other subjects?(Language/Science/Math/Reading) Enter 'Exit' to exit:").upper()
                    if sub == "LANGUAGE" or sub == "SCIENCE" or sub == "MATH" or sub == "READING":
                        retry = False
                    elif sub == "EXIT":
                        log.close()
                        retry = False
                        print("Thanks for using my program! -Kaji")
                        time.sleep(3)
                        run = False
                    else:
                        print("Invalid input, please try again.")
                        retry = True
            if sub == "SCIENCE":
                n = 0
                sci = True
                print("\n\n\n\n\n\nSCIENCE TEST:")
                print("START")
                ans = ""
                SciAnswers = []
                while sci == True:
                    n = n + 1
                    ans = input(str(n) + ". ").upper()
                    if ans not in Valid:
                        n = n - 1
                        print("Invalid answer. Going back...\n")
                    else:
                        SciAnswers.append(ans)
                        if n == 100:
                            sci = False
                c = 0
                t = 0
                check = ""
                print("\nRESULTS: ")
                log.write(Username + "'s Science Exam Summary (" + str(datetime.datetime.now()) + "):\n")
                for Sanswer in SciAnswers:
                    t = t + 1
                    if Sanswer == ScienceKey["S" + str(t)]:
                        check = "Correct"
                        c = c + 1
                    else:
                        check = "Incorrect"
                    print(str(t) + ". " + Sanswer + " - " + check)
                    log.write(str(t) + ". " + Sanswer + " - " + check + "\n")
                p = (c / t) * 100
                p = round(p, 2)
                print("\nScience Score: " + str(c) + "/" + str(t))
                print("Rating: " + str(p) + "%\n\n")
                log.write("\nScience Score: " + str(c) + "/" + str(t))
                log.write("\nRating: " + str(p) + "%\n\n\n\n")
                retry = True
                while retry == True:
                    sub = input(Username + ", do you want to try again or proceed with other subjects?(Language/Science/Math/Reading) Enter 'Exit' to exit:").upper()
                    if sub == "LANGUAGE" or sub == "SCIENCE" or sub == "MATH" or sub == "READING":
                        retry = False
                    elif sub == "EXIT":
                        log.close()
                        retry = False
                        print("Thanks for using my program! -Kaji")
                        time.sleep(3)
                        run = False
                    else:
                        print("Invalid input, please try again.")
                        retry = True
            if sub == "MATH":
                n = 0
                math = True
                print("\n\n\n\n\n\nMATHEMATICS TEST:")
                print("START")
                ans = ""
                MathAnswers = []
                while math == True:
                    n = n + 1
                    ans = input(str(n) + ". ").upper()
                    if ans not in Valid:
                        n = n - 1
                        print("Invalid answer. Going back...\n")
                    else:
                        MathAnswers.append(ans)
                        if n == 100:
                            math = False
                c = 0
                t = 0
                check = ""
                print("\nRESULTS: ")
                log.write(Username + "'s Mathematics Exam Summary (" + str(datetime.datetime.now()) + "):\n")
                for Manswer in MathAnswers:
                    t = t + 1
                    if Manswer == MathKey["M" + str(t)]:
                        check = "Correct"
                        c = c + 1
                    else:
                        check = "Incorrect"
                    print(str(t) + ". " + Manswer + " - " + check)
                    log.write(str(t) + ". " + Manswer + " - " + check + "\n")
                p = (c / t) * 100
                p = round(p, 2)
                print("\nMathematics Score: " + str(c) + "/" + str(t))
                print("Rating: " + str(p) + "%\n\n")
                log.write("\nMathematics Score: " + str(c) + "/" + str(t))
                log.write("\nRating: " + str(p) + "%\n\n\n\n")
                retry = True
                while retry == True:
                    sub = input(Username + ", do you want to try again or proceed with other subjects?(Language/Science/Math/Reading) Enter 'Exit' to exit:").upper()
                    if sub == "LANGUAGE" or sub == "SCIENCE" or sub == "MATH" or sub == "READING":
                        retry = False
                    elif sub == "EXIT":
                        log.close()
                        retry = False
                        print("Thanks for using my program! -Kaji")
                        time.sleep(3)
                        run = False
                    else:
                        print("Invalid input, please try again.")
                        retry = True
            if sub == "READING":
                n = 0
                read = True
                print("\n\n\n\n\n\nREADING COMPREHENSION TEST:")
                print("START")
                ans = ""
                ReadAnswers = []
                while read == True:
                    n = n + 1
                    ans = input(str(n) + ". ").upper()
                    if ans not in Valid:
                        n = n - 1
                        print("Invalid answer. Going back...\n")
                    else:
                        ReadAnswers.append(ans)
                        if n == 149:
                            read = False
                c = 0
                t = 0
                check = ""
                print("\nRESULTS: ")
                log.write(Username + "'s Reading Comprehension Exam Summary (" + str(datetime.datetime.now()) + "):\n")
                for Ranswer in ReadAnswers:
                    t = t + 1
                    if Ranswer == ReadingKey["R" + str(t)]:
                        check = "Correct"
                        c = c + 1
                    else:
                        check = "Incorrect"
                    print(str(t) + ". " + Ranswer + " - " + check)
                    log.write(str(t) + ". " + Ranswer + " - " + check + "\n")
                p = (c / t) * 100
                p = round(p, 2)
                print("\nReading Comprehension Score: " + str(c) + "/" + str(t))
                print("Rating: " + str(p) + "%\n\n")
                log.write("\nReading Comprehension Score: " + str(c) + "/" + str(t))
                log.write("\nRating: " + str(p) + "%\n\n\n\n")
                retry = True
                while retry == True:
                    sub = input(Username + ", do you want to try again or proceed with other subjects?(Language/Science/Math/Reading) Enter 'Exit' to exit:").upper()
                    if sub == "LANGUAGE" or sub == "SCIENCE" or sub == "MATH" or sub == "READING":
                        retry = False
                    elif sub == "EXIT":
                        log.close()
                        retry = False
                        print("Thanks for using my program! -Kaji")
                        time.sleep(3)
                        run = False
                    else:
                        print("Invalid input, please try again.")
                        retry = True
    elif sub == "EXIT":
        log.close()
        print("Thanks for using my program! -Kaji")
        time.sleep(3)
        run = False
    else:
        print("You have entered an invalid input. Please try again.")
        run = True
