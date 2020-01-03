import random
import time

names = ['Sunny', 'Bunny', 'Chinny', 'Vinny']
subjects = ['Python', 'Java', 'Blockchain']


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(subjects)
        }
        yield person


t1 = time.clock()
people = people_generator(10000000)
t2 = time.clock()
print('Took {}'.format(t2-t1))
