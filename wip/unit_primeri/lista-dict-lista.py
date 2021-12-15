l = [
     {
      "ime": "alek 1",
      "prezime": "d 1",
      "god": 1,
      },
     {
      "ime": "alek 2",
      "prezime": "d 2",
      "god": 2,
      },
     {
      "ime": "alek 3",
      "prezime": "d 3",
      "god": 1977,
      },
     ]

d = []

for index, x in enumerate(l):
    
    d.append(x["god"])
print(type(d))
print("Minimum i maksimum godina je: ", min(d), " i ", max(d))
