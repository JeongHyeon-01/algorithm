rock = [5, 3, 4, 1, 3, 8]
dog = [{
    "name" : "루비독",
    "age" : "95년생",
    "jump" : "3",
    "weight" : "4",
    },{
    "name" : "피치독",
    "age" : "95년생",
    "jump" : "3",
    "weight" : "3",
    },{
    "name" : "씨-독",
    "age" : "72년생",
    "jump" : "2",
    "weight" : "1",
    },{
    "name" : "코볼독",
    "age" : "59년생",
    "jump" : "1",
    "weight" : "1",
    },]

def cross(rock, dog):
    answer = [i['name'] for i in dog]
    for i in dog:
        idx = 0
        while idx < len(rock)-1:
            idx += int(i['jump'])
            rock[idx-1] -= int(i['weight'])
            if rock[idx-1] < 0:
                del answer[answer.index(i['name'])]
                break
    return answer


print(cross(rock.copy(), dog.copy()))

import json

json_dog = json.dumps(dog,ensure_ascii=False)
print(type(json_dog),json_dog)
json_dog = json.loads(json_dog)
print(type(json_dog),json_dog)
print(json_dog[0])
