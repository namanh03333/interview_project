from test_project import create_app,db

app = create_app()

with app.app_context():
    db.create_all()
    print("Thanh Cong")
    
if __name__ == '__main__':
    app.run(debug=True)