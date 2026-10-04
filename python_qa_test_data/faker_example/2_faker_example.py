from faker import Faker

locales = ['en-US', 'ru-RU', 'ja-JP']
weights = [1, 2, 3]

fake = Faker(locales)
print(fake.locales)
Faker.seed()