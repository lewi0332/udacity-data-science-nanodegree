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