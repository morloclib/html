import html
import pandas as pd

def toHtml(x) -> str:
    if(isinstance(x, pd.DataFrame)):
        return x.to_html()
    elif(isinstance(x, str)):
        return html.escape(x)
    elif(isinstance(x, list)):
        return "<ol>" + "".join(["<li>" + toHtml(item) + "</li>" for item in x]) + "</ol>"
    elif(isinstance(x, set)):
        return "<ol>" + "".join(["<li>" + toHtml(item) + "</li>" for item in x]) + "</ol>"
    elif(isinstance(x, dict)):
        return "<ol>" + "".join(["<li>" + toHtml(key) + " : " + toHtml(val) + "</li>" for (key,val) in x.items()]) + "</ol>"
    else:
        return html.escape(str(x))

def writeHtml(html, filename):
    with open(filename, "w") as f:
        f.write(html)
