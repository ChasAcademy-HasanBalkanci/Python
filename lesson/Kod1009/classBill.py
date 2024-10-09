class Bil:
    def __init__(self, model, färg):
        self.model = model
        self.färg = färg
    
    def __str__(self):
        return f"Model: {self.model}, Färg: {self.färg}"
        

    def information(self):
        return f"Bilmodell: {self.model}, Färg: {self.färg}"

min_bil = Bil("Golf", "Grön")

print(min_bil)