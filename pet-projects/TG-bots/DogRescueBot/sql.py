import sqlite3


# db connect
def sqlite_open_connection(db):
    conn = sqlite3.connect(db, check_same_thread=True)
    return conn


def sqlite_close_connection(conn):
    conn.commit()
    conn.close()


# db connect
def sqlite_execute(conn, command):
    cursor = conn.cursor()
    cursor.execute(command)
    last_row_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    return last_row_id


def sqlite_select(conn, command):
    cursor = conn.cursor()
    cursor.execute(command)
    rows = cursor.fetchall()
    cursor.close()
    return rows


def sqlite_insert_chat_status(chat_id, last_update):
    com_start = "INSERT OR IGNORE  INTO chat_status (chat_id, last_update) VALUES " \
                "( '{id}', '{lu}' )".format(id=chat_id, lu=last_update)
    print("Insert user {id} into db".format(id=chat_id))
    _ = sqlite_execute(com_start)


def sqlite_update_chat_status_full(chat_id, chat_status, user_in_process, last_update):
    com_start = \
        "UPDATE chat_status " \
        "set chat_status = '{cs}', last_update = '{lu}', user_in_process = {up} " \
        "where chat_id = {cid}".format(cid=chat_id, cs=chat_status, lu=last_update, up=user_in_process)
    print("updated {cid} to status {cs} for line {up}".format(cid=chat_id, cs=chat_status, up=user_in_process))
    sqlite_execute(com_start)


def sqlite_update_chat_status_only(chat_id, chat_status, last_update):
    com_start = \
        "UPDATE chat_status " \
        "set chat_status = '{cs}', last_update = '{lu}'" \
        "where chat_id = {cid}".format(cid=chat_id, cs=chat_status, lu=last_update)
    print("updated {cid} to status '{cs}'".format(cid=chat_id, cs=chat_status))
    sqlite_execute(com_start)


def sqlite_insert_new_bl_line():
    com_start = "INSERT INTO black_list (reason) VALUES ('')"
    new_bl_id = sqlite_execute(com_start)
    print("new bl line created")
    return new_bl_id


def sqlite_update_bl_line(line_id,
                          name="NULL",
                          surname="NULL",
                          phone="NULL",
                          vk="NULL",
                          other_contact="NULL",
                          reason="NULL"):
    com_start = \
        "UPDATE black_list " \
        "set name = '{1}', surname = '{2}', phone = '{3}', vk = '{4}', other_contact = '{5}', reason = '{6}' " \
        "where id = {0}".format(line_id, name, surname, phone, vk, other_contact, reason)
    new_bl_id = sqlite_execute(com_start)
    return new_bl_id


def sqlite_get_status(chat_id):
    com_status = "SELECT chat_status, user_in_process " \
                 "FROM chat_status " \
                 "WHERE chat_id = {lid} ".format(lid=chat_id)
    print(com_status)
    rows = sqlite_select(com_status)
    return rows[0]

