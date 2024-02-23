from django.shortcuts import render
import mysql.connector


def show_data(request):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password123#@!",
        database="jadidlar"
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM jadidlar.poems")
    data = cursor.fetchall()

    conn.close()

    return render(request, 'data_list.html', {'data': data})


def show_data_news(request):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password123#@!",
        database="jadidlar"
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM jadidlar.news")
    data = cursor.fetchall()

    # Fetch column names
    column_names = [i[0] for i in cursor.description]
    print(column_names)

    conn.close()

    return render(request, 'data_news.html', {'data': data})
