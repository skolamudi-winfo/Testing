from fastapi import FastAPI


app = FastAPI(
    title="Winfo Agents for McKesson",
    version='25.9.1',
    description="An intelligent Winfo AI Agent APIs"
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)