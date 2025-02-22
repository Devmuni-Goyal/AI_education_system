from fastapi.responses import HTMLResponse 

def get_home_data():
    """
    Function to return the homepage HTML content dynamically.
    """
    home_data = """
    <html>
        <head>
            <title>AI-Based Education Platform</title>
        </head>
        <body>
            <h1>Welcome to AI-Based  Education Platform</h1>
        <header> 
            <nav>
                <ul>
                    <li><a href='/ai_learning'>AI Learning</a></li>
                    <li><a href='/resources_hub'>Resources Hub</a></li>
                    <li><a href='/ethics_of_ai'>Ethics of AI</a></li>
                    <li><a href='/about_us'>About Us</a></li>
                    <li><a href='/contact_us'>Contact Us</a></li>
                </ul>
            </nav>
        </header>
        </body>
    </html>
    """
    return HTMLResponse(content=home_data)
