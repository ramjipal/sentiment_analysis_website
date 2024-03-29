import requests
import json

def get_comments(creden):
     creden_list = creden.split("_")
     page_id = creden_list[0]
     post_id = creden_list[1]
     access_token = creden_list[2]
     print(page_id, post_id, access_token)

     url = f'https://graph.facebook.com/v16.0/{page_id}_{post_id}/comments?access_token={access_token}'
     response = requests.request("GET", url)
     data = json.loads(response.text)
     all_comments = []
     for comment in data['data']:
          all_comments.append(comment['message'])
     return all_comments


if __name__ == "__main__":
     comments = get_comments("61557505631333_122105776010250187_EAAEdeXXODK0BOzas1ZAegvfyi2jq8XBdViNApKi87ZB3VsLO6EFnjzE8EuZAUzZAY5433pUj756LavUJ8WG6iKnOj5yEa0WI3UI2HR9GnQx9I8RduKbYMZAAgFhBwp7ntBmFldsexC0RQrX88ZCuoZBZA3MQWVfdL2TyXad3viuV60ZCUspOIWGg2PX7yTgDZAkdsZD")
     print(comments)