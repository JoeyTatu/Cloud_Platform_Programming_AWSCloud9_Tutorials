{"changed":true,"filter":false,"title":"app.py","tooltip":"/S3AppFiles-20211026/app.py","value":"import os\n\nfrom flask import Flask, render_template, request, redirect, send_file, url_for\n\nfrom s3_demo import list_files, download_file, upload_file\n\n\napp = Flask(__name__)\nUPLOAD_FOLDER = \"uploads\"\nBUCKET = \"joeysbucket1234\"\n\n\n@app.route('/')\ndef entry_point():\n    #return 'Hello World!'\n    return storage()\n\n\n@app.route(\"/storage\")\ndef storage():\n    contents = list_files(\"joeysbucket1234\")\n    return render_template('storage.html', contents=contents)\n\n\n@app.route(\"/upload\", methods=['POST'])\ndef upload():\n    if request.method == \"POST\":\n        f = request.files['file']\n        f.save(f.filename)\n        upload_file(f\"{f.filename}\", BUCKET)\n\n        return redirect(\"/storage\")\n\n\n@app.route(\"/download/<filename>\", methods=['GET'])\ndef download(filename):\n    if request.method == 'GET':\n        output = download_file(filename, BUCKET)\n\n        return send_file(output, as_attachment=True)\n\n\nif __name__ == '__main__':\n     app.run(host='127.0.0.1', port=8080, debug=True)\n","undoManager":{"mark":-2,"position":9,"stack":[[{"start":{"row":9,"column":10},"end":{"row":9,"column":35},"action":"remove","lines":["PUT YOUR BUCKET NAME HERE"],"id":2},{"start":{"row":9,"column":10},"end":{"row":9,"column":25},"action":"insert","lines":["joeysbucket1234"]}],[{"start":{"row":19,"column":27},"end":{"row":19,"column":52},"action":"remove","lines":["PUT YOUR BUCKET NAME HERE"],"id":3},{"start":{"row":19,"column":27},"end":{"row":19,"column":42},"action":"insert","lines":["joeysbucket1234"]}],[{"start":{"row":42,"column":19},"end":{"row":42,"column":26},"action":"remove","lines":["0.0.0.0"],"id":4},{"start":{"row":42,"column":19},"end":{"row":42,"column":20},"action":"insert","lines":["1"]},{"start":{"row":42,"column":20},"end":{"row":42,"column":21},"action":"insert","lines":["2"]},{"start":{"row":42,"column":21},"end":{"row":42,"column":22},"action":"insert","lines":["7"]},{"start":{"row":42,"column":22},"end":{"row":42,"column":23},"action":"insert","lines":["."]},{"start":{"row":42,"column":23},"end":{"row":42,"column":24},"action":"insert","lines":["0"]},{"start":{"row":42,"column":24},"end":{"row":42,"column":25},"action":"insert","lines":["."]},{"start":{"row":42,"column":25},"end":{"row":42,"column":26},"action":"insert","lines":["0"]},{"start":{"row":42,"column":26},"end":{"row":42,"column":27},"action":"insert","lines":["."]}],[{"start":{"row":42,"column":27},"end":{"row":42,"column":28},"action":"insert","lines":["1"],"id":5}],[{"start":{"row":14,"column":11},"end":{"row":14,"column":25},"action":"remove","lines":["'Hello World!'"],"id":6},{"start":{"row":14,"column":11},"end":{"row":14,"column":33},"action":"insert","lines":["@app.route(\"/storage\")"]}],[{"start":{"row":14,"column":11},"end":{"row":14,"column":33},"action":"remove","lines":["@app.route(\"/storage\")"],"id":7},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["s"]},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":14,"column":11},"end":{"row":14,"column":13},"action":"remove","lines":["st"],"id":8},{"start":{"row":14,"column":11},"end":{"row":14,"column":20},"action":"insert","lines":["storage()"]}],[{"start":{"row":13,"column":18},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":25},"action":"insert","lines":["return 'Hello World!'"],"id":12}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["#"],"id":13}]]},"ace":{"folds":[],"scrolltop":379.5,"scrollleft":0,"selection":{"start":{"row":43,"column":5},"end":{"row":43,"column":53},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":26,"state":"start","mode":"ace/mode/python"}},"timestamp":1635280003002}