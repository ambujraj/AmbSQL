![ambsql](images/Screenshot.PNG)
<br>
# AmbSQL
* AmbSQL is a Relational Database Management System which created with keeping in focus the speed and the ease to operate on.
* Made With &#x2764; in Python3

Take a look at our [website](https://ambujraj.github.io/AmbSQL/homepage/)

# Documentation
> Please refer to the documentation at https://github.com/ambujraj/AmbSQL/wiki/Documentation

# Compatibility
> This program is compatible with python - 3.x

# Installation
## For Command-line Interface
* Download the AmbSQL.exe file from https://github.com/ambujraj/AmbSQL/releases and run it on Your PC.<br>
* AmbSQL can also be downloaded from https://ambujraj.github.io/AmbSQL/download/.

## For Python Package
You can use one of the below methods to download and use this repository.<br><br>
Using pip:<br>
`$ pip install ambsql`<br><br>
Manually using CLI:<br>
`$ git clone https://github.com/ambujraj/AmbSQL.git`<br>
`$ cd AmbSQL`<br>
`$ sudo python3 setup.py install (Linux and MacOS)`<br>
`$ python setup.py install (Windows)`<br><br>
Manually using UI:<br>
Go to the [repo on github](https://github.com/ambujraj/AmbSQL) => Click on 'Clone or Download' => Click on 'Download ZIP' and save it on your local disk.

# Usage
If installed CLI, open the AmbSQL.exe file and get the work started.<br><br>
If installed using pip or CLI:<br>
`$ python` (Windows)
<br>or<br>
`$ python3` (Linux or MacOS)<br>
`>>>from ambsql import *`<br><br>
If installed using UI, unzip the file downloaded, go to the 'AmbSQL' directory and use one of the below commands:<br>
`$ python3 AmbSQL.py` (Linux or MacOS)
<br>or<br>
`$ python AmbSQL.py` (Windows)

# Examples
If you installed <b>package</b> using pip or CLI, below is the sample code:<br>
`from ambsql import *`<br>
`createtable('studenttable', 'name', 'age')`<br>
`insertvalues('studenttable', 'Jack', 21)`<br>
`showvalues('studenttable')`<br><br>
If you installed <b>AmbSQL.exe</b>, below is the sample code:<br>
`> connect`<br>
`> createtable(studenttable, name, age)`<br>
`> insertvalues(studenttable, Jack, age)`<br>
`> showvalues(studenttable)`

 # Contributors
> Check the list of contributors [here](https://github.com/ambujraj/AmbSQL/blob/master/CREDITS)

# Help Us Improve
> You can suggest us of new improvements you want by creating new Issue [here](https://github.com/ambujraj/AmbSQL/issues)

## Important Notice

**AmbSQL** has been selected at [GirlScript Summer of Code 2021](https://www.gssoc.tech/)!!! 
<p align="center">
<img src="https://www.gssoc.tech/images/type-logo.png">
</p>

## 👨 Project Admin
- Ambuj Raj <p>[<img src="https://img.icons8.com/windows/32/000000/github-2.png" display = "inline-block">](https://github.com/ambujraj) [<img src="https://img.icons8.com/ios-glyphs/30/000000/linkedin-2.png"/>](https://www.linkedin.com/in/ambujraj/)</p>

## 👬  Mentors

Feel free to ask your queries!! 🙌

## Contributors 

<table>
	<tr>
		<td>
		<a href="https://github.com/ambujraj/AmbSQL/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ambujraj/AmbSQL" />
</a>
		</td>
	</tr>
</table>

## Slack Channel

- [#proj_ambsql](https://gssoc20.slack.com/messages/proj_ambsql)

# License
[MIT License](https://github.com/ambujraj/AmbSQL/blob/master/LICENSE)
