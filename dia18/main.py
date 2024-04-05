from dia18.get_module import request_get
import templates as t

def build_html(url):
    response = request_get(url)
    text = ''
    for resultados in response:
        
        text += t.html_template.substitute(
            title_es = resultados['name']['spanish'],
            title_en = resultados['name']['english'],
            url = resultados['images']['main'])
        
        return t.html_template.substitute(body = text)
    
if __name__ == '__main__':
    html = build_html('https://aves.ninjas.cl/api/birds')
    with open('aves.html', 'w') as f:
        f.write(html)