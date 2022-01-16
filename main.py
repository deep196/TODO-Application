from flask import Flask, request, render_template
import dd

app = Flask(__name__)


@app.route("/data")
def data():
    return render_template("data.html")


@app.route("/task_data", methods=["POST"])
def get_task_data():
    task_name = request.form["task_name"]
    task_description = request.form["task_description"]
    task_deadline = request.form["task_deadline"]
    
    if dd.insert_task(task_name,task_description,task_deadline):
        return "Success"
    else:
        return "Exception- contact developer"
    

@app.route("/show_task")
def show_task():
    
    tasks = dd.get_tasks()
    
    if tasks == False:
        return "Exception- contact developer"
    else:
        return render_template("new_info.html",data=tasks)
        
        
@app.route("/update_task/<id>")
def update_task(id):
    
    task = dd.get_task(id) 
    
    if task == False:
         return "Exception- contact developer"
    else:
        return render_template("info.html",data=task)
    
    
@app.route("/edit_task/<id>", methods=["POST"])
def edit_task(id):
    task_name = request.form["task_name"]
    task_description = request.form["task_description"]
    task_deadline = request.form["task_deadline"]
    
    
    if dd.update_task(id,task_name,task_description,task_deadline):
        return render_template("data.html")
    else:
        return "Exception- contact developer"    
    
@app.route("/delete_task/<id>")
def delete_task(id):
    
    if dd.delete_task(id):
        return render_template("data.html")
    else:
        return "Exception- contact developer"
    

    

app.run()
