import requests


def get_author_info(user_id):
    author_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    author_response = requests.get(author_url)

    if author_response.status_code == 200:
        author_data = author_response.json()
        author_name = author_data['name']
    else:
        print(f"Unable to retrieve author data for ID {user_id}")
        return

    posts_url = 'https://jsonplaceholder.typicode.com/posts'
    posts_response = requests.get(posts_url)

    if posts_response.status_code == 200:
        posts_data = posts_response.json()
        author_posts = [post['title'] for post in posts_data if post['userId'] == user_id]
    else:
        print("Unable to retrieve posts data")
        return

    return author_name, author_posts


if __name__ == '__main__':
    user_id = int(input("Enter the ID of the author: "))

    author_info = get_author_info(user_id)

    if author_info:
        author_name, author_posts = author_info
        print(f"Author's Name: {author_name}")

        if author_posts:
            print("Author's Posts:")
            for post_title in author_posts:
                print(post_title)
        else:
            print("No posts found for this author.")
    else:
        print("Author not found.")
