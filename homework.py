from threading import Thread
import time


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово №{i+1}\n')
            time.sleep(0.1)
    print(f'Запись в файл "{file_name}" завершена')


start = time.time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
end = time.time()
res_func = (end-start)


fi_thr = Thread(target=wite_words, args=(10, 'example5.txt'))
se_thr = Thread(target=wite_words, args=(30, 'example6.txt'))
th_thr = Thread(target=wite_words, args=(200, 'example7.txt'))
fo_thr = Thread(target=wite_words, args=(100, 'example8.txt'))

start = time.time()
fi_thr.start()
se_thr.start()
th_thr.start()
fo_thr.start()

fi_thr.join()
se_thr.join()
th_thr.join()
fo_thr.join()
end = time.time()
res_thr = (end-start)

print(f'Время затраченное одним потоком: {res_func} с\nВремя затраченное мультипотоком: {res_thr} с')

