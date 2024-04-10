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
     comments = get_comments("61557505631333_122105776010250187_EAAEdeXXODK0BO87GGvvuD40KKt32FMQUUm0rrBZBhf6zf8QXwHKgRpQxcnWyr1lk4cb0DWevE6VkgUDC5inPBZAjzJjUjFjJgsUDaV5rDPzyxLLZCS0B01H5bS5I0nOLok3NnbpuFp1ePRDhmgzZAv6sEsEtf1RCHC3kqy6knA4PZA17ZACqi0jHfD5JhVBasNC0D9eRpimZC8otcg6m8Du1RgZD")
     print(comments)