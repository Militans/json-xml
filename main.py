# 14) Напишите классы для предметной области животные. Возможные классы:
# млекопитающее и птица. В 4-м и 5-м пунктах хранение объектов одного класса
# реализовать в формате JSON, другого − в формате XML.
# {name: lion, legs: 4, eyes: 2, color_eyes: blue, sound: roar}

import json
import time
import os.path
import pprint
from xml.etree import ElementTree as ET


class Animal(object):

    def __init__(self, country, name, color):
        self.name = name
        self.country = country
        self.color = color
        self.status = None

    def set_name(self, name):
        self.name = name

    def set_living_country(self, country):
        self.country = country
        print(f"{self.name} is moving to {self.country}")
        time.sleep(1)
        print("Success!")

    def set_color(self, color):
        self.color = color

    def get_name(self):
        return self.name

    def get_living_country(self):
        return self.country

    def get_color(self):
        return self.color

    def move(self):
        print(str(self.name) + " is moving")

    def get_status(self):
        return self.status

    def to_json(self):
        return {
            "name": self.name,
            "country": self.country,
            "color": self.color,
            "status": self.status
        }

    @staticmethod
    def from_json(file):
        name = file["name"]
        country = file["country"]

        color = file["color"]

        return Predator(country, name, color)


class Predator(Animal):

    def move(self):
        assert self.name is not None, "Animal can not move without name"
        print(f"Predator is moving, his name is {self.name}")
        self.status = "moving"

    def hunt(self):
        print(f"{self.name} is hunting now, hi's hungry")
        self.status = "hunting"

    def sleep(self):
        print(f"{self.name} is sleeping")
        self.status = "sleeping"


class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying now")
        self.status = "fly"

    def get_egg(self):
        print("The egg has got")
        self.status = "chill"

    def soud(self): print("uwu")


def restart():
    n = input("Do you want anything else? yes/no\n")
    if n == "yes":
        main()
    elif n == "no":
        print("goodbye")
    else:
        print("only [yes] or [no]")


def creating_data():
    if os.path.exists("Lab_1.json"):
        print("The database is already exists")
    else:
        a = {"Predators": []}
        with open("Lab_1.json", "w") as file:
            json.dump(a, file)
        print("Success!")


# need redaction

def get_data():
    try:
        with open("Lab_1.json", 'r', encoding='utf-8') as inp:
            data = inp.read()
            json_data = json.loads(data)
        pprint.pprint(json_data)
    except FileNotFoundError as e:
        print("You haven't database")


def remove_element(name):
    try:
        with open("Lab_1.json", 'r', encoding='utf-8') as inp:
            js = json.load(inp)
        js["Predators"] = [pred for pred in js["Predators"] if pred['name'] != name]
        with open("Lab_1.json", 'w') as output:
            json.dump(js, output, indent=4)
    except FileNotFoundError as err:
        print("You have not the datafile")
    except KeyError as e:
        print("Incorrect name of the element")


def add_element(predator):
    try:
        with open("Lab_1.json", 'r', encoding='utf-8') as inp:
            js = json.load(inp)
        js["Predators"].append(predator.to_json())
        with open("Lab_1.json", 'w') as output:
            json.dump(js, output, indent=4)
    except FileNotFoundError as e:
        print(e)


def change_element(elem, param, new_param):
    try:
        with open("Lab_1.json", 'r', encoding='utf-8') as inp:
            js = json.load(inp)
        temp_animal = Animal.from_json(js["Predators"][elem])
        if param == "name":
            temp_animal.set_name(new_param)
            print("Success!")
            remove_element(elem)
            add_element(temp_animal)
        elif param == "country":
            temp_animal.set_living_country(new_param)
            print("Success!")
            remove_element(elem)
            add_element(temp_animal)
        elif param == "color":
            temp_animal.set_color(new_param)
            print("Success!")
            remove_element(elem)
            add_element(temp_animal)
            restart()
        else:
            print("Uncorrected param")
            return
    except KeyError:
        print("You haven't this object or uncorrected param")
        restart()
    except FileNotFoundError:
        print("You haven't the database")


def remove_database():
    try:
        os.remove("Lab_1.json")
        print("Success!")
    except FileNotFoundError as error:
        print("Nothing to delete")


def methods(predator, name_of_method):
    try:
        with open("Lab_1.json", 'r', encoding='utf-8') as inp:
            js = json.load(inp)
        temp_animal = Animal.from_json(js["Predators"][predator])
        if name_of_method == "move":
            temp_animal.move()
            remove_element(predator)
            add_element(temp_animal)
        elif name_of_method == "hunt":
            temp_animal.hunt()
            remove_element(predator)
            add_element(temp_animal)
        elif name_of_method == "sleep":
            temp_animal.sleep()
            remove_element(predator)
            add_element(temp_animal)
        else:
            print("Uncorrected command")
        restart()
    except KeyError:
        print("uncorrected name or function")
        restart()
    except FileNotFoundError:
        print("You have no database")
        restart()


def creating_data_xml():
    if os.path.exists("Lab_1a.xml"):
        print("You already have the database!")
    else:
        root = ET.Element("Birds")
        tree = ET.ElementTree(root)
        with open("Lab_1a.xml", 'wb') as out:
            tree.write(out)
        print("Success!")


def get_data_xml():
    try:
        root_node = ET.parse("Lab_1a.xml").getroot()
        print(str(root_node.tag) + ':')
        for child in root_node:
            print('\t' + str(child.tag) + ':')
            for child_2 in child:
                print('\t' + '\t' + str(child_2.tag) + ':', child_2.text)
    except FileNotFoundError:
        print("You have no datafile")


def add_element_xml(predator):
    try:
        root = ET.parse("Lab_1a.xml").getroot()
        name_pr = ET.SubElement(root, str(predator.name))
        name = ET.SubElement(name_pr, "name")
        name.text = predator.name
        country = ET.SubElement(name_pr, "country")
        country.text = predator.country
        color = ET.SubElement(name_pr, "color")
        color.text = predator.color
        status = ET.SubElement(name_pr, "status")
        status.text = predator.status
        tree = ET.ElementTree(root)
        with open("Lab_1a.xml", 'wb') as fn:
            tree.write(fn)
    except FileNotFoundError as e:
        print("You have no database for this type of animal")


def remove_element_xml(name):
    try:
        root = ET.parse("Lab_1a.xml").getroot()
        root.remove(root.find(name))
        tree = ET.ElementTree(root)
        with open("Lab_1a.xml", 'wb') as fn:
            tree.write(fn)
    except FileNotFoundError:
        print("You have not the datafile")
    except TypeError:
        print("Incorrect name of the element")


def change_element_xml(elem, param, new_param):
    try:
        root = ET.parse("Lab_1a.xml").getroot()
        temp_animal = Bird(root.find(elem).find("country").text,
                           root.find(elem).find("name").text,
                           root.find(elem).find("color").text)
        if param == "name":
            temp_animal.set_name(new_param)
            print("Success!")
            remove_element_xml(elem)
            add_element_xml(temp_animal)
        elif param == "country":
            temp_animal.set_living_country(new_param)
            remove_element_xml(elem)
            add_element_xml(temp_animal)
        elif param == "color":
            temp_animal.set_color(new_param)
            print("Success!")
            remove_element_xml(elem)
            add_element_xml(temp_animal)
        else:
            print("Uncorrected param")
            print("only [name], [country], [color]")

    except FileNotFoundError:
        print("Have no no database")
    except AttributeError:
        print("Uncorrected element")


def remove_database_xml():
    try:
        os.remove("Lab_1a.xml")
        print("Success!")
    except FileNotFoundError as error:
        print("Nothing to delete")


def methods_xml(predator, name_of_method):
    try:
        root = ET.parse("Lab_1a.xml").getroot()
        temp_animal = temp_animal = Bird(root.find(predator).find("country").text,
                                         root.find(predator).find("name").text,
                                         root.find(predator).find("color").text)
        if name_of_method == "fly":
            temp_animal.fly()
            remove_element_xml(predator)
            add_element_xml(temp_animal)
        elif name_of_method == "get_egg":
            temp_animal.get_egg()
            remove_element_xml(predator)
            add_element_xml(temp_animal)
        elif name_of_method == "sound":
            temp_animal.soud()
            remove_element_xml(predator)
            add_element_xml(temp_animal)
        else:
            print("Uncorrected command")
        restart()
    except AttributeError:
        print("Uncorrected name of bird")
        restart()
    except FileNotFoundError:
        print("You have no database")
        restart()


def main():
    print("Hello, you can interact with two objects:\n",
          "[1] - Birds\n",
          "[2] - Predators\n",
          "choose the point\n")
    try:
        k = int(input())
        print()
        assert (0 < k < 3), "Uncorrected number of command"
        if k == 1:
            print("What do you want to do?\n", "[1] - if u wanna add an element", '\n',
                  "[2] - if you wanna delete an element\n",
                  "[3] - if you wanna change the element\n",
                  "[4] - if you wanna display the database\n",
                  "[5] - if you wanna create the database\n",
                  "[6] - if you wanna delete the database\n",
                  "[7] - if you wanna do with some elem\n")
            try:
                n = int(input())
                print()
                assert (0 < n <= 7), "Uncorrected number of command"
                if n == 1:
                    print("Please, enter the parameters")
                    print("Parameters must be 3: country, name, color")
                    prd = [str(x) for x in input().split()]
                    add_element_xml(Bird(prd[0], prd[1], prd[2]))
                    restart()
                elif n == 2:
                    name = input("What element you wanna delete\n")
                    remove_element_xml(name)
                    restart()
                elif n == 3:
                    print("What element do you wanna change?")
                    elem = input()
                    print("What param do you wanna change?")
                    param = input()
                    print("Enter new param")
                    new_param = input()
                    change_element_xml(elem, param, new_param)
                    restart()
                elif n == 4:
                    get_data_xml()
                    restart()
                elif n == 5:
                    creating_data_xml()
                    restart()
                elif n == 6:
                    remove_database_xml()
                    restart()
                elif n == 7:
                    print("Please enter the name of bird and the method\n",
                          "you can choose three methods:\n",
                          "[fly], [get_egg] and [sound]")
                    inp = [str(d) for d in input().split()]
                    methods_xml(inp[0], inp[1])
                    restart()
            except ValueError as e:
                print(e)
                restart()
        elif k == 2:
            print("What do you want to do?\n", "[1] - if u wanna add an element", '\n',
                  "[2] - if you wanna delete an element\n",
                  "[3] - if you wanna change the element\n",
                  "[4] - if you wanna display the database\n",
                  "[5] - if you wanna create the database\n",
                  "[6] - if you wanna delete the database\n",
                  "[7] - if you wanna do with some elem\n")
            try:
                n = int(input())
                print()
                assert (0 < n <= 7), "Uncorrected number of command"
                if n == 1:
                    print("Please, enter the parameters")
                    print("Parameters must be 3: country, name, color")
                    prd = [str(x) for x in input().split()]
                    add_element(Predator(prd[0], prd[1], prd[2]))
                    restart()
                elif n == 2:
                    name = input("What element you wanna delete\n")
                    remove_element(name)
                    restart()
                elif n == 3:
                    print("What element do you wanna change?")
                    elem = input()
                    print("What param do you wanna change?")
                    param = input()
                    print("Enter new param")
                    new_param = input()
                    change_element(elem, param, new_param)
                    restart()
                elif n == 4:
                    get_data()
                    restart()
                elif n == 5:
                    creating_data()
                    restart()
                elif n == 6:
                    remove_database()
                    restart()
                elif n == 7:
                    print("Please enter the name of predator and the method\n",
                          "you can choose three methods:\n",
                          "[move], [hunt] and [sleep]")
                    inp = [str(d) for d in input().split()]
                    try:
                        methods(inp[0], inp[1])
                    except IndexError:
                        print("there is not enough method or name of predator")
            except ValueError as e:
                print(e)
                restart()
    except ValueError:
        print("Only integers")
        restart()


if __name__ == "__main__":
    main()
