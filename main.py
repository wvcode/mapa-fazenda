from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Configurações de CORS (opcional se frontend e backend estiverem no mesmo domínio)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Substitua por domínio específico se necessário
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir arquivos estáticos (imagens, CSS se quiser externo)
app.mount("/img", StaticFiles(directory="img"), name="img")


# Servir o index.html
@app.get("/", response_class=HTMLResponse)
async def serve_index():
    return FileResponse("index2.html")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
