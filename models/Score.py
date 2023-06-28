class Score:
    def __init__(self, value:int):
        self.value = value

    def getModifier(self):
        return self.value // 2 - 5

    def getClassification(self):
        if self.value >= 50:
            return "godlike"
        elif self.value >= 32:
            return "superhuman"
        elif self.value >= 30:
            return "Best in the planet"
        elif self.value >= 25:
            return "Best in the continent"
        elif self.value >= 22:
            return "Best in the country"
        elif self.value >= 19:
            return "Best in the state"
        elif self.value >= 17:
            return "Famous among multiple cities"
        elif self.value >= 15:
            return "Famous in a city"
        elif self.value >= 12:
            return "Prodigy"
        elif self.value >= 10:
            return "Extremely talented"
        elif self.value >= 7:
            return "Very talented"
        elif self.value >= 5:
            return "Talented"
        elif self.value >= 4:
            return "Proficient"
        elif self.value >= 2:
            return "Above average"
        elif self.value >= 0:
            return "Average"
        elif self.value >= -1:
            return "Below average"
        elif self.value >= -2:
            return "Unskilled"
        elif self.value >= -3:
            return "Incompetent"
        elif self.value >= -4:
            return "Exgtremely incompetent"
        elif self.value >= -5:
            return "Disabled"

    def to_dict(self):
        return {
            "value": self.value,
            "modifier": self.getModifier()
        }











