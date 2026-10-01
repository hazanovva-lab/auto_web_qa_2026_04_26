from faker import Faker

faker = Faker()
# print(f'name: {faker.name()}')
# print(f'address: {faker.address()}')
# print(f'text: {faker.text()}')


faker_ru = Faker('ru_RU')

print(f'Russian name: {faker_ru.name()}')
print(f'Russian address: {faker_ru.address()}')
print(f'Russian text: {faker_ru.text()}')
print(f'Russian phon number: {faker_ru.phone_number()}')
print(f'Russian job: {faker_ru.job()}')
print(f'Russian snils: {faker_ru.snils()}')