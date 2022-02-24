CREATE TABLE IF NOT EXISTS regions(
					 id INTEGER PRIMARY KEY AUTOINCREMENT,
					 region_name VARCHAR(40)
					 );
						
CREATE TABLE IF NOT EXISTS cities(
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					region_id INTEGER UNSIGNED,
					city_name VARCHAR(40) NOT NULL UNIQUE,

					FOREIGN KEY(region_id) REFERENCES regions(id)
					);
					  
CREATE TABLE IF NOT EXISTS users(
				   id INTEGER PRIMARY KEY AUTOINCREMENT,
				   second_name VARCHAR(30) NOT NULL,
				   first_name VARCHAR(30) NOT NULL,
				   patronymic VARCHAR(30),
				   region INTEGER UNSIGNED,
				   city INTEGER UNSIGNED,
				   phone VARCHAR(16) UNIQUE,
				   email VARCHAR(60) UNIQUE,

				   FOREIGN KEY(region) REFERENCES regions(id),
				   FOREIGN KEY(city) REFERENCES cities(id)
				   );

INSERT INTO regions(region_name)
     VALUES ('Краснодарский край'),
            ('Ростовская область'),
            ('Ставропольский край');
										
INSERT INTO cities(region_id, city_name)
     VALUES (1, 'Краснодар'),
            (1, 'Кропоткин'),
            (1, 'Славянск'),
            (2, 'Ростов'),
            (2, 'Шахты'),
            (2, 'Батайск'),
            (3, 'Ставрополь'),
            (3, 'Пятигорск'),
            (3, 'Кисловодск');

INSERT INTO users(second_name, first_name, patronymic, region, city, phone, email)
	 VALUES ('Иванов', 'Виталий', 'Викторович', 1, 1, '+7 918 123 23 25', 'ivanov@mail.ru'),
	 		('Петров', 'Константин', 'Васильевич', 1, 2, '+7 961 435 78 88', 'petrov@gmail.com'),
	 		('Васечкин', 'Валерий', 'Александрович', 2, 4, '+7 928 488 23 45', 'vas@mail.ru'),
	 		('Подгорный', 'Анатолий', 'Николаевич', 3, 9, '+7 938 497 54 36', 'pek@yandex.ru'),
	 		('Нагорный', 'Сергей', 'Маркович', 1, 3, '+7 918 112 24 76', 'mek@mail.ru');
