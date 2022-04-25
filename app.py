import imp
from flask import Flask,request,render_template
import PIL
from PIL import Image
import OCR
from OCR import engine
import os


app=Flask(__name__) #name of the application is app

@app.route('/', methods=['POST','GET'])
def upload():
    if request.method=='POST':
        f=request.files['file'] 
        print(f.filename)       
        f.save(f.filename)
        
        pr=engine(f.filename)
        nam=f.filename
        # os.remove(f.filename)        
        return render_template('file_upload.html',name=nam, predicted_value="Successfully converted")        
    return render_template('file_upload.html')


if __name__=="__main__":
    app.run(host="localhost",port=5010,debug=True)