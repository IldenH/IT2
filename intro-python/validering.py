def validering():
    while True:
        try:
            tall = int(input("Skriv et positivt heltall: "))
            if tall < 0:
                print("Tallet må være positivt")
                continue
            break
        except ValueError:
            print("Du må skrive et tall")
            continue


try:
    validering()
except KeyboardInterrupt:
    print("\nHade!")
    exit(0)
