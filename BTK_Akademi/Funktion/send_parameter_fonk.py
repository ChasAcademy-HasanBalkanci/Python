def selamlama(fn):
    def inner(ad):
        fn(ad)
    return inner
@selamlama
def gunaydin(ad):
    print(f"{ad}, günaydın")

@selamlama
def iyi_gunler(ad):
    print(f"{ad}, iyi günler")

gunaydin("Cinar")
iyi_gunler("Cinar")