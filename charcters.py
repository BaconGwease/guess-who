class Character:
    def __init__(self, name, hair_color, eye_color, glasses, hat, gender, facial_hair=False, skin_color=None, accessories=None):
        self.name = name
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.glasses = glasses
        self.hat = hat
        self.gender = gender
        self.facial_hair = facial_hair
        self.skin_color = skin_color
        self.accessories = accessories
        
    def __str__(self):
        return (f"Name: {self.name}, Hair Color: {self.hair_color}, Eye Color: {self.eye_color}, "
                f"Glasses: {self.glasses}, Hat: {self.hat}, Gender: {self.gender}, Facial Hair: {self.facial_hair}, "
                f"Skin Color: {self.skin_color}, Accessories: {self.accessories}")

Brian = Character()

