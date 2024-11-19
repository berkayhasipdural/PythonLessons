website = "http://www.berkayhasip.com"
course = "Pyhton Kursu: Bastan Sona Python Programlama Rehberiniz (40 saat)"

lengthWebsite = len(website)
lengthCourse = len(course)

print(lengthWebsite)
print(website[7:10])
print(website[lengthWebsite-3:lengthWebsite])
print(course[:15], course[-15:])
print(course[::-1])

name, surname, age, job = 'Berkay', 'Dural', 18, 'Developer'
result = 'Benim adim {} {} , yasim {} ve meslegim {}.'.format(name, surname, age, job)
result = f'Benim adim {name} {surname} , yasim {age} ve meslegim {job}.'
print(result)

a3 = 'abc' * 3
print(a3)