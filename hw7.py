import sqlite3

def create_tables(conn):
    conn.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    ''')
    conn.commit()

def add_books(conn, name, author, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute('''
        INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, author, publication_year, genre, number_of_pages, number_of_copies))
    conn.commit()

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    
    create_tables(conn)

    add_books(conn, 'Дракула', 'Абрахам Брэм Стокер', 1897, 'готический роман ужасов', 318, 15)
    add_books(conn, 'Темная башня Стрелок', 'Стивен Кинг',1987, 'темный фэнтези', 250, 10 )
    add_books(conn, 'Кастлвания Проклятия тьмы', 'Джереми Блэк', 2008, 'графический роман игры',200, 1 )
    add_books(conn, 'Демоны Гоэтии', 'неизвестный сборник оккультистов', 1600 ,'оккультизм',480, 15 )
    add_books(conn, 'Ужас в музее', 'Лавкрафт Филипс Говард', 1932 ,'ужасы', 576, 3 )
    add_books(conn, 'Бесы', 'Федор Достоевский', 1872 ,'политизированный роман', 650 , 15 )
    add_books(conn, 'Палата номер шесть', 'Антон Чехов', 1892 ,'повесть', 320 , 10 )
    add_books(conn, 'Красная комната', 'Эдогава Рампо', 1991 ,'сборник детектив', 512 , 1 )
    add_books(conn, 'Убийство в улице', 'Эдгар Аллан По', 1841 ,'сборник детектив', 48, 2 )
    add_books(conn, 'Дикий гусь: Танцовщица', 'Мори Огай Тосон Симадзаки', 1990 ,'романтический повесть', 526 ,1 )
