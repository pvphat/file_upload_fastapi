from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse
import os

files_home_path = r"E:\source\learning\file_upload_fastapi\files" # need to change or put to env file

router = APIRouter()

@router.get("/excel_files")
def get_excel_file(filename: str):
    file_path = os.path.join(files_home_path, filename)
    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename=filename)
    else:
        return {"message": "File does not exist."}        

@router.post("/excel_files")
def upload_excel_file(file: UploadFile):
    try:
        file_path = os.path.join(files_home_path, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        return {"message": "Successfully save."}
    except:
        return {"message": "Fail to save."}

@router.delete("/excel_files")
def delete_excel_file(filename: str):
    try:
        file_path = os.path.join(files_home_path, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            return {"message": "Successfully delete."}
        else:
            return {"message": "File does not exist."}
    except:
        return {"message": "Fail to delete"}        

@router.put("/excel_files")
def modify_excel_file(file: UploadFile):
    try:
        file_path = os.path.join(files_home_path, file.filename)
        if os.path.exists(file_path):
            with open(file_path, "wb") as f:
                f.write(file.file.read())
            return {"message": "Successfully update."}
        else:
            return {"message": "File does not exist."}
    except:
        return {"message": "Fail to update."}