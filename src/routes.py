from app import app
from flask import render_template, request, flash, redirect

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        year = request.form["year"]
        publisher = request.form["publisher"]
        ISBN_number = request.form["ISBN_number"]

        if len(title) < 1 or len(title) > 25:
            flash("Title must have 1-25 characters")
            return render_template(index.html)
        
        if len(author) < 1 or len(author) > 25:
            flash("Author must have 1-25 characters")
            return render_template(index.html)
        
        if not year.strip():
            flash("Year is required")
            return render_template(index.html)
        
        if not year.isdigit() or int(year) < 0:
            flash("Year must be a positive number")
        
        if len(publisher) < 1 or len(publisher) > 25:
            flash("Publisher must have 1-25 characters")
            return render_template(index.html)
        
        if not ISBN_number.strip():
            flash("ISBN_number is required")
            return render_template(index.html)
        
        if not ISBN_number.isdigit() or len(ISBN_number) < 13:
            flash("ISBN number must be 13 digits")
        
        flash("Book citation added, successfully!", "success")
        return redirect("/")
        
    return render_template(index.html)