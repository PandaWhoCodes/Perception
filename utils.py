from db_utils import create_connection, run_query
import secrets
import random
from collections import Counter
from datetime import datetime


def insert_user(data):
    """
    insert new user
    :param data: user data from front-end
    """
    token = secrets.token_urlsafe(20)
    query = "INSERT into users(name,email,image_url,api_token) VALUES(%s,%s,%s,%s)"
    conn = create_connection()
    run_query(conn, query, [data["name"], data["email"], data["image"], token])
    conn.close()


def update_user_token(data):
    """
    update token for already registered users
    """
    token = secrets.token_urlsafe(20)
    query = "UPDATE users SET api_token='%s' where email='%s'" % (token, data["email"])
    conn = create_connection()
    run_query(conn, query, [])
    conn.close()


def update_user_image(data):
    """
    update the user image
    :param data: data recieved from the client side
    """
    query = "UPDATE users SET image_url='%s' where email='%s'" % (data["image"], data["email"])
    conn = create_connection()
    run_query(conn, query, [])
    conn.close()


def get_user_data(email):
    """
    Get user data
    :param email: email of the user
    :return: formatted response for login function
    """
    query = "SELECT * from users where email='{}'".format(email)
    # print(query)
    conn = create_connection()
    result = run_query(conn, query)[0]
    # print(result)
    conn.close()
    data = {"code": 1, "message": "logged In successfully",
            "data": {"user_id": result["user_id"], "name": result["name"], "email": result["email"],
                     "image": result["image_url"],
                     "api_token": result["api_token"]}}
    return data


def get_page_number(offset, limit, l):
    """
    :param offset:
    :param limit:
    :param l:
    :return: returns page number
    """
    if offset > l:
        return -1
    elif offset < limit:
        return 1
    else:
        if offset % limit == 0:
            return offset // limit
        else:
            return offset // limit + 1


def get_last_page(limit, l):
    if l % limit == 0:
        return l // limit
    else:
        return l // limit + 1


def get_page_till(offset, limit, l):
    if offset + limit > l:
        return l
    else:
        return offset + limit


def get_images(topic):
    sql = "select * from content where content_type='image' and topic='" + topic.lower() + "';"
    conn = create_connection()
    results = run_query(conn=conn, query=sql)
    return results


def get_datetime(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def get_email(user_id):
    sql = "select * from users where user_id=" + str(user_id)
    conn = create_connection()
    results = run_query(conn=conn, query=sql)
    try:
        return results[0]["email"]
    except Exception as e:
        print(e)
        return None


def get_topics_from(data, offset, limit):
    till = get_page_till(offset, limit, len(data))
    return data[offset:till]


def get_session_token(user_id):
    sql = "select * from users where user_id={}".format(user_id)
    conn = create_connection()
    results = run_query(conn=conn, query=sql)
    conn.close()
    return results[0]["api_token"]


def get_topics_data(data, offset, limit):
    data = list(data)
    l = len(data)
    to_send = {"code": 1, "message": "topics fetched successfully",
               "data": {"total": l, "current_page": get_page_number(offset, limit, l),
                        "last_page": get_last_page(limit, l), "per_page": limit, "from": offset,
                        "to": get_page_till(offset, limit, l), "topics": get_topics_from(data, offset, limit)}}
    return to_send


def calc_percent(word_freq):
    """
    Calculates and sends the word freq with percentage
    :param word_freq: counter object
    :return: dict with words and their percentage
    """
    total = 0
    freq_percent = {}
    for word, count in word_freq:
        total = total + count
    for word, count in word_freq:
        freq_percent[word] = int((count / total) * 100)
    return freq_percent


def get_word_percent(words):
    """
    Gets word list from the database and returns the frequency percentage of each word
    :param words: words_input from the user_content table
    :return: dict with words input frequency percentage
    """
    user_words = []
    stop_words = ("END_TIME", "START_TIME")
    for word in words:
        stipped_word = word["words"].replace(" ", "")
        if word["words"] not in stop_words and len(stipped_word) > 1:
            user_words.extend(word["words"].split(","))
    word_freq = Counter(user_words).items()
    return calc_percent(word_freq)
