class Score:
    def __init__(self, value:int):
        self.value = value

    def getModifier(self):
        return self.value // 2 - 5

    def getClassification(self):
        if self.value >= 60:
            return "godlike"
        elif self.value >= 54:
            return "superhuman"
        elif self.value >= 50:
            return "Best in the planet"
        elif self.value >= 40:
            return "Best in the continent"
        elif self.value >= 34:
            return "Best in the country"
        elif self.value >= 30:
            return "Best in the state"
        elif self.value >= 28:
            return "Famous among multiple cities"
        elif self.value >= 26:
            return "Famous in a city"
        elif self.value >= 24:
            return "Prodigy"
        elif self.value >= 22:
            return "Extremely talented"
        elif self.value >= 20:
            return "Very talented"
        elif self.value >= 18:
            return "Talented"
        elif self.value >= 16:
            return "Proficient"
        elif self.value >= 14:
            return "Above average"
        elif self.value >= 10:
            return "Average"
        elif self.value >= 8:
            return "Below average"
        elif self.value >= 6:
            return "Unskilled"
        elif self.value >= 4:
            return "Incompetent"
        elif self.value >= 2:
            return "Exgtremely incompetent"
        elif self.value >= 0:
            return "Disabled"

    def to_dict(self):
        return {
            "value": self.value,
            "modifier": self.getModifier(),
            "classification": self.getClassification()
        }











