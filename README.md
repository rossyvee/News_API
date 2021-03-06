**# News APP
- An application that helps people who want to watch news in realtime without having to bingewatch TV for the News.It uses the News Api
## Table of Content
+ [Description](#description)
+ [Installation Requirement]( Requisites)
+ [Technology Used](technology-used)
+ [Live links](#Live links)
+ [Reference](#reference)
+ [Licence](#licence)
+ [Authors Info](#aut)

## Description
The news Api will allow users to access the news without waiting for the news to air at a specified time
## Technology Used
* Flask
* Python3
* Heroku
* Bootstrap

## Requirements
* A stable internet connection
## User Story
* A user would see various news sources on the homepage of the application.
* A user would also be able to select a news source and see all news articles from the selected news source in the application.
* A user will be able to see the image, description and the time a news article was created from the News-Articles tab.
* A click on an article and read the full article on the source website.
## set up instruction and installation
 1. clone this repository to a folder https://github.com/rossyvee/News_API
 2. Extract the cloned file and install requirements
* cd News_Api_V2
* pip install -r requirements.txt
  3. Export configurations
  export API_KEY='{Enter your News Api Key}
  4.python3.10 -m venv virtual --without-pip
# Running the application locally

source virtual/bin/activate

pip install -r requirements.txt

gunicorn --bind 0.0.0.0:5000 app:app

- alternatively run (make sure the virtual environment is activated)

python run.py 

## Behaviour Drive and Development

| Behaviour     | Input              | Output
|---------------|--------------------| --------    |
| Display news sources | 'flask run         |  List of various news sources is displayed' |
| Display tabs with news by category  | Click the tab link | Clickable links to open news based on category  |
|Display articles from a news source|Click the news source|Redirected to a page with articles from the source|
|To Read an entire article|click a link to the article|Redirected to the news source's site to read the entire article|



[live-link](https://github.com/rossyvee/News_API)

# Debugging commands
```
python3.10 -m venv virtual --without-pip
```
# Running the application locally
```

source virtual/bin/activate

pip install -r requirements.txt
 flask run 

## Reference
  ### The reference materials used in this project can be accessed though this link
  * [Resource](https://moringaschool.instructure.com/courses/631/assignments/10035?module_item_id=57241)
  ## Licence
MIT License
Copyright (c) [2022] [Roseline Akinyi]
Permission is  granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
## Authors Info
Slack Profile - Rose Akinyi.

LinkedIn - (Roseline Akinyi: https://www.linkedin.com/in/roseline-akinyi-065875895/)

Email - roseakinyi001@gmail.com



