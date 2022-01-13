from flask import Flask
import ghhops_server as hs
import deephops.base as lf


# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)


@app.route("/help")
def apphelp():
    return "Huge thanks to Andrew for this tool"


for i in lf.instances:
    kwargs_dict = dict(i._no_func_dict())
    print(kwargs_dict)
    hops.component(**kwargs_dict)(i._comp_func)



# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    app.run()

