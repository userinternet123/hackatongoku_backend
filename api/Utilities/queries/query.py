from sqlalchemy import text

def get_query(fecha_inicial, fecha_final):
    query = text(f"""
        SELECT 
            *
        FROM 
           dbo.TPrueba 
    """)
    return query
