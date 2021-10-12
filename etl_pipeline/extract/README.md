# Summary of the data types in this project
# Table of Contents
1. [CSV files](#CSV-files)
2. [JSON](#JSON)
3. [XML](#XML)
4. [SQL databases](#SQL-databases)
5. [Text Files](#Text-Files)
6. [Extracting Data from the Web](#Extracting-Data-from-the-Web)

## CSV files
CSV stands for comma-separated values. These types of files separate values with a comma, and each entry is on a 
separate line. Oftentimes, the first entry will contain variable names. Here is an example of what CSV data looks like. 
This is an abbreviated version of the first three lines in the World Bank projects data csv file.

    id,regionname,countryname,prodline,lendinginstr
    P162228,Other,World;World,RE,Investment Project Financing
    P163962,Africa,Democratic Republic of the Congo;Democratic Republic of the Congo,PE,Investment Project Financing

## JSON
JSON is a file format with key/value pairs. It looks like a Python dictionary. The exact same CSV file represented in 
JSON could look like this:

    [{"id":"P162228","regionname":"Other","countryname":"World;World","prodline":"RE","lendinginstr":"Investment Project Financing"},{"id":"P163962","regionname":"Africa","countryname":"Democratic Republic of the Congo;Democratic Republic of the Congo","prodline":"PE","lendinginstr":"Investment Project Financing"},{"id":"P167672","regionname":"South Asia","countryname":"People\'s Republic of Bangladesh;People\'s Republic of Bangladesh","prodline":"PE","lendinginstr":"Investment Project Financing"}]

Each line in the data is inside of a squiggly bracket {}. The variable names are the keys, and the variable values are 
the values.

There are other ways to organize JSON data, but the general rule is that JSON is organized into key/value pairs. 
For example, here is a different way to represent the same data using JSON:

    
    {"id":{"0":"P162228","1":"P163962","2":"P167672"},"regionname":{"0":"Other","1":"Africa","2":"South Asia"},"countryname":{"0":"World;World","1":"Democratic Republic of the Congo;Democratic Republic of the Congo","2":"People\'s Republic of Bangladesh;People\'s Republic of Bangladesh"},"prodline":{"0":"RE","1":"PE","2":"PE"},"lendinginstr":{"0":"Investment Project Financing","1":"Investment Project Financing","2":"Investment Project Financing"}} XML Another data format is called XML (Extensible Markup Language). XML is very similar to HTML at least in terms of formatting. The main difference between the two is that HTML has pre-defined tags that are standardized. In XML, tags can be tailored to the data set. Here is what this same data would look like as XML. <ENTRY> <ID>P162228</ID> <REGIONNAME>Other</REGIONNAME> <COUNTRYNAME>World;World</COUNTRYNAME> <PRODLINE>RE</PRODLINE> <LENDINGINSTR>Investment Project Financing</LENDINGINSTR> </ENTRY> <ENTRY> <ID>P163962</ID> <REGIONNAME>Africa</REGIONNAME> <COUNTRYNAME>Democratic Republic of the Congo;Democratic Republic of the Congo</COUNTRYNAME> <PRODLINE>PE</PRODLINE> <LENDINGINSTR>Investment Project Financing</LENDINGINSTR> </ENTRY> <ENTRY> <ID>P167672</ID> <REGIONNAME>South Asia</REGIONNAME> <COUNTRYNAME>People's Republic of Bangladesh;People's Republic of Bangladesh</COUNTRYNAME> <PRODLINE>PE</PRODLINE> <LENDINGINSTR>Investment Project Financing</LENDINGINSTR> </ENTRY> XML is falling out of favor especially because JSON tends to be easier to navigate; however, you still might come across XML data. The World Bank API, for example, can return either XML data or JSON data. From a data perspective, the process for handling HTML and XML data is essentially the same. SQL databases SQL databases store data in tables using primary and foreign keys. In a SQL database, the same data would look like this: id	regionname	countryname	prodline	lendinginstr P162228	Other	World;World	RE	Investment Project Financing P163962	Africa	Democratic Republic of the Congo;Democratic Republic of the Congo	PE	Investment Project Financing P167672	South Asia	People's Republic of Bangladesh;People's Republic of Bangladesh	PE	Investment Project Financing Text Files This course won't go into much detail about text data. There are other Udacity courses, namely on natural language processing, that go into the details of processing text for machine learning. Text data present their own issues. Whereas CSV, JSON, XML, and SQL data are organized with a clear structure, text is more ambiguous. For example, the World Bank project data country names are written like this Democratic Republic of the Congo;Democratic Republic of the Congo In the World Bank Indicator data sets, the Democratic Republic of the Congo is represented by the abbreviation "Congo, Dem. Rep." You'll have to clean these country names to join the data sets together. Extracting Data from the Web In this lesson, you'll see how to extract data from the web using an APIs (Application Programming Interface). APIs generally provide data in either JSON or XML format. Companies and organizations provide APIs so that programmers can access data in an official, safe way. APIs allow you to download, and sometimes even upload or modify, data from a web server without giving you direct access. QUIZ QUESTION Match the data with its format DATA FORMAT {'players' :5, 'date':'Jul 5 1999'} players, date 5, Jul 5 1999 <entry><players>5</players><date>July 5 1999</date></entry> ;

## XML
Another data format is called XML (Extensible Markup Language). XML is very similar to HTML at least in terms of 
formatting. The main difference between the two is that HTML has pre-defined tags that are standardized. In XML, tags 
an be tailored to the data set. Here is what this same data would look like as XML.

    <ENTRY>
      <ID>P162228</ID>
      <REGIONNAME>Other</REGIONNAME>
      <COUNTRYNAME>World;World</COUNTRYNAME>
      <PRODLINE>RE</PRODLINE>
      <LENDINGINSTR>Investment Project Financing</LENDINGINSTR>
    </ENTRY>
    <ENTRY>
      <ID>P163962</ID>
      <REGIONNAME>Africa</REGIONNAME>
      <COUNTRYNAME>Democratic Republic of the Congo;Democratic Republic of the Congo</COUNTRYNAME>
      <PRODLINE>PE</PRODLINE>
      <LENDINGINSTR>Investment Project Financing</LENDINGINSTR>
    </ENTRY>
    <ENTRY>
      <ID>P167672</ID>
      <REGIONNAME>South Asia</REGIONNAME>
      <COUNTRYNAME>People's Republic of Bangladesh;People's Republic of Bangladesh</COUNTRYNAME>
      <PRODLINE>PE</PRODLINE>
      <LENDINGINSTR>Investment Project Financing</LENDINGINSTR>
    </ENTRY>

XML is falling out of favor especially because JSON tends to be easier to navigate; however, you still might come across 
XML data. The World Bank API, for example, can return either XML data or JSON data. From a data perspective, the process 
for handling HTML and XML data is essentially the same.

## SQL databases
SQL databases store data in tables using primary and foreign keys. In a SQL database, the same data would look like this:

| id      | regionname | countryname | prodline | lendinginstr |
| ------- | ---------- | ----------- | ---------- | ----------- |
| P162228 | Other      | World;World | RE         | Investment Project Financing |
| P167672 | South Asia | Democratic Republic of the Congo;Democratic Republic of the Congo | PE | Investment Project Financing |
| P167672 | South Asia | People's Republic of Bangladesh;People's Republic of Bangladesh | RE | Investment Project Financing |

## Text Files
We won't go into muc h detail about text data. However, on others project on Natural Language Processing, we will go 
into more details of processing text for Machine Learning.

Text data present their own issues. Whereas CSV, JSON, XML, and SQL data are organized with a clear structure, text is 
more ambiguous. For example, the World Bank project data country names are written like this

    Democratic Republic of the Congo;Democratic Republic of the Congo

In the World Bank Indicator data sets, the [Democratic Republic of the Congo](https://data.worldbank.org/country/congo-dem-rep?view=chart) 
is represented by the abbreviation "Congo, Dem. Rep." We'll have to clean these country names to join the data sets 
together.

## Extracting Data from the Web
In this project, we'll extract data from the web using an APIs (Application Programming Interface). APIs generally 
provide data in either JSON or XML format.

Companies and organizations provide APIs so that programmers can access data in an official, safe way. APIs allow us 
to download, and sometimes even upload or modify, data from a web server without giving us direct access.