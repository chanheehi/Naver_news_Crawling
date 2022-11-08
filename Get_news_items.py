import requests
from bs4 import BeautifulSoup
import time

def Get_news_items(url, max_idx):
    for count in range(1, max_idx, 10):    # 몇 페이지까지 크롤링할지 결정
        
        response = requests.get(url+str(count))    # url에 접속해서 html을 가져옴
        html = response.text    # html 소스코드를 문자열로 저장
        soup = BeautifulSoup(html, 'html.parser')   # html.parser를 통해 html을 파싱한다.
        articles = soup.select('div.info_group')    # div 태그 중 class가 info_group인 것을 선택

        title_list, date_list, content_list, url_list = [], [], [], []    # 빈 리스트 생성

        for article in articles:
            links = article.select('a.info')    # a 태그 중 class가 info인 것을 선택
            url = links[1].attrs['href']    # url을 가져옴
            response = requests.get(url, headers={'User-agent' : 'Mozila/5.0'}) #사람인척 하기위한 headers
            html = response.text    # html 소스코드를 문자열로 저장
            soup = BeautifulSoup(html, 'html.parser')   # html.parser를 통해 html을 파싱

            print(count,url)
            if 'entertain' in response.url: # 연예뉴스
                title = soup.select_one(".end_tit").text.replace('"', '').replace("'", "").strip() # 제목, 날짜, 내용 정제해서 대입
                date = soup.select_one('span.author em').text.replace('.', '')[0:8] # 날짜
                content = soup.select_one("#articeBody").text.replace("'", "").replace('"', '').strip() # 위와 동일
                if(len(content) >= 9000): # 내용의 길이가 9000 이상이면 DB에 넣을수 없으므로 넘어가기
                    continue
                time.sleep(0.2)

            elif 'sports' in response.url: # 스포츠뉴스
                title = soup.select_one("h4.title").text.replace('"', '').replace("'", "").strip() # 제목, 날짜, 내용 정제해서 대입
                date = soup.select_one('div.news_headline div.info>span').text.replace('.', '')[5:13]   # 날짜
                content = soup.select_one(".content_area #newsEndContents") # div와 p태그를 제거하기위해 전체를 가져옴
                if(len(content) >= 9000): # 내용의 길이가 9000 이상이면 DB에 넣을수 없으므로 넘어가기
                    continue
        
                divs = content.select('div') # div 태그 제거
                for div in divs:
                    div.decompose() # 위와 동일
                paragraphs = content.select('p') # p 태그 제거
                for p in paragraphs:
                    p.decompose() # 위와 동일

                content = content.text.replace("'", "").replace('"', '').strip() #div와 p태그를 제거했으니 text만 대입
                time.sleep(0.2)

            else: # 일반뉴스
                form = soup.select_one('#ct > div.media_end_head.go_trans') #날것의 데이터 뽑아오기
                form_1 = soup.select_one("#dic_area").text # 위와 동일
            
                title = form.select_one('div.media_end_head_title > h2').text.replace('"', '').replace("'", "").strip() # 제목, 날짜, 내용 정제해서 대입
                date = form.select_one('div.media_end_head_info_datestamp > div > span').text[0:11].replace('.','')
                content = form_1.replace("'", "").replace('"', '').strip() # 위와 동일
                if(len(content) >= 9000):   # 내용의 길이가 9000 이상이면 DB에 넣을수 없으므로 넘어가기
                    continue
            time.sleep(0.2)
            title_list.append(title)    # 기사 제목을 리스트에 추가
            date_list.append(date)  # 기사 날짜를 리스트에 추가
            content_list.append(content)    # 기사 내용을 리스트에 추가
            url_list.append(url)    # 기사 url을 리스트에 추가
        
        return title_list, date_list, content_list, url_list 

