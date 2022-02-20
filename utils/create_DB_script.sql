CREATE TABLE IF NOT EXISTS regions(
					 id INTEGER PRIMARY KEY AUTOINCREMENT,
					 region_name VARCHAR(40)
					 );
						
CREATE TABLE IF NOT EXISTS cities(
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					region_id INTEGER UNSIGNED NOT NULL,
					city_name VARCHAR(40) NOT NULL UNIQUE,

					FOREIGN KEY(region_id) REFERENCES regions(id)
					);
					  
CREATE TABLE IF NOT EXISTS users(
				   id INTEGER PRIMARY KEY AUTOINCREMENT,
				   second_name VARCHAR(30) NOT NULL,
				   first_name VARCHAR(30) NOT NULL,
				   patronymic VARCHAR(30),
				   region INTEGER UNSIGNED NOT NULL,
				   city INTEGER UNSIGNED NOT NULL,
				   phone VARCHAR(16) NOT NULL UNIQUE,
				   email VARCHAR(60) NOT NULL UNIQUE,

				   FOREIGN KEY(region) REFERENCES regions(id),
				   FOREIGN KEY(city) REFERENCES cities(id)
				   );

INSERT INTO regions(region_name) VALUES ('Краснодарский край'), 
										('Ростовская область'), 
										('Ставропольский край');
										
INSERT INTO cities(region_id, city_name) VALUES (1, 'Краснодар'),
												(1, 'Кропоткин'),
												(1, 'Славянск'),
												(2, 'Ростов'),
												(2, 'Шахты'),
												(2, 'Батайск'),
												(3, 'Ставрополь'),
												(3, 'Пятигорск'),
												(3, 'Кисловодск');
