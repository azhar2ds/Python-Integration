import random
import time

names = ['Sunny','Bunny','Chinny','Vinny']
subjects = ['Python','Java','Blockchain']

def people_list(num_people):
    results = []
    for i in range(num_people):
        person = {
            'id':i,
            'name': random.choice(names),
            'major':random.choice(subjects)
                }
        results.append(person)
    return results


t1 = time.clock()
people = people_list(10000000)
t2 = time.clock()
print('Took {}'.format(t2-t1))