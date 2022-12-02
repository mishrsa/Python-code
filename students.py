class Students (object):
    def __init__(self, name, house):
        if not name:
            raise ValueError('Missing Name field')
        if house not in ["Pipraich", "Lehani", "Gorakhpur", "Langadi"]:
            raise ValueError ('Invalid house name')
        self.name = name
        self.house = house
    def __str__(self):
        return (f"{self.name} from {self.house}")


def main ():
    student = get_student()
    print (student)
def get_student():
    name = input("Name: ")
    house = input("house: ")
    return Students(name, house)
   










if __name__ == "__main__":
    main()

