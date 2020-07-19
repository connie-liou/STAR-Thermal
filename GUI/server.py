from waitress import serve

from app import server

serve(server, host = '0.0.0.0',port=8050, max_request_header_size=107374182)



