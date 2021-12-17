{"changed":true,"filter":false,"title":"app.py","tooltip":"/S3AppFiles-20211026/app.py","value":"import os\n\nfrom flask import Flask, render_template, request, redirect, send_file, url_for\n\nfrom s3_demo import list_files, download_file, upload_file\n\n\napp = Flask(__name__)\nUPLOAD_FOLDER = \"uploads\"\nBUCKET = \"joeysbucket1234\"\n\n\n@app.route('/')\ndef entry_point():\n    #return 'Hello World!'\n    return storage()\n\n\n@app.route(\"/storage\")\ndef storage():\n    contents = list_files(\"joeysbucket1234\")\n    return render_template('storage.html', contents=contents)\n\n\n@app.route(\"/upload\", methods=['POST'])\ndef upload():\n    if request.method == \"POST\":\n        f = request.files['file']\n        f.save(f.filename)\n        upload_file(f\"{f.filename}\", BUCKET)\n\n        return redirect(\"/storage\")\n\n\n@app.route(\"/download/<filename>\", methods=['GET'])\ndef download(filename):\n    if request.method == 'GET':\n        output = download_file(filename, BUCKET)\n\n        return send_file(output, as_attachment=True)\n\n\nif __name__ == '__main__':\n     app.run(host='127.0.0.1', port=8080, debug=True)\n","undoManager":{"mark":-2,"position":1,"stack":[[{"start":{"row":9,"column":0},"end":{"row":9,"column":25},"action":"remove","lines":["BUCKET = \"joeysbucket1234"],"id":2}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":25},"action":"insert","lines":["BUCKET = \"joeysbucket1234"],"id":3}]]},"ace":{"folds":[],"scrolltop":300,"scrollleft":0,"selection":{"start":{"row":39,"column":52},"end":{"row":39,"column":52},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":20,"state":"start","mode":"ace/mode/python"}},"timestamp":1637401138108}