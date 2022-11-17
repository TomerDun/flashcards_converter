from requests_html import HTMLSession
from bs4 import BeautifulSoup
import json

def get_page(url:str = 'https://quizlet.com/692851723/test-flash-cards/', cookie = 'set_num_visits_per_set=4; qi5=1fudu4auugpc2:RwHvyyuQBuT1r6741ooC; fs=qknv7y; qlts=1_ssVt0Wogh5H-riaTE5luRQi3iI9cjVUKlHsvNSwxImKxxAF4mUZpTImjX62A7AWxIJsYsoa.LQrveA; days_since_last_visit=2; akv={}; _gcl_au=1.1.295132937.1668526674; _ga=GA1.2.1277051194.1668526674; _gid=GA1.2.1248863029.1668526674; __qca=P0-655232566-1668526674041; _pbjs_userid_consent_data=3524755945110770; afUserId=0284c403-d4dc-4ae1-9c11-aacd56e16a5d-o; AF_SYNC=1668526675273; __gads=ID=01edea431c558bcf:T=1668526673:S=ALNI_MbXWlTHk_4EGLeqhr4AFYlsYbjwSw; _lr_geo_location=IL; qtkn=CupF5NBYxBf8mZSRHwzp52; app_session_id=242f94a2-7099-445c-b820-1243a03f2e93; __cf_bm=JL83J_O4jO..yqUsQ1_qOO62sEp17p35pDMQTVozgQU-1668587976-0-Af2qgnXA5IvlU3T8Zkgf3I5qar+3TsH6LhuzZZim0R05LBS1BXf7Q0OcaKXFTyfZOkxWZEqhErOjiMTTDjjJavA=; __cfruid=034ce59b9ea724efb5d1ba5120c12bbd5fccb4f6-1668587976; _cfuvid=YpDCFxM4F0iByvUjUVWgzT3fn5iSEXq5VXUv5PXDstA-1668587976500-0-604800000; qmeasure__persistence={"28":"00000100","33":"01000100"}; session_landing_page=StudyFeed/latestActivity; ab.storage.deviceId.6f8c2b67-8bd5-42f6-9c5f-571d9701f693={"g":"bf5b103d-a6ce-9484-2f31-7a6dd4ec58ba","c":1606826481830,"l":1668587979761}; ab.storage.userId.6f8c2b67-8bd5-42f6-9c5f-571d9701f693={"g":"180734155","c":1606826481828,"l":1668587979762}; has_seen_logged_in_home_page_timestamp=1668587979898; __gpi=UID=00000b20b827a14b:T=1668526673:RT=1668587981:S=ALNI_MajVLXH3Vu5yN7WMOnoCFF1CxriOA; study_event_limiter=[]; ab.storage.sessionId.6f8c2b67-8bd5-42f6-9c5f-571d9701f693={"g":"745aca5f-33c9-8558-e5ae-1d44af0646f2","e":1668590069099,"c":1668587979761,"l":1668588269099}; tsp=create_set_page', log=True) -> str:         
    s = HTMLSession()
    r = s.get(url, headers={'Set-Cookie': cookie})
    text = r.text
    if log: print('--got page--')
    return text


def get_words(page, log=True):
    soup = BeautifulSoup(page)
    container = soup.find('div', class_='SetPageTerms-termsList')
    words = container.find_all('span')
    word_list = [word.text for word in words]
    if log: print('--got word list--')
    return word_list

def format_words(words, name, description, log=True):
    output = {
        'name': name,
        'desc': description        
    }
    word_list = []
    word_dict = {'term': '', 'def': ''}
    for i in range(len(words)):
        if i % 2 == 0:
            word_dict['term'] = words[i]
        else:
            word_dict['def'] = words[i]
            word_list.append(word_dict.copy())
    output['cards'] = word_list
    if log: print('--Formatted words--')
    return output

def main():
    name = input('Set name: ')
    desc = input('Set Description: ')
    file_name = input('File name (no extension): ')
    url = input('Page url: ')

    page = get_page(url=url)
    words = get_words(page)
    output = format_words(words, name, desc)
    output_json = json.dumps(output, ensure_ascii=False, indent=4)

    with open(f'output/{file_name}.json', 'w', encoding='utf-16') as f:
        f.write(output_json)

    print('--done--')

if __name__ == '__main__':
    main()