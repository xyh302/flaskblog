from app import create_app

app = create_app()

@app.shell_context_processor
def make_shell_context():
    pass
