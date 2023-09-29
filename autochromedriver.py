from os import system
try:
    import requests
    import zipfile
    import io
    import os
    from selenium import webdriver
except ModuleNotFoundError:
    ls = ['requests', 'zipfile', 'io', 'selenium']
    for any0 in ls:
        cmd = 'pip install ' + any0
        system(cmd)


def update():

    # Set the URL for the latest version of ChromeDriver
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'

    # Send a GET request to the URL
    response = requests.get(url)

    # Get the latest version number from the response
    latest_version = response.text.strip()

    # Set the URL for the ChromeDriver download
    download_url = f'https://chromedriver.storage.googleapis.com/{latest_version}/chromedriver_win32.zip'

    # Send a GET request to the download URL
    response = requests.get(download_url)

    # Unzip the downloaded file
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
        zip_file.extractall()

    os.path.abspath('chromedriver.exe')
    # Get the path to the ChromeDriver executable
    # executable_path = os.path.abspath('chromedriver.exe')

    # # Initialize the WebDriver
    # driver = webdriver.Chrome(executable_path=executable_path)
    #
    # # Navigate to the website you want to copy the HTML from
    # driver.get("https://www.example.com")
    #
    # # Fetch the HTML of the page
    # html = driver.page_source
    #
    # # Close the WebDriver
    # driver.quit()
    #
    # # Print the HTML to the console
    # print(html)


if __name__ == "__main__":
    update()
