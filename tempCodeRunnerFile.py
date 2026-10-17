#A tiny jason web server using only the standard library
import json
from http.server import BaseHTTPRequestHandler,HTTPServer
from urllib.parse import parse_qs, urlparse

class Handler(BaseHTTPRequestHandler):

    def _send_json(self,status:int,payload:dict)->None:
        body=json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type","application/json")
        self.send_header("Content-Length",str(len(body)))
        self.end_headers()
        self.wfile.write(body)



    def do_GET(self)->None:
        parsed=urlparse(self.path)
        if parsed.path=="/hello":
            name=parse_qs(parsed.query).get("name",["world"])[0]


            self._send_json(200,{"message":f"Hello,{name}!"})

        else:
            self._send_json(404,{"error":"Not found"})

    def do_POST(self)->None:
        if urlparse(self.path).path !="/echo":
            self._send_json(404,{"error":"Not found"})
            return

        length=int(self.headers.get("Content-length",0))
        raw=self.rfile.read(length)

        try:
            data=json.loads(raw)
        except json.JSONDecodeError:
            self._send_json(400,{"error":"Body must be valid JSON"})
            return

        self._send_json(200,{"you_sent":data})

if __name__=="__main__":

            server=HTTPServer(("127.0.0.1",8000),Handler)

            print("Serving on http://127.0.0.1:8000 (Ctrl+C to stop)")
            server.serve_forever()




