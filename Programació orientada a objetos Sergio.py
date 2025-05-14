class dog: 
    def __init__(self, size, color, race, price, name):
        self.size = size
        self.color = color
        self.race = race
        self.price = price
        self.name = name
    def walking(self):
        print(f"{self.name}is walking")

Rufo = dog("Small", "orange-brown", "Cocker spanish", "Free", "Rufo")
print(f"{Rufo.name}: {Rufo.size}, {Rufo.color}, {Rufo.race}, {Rufo.price}")

Bolt = dog("Small", "white", "Dog white German", "Free", "Bolt")
print(f"{Bolt.name}: {Bolt.size}, {Bolt.color}, {Bolt.race}, {Bolt.price}")

Snoopy = dog("Small", "white", "Beagle", "Free", "Snoopy")
print(f"{Snoopy.name}: {Snoopy.size}, {Snoopy.color}, {Snoopy.race}, {Snoopy.price}")

Chop = dog("Big", "black", "Rottweiler", "Free", "Chop")
print(f"{Chop.name}: {Chop.size}, {Chop.color}, {Chop.race}, {Chop.price}")

Fake_Rufo = dog("Small", "white", "Pug", "Free", "Fake_Rufo")
print(f"{Fake_Rufo.name}: {Fake_Rufo.size}, {Fake_Rufo.color}, {Fake_Rufo.race}, {Fake_Rufo.price}")

Zeus = dog("Big", "orange-brown", "Chop Chop", "Free", "Zeus")
print(f"{Zeus.name}: {Zeus.size}, {Zeus.color}, {Zeus.race}, {Zeus.price}")
Zeus.walking()





class friends_And_Me:
    def __init__(friends, size, color, haircolor, eyecolor, name):
        friends.size = size
        friends.color = color
        friends.haircolor = haircolor 
        friends.eyecolor = eyecolor
        friends.name = name

    def mood(friends):
        print(f"{friends.name} is in a mood")

Sergio = friends_And_Me("Tall", "passion cinnamon", "black", "brown", "Sergio")
print(f"{Sergio.name}: {Sergio.size}, {Sergio.color}, {Sergio.haircolor}, {Sergio.eyecolor}")

Andrea = friends_And_Me("small", "brown", "brown", "brown", "Andrea")
print(f"{Andrea.name}: {Andrea.size}, {Andrea.color}, {Andrea.haircolor}, {Andrea.eyecolor}")

Alvaro = friends_And_Me("medium", "white", "brown", "brown", "Alvaro")
print(f"{Alvaro.name}: {Alvaro.size}, {Alvaro.color}, {Alvaro.haircolor}, {Alvaro.eyecolor}")

Julian = friends_And_Me("medium", "white", "brown", "brown", "Julian")
print(f"{Julian.name}: {Julian.size}, {Julian.color}, {Julian.haircolor}, {Julian.eyecolor}")

Camilo = friends_And_Me("Tall", "white", "black", "brown", "Camilo")
print(f"{Camilo.name}: {Camilo.size}, {Camilo.color}, {Camilo.haircolor}, {Camilo.eyecolor}")


class tennis_brand:
    def __init__(brand, origin, color, average_price, style, name):
        brand.origin = origin
        brand.color = color
        brand.average_price = average_price
        brand.style = style
        brand.name = name

    def slogan(brand):
        print(f"{brand.name} says: 'Step into greatness!'")

Nike = tennis_brand("USA", "white", "$120", "Sport", "Nike")
print(f"{Nike.name}: {Nike.origin}, {Nike.color}, {Nike.average_price}, {Nike.style}")

Adidas = tennis_brand("Germany", "black", "$100", "Sport", "Adidas")
print(f"{Adidas.name}: {Adidas.origin}, {Adidas.color}, {Adidas.average_price}, {Adidas.style}")

Puma = tennis_brand("Germany", "red", "$90", "Sport", "Puma")
print(f"{Puma.name}: {Puma.origin}, {Puma.color}, {Puma.average_price}, {Puma.style}")

Converse = tennis_brand("USA", "white", "$70", "Casual", "Converse")
print(f"{Converse.name}: {Converse.origin}, {Converse.color}, {Converse.average_price}, {Converse.style}")

Vans = tennis_brand("USA", "black", "$65", "Casual", "Vans")
print(f"{Vans.name}: {Vans.origin}, {Vans.color}, {Vans.average_price}, {Vans.style}")

NewBalance = tennis_brand("USA", "grey", "$110", "Running", "New Balance")
print(f"{NewBalance.name}: {NewBalance.origin}, {NewBalance.color}, {NewBalance.average_price}, {NewBalance.style}")


        