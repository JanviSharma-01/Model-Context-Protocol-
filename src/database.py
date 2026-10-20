import pymysql
from config import DB_CONFIG

def get_db_connection():
    """Establishes connection to MySQL or falls back gracefully."""
    try:
        connection = pymysql.connect(
            host=DB_CONFIG.get("host", "localhost"),
            user=DB_CONFIG.get("user", "root"),
            password=DB_CONFIG.get("password", ""),
            database=DB_CONFIG.get("database", "test_db"),
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except Exception as e:
        print(f"[Database Connection Warning]: {e}")
        return None

def execute_query(sql_query: str):
    """Executes SQL query or returns mock data fallback."""
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql_query)
                result = cursor.fetchall()
                conn.commit()
                return result
        except Exception as err:
            return {"error": str(err)}
        finally:
            conn.close()
    
    # Fallback response for local offline execution
    return {
        "status": "mock_execution",
        "query": sql_query,
        "rows_affected": 1,
        "data": [{"id": 101, "name": "Janvi Sharma", "role": "SDE Intern"}]
    }
