with open("nyc_weather.csv", "r") as rf:
    arr = []
    for i in rf.readlines()[1::]:
        day, temp = i.split(",")
        arr.append(int(temp))

print(sum(arr[:7])/7)
print(max(arr[:10]))


weather_dict = {}

with open("nyc_weather.csv","r") as rf:
    for i in rf.readlines()[1::]:
        day, temp = i.split(",")
        temp = int(temp)
        weather_dict[day] = temp
    
print(weather_dict)

print(weather_dict["Jan 9"])
print(weather_dict["Jan 4"])


with open("poem.txt", "r") as rf:
    d = {}
    words =rf.read().split()
    for i in set(words):
        d[i] = words.count(i)

print(d)



