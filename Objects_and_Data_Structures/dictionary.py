# #key - value

# 41 => kocaeil 34 => istanbul

# sehirler = ['kocaeil', 'istanbul']
# plakalar = [41, 34]

# print(plakalar[sehirler.index('kocaeil')])

# print(plakalar['kocaeil']) => 41
# print(plakalar['istanbul']) => 34

# plakalar = {'kocaeil': 41, 'istanbul': 34}

# print(plakalar['istanbul'])

# plakalar['ankara'] = 6
# plakalar['kocaeil'] = 'new value'

# print(plakalar)

users = {
    'berkaydural': {
        'age': 18,
        'roles': ['admin', 'user'],
        'gender':'male',
        'job': 'developer',
        'email': 'mail@berkayhasip.com'
    },
    'duralberkay': {
        'age': 19,
        'roles': ['user'],
        'gender':'male',
        'job': 'developer',
        'email': 'mail@duralberkay.com'
    },
}

print(users['berkaydural']['roles'])

      