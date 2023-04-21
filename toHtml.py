import html
import pandas as pd

def toHtml(x) -> str:
    if(isinstance(x, pd.DataFrame)):
        return x.to_html()
    elif(isinstance(x, str)):
        return html.escape(x)
    elif(isinstance(x, list)):
        return "<ul>" + "\n".join(["<li>" + toHtml(item) + "</li>" for item in x]) + "</ul>"
    elif(isinstance(x, set)):
        return "<ul>" + "\n".join(["<li>" + toHtml(item) + "</li>" for item in x]) + "</ul>"
    elif(isinstance(x, dict)):
        return "<ul>" + "\n".join(["<li>" + toHtml(key) + " : " + toHtml(val) + "</li>" for (key,val) in x.items()]) + "</ul>"
    else:
        return html.escape(str(x))
