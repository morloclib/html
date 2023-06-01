import html
import pandas as pd

def toHtml(x) -> str:
    if(isinstance(x, pd.DataFrame)):
        return x.to_html()
    elif(isinstance(x, str)):
        return html.escape(x)
    elif(isinstance(x, dict)):
        return "<ol>" + "".join(["<li>" + toHtml(key) + " : " + toHtml(val) + "</li>" for (key,val) in x.items()]) + "</ol>"
    elif(isinstance(x, (list, tuple, set))):
        return "<ol>" + "".join(["<li>" + toHtml(item) + "</li>" for item in x]) + "</ol>"
    else:
        return html.escape(str(x))

def tag(tag_str, x):
    return "<" + tag_str + ">" + x + "</" + tag_str + ">"


def writeHtml(filename, html):
    with open(filename, "w") as f:
        f.write(html)
