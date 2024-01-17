from fastapi import FastAPI, Query, __version__
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
john_doe_profile = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "Anystate",
        "zip_code": "12345"
    },
    "age": 31,
    "occupation": "Software Engineer",
    "interests": ["programming", "hiking", "traveling", "reading"],
    "phone_number": "555-1234"
}

app.mount("/static", StaticFiles(directory="static"), name="static")

html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>FastAPI on Vercel</title>
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon" />
    </head>
    <body>
        <div class="bg-gray-200 p-4 rounded-lg shadow-lg">
            <h1>Hello from FastAPI@{__version__}</h1>
            <ul>
                <li><a href="/docs">/docs</a></li>
                <li><a href="/redoc">/redoc</a></li>
            </ul>
            <p>Powered by <a href="https://vercel.com" target="_blank">Vercel</a></p>
        </div>
    </body>
</html>
"""

@app.get("/")
async def root():
    return HTMLResponse(html)

@app.get('/getProfile')
async def get_profile(email: str = Query(None, regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")):
    # Check if the email matches John Doe's email, otherwise return a generic message
    if email.lower() == john_doe_profile["email"].lower():
        return john_doe_profile
    else:
        return {"message": "No profile found for this email"}

@app.post('/sendEmail')
async def send_email(email: str):
    # Here, you would normally have code to send an email.
    # For demonstration purposes, we're just using a print statement.
    print(f"Email would be sent to {email}")

    # Simulate email sending process
    # ... email sending logic ...

    return {"message": "Email sent successfully", "email": email}