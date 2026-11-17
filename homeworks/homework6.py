from faker import Faker

# Эта библиотека нужна для генерации реалистичных фальшивых данных (имен, адресов, email, телефонов и т.д.),
# что очень удобно для тестирования программ, заполнения баз данных и создания макетов.
fake = Faker("ru_RU")
print("Сгенерированные тестовые данные:")
print(f"Имя: {fake.name()}")
print(f"Адрес: {fake.address()}")
print(f"Email: {fake.email()}")
print(f"Телефон: {fake.phone_number()}")
