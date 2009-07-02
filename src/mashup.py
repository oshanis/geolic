#!/usr/bin/python

import cgi
import cgitb
from lookup import *

cgitb.enable()

def main():
    print "Content-type: text/html"
    print
    print """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Geospatial Data License Mashup Demo</title>
<script>
function clear(){
   document.getElementById("result").innerHTML="";
}
</script>
</head>

<body>
<h1>Geospatial Data License Mashup Demo</h1>

<form id="simpledemo" name="simpledemo" method="post" action="mashup.py"><label></label> 
  <p>Mash up 2 Geospatial data sources. Consider you are mashing up Road and Restaurant Data respectively. </p>
  <p>Select the license for each of these different data sets:</p>
  
  <table><tr>
  <td>Roads</td>
  <td>
    <select name="license">
      <option value="PD">Public Domain</option>
      <option value="CC0">CC-Zero</option>
      <option value="BY">BY</option>
      <option value="BY-NC">BY-NC</option>
      <option value="BY-NC-ND">BY-NC-ND</option>
      <option value="BY-NC-ND-SA">BY-NC-ND-SA</option>
      <option value="BY-NC-SA">BY-NC-SA</option>
      <option value="BY-ND">BY-ND</option>
      <option value="BY-ND-SA">BY-ND-SA</option>
      <option value="BY-SA">BY-SA</option>
      <option value="ARR">All Rights Reserved</option>
      <option value="NL">No License Given!</option>
    </select>
  </td></tr>
  <tr><td>Restautants</td><td>
    <select name="license">
      <option value="PD">Public Domain</option>
      <option value="CC0">CC-Zero</option>
      <option value="BY">BY</option>
      <option value="BY-NC">BY-NC</option>
      <option value="BY-NC-ND">BY-NC-ND</option>
      <option value="BY-NC-ND-SA">BY-NC-ND-SA</option>
      <option value="BY-NC-SA">BY-NC-SA</option>
      <option value="BY-ND">BY-ND</option>
      <option value="BY-ND-SA">BY-ND-SA</option>
      <option value="BY-SA">BY-SA</option>
      <option value="ARR">All Rights Reserved</option>
      <option value="NL">No License Given!</option>
    </select>
  </td></tr></table>
  
  <p>
    <input type="submit" name="mashup2" value="Submit" />
  </p>
</form>"""

    print """<form id="complexdemo" name="complexdemo" method="post" action="mashup.py"><label></label> 
  <p>You can also mash up 3 sources of Geospatial data. For example, consider you are mashing up Roads, Restaurants and Forrest Geospatial Data. </p>
  <p>Select the license for each of these different data sets:</p>
  
  <table><tr>
  <td>Roads</td>
  <td>
    <select name="license">
      <option value="PD">Public Domain</option>
      <option value="CC0">CC-Zero</option>
      <option value="BY">BY</option>
      <option value="BY-NC">BY-NC</option>
      <option value="BY-NC-ND">BY-NC-ND</option>
      <option value="BY-NC-ND-SA">BY-NC-ND-SA</option>
      <option value="BY-NC-SA">BY-NC-SA</option>
      <option value="BY-ND">BY-ND</option>
      <option value="BY-ND-SA">BY-ND-SA</option>
      <option value="BY-SA">BY-SA</option>
      <option value="ARR">All Rights Reserved</option>
      <option value="NL">No License Given!</option>
    </select>
  </td></tr>
  <tr><td>Restautants</td><td>
    <select name="license">
      <option value="PD">Public Domain</option>
      <option value="CC0">CC-Zero</option>
      <option value="BY">BY</option>
      <option value="BY-NC">BY-NC</option>
      <option value="BY-NC-ND">BY-NC-ND</option>
      <option value="BY-NC-ND-SA">BY-NC-ND-SA</option>
      <option value="BY-NC-SA">BY-NC-SA</option>
      <option value="BY-ND">BY-ND</option>
      <option value="BY-ND-SA">BY-ND-SA</option>
      <option value="BY-SA">BY-SA</option>
      <option value="ARR">All Rights Reserved</option>
      <option value="NL">No License Given!</option>
    </select>
  </td></tr>
    <tr><td>Forrests</td><td>
    <select name="license">
      <option value="PD">Public Domain</option>
      <option value="CC0">CC-Zero</option>
      <option value="BY">BY</option>
      <option value="BY-NC">BY-NC</option>
      <option value="BY-NC-ND">BY-NC-ND</option>
      <option value="BY-NC-ND-SA">BY-NC-ND-SA</option>
      <option value="BY-NC-SA">BY-NC-SA</option>
      <option value="BY-ND">BY-ND</option>
      <option value="BY-ND-SA">BY-ND-SA</option>
      <option value="BY-SA">BY-SA</option>
      <option value="ARR">All Rights Reserved</option>
      <option value="NL">No License Given!</option>
    </select>
  </td></tr></table>
  
  <p>
    <input type="submit" name="Submit" value="Submit" />
  </p>

  <p>Likewise you can combine as many data sources you want, as long as the corresponding licenses allow it!</p>
</form>

"""
    process()

    print """</body></html>"""
            


def process():
   l = LookupTable(); 
   inputs = cgi.FieldStorage()
   licenses = inputs.getlist("license")
   if licenses:
      print "<div id='result'><hr><h3>License Result</h3>"
      print "The component licenses were: "
      for license in licenses:
         print license
         print ""
         
      resultant = l.query(licenses[0],licenses[1:len(licenses)])
      if resultant == "X":
         print "<br/><font color='red'>The data sources cannot be combined.</font>"
      else:
         print "<br/>The resultant license is: <font color='red'>"
         print resultant
      print """</font>
      <form method="post" action="mashup.py">
         <p><input type="submit" value="Clear"/></p>
      </form><hr/>
"""
        
if __name__ == "__main__":
  main()
  
