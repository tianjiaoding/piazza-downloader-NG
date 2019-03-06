import requests
import json
import os

def main():

    # Replace with your email and password here
    login_data = {
            "method": "user.login",
            "params": {"email": "dingtj@shanghaitech.edu.cn",
                       "pass": "GoodLuck"}
        }
    session = requests.Session()
    r = session.post(
            "https://piazza.com/logic/api",
            data=json.dumps(login_data),
        )

    # A simple proofchecker
    if r.json()["result"] not in ["OK"]:
        raise Exception("Login failed. Check your login details in the Python code.")

    resources_dir_name = 'resources'

    # Create resources directory to save all resources to
    if not os.path.exists(resources_dir_name):
        os.mkdir(resources_dir_name)

    # Read file with links
    urls_file = open('resources_links.txt')
    urls = urls_file.readlines()

    # Read file with resources names
    files_names_file = open('resources_names.txt')
    names = files_names_file.readlines()

    for index, link in enumerate(urls):
        # Strip removes newlines and whitespaces on sides.
        file_name = names[index].strip()
        file_name = os.path.join(resources_dir_name, file_name)

        # Remove the new line symbol at the end
        link = link[:-1]
        print("downloading {}".format(file_name))
        r = session.get(link)

        # Write to a file with specified name.
        # In case it exists, overwrite it.
        new_file = open(file_name, 'wb')
        new_file.write(r.content)
        new_file.close()

        print("file {} was successfully saved".format(file_name))

if __name__ == '__main__':
    main()
