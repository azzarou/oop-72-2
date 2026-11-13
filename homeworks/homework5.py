# Задание 1
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

def is_admin(func):
    def wrapper(user):
        if user.role == "admin":
            return func(user)
        else:
            print("У вас нет доступа")
    return wrapper

@is_admin
def delete_video(user):
    print("Видео удалено")

admin = User("Ardager", "admin")
user = User("Bek", "user")

delete_video(admin)
delete_video(user)

# Задание 2
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Время выполнения: {round(end - start, 1)} секунд")
    return wrapper

@timer
def download_video():
    time.sleep(2)
    print("Видео загружено")

download_video()
