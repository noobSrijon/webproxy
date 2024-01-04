from flask import Flask, request, Response, session, render_template
import requests
from urllib.parse import urljoin, urlparse


def extract_domain(link):
  parsed_url = urlparse(link)
  domain = parsed_url.netloc
  return domain


app = Flask(__name__)
app.config['SECRET_KEY'] = "yssIBKNLensdqc9WNxHpHttg"


@app.before_request
def update_link():
  try:
    session['last_url'] = session['base_url'] + request.path
  except:
    pass


@app.route('/')
def index():
  session.clear()
  return render_template('index.html')


@app.route('/proxy', methods=['POST', 'GET'])
def proxy():
  target_url = request.form.get('target_url') or request.args.get('target_url')
  if 'https://' not in target_url:
    target_url = 'https://' + target_url
  session['base_url'] = target_url

  if request.method == 'GET':
    response = requests.get(target_url)
  elif request.method == 'POST':
    response = requests.post(target_url, data=request.form)
  headers = dict(response.headers)
  headers.pop('Transfer-Encoding', None)
  headers.pop('Content-Encoding', None)

  content = response.content.decode('utf-8')
  content = content.replace(
      'href="/', 'href="/proxys?target_url=' + urljoin(target_url, '/'))
  content = content.replace(
      'src="/', 'src="/proxys?target_url=' + urljoin(target_url, '/'))

  return Response(content, response.status_code, headers)


@app.route('/proxys')
def proxys():
  url_value = request.args.get('target_url')
  url = urljoin(session['base_url'], url_value)

  response = requests.get(url)
  target_url = url

  headers = dict(response.headers)
  headers.pop('Transfer-Encoding', None)
  headers.pop('Content-Encoding', None)

  content = response.content.decode('utf-8')
  content = content.replace(
      'href="/', 'href="/proxys?target_url=' + urljoin(target_url, '/'))
  content = content.replace(
      'src="/', 'src="/proxys?target_url=' + urljoin(target_url, '/'))

  return Response(content, response.status_code, headers)


@app.errorhandler(404)
def page_not_found(e):
  slug = request.path
  redirect_url = '/proxy?target_url=' + urljoin(
      'https://' + extract_domain(session['base_url']), request.path)

  response = requests.get(urljoin(session['base_url'], request.path))

  # Forward the target server's response back to the client
  headers = dict(response.headers)
  headers.pop('Transfer-Encoding', None)
  headers.pop('Content-Encoding', None)

  # Rewrite links in the response content
  content = response.content.decode('utf-8')
  content = content.replace(
      'href="/', 'href="/proxys?target_url=' + urljoin(redirect_url, '/'))
  content = content.replace(
      'src="/', 'src="/proxys?target_url=' + urljoin(redirect_url, '/'))

  # Update the last successful URL
  session['last_url'] = urljoin(
      'https://' + extract_domain(session['last_url']), slug)

  return Response(content, response.status_code, headers)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
