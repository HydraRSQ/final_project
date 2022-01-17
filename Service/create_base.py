import sqlite3
import pymysql
from config import host, user, password, database




def create_tables():
    con = pymysql.connect(host=host, user=user, password = password)
    with con:
        with con.cursor() as cur:
            cur.execute(f'CREATE DATABASE IF NOT EXISTS {database}')
            con.commit()
    connection = pymysql.connect(host=host, user=user, password = password, database = database)
    with connection:
        with connection.cursor() as cur:
            # cur.execute('Create database base')
            cur.execute('CREATE TABLE IF NOT EXISTS `base`.`employees_table` ( `id` INT NOT NULL AUTO_INCREMENT , `name` TEXT NOT '
                        'NULL , `specialization` INT NOT NULL , `salary` INT NOT NULL , `bonus` INT NOT NULL , '
                        '`project` TEXT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB')

            cur.execute('CREATE TABLE IF NOT EXISTS `base`.`projects_table` ( `id` INT NOT NULL AUTO_INCREMENT , `name` TEXT NOT '
                        'NULL , `status` TEXT NOT NULL , `budget` INT NOT NULL , `deadline` DATE NOT NULL , '
                        '`employees` INT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;')
            connection.commit()

    return {'success': True}
