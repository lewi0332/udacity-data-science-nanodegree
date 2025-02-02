# Why should a data scientist learn web development?

In this course, you are going to use Flask to build a data dashboard. You might be thinking that you already have good tools for visualizing data such as matplotlib, seaborn, or Tableau.

However, the web development skills you'll learn in this lesson will prepare you for building other types of data science applications. Data scientists are increasingly being asked to deploy their work as an application in the cloud.

For example, consider a project where you build a model that classifies disaster relief messages into categories. With your web development skills, you could turn that model into a web app where you would input a message and display the resulting message category.

As another example, consider a system that recommends movies based on a user's preferences. Part of the recommendation engine could include a web application that displays recommended products based on a userid. What you learn in this course will set you up for building the web app portion of the recommendation engine.

# How to Think about This Lesson

The lesson first gives an overview of the three base languages for web development: html, css, and JavaScript. You could take an entire course just on each of these languages. The goal is for you to get comfortable writing at least some code in each language so that you understand the web template files at the end of the lesson. This lesson goes through a lot of information to get you up to speed.

To work with the web template and make a data dashboard, you will only need to write Python code. If you want to customize the dashboard, you can do so with just a few changes to the html code. But the underlying technologies of data dashboard will be css, html, JavaScript, and Python.

## Lesson Outline
- Basics of a web app
    - html
    - css
    - javascript

- Front-end libraries
    - boostrap
    - plotly
- Back-end libraries
    - flask
- Deploy a web app to the cloud

## Lesson Files
All of the lesson's exercises are contained in classroom workspaces. You'll even deploy a web app from the classroom workspace; however, if you prefer to work locally, you can find the lesson files in this [data scientist nanodegree GitHub repo](https://github.com/udacity/DSND_Term2/tree/master/lessons/WebDevelopment).

# Introduction to HTML

## HTML Document Example

Here is an example of HTML code

```
<!DOCTYPE html>

<html>

<head>
    <title>Page Title</title>
</head>

<body>
    <h1>A Photo of a Beautiful Landscape</h1>
    <a href="https://www.w3schools.com/tags">HTML tags</a>
    <p>Here is the photo</p>
    <img src="photo.jpg" alt="Country Landscape">
</body>

</html>
```

## Explanation of the HTML document
As you progress through the lesson, you'll find that the `<head>` tag is mostly for housekeeping like specifying the page title and adding meta tags. Meta tags are in essence information about the page that web crawlers see but users do not. The head tag also contains links to javascript and css files, which you'll see later in the lesson.

The website content goes in the `<body>` tag. The body tag can contain headers, paragraphs, images, links, forms, lists, and a handful of other tags. Of particular note in this example are the link tag `<a>` and the image tag `<img>`.

Both of these tags link to external information outside of the html doc. In the html code above, the link `<a>` tag links to an external website called w3schools. The href is called an attribute, and in this case href specifies the link.

The image `<img>` tag displays an image called "photo.jpg". In this case, the jpg file and the html document are in the same directory, but the documents do not have to be. The src attribute specifies the path to the image file relative to the html document. The alt tag contains text that gets displaced in case the image cannot be found.

## Full List of Tags and How to Use Them

This is a link to one of the best references for html. Use this website to look up html tags and how to use them. [W3Schools HTML Tags](https://www.w3schools.com/tags/default.asp)

In fact, the [W3Schools website](https://www.w3schools.com/) has a lot of free information about web development syntax.

## Checking your HTML

It's a good idea to check the validity of your HTML. Here is a website that checks your HTML for syntax errors: [W3C Validator](https://validator.w3.org/#validate_by_input). Try pasting your HTML code here and running the validator. You can read through the error messages and fix your HTML.

# Div and Span

## Summary of Div and Span Elements
You can use div elements to split off large chunks of html into sections. Span elements, on the other hand, are for small chunks of html. You generally use span elements in the middle of a piece of text in order to apply a specific style to that text. You'll see how this works a bit later in the CSS portion of the lesson.

```
<div>
   <p>This is an example of when to use a div elements versus a span element. A span element goes around <span>a small chunk of html</span></p>
</div>
```

# IDs and Classes

## Example HTML
```
<div id="top">
    <p class="first_paragraph">First paragraph of the section</p>
    <p class="second_paragraph">Second paragraph of the section</p>
</div>

<div id="bottom">
    <p class="first_paragraph">First paragraph of the section</p>
    <p class="second_paragraph">Second paragraph of the section</p>
</div>
```

# CSS 

## CSS and this Lesson

To build the data dashboard at the end of this lesson, you won't need to actually write any CSS. Instead, you'll use libraries that take care of the CSS for you. In this that, that would be the [Bootstrap library](https://www.w3.org/Style/CSS20/history.html).

But if you are interested in understanding what Bootstrap is doing under the hood, then you need to understand how to style a website with CSS. This page has a summary of some important aspects of CSS programming.

## What is the Purpose of CSS?

In most professional websites, css is kept in a separate stylesheet. This makes it easier to separate content (html) from style (css). Code becomes easier to read and maintain.

If you're interested in the history of css and how it came about, here is an interesting link: [history of css](https://www.w3.org/Style/CSS20/history.html).

CSS stands for cascading style sheets. The "cascading" refers to how rules trickle down to the various layers of an html tree. For example, you might specify that all paragraphs have the same font type. But then you want to override one of the paragraphs to have a different font type. How does a browser decide which rules apply when there is a conflict? That's based on the cascade over. You can read more about that [here](https://www.lifewire.com/what-does-cascade-mean-3466872).

## Different ways to write CSS

As discussed in the video, there are essentially two ways to write CSS: **inline** or with a **stylesheet**.

Inline means that you specify the CSS directly inside of an html tag like so:

```
<p style="font-size:20px;">This is a paragraph</p>
```

Alternatively, you can put the CSS in a stylesheet. The stylesheet can go underneath an html head tag like so:

```
...
<head>
   <style>
       p {font-size: 20px;}
   </style>
</head>
```

Or the css can go into its own separate css file (extension .css). Then you can link to the css file within the html head tag like so:

```
<head>
    <link rel="stylesheet" type"text/css" href="style.css">
</head>
```

where `style.css` is the path to the style.css file. Inside the style.css file would be the style rules such as

```
p {
  color:red;
}
```

## CSS Rules and Syntax

CSS is essentially a set of rules that you can use to stylize html. The [W3 Schools CSS Website](https://www.w3schools.com/css/default.asp) is a good place to find all the different rules you can use. These including styling text, links, margins, padding, image, icons and background colors among other options.

The general syntax is that you:

1. select the html element, id, and/or class of interest
2. specify what you want to change about the element
3. specify a value, followed by a semi-colon

For example

```
a {
  text-decoration:none;
}
```

where a is the element of interest, text-decoration is what you want to change, and none is the value. You can write multiple rules within one set of brackets like:

```
a {
  text-decoration:none;
  color:blue;
  font-weight:bold;
}
```

You can also select elements by their class or id.

To select by class name, you use a dot like so:

```
.class_name {
   color: red;
}
```

To select by id name, you use the pound sign:

```
#id_name {
  color: red;
}
```

You can make more complex selections as well like "select paragraphs inside the div with id "div_top" . If your html looks like this,

```
<div id="div_top">
   <p>This is a paragraph</p>
</div>
```

then the CSS would be like this:

```
div#div_top p {
  color: red;
}
```

## Margins and Padding

The difference between margin and padding is a bit tricky. Margin rules specify a spatial buffer on the outside of an element. Padding specifies an internal spatial buffer.

These examples below show how this works. They use a div element with a border. Here is the div without any margin or padding:

```
<div style="border:solid red 1px;">
    Box
</div>
```

<div style="border:solid red 1px;">Box</div><br>

**Margin**


In this case, the div has a margin of 40 pixels. This creates a spatial buffer on the outside of the div element.

```
<div style="border:solid red 1px;margin:40px;">
    Box
</div>
```

<div style="border:solid red 1px;margin:40px;">
    Box
</div><br>


**Padding**

This next case has a padding of 40px. In the case of padding, the spatial buffer is internal.

```
<div style="border:solid red 1px;padding:40px;">
    Box
</div>
```

<div style="border:solid red 1px;padding:40px;">
    Box
</div><br>


**Margin and Padding**

In this case, the div element has both a margin of 40 pixels and a padding of 40 pixels.

```
<div style="border:solid red 1px;margin:40px;padding:40px;">
    Box
</div>
```

<div style="border:solid red 1px;margin:40px;padding:40px;">
    Box
</div><br>


## Specifying Size: Pixels versus Percent versus EM Units

In CSS there are various ways to define sizes, widths, and heights. The three main ones are pixels, percentages, and em units.

When you use px, you're defining the exact number of pixels an element should use in terms of size. So

```
<p style="font-size: 12px;">
```

means the font-size will be exactly 12 pixels.

The percent and em units have a similar function. They dynamically change sizing based on a browser's default values. For example

```
<p style="font-size: 100%"> 
```

means to use the default browser font size. 150% would be 1.5 times the default font size. 50% would be half. Similarly, 1em unit would be 1 x default_font. So 2em would be 2 x default font, etc. The advantage of using percents and em is that your web pages become dynamic. The document adapts to the default settings of whatever device someone is using be that a desktop, laptop or mobile phone.

As an aside, percentages and em units are actually calculating sizes relative to parent elements in the html tree. For example, if you specify a font size in a body tag , then the percentages will be relative to the body element:

```
<body style="font-size: 20px">
    <p style="font-size:80%">This is a paragraph</p>
...
</body>
```

<body style="font-size: 20px">
    <p style="font-size:80%">This is a paragraph</p>
...
</body><br>

Because different browsers might render html and CSS differently, there isn't necessarily a right or wrong way to specify sizes. This will depend on who will use your website and on what type of devices. You can read more here. You won't need to worry about all of this because in the web app, you're going to use a CSS framework that takes care of all of this for you.

# Javascript 

## JavaScript and this Lesson

To build the data dashboard at the end of this lesson, you won't need to write any JavaScript at all. That's because you'll use libraries (Bootstrap and Plotly) that take care of the JavaScript for you.

You won't need to get into the details of JavaScript syntax, but it's good to have at least an idea of what is happening under the hood.

What is JavaScript?
- JavaScript is a high level language like Python, PHP, Ruby, and C++. It was specifically developed to make the front-end of a web application more dynamic; however, you can also use javascript to program the back-end of a website with the JavaScript runtime environment node.
- Java and javaScript are two completely different languages that happen to have similar names.
- JavaScript syntax, especially for front-end web development, is a bit tricky. It's much easier to write front-end JavaScript code using a framework such as jQuery.

## Basic JavaScript Syntax
Here are a few rules to keep in mind when writing JavaScript:

- a line of code ends with a semi-colon ;
- () parenthesis are used when calling a function much like in Python
- {} curly braces surround large chunks of code or are used when initializing dictionaries
- [] square brackets are used for accessing values from arrays or dictionaries much like in Python

Here is an example of a JavaScript function that sums the elements of an array.

```
function addValues(x) {
  var sum_array = 0;
  for (var i=0; i < x.length; i++) {   
    sum_array += x[i];
  }
  return sum_array;
}

addValues([3,4,5,6]);
```

## What is jQuery?
Jquery is a JavaScript library that makes developing the front-end easier. JavaScript specifically helps with manipulating html elements. The reason we are showing you Jquery is because the Bootstrap library you'll be using depends on Jquery. But you won't need to write any Jquery yourself.

Here is a link to the documentation of the core functions in jquery: [jQuery API documentation](https://api.jquery.com/)

Jquery came out in 2006. There are newer JavaScript tools out there like [React](https://reactjs.org/) and [Angular](https://angularjs.org/).

As a data scientist, you probably won't need to use any of these tools. But if you work in a startup environment, you'll most likely hear front-end engineers talking about these tools.

## jQuery Syntax

The jQuery library simplifies JavaScript quite a bit. Compare the syntax. Compare these two examples from the video for changing the h1 title element when clicking on the image.

This is pure JavaScript code for changing the words in the h1 title element.

```
        function headFunction() {
            document.getElementsByTagName("h1")[0].innerHTML = 
                  "A Photo of a Breathtaking View";
        }
```

This code searches the html document for all h1 tags, grabs the first h1 tag in the array of h1 tags, and then changes the html. Note that the above code is only the function. You'd also have to add an onClick action in the image html tag like so:

```
<img src="image.jpg" onclick="headFunction()">
```

The jQuery code is more intuitive. Once the document has loaded, the following code adds an onclick event to the image. Once the image is clicked, the h1 tag's text is changed.

```
         $(document).ready(function(){
            $("img").click(function(){
                $("h1").text("A Photo of a Breathtaking View");
            });
        });
```

The dollar sign $ is jQuery syntax that says "grab this element, class or id". That part of the syntax should remind you somewhat of CSS. For example $("p#first") means find the paragraph with id="first". Or $("#first") would work as well.

Javascript has something called callback function, which can make learning javascript a bit tricky. Callback functions are essentially functions that can be inputs into other functions. In the above code, there is the ready() function that waits for the html document to load. Then there is another function being passed into the ready function. This section function adds an on-click event to an image tag. Then there's another function passed into the click() function, which changes the h1 text.

# Plotly

## Chart Libraries
There are many web chart libraries out there for all types of use cases. When choosing a library, you should consider checking whether or not the library is still being actively developed.

[d3.js](https://d3js.org/) is one of the most popular (and complex!) javascript data visualization libraries. This library is still actively being developed, which you can tell because the latest commit to the [d3 GitHub repository](https://github.com/d3/d3) is fairly recent.

Other options include [chart.js](https://classroom.udacity.com/nanodegrees/nd025/parts/0469f04b-1440-4b2c-9f69-8882d6ec436b/modules/237f5e87-7a8e-49d1-aab9-241006ce715e/lessons/3737ebcb-984e-4959-bf2a-95fe13de4916/concepts/ww.chartjs.org/), [Google Charts](https://developers.google.com/chart/), and [nvd3.js](http://nvd3.org/), which is built on top of d3.js

## Why Plotly
For this lesson, we've chosen plotly for a specific reason: [Plotly](https://plot.ly/), although a private company, provides open source libraries for both JavaScript and Python.

Because the web app you're developing will have a Python back-end, you can use the Python library to create your charts. Rather than having you learn more JavaScript syntax, you can use the Python syntax that you already know. However, you haven't built a back-end yet, so for now, you'll see the basics of how Plotly works using the JavaScript library. The syntax between the Python and Javascript versions is similar.

Later in the lesson, you'll switch to the Python version of the Plotly library so that you can prepare visualizations on the back-end of your web app. Yet you could write all the visualization code in JavaScript if you wanted to. Watch the screencast below to learn the basics of how Plotly works, and then continue on to the Plotly exercise.

Here are a few links to some helpful parts of the plotly documentation:

[javascript examples](https://plot.ly/javascript/)
[getting started](https://plot.ly/javascript/getting-started/)
[linking to the plotly library](https://plot.ly/javascript/getting-started/#plotlyjs-cdn)

# The Backend 

In this next part of the lesson, you'll build a backend using Flask. Because Flask is written in Python, you can use any Python library in your backend including pandas and scikit-learn.

In this part of the lesson, you'll practice

- setting up the backend
- linking the backend and the frontend together
- deploying the app to a server so that the app is available from a web address

## What is Flask?
[Flask](http://flask.pocoo.org/). A web framework takes care of all the routing needed to organize a web page so that you don't have to write the code yourself!

When you type "[http://www.udacity.com](http://www.udacity.com%22/)" into a browser, your computer sends out a request to another computer (ie the server) where the Udacity website is stored. Then the Udacity server sends you the files needed to render the website in your browser. The Udacity computer is called a server because it "serves" you the files that you requested.

The HTTP part of the web address stands for Hypter-text Transfer Protocol. HTTP defines a standard way of sending and receiving messages over the internet.

When you hit enter in your browser, your computer says "get me the files for the web page at [www.udacity.com](http://www.udacity.com%22/)": except that message is sent to the server with the syntax governed by HTTP. Then the server sends out the files via the protocol as well.

There needs to be some software on the server that can interpret these HTTP requests and send out the correct files. That's where a web framework like Flask comes into play. A framework abstracts the code for receiving requests as well as interpreting the requests and sending out the correct files.

Why Flask?
- First and foremost, you'll be working with Flask because it is written in Python. You won't need to learn a new programming language.
- Flask is also a relatively simple framework, so it's good for making a small web app.
- Because Flask is written in Python, you can use Flask with any other Python library including pandas, numpy and scikit-learn. In this lesson, you'll be deploying a data dashboard and pandas will help get the data ready.

## Getting started with Flask

## Using Flask in the Classroom Workspace
In the next part of the lesson, you'll see a classroom workspace. The classroom workspace already has Flask set up for you. So for now, all you need to do to run the Flask app is to open a Terminal and type.

```
python worldbank.py
```

That assumes you are in the default workspace directory within Terminal. That will get the server running.

## Seeing your App in the Workspace
Once the server is running, open a new terminal window and type

```
env | grep WORK
```

This command will return the Linux environmental variables that contain information about your classroom workspace. The `env` command will list all the environmental variables. The `|` symbol is a pipe for sending output from one command to another. The `grep` command searches text, so `grep WORK` will search for any text containing the word WORK.

The command should return two variables:

```
WORKSPACEDOMAIN=udacity-student-workspaces.com
WORKSPACEID=viewc7f3319f2
```

Your WORKSPACEID variable will be different but the WORKSPACEDOMAIN should be the same. Now, open a new web browser window, and type the following in the address bar:

```
http://WORKSPACEID-3001.WORKSPACEDOMAIN
```

In this example, that would be: https://viewc7f3319f2-3001.udacity-student-workspaces.com/

DON'T FORGET TO INCLUDE -3001. You should be able to see the web app. The number `-3001` represents the port for accessing your web app.

## Creating New Pages

To create a new web page, you first need to specify the route in the routes.py as well as the name of the html template.
```
@app.route('/new-route')
def render_the_route():
    return render_template('new_route.html')
```

The route name, function name, and template name do not have to match; however, it's good practice to make them similar so that the code is easier to follow.

The new_route.html file must go in the templates folder. Flask automatically looks for html files in the templates folder.

## What is @app.route?
To use Flask, you don't necessarily need to know what @app.route is doing. You only have to remember that the path you place inside of @app.route() will be the web address. And then the function you write below @app.route is used to render the correct html template file for the web address.

In Python, the @ symbol is used for decorators. Decorators are a shorthand way to input a function into another function. Take a look at this code. Python allows you to use a function as an input to another function:

```
def decorator(input_function):

    return input_function

def input_function():
    print("I am an input function")

decorator_example = decorator(input_function)
decorator_example()
```

Running this code will print the string:

*I am an input function*

Decorators provide a short-hand way of getting the same behavior:

```
def decorator(input_function):
    print("Decorator function")
    return input_function

@decorator
def input_function():
    print("I am an input function")

input_function()
```

This code will print out:

*Decorator function*
*I am an input function*

Instead of using a decorator function, you could get the same behavior with the following code:

```
input_function = decorator(input_function)
input_function()
```

Because `@app.route()` has the `.` symbol, there's an implication that app is a class (or an instance of a class) and route is a method of that class. Hence a function written underneath `@app.route()` is going to get passed into the route method. The purpose of `@app.route()` is to make sure the correct web address gets associated with the correct html template. This code

```
@app.route('/homepage')
def some_function()
  return render_template('index.html')
```

is ensuring that the web address '[www.website.com/homepage](http://www.website.com/homepage%60)` is associated with the index.html template.

If you'd like to know more details about decorators and how @app.route() works, check out these tutorials:

- [how @app.route works](https://ains.co/blog/things-which-arent-magic-flask-part-1.html)
- [general decorators tutorial](https://ains.co/blog/things-which-arent-magic-flask-part-1.html)

# Flask + Pandas

Code from the Screencast
Here is the code from the routes.py file before refactoring.

The data set comes from this link at the World Bank's data repository: link to dataset

``` 
from worldbankapp import app
from flask import render_template
import pandas as pd

df = pd.read_csv('data/API_SP.RUR.TOTL.ZS_DS2_en_csv_v2_9948275.csv', skiprows=4)

# Filter for 1990 and 2015, top 10 economies
df = df[['Country Name','1990', '2015']]
countrylist = ['United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'Brazil', 'Italy', 'Canada']
df = df[df['Country Name'].isin(countrylist)]

# melt year columns  and convert year to date time
df_melt = df.melt(id_vars='Country Name', value_vars = ['1990', '2015'])
df_melt.columns = ['country','year', 'variable']
df_melt['year'] = df_melt['year'].astype('datetime64[ns]').dt.year

# add column names
df_melt.columns = ['country', 'year', 'percentrural']

# prepare data into x, y lists for plotting
df_melt.sort_values('percentrural', ascending=False, inplace=True)

data = []
for country in countrylist:
    x_val = df_melt[df_melt['country'] == country].year.tolist()
    y_val =  df_melt[df_melt['country'] == country].percentrural.tolist()
    data.append((country, x_val, y_val))
    print(country, x_val, y_val)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/project-one')
def project_one():
    return render_template('project_one.html')
```

## Flask with Plotly and Pandas Part 1
In this next video, you'll see an example of how to pass data from the back end to the front end of the web app. In the next four parts of this lesson, you'll get a sense for how data and Plotly code can be taken from the back end and, sent to the front end, and then used to render plots on the front end. The goal of these next few videos is to show you how the web template works, which you'll be using later in the final exercise.

## Summary Part 1
The purpose of this section is to give you an idea of how the final web app works in terms of passing information back and forth between the back end and front end. The web template you'll be using at the end of the lesson will already provide the code for sharing information between the back and front ends. Your task will be to wrangle data and set up the plotly visualizations using Python. But it's important to get a sense for how the web app works.

In the video above, the data set was sent from the back end to the front end. This was accomplished by including a variable in the render_template() function like so:

```
data = data_wrangling()

@app.route('/')
@app.route('/index')
def index():
   return render_template('index.html', data_set = data)
```

What this code does is to first load the data using the data_wrangling function from wrangling.py. This data gets stored in a variable called data.

In render_template, that data is sent to the front end via a variable called data_set. Now the data is available to the front_end in the data_set variable.

In the index.html file, you can access the data_set variable using the following syntax:

```
{{ data_set }}
```

You can do this because Flask comes with a template engine called Jinja. Jinja also allows you to put control flow statements in your html using the following syntax:

```
{% for tuple in data_set %}
  <p>{{tuple}}</p>
{% end_for %}
```

The logic is:

1. Wrangle data in a file (aka Python module). In this case, the file is called wrangling.py. The wrangling.py has a function that returns the clean data.
2. Execute this function in routes.py to get the data in routes.py
3. Pass the data to the front-end (index.html file) using the render_template method.
4. Inside of index.html, you can access the data variable with the squiggly bracket syntax {{ }}

## Next
In the next part, you'll see how to create a Plotly visualization on the back end and then send the visualization code to the front end for rendering.

## Flask with Plotly and Pandas Part 2
In this section, you'll see how to create a Plotly visualization on the back end and then send the information to the front end for rendering.

## Summary Part 2
In the second part, a Plotly visualization was set up on the back-end inside the routes.py file using Plotly's Python library. The Python plotly code is a dictionary of dictionaries. The Python dictionary is then converted to a JSON format and sent to the front-end via the render_templates method.

Simultaneously a list of ids are created for the plots. This information is also sent to the front-end using the render_template() method.

On the front-end, the ids and visualization code (JSON code) is then used with the Plotly javascript library to render the plots.

In summary:

1. Python is used to set up a Plotly visualization
2. An id is created associated with each visualization
3. The Python Plotly code is converted to JSON
4. The ids and JSON are sent to the front end (index.html).
5. The front end then uses the ids, JSON, and JavaScript Plotly library to render the plots.

## JavaScript or Python
You could actually do all of this with only JavaScript. You would read the data, wrangle the data, and then create the plots all using JavaScript; however, to do all of this in JavaScript, you'd need to learn more about JavaScript programming. Instead, you can use the pandas and Python skills you already have to wrangle data on the back-end.

Flask with Plotly and Pandas Part 3
Here, the screencast video shows how to make more complex visualizations in Plotly. This example shows a line chart containing a unique line for each country in the data set.


## Summary Part 3
In part 3, the code iterated through the data set to create a visualization with multiple lines: one for each country.

The original code for a line chart with a single line was:

```
graph_one = [go.Scatter(
  x = data[0][1],
  y = data[0][2],
  mode = 'lines',
  name = country
)]
```

To make a visualization with multiple lines, graph_one will be a list of line charts. This was accomplished with the following code:

```
graph_one = []
for data_tuple in data:
   graph_one.append(go.Scatter(
   x = data_tuple[1],
   y = data_tuple[2],
   mode = 'lines',
   name = data_tuple[0]
))
```

## Next
In the last section of flask, plotly, and pandas, you'll see how to add more visualizations to the data dashboard. Then, you'll see some example code and finally you will practice using flask, plotly, and pandas together.

## Flask with Plotly and Pandas Part 4
In this next section, you'll see how to add more visualizations in the back end code and then render those visualizations on the front end.


## Summary Part 4
In the last part, three more visualizations were added to the wrangling Python module. The wrangling included reading in the data, cleaning the data, and preparing the Plotly code. Each visualization's code was appended to a list called `figures`. These visualizations were then imported into the routes.py file. This figures list was sent from the back end to the front end via the render_template method. A list of ids were also sent from the back end to the front end.

Then on the front end (index.html), a div was created for each visualization's id. And with help from the JavaScript Plotly library, each visualization was rendered inside appropriate div.

## Beyond a CSV file
Besides storing data in a local csv file (or text, json, etc.), you could also store the data in a database such as a SQL database.

The database could be local to your website meaning that the database file is stored on the same server as your website; alternatively, the database could be stored somewhere else like on a separate database server or with a cloud service like Amazon AWS.

Using a database with your web app goes beyond the scope of this introduction to web development, here are a few resources for using databases with Flask apps:

1. [Tutorial - Using Databases with Flask](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
2. [SQL Alchemy- a Python toolkit for working with SQL](http://docs.sqlalchemy.org/en/latest/)
3. [Flask SQLAlchemy - a Flask library for using SQLAlchemy with Flask](http://flask-sqlalchemy.pocoo.org/2.3/)

## Next Steps
In the next part of the lesson, you can look at the code and try running the web app from the classroom. Then in the next exercise, you'll practice adding another visualization to the web app.

# Deployment

## Other Services Besides Heroku
Heroku is just one option of many for deploying a web app, and Heroku is actually owned by Salesforce.com.

The big internet companies offer similar services like [Amazon's Lightsail](https://aws.amazon.com/lightsail/), [Microsoft's Azure](https://azure.microsoft.com/en-us/resources/samples/python-docs-hello-world/), [Google Cloud](https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env), and [IBM Cloud](https://www.ibm.com/blogs/bluemix/2015/03/simple-hello-world-python-app-using-flask/) (formerly IBM Bluemix). However, these services tend to require more configuration. Most of these also come with either a free tier or a limited free tier that expires after a certain amount of time.

## Instructions Deploying from the Classroom
Here is the code used in the screencast to get the web app running:

First, a new folder was created for the web app and all of the web app folders and files were moved into the folder:

```
mkdir web_app
mv -t web_app data worldbankapp wrangling_scripts worldbank.py
```

The next step was to create a virtual environment and then activate the environment:

```
conda update python
python3 -m venv worldbankvenv
source worldbankenv/bin/activate
```

Then, pip install the Python libraries needed for the web app

```
pip install flask pandas plotly gunicorn
```

The next step was to install the heroku command line tools:

```
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
https://devcenter.heroku.com/articles/heroku-cli#standalone-installation
heroku —-version
```

And then log into heroku with the following command

```
heroku login
```

Heroku asks for your account email address and password, which you type into the terminal and press enter.

The next steps involved some housekeeping:


- remove `app.run()` from worldbank.py
- type `cd web_app` into the Terminal so that you are inside the folder with your web app code.

Then create a proc file, which tells Heroku what to do when starting your web app:

```
touch Procfile
```

Then open the Procfile and type:

```
web gunicorn worldbank:app
```

Next, create a requirements file, which lists all of the Python library that your app depends on:

```
pip freeze > requirements.txt
```

And initialize a git repository and make a commit:

```
git init
git add .
git commit -m ‘first commit’
```

Now, create a heroku app:

```
heroku create my-app-name
```

where `my-app-name` is a unique name that nobody else on Heroku has already used.

The `heroku create` command should create a git repository on Heroku and a web address for accessing your web app. You can check that a remote repository was added to your git repository with the following terminal command:

```
git remote -v
```

Next, you need to push your git repository to the remote heroku repository with this command:

```
git push heroku master
```

Now, you can type your web app's address in the browser to see the results.

## Virtual Environments vs. Anaconda
Virtual environments and Anaconda serve a very similar purpose. Anaconda is a distribution of Python (and the analytics language R) specifically for data science. Anaconda comes installed with a package and environment manager called conda. You can create [separate environments using conda](https://conda.io/docs/user-guide/tasks/manage-environments.html). However, these environments automatically come with Python packages meant for data science.

Virtual environments, on the other hand, come with the Python language but do not pre-install other packages.

The classroom workspace has many other Python libraries pre-installed including an installation of [Anaconda](https://www.anaconda.com/distribution/).

When installing a web app to a server, you should only include the packages that are necessary for running your web app. Otherwise you'd be installing Python packages that you don't need.

To ensure that your app only installs necessary packages, you should create a **virtual Python environment**. A virtual Python environment is a separate Python installation on your computer that you can easily remove and won't interfere with your main Python installation.

There is more than one Python package that can set up virtual environments. In the past, you had to install these packages yourself. With Python 3.6, there is a virtual environment package that comes with the Python installation. The packaged is called venv

However, there is a bug with anaconda's 3.6 Python installation on a Linux system. So in order to use venv in the workspace classroom, you first need to update the Python installation as shown in the instructions above.

## Creating a Virtual Environment in the Classroom
Open a terminal window in a workspace and type:

```
conda update python
```

When asked for confirmation, type y and hit enter. Your Python installation should update.

Next, make sure you are in the folder where you want to build your web app. In the classroom, the workspace folder is fine. But on your personal computer, you'll want to make a new folder. For example:

```
mkdir myapp
```

will create a new folder called myapp and `cd myapp` will change your current directory so that you are inside the myapp folder.

Then to create a virtual environment type:

```
python3 -m venv name
```

where name can be anything you want. You'll see a new folder appear in the workspace with your environment name.

Finally, to activate the virtual environment. Type:

```
source name/bin/activate
```

You can tell that your environment is activated because the name will show up in parenthesis on the left side of the terminal.

## Creating a Virtual Environment Locally on Your Computer
You can develop your app using the classroom workspace. If you decide to develop your app locally on your computer, you should set up a virtual environment there as well. Different versions of Python have different ways of setting up virtual environments. Assuming you are using Python 3.6 and are on a linux or macOS system, then you should be able to set up a virtual environment on your local machine just by typing:

```
python3 -m venv name
```

and then to activate:

```
source name/bin/activate
```

On Windows, the command is;

```
c:\>c:\Python35\python -m venv c:\path\to\myenv
```

and to activate:

```
C:\> <venv>\Scripts\activate.bat
```

For more information, read through this [link](https://docs.python.org/3/tutorial/venv.html).

## Databases for Your App
The web app in this lesson does not need a database. All of the data is stored in CSV files; however, it is possible to include a database as part of a Flask app. One common use case would be to store user login information such as username and password.

Flask is database agnostic meaning Flask can work with a number of different database types. If you are interested in learning about how to include a database as part of a Flask app, here are some resources:

[Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
[Heroku - Provision a Database](https://devcenter.heroku.com/articles/getting-started-with-python#provision-a-database)

## Deployment
In the next part of the lesson, you'll find a workspace where you can practice deploying the world bank web app. Set up an account on [Heroku](https://classroom.udacity.com/nanodegrees/nd025/parts/0469f04b-1440-4b2c-9f69-8882d6ec436b/modules/237f5e87-7a8e-49d1-aab9-241006ce715e/lessons/3737ebcb-984e-4959-bf2a-95fe13de4916/concepts/www.heroku.com) and then follow the instructions shown in this part of the lesson.

You'll need to use a different name for the web app since the one used in this lesson is already taken.