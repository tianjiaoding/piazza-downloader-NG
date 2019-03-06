

# Piazza resources downloader

Provides a tool to download all resources linked in the Piazza resources panel.

## Requirements
* `Python`, works with either 2 or 3.

* `Requests`, which is a handy library to handle http operations. It can be installed via different ways.

  **Using pip:**
  ```shell
  pip install requests
  ```
  **Using anaconda:**
  ```shell
  conda install -c anaconda requests
  ```

## Getting started

1. Clone the repository.
```shell
git clone https://github.com/tianjiaoding/piazza-downloader-NG.git
```
1. Go to Piazza resources page where all the resources can be dowloaded.

1. In your broswer, excute the Javascript code `fetch_urls_and_names.js` that is in the repository.

  * For example, if you are using Chrome, press `F12` and go to the `Console` tab. If you are using Firefox, got to `Developer > Debugger` and then `Console`.
  * Copy and paste the aforementioned code, then press `Enter`.

1. You should see outputs in your console with links and with names. Put links in `resources_links.txt`, and put names in `resources_names.txt`. Replace the existing ones if you like.

1. Edit your login details in the Python code, and execute it.
```shell
cd piazza-downloader-NG
python get_resources_files.py
```

# Acknowledgement
This work is based on [`warmspringwinds`'s repository](https://github.com/warmspringwinds/piazza_resources_downloader). However, the original version is no longer being maintained and not functional in many cases, e.g., when login is required, or the link contains newline symbol. This work aims at fixing those problems and providing a working tool.
