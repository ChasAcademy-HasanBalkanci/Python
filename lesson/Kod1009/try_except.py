def dela():
    try:
        tal1 = int(input("Ange ett tal: "))
        tal2 = int(input("Ange ett annat tal: "))
        resultat = tal1 / tal2
        print(f"Resultatet av {tal1} / {tal2} är {resultat}")
    except ZeroDivisionError:
        print("Något gick fel, du kan inte dela med noll.")
        dela()
    except Exception as error:
        print(f"Fel: {error}. Du måste ange korrekta tal.")
        dela()
dela()