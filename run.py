try:
    from app import create_app
except ModuleNotFoundError:
    
    from app.app import create_app 


from app.repositories.user_repository import init_db


app = create_app()

if __name__ == "__main__":
    init_db()        
    app.run(debug=True)