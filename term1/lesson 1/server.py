from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse # 解析 query 字符串 与 url 字符串
import json # json 库

host = 'localhost' # 域名
port = 3636 # 端口号
data = {
  "name": "wang",
  "hobby": [
    {
      "id": 1,
      "text": "abc"
    },
    {
      "id": 2,
      "text": "bca"
    }
  ]
}

# 继承 BaseHTTPRequestHandler 父类
class SimServer(BaseHTTPRequestHandler):

  # 跨域
  def end_headers(self):
    self.send_header('Access-Control-Allow-Origin', 'http://127.0.0.1:5500') # 跨域源
    self.send_header('Access-Control-Allow-Methods', 'GET,POST,PUT,PATCH,DELETE') # 跨域方法
    self.send_header('Access-Control-Allow-Header', 'Content-Type') # 跨域自定义请求头字段
    super().end_headers()
    
  # get 
  def do_GET(self):
    req_url = urlparse(self.path) # 获取请求路径
    query_str = req_url.query # 获取 query 参数字符串

    parsed_query = parse_qs(query_str) # 解析 字符串

    print(parsed_query['a'][0])

    self.send_response(200)
    self.send_header('Content-Type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps(data).encode('utf-8'))

  # post
  def do_POST(self):
    contentLength = int(self.headers['Content-Length'])
    content = self.rfile.read(contentLength)
    print(json.loads(content))

    self.send_response(200)
    self.send_header('Content-Type', 'application/json')
    self.end_headers()

    self.wfile.write(json.dumps({
      "msg": "success"
    }).encode('utf-8'))

# 服务实例
server = HTTPServer((host, port), SimServer)
print('listen on http://localhost:3636')

# 长时连接
server.serve_forever()