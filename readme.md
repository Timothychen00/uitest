# 檔案說明
```python
- seleniumver
- robotframeworker
    - Libraries     #python撰寫的庫文件
    - Resources     #按照頁面區分
    - tests         #不要出現xpath
    - screenshots   #test執行完成後自動截圖
    logs.txt        #用於輸出完整的debug訊息
    log.html        #robotframework執行後自動產生
    output.xml      #robotframework執行後自動產生
    report.html     #robotframework執行後自動產生
```

**如果出bug建議直接看logs.txt，裡面可以看到報錯的準確時機點，用於回推錯誤的發生情況**

# 環境建置
## Setup






```bash
robot --pythonpath . --debug logs --loglevel TRACE  tests/SAA006.robot
```


















Exception in thread Http2SingleStreamLayer-1:
Traceback (most recent call last):
  File "/Users/timothychen_1/.pyenv/versions/3.10.0/lib/python3.10/threading.py", line 1009, in _bootstrap_inner
    self.run()
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/seleniumwire/thirdparty/mitmproxy/server/protocol/http2.py", line 719, in run
    layer()
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/seleniumwire/thirdparty/mitmproxy/server/protocol/http.py", line 206, in __call__
    if not self._process_flow(flow):
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/seleniumwire/thirdparty/mitmproxy/server/protocol/http.py", line 452, in _process_flow
    self.send_response(f.response)
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/seleniumwire/thirdparty/mitmproxy/server/protocol/http.py", line 53, in send_response
    self.send_response_headers(response)
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/seleniumwire/thirdparty/mitmproxy/server/protocol/http2.py", line 389, in wrapper
    result = func(self, *args, **kwargs)
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/seleniumwire/thirdparty/mitmproxy/server/protocol/http2.py", line 682, in send_response_headers
    self.connections[self.client_conn].safe_send_headers(
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/seleniumwire/thirdparty/mitmproxy/server/protocol/http2.py", line 53, in safe_send_headers
    self.send_headers(stream_id, headers.fields, **kwargs)
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/h2/connection.py", line 770, in send_headers
    frames = stream.send_headers(
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/h2/stream.py", line 863, in send_headers
    events = self.state_machine.process_input(input_)
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/h2/stream.py", line 129, in process_input
    return func(self, previous_state)
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/h2/stream.py", line 350, in send_on_closed_stream
    raise StreamClosedError(self.stream_id)
h2.exceptions.StreamClosedError: 1
Exception in thread Http2SingleStreamLayer-3:
Traceback (most recent call last):
  File "/Users/timothychen_1/.pyenv/versions/3.10.0/lib/python3.10/threading.py", line 1009, in _bootstrap_inner
    self.run()
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/seleniumwire/thirdparty/mitmproxy/server/protocol/http2.py", line 719, in run
    layer()
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/seleniumwire/thirdparty/mitmproxy/server/protocol/http.py", line 206, in __call__
    if not self._process_flow(flow):
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/seleniumwire/thirdparty/mitmproxy/server/protocol/http.py", line 452, in _process_flow
    self.send_response(f.response)
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/seleniumwire/thirdparty/mitmproxy/server/protocol/http.py", line 53, in send_response
    self.send_response_headers(response)
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/seleniumwire/thirdparty/mitmproxy/server/protocol/http2.py", line 389, in wrapper
    result = func(self, *args, **kwargs)
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/seleniumwire/thirdparty/mitmproxy/server/protocol/http2.py", line 682, in send_response_headers
    self.connections[self.client_conn].safe_send_headers(
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/seleniumwire/thirdparty/mitmproxy/server/protocol/http2.py", line 53, in safe_send_headers
    self.send_headers(stream_id, headers.fields, **kwargs)
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/h2/connection.py", line 770, in send_headers
    frames = stream.send_headers(
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/h2/stream.py", line 863, in send_headers
    events = self.state_machine.process_input(input_)
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/h2/stream.py", line 129, in process_input
    return func(self, previous_state)
  File "/Users/timothychen_1/.local/share/virtualenvs/uitest-EKjzdnMH/lib/python3.10/site-packages/h2/stream.py", line 350, in send_on_closed_stream
    raise StreamClosedError(self.stream_id)
h2.exceptions.StreamClosedError: 3

###




# run the test suite
robot --pythonpath . tests/____robot_test_features.robot.robot

# Virtual Env
- pyenv
- peotry
- 