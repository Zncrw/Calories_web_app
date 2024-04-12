# Counting calories webbapp
## About project:
<p> In this project i try to implement easy web form for counting how many calories you should get. I am using OOP
principes and i try to implement some cybersecurity principles to prevent attacks. Also using Flask framework and web scraping
by BeautifulSoup library.</p>
<br>
### Scraping temperature:
<p> In this project app scrape actual temperature in city from <italic>www.timeanddate.com/weather.</italic> Temperature is
important to get calculation on <bold>BMR</bold></p><br>
<p> BMR formula: (10*weight) + (6.25*height) - (5*age) + 5 -(10*temperature)</p>
<br>
### Security:
<p> I tried to prevent some known attack to websites using libraries like </p>
<br>
<p>Bleach: this library I used to sanitize users input to prevent some XSS attacks or Code Injections </p>
<br>
<p> Talisman: Talisman is a small Flask extension that handles setting HTTP headers that can help protect against a few common web application security issues.</p>
<br>
## Libraries:
<p> All used libraries and their versions you can find in requirements.txt file. </p>

## Showcase:
At start you will get to the homepage
![img.png](img.png)
After clicking on link you will be redirected on form, where app needs some your information to get results.
![img_1.png](img_1.png)

And finally after clicking to "Calculate" button you will get the result shown bellow
![img_2.png](img_2.png)