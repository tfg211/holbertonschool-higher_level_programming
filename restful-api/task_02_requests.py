import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints the titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print("Status Code: {}".format(response.status_code))
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves specific fields to a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        structured_data = []
        
        # Structure the data into a list of dictionaries with specific keys
        for post in posts:
            structured_data.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })
            
        # Write the data into a CSV file called posts.csv
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(structured_data)
