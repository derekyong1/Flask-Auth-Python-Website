from website import create_app

app = create_app()


# Only run web server if we run this specific file
if __name__ == '__main__':
    app.run(debug=True)

