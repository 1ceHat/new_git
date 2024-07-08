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
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    """
        Класс ЮрТуба, содержащий аттрибуты: текущего пользователя (User), список пользователей (User),
        список видео (Video)
    """
    def __init__(self, current_user=None, users = [], videos = []):
        self.current_user = current_user
        self.users = users
        self.videos = videos

    def log_in(self, nickname, password):
        correct_nickname = False
        correct_password = False
        for user in self.users:
            if nickname == user.nickname:
                correct_nickname = True
            if password == user.password:
                correct_password = True

            if correct_password and correct_nickname:
                self.current_user = user
                print(f"Приветствуем, {nickname}")
                break

            if correct_password or correct_password:
                if not correct_nickname:
                    print("Пользователь не найден!")
                elif not correct_password:
                    print("Неверный пароль!")
                break

    def register(self, nickname, password, age):
        nickname_exist = False
        for user in self.users:
            if nickname == user.nickname:
                nickname_exist = True
                break

        if not nickname_exist:
            self.current_user = User(nickname, password, age)
            self.users.append(self.current_user)

            print(f"Пользователь '{nickname}' успешно добавлен!")
        else:
            print(f"Пользователь '{nickname}' уже существует!")

    def log_out(self):
        self.current_user = None

    def add(self, *other):
        for video in other:
            if video.title not in self.videos:
                self.videos.append(video)
                print("Видео успешно добавлено!")
            else:
                print(f"Видео {video.title} уже существует!")

    def get_videos(self, word):
        word = word.lower()
        founded_videos = []
        for video in self.videos:
            if word in video.title.lower():
                founded_videos.append(video.title)

        return founded_videos

    def watch_video(self, film):
        video_exist = False
        video_index = None
        for i in range(len(self.videos)):
            if film == self.videos[i].title:
                video_index = i
                video_exist = True
                break

        if video_exist:
            if not self.current_user:
                print("Войдите в аккаунт, чтобы смотреть видео :)")
            elif self.videos[video_index].adult_mode and self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу :с")
            else:
                for i in range(self.videos[video_index].duration):
                    self.videos[video_index].time_now += 1
                    print(self.videos[video_index].time_now, end=' ')
                    #sleep(1)
                print("Видео закончено!")
                self.videos[video_index].time_now = 0
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

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')