import praw
import re
user_agent = "Scrapper 1.0 by /u/python.engineer"
reddit = praw.Reddit(
    client_id = "9Gf7qp5gGGuFwija9oeL5A",
    client_secret = "XhNXA-JKnXNsPaZZdnIkuV_8bDec9Q",
    user_agent = user_agent
)

def get_comments(url):
    post = reddit.submission(url = url)
    my_comm_set = set()
    for comment in post.comments:
        my_comm_set.add(comment.body)
    pattern = r"&#\d+;?;"
    my_comm_list = []
    for comment in my_comm_set:
        comment = re.sub(pattern, "", comment)
        my_comm_list.append(comment)
    return my_comm_list
    

# if __name__ == "__main__":
#     url = "https://www.reddit.com/r/HazbinHotel/comments/1afjsbx/why_is_nifty_the_way_she_is/"
#     comment_list = get_comment(url)
#     print(comment_list)