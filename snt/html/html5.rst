HTML 5 is the actual HTML version.

An HTML 5 document must have the following structure::

  <!doctype html>
  <html lang="fr">
    <head>
      <meta charset="UTF-8" />
      <title>Document< /title>
      <link href="my.css" rel="stylesheet">
    </head>
    <body>
      ...
    <script src="my.js"></script>
    </body>
  </html>


To open a link in a new browser window::

  <a href="https://www.w3schools.com"
     target="_blank">Visit W3Schools.com !</a>

To use an image as a link::

  <a href="https://www.w3schools.com">
    <img border="0" alt="W3Schools" src="logo_w3s.gif" width="100" height="100">
  </a>

To add your own CSS use `<link href=` at the end of `<head>` section::

  ...
    <meta charset="UTF-8" />
    <title>Document< /title>
    <link href="my.css" rel="stylesheet">
  </head>

To add your own Javascript (JS) use `<script src=` at the end of `<body>` section::

  ...
    <script src="my.js"></script>
    </body>
  </html>

