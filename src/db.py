import sqlite3

from . import foo

DB_FILE = 'schedules.sqlite'

def open_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id integer PRIMARY KEY,
            name text NOT NULL UNIQUE,
            tz_offset integer NOT NULL DEFAULT 0,
            min_time integer NOT NULL DEFAULT 0,
            max_time integer NOT NULL DEFAULT 0
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS schedules (
            id integer PRIMARY KEY,
            name text NOT NULL UNIQUE
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS schedule_users (
            schedule_id integer NOT NULL,
            user_id integer NOT NULL,
            UNIQUE(schedule_id, user_id)
        )
    ''')
    conn.commit()
    return conn

def get_usersInSchedule(conn, scheduleName):
    c = conn.cursor()
    c.execute('''
        SELECT users.name FROM users
        INNER JOIN schedule_users ON schedule_users.user_id = users.id
        INNER JOIN schedules ON schedule_users.schedule_id = schedules.id
        WHERE schedules.name = ?
    ''', (scheduleName,))
    rows = c.fetchall()
    return [row[0] for row in rows]

def get_user(conn, name):
    c = conn.cursor()
    c.execute('SELECT id, name, tz_offset, min_time, max_time FROM users WHERE name = ?', (name,))
    row = c.fetchone()
    return foo.User({"nick": row[1], "timeZone": row[2], "minTime": row[3], "maxTime": row[4]}) if row else None

def get_users(conn):
    c = conn.cursor()
    c.execute('SELECT id, name, tz_offset, min_time, max_time FROM users')
    rows = c.fetchall()
    return [foo.User({"nick": row[1], "timeZone": row[2], "minTime": row[3], "maxTime": row[4]}) for row in rows]

def add_user(conn, user: foo.User):
    c = conn.cursor()
    c.execute('''
        INSERT INTO users (name, tz_offset, min_time, max_time)
        VALUES (?, ?, ?, ?)
    ''', (user.nick, user.timeZone, user.minTime, user.maxTime))
    conn.commit()

def add_userToShedule(conn, userName, scheduleName):
    c = conn.cursor()
    c.execute('''
        INSERT INTO schedule_users (schedule_id, user_id)
        VALUES (
            (SELECT id FROM schedules WHERE name = ?),
            (SELECT id FROM users WHERE name = ?)
        )
    ''', (scheduleName, userName))
    conn.commit()

def delete_userToSchedule(conn, userName, scheduleName):
    c = conn.cursor()
    c.execute('''
        DELETE FROM schedule_users
        WHERE schedule_id = (SELECT id FROM schedules WHERE name = ?)
        AND user_id = (SELECT id FROM users WHERE name = ?)
    ''', (scheduleName, userName))
    conn.commit()

def add_schedule(conn, name):
    c = conn.cursor()
    c.execute('''
        INSERT INTO schedules (name)
        VALUES (?)
    ''', (name,))
    conn.commit()

def delete_schedule(conn, name):
    c = conn.cursor()
    c.execute('DELETE FROM schedules WHERE name = ?', (name,))
    conn.commit()

def get_schedules(conn):
    c = conn.cursor()
    c.execute('SELECT id, name FROM schedules')
    rows = c.fetchall()
    return [{"id": row[0], "name": row[1]} for row in rows]

def set_user(conn, user: foo.User):
    c = conn.cursor()
    c.execute('''
        INSERT INTO users (name, tz_offset, min_time, max_time)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(name) DO UPDATE SET
            tz_offset = excluded.tz_offset,
            min_time = excluded.min_time,
            max_time = excluded.max_time
    ''', (user.nick, user.timeZone, user.minTime, user.maxTime))
    conn.commit()

def update_user_name(conn, old_name, new_name):
    c = conn.cursor()
    c.execute('UPDATE users SET name = ? WHERE name = ?', (new_name, old_name))
    conn.commit()

def update_user_tz(conn, name, tz_offset):
    c = conn.cursor()
    c.execute('UPDATE users SET tz_offset = ? WHERE name = ?', (tz_offset, name))
    conn.commit()

def update_user_min_time(conn, name, min_time):
    c = conn.cursor()
    c.execute('UPDATE users SET min_time = ? WHERE name = ?', (min_time, name))
    conn.commit()

def update_user_max_time(conn, name, max_time):
    c = conn.cursor()
    c.execute('UPDATE users SET max_time = ? WHERE name = ?', (max_time, name))
    conn.commit()

def delete_user(conn, name):
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE name = ?', (name,))
    conn.commit()

def close_db(conn):
    conn.close()

