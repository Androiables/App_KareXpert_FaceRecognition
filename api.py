from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from pathlib import Path
from face_detect import FaceDetector
from model import ImageData
import base64

app = FastAPI()
detector = FaceDetector()

# If you need to enable CORS (Cross-Origin Resource Sharing), you can configure it like this:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Nothing here"}

upload_dir = "uploads"
Path(upload_dir).mkdir(parents=True, exist_ok=True)

@app.post("/match/")
def match(file: ImageData):

    filename = "uploads/image.jpeg"
    content_type = file.imageData[5:15]

    _, base64_data = file.imageData.split(",", 1)


    if content_type != "image/jpeg":
        return JSONResponse(content={"message": "Format not supported please upload in jpeg image only"}, status_code=500)
    with open(filename, "wb") as f:
        image_binary = base64.b64decode(base64_data)
        f.write(image_binary)

    try:
        Person = detector.matchFace(filename)
        print(Person)
        return JSONResponse(content={"name": f"{Person}"})
    except Exception as e:
        return JSONResponse(content={"message": f"Error processing the image: {str(e)}"}, status_code=500)
    finally:
        image = Path(filename)
        image.unlink()
    
@app.post("/addNewPerson/")
def addNewPerson(file: UploadFile, name: str):
    content_type = file.content_type

    if content_type != "image/jpeg":
        return JSONResponse(content={"message": "Format not supported please upload in jpeg image only"}, status_code=500)
    path = f"uploads/{name}"
    with open(path, "wb") as f:
        f.write(file.file.read())

    print("Adding new person...")
    if not detector.faceExists(path):
        return JSONResponse(content={"message": "This image doesn't contain a face"}, status_code=500)
    detector.trainModel("uploads/")

    return JSONResponse(content={
        "message": "Face Added Successfully"
    }, status_code=100)
