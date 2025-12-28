from database import get_db_connection

def create_task(title, description, status):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO tasks (title, description, status)
        VALUES (%s, %s, %s) RETURNING id;
    """, (title, description, status))
    task_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return task_id

def get_tasks():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, description, status FROM tasks;")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def update_task(task_id, title, description, status):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE tasks SET title=%s, description=%s, status=%s WHERE id=%s;
    """, (title, description, status, task_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_task(task_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=%s;", (task_id,))
    conn.commit()
    cur.close()
    conn.close()
