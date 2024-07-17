import os
import re
import requests

def download_episode(anime_link, episode_number):
    # Sending a GET request to the anime link
    response = requests.get(anime_link + episode_number)

    # Finding the download link in the response HTML
    download_link = re.search(r'"file":"([^"]+)"', response.text).group(1).replace('\\', '')

    # Downloading the episode using the download link
    episode_content = requests.get(download_link).content

    # Getting the desktop directory path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Saving the episode on the desktop
    file_path = os.path.join(desktop_path, f"episode_{episode_number}.mp4")
    with open(file_path, "wb") as f:
        f.write(episode_content)

    print(f"Episode {episode_number} downloaded successfully!\nSaved to: {file_path}")

# Asking the user for the link to the anime
anime_link = input("Enter the 9anime link to the anime: ")

# Asking the user for the episode number
episode_number = input("Enter the episode number: ")

# Downloading the episode
download_episode(anime_link, episode_number)
