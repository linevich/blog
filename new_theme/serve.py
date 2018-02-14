from livereload import Server, shell

server = Server()
server.watch('./*')
server.watch('./build/*')

server.serve(open_url=True)