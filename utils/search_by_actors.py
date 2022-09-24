import sqlite3
import json


def search_by_actors(first_actor, second_actor):
    with sqlite3.connect('netflix.db') as connection:
        # first_actor = f"%{ first_actor }%"
        # second_actor = f"%{ second_actor }%"
        cursor = connection.cursor()
        sqlite_query = """
                        select title, cast
                        from netflix
                        limit 100
                    """
        cursor.execute(sqlite_query)
        # cursor.execute(sqlite_query, (first_actor, second_actor))
        executed_query = cursor.fetchall()
        # answer_list = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in executed_query]
        # res = json.dumps(answer_list)

    return executed_query
