""" – Вот наши условия, – наконец нарушил молчание Сильвер. – Вы отдадите нам карту,
     чтобы мы могли заняться поисками клада. Тогда мы оставим вам половину припасов и первому же
      встреченному кораблю сообщим, что вы нуждаетесь в помощи.
– И это все? – осведомился капитан Смоллетт.
– Это мое последнее слово, будь я проклят! – ответил Джон. – Если вы откажетесь, 
то с вами будут говорить наши мушкеты.
– Превосходно, – сказал капитан. – А теперь выслушайте меня. Если вы явитесь сюда поодиночке и без оружия,
 то я всего лишь закую всех вас в кандалы и доставлю в Англию, где вас будут судить по закону.
Напишите программу, которая выберет условия, на которые можно согласиться.
Вашему решению будет доступен файл базы данных с таблицей Talks формата (показана БД для примеров):
id, condition, author, suitable, level_of_trust

PIC

Формат ввода
Вводится имя файла БД, затем два условия отбора, которые должны выполняться одновременно, и поле,
 по которому происходит сортировка выводимых значений.
Формат вывода
Вывести подходящие условия (condition), отсортированные по указанному полю. Каждое с новой строки.
    """

import sqlite3
import pprint



if __name__ == '__main__':
    name_db1 = 'discussion.db'  
    name_db2 = 'conversations.db'
    dbs = [name_db1, name_db2]
    
    condition = [("author = 'Silver'", "level_of_trust BETWEEN 6 AND 15", "id"),
                  ("suitable = 1", "level_of_trust > 10", "author")]
    i = 0
    for name_db in dbs:
        # name_db = input()
        condition1, condition2, sorting = condition[i]
        i+=1
        path_db = f"/Users/alexander/Documents/yandex/test_1/2020_E2L2_fOkUl/{name_db}"
        conn = sqlite3.connect(path_db)
        cur = conn.cursor()
        cur.execute('''SELECT name FROM sqlite_master WHERE type='table';''')
        name_table, = cur.fetchall()[0]
        sql = f"SELECT * FROM {name_table};"
        cur.execute(sql)
        list_element = cur.fetchall()

        sql = f"pragma table_info('{name_table}')"
        cur.execute(sql)
        list_columns = cur.fetchall()
        
        sql = f"SELECT condition FROM {name_table} WHERE {condition1} AND {condition2} ORDER BY {sorting} ASC;"
        cur.execute(sql)
        execute = cur.fetchall()
        for item in execute:
            item_, = item
            print(item_)
        


        