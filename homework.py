from time import sleep


class User:
    """
        Класс пользователей, содержащий аттрибуты: логин, пароль, возраст
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.age = age
        self.password = hash(password)

    def __str__(self):
        return self.nickname


class Video:
    """
        Класс видео, содержащий аттрибуты: название, продолжительность, текущее время, возрастное ограничение
    """
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    """
        Класс ЮрТуба, содержащий аттрибуты: текущего пользователя (User), список пользователей (User),
        список видео (Video)
    """
    def __init__(self, current_user=None, users=None, videos=None):
        self.current_user = current_user
        if users is None:
            self.users = []
        if videos is None:
            self.videos = []

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname:
                if hash(password) != user.password:
                    print('Неверный пароль!')
                    break
                else:
                    self.current_user = user
                    print(f"Приветствуем, {user.nickname} :)")
                    break
        else:
            print(f'Пользователя {nickname} не существует!')

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print(f"Пользователь '{nickname}' уже существует!")
                break
        else:
            self.current_user = User(nickname, password, age)
            self.users.append(self.current_user)
            print(f"Пользователь '{nickname}' успешно добавлен!")

    def log_out(self):
        self.current_user = None

    def add(self, *other):
        for video in other:
            for current_video in self.videos:
                if video.title.lower() == current_video.title.lower():
                    break
            else:
                self.videos.append(video)

    def get_videos(self, word):
        word = word.lower()
        founded_videos = []
        for video in self.videos:
            if word in video.title.lower():
                founded_videos.append(video.title)

        return founded_videos

    def watch_video(self, film):
        for i in range(len(self.videos)):
            if film.lower() == self.videos[i].title.lower():
                if self.current_user is None:
                    print("Войдите в аккаунт, чтобы смотреть видео :)")
                elif self.videos[i].adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу :с")
                else:
                    for j in range(self.videos[i].duration):
                        self.videos[i].time_now += 1
                        print(self.videos[i].time_now, end=' ')
                        sleep(1)
                    print("Видео закончено!")
                    self.videos[i].time_now = 0
                break
        else:
            print(f"Видео '{film}' не найдено!")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.log_in('vasya_pupkin', 'lolkekcheburek')
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')